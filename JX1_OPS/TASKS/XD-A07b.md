---
id: XD-A07b
title: Đóng A-07b: rà cắt con trỏ 64→32
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-A07b
worktree: D:\JX-wt\XD-A07b
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-A07b.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao 03:35"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **A-07b**. Đọc `TASKS/A-07b.md` và báo cáo liên quan; đối chiếu từng vế tiêu chí với mã trong `gameserver/Sources` (chỉ đọc, grep chỗ ép con trỏ sang int/DWORD); nêu số chỗ đã rà và số còn lại.
Đầu ra: `JX1_OPS/REPORTS/XD-A07b.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả

- **XD-A07b DONE:** đã đối chiếu từng tiêu chí việc cha; xem [báo cáo XD-A07b](../REPORTS/XD-A07b.md).
- Quét 1.013 tệp, thu 6.744 dòng ứng viên; phân loại đủ 12/12 dòng trong nhóm lời gọi đã chọn, với 7 đường Core dùng lại địa chỉ đã đi qua kiểu hẹp. Chưa đếm được số lỗi còn lại toàn server.
- **A-07b CHƯA ĐẠT:** cây đối chiếu còn chỗ ép hẹp; chưa xác minh revision đã sửa. Kết quả link thành công thuộc snapshot A-07c. Không sửa mã hay chạy build, exe, VM hoặc mạng.
- Bàn giao hai tệp Markdown cho Tổng quan commit; các mốc tiến độ đã báo trong trao đổi vì tệp nhịp nằm ngoài vùng ghi.
