# sumvo.site

Site tài liệu + blog cá nhân chạy [Hugo](https://gohugo.io/) với theme [hugo-book](https://github.com/alex-shpak/hugo-book) (giao diện docs/wiki kiểu BookStack). Chạy trên VPS bằng nginx; mục `/maotrungwork/` và `/edm/` chỉ mở cho email Google được chia sẻ.

## Chạy local

Yêu cầu Hugo extended ≥ 0.158 (đang dùng 0.164.0). Cài trên macOS: `brew install hugo`

```bash
hugo server -D    # xem trước tại http://localhost:1313
hugo --gc --minify    # build production ra thư mục public/
```

## Cấu trúc nội dung

```
content/
├── docs/                  # Tài liệu — hiện thành cây sidebar (sách → chương → trang)
│   ├── huong-dan-su-dung/
│   └── ghi-chu-ky-thuat/
│       └── linux/
└── posts/                 # Blog
```

- Thứ tự sidebar: chỉnh `weight` trong front matter.
- Section gập được: `bookCollapseSection: true` trong `_index.md`.

## Hạ tầng

| Phần | Chỗ |
|---|---|
| Site Hugo | VPS `/var/www/sumvosite/site` |
| Báo cáo `/maotrungwork/`, tài liệu học `/edm/` | VPS `/var/www/sumvosite/private`. Bản gốc ở `static/maotrungwork/`, `static/edm/` trên máy Mac, không nằm trong git |
| workgate: đăng nhập Google, kiểm quyền | `infra/workgate.py`, systemd `workgate`, `127.0.0.1:8090` |
| Cấu hình workgate | VPS `/etc/sumvosite/workgate.env` |
| Danh sách chia sẻ | VPS `/var/lib/workgate/acl.json` |
| vhost nginx, SSL | `infra/setup-sumvosite.sh`, Let's Encrypt tự gia hạn |
| `maotrung.sumvo.site` | Domain phụ, chuyển 301 về `https://sumvo.site` cùng đường dẫn |
| Kết nối deploy | `.deploy.env` trên máy Mac, không commit, mẫu ở `.deploy.env.example` |
| Google OAuth client | Google Cloud project `sumvosite` của sumvo.it@gmail.com, client `workgate` |
| Trang quyền riêng tư (link trên màn hình đăng nhập Google) | `content/privacy.md`, ra `/privacy/` |

DNS tại GoDaddy:

| Loại | Tên | Giá trị |
|---|---|---|
| A | @ | IP VPS |
| CNAME | www | @ |
| A | maotrung | IP VPS |
| MX, TXT, TXT `zmail._domainkey` | | Email Zoho, không sửa |

## Deploy

Push lên `main` không deploy. Deploy bằng lệnh trên máy Mac:

| Việc | Lệnh |
|---|---|
| Báo cáo mới hoặc sửa báo cáo, sửa `/edm/` | `scripts/deploy-vps.sh reports` |
| Site Hugo | `scripts/deploy-vps.sh site` |
| Cả hai | `scripts/deploy-vps.sh` |
| `infra/` đổi | `scripts/deploy-vps.sh infra`, rồi trên server `sudo bash ~/infra/setup-sumvosite.sh` |

Cập nhật cột Trạng thái biên bản weekly từ TASKS.md: `python3 scripts/report-sync.py --deploy`.

## Chia sẻ /maotrungwork/ và /edm/ theo Gmail

Mỗi request vô `/maotrungwork/` hoặc `/edm/` nginx hỏi workgate: chưa đăng nhập thì chuyển qua Google, email chưa được chia sẻ thì báo chưa có quyền. `/maotrungwork/` liệt kê các trang người đang đăng nhập được xem, gồm cả trang trong `/edm/`.

Trang `/edm/` là file `.html` nằm chung thư mục với ảnh, nên chia sẻ theo thư mục: chọn `Toàn bộ /edm/`. Chia sẻ đúng một file `.html` thì người nhận không tải được ảnh `slides/`.

Owner (email trong `OWNER_EMAILS`) xem mọi trang. Chia sẻ:

1. Mở `https://sumvo.site/_auth/share`, hoặc bấm Chia sẻ cạnh trang ở `/maotrungwork/`.
2. Nhập email, chọn trang, `Toàn bộ /maotrungwork/` hoặc `Toàn bộ /edm/`, bấm Chia sẻ.
3. Gửi link hiện ra cho người nhận. Họ đăng nhập Google bằng đúng email đó.

Thu hồi: bấm Thu hồi trong bảng, có hiệu lực ngay request kế tiếp. Gmail bỏ qua dấu chấm và phần `+nhãn`: chia sẻ `a.b@gmail.com` thì người đăng nhập `ab@gmail.com` cũng xem được.

Đổi owner: sửa `OWNER_EMAILS` (cách nhau dấu phẩy) trong `/etc/sumvosite/workgate.env`, chạy `sudo systemctl restart workgate`. Log xem, chặn, chia sẻ: `sudo journalctl -u workgate`.

## Khoá mật khẩu mục Enterprise Architecture

Mục `/enterprise-architecture/` được mã hoá bằng [staticrypt](https://github.com/robinmoisson/staticrypt) lúc deploy, chỉ giải mã ở trình duyệt khi nhập đúng mật khẩu. Đây là hàng rào chặn khách vãng lai và công cụ tìm kiếm, không phải bảo mật cấp doanh nghiệp.

`scripts/deploy-vps.sh` lấy mật khẩu từ biến `EA_PASSWORD` hoặc Keychain. Lưu vô Keychain một lần:

```bash
security add-generic-password -s sumvosite-ea -a sumvo -w
```

Đổi mật khẩu: xoá bằng `security delete-generic-password -s sumvosite-ea`, lưu lại, chạy `scripts/deploy-vps.sh site`.

RSS feed của mục này đã tắt (`outputs: ["html"]` trong `_index.md`) để không lộ nội dung qua `/enterprise-architecture/index.xml`.

## Dựng lại server từ đầu

Cần nền của repo `maotrung-web` (`setup-server.sh`): nginx, certbot, snippet `acme-challenge`, `security-headers`, `static-site`.

1. Google Cloud Console > Google Auth Platform: tạo project. Branding: tên app, email hỗ trợ, home page `https://sumvo.site/`, privacy `https://sumvo.site/privacy/`, Authorized domain `sumvo.site`. Audience: External, bấm Publish app. Clients > Create client > Web application, Authorized redirect URI `https://sumvo.site/_auth/callback`. Client secret chỉ hiện một lần lúc tạo.
2. GoDaddy: A `@` và CNAME `www` như bảng DNS ở trên.
3. Máy Mac: `scripts/deploy-vps.sh infra`.
4. Server: `sudo bash ~/infra/setup-sumvosite.sh`. Domain chưa trỏ về server thì chỉ chạy HTTP; trỏ xong chạy lại để lấy SSL.
5. Server: điền `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `OWNER_EMAILS` trong `/etc/sumvosite/workgate.env`, chạy `sudo systemctl restart workgate`.
6. Máy Mac: `scripts/deploy-vps.sh`.

`setup-sumvosite.sh` không có param thì dựng `sumvo.site` kèm domain phụ `maotrung.sumvo.site`. Domain khác: `sudo bash ~/infra/setup-sumvosite.sh <domain> [domain phụ...]`; domain chính mới cần thêm `https://<domain>/_auth/callback` vô redirect URI và `BASE_URL=https://<domain>/` trong `.deploy.env`.

## Lịch sử

- 2026-10-22: chuyển từ GitHub Pages sang VPS để chia sẻ `/maotrungwork/` theo email Google thay cho mật khẩu chung. Repo `sumvoit/sumvosite` public nên báo cáo được gỡ khỏi git; các commit trước ngày này vẫn chứa báo cáo cũ. Staging `maotrung.sumvo.site` dùng lúc dựng, giữ lại làm domain phụ chuyển 301 về `sumvo.site`.
