---
id: XD-B05
title: Chuẩn bị B-05: Tống Kim — mã, công tắc và giới hạn cần chủ đặt
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-B05
worktree: D:\JX-wt\XD-B05
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-B05.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Việc chuẩn bị cho **B-05**. Đọc B-03/D4 và mã/script Tống Kim (Battle/Songjin); nêu công tắc bật, tham số giới hạn (số người, giờ, phần thưởng), chỗ nào cần chủ quyết (liệt kê câu hỏi ngắn 2–3 lựa chọn + khuyến nghị); chỉ đọc.
Đầu ra: `JX1_OPS/REPORTS/XD-B05.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và đúng phạm vi, mỗi nhận định có bằng chứng hoặc nhãn CHƯA KIỂM.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
