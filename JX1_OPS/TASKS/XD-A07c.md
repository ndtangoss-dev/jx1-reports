---
id: XD-A07c
title: Đóng A-07c: kiểm bằng chứng sửa link ms64.lib
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-A07c
worktree: D:\JX-wt\XD-A07c
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-A07c.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Việc phụ cho **A-07c** (sửa link gs001, `__imp___iob_func`, nhánh A-07b). Đọc `TASKS/A-07c.md`, REPORTS A-07*, log build ở D:/JX-build (chỉ đọc); kết luận đạt/chưa với bằng chứng file:dòng hoặc lệnh kiểm tĩnh (ví dụ dumpbin trên bản có sẵn nếu có sẵn, không chạy exe lạ).
Đầu ra: `JX1_OPS/REPORTS/XD-A07c.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế có bằng chứng hoặc ghi rõ thiếu gì.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
