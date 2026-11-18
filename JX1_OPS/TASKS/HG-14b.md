---
id: HG-14b
title: (lần 2) Hiểu game: trang bị, độ bền và sửa đồ
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-14b
worktree: D:\JX-wt\HG-14b
depends_on: []
backlog_ref: "#207 dot 3 (BACKLOG, HG-14)"
vung_file: [JX1_OPS/DESIGN/HIEU-DO-BEN-SUA-DO.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "lam lai: ban dau PARTIAL thieu source"
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

## Nguồn bổ sung (sửa lỗi lần trước)
Worktree KHÔNG có mã nguồn: đọc trực tiếp (chỉ đọc) client C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes và server C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src (và thư mục Sources cha). Ghi chỉ tệp đầu ra.

## Kết quả
- PARTIAL (19/11/2026): giữ nguyên phần HG-14 đã có; bổ sung đường Lua và cấu hình tại `JX1_OPS/DESIGN/HIEU-DO-BEN-SUA-DO.md`.
- Đã kiểm 3 cầu nối đặt độ bền/đồng bộ và mẫu gamesetting; chưa có Lua/INI rời trong hai root được giao, chưa xác minh NPC/phí đặc biệt/cấu hình thực nạp.
- Báo cáo: `JX1_OPS/REPORTS/HG-14b.md`; không sửa source, không build/test game, exe, VM, mạng; không commit/push, Tổng quan commit.
- Nhịp `D:\JX-wt\HG-14b.nhip` ngoài workspace ghi nên không tạo; không tạo TSV ngoài vùng, đã đặt hàng đề xuất trong báo cáo cho PM.
