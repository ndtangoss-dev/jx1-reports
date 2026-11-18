---
id: XD-E01
title: Đóng E-01: client Python
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-E01
worktree: D:\JX-wt\XD-E01
depends_on: []
backlog_ref: "đóng việc cha E-01 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-E01.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **E-01** (không vào mẫu số). Đọc `JX1_OPS/TASKS/E-01.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/E-01-thieu-giao-thuc.md và E-01b-thieu-giao-thuc.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì ghi chính xác gói tin đăng nhập còn thiếu (đối chiếu mã Bishop/KSelPlayer có file:dòng). Kết luận cuối bằng một dòng: "E-01 ĐẠT" hoặc "E-01 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-E01.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
