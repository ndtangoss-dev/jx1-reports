---
id: HG-05b
title: Hiểu game: điều CHƯA KIỂM — phần báo cáo còn lại
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-05b
worktree: D:\JX-wt\HG-05b
depends_on: []
backlog_ref: "#202 duong 70%: nhom Hieu game (BACKLOG, HG-05b)"
vung_file: [JX1_OPS/DESIGN/DANH-SACH-CHUA-KIEM-2.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Tiếp HG-05 (đã rà 82 báo cáo, xem `JX1_OPS/DESIGN/DANH-SACH-CHUA-KIEM.md`): rà các báo cáo trong `JX1_OPS/REPORTS/` mà bảng đó CHƯA phủ, gộp mục CHƯA KIỂM thành bảng cùng định dạng, ghi tổng số báo cáo đã phủ/tổng; nhóm theo loại cần kiểm (client thật, VM, chủ duyệt, đọc mã).
Đầu ra: `JX1_OPS/DESIGN/DANH-SACH-CHUA-KIEM-2.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình, có ít nhất 1 sơ đồ mermaid. Xong khi: tệp tồn tại, trả lời đủ các câu hỏi ở trên (mỗi câu có nhãn), điều chưa biết ghi CHƯA KIỂM, không bịa.

## Nguồn cần đọc
- Báo cáo: `JX1_OPS/DESIGN/DANH-SACH-CHUA-KIEM.md` và thư mục `JX1_OPS/REPORTS/`
- Worktree của bạn KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`. Có thể tra nhanh bằng `D:/JX-tools/graphify-venv/Scripts/graphify.exe query "<câu hỏi>"` chạy trong `D:/JX-build/src18/jxOnline` (đồ thị server 51.690 nút).

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).
