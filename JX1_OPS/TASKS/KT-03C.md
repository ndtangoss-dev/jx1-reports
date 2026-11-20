---
id: KT-03C
title: Bản đồ chuỗi: quái/NPC xuất hiện trên màn (đồng bộ, tầm nhìn)
status: running
level: L3
agent: codex
effort: high
priority: 1
owner: B
branch: task/KT-03C
worktree: D:\JX-wt\KT-03C
depends_on: []
backlog_ref: "Q-100 (20/11 12:02, đại vương duyệt: tiểu yêu bù kiến thức + chia thư mục)"
vung_file: ['JX1_OPS/HIEU-GAME/04-quai-npc-ban-do/BAN-DO-QUAI-HIEN-THI.md']
tai_nguyen: []
updated: 2026-11-20
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Lỗi chủ báo: đi tới nơi quái mới đột ngột hiện. Nguồn sẵn: DESIGN/B-01-LOC-HIEN-THI.md, visibility.ini (B-02), phần B ghi cuối HOP-THU/A-B.md (khóa yêu cầu quái 100 frame KNpcSet.cpp:1022, NormalSync). Chuỗi: server chọn NPC trong tầm → gói sync → client yêu cầu chi tiết → tạo NPC → vẽ. Ghi các tham số tầm nhìn/khoảng cách/chu kỳ và chỗ có thể chỉnh. Đầu ra là MỘT "bản đồ chuỗi" dễ tra cho A/B khi sửa mã: (1) tóm tắt bằng lời thường; (2) chuỗi từ thao tác người chơi → client → gói tin → server → Lua → dữ liệu → hiển thị, mỗi bước file:dòng + tên hàm; (3) chỗ dự án đã sửa đè (qh9A/B-0xx/qhcuonghoa.lua...) so với gốc; (4) chỗ dễ làm sai khi sửa; (5) "KỊCH BẢN KIỂM ĐỘNG" cho đợt 2: đồ/nhân vật cần, thao tác, số đọc ở đâu, kỳ vọng (để A/bot chạy sau; worker KHÔNG tự chạy).

## Nguồn cần đọc
- `JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md`, `JX1_OPS/MA-NGUON/*.md` (bản đồ mã tự sinh), sổ tay `SO-TAY-*/HIEU-*` liên quan, REPORTS nêu ở trên.
- Mã: client `D:\JX-build\qh9A\Classes`, server `D:\JX-build\src18` (bản dự án ở `D:\JX-wt\QH-B035`), script `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\script`.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ sửa tệp trong vung_file.
- KHÔNG sửa mã, KHÔNG chạy exe/gs001, KHÔNG đụng Test-36/LDPlayer/VM/Main VM, không mạng, không đọc khóa/mật khẩu.
- Tra Graphify TRƯỚC khi đọc mã (`D:\JX-tools\graphify-venv\Scripts\graphify.exe query|explain|path`, gốc client `D:\JX-build\qh9A\Classes`, server `D:\JX-build\src18`); ghi dòng "ĐÃ TRA ĐỒ THỊ: lệnh → kết quả" trong báo cáo. Đồ thị chỉ để định vị: kiểm lại file thật và dòng hiện tại.
- Đọc trước kiến thức sẵn có (DESIGN/MUC-LUC-TRI-THUC.md, REPORTS liên quan, sổ tay) và ghi "ĐÃ ĐỌC KIẾN THỨC: ..."; không viết lại cái đã có, chỉ bù chỗ thiếu và dẫn nguồn.
- File nguồn GBK: đọc đúng mã GBK khi gặp chữ Hán; ghi cả chữ Hán gốc + pinyin + tiếng Việt.
- Mỗi lần đọc <= ~400 dòng; không đọc cả thư mục lớn.
- Mọi điều ghi nhãn ĐÃ ĐỌC MÃ (file:dòng) / TÀI LIỆU / CHƯA KIỂM TRONG GAME. Không ghi "đã kiểm" nếu chưa chạy game.
- Commit: Tổng quản commit hộ; không push tay.

## Báo cáo cuối
`JX1_OPS/REPORTS/KT-03C.md` theo DESIGN/CHUAN-BAO-CAO.md: TÓM TẮT 5 DÒNG, 1 sơ đồ Mermaid, dòng `liên quan: ...`, ĐÃ TRA ĐỒ THỊ, ĐÃ ĐỌC KIẾN THỨC, DA XAC MINH / CHUA XAC MINH, DONE/PARTIAL/BLOCKED.

## Nhịp sống
Ở mốc lớn ghi một dòng vào `D:\JX-wt\KT-03C.nhip`.

## Kết quả
- Trạng thái: DONE cho bản đồ chuỗi tĩnh; không chạy build/game/VM/mạng.
- Đầu ra: `JX1_OPS/HIEU-GAME/04-quai-npc-ban-do/BAN-DO-QUAI-HIEN-THI.md` và báo cáo `JX1_OPS/REPORTS/KT-03C.md`.
- Đã đối chiếu movement → NormalSync/BroadCast → request NPC → NPC_SYNC → tạo/vẽ; B-02 tách riêng và runtime chưa xác minh.
- Kịch bản kiểm động đã chuẩn bị cho A/bot; worker không chạy.
- Không commit theo phân công Tổng quan; chưa có SHA.
- Nhịp ngoài workspace: ghi `D:\JX-wt\KT-03C.nhip` bị Access denied tại mốc bắt đầu.
