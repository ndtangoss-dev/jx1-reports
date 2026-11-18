---
id: XD-E05
title: Đóng E-05: đối chiếu BACKLOG #170
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-E05
worktree: D:\JX-wt\XD-E05
depends_on: []
backlog_ref: "đóng việc cha E-05 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-E05.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **E-05** (không vào mẫu số). Đọc `JX1_OPS/TASKS/E-05.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/E-05a-khung-tester.md và E-05b-kich-ban-full-cycle.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì liệt kê chính xác phần còn thiếu của "xong khi" trong BACKLOG. Kết luận cuối bằng một dòng: "E-05 ĐẠT" hoặc "E-05 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-E05.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
