# sumvo.site

Site tài liệu + blog cá nhân chạy [Hugo](https://gohugo.io/) với theme [hugo-book](https://github.com/alex-shpak/hugo-book) (giao diện docs/wiki kiểu BookStack).

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

## Deploy — GitHub Pages + domain sumvo.site

1. Tạo repo trên GitHub (vd `sumvo/sumvosite`), push code:

   ```bash
   git remote add origin git@github.com:sumvo/sumvosite.git
   git push -u origin main
   ```

2. Trên GitHub: **Settings → Pages → Source: GitHub Actions**. Workflow `.github/workflows/deploy.yml` sẽ tự build + deploy mỗi lần push lên `main`.

3. **Settings → Pages → Custom domain**: nhập `sumvo.site`, bật **Enforce HTTPS** (file `static/CNAME` đã có sẵn).

4. Cấu hình DNS tại nhà cung cấp domain:

   | Type  | Name | Value |
   |-------|------|-------|
   | A     | @    | 185.199.108.153 |
   | A     | @    | 185.199.109.153 |
   | A     | @    | 185.199.110.153 |
   | A     | @    | 185.199.111.153 |
   | CNAME | www  | `<username>.github.io` |

5. Nếu repo không phải `sumvo/sumvosite`, sửa lại `BookRepo` trong `hugo.toml`.

## Khoá mật khẩu mục Enterprise Architecture

Site 100% tĩnh (GitHub Pages) nên không có login/session thật ở server. Mục `/enterprise-architecture/` được khoá bằng [staticrypt](https://github.com/robinmoisson/staticrypt): sau khi Hugo build xong, các trang HTML trong mục này được mã hoá bằng mật khẩu, chỉ giải mã được ở trình duyệt (client-side) khi nhập đúng mật khẩu. Đây là hàng rào "khách vãng lai/công cụ tìm kiếm không đọc được", không phải bảo mật cấp doanh nghiệp.

**Thiết lập:**

1. Trên GitHub: **Settings → Secrets and variables → Actions → New repository secret**, tạo secret tên `EA_PASSWORD` với giá trị là mật khẩu bạn muốn dùng.
2. Push lên `main` — bước "Password-protect Enterprise Architecture section" trong `deploy.yml` sẽ tự chạy nếu secret tồn tại; nếu không đặt secret, mục này vẫn build công khai như bình thường.
3. Khi vào `sumvo.site/enterprise-architecture/`, nhập mật khẩu và tick **Remember me** để không phải nhập lại ở các trang con khác trong cùng mục (lưu 30 ngày trong localStorage của trình duyệt).

**Test ở local trước khi push:**

```bash
hugo --gc --minify --baseURL "https://sumvo.site/"
STATICRYPT_PASSWORD='mat-khau-thu' npx --yes staticrypt@3.5.4 public/enterprise-architecture -r -d public --short --remember 30 -c false
hugo server -s public   # hoặc: python3 -m http.server -d public 8080
```

Lưu ý: RSS feed của mục này đã bị tắt (`outputs: ["html"]` trong `_index.md`) để tránh lộ nội dung qua `/enterprise-architecture/index.xml`.

## VPS và chia sẻ /maotrungwork/ theo Gmail

Đang dựng song song. sumvo.site vẫn chạy GitHub Pages tới bước Chuyển DNS.

| Phần | Chỗ |
|---|---|
| Site Hugo | VPS `/var/www/sumvosite/site` |
| Báo cáo `/maotrungwork/` | VPS `/var/www/sumvosite/private`, bản gốc ở `static/maotrungwork/` trên máy Mac |
| workgate: đăng nhập Google, kiểm quyền | `infra/workgate.py`, systemd `workgate`, `127.0.0.1:8090` |
| Cấu hình workgate | VPS `/etc/sumvosite/workgate.env` |
| Danh sách chia sẻ | VPS `/var/lib/workgate/acl.json` |
| Kết nối deploy | `.deploy.env` trên máy Mac, không commit |
| Google OAuth client | Google Cloud project `sumvosite` của sumvo.it@gmail.com, client `workgate` |
| Trang quyền riêng tư (link trên màn hình đăng nhập Google) | `content/privacy.md`, ra `/privacy/` |

Mỗi request vô `/maotrungwork/` nginx hỏi workgate: chưa đăng nhập thì chuyển qua Google, email chưa được chia sẻ thì báo chưa có quyền. `/maotrungwork/` liệt kê các trang người đang đăng nhập được xem. Log xem, chặn, chia sẻ: `journalctl -u workgate`.

### Chia sẻ

Owner (email trong `OWNER_EMAILS`) mở `/_auth/share`, nhập email, chọn trang hoặc `/maotrungwork/` cho toàn bộ, bấm Chia sẻ, gửi link cho người nhận. Ở `/maotrungwork/`, owner bấm Chia sẻ cạnh từng trang. Thu hồi có hiệu lực ngay request kế tiếp.

Gmail bỏ qua dấu chấm và phần `+nhãn`: chia sẻ `a.b@gmail.com` thì người đăng nhập `ab@gmail.com` cũng xem được.

### Dựng lần đầu

1. Google Cloud Console > Google Auth Platform: tạo project. Branding: tên app, email hỗ trợ, home page `https://sumvo.site/`, privacy `https://sumvo.site/privacy/`, Authorized domain `sumvo.site`. Audience: External, bấm Publish app. Clients > Create client > Web application, Authorized redirect URIs: `https://sumvo.site/_auth/callback` và `https://maotrung.sumvo.site/_auth/callback`. Client secret chỉ hiện một lần lúc tạo.
2. GoDaddy: thêm A record `maotrung` trỏ IP VPS.
3. Máy Mac: `scripts/deploy-vps.sh infra`.
4. Server: `sudo bash ~/infra/setup-sumvosite.sh maotrung.sumvo.site`.
5. Server: điền `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `OWNER_EMAILS` trong `/etc/sumvosite/workgate.env`, chạy `sudo systemctl restart workgate`.
6. Máy Mac: lưu mật khẩu EA vô Keychain (`security add-generic-password -s sumvosite-ea -a sumvo -w`), đặt `BASE_URL=https://maotrung.sumvo.site/` trong `.deploy.env`, chạy `scripts/deploy-vps.sh`.

### Deploy

| Việc | Lệnh trên máy Mac |
|---|---|
| Báo cáo mới hoặc sửa báo cáo | `scripts/deploy-vps.sh reports` |
| Site Hugo | `scripts/deploy-vps.sh site` |
| Cả hai | `scripts/deploy-vps.sh` |
| `infra/` đổi | `scripts/deploy-vps.sh infra`, rồi chạy lại `setup-sumvosite.sh` trên server |

### Chuyển DNS, tắt bản GitHub Pages

1. GoDaddy: A `@` trỏ IP VPS, xoá 4 A record của GitHub; `www` đổi CNAME thành `sumvo.site`. Giữ nguyên MX, TXT của Zoho.
2. Server: `sudo bash ~/infra/setup-sumvosite.sh` để lấy SSL cho sumvo.site.
3. Máy Mac: đặt `BASE_URL=https://sumvo.site/` trong `.deploy.env`, chạy `scripts/deploy-vps.sh`.
4. Gỡ báo cáo khỏi git: `git rm -r --cached static/maotrungwork`, thêm `static/maotrungwork/` vô `.gitignore`, commit, push.
5. GitHub > Settings > Pages: tắt Pages, xoá workflow `deploy.yml`.

Giữa bước 1 và bước 2, sumvo.site chạy HTTP vài phút. Sau bước 4, `report-sync.py --commit` không còn tác dụng: cập nhật báo cáo bằng `scripts/deploy-vps.sh reports`.
