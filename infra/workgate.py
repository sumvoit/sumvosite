#!/usr/bin/env python3
"""workgate: đăng nhập Google và chia sẻ trang theo email cho sumvo.site.

nginx gọi /_auth/check (auth_request) trước mỗi request vô các mục trong PROTECTED_PREFIXES:
200 cho xem, 401 chưa đăng nhập, 403 email chưa được chia sẻ.
Danh sách chia sẻ lưu ở ACL_FILE, sửa tay file này cũng có hiệu lực ngay.
Email trong OWNER_EMAILS xem mọi trang và quản lý chia sẻ tại /_auth/share.

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
import threading
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
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
CONTENT_ROOT = env("CONTENT_ROOT", "/var/www/sumvosite/private")
# Mục cần đăng nhập, cách nhau dấu phẩy. Mục đầu tiên là trang chính liệt kê các trang được chia sẻ.
PREFIXES = ["/" + p.strip().strip("/") + "/"
            for p in env("PROTECTED_PREFIXES", "/maotrungwork/,/edm/").split(",") if p.strip().strip("/")]
PREFIX = PREFIXES[0]
SESSION_DAYS = int(env("SESSION_DAYS", "7"))
LISTEN = env("LISTEN", "127.0.0.1:8090")

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


# ---- danh sách chia sẻ ----

class Acl:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.mtime = None
        self.shares = []

    def _load(self):
        try:
            mtime = os.stat(self.path).st_mtime_ns
        except FileNotFoundError:
            self.shares, self.mtime = [], None
            return
        if mtime != self.mtime:
            with open(self.path, encoding="utf-8") as f:
                self.shares = json.load(f).get("shares", [])
            self.mtime = mtime

    def _save(self):
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"shares": self.shares}, f, ensure_ascii=False, indent=1)
            f.write("\n")
        os.replace(tmp, self.path)
        self.mtime = os.stat(self.path).st_mtime_ns

    def all(self):
        with self.lock:
            self._load()
            return list(self.shares)

    def add(self, email, path, by):
        with self.lock:
            self._load()
            if any(norm_email(s["email"]) == norm_email(email) and s["path"] == path for s in self.shares):
                return False
            self.shares.append({"email": email, "path": path, "by": by, "at": now_vn()})
            self._save()
            return True

    def remove(self, email, path):
        with self.lock:
            self._load()
            keep = [s for s in self.shares
                    if not (norm_email(s["email"]) == norm_email(email) and s["path"] == path)]
            if len(keep) == len(self.shares):
                return False
            self.shares = keep
            self._save()
            return True


ACL = Acl(ACL_FILE)


def allowed(email, path):
    if email in OWNERS:
        return True
    return any(norm_email(s["email"]) == email and covers(s["path"], path) for s in ACL.all())


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
input{width:100%;font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px}
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


def layout(title, body, kicker="Mao Trung · Work"):
    return (f'<!doctype html><html lang="vi"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex,nofollow"><title>{esc(title)}</title>'
            f'<style>{CSS}</style></head><body><main><div class="kicker">{esc(kicker)}</div>'
            f'<h1>{esc(title)}</h1>{body}</main></body></html>')


def account_bar(email, extra=""):
    return (f'<div class="bar"><span>Đăng nhập: {esc(email)}</span>{extra}'
            f'<a href="/_auth/login?next={urllib.parse.quote(PREFIX)}">Đổi tài khoản</a>'
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

    def page(self, code, title, body, cookies=()):
        self.send(code, layout(title, body), {
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
        self.send(405)

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
        email, _, who = self.session()
        target = safe_next(self.headers.get("X-Original-URI") or q.get("next"))
        if not email:
            return self.to_google(target)
        self.page(403, "Chưa được chia sẻ trang này",
                  f"<p>Tài khoản <b>{esc(who)}</b> chưa có quyền xem trang này. "
                  "Nhờ người gửi link chia sẻ cho email của bạn, hoặc đăng nhập bằng tài khoản khác.</p>"
                  f'<p><a class="btn" href="/_auth/login?next={urllib.parse.quote(target)}">Đăng nhập tài khoản khác</a> '
                  f'<a class="btn ghost" href="{PREFIX}">Trang được chia sẻ với tôi</a></p>')

    def home(self, q):
        email, _, who = self.session()
        if not email:
            return self.to_google(PREFIX)
        owner = email in OWNERS
        mine = [p for p in pages() if allowed(email, p["path"])]
        rows = "".join(
            f'<li><a class="row" href="{esc(p["path"])}"><span class="t">{esc(p["title"])}</span>'
            f'<span class="d">{esc(p["path"].strip("/"))}</span></a>'
            + (f'<a class="sh" href="/_auth/share?{urllib.parse.urlencode({"path": p["share"]})}">Chia sẻ</a>' if owner else "")
            + "</li>" for p in mine
        ) or '<li class="empty">Chưa có trang nào được chia sẻ với email này.</li>'
        extra = '<a href="/_auth/share">Quản lý chia sẻ</a>' if owner else ""
        log("home", who, len(mine), self.ip())
        self.page(200, "Trang được chia sẻ với bạn",
                  f'<div class="card"><ul class="list">{rows}</ul></div>' + account_bar(who, extra))

    # ---- quản lý chia sẻ (owner) ----

    def csrf(self, tok):
        return mac("csrf|" + tok)[:32]

    def owner_or_stop(self):
        email, tok, who = self.session()
        if not email:
            self.to_google("/_auth/share")
            return None, None
        if email not in OWNERS:
            self.page(403, "Chỉ chủ trang được quản lý chia sẻ", f'<p><a href="{PREFIX}">Về trang chính</a></p>')
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
            link = PUBLIC_URL + q.get("p", PREFIX)
            msg = (f'<div class="msg ok">Đã chia sẻ <b>{esc(titles.get(q.get("p"), q.get("p")))}</b> với '
                   f'<b>{esc(q.get("e"))}</b>. Gửi link cho người nhận, họ đăng nhập Google bằng đúng email này:'
                   f'<input readonly value="{esc(link)}"></div>')
        elif m == "removed":
            msg = f'<div class="msg ok">Đã thu hồi quyền của <b>{esc(q.get("e"))}</b>.</div>'
        elif m == "exists":
            msg = '<div class="msg">Email này đã có quyền với trang đó.</div>'
        elif m == "bad":
            msg = (f'<div class="msg bad">Email hoặc đường dẫn không hợp lệ. Đường dẫn phải bắt đầu bằng '
                   f'{esc(" hoặc ".join(PREFIXES))}.</div>')

        token = self.csrf(tok)
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
            f'<td><form method="post" action="/_auth/share">'
            f'<input type="hidden" name="csrf" value="{token}"><input type="hidden" name="action" value="remove">'
            f'<input type="hidden" name="email" value="{esc(s["email"])}"><input type="hidden" name="path" value="{esc(s["path"])}">'
            f'<button class="btn ghost small" type="submit">Thu hồi</button></form></td></tr>'
            for s in shares)
        table = (f'<div class="card"><table><thead><tr><th>Email</th><th>Trang</th><th>Lúc</th><th></th></tr></thead>'
                 f'<tbody>{rows}</tbody></table></div>' if shares
                 else '<div class="card"><p class="empty">Chưa chia sẻ cho ai.</p></div>')

        owners = ", ".join(OWNER_LIST)
        self.page(200, "Quản lý chia sẻ",
                  msg + form + f"<h2>Đang chia sẻ</h2>{table}"
                  f'<p class="mute">Owner xem được mọi trang: {esc(owners)}. Đổi owner trong file env của workgate.</p>'
                  + account_bar(email, f'<a href="{PREFIX}">Trang chính</a>'))

    def share_post(self):
        email, tok = self.owner_or_stop()
        if not email:
            return
        origin = self.headers.get("Origin")
        if origin and origin != PUBLIC_URL:
            return self.send(403)
        length = min(int(self.headers.get("Content-Length") or 0), 8192)
        form = dict(urllib.parse.parse_qsl(self.rfile.read(length).decode("utf-8", "replace")))
        if not hmac.compare_digest(form.get("csrf", ""), self.csrf(tok)):
            return self.send(403)
        target = form.get("email", "").strip().lower()
        path = share_path(form.get("path", ""))
        if not EMAIL_RE.match(target) or not path:
            return self.redirect("/_auth/share?m=bad", 303)
        if form.get("action") == "remove":
            ACL.remove(target, path)
            log("unshare", email, target, path)
            return self.redirect("/_auth/share?" + urllib.parse.urlencode({"m": "removed", "e": target}), 303)
        if not ACL.add(target, path, email):
            return self.redirect("/_auth/share?m=exists", 303)
        log("share", email, target, path)
        self.redirect("/_auth/share?" + urllib.parse.urlencode({"m": "added", "e": target, "p": path}), 303)


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
