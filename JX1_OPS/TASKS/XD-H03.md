---
id: XD-H03
title: Gộp mọi điều CHƯA KIỂM từ báo cáo
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-H03
worktree: D:\JX-wt\XD-H03
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-H03.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Quét `JX1_OPS/REPORTS/*.md` và `DESIGN/*.md`, trích mọi mục "Chưa kiểm" thành một bảng gộp (nguồn, điều chưa kiểm, cách kiểm an toàn, cần VM hay không). Tối thiểu 40 dòng.
Đầu ra: `JX1_OPS/REPORTS/XD-H03.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- Trạng thái: PARTIAL — đã tạo báo cáo XD-H03.md với 311 hàng tiêu đề có nhãn và nguồn file:dòng; cần tiếp tục khai triển phần thân thành từng điều riêng.
- Báo cáo vượt ngưỡng 40 hàng, có nhãn CHƯA KIỂM, cách kiểm an toàn, yêu cầu VM có điều kiện và kết luận cuối CHƯA ĐẠT.
- Không chạy build/exe/VM/mạng; ghi nhịp tới D:\JX-wt\XD-H03.nhip bị từ chối quyền; không commit/push.
