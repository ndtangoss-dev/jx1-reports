# Đánh giá bằng chứng của Haiku (ảnh p46qa-*, p46-*)

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Người đánh giá: Sonnet (QA Lead)

Phương pháp: đã xem trực tiếp một mẫu ảnh (khoảng 20 trên hơn 130 ảnh): p46-m3, p46qa-06, 08, 14, 16, 18, 20, 22, 28, 32, 45, 50, 60, 70, 78, 85, s05-tip. Ảnh khác chưa xem; kết luận "chưa thấy" nghĩa là chưa thấy trong mẫu, không phải chắc chắn không có.

## Có bằng chứng

| Mục | Bằng chứng | Mức |
|---|---|---|
| Vào game, nhân vật jxt36a ở Ba Lăng Huyện, Cấp 1, HP 204/204 | p46qa-06, 08, 14 | Đủ |
| Nhận Lệnh bài GM từ Lễ Quan | chat "Lệnh bài GM x 1" (p46qa-14, 16) | Đủ |
| Mở bảng GM, 11 nút, kèm dòng thông tin | p46qa-18 | Đủ cho kiểm kê menu chính |
| Hộp "Nhap Cap Do", nhập 200 | p46qa-20, 22 | Đủ cho hộp thoại; giá trị hợp lệ khác chưa thử |
| Cấp 1 thành Cấp 200, HP 204 thành 1000 | p46qa-14 so với 60/70; chat 196 đến 200 (p46qa-28) | Đủ, trước/sau có |
| Bảng kỹ năng 23 kỹ năng cấp 20, điểm kỹ năng 199 | p46qa-28 | Đủ về số lượng; chưa đủ về tên |
| Mô tả kỹ năng Tâm Giới Quy Thiên | p46qa-32 | Đủ cho một kỹ năng |
| Bản đồ lớn mở, nhãn NPC, ô tọa độ, Tìm tọa độ, Đóng | p46-m3, p46qa-78 | Đủ |
| Nhận tiền và xu (lượng và xu tăng trước/sau) | p46qa-70 | Đủ cho số dư; nút GM tương ứng chưa ghi rõ |
| Mở cửa hàng Học trò thợ rèn, xem chi tiết vũ khí | p46qa-45 | Đủ |
| Đã mua hàng: tiền giảm, chat "Thiết Trụy thủ x 1", "Mã Bài - Ngựa 8x x 1" | p46qa-85 | Có, nhưng không rõ từng giao dịch riêng |

## Chưa có bằng chứng (trong mẫu đã xem)

| Mục | Vấn đề |
|---|---|
| Menu con của Admin Quản Lý 1/2, ReloadScript, Goi npc test, SetFightState, Quản Lý Server, Đổi màu, Reset vượt ải, Open Các Tính Năng | Không mở (đúng quy tắc an toàn); chưa mở không phải lỗi. |
| "Nhận Kỹ Năng 15x" là gì, và nút nào cho tiền | Không có ảnh chụp bảng menu con "Nhận Các Loại Điểm" trong mẫu; thứ tự bấm không ghi. Cần ảnh menu con và ảnh trước/sau từng nút. |
| Điều hướng bằng "Tìm tọa độ" thực sự tự đi | Chỉ có ô nhập "198/197" (p46qa-78) và ảnh ở 202/198 (p46qa-50); không có chuỗi tọa độ theo thời gian. Nhân vật có thể đi bằng joystick. Đặc biệt p46qa-50 cho thấy nhân vật ở 202/198, lệch 198/197, và vẫn mở được cửa hàng: tương tác từ xa, chưa biết tầm. |
| Mua đủ mỗi loại vũ khí | Chỉ thấy một vũ khí mua và trang cửa hàng đầu. |
| Thần Hành Phù, Bảo Vật, ngựa được dùng/cưỡi | Chưa thấy ảnh Bảo Vật, Thần Hành Phù trong hành trang, hay nhân vật cưỡi ngựa. Chỉ có chat "Mã Bài - Ngựa 8x". |
| Phong Lăng Độ, 162/186 | Chưa thấy ảnh trong mẫu. |
| Mọi số đo hiệu năng (frame time, p50/p95/p99) | Chưa thấy; các ảnh chỉ có FPS tức thời trên HUD (26 đến 82), dao động quá lớn nên không dùng làm số đo. Chưa có file log kèm. |
| Thử kỹ năng, đạn | Chưa thấy ảnh thi triển kỹ năng trong mẫu. |

## Điểm cần chú ý về chất lượng
- Ảnh có dấu thời gian trên HUD (10:23 đến 10:49) tiện sắp thứ tự, nhưng nhiều ảnh bị bảng/ chat che; ảnh phóng to (-zoom, -tip) giúp đọc chữ nhỏ.
- Chính tả NPC "Lễ Quan"/"Lệ Quan" và vũ khí "Thiết Trụy thủ" đọc từ ảnh có thể lệch dấu; ghi cả hai biến thể.
- Chữ đọc từ ảnh bởi AI có rủi ro sai chữ số; số quan trọng (tọa độ, tiền) cần ít nhất hai ảnh khớp.
- Thiếu hồ sơ thao tác: ảnh không kèm ghi chú thao tác (nút nào, lúc nào). Cần nhật ký thao tác kèm tên ảnh.
