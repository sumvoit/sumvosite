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
