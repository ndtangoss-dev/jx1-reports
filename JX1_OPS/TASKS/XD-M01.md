---
id: XD-M01
title: Đóng M-01: kiểm các mục bảo trì
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-M01
worktree: D:\JX-wt\XD-M01
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-M01.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao"
---

## Mục tiêu và tiêu chí xong
Việc phụ cho **M-01** (mục lục/bảng/TASKS). Đối chiếu `TASKS/` với `BACKLOG.md`: file thiếu, status mâu thuẫn, mã trùng, README/mục lục thiếu; kết luận danh sách sửa cụ thể (không sửa tệp ngoài đầu ra).
Đầu ra: `JX1_OPS/REPORTS/XD-M01.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế có bằng chứng hoặc ghi rõ thiếu gì.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
