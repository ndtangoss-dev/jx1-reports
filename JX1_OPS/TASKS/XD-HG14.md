---
id: XD-HG14
title: Tìm nguồn cho HG-14: script sửa đồ và dữ liệu độ bền
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-HG14
worktree: D:\JX-wt\XD-HG14
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-HG14.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Việc phụ cho **HG-14**/HG-16 (báo cáo PARTIAL do thiếu script NPC). Tìm trong các thư mục có thể đọc (C:/Jx1CocoV3, D:/JX-build, D:/jx1-ops-wt, data_cdn) mọi bản sao script Lua/INI về sửa đồ (`repair`, `Repair`, sửa đồ, độ bền) và tân thủ (`newplayer`, `online.lua`); ghi đường dẫn thật + 3–5 trích dẫn có file:dòng; nếu không có, ghi bằng chứng đã tìm (lệnh + kết quả) và nguồn thay thế.
Đầu ra: `JX1_OPS/REPORTS/XD-HG14.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế có bằng chứng hoặc ghi rõ thiếu gì.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
