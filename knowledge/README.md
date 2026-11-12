# Knowledge base QA JX1 mobile (Phase 46)

Ngày lập: 2026-11-12. Build: Fix36 + p46 diag. Người lập: Sonnet (QA Lead), từ ảnh và ghi chép của Haiku/Opus. Nhân vật test: jxt36a (hệ Kim). Môi trường: LDPlayer 960x540, server test 36Hz (VM thử, không phải Main VM).

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| minimap/ | Cách mở, thành phần và chức năng minimap / bản đồ lớn |
| npcs/ | Hồ sơ NPC (mỗi NPC một file) và danh sách nhãn đọc từ bản đồ lớn |
| navigation/ | Cách di chuyển, tìm tọa độ, phát hiện kẹt |
| gm-token/ | Sơ đồ menu Lệnh bài GM, phân loại an toàn từng mục |
| items/ | Vật phẩm cần cho test |
| skills/ | Kỹ năng và bảng kỹ năng |
| maps/ | Hồ sơ bản đồ |

## Mẫu hồ sơ

Mỗi hồ sơ gồm: tên chính xác (đúng như hiển thị), bản đồ, tọa độ, bằng chứng (chỉ tên file ảnh, không nhúng, không đường dẫn), thao tác, kết quả, trạng thái, ngày, build.

## Quy tắc trạng thái

- **VERIFIED**: đã thực hiện và có bằng chứng trực tiếp (ảnh/log cho thấy trạng thái thay đổi đúng như dự kiến). Toast "thành công" một mình không đủ; phải thấy HUD/hành trang/bảng kỹ năng đổi.
- **DISCOVERED**: đã nhìn thấy trên giao diện nhưng chưa thử, hoặc đã thử nhưng kết quả chưa xác nhận đủ.
- **NOT_TESTED**: biết có, chưa thao tác. Mục GM rủi ro luôn ở NOT_TESTED cho tới khi được duyệt.
- **UNKNOWN**: chưa biết (chức năng, giá trị hợp lệ, cách hoàn tác).
- **BLOCKED**: không làm được do thiếu công cụ hoặc điều kiện game; ghi rõ giới hạn.

Không nâng DISCOVERED/UNKNOWN lên VERIFIED nếu chưa có bằng chứng thực nghiệm. Phân loại an toàn của mục GM chưa mở là "phân loại tạm theo nhãn, chưa xác minh".

## Quy tắc dữ liệu

Không ghi IP, mật khẩu, tên tài khoản đăng nhập, token, đường dẫn tuyệt đối vào đây. Chỉ dùng tên nhân vật jxt36a. Ảnh bằng chứng chỉ ghi tên file; bản gốc do Haiku/Opus lưu cùng đợt chạy.

## Chỉ mục

- minimap/minimap-ban-do-lon.md
- navigation/tim-toa-do-va-di-chuyen.md
- navigation/phat-hien-ket.md
- npcs/le-quan.md, npcs/hoc-tro-tho-ren.md, npcs/nhan-ban-do-ba-lang-huyen.md
- gm-token/lenh-bai-gm-so-do-menu.md, gm-token/nhan-cac-loai-diem.md
- items/lenh-bai-gm.md, items/tien-xu-ngua-vu-khi.md
- skills/bang-ky-nang-cap-200.md
- maps/ba-lang-huyen.md
