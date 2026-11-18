---
id: HG-16b
title: (lần 2) Hiểu game: sự kiện đăng nhập và khởi tạo nhân vật mới
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-16b
worktree: D:\JX-wt\HG-16b
depends_on: []
backlog_ref: "#207 dot 3 (BACKLOG, HG-16)"
vung_file: [JX1_OPS/DESIGN/HIEU-TAO-NHAN-VAT-MOI.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "lam lai: ban dau PARTIAL thieu source"
---

## Mục tiêu và tiêu chí xong
Tạo nhân vật mới: chọn hệ/giới tính, chỉ số khởi đầu, vật phẩm phát, bản đồ xuất phát, script (online.lua/newplayer); đường client KSelPlayer → Bishop → GS → Goddess.
Đầu ra: `JX1_OPS/DESIGN/HIEU-TAO-NHAN-VAT-MOI.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình, ít nhất 1 sơ đồ mermaid. Xong khi: tệp tồn tại, đủ 5 dòng tóm tắt, >=10 dẫn file:dòng đúng, có mục "Chưa kiểm".

## Nguồn cần đọc
- Worktree của bạn KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`. Tra nhanh được bằng `D:/JX-tools/graphify-venv/Scripts/graphify.exe query "<câu hỏi>"` chạy trong `D:/JX-build/src18/jxOnline`.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).

## Nguồn bổ sung (sửa lỗi lần trước)
Worktree KHÔNG có mã nguồn: đọc trực tiếp (chỉ đọc) client C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes và server C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src (và thư mục Sources cha). Ghi chỉ tệp đầu ra.
