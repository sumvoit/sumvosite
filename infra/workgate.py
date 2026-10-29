#!/usr/bin/env python3
"""workgate: đăng nhập Google và chia sẻ trang theo email cho sumvo.site.

nginx gọi /_auth/check (auth_request) trước mỗi request vô các mục trong PROTECTED_PREFIXES:
200 cho xem, 401 chưa đăng nhập, 403 email chưa được chia sẻ.
Danh sách chia sẻ lưu ở ACL_FILE, sửa tay file này cũng có hiệu lực ngay.
Email trong OWNER_EMAILS xem mọi trang và quản lý chia sẻ tại /_auth/share.

Người chưa có quyền gửi yêu cầu kèm lời nhắn từ trang 403, lưu ở REQUESTS_FILE.
Owner duyệt hoặc từ chối tại /_auth/share. Có SMTP_HOST thì email báo owner khi có yêu cầu
và báo người yêu cầu khi được cấp quyền.

Cấu hình bằng biến môi trường, xem infra/setup-sumvosite.sh. Chỉ dùng thư viện chuẩn Python 3.10.
"""
import base64
import hashlib
import hmac
import html
import json
import os
import posixpath
import re
import secrets
import smtplib
import ssl
import threading
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import formatdate, make_msgid, parseaddr
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def env(name, default=""):
    return os.environ.get(name, default).strip()


PUBLIC_URL = env("PUBLIC_URL", "https://sumvo.site").rstrip("/")
CLIENT_ID = env("GOOGLE_CLIENT_ID")
CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET")
AUTH_URL = env("GOOGLE_AUTH_URL", "https://accounts.google.com/o/oauth2/v2/auth")
TOKEN_URL = env("GOOGLE_TOKEN_URL", "https://oauth2.googleapis.com/token")
SECRET = env("SESSION_SECRET").encode()
ACL_FILE = env("ACL_FILE", "/var/lib/workgate/acl.json")
REQUESTS_FILE = env("REQUESTS_FILE", os.path.join(os.path.dirname(ACL_FILE), "requests.json"))
CONTENT_ROOT = env("CONTENT_ROOT", "/var/www/sumvosite/private")
# Mục cần đăng nhập, cách nhau dấu phẩy. Mục đầu tiên là trang chính liệt kê các trang được chia sẻ.
PREFIXES = ["/" + p.strip().strip("/") + "/"
            for p in env("PROTECTED_PREFIXES", "/maotrungwork/,/edm/").split(",") if p.strip().strip("/")]
PREFIX = PREFIXES[0]
# Tên hiện trên đầu trang của từng mục, mục không có tên dùng SITE_NAME
SITE_NAME = "sumvo.site"
SECTION_NAMES = {"/maotrungwork/": "Mao Trung · Work", "/edm/": "sumvo.site · EDM"}
SESSION_DAYS = int(env("SESSION_DAYS", "7"))
LISTEN = env("LISTEN", "127.0.0.1:8090")
# Email báo yêu cầu quyền. Cổng 465 dùng SSL, cổng khác dùng STARTTLS. Để trống SMTP_HOST thì không gửi.
SMTP_HOST = env("SMTP_HOST")
SMTP_PORT = int(env("SMTP_PORT", "465"))
SMTP_USER = env("SMTP_USER")
SMTP_PASSWORD = env("SMTP_PASSWORD")
MAIL_FROM = env("MAIL_FROM") or SMTP_USER
NOTE_MAX = 500
# Số yêu cầu đang chờ tối đa của một email
PENDING_MAX = 20

SECURE = PUBLIC_URL.startswith("https://")
REDIRECT_URI = PUBLIC_URL + "/_auth/callback"
ISSUERS = ("https://accounts.google.com", "accounts.google.com")
VN = timezone(timedelta(hours=7))
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
REPORT_RE = re.compile(r"/(\d{4})/rp-[a-z]+-(\d{2})-(\d{2})/$")


def norm_email(e):
    """Gmail bỏ qua dấu chấm và phần +nhãn: a.b+x@gmail.com và ab@gmail.com là một tài khoản."""
    e = e.strip().lower()
    local, _, domain = e.partition("@")
    if domain in ("gmail.com", "googlemail.com"):
        local = local.split("+", 1)[0].replace(".", "")
        domain = "gmail.com"
    return f"{local}@{domain}"


# Email hiển thị giữ nguyên như nhập, so sánh bằng norm_email
OWNER_LIST = [e.strip().lower() for e in env("OWNER_EMAILS").split(",") if e.strip()]
OWNERS = {norm_email(e) for e in OWNER_LIST}


def norm_path(p):
    p = urllib.parse.unquote(urllib.parse.urlsplit(p).path or "/")
    trailing = p.endswith("/")
    p = posixpath.normpath("/" + p.lstrip("/"))
    return p + "/" if trailing and p != "/" else p


def share_path(p):
    """Đường dẫn chia sẻ: thư mục kết thúc bằng /, file .../index.html quy về thư mục."""
    p = norm_path(p.strip())
    if p.endswith("/index.html"):
        p = p[: -len("index.html")]
    elif not p.endswith("/") and "." not in posixpath.basename(p):
        p += "/"
    return p if p.startswith(tuple(PREFIXES)) else None


def section(path):
    """Mục chứa path, không thuộc mục nào thì trả mục đầu tiên."""
    path = norm_path(path or "/")
    return next((x for x in PREFIXES if path.startswith(x) or path == x[:-1]), PREFIX)


def section_name(prefix):
    return SECTION_NAMES.get(prefix, SITE_NAME)


def covers(share, path):
    if share.endswith("/"):
        return path.startswith(share) or path == share[:-1]
    return path == share


def now_vn():
    return datetime.now(VN).strftime("%Y-%m-%d %H:%M")


def log(*parts):
    print(*parts, flush=True)


_seen = {}
_seen_lock = threading.Lock()


def log_once(*parts):
    """URL thư mục qua nginx index nên /_auth/check bị gọi 2 lần cho một lượt xem: gộp dòng trùng trong 5 giây."""
    now = time.time()
    with _seen_lock:
        if now - _seen.get(parts, 0) < 5:
            return
        if len(_seen) > 1000:
            _seen.clear()
        _seen[parts] = now
    log(*parts)


# ---- ký cookie ----

def b64e(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def b64d(s):
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def mac(data):
    return b64e(hmac.new(SECRET, data.encode(), hashlib.sha256).digest())


def sign(obj):
    body = b64e(json.dumps(obj, separators=(",", ":")).encode())
    return f"{body}.{mac(body)}"


def unsign(token, kind):
    try:
        body, sig = token.split(".")
        if not hmac.compare_digest(sig, mac(body)):
            return None
        obj = json.loads(b64d(body))
    except (ValueError, TypeError):
        return None
    if obj.get("k") != kind or obj.get("x", 0) < time.time():
        return None
    return obj


# ---- danh sách chia sẻ, yêu cầu quyền ----

class Store:
    """Một list bản ghi trong file JSON {key: [...]}. Đọc lại khi file đổi nên sửa tay có hiệu lực ngay."""

    def __init__(self, path, key):
        self.path = path
        self.key = key
        self.lock = threading.Lock()
        self.mtime = None
        self.items = []

    def _load(self):
        try:
            mtime = os.stat(self.path).st_mtime_ns
        except FileNotFoundError:
            self.items, self.mtime = [], None
            return
        if mtime != self.mtime:
            with open(self.path, encoding="utf-8") as f:
                self.items = json.load(f).get(self.key, [])
            self.mtime = mtime

    def _save(self):
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({self.key: self.items}, f, ensure_ascii=False, indent=1)
            f.write("\n")
        os.replace(tmp, self.path)
        self.mtime = os.stat(self.path).st_mtime_ns

    def all(self):
        with self.lock:
            self._load()
            return list(self.items)

    def add(self, item, same):
        """Thêm item nếu chưa có bản ghi nào same() đúng."""
        with self.lock:
            self._load()
            if any(same(x) for x in self.items):
                return False
            self.items.append(item)
            self._save()
            return True

    def remove(self, pick):
        """Bỏ các bản ghi pick() đúng, trả về các bản ghi đã bỏ."""
        with self.lock:
            self._load()
            gone = [x for x in self.items if pick(x)]
            if gone:
                self.items = [x for x in self.items if not pick(x)]
                self._save()
            return gone


ACL = Store(ACL_FILE, "shares")
REQUESTS = Store(REQUESTS_FILE, "requests")


def match(email, path):
    return lambda x: norm_email(x["email"]) == norm_email(email) and x["path"] == path


def allowed(email, path):
    if email in OWNERS:
        return True
    return any(norm_email(s["email"]) == email and covers(s["path"], path) for s in ACL.all())


def pending():
    """Yêu cầu đang chờ. Yêu cầu đã có quyền bằng đường khác (chia sẻ tay, sửa acl.json) thì bỏ luôn."""
    REQUESTS.remove(lambda r: allowed(norm_email(r["email"]), r["path"]))
    return REQUESTS.all()


def pages():
    """Các trang trong PREFIXES, trừ trang danh sách do gen-report-index sinh.
    Thư mục có index.html là một trang, chia sẻ theo thư mục.
    File .html khác là một trang, chia sẻ theo thư mục chứa nó để kèm ảnh và file đi cùng."""
    out = []
    for prefix in PREFIXES:
        for d, dirs, files in os.walk(os.path.join(CONTENT_ROOT, prefix.strip("/"))):
            dirs.sort()
            share = "/" + os.path.relpath(d, CONTENT_ROOT).replace(os.sep, "/").strip("/") + "/"
            for name in sorted(files):
                if not name.endswith(".html"):
                    continue
                with open(os.path.join(d, name), encoding="utf-8", errors="replace") as f:
                    head = f.read(8192)
                if 'content="gen-report-index"' in head:
                    continue
                path = share if name == "index.html" else share + name
                m = TITLE_RE.search(head)
                title = html.unescape(m.group(1).strip()) if m else path
                r = REPORT_RE.search(path)
                key = r.group(1) + r.group(3) + r.group(2) if r else "0" + path
                out.append({"path": path, "share": share, "title": title, "key": key})
    out.sort(key=lambda p: p["key"], reverse=True)
    return out


def target_page(url):
    """(đường dẫn chia sẻ, tên trang) của url người dùng mở, không có trên đĩa thì None.
    Trang .html lẻ chia sẻ theo thư mục chứa nó như pages()."""
    path = share_path(url)
    if not path:
        return None
    for p in pages():
        if p["path"] == path:
            return p["share"], p["title"]
    disk = os.path.join(CONTENT_ROOT, path.strip("/"))
    if os.path.isfile(disk) or os.path.isfile(os.path.join(disk, "index.html")):
        return path, path
    return None


# ---- email ----

def mail(to, subject, body, reply_to=None):
    """Gửi email ở thread nền, lỗi chỉ ghi log. Không có SMTP_HOST thì bỏ qua."""
    if not SMTP_HOST or not to:
        return
    msg = EmailMessage()
    msg["From"] = MAIL_FROM
    msg["To"] = ", ".join(to)
    msg["Subject"] = " ".join(subject.split())
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=parseaddr(MAIL_FROM)[1].rpartition("@")[2] or None)
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)

    def run():
        try:
            ctx = ssl.create_default_context()
            if SMTP_PORT == 465:
                s = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=20, context=ctx)
            else:
                s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20)
            with s:
                if SMTP_PORT != 465:
                    s.starttls(context=ctx)
                if SMTP_USER:
                    s.login(SMTP_USER, SMTP_PASSWORD)
                s.send_message(msg)
            log("mail", msg["To"], msg["Subject"])
        except Exception as e:
            log("mail-error", msg["To"], type(e).__name__, str(e)[:200])

    threading.Thread(target=run, daemon=True).start()


# ---- Google ----

def exchange(code):
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=10) as r:
        tok = json.load(r)
    # id_token nhận thẳng từ token endpoint qua TLS nên tin được nội dung, chỉ cần kiểm claim
    claims = json.loads(b64d(tok["id_token"].split(".")[1]))
    if claims.get("aud") != CLIENT_ID or claims.get("iss") not in ISSUERS or claims.get("exp", 0) < time.time():
        raise ValueError("id_token sai aud, iss hoặc đã hết hạn")
    return claims


# ---- giao diện ----

CSS = """
:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2430;--mute:#5b6676;--line:#e3e7ed;--acc:#1f5fbf;--bad:#b42318;--ok:#067647}
@media (prefers-color-scheme:dark){:root{--bg:#12161c;--card:#1a2028;--ink:#e6e9ee;--mute:#9aa4b2;--line:#2c3440;--acc:#7fb0ff;--bad:#ff8a80;--ok:#6ce9a6}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:860px;margin:0 auto;padding:32px 16px 64px}
.kicker{color:var(--acc);font-weight:600;font-size:13px;letter-spacing:.04em;text-transform:uppercase}
h1{font-size:26px;line-height:1.3;margin:6px 0 20px}
h2{font-size:18px;margin:32px 0 12px}
a{color:var(--acc)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px}
ul.list{list-style:none;margin:0;padding:0}
ul.list li{display:flex;align-items:center}
ul.list li+li{border-top:1px solid var(--line)}
ul.list a.row{flex:1;display:flex;gap:16px;align-items:baseline;padding:14px 18px;color:inherit;text-decoration:none}
ul.list a.row:hover .t{color:var(--acc)}
ul.list a.sh{padding:0 18px;font-size:13px;white-space:nowrap}
.t{flex:1;font-weight:500}
.d,.mute{color:var(--mute);font-size:13px}
.empty{padding:14px 18px;color:var(--mute)}
.bar{display:flex;gap:12px;flex-wrap:wrap;align-items:center;color:var(--mute);font-size:13px;margin-top:24px}
.btn{display:inline-block;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:9px 16px;font:inherit;font-weight:600;cursor:pointer;text-decoration:none}
.btn.ghost{background:transparent;color:var(--acc);border:1px solid var(--line)}
.btn.small{padding:4px 10px;font-size:13px;font-weight:500}
form.add{display:grid;grid-template-columns:1fr 1.4fr auto;gap:10px;padding:16px}
input,textarea{width:100%;font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px}
textarea{resize:vertical;min-height:84px}
form.req{display:grid;gap:12px;padding:20px}
form.req p{margin:0}
form.req .btn{justify-self:start}
.note{white-space:pre-wrap;word-break:break-word}
.act{white-space:nowrap}
.act form{display:inline}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:10px 14px;border-top:1px solid var(--line);vertical-align:top}
th{border-top:0;color:var(--mute);font-weight:500;font-size:13px}
.msg{padding:12px 16px;border-radius:8px;margin-bottom:16px;border:1px solid var(--line);background:var(--card)}
.msg.ok{border-color:var(--ok)}.msg.bad{border-color:var(--bad);color:var(--bad)}
.msg input{margin-top:8px}
@media (max-width:640px){form.add{grid-template-columns:1fr}ul.list a.row{flex-wrap:wrap;gap:4px 12px}.t{flex-basis:100%}
table,tbody,tr,td{display:block}thead{display:none}td{border-top:0;padding:4px 14px}tr{border-top:1px solid var(--line);padding:8px 0}}
"""

CSP = ("default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; "
       "form-action 'self' https://accounts.google.com; frame-ancestors 'none'")


def esc(s):
    return html.escape(str(s), quote=True)


def layout(title, body, kicker=SITE_NAME):
    return (f'<!doctype html><html lang="vi"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex,nofollow"><title>{esc(title)}</title>'
            f'<style>{CSS}</style></head><body><main><div class="kicker">{esc(kicker)}</div>'
            f'<h1>{esc(title)}</h1>{body}</main></body></html>')


def account_bar(email, extra="", nxt=PREFIX):
    return (f'<div class="bar"><span>Đăng nhập: {esc(email)}</span>{extra}'
            f'<a href="/_auth/login?next={urllib.parse.quote(nxt)}">Đổi tài khoản</a>'
            f'<a href="/_auth/logout">Đăng xuất</a></div>')


def cookie(name, value, path="/", max_age=None):
    parts = [f"{name}={value}", f"Path={path}", "HttpOnly", "SameSite=Lax"]
    if SECURE:
        parts.append("Secure")
    if max_age is not None:
        parts.append(f"Max-Age={max_age}")
    return "; ".join(parts)


def safe_next(n):
    if n and n.startswith("/") and not n.startswith("//") and "\\" not in n:
        return n
    return PREFIX


class Handler(BaseHTTPRequestHandler):
    server_version = "workgate"
    sys_version = ""

    def log_message(self, fmt, *args):
        pass

    # ---- tiện ích ----

    def ip(self):
        return self.headers.get("X-Real-IP") or self.client_address[0]

    def cookies(self):
        c = SimpleCookie()
        try:
            c.load(self.headers.get("Cookie", ""))
        except Exception:
            pass
        return {k: m.value for k, m in c.items()}

    def session(self):
        """(email chuẩn hoá để so quyền, token cookie, email hiển thị)."""
        tok = self.cookies().get("wg", "")
        s = unsign(tok, "s") if tok else None
        return (s["e"], tok, s.get("d", s["e"])) if s else (None, None, None)

    def send(self, code, body="", headers=None, cookies=()):
        data = body.encode() if isinstance(body, str) else body
        self.send_response(code)
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        for c in cookies:
            self.send_header("Set-Cookie", c)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if data and self.command != "HEAD":
            self.wfile.write(data)

    def page(self, code, title, body, cookies=(), kicker=SITE_NAME):
        self.send(code, layout(title, body, kicker), {
            "Content-Type": "text/html; charset=utf-8",
            "Cache-Control": "no-store",
            "Content-Security-Policy": CSP,
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "same-origin",
            "X-Robots-Tag": "noindex, nofollow",
        }, cookies)

    def redirect(self, url, code=302, cookies=()):
        self.send(code, "", {"Location": url, "Cache-Control": "no-store"}, cookies)

    # ---- định tuyến ----

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        q = dict(urllib.parse.parse_qsl(u.query))
        route = {
            "/_auth/check": self.check,
            "/_auth/start": self.start,
            "/_auth/login": self.login,
            "/_auth/callback": self.callback,
            "/_auth/logout": self.logout,
            "/_auth/denied": self.denied,
            "/_auth/home": self.home,
            "/_auth/share": self.share_page,
            "/_auth/": lambda q: self.redirect(PREFIX),
        }.get(u.path)
        if route:
            return route(q)
        self.page(404, "Không có trang này", f'<p><a href="{PREFIX}">Về trang chính</a></p>')

    do_HEAD = do_GET

    def do_POST(self):
        path = urllib.parse.urlsplit(self.path).path
        if path == "/_auth/check":
            return self.check({})
        if path == "/_auth/share":
            return self.share_post()
        if path == "/_auth/request":
            return self.request_post()
        self.send(405)

    def read_form(self, tok):
        """Form POST đã kiểm Origin và CSRF. Sai thì trả 403 và None."""
        origin = self.headers.get("Origin")
        length = min(int(self.headers.get("Content-Length") or 0), 8192)
        form = dict(urllib.parse.parse_qsl(self.rfile.read(length).decode("utf-8", "replace")))
        if (origin and origin != PUBLIC_URL) or not hmac.compare_digest(form.get("csrf", ""), self.csrf(tok)):
            self.send(403)
            return None
        return form

    # ---- nginx auth_request ----

    def check(self, q):
        email, _, who = self.session()
        if not email:
            return self.send(401)
        path = norm_path(self.headers.get("X-Original-URI", "/"))
        if not allowed(email, path):
            log_once("deny", who, path, self.ip())
            return self.send(403)
        if path.endswith("/") or path.endswith(".html"):
            log_once("view", who, path, self.ip())
        self.send(200, "", {"X-Auth-Email": who})

    # ---- đăng nhập ----

    def start(self, q):
        self.to_google(self.headers.get("X-Original-URI", PREFIX))

    def login(self, q):
        self.to_google(q.get("next", PREFIX))

    def to_google(self, nxt):
        if not CLIENT_ID or not CLIENT_SECRET:
            return self.page(503, "Chưa cấu hình đăng nhập Google",
                             "<p>Điền GOOGLE_CLIENT_ID và GOOGLE_CLIENT_SECRET trong file env của workgate.</p>")
        nonce = secrets.token_urlsafe(18)
        st = sign({"k": "st", "n": nonce, "next": safe_next(nxt), "x": time.time() + 600})
        params = urllib.parse.urlencode({
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECT_URI,
            "response_type": "code",
            "scope": "openid email",
            "state": nonce,
            "prompt": "select_account",
        })
        self.redirect(f"{AUTH_URL}?{params}", cookies=[cookie("wg_state", st, "/_auth/", 600)])

    def callback(self, q):
        clear = cookie("wg_state", "", "/_auth/", 0)
        st = unsign(self.cookies().get("wg_state", ""), "st")
        retry = f'<p><a class="btn" href="/_auth/login?next={urllib.parse.quote(PREFIX)}">Đăng nhập lại</a></p>'
        if not st or not hmac.compare_digest(q.get("state", ""), st["n"]):
            return self.page(400, "Phiên đăng nhập hết hạn", retry, [clear])
        if q.get("error") or not q.get("code"):
            return self.page(403, "Chưa đăng nhập", "<p>Đăng nhập Google bị huỷ.</p>" + retry, [clear])
        try:
            claims = exchange(q["code"])
        except Exception as e:
            log("login-error", type(e).__name__, str(e)[:200], self.ip())
            return self.page(502, "Không xác thực được với Google", retry, [clear])
        if not claims.get("email") or claims.get("email_verified") is not True:
            return self.page(403, "Email chưa xác minh", "<p>Tài khoản Google này chưa xác minh email.</p>" + retry, [clear])
        who = claims["email"].strip().lower()
        tok = sign({"k": "s", "e": norm_email(who), "d": who, "x": int(time.time()) + SESSION_DAYS * 86400})
        log("login", who, self.ip())
        self.redirect(st["next"], cookies=[clear, cookie("wg", tok, "/", SESSION_DAYS * 86400)])

    def logout(self, q):
        self.page(200, "Đã đăng xuất",
                  f'<p><a class="btn" href="/_auth/login?next={urllib.parse.quote(PREFIX)}">Đăng nhập lại</a></p>',
                  [cookie("wg", "", "/", 0)])

    # ---- trang ----

    def denied(self, q):
        """Trang 403: gửi yêu cầu quyền cho owner như Google Drive, hoặc chuyển tài khoản."""
        email, tok, who = self.session()
        target = safe_next(self.headers.get("X-Original-URI") or q.get("next"))
        if not email:
            return self.to_google(target)
        sec = section(target)
        kicker = section_name(sec)
        home = f'<a href="{esc(sec)}">Trang được chia sẻ với tôi</a>'
        page = target_page(target)
        # Có quyền mà vẫn tới đây là 403 của nginx (thư mục không có index.html), không phải thiếu quyền
        if allowed(email, norm_path(target)) or not page:
            return self.page(404, "Không có trang này", f"<p>{home}</p>", kicker=kicker)
        switch = (f'<div class="bar"><span>Đăng nhập: {esc(who)}</span>'
                  f'<a href="/_auth/login?next={urllib.parse.quote(target)}">Chuyển tài khoản</a>{home}</div>')
        after = ("Bạn sẽ nhận email khi được cấp quyền, sau đó mở lại link này." if SMTP_HOST
                 else "Khi được cấp quyền, mở lại link này để xem.")
        sent = next((r for r in pending() if match(email, page[0])(r)), None)
        if sent:
            return self.page(403, "Đã gửi yêu cầu",
                             f'<div class="msg ok">Đã gửi yêu cầu quyền xem trang này lúc {esc(sent["at"])}. '
                             f"{after}</div>" + switch, kicker=kicker)
        self.page(403, "Bạn cần quyền truy cập",
                  f'<form class="req card" method="post" action="/_auth/request">'
                  f'<input type="hidden" name="csrf" value="{self.csrf(tok)}">'
                  f'<input type="hidden" name="next" value="{esc(target)}">'
                  f"<p>Yêu cầu quyền truy cập, hoặc chuyển sang tài khoản đã được chia sẻ.</p>"
                  f'<textarea name="note" maxlength="{NOTE_MAX}" placeholder="Lời nhắn (không bắt buộc)"></textarea>'
                  f'<button class="btn" type="submit">Yêu cầu quyền truy cập</button></form>' + switch,
                  kicker=kicker)

    def request_post(self):
        email, tok, who = self.session()
        if not email:
            return self.redirect(PREFIX, 303)
        form = self.read_form(tok)
        if form is None:
            return
        url = safe_next(form.get("next"))
        page = target_page(url)
        if not page or allowed(email, norm_path(url)):
            return self.redirect(url, 303)
        path, title = page
        if sum(norm_email(r["email"]) == email for r in REQUESTS.all()) >= PENDING_MAX:
            return self.page(429, "Đang chờ quá nhiều yêu cầu",
                             f"<p>Email {esc(who)} đã có {PENDING_MAX} yêu cầu chưa được xử lý. "
                             "Chờ owner duyệt rồi gửi tiếp.</p>", kicker=section_name(section(url)))
        note = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", form.get("note", "").replace("\r\n", "\n")).strip()[:NOTE_MAX]
        url = norm_path(url)
        req = {"email": who, "path": path, "url": url, "title": title, "note": note, "at": now_vn()}
        if REQUESTS.add(req, match(email, path)):
            log("request", who, path, self.ip())
            mail(OWNER_LIST, f"{who} xin quyền xem: {title}",
                 f"{who} xin quyền xem trang:\n\n{title}\n{PUBLIC_URL}{url}\n\n"
                 + (f"Lời nhắn:\n{note}\n\n" if note else "")
                 + f"Duyệt hoặc từ chối: {PUBLIC_URL}/_auth/share#yeu-cau\n"
                 f"Trả lời email này là trả lời {who}.\n", reply_to=who)
        self.redirect(url, 303)

    def home(self, q):
        """Trang đầu của một mục: các trang trong mục đó người đang đăng nhập được xem."""
        sec = section(self.headers.get("X-Original-URI") or q.get("s"))
        email, _, who = self.session()
        if not email:
            return self.to_google(sec)
        owner = email in OWNERS
        mine = [p for p in pages() if allowed(email, p["path"])]
        here = [p for p in mine if p["path"].startswith(sec)]
        rows = "".join(
            f'<li><a class="row" href="{esc(p["path"])}"><span class="t">{esc(p["title"])}</span>'
            f'<span class="d">{esc(p["path"][len(sec):])}</span></a>'
            + (f'<a class="sh" href="/_auth/share?{urllib.parse.urlencode({"path": p["share"]})}">Chia sẻ</a>' if owner else "")
            + "</li>" for p in here
        ) or '<li class="empty">Chưa có trang nào được chia sẻ với email này.</li>'
        # Mục khác người này cũng xem được
        extra = "".join(f'<a href="{esc(x)}">{esc(section_name(x))}</a>' for x in PREFIXES
                        if x != sec and any(p["path"].startswith(x) for p in mine))
        if owner:
            n = len(pending())
            extra += (f'<a href="/_auth/share#yeu-cau"><b>{n} yêu cầu quyền</b></a>' if n else "")
            extra += '<a href="/_auth/share">Quản lý chia sẻ</a>'
        log("home", who, sec, len(here), self.ip())
        self.page(200, "Trang được chia sẻ với bạn",
                  f'<div class="card"><ul class="list">{rows}</ul></div>' + account_bar(who, extra, sec),
                  kicker=section_name(sec))

    # ---- quản lý chia sẻ (owner) ----

    def csrf(self, tok):
        return mac("csrf|" + tok)[:32]

    def owner_or_stop(self):
        email, tok, who = self.session()
        if not email:
            self.to_google("/_auth/share")
            return None, None
        if email not in OWNERS:
            self.page(403, "Chỉ chủ trang được quản lý chia sẻ",
                      "<p>" + " ".join(f'<a href="{esc(x)}">{esc(section_name(x))}</a>' for x in PREFIXES) + "</p>")
            return None, None
        return who, tok

    def share_page(self, q):
        email, tok = self.owner_or_stop()
        if not email:
            return
        all_pages = pages()
        titles = {x: "Toàn bộ " + x for x in PREFIXES}
        for p in all_pages:
            titles.setdefault(p["share"], p["title"])

        msg = ""
        m = q.get("m")
        if m == "added":
            link = PUBLIC_URL + (q.get("u") or q.get("p", PREFIX))
            msg = (f'<div class="msg ok">Đã chia sẻ <b>{esc(titles.get(q.get("p"), q.get("p")))}</b> với '
                   f'<b>{esc(q.get("e"))}</b>. '
                   + ("Đã gửi email báo người yêu cầu. Link trang:" if q.get("n") and SMTP_HOST
                      else "Gửi link cho người nhận, họ đăng nhập Google bằng đúng email này:")
                   + f'<input readonly value="{esc(link)}"></div>')
        elif m == "removed":
            msg = f'<div class="msg ok">Đã thu hồi quyền của <b>{esc(q.get("e"))}</b>.</div>'
        elif m == "declined":
            msg = f'<div class="msg ok">Đã từ chối yêu cầu của <b>{esc(q.get("e"))}</b>.</div>'
        elif m == "exists":
            msg = '<div class="msg">Email này đã có quyền với trang đó.</div>'
        elif m == "bad":
            msg = (f'<div class="msg bad">Email hoặc đường dẫn không hợp lệ. Đường dẫn phải bắt đầu bằng '
                   f'{esc(" hoặc ".join(PREFIXES))}.</div>')

        token = self.csrf(tok)

        def act(action, label, ghost, s):
            return (f'<form method="post" action="/_auth/share">'
                    f'<input type="hidden" name="csrf" value="{token}"><input type="hidden" name="action" value="{action}">'
                    f'<input type="hidden" name="email" value="{esc(s["email"])}"><input type="hidden" name="path" value="{esc(s["path"])}">'
                    f'<button class="btn small{" ghost" if ghost else ""}" type="submit">{label}</button></form>')

        reqs = sorted(pending(), key=lambda r: r["at"], reverse=True)
        requests = (
            f'<h2 id="yeu-cau">Yêu cầu quyền truy cập ({len(reqs)})</h2><div class="card"><table>'
            f'<thead><tr><th>Email</th><th>Trang</th><th>Lời nhắn</th><th>Lúc</th><th></th></tr></thead><tbody>'
            + "".join(
                f'<tr><td>{esc(r["email"])}</td>'
                f'<td><a href="{esc(r.get("url", r["path"]))}">{esc(r.get("title") or r["path"])}</a>'
                f'<div class="mute">{esc(r["path"])}</div></td>'
                f'<td class="note">{esc(r.get("note", ""))}</td>'
                f'<td class="mute">{esc(r["at"])}</td>'
                f'<td class="act">{act("add", "Duyệt", False, r)} {act("decline", "Từ chối", True, r)}</td></tr>'
                for r in reqs)
            + "</tbody></table></div>" if reqs else "")

        options = "".join(f'<option value="{esc(k)}">{esc(t)}</option>' for k, t in titles.items())
        form = (f'<form class="add card" method="post" action="/_auth/share">'
                f'<input type="hidden" name="csrf" value="{token}"><input type="hidden" name="action" value="add">'
                f'<input type="email" name="email" placeholder="email@gmail.com" required>'
                f'<input name="path" list="pages" value="{esc(q.get("path") or q.get("p") or PREFIX)}" required>'
                f'<datalist id="pages">{options}</datalist>'
                f'<button class="btn" type="submit">Chia sẻ</button></form>')

        shares = sorted(ACL.all(), key=lambda s: (s["path"], s["email"]))
        rows = "".join(
            f'<tr><td>{esc(s["email"])}</td>'
            f'<td><a href="{esc(s["path"])}">{esc(titles.get(s["path"], s["path"]))}</a></td>'
            f'<td class="mute">{esc(s.get("at", ""))}</td>'
            f'<td>{act("remove", "Thu hồi", True, s)}</td></tr>'
            for s in shares)
        table = (f'<div class="card"><table><thead><tr><th>Email</th><th>Trang</th><th>Lúc</th><th></th></tr></thead>'
                 f'<tbody>{rows}</tbody></table></div>' if shares
                 else '<div class="card"><p class="empty">Chưa chia sẻ cho ai.</p></div>')

        owners = ", ".join(OWNER_LIST)
        self.page(200, "Quản lý chia sẻ",
                  msg + form + requests + f"<h2>Đang chia sẻ</h2>{table}"
                  f'<p class="mute">Owner xem được mọi trang: {esc(owners)}. Đổi owner trong file env của workgate.</p>'
                  + account_bar(email, "".join(f'<a href="{esc(x)}">{esc(section_name(x))}</a>' for x in PREFIXES)))

    def share_post(self):
        email, tok = self.owner_or_stop()
        if not email:
            return
        form = self.read_form(tok)
        if form is None:
            return
        target = form.get("email", "").strip().lower()
        path = share_path(form.get("path", ""))
        if not EMAIL_RE.match(target) or not path:
            return self.redirect("/_auth/share?m=bad", 303)
        if form.get("action") == "remove":
            ACL.remove(match(target, path))
            log("unshare", email, target, path)
            return self.redirect("/_auth/share?" + urllib.parse.urlencode({"m": "removed", "e": target}), 303)
        if form.get("action") == "decline":
            REQUESTS.remove(match(target, path))
            log("decline", email, target, path)
            return self.redirect("/_auth/share?" + urllib.parse.urlencode({"m": "declined", "e": target}), 303)
        added = ACL.add({"email": target, "path": path, "by": email, "at": now_vn()}, match(target, path))
        # Duyệt yêu cầu hay chia sẻ tay đều đáp ứng các yêu cầu đang chờ nằm trong path: báo người yêu cầu
        done = REQUESTS.remove(lambda r: norm_email(r["email"]) == norm_email(target) and covers(path, r["path"]))
        for r in done:
            log("approve", email, r["email"], r["path"])
            mail([r["email"]], f"Đã được cấp quyền xem: {r['title']}",
                 f"{email} đã cấp quyền xem trang cho {r['email']}:\n\n{r['title']}\n{PUBLIC_URL}{r['url']}\n\n"
                 f"Mở link và đăng nhập Google bằng {r['email']}.\n", reply_to=email)
        if not added:
            return self.redirect("/_auth/share?m=exists", 303)
        log("share", email, target, path)
        q = {"m": "added", "e": target, "p": path}
        if done:
            q.update(n="1", u=done[0]["url"])
        self.redirect("/_auth/share?" + urllib.parse.urlencode(q), 303)


def main():
    if len(SECRET) < 32:
        raise SystemExit("SESSION_SECRET thiếu hoặc ngắn hơn 32 ký tự")
    host, port = LISTEN.rsplit(":", 1)
    srv = ThreadingHTTPServer((host, int(port)), Handler)
    srv.daemon_threads = True
    log(f"workgate nghe {LISTEN}, bảo vệ {', '.join(PREFIXES)}, owner: {', '.join(OWNER_LIST) or 'chưa có'}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
