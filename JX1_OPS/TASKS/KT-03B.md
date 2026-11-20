---
id: KT-03B
title: Bản đồ chuỗi: nút đánh thường và làn lệnh kỹ năng
status: ready
level: L3
agent: codex
effort: high
priority: 1
owner: B
branch: task/KT-03B
worktree: D:\JX-wt\KT-03B
depends_on: []
backlog_ref: "Q-100 (20/11 12:02, đại vương duyệt: tiểu yêu bù kiến thức + chia thư mục)"
vung_file: ['JX1_OPS/HIEU-GAME/03-ky-nang-chien-dau/BAN-DO-DANH-THUONG-LAN-LENH.md']
tai_nguyen: []
updated: 2026-11-20
---

## Mục tiêu và tiêu chí xong
Lỗi chủ báo: bấm nút đánh thường chỉ chạy tới quái, không đánh. Nguồn sẵn: REPORTS/LAN-LENH-KY-NANG*, phần B đề xuất cuối HOP-THU/A-B.md (KNpcSet.cpp:1022, KNpcAI.cpp:772, KNpc.cpp:6762-6830, Settings\CmdLane.ini). Chuỗi: nút client → lệnh → gói tin → server KNpc xử lý kỹ năng/di chuyển → bán kính tấn công → trả kết quả. Liệt kê các giả thuyết lỗi kèm điểm kiểm. Đầu ra là MỘT "bản đồ chuỗi" dễ tra cho A/B khi sửa mã: (1) tóm tắt bằng lời thường; (2) chuỗi từ thao tác người chơi → client → gói tin → server → Lua → dữ liệu → hiển thị, mỗi bước file:dòng + tên hàm; (3) chỗ dự án đã sửa đè (qh9A/B-0xx/qhcuonghoa.lua...) so với gốc; (4) chỗ dễ làm sai khi sửa; (5) "KỊCH BẢN KIỂM ĐỘNG" cho đợt 2: đồ/nhân vật cần, thao tác, số đọc ở đâu, kỳ vọng (để A/bot chạy sau; worker KHÔNG tự chạy).

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
`JX1_OPS/REPORTS/KT-03B.md` theo DESIGN/CHUAN-BAO-CAO.md: TÓM TẮT 5 DÒNG, 1 sơ đồ Mermaid, dòng `liên quan: ...`, ĐÃ TRA ĐỒ THỊ, ĐÃ ĐỌC KIẾN THỨC, DA XAC MINH / CHUA XAC MINH, DONE/PARTIAL/BLOCKED.

## Kết quả

## Nhịp sống
Ở mốc lớn ghi một dòng vào `D:\JX-wt\KT-03B.nhip`.
