---
id: XD-O01
title: Đóng O-01: vận hành định kỳ
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-O01
worktree: D:\JX-wt\XD-O01
depends_on: []
backlog_ref: "đóng việc cha O-01 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-O01.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **O-01** (không vào mẫu số). Đọc `JX1_OPS/TASKS/O-01.md` và BACKLOG dòng O-01; gom bằng chứng các lần chạy định kỳ có trong `JX1_OPS/REPORTS` và `STATE`. Kết luận ĐẠT/CHƯA ĐẠT từng vế.
Đầu ra: `JX1_OPS/REPORTS/XD-O01.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
