---
id: XD-W02
title: W-02: vì sao cấp cường hóa Lua không tới client
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-W02
worktree: D:JX-wtXD-W02
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-W02.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao 03:35"
---

## Mục tiêu và tiêu chí xong
Đọc `DESIGN/KE-HOACH-TAI-HIEN-HIEU-UNG.md` mục 4. Chỉ đọc mã: server `ScriptFuns.cpp` quanh dòng 10912 (SetItemEnChance) và đường `s2cSyncItem`; client `KProtocolProcess.cpp` nhận gói đồng bộ item và nơi đọc nEnChance. Trả lời: hàm có đồng bộ nEnChance xuống client không, qua gói nào, field nào; giả thuyết vì sao tooltip không có "+N". Không sửa mã.
Đầu ra: `JX1_OPS/REPORTS/XD-W02.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).
