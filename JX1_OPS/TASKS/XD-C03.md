---
id: XD-C03
title: Đóng C-03: kiểm tiêu chí jxweb
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-C03
worktree: D:\JX-wt\XD-C03
depends_on: []
backlog_ref: "đóng việc cha C-03 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-C03.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **C-03** (không vào mẫu số). Đọc `JX1_OPS/TASKS/C-03.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/C-03-jxweb.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì vá tối thiểu trong thư mục mã jxweb; xác nhận bind mặc định 127.0.0.1 bằng file:dòng. Kết luận cuối bằng một dòng: "C-03 ĐẠT" hoặc "C-03 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-C03.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
DONE — XD-C03 đã đối chiếu đủ 6 vế tiêu chí; báo cáo: `JX1_OPS/REPORTS/XD-C03.md`.
THẤY — Python `-I -B`: 3/3 ca gốc không socket PASS; kiểm bổ sung logic bind/handler trong RAM đạt; biên dịch 3/3 tệp đạt, 0 mẫu credential phát hiện trong phạm vi quét.
CHƯA KIỂM — 3 ca socket chưa chạy do cấm mạng; C-03 CHƯA ĐẠT đầy đủ; không sửa mã hoặc kết luận cũ, không VM/exe game/mạng.
Bàn giao Tổng quan commit hộ; chưa có SHA/push mới. Ghi `D:\JX-wt\XD-C03.nhip` bị Access denied, không đổi quyền hoặc thử vượt sandbox.
