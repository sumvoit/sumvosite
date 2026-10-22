#!/usr/bin/env bash
# Build sumvo.site và đẩy lên VPS.
#   scripts/deploy-vps.sh            site Hugo + trang cần đăng nhập
#   scripts/deploy-vps.sh site       chỉ site Hugo
#   scripts/deploy-vps.sh reports    chỉ trang cần đăng nhập: báo cáo static/maotrungwork/, tài liệu static/edm/
#   scripts/deploy-vps.sh infra      chép infra/ lên ~/infra/ trên server, sau đó chạy setup-sumvosite.sh trên server
# Kết nối và BASE_URL lấy từ .deploy.env (không commit), mẫu ở .deploy.env.example.
# Mật khẩu mục Enterprise Architecture lấy từ biến EA_PASSWORD hoặc Keychain. Lưu vô Keychain một lần:
#   security add-generic-password -s sumvosite-ea -a sumvo -w
set -euo pipefail

cd "$(dirname "$0")/.."
[ -f .deploy.env ] || { echo "Thiếu .deploy.env: chép từ .deploy.env.example rồi điền"; exit 1; }
. ./.deploy.env
: "${DEPLOY_HOST:?thiếu DEPLOY_HOST}" "${DEPLOY_PORT:?thiếu DEPLOY_PORT}" "${DEPLOY_KEY:?thiếu DEPLOY_KEY}"
BASE_URL=${BASE_URL:-https://sumvo.site/}
SSH="ssh -i $DEPLOY_KEY -p $DEPLOY_PORT"
REMOTE=/var/www/sumvosite
OUT=$(mktemp -d)
trap 'rm -rf "$OUT"' EXIT

# openrsync của macOS không nhận --chmod=D755,F644: chỉnh quyền bản build trước khi đẩy
push() {
    chmod -R u=rwX,go=rX "$1"
    rsync -rlpt --delete --delay-updates -e "$SSH" "$1/" "$DEPLOY_HOST:$2/"
}

site() {
    local pw=${EA_PASSWORD:-$(security find-generic-password -s sumvosite-ea -w 2> /dev/null || true)}
    [ -n "$pw" ] || { echo "Thiếu mật khẩu EA: đặt EA_PASSWORD hoặc lưu Keychain (xem đầu file)"; exit 1; }
    hugo --gc --minify --quiet --baseURL "$BASE_URL" -d "$OUT/public"
    rm -rf "$OUT/public/maotrungwork" "$OUT/public/edm"
    (cd "$OUT" && STATICRYPT_PASSWORD="$pw" npx --yes staticrypt@3.5.4 public/enterprise-architecture \
        -r -d public --short --remember 30 -c false > /dev/null)
    push "$OUT/public" "$REMOTE/site"
    echo "OK: site -> $DEPLOY_HOST:$REMOTE/site"
}

reports() {
    mkdir -p "$OUT/private"
    rsync -a static/maotrungwork static/edm "$OUT/private/"
    bash scripts/gen-report-index.sh "$OUT/private/maotrungwork/report"
    push "$OUT/private" "$REMOTE/private"
    echo "OK: báo cáo, /edm/ -> $DEPLOY_HOST:$REMOTE/private"
}

infra() {
    rsync -rlt -e "$SSH" infra/ "$DEPLOY_HOST:infra/"
    echo "OK: infra/ -> $DEPLOY_HOST:~/infra/. Trên server: sudo bash ~/infra/setup-sumvosite.sh [domain]"
}

case "${1:-all}" in
    site) site ;;
    reports) reports ;;
    infra) infra ;;
    all) site && reports ;;
    *) sed -n '2,9p' "$0"; exit 1 ;;
esac
