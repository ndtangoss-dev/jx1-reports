---
id: XD-CL01
title: Đóng CL-01: đối chiếu C01..C05
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-CL01
worktree: D:\JX-wt\XD-CL01
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-CL01.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **CL-01**. Đọc `TASKS/CL-01.md` và các báo cáo C01..C05; lập bảng từng ca: đạt/chờ chủ/lý do kèm file:dòng. Không chạy client.
Đầu ra: `JX1_OPS/REPORTS/XD-CL01.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
