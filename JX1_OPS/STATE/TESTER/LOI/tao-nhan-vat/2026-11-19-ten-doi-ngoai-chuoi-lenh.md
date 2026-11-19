# LOI-tao-nhan-vat-001 — Tên đổi ngoài chuỗi lệnh và cảnh báo tên không hợp lệ

- Mục: tao-nhan-vat; TS-03 lượt 3.
- Mức độ: chặn kiểm có kiểm soát; chưa xác định mức lỗi game.
- Trạng thái: QUAN SÁT — CHƯA TÁI HIỆN CÓ KIỂM SOÁT; ghi Tổng quản qua hồ sơ, chưa gửi ngoài.
- Các bước đã thực hiện (chưa phải chuỗi tái hiện lỗi hoàn chỉnh):
  1. Form testa: tap(830,772), chờ/ảnh chọn máy chủ; tap(500,298), ảnh 08 màn tạo/tên placeholder.
  2. Tra bảng Võ Đang/Côn Lôn → Thổ; tap(960,855), ảnh 10 mẫu đổi/tên T36nv2 dù worker chưa gõ.
  3. Chỉ screenshot ID ts03-r3-20261119-130520731-11: ảnh 11 tên Tsbaone và “Tên nhân vật chứa ký tự đặc biệt hoặc các ký tự không được phép!”. Worker không text/key/tap Xác định.
- Kết quả thực tế: [ĐÃ XÁC MINH] tên/UI đổi ngoài chuỗi lệnh worker. [CHƯA XÁC MINH] nguyên nhân, đầu điều khiển khác, thao tác kích hoạt cảnh báo. Không suy chuỗi ASCII thấy trên ảnh là byte tên game đã nhận.
- Kết quả mong đợi: xác định một đầu điều khiển và ghi đủ lệnh/ảnh trước kiểm tạo; chỉ nhận tạo đạt khi có tên trong danh sách/kết quả lưu, giữ T36nv1. Chưa có cơ sở khẳng định tên thấy trên ảnh phải được chấp nhận.
- Ảnh/log: [08](../../KIEN-THUC/dang-nhap/TS-03-L3-1305/08.jpg), [10](../../KIEN-THUC/dang-nhap/TS-03-L3-1305/10.jpg), [11](../../KIEN-THUC/dang-nhap/TS-03-L3-1305/11.jpg), [ID/băm](../../KIEN-THUC/dang-nhap/TS-03-L3-1305/bang-chung.tsv). JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03-L3-1305/lenh.jsonl:1–11; ket-qua.jsonl:1–11, đoạn liên quan:8–11. JPEG <1 MB, không có mật khẩu/khóa.
- Tái hiện được mấy lần / mấy: 0 lượt tái hiện chủ động, 1 lần quan sát cảnh báo lúc 13:12:14; không lặp thử tên khi chưa rõ người điều khiển.
- Tiểu yêu, LD, giờ: TS-03; T36-tester01 theo task/hòm (chưa kiểm độc lập đích cầu); 19/11/2026, 13:08–13:12, UTC+7.
- Xử lý/bước tiếp: dừng mọi tap/text sau ảnh 11, hỏi người dùng về điều khiển đồng thời; chưa có trả lời tại mốc ghi hồ sơ. Tổng quản xác nhận một đầu điều khiển/hướng dẫn xử lý cảnh báo rồi tiếp tục. Chưa sửa mã/cấu hình, chưa xóa nhân vật.

liên quan: [báo cáo TS-03](../../../../REPORTS/TS-03.md), [bàn giao tạo](../../BAN-GIAO/tao-nhan-vat/README.md).
