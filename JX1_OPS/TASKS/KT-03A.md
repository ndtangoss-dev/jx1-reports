---
id: KT-03A
title: Bản đồ chuỗi: tài phú và phi phong (yêu cầu, tự tháo)
status: running
level: L3
agent: codex
effort: high
priority: 1
owner: B
branch: task/KT-03A
worktree: D:\JX-wt\KT-03A
depends_on: []
backlog_ref: "Q-100 (20/11 12:02, đại vương duyệt: tiểu yêu bù kiến thức + chia thư mục)"
vung_file: ['JX1_OPS/HIEU-GAME/01-trang-bi-cuong-hoa/BAN-DO-TAI-PHU-PHI-PHONG.md']
tai_nguyen: []
updated: 2026-11-20
status_note: "Tong quan giao bang JX-K4"
---

## Mục tiêu và tiêu chí xong
Theo Q-90: tài phú là thuộc tính nhân vật (magic_special_point, m_nWealth), yêu cầu mặc phi phong kiểu sức mạnh (magic_item_reserve8, EnoughAttrib), tự tháo QhCheckPifeng. Nguồn bản dự án: patch DESIGN/QH-B039-tai-phu.patch, HOP-THU/A-B.md (hợp đồng v6), DESIGN/QH-B035-PHI-PHONG.md. Ghi rõ chỗ dự án thêm so với gốc, đường client hiển thị tooltip/khung nhân vật. Đầu ra là MỘT "bản đồ chuỗi" dễ tra cho A/B khi sửa mã: (1) tóm tắt bằng lời thường; (2) chuỗi từ thao tác người chơi → client → gói tin → server → Lua → dữ liệu → hiển thị, mỗi bước file:dòng + tên hàm; (3) chỗ dự án đã sửa đè (qh9A/B-0xx/qhcuonghoa.lua...) so với gốc; (4) chỗ dễ làm sai khi sửa; (5) "KỊCH BẢN KIỂM ĐỘNG" cho đợt 2: đồ/nhân vật cần, thao tác, số đọc ở đâu, kỳ vọng (để A/bot chạy sau; worker KHÔNG tự chạy).

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
`JX1_OPS/REPORTS/KT-03A.md` theo DESIGN/CHUAN-BAO-CAO.md: TÓM TẮT 5 DÒNG, 1 sơ đồ Mermaid, dòng `liên quan: ...`, ĐÃ TRA ĐỒ THỊ, ĐÃ ĐỌC KIẾN THỨC, DA XAC MINH / CHUA XAC MINH, DONE/PARTIAL/BLOCKED.

## Nhịp sống
Ở mốc lớn ghi một dòng vào `D:\JX-wt\KT-03A.nhip`.

## Kết quả

- **DONE — khảo sát tĩnh ngày 20/11/2026.** Đã tạo `JX1_OPS/HIEU-GAME/01-trang-bi-cuong-hoa/BAN-DO-TAI-PHU-PHI-PHONG.md` và báo cáo `JX1_OPS/REPORTS/KT-03A.md`; đủ 8/8 nhóm phạm vi, 10 ô tài phú, 11 bậc/nhóm biến thể phi phong và 18 kịch bản kiểm động (0/18 đã chạy).
- Đã tra Graphify và ghi đúng kết quả thiếu/mơ hồ/chờ không trả kết quả; đã đối chiếu file thật ở src18, QH-B035 và qh9A. Không dùng đồ thị hoặc báo cáo cũ thay bằng chứng mã hiện tại.
- Ghi riêng các khác biệt: mobile AutoEquip rồi hậu kiểm; túi đầy giữ phi phong khác lời v6; reserve8 khác tên requirement nháp; Lua B-044 bỏ đường xin W và E cuối0 có thể ghi đè cache UI. Không sửa kết luận, số liệu hoặc tệp báo cáo cũ.
- Không sửa mã/Settings, không build, chạy game/exe server/VM, dùng mạng hoặc đọc khóa/mật khẩu. Không stage/commit/push theo yêu cầu; Tổng quản commit hộ, chưa có SHA mới.
- Tệp nhịp `D:\JX-wt\KT-03A.nhip` ngoài vùng ghi sandbox nên không tạo/cập nhật; các mốc quan sát được và giới hạn này được ghi trong báo cáo, không bịa giờ bắt đầu hoặc nhận đã ghi nhịp.
- Bàn giao: Tổng quản rà tài liệu/commit; A/B xác nhận đúng cặp client/server/Lua rồi giao A/bot kiểm động theo 18 ca. Dữ liệu requirement, binary/APK triển khai, đăng nhập và hành vi thật vẫn CHƯA XÁC MINH.
