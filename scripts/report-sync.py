#!/usr/bin/env python3
"""report-sync: đưa câu trạng thái mới nhất của task trong TASKS.md vô cột Trạng thái
của bảng "4. Next action" trên biên bản weekly đã đăng (static/maotrungwork/report/<năm>/rp-weekly-dd-mm/index.html).

Mối nối: dòng task ghi `weekly dd/mm việc N`. Script tìm thư mục rp-weekly-dd-mm, hàng STT N,
và nối `<br>dd/mm: câu trạng thái` vô cuối ô Trạng thái nếu câu đó chưa có. Không sửa gì khác.

Cách dùng (chạy trong ~/Projects/sumvosite hoặc bất kỳ đâu):
    python3 scripts/report-sync.py            # sửa file, in thay đổi
    python3 scripts/report-sync.py --dry-run  # chỉ in, không ghi
    python3 scripts/report-sync.py --commit   # sửa rồi git commit (không push)
"""
import argparse
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
REPORT_DIR = os.path.join(SITE, "static", "maotrungwork", "report")
TASKS_CANDIDATES = [
    os.environ.get("MAOTRUNG_TASKS", ""),
    os.path.expanduser("~/Projects/MaoTrung/TASKS.md"),
    os.path.expanduser("~/mnt/MaoTrung/TASKS.md"),
]

TASK_LINE = re.compile(r"^- \[( |x)\] (T\d{3,}) (.*)$")
LINK = re.compile(r"weekly (\d{2})/(\d{2}) việc (\d+)")
STATUS = re.compile(r"(?:Trạng thái(?: họp)? )?(\d{2}/\d{2})(?: \d{2}:\d{2})?: ([^\n]+?)\s*$")
DONE = re.compile(r"^~~\*\*(.+?)\*\*~~ \((\d{4})-(\d{2})-(\d{2})\);?\s*(.*)$")


def find_tasks():
    for p in TASKS_CANDIDATES:
        if p and os.path.isfile(p):
            return p
    sys.exit("Không thấy TASKS.md. Đặt biến MAOTRUNG_TASKS=<đường dẫn>.")


def status_of(done, body):
    """Trả về (dd/mm, câu trạng thái) hoặc None."""
    if done:
        m = DONE.match(body)
        if not m:
            return None
        note = m.group(5).strip().rstrip(".")
        return f"{m.group(4)}/{m.group(3)}", "Xong." + (f" {note}." if note else "")
    # câu trạng thái là mệnh đề cuối cùng có dạng "dd/mm: ..."
    parts = re.split(r"(?<=\.)\s+", body)
    for seg in reversed(parts):
        m = STATUS.search(seg)
        if m:
            text = m.group(2).strip()
            if not text.endswith("."):
                text += "."
            return m.group(1), text[0].upper() + text[1:]
    return None


def read_links(path):
    out = []
    for ln in open(path, encoding="utf-8"):
        m = TASK_LINE.match(ln.rstrip("\n"))
        if not m:
            continue
        done, tid, body = m.group(1) == "x", m.group(2), m.group(3)
        lk = LINK.search(body)
        if not lk:
            continue
        st = status_of(done, body)
        if not st:
            continue
        out.append({"id": tid, "day": lk.group(1), "month": lk.group(2), "stt": lk.group(3),
                    "date": st[0], "text": st[1]})
    return out


def report_file(day, month):
    for year in sorted(os.listdir(REPORT_DIR), reverse=True):
        p = os.path.join(REPORT_DIR, year, f"rp-weekly-{day}-{month}", "index.html")
        if os.path.isfile(p):
            return p
    return None


ROW = re.compile(r'(<tr><td class="c-stt" data-label="STT">(\d+)</td>.*?<td class="" data-label="Trạng thái">)(.*?)(</td></tr>)', re.S)


def sync_file(path, items, dry):
    src = open(path, encoding="utf-8").read()
    sec = src.find("<h2>4. Next action</h2>")
    if sec < 0:
        print(f"  bỏ qua {path}: không có mục 4. Next action")
        return 0
    head, tail = src[:sec], src[sec:]
    by_stt = {it["stt"]: it for it in items}
    changed = []

    def fix(m):
        it = by_stt.get(m.group(2))
        if not it:
            return m.group(0)
        cell = m.group(3)
        line = f"{it['date']}: {html.escape(it['text'], quote=False)}"
        plain = html.unescape(re.sub(r"<[^>]+>", " ", cell))
        # đã có đúng câu, hoặc đã có dòng cùng ngày (biên bản thường ghi dài hơn TASKS.md) thì giữ nguyên
        if it["text"].rstrip(".").lower() in plain.lower():
            return m.group(0)
        # ô đã có dòng ngày mới hơn thì giữ nguyên; dòng cùng ngày thì thay bằng câu mới nhất của TASKS.md
        def key(d):
            dd, mm = d.split("/")
            return mm + dd
        have = re.findall(r"(?:^|<br>)\s*(\d{2}/\d{2}):", cell)
        if any(key(h) > key(it["date"]) for h in have):
            return m.group(0)
        # dòng ghi đúng ngày họp là của biên bản, không đụng; chỉ thay dòng cùng ngày cho các ngày sau họp
        if it["date"] == f"{it['day']}/{it['month']}" and it["date"] in have:
            return m.group(0)
        changed.append((it["id"], it["stt"], line))
        same = re.compile(r"(^|<br>)\s*" + re.escape(it["date"]) + r":[^<]*(?=<br>|$)")
        if same.search(cell):
            new_cell = same.sub(lambda s: s.group(1) + line, cell, count=1)
        else:
            new_cell = (cell.rstrip() + "<br>" + line) if cell.strip() else line
        return m.group(1) + new_cell + m.group(4)

    tail2 = ROW.sub(fix, tail)
    for tid, stt, line in changed:
        print(f"  việc {stt} ({tid}): + {line}")
    if changed and not dry:
        open(path, "w", encoding="utf-8").write(head + tail2)
    return len(changed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args()
    tasks = find_tasks()
    links = read_links(tasks)
    groups = {}
    for it in links:
        groups.setdefault((it["day"], it["month"]), []).append(it)
    total, touched = 0, []
    for (d, mth), items in sorted(groups.items()):
        f = report_file(d, mth)
        if not f:
            print(f"rp-weekly-{d}-{mth}: chưa có trên sumvosite, bỏ qua {len(items)} task")
            continue
        print(f"rp-weekly-{d}-{mth}: {len(items)} task có mối nối")
        n = sync_file(f, items, a.dry_run)
        total += n
        if n:
            touched.append((f, d, mth))
    print(f"{'Sẽ sửa' if a.dry_run else 'Đã sửa'} {total} ô trạng thái.")
    if a.commit and touched and not a.dry_run:
        import datetime
        today = datetime.date.today().strftime("%d/%m")
        names = ", ".join(f"rp-weekly-{d}-{m}" for _, d, m in touched)
        subprocess.run(["git", "-C", SITE, "add"] + [f for f, _, _ in touched], check=True)
        subprocess.run(["git", "-C", SITE, "commit", "-q", "-m", f"Cập nhật trạng thái {names} tới {today}"], check=True)
        sha = subprocess.run(["git", "-C", SITE, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
        print(f"Đã commit {sha}, chưa push.")


if __name__ == "__main__":
    main()
