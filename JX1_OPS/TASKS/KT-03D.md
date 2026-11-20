---
id: KT-03D
title: Bản đồ chuỗi: di chuyển và cưỡi ngựa (nguồn gây khựng 4–5 giây)
status: done
level: L3
agent: codex
effort: high
priority: 1
owner: B
branch: task/KT-03D
worktree: D:\JX-wt\KT-03D
depends_on: []
backlog_ref: "Q-100 (20/11 12:02, đại vương duyệt: tiểu yêu bù kiến thức + chia thư mục)"
vung_file: ['JX1_OPS/HIEU-GAME/02-nhan-vat-thuoc-tinh/BAN-DO-DI-CHUYEN-CUOI-NGUA.md']
tai_nguyen: []
updated: 2026-11-20
status_note: "da gop (B), Chat duyet #B-051"
---

## Mục tiêu và tiêu chí xong
Lỗi chủ báo: cưỡi ngựa cứ 4–5 giây khựng một nhịp (trên LAN chưa tái hiện). Nguồn sẵn: báo cáo nội suy/đo mạng vc22–vc23 (TU-SONNET 19/11), REPORTS/DO-MUOT-MOC-GOC*. Chuỗi: joystick → lệnh di chuyển client → gói → server đối chiếu vị trí → sửa vị trí (kéo lùi) → nội suy client; chu kỳ nào ~4–5 giây (đồng bộ vị trí, ping, tick) có thể gây khựng. Đầu ra là MỘT "bản đồ chuỗi" dễ tra cho A/B khi sửa mã: (1) tóm tắt bằng lời thường; (2) chuỗi từ thao tác người chơi → client → gói tin → server → Lua → dữ liệu → hiển thị, mỗi bước file:dòng + tên hàm; (3) chỗ dự án đã sửa đè (qh9A/B-0xx/qhcuonghoa.lua...) so với gốc; (4) chỗ dễ làm sai khi sửa; (5) "KỊCH BẢN KIỂM ĐỘNG" cho đợt 2: đồ/nhân vật cần, thao tác, số đọc ở đâu, kỳ vọng (để A/bot chạy sau; worker KHÔNG tự chạy).

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
`JX1_OPS/REPORTS/KT-03D.md` theo DESIGN/CHUAN-BAO-CAO.md: TÓM TẮT 5 DÒNG, 1 sơ đồ Mermaid, dòng `liên quan: ...`, ĐÃ TRA ĐỒ THỊ, ĐÃ ĐỌC KIẾN THỨC, DA XAC MINH / CHUA XAC MINH, DONE/PARTIAL/BLOCKED.

## Kết quả

## Nhịp sống
Ở mốc lớn ghi một dòng vào `D:\JX-wt\KT-03D.nhip`.

## Kết quả cuối

Trạng thái: PARTIAL. Đã tạo bản đồ chuỗi tĩnh `JX1_OPS/HIEU-GAME/02-nhan-vat-thuoc-tinh/BAN-DO-DI-CHUYEN-CUOI-NGUA.md` và báo cáo `JX1_OPS/REPORTS/KT-03D.md`; đã lần theo client walk/run, server handler, nhánh cưỡi ngựa và nội suy client. Chưa xác nhận nguyên nhân khựng 4–5 giây; cạnh gọi joystick → vòng lệnh, dữ liệu Lua/bảng tốc độ và phép đo kiểm động còn thiếu. Không build/chạy game exe/VM/mạng; không sửa mã nguồn. Graphify CLI query đã được gọi hai lần và lỗi không tìm thấy graph theo worktree hiện tại; đã dừng CLI, dùng graph report sinh sẵn để định vị rồi kiểm file thật. Không ghi được `D:\JX-wt\KT-03D.nhip` do quyền truy cập bị từ chối ngoài worktree; không đổi quyền. Chưa commit/push; Tổng quản commit hộ.

Bước tiếp theo: A/B chạy kịch bản trong báo cáo khi được giao, thu HUD FPS/ping, trace P1–P4/U và SvrFPS/tick; chỉ kết luận sau khi log trùng thời điểm khựng.

Lỗi/cách thử: ripgrep không có trong shell nên dùng Select-String; một lần tìm tên file đệ quy cho đầu ra quá rộng, đã dừng và chuyển sang truy vấn đường dẫn cụ thể. Lệnh đó chỉ liệt kê đường dẫn, không mở nội dung file.
