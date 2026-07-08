---
title: Tổ chức nội dung
weight: 2
---

# Tổ chức nội dung

Cấu trúc thư mục ánh xạ trực tiếp thành cây sidebar:

```
content/
├── docs/                    # "Kệ sách"
│   ├── ten-sach/            # Sách (thư mục có _index.md)
│   │   ├── _index.md
│   │   ├── chuong-1/        # Chương (thư mục con)
│   │   │   ├── _index.md
│   │   │   └── trang-1.md   # Trang
│   │   └── trang-le.md
└── posts/                   # Blog
```

Mẹo:

- `weight` trong front matter quyết định thứ tự trong sidebar (nhỏ hơn = lên trên).
- `bookCollapseSection: true` trong `_index.md` làm section gập lại được.
- `bookHidden: true` ẩn trang khỏi sidebar.
