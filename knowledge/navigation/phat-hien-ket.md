# Phát hiện kẹt khi điều hướng

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Trạng thái: quy trình đề xuất (chưa có ví dụ kẹt thực tế)

## Tín hiệu
- Chính: tọa độ ở đáy minimap (hoặc dòng "Tọa Độ" trên bảng GM). Đọc 2 lần cách nhau 3 giây khi đang ra lệnh đi.
- Phụ: ảnh đổi hay không, hoạt ảnh chạy tại chỗ, nhãn đích.

## Quy tắc
1. Tọa độ không đổi qua 2 lần đọc liên tiếp (tổng 6 giây) trong khi nhân vật không thi triển/không mở bảng/không đang tải bản đồ: nghi kẹt.
2. Phân biệt trước khi kết luận: đang tải bản đồ, đang cast kỹ năng, bảng giao diện che/khóa điều khiển, ping cao (HUD hiển thị ms).
3. Tối đa 2 lần thử cùng cách (cùng hướng, cùng lệnh). Lần 3 phải đổi: hướng khác, đi vòng, dùng Tìm tọa độ tới điểm trung gian, hoặc đóng mọi bảng rồi thử lại.
4. Vẫn không đi được sau khi đổi cách: ghi MOVEMENT_BLOCKED, lưu ảnh, tọa độ, hướng đã thử, nghi ngờ nguyên nhân (tường/cổng/khu cấm/khóa điều khiển). Không chạy vô hạn.
5. Chỉ gắn SUCCESS khi tọa độ thực sự tiến gần đích hoặc đúng NPC được chọn.
