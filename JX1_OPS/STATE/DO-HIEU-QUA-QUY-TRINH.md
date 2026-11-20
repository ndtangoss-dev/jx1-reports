# ĐO HIỆU QUẢ VÁ QUY TRÌNH (Q-99/Q-100) — Chat ghi, đại vương xem

## Mốc trước khi vá (06:59–11:52, 20/11) — đo từ kho
- Quyết định Chat ra: 12 (Q-88..Q-98b) trong ~5 giờ → đổi hướng lớn 4 lần (tài phú client → thuộc tính; vá tại chỗ → chuỗi gốc → nút mới).
- Thư Chat→A/B: ~20. Bản gs001 nạp hỏng/hoàn tác: 2 (B-040 sập, B-041 bỏ). Restart gs001: ≥4 (≈40–60 phút chờ).
- Tiêu chí cường hóa (Q-94) đạt bằng số thật: 0/8.
- Báo cáo có "ĐÃ TRA ĐỒ THỊ": 0. Dẫn sổ tay/MA-NGUON trong A-B.md: 0.
- Tiểu yêu chạy: 0 (5 khóa rảnh cả buổi).

## Chỉ số theo dõi sau vá (Chat cập nhật mỗi giờ)
| Giờ | Tiêu chí (c) đạt /8 | Bước hồ sơ ĐÃ KIỂM | Quyết định đổi hướng mới | Báo cáo có ĐÃ TRA ĐỒ THỊ / tổng | Báo cáo bị trả lại | DANG-LAM cập nhật (A/B) | Tiểu yêu chạy / KT xong | Restart gs001 |
|---|---|---|---|---|---|---|---|---|
| 12:10 | 0 | 0 | 0 | B: có (B-046) / A: chưa | 0 | chưa / chưa | 0 / 0 | 0 |
| 12:13 | 1 (TC1 nút mới mở UI Give gốc) | 2 (bước 1 nạp Lua, bước 3 nút mới+vc27) | 0 | A: ảnh có, chưa ghi dòng tra đồ thị / B: có | 0 | A có / B có (hook SessionStart+Graphify B đã kiểm) | 0 / 0 (9 KT ready, Tổng quản chưa giao) | 0 |

Nghiệm thu hình ảnh 12:13 (Chat xem ảnh DESIGN/ANH-NGHIEM-THU/q97-*):
- q97-nut-cuonghoa-moi-man-chinh: nút mới là ô vuông nhỏ biểu tượng lửa cạnh nút Auto (góc phải trên). ĐẠT chức năng; CHƯA ĐẠT dễ thấy: nhỏ, không có chữ "Cường hóa" như các nút bên cạnh (Xếp Hạng, Sơn Động, Auto) → yêu cầu thêm nhãn chữ cùng kiểu.
- q97-ui-giao-goc: cửa sổ "Giao" gốc mở cùng Hành Trang; lời nhắc gốc ghi "1 mảnh trang bị và 1 viên đá cường hóa" (không phải lời nhắc của B "đồ đang mặc hãy tháo ra") → client đang hiện mô tả cũ, cần sửa chữ theo luật ta (thủy tinh 3 loại).
- q97-giao-xac-nhan: thông báo lỗi gốc, chữ dịch tối nghĩa ("tảng đá phối hợp không đúng") → callback đang về sysError gốc, chưa tới Lua B (B đang tra).
