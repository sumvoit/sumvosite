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
