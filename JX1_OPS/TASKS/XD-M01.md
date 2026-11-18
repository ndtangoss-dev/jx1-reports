---
id: XD-M01
title: Đóng M-01: bảo trì mục lục
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-M01
worktree: D:\JX-wt\XD-M01
depends_on: []
backlog_ref: "đóng việc cha M-01 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-M01.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **M-01** (không vào mẫu số). Đọc `JX1_OPS/TASKS/M-01.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/M-01-kiem-tra-may-that.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì liệt kê việc bảo trì cụ thể còn lại. Kết luận cuối bằng một dòng: "M-01 ĐẠT" hoặc "M-01 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-M01.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả

- [THẤY] DONE — Đã kiểm offline ba hạng mục nhận diện từ tên việc M-01, ghi lệnh và kết quả tại `JX1_OPS/REPORTS/XD-M01.md`.
- [THẤY] M-01 CHƯA ĐẠT vì thiếu tiêu chí đóng, thiếu mục riêng trong mục lục và XD-M01 vẫn vào mẫu số Markdown.
- [CHƯA KIỂM] Chưa chạy build, exe game, VM, mạng hoặc đo lại máy thật. Tệp nhịp ngoài vùng ghi. Tổng quan phụ trách commit.
