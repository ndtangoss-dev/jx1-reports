---
id: HG-S1
title: Hiểu game: vòng tick gs001, lỗi online.lua mỗi phút và giật ngựa (sổ tay còn thiếu)
status: running
level: L3
agent: codex
effort: high
owner: A
priority: 1
branch: task/HG-S1
worktree: D:\JX-wt\HG-S1
depends_on: []
backlog_ref: "#347 (Chat 16:40), STATE/HANG-DOI-VIEC.md mục S-1"
vung_file: [JX1_OPS/HIEU-GAME/07-server-luu-tru/SO-TAY-TICK-GS001.md, JX1_OPS/REPORTS/HG-S1.md]
tai_nguyen: []
updated: 2026-11-21
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Viết sổ tay `HIEU-GAME/07-server-luu-tru/SO-TAY-TICK-GS001.md` (đọc tĩnh): (1) vòng Activate/tick chính của gs001 (KSubWorld/KPlayer/KNpc), tần số, thứ gì ăn tick; (2) `script\system\online.lua` được gọi từ đâu mỗi phút (hàm OnLine trong mã server), lỗi "Script error ... online.lua" nghĩa là gì và nó có chặn tick không; (3) trạng thái cưỡi ngựa và đồng bộ vị trí (S/KPlayer.cpp:3716-3769, gói SyncPlayerMin/SyncObjectState) liên quan gì tới "giật ngựa khi đi".
Mỗi điều ghi THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Có TÓM TẮT 5 DÒNG đầu file, dòng "ĐÃ ĐỌC SỔ TAY: <tệp HIEU-GAME>" cho mọi sổ tay liên quan (SO-TAY-NGUA-PHI-PHONG.md, 06-mang-goi-tin/SO-TAY-GOI-TIN.md, SO-TAY-VONG-LAP-SERVER.md).

## Nguồn cần đọc
- Server (chỉ đọc): `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/Core/Src/` (KPlayer.cpp, KSubWorld.cpp, KNpc.cpp, ScriptFuns.cpp) và `MultiServer/GameServer/`.
- Lua: `D:/JX-source` hoặc `C:/Jx1CocoV3/docs-analysis/out/online.fixed.lua` (bản hook thử, chỉ để biết dạng; không coi là bản trên VM).
- HIEU-GAME/06-mang-goi-tin/SO-TAY-VONG-LAP-SERVER.md, HIEU-GAME/01-trang-bi-cuong-hoa/SO-TAY-NGUA-PHI-PHONG.md.

## Phạm vi và quyền đã duyệt
- Được sửa: đúng vung_file. Không sửa mã game, không build, không chạy exe/VM/mạng.
- Commit: có (nhánh task); push: không.

## Báo cáo cuối
`JX1_OPS/REPORTS/HG-S1.md` theo mẫu (1 sơ đồ Mermaid, `liên quan: ...`, TOM TAT 5 DONG, ĐÃ XÁC MINH / CHƯA XÁC MINH, DONE/PARTIAL).
