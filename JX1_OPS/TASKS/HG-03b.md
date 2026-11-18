---
id: HG-03b
title: (lần 2) Hiểu game: vì sao cấp cường hóa từ Lua không tới client
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-03b
worktree: D:\JX-wt\HG-03b
depends_on: []
backlog_ref: "#195 hang doi viec, muc [SONNET-THÊM] hiểu game"
vung_file: [JX1_OPS/DESIGN/HIEU-CAP-CUONG-HOA-LUA.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "lam lai: ban dau PARTIAL do worktree thieu source"
---

## Mục tiêu và tiêu chí xong
Đọc `SetItemEnChance` (ScriptFuns.cpp ~10912), đường `s2cSyncItem` và nơi client đọc `nEnChance`; trả lời: hàm đồng bộ trường nào, thiếu bước nào, tooltip "+N" lấy từ đâu. Không sửa mã.
Đầu ra: `JX1_OPS/DESIGN/HIEU-CAP-CUONG-HOA-LUA.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình.

## Nguồn cần đọc
- `gameserver/Sources/Core/Src/ScriptFuns.cpp` (~10912), `KProtocolProcess.cpp` (s2cSyncItem ~1819, 2976, 3098), `JX1_OPS/DESIGN/KE-HOACH-TAI-HIEN-HIEU-UNG.md` mục 4.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).

## Nguồn bổ sung (sửa lỗi lần trước)
Nguồn thật (đọc được, đường dẫn tuyệt đối): server C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\ScriptFuns.cpp (~10912); client C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocolProcess.cpp; server KProtocolProcess.cpp/s2cSyncItem tìm dưới C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources. Worktree của bạn KHÔNG có mã nguồn: hãy đọc trực tiếp các đường dẫn tuyệt đối này (chỉ đọc; ghi chỉ ở tệp đầu ra).
