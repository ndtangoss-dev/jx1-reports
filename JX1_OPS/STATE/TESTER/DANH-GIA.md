# ĐÁNH GIÁ TESTER (Sonnet chấm mỗi 30 phút: thông tin mới thật? lỗi tái hiện được? lặp/treo?)

## 19/11 12:15 — Sonnet chấm TS-03 (tester01, mục dang-nhap/tao-nhan-vat, qua cầu)
- Bước thật: [THẤY] 15 lệnh qua cầu (chụp, chạm Hành trang, Cài đặt→Đăng xuất→Bắt đầu→chọn máy chủ→mũi tên tài khoản), có ảnh + ket-qua.jsonl. 1/4 bước kiểm thật (cầu hoạt động + điều hướng); chưa đăng nhập/tạo nhân vật.
- Thông tin mới thật: form đang lưu `testa` chứ không phải `tester01`; mật khẩu `tester01` chưa lưu trong app (khác lời giao). Tiểu yêu đúng khi DỪNG, không nhập/suy đoán mật khẩu (đúng luật).
- Chất lượng: TỐT (làm thật, ghi bằng chứng, dừng đúng chỗ). Lần chấm tốt thứ 1 (Q-59 cần ≥2 liên tiếp trước tester02).
- [TỰ QUYẾT] gỡ chặn: lượt kế cho dùng tài khoản `testa` đã lưu trên LD này (Sonnet không dùng LD cùng lúc) để tạo thêm nhân vật theo bảng ngũ hành; không nhập mật khẩu.

## 19/11 13:10 — TS-03 lượt 2 và 3 (tester01, khóa JX-K4): KHÔNG ĐẠT
- Cầu im từ 11:59; cả hai lượt tiểu yêu chạy (có nhịp tim) nhưng chỉ sửa tài liệu, 0 lệnh thật. Không phải lỗi khóa/tốc độ 0.5x (nó chạy được) mà là không thao tác. Không chấm TỐT. Chuỗi tốt liên tiếp quay về 0.
