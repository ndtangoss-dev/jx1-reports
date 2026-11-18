---
id: XD-O01b
title: Đóng O-01: bảng bằng chứng theo tiêu chí
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-O01b
worktree: D:\JX-wt\XD-O01b
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-O01b.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao"
---

## Mục tiêu và tiêu chí xong
Việc phụ cho **O-01**. Đọc dòng O-01 BACKLOG và `REPORTS/XD-O01.md`; lập bảng từng vế "xong khi": đạt/chưa, bằng chứng; nêu chính xác điều cần để đóng.
Đầu ra: `JX1_OPS/REPORTS/XD-O01b.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế tiêu chí có bằng chứng hoặc ghi rõ thiếu gì.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
