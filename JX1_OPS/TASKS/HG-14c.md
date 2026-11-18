---
id: HG-14c
title: (lần 3) Hiểu game: trang bị, độ bền và sửa đồ
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-14c
worktree: D:\JX-wt\HG-14c
depends_on: []
backlog_ref: "#207 dot 3 (BACKLOG, HG-14)"
vung_file: [JX1_OPS/DESIGN/HIEU-DO-BEN-SUA-DO.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "gop 19/11 05:35; dong muc nguon tinh, runtime CHUA KIEM, xem REPORTS/HG-14c.md"
---

## Mục tiêu và tiêu chí xong
Độ bền trang bị giảm khi nào, sửa đồ ở đâu, giá sửa, khi độ bền 0 thì sao; mã KItem/KItemList và script NPC sửa đồ.
Đầu ra: `JX1_OPS/DESIGN/HIEU-DO-BEN-SUA-DO.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình, ít nhất 1 sơ đồ mermaid. Xong khi: tệp tồn tại, đủ 5 dòng tóm tắt, >=10 dẫn file:dòng đúng, có mục "Chưa kiểm".

## Nguồn cần đọc
- Worktree của bạn KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`. Tra nhanh được bằng `D:/JX-tools/graphify-venv/Scripts/graphify.exe query "<câu hỏi>"` chạy trong `D:/JX-build/src18/jxOnline`.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).

## Bổ sung (nguồn Lua/INI đã tìm thấy — LÀM PHẦN NÀY)
Gốc `G` = `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs` (chỉ đọc). Lua sửa đồ: `G/script/tnlteam/npc/addnpc.lua:50–60` và hai Lua phục hồi trang bị; `G/Settings/item/AbradeRate.ini`; `G/Settings/gamesetting.ini:84–86` (nhóm cấm sửa). Đọc, tính ví dụ phí/nguyên liệu, thêm vào tài liệu. Cập nhật `JX1_OPS/DESIGN/HIEU-DO-BEN-SUA-DO.md`: bỏ nhãn PARTIAL nếu đủ bằng chứng, giữ mục "Chưa kiểm" cho phần cần chạy game. Ghi "## Kết quả" mới ở cuối tệp task. Xem `JX1_OPS/REPORTS/XD-HG14.md` (đã gộp) để lấy danh sách dòng.
