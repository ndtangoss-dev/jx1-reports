---
id: XD-H05
title: Kiểm tra liên kết nội bộ DESIGN/REPORTS
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-H05
worktree: D:\JX-wt\XD-H05
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-H05.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Viết và chạy script python -I (chỉ đọc) quét đường dẫn/file:dòng trong `DESIGN` và `REPORTS`, báo tệp nhắc tới mà không tồn tại. Lưu script ở `JX1_OPS/TOOLS/kiem_lien_ket.py`, kết quả trong báo cáo.
Đầu ra: `JX1_OPS/REPORTS/XD-H05.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
