---
id: XD-P03
title: Chuẩn bị P-03: kế hoạch đo đường cong tải theo số Bot
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-P03
worktree: D:\JX-wt\XD-P03
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-P03.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao"
---

## Mục tiêu và tiêu chí xong
Việc chuẩn bị cho **P-03** (đường cong tải theo số Bot, sau E-01). Đọc BACKLOG P-03/E-06, báo cáo E-01*, P-02 (bộ đo một lệnh) và công cụ Bot sẵn có; viết kế hoạch chạy: các mức số Bot, số đo (CPU/RAM/độ trễ tick), lệnh chạy trên Test-36, điều kiện dừng an toàn, mẫu bảng kết quả. Không chạy gì.
Đầu ra: `JX1_OPS/REPORTS/XD-P03.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và đúng phạm vi, mỗi nhận định có bằng chứng hoặc nhãn CHƯA KIỂM.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- PARTIAL: đã hoàn thành báo cáo kế hoạch tĩnh tại JX1_OPS/REPORTS/XD-P03.md.
- Chưa chạy test/build/exe/VM/mạng; nguồn tick/CPU/RAM và launcher nhiều Bot còn CHƯA KIỂM.
- Tệp nhịp D:\JX-wt\XD-P03.nhip bị Access denied; không thay đổi quyền.
