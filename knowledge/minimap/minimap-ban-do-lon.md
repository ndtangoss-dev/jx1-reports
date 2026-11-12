# Minimap và bản đồ lớn

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Bản đồ khảo sát: Ba Lăng Huyện

## Minimap nhỏ (góc phải trên)
- Hiển thị tên bản đồ, chấm màu (NPC/người chơi, chưa rõ ý nghĩa từng màu: UNKNOWN), và dòng tọa độ nhân vật dạng X/Y ở đáy ô (ví dụ 203/199, 202/198). Trạng thái: VERIFIED (p46qa-08.png, p46qa-50.png, p46-m3.png).
- Dòng tọa độ này là nguồn đọc vị trí rẻ nhất cho phát hiện kẹt (AI đọc ảnh). Độ tin cậy khi đọc ảnh nhỏ: chưa đo; nên chụp zoom (p46qa-06-minimap-zoom.png là ví dụ).

## Mở bản đồ lớn
- Thao tác: CHẠM ĐÚP nhanh vào minimap, hai chạm cách nhau dưới khoảng 0,33 s (mã nguồn so sánh dưới 6 nhịp game). Chạm đơn không có tác dụng.
- Lệnh đã chạy được: `input tap 895 55 & sleep 0.12; input tap 895 55`.
- Kết quả: bản đồ lớn mở. Trạng thái: VERIFIED (p46-m3.png, p46qa-78.png).

## Thành phần bản đồ lớn
| Thành phần | Ghi chú | Trạng thái |
|---|---|---|
| Tên bản đồ (trên trái) | "Ba Lăng Huyện" | VERIFIED (p46-m3.png) |
| Ô nhập tọa độ | hiện "0/0" khi trống; nhập dạng X/Y, ví dụ 198/197 | VERIFIED (p46qa-78.png) |
| Nút "Tìm tọa độ" | đặt điểm đến theo tọa độ đã nhập; kết quả di chuyển xem navigation/tim-toa-do-va-di-chuyen.md | DISCOVERED |
| Nút "Đóng" | đóng bản đồ lớn | VERIFIED hiển thị; kết quả đóng chưa kiểm riêng |
| Nhãn NPC/địa điểm | chữ vàng trên bản đồ | VERIFIED (p46-m3.png) |
| Chấm tím | cụm quanh khu Lễ Quan; ý nghĩa chưa rõ | UNKNOWN |

## Chưa có / chưa kiểm
- Tìm NPC theo tên: giao diện chưa thấy ô tìm tên hay danh sách NPC. Cách thực tế: đọc nhãn trên bản đồ, đọc tọa độ, nhập vào "Tìm tọa độ". Trạng thái: DISCOVERED (chưa thấy chức năng tìm tên).
- Chỉ đường/đánh dấu tự động trên bản đồ lớn: UNKNOWN.
- Có kéo/thu phóng bản đồ lớn không: NOT_TESTED.
- Mở/đóng minimap khi đang chạy có ảnh hưởng frame time không: NOT_TESTED (ca A6 trong kế hoạch).
