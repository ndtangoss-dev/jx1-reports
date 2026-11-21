---
id: HG-S2
title: Hiểu game: giật ngựa phía client (kéo về vị trí, CORRECT_SYNC_RANGE) và số quái/NPC ăn tick (nối #B-090)
status: ready
level: L3
agent: codex
effort: high
owner: B
priority: 1
branch: task/HG-S2
worktree: D:\JX-wt\HG-S2
depends_on: []
backlog_ref: "#B-090 (A-B.md 18:50), SO-TAY-TICK-GS001.md"
vung_file: [JX1_OPS/HIEU-GAME/07-server-luu-tru/SO-TAY-GIAT-NGUA-CLIENT.md, JX1_OPS/REPORTS/HG-S2.md]
tai_nguyen: []
updated: 2026-11-21
---

## Mục tiêu và tiêu chí xong
Viết sổ tay `HIEU-GAME/07-server-luu-tru/SO-TAY-GIAT-NGUA-CLIENT.md` (đọc tĩnh): (1) client xử lý gói đồng bộ vị trí người chơi/ngựa thế nào, khi nào kéo nhân vật về vị trí server (tìm `CORRECT_SYNC_RANGE` hoặc tương đương), ngưỡng, có nội suy không; (2) số quái/NPC mỗi bản đồ chính (đọc `HIEU-GAME/04-quai-npc-ban-do/` rồi dữ liệu Settings) để ước NPC trong vùng hoạt động; (3) đối chiếu kết luận #B-090: xếp hạng nghi phạm tick (KRegion.cpp NewRegActivate, NormalSync) có số lượng nào ủng hộ/bác bỏ.
Mỗi điều ghi THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. TÓM TẮT 5 DÒNG đầu file; dòng "ĐÃ ĐỌC SỔ TAY: <tệp>" cho mọi sổ tay liên quan (SO-TAY-TICK-GS001.md, SO-TAY-NGUA-PHI-PHONG.md, BAN-DO-DI-CHUYEN-CUOI-NGUA.md, 04-quai-npc-ban-do/SO-TAY-QUAI-NPC-BAN-DO.md).

## Nguồn cần đọc
- Client (chỉ đọc): `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes`.
- Server (chỉ đọc): `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/Core/Src/` (KRegion.cpp, KNpc.cpp NormalSync).
- A-B.md mục "B → A/Chat 18:50 — #B-090".

## Phạm vi và quyền đã duyệt
- Được sửa: đúng vung_file. Không sửa mã game, không build, không chạy exe/VM/mạng.
- Commit: có (nhánh task); push: không.

## Báo cáo cuối
`JX1_OPS/REPORTS/HG-S2.md` theo mẫu (1 sơ đồ Mermaid, `liên quan: ...`, TOM TAT 5 DONG, ĐÃ XÁC MINH / CHƯA XÁC MINH, DONE/PARTIAL).
