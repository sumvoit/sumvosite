#!/usr/bin/env bash
# Sinh trang danh sách báo cáo MaoTrung từ thư mục report/<năm>/rp-<loại>-<dd>-<mm>/.
#   report/<năm>/                -> tất cả báo cáo của năm
#   report/<loại>/<năm>/         -> báo cáo theo loại (weekly, monthly, daily) của năm
# Chạy sau khi Hugo build, trước bước staticrypt.
# Cách dùng: scripts/gen-report-index.sh [public/maotrungwork/report]
set -euo pipefail

ROOT="${1:-public/maotrungwork/report}"
[ -d "$ROOT" ] || exit 0

label() {
  case "$1" in
    weekly) echo "Weekly" ;; monthly) echo "Monthly" ;; daily) echo "Daily" ;; *) echo "Tất cả" ;;
  esac
}

# In danh sách "mmdd<TAB>tên<TAB>loại<TAB>dd/mm<TAB>title" của năm, mới nhất trước, lọc theo loại nếu có.
list_reports() {
  local year="$1" type="$2" dir name t d m title
  for dir in "$ROOT/$year"/rp-*/; do
    [ -f "$dir/index.html" ] || continue
    name="$(basename "$dir")"
    [[ "$name" =~ ^rp-(monthly|weekly|daily)-([0-9]{2})-([0-9]{2})$ ]] || continue
    t="${BASH_REMATCH[1]}" d="${BASH_REMATCH[2]}" m="${BASH_REMATCH[3]}"
    [ -z "$type" ] || [ "$type" = "$t" ] || continue
    title="$(sed -n 's:.*<title>\(.*\)</title>.*:\1:p' "$dir/index.html" | head -1)"
    printf '%s%s\t%s\t%s\t%s/%s\t%s\n' "$m" "$d" "$name" "$t" "$d" "$m" "${title:-$name}"
  done | sort -r
}

write_index() {
  local out="$1" year="$2" type="$3" heading rows
  heading="Báo cáo $(label "$type") $year"
  rows="$(list_reports "$year" "$type" | while IFS=$'\t' read -r _ name t date title; do
    printf '<li><a href="/maotrungwork/report/%s/%s/"><span class="d">%s/%s</span><span class="t">%s</span><span class="k">%s</span></a></li>\n' \
      "$year" "$name" "$date" "$year" "$title" "$t"
  done)"
  [ -n "$rows" ] || rows='<li class="empty">Chưa có báo cáo.</li>'
  mkdir -p "$out"
  cat > "$out/index.html" <<HTML
<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<title>$heading</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2430;--mute:#5b6676;--line:#e3e7ed;--acc:#1f5fbf}
@media (prefers-color-scheme:dark){:root{--bg:#12161c;--card:#1a2028;--ink:#e6e9ee;--mute:#9aa4b2;--line:#2c3440;--acc:#7fb0ff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 "Be Vietnam Pro",system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:32px 16px 64px}
.kicker{color:var(--acc);font-weight:600;font-size:13px;letter-spacing:.04em;text-transform:uppercase}
h1{font-size:26px;line-height:1.3;margin:6px 0 20px}
ul{list-style:none;margin:0;padding:0;background:var(--card);border:1px solid var(--line);border-radius:10px}
li+li{border-top:1px solid var(--line)}
a{display:flex;gap:16px;align-items:baseline;padding:14px 18px;color:inherit;text-decoration:none}
a:hover .t{color:var(--acc)}
.d{color:var(--mute);font-variant-numeric:tabular-nums;white-space:nowrap}
.t{flex:1;font-weight:500}
.k{color:var(--mute);font-size:12px;text-transform:uppercase;letter-spacing:.04em}
.empty{padding:14px 18px;color:var(--mute)}
@media (max-width:560px){a{flex-wrap:wrap;gap:4px 12px}.t{flex-basis:100%;order:3}}
</style></head><body><main>
<div class="kicker">Mao Trung · Danh sách báo cáo</div>
<h1>$heading</h1>
<ul>
$rows
</ul>
</main></body></html>
HTML
}

for ydir in "$ROOT"/[0-9][0-9][0-9][0-9]/; do
  [ -d "$ydir" ] || continue
  year="$(basename "$ydir")"
  write_index "$ROOT/$year" "$year" ""
  for type in weekly monthly daily; do
    write_index "$ROOT/$type/$year" "$year" "$type"
  done
done
