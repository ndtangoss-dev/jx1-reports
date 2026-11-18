---
id: XD-P02
title: Đóng P-02: bộ đo chuẩn
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-P02
worktree: D:\JX-wt\XD-P02
depends_on: []
backlog_ref: "đóng việc cha P-02 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-P02.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **P-02** (không vào mẫu số). Đọc `JX1_OPS/TASKS/P-02.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/P-02-bench.md và KIEM-P-02.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì chạy lệnh jxbench với dữ liệu mẫu, vá nếu lỗi. Kết luận cuối bằng một dòng: "P-02 ĐẠT" hoặc "P-02 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-P02.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
