#!/usr/bin/env bash
# Dựng sumvo.site trên VPS: vhost nginx, SSL Let's Encrypt, workgate (đăng nhập Google cho /maotrungwork/ và /edm/).
# Cần nền của maotrung-web (setup-server.sh): nginx, certbot, snippet acme-challenge, security-headers, static-site.
#   Máy Mac:  scripts/deploy-vps.sh infra
#   Server:   sudo bash ~/infra/setup-sumvosite.sh [domain] [domain phụ...]
# Không có param: domain sumvo.site, domain phụ maotrung.sumvo.site.
# Domain phụ có SSL riêng và chuyển 301 về https://<domain> cùng đường dẫn.
# Vhost chỉ phục vụ domain của lần chạy gần nhất, PUBLIC_URL trong file env đổi theo.
# Chạy lại được: SESSION_SECRET, Google client, owner và danh sách chia sẻ giữ nguyên. Chạy lại mỗi khi infra/ đổi.
# Domain chưa trỏ về server thì chỉ chạy HTTP; trỏ xong chạy lại để lấy SSL.
set -euo pipefail

HERE=$(cd "$(dirname "$0")" && pwd)
[ $# -gt 0 ] || set -- sumvo.site maotrung.sumvo.site
DOMAIN=$1
ALIASES=("${@:2}")
SITE_ROOT=/var/www/sumvosite
DEPLOY_USER=${DEPLOY_USER:-${SUDO_USER:?chạy bằng sudo từ user deploy: sudo bash ~/infra/setup-sumvosite.sh}}
VHOST=/etc/nginx/sites-available/sumvosite
CERT_DIR=/etc/letsencrypt/live/$DOMAIN
ENV_FILE=/etc/sumvosite/workgate.env

for d in "$DOMAIN" "${ALIASES[@]}"; do
    [[ "$d" =~ ^[a-z0-9.-]+$ ]] || { echo "domain chỉ gồm a-z, 0-9, ., -: $d"; exit 1; }
done
for s in acme-challenge security-headers static-site; do
    [ -f "/etc/nginx/snippets/$s.conf" ] || { echo "Thiếu /etc/nginx/snippets/$s.conf, chạy setup-server.sh của maotrung-web trước"; exit 1; }
done

# Thư mục web: deploy-vps.sh rsync vô bằng DEPLOY_USER
install -d -m 0755 "$SITE_ROOT"
install -d -m 0755 -o "$DEPLOY_USER" -g "$DEPLOY_USER" "$SITE_ROOT/site" "$SITE_ROOT/private"

# workgate: user riêng, không shell
id workgate > /dev/null 2>&1 || useradd --system --no-create-home --shell /usr/sbin/nologin workgate
install -d -m 0755 /usr/local/lib/workgate
install -m 0644 "$HERE/workgate.py" /usr/local/lib/workgate/workgate.py
install -d -m 0700 /etc/sumvosite
if [ ! -f "$ENV_FILE" ]; then
    (
        umask 077
        {
            echo "PUBLIC_URL=https://$DOMAIN"
            echo "GOOGLE_CLIENT_ID="
            echo "GOOGLE_CLIENT_SECRET="
            echo "OWNER_EMAILS="
            echo "SESSION_SECRET=$(openssl rand -hex 32)"
            echo "SESSION_DAYS=7"
            echo "CONTENT_ROOT=$SITE_ROOT/private"
            echo "ACL_FILE=/var/lib/workgate/acl.json"
        } > "$ENV_FILE"
    )
fi
# Email báo yêu cầu quyền: thêm khoá còn thiếu vô file env cũ, giá trị điền tay
for kv in SMTP_HOST= SMTP_PORT=465 SMTP_USER= SMTP_PASSWORD= MAIL_FROM=; do
    grep -q "^${kv%%=*}=" "$ENV_FILE" || echo "$kv" >> "$ENV_FILE"
done
sed -i "s|^PUBLIC_URL=.*|PUBLIC_URL=https://$DOMAIN|" "$ENV_FILE"
chmod 600 "$ENV_FILE"
install -m 0644 "$HERE/workgate.service" /etc/systemd/system/workgate.service
systemctl daemon-reload
systemctl enable workgate > /dev/null 2>&1
systemctl restart workgate

install -m 0644 "$HERE/nginx-sumvosite.conf" /etc/nginx/snippets/sumvosite.conf

ZONE='limit_req_zone $binary_remote_addr zone=sumvosite_auth:10m rate=30r/m;'
SSL="    ssl_certificate $CERT_DIR/fullchain.pem;
    ssl_certificate_key $CERT_DIR/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;"

cert_has() {
    [ -f "$CERT_DIR/cert.pem" ] && openssl x509 -in "$CERT_DIR/cert.pem" -noout -text | grep -q "DNS:$1\b"
}

write_http() {
    cat > "$VHOST" << NGINX
$ZONE

server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN;
    include snippets/acme-challenge.conf;
    include snippets/security-headers.conf;
    include snippets/sumvosite.conf;
}
NGINX
}

# Domain phụ đã có SSL: chuyển 301 về domain chính
alias_blocks() {
    local a
    for a in "${ALIASES[@]}"; do
        [ -f "/etc/letsencrypt/live/$a/fullchain.pem" ] || continue
        cat << NGINX

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name $a;
    ssl_certificate /etc/letsencrypt/live/$a/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$a/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    return 301 https://$DOMAIN\$request_uri;
}
NGINX
    done
}

write_https() {
    local www=""
    if cert_has "www.$DOMAIN"; then
        www="
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name www.$DOMAIN;
$SSL
    return 301 https://$DOMAIN\$request_uri;
}"
    fi
    cat > "$VHOST" << NGINX
$ZONE

server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN ${ALIASES[*]};
    include snippets/acme-challenge.conf;
    location / {
        return 301 https://$DOMAIN\$request_uri;
    }
}
$www
$(alias_blocks)
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name $DOMAIN;
$SSL

    add_header Strict-Transport-Security "max-age=31536000" always;
    include snippets/security-headers.conf;
    include snippets/sumvosite.conf;
}
NGINX
}

reload() {
    ln -sfn "$VHOST" /etc/nginx/sites-enabled/sumvosite
    nginx -t
    systemctl reload nginx
}

# Domain trỏ về server này: đặt file thử vô thư mục challenge rồi gọi qua domain
points_here() {
    local t got
    t=$(openssl rand -hex 16)
    install -d -m 0755 /var/www/letsencrypt/.well-known/acme-challenge
    echo "$t" > "/var/www/letsencrypt/.well-known/acme-challenge/$t"
    # Resolve qua DNS public (DoH) như Let's Encrypt: DNS nội bộ GreenNode giữ cache "không có" tới 10 phút
    got=$(curl -fsS --max-time 5 --doh-url https://1.1.1.1/dns-query \
        "http://$1/.well-known/acme-challenge/$t" 2> /dev/null || true)
    rm -f "/var/www/letsencrypt/.well-known/acme-challenge/$t"
    [ "$got" = "$t" ]
}

if [ -f "$CERT_DIR/fullchain.pem" ]; then write_https; else write_http; fi
reload

if ! points_here "$DOMAIN"; then
    echo "CHUA SSL: $DOMAIN chua tro ve server nay. Doi A record roi chay lai."
    exit 0
fi

DOMAINS=(-d "$DOMAIN")
points_here "www.$DOMAIN" && DOMAINS+=(-d "www.$DOMAIN")
if ! cert_has "$DOMAIN" || { [ ${#DOMAINS[@]} -gt 2 ] && ! cert_has "www.$DOMAIN"; }; then
    # Dùng tài khoản Let's Encrypt sẵn có trên server (đã đăng ký khi cài xaynhalandau, cqa)
    certbot certonly --webroot -w /var/www/letsencrypt --cert-name "$DOMAIN" "${DOMAINS[@]}" \
        --expand --agree-tos --non-interactive --deploy-hook "systemctl reload nginx"
fi

for a in "${ALIASES[@]}"; do
    [ -f "/etc/letsencrypt/live/$a/fullchain.pem" ] && continue
    if points_here "$a"; then
        certbot certonly --webroot -w /var/www/letsencrypt --cert-name "$a" -d "$a" \
            --agree-tos --non-interactive --deploy-hook "systemctl reload nginx"
    else
        echo "BO QUA $a: chua tro ve server nay"
    fi
done

write_https
reload
echo "OK: https://$DOMAIN"
grep -q '^GOOGLE_CLIENT_ID=.\+' "$ENV_FILE" || echo "Chua dien GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, OWNER_EMAILS trong $ENV_FILE"
