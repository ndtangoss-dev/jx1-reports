# Điều hướng bằng "Tìm tọa độ"

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Bản đồ: Ba Lăng Huyện

## Quy trình đã thấy
1. Chạm đúp minimap để mở bản đồ lớn (xem minimap/minimap-ban-do-lon.md).
2. Chạm ô tọa độ, nhập X/Y (ví dụ 198/197). Ảnh: p46qa-78.png cho thấy ô chứa "198/197".
3. Nhấn "Tìm tọa độ", rồi "Đóng".
4. Chờ nhân vật tự đi; đọc tọa độ ở đáy minimap để xác nhận tiến gần.

Trạng thái bước 2: VERIFIED (nhập được). Bước 3-4: DISCOVERED. Lý do: p46qa-50.png cho thấy nhân vật ở 202/198 với NPC "Học trò thợ rèn" đang là mục tiêu và p46qa-45.png sau đó mở cửa hàng, nhưng chưa có chuỗi ảnh tọa độ liên tiếp chứng minh nhân vật tự đi bằng "Tìm tọa độ" (khác với Haiku tự điều khiển joystick). Cần Haiku ghi lại chuỗi tọa độ theo thời gian.

## Tọa độ tham chiếu (do chủ máy cung cấp, Ba Lăng Huyện)
| Đối tượng | Tọa độ | Trạng thái |
|---|---|---|
| Lễ Quan | 203/199 | VERIFIED: GM board ghi 203/199 khi nhân vật đứng cạnh NPC (p46qa-18.png) |
| Học trò thợ rèn | 198/197 | DISCOVERED: nhân vật đứng gần, ở 202/198, NPC mở được cửa hàng (p46qa-50.png, p46qa-45.png); tọa độ NPC chính xác chưa đối chiếu |
| Phong Lăng Độ (kịch bản chuẩn) | 162/186 | NOT_TESTED |

## Lưu ý
- Tọa độ ô khác pixel: GM board hiển thị cả X/Y*32 (ví dụ 52128/102208 và 1629/3194); quy đổi giữa hai hệ tọa độ chưa xác minh: UNKNOWN.
- Thời gian tự đi, độ chính xác điểm đến, hành vi khi bị chặn: NOT_TESTED.
