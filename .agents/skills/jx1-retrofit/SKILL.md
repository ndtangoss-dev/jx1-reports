---
name: jx1-retrofit
description: Chuẩn hóa báo cáo JX1 cũ theo JX1_OPS/DESIGN/CHUAN-BAO-CAO.md mà không đổi kết luận; lập bảng phạm vi và chỉ mục.
---
# Chuẩn hóa báo cáo cũ JX1
1. Đọc `JX1_OPS/DESIGN/CHUAN-BAO-CAO.md` trước. Mỗi báo cáo: giữ nguyên TÓM TẮT, kết luận, số liệu, bằng chứng.
2. Thêm khối thông tin (Loại, Chủ đề, Từ khóa, Trạng thái, Độ phủ, Liên quan, Cần tôi quyết định) ngay dưới tiêu đề.
3. Thêm 1 sơ đồ Mermaid, bảng "Phạm vi và độ phủ" đủ phần tử (đếm từ dữ liệu gốc chỉ đọc, ghi nguồn file:dòng).
4. Phát hiện sai/sót/lỗi mã hóa: ghi vào mục "Phát hiện khi chuẩn hóa" cuối file; không sửa lặng kết luận.
5. Từ khóa gồm tên Việt, tên gốc, ID. Liên quan trỏ tới báo cáo/DESIGN/BUG có thật (kiểm file tồn tại).
6. Ghi `REPORTS/_CHIMUC/<ID>.tsv` (file, loại, chủ đề, từ khóa, trạng thái, độ phủ, liên quan), UTF-8, tab.
7. Làm từng file, commit sau mỗi 5 file. Không sửa mã, không chạy exe/VM/mạng, không push.
8. (#107.7) Thêm mục "Giải mã tên": bảng tên gốc | mã hóa (GBK cho Hán, TCVN3 cho Việt cũ) | chữ đúng UTF-8 | file:dòng. Giữ nguyên tên gốc.
9. (#107.7) Thêm mục "Sắp theo cấu trúc game": kỹ năng theo phái → nhánh → cấp học, trang bị theo bộ liệt kê từng món, quái/NPC theo bản đồ. Báo cáo R đã xong chỉ cần thêm hai mục này (đợt bổ sung), không làm lại.
