---
id: XD-E06
title: Chuẩn bị E-06: kế hoạch đo tải và tiêu chí chuyển Bot vào server
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-E06
worktree: D:\JX-wt\XD-E06
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-E06.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Việc chuẩn bị cho **E-06**. Đọc thiết kế Bot trong `DESIGN/BOT/` và báo cáo E-*; liệt kê phương án (Bot ngoài vs trong server), tiêu chí quyết định đo được, số cần đo; chỉ kế hoạch, không chạy.
Đầu ra: `JX1_OPS/REPORTS/XD-E06.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và đúng phạm vi, mỗi nhận định có bằng chứng hoặc nhãn CHƯA KIỂM.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
