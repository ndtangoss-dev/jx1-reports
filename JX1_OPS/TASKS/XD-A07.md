---
id: XD-A07
title: Đóng A-07: đối chiếu tiêu chí
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-A07
worktree: D:\JX-wt\XD-A07
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-A07.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao 03:35"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **A-07**. Đọc `JX1_OPS/TASKS/A-07.md`, dòng A-07 trong BACKLOG và các báo cáo A-07*. Với từng vế tiêu chí ghi bằng chứng file:dòng; vế chưa đạt (ví dụ bước 3 VBoxSVC) liệt kê phần thiếu và cách làm an toàn, không làm thật.
Đầu ra: `JX1_OPS/REPORTS/XD-A07.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- DONE phần XD-A07: đã tạo JX1_OPS/REPORTS/XD-A07.md, đối chiếu 9/9 nguồn và 15/15 vế; A-07 CHƯA ĐẠT điều kiện đóng.
- Thiếu bằng chứng dòng crash/dump/PDB đúng bộ, xác nhận VBoxSVC/VM và bước 3–6; cách tiếp tục an toàn đã ghi, không làm thật.
- Chỉ đọc tài liệu, kiểm tra tồn tại 4/4 tệp công cụ; không sửa nguồn/kết luận cũ, không build/exe/VM/mạng, không commit/push.
- Ghi D:\JX-wt\XD-A07.nhip bị Access denied do ngoài vùng ghi; không vượt quyền. Tổng quan nhận bàn giao phần commit.
