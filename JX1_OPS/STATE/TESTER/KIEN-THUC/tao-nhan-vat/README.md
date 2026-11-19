# KIẾN THỨC: tao-nhan-vat
## Cần làm gì (từng bước, ai đọc cũng làm lại được)
(chưa có)
## Đã biết (kèm nguồn: ảnh/log/file:dòng)
(chưa có)
## Chưa hiểu
(chưa có)

## Ghi nhận TS-03 từ tài liệu

- Điều học được: Chọn ngũ hành khi tạo nhân vật; gia nhập môn phái là bước sau khi vào game.
- Bằng chứng: `JX1_OPS/STATE/TESTER/KIEN-THUC/mon-phai-ngu-hanh/README.md:3` (tài liệu tĩnh; CHƯA KIỂM màn hình tạo của TS-03).
- Cách dùng lại: Tra bảng theo môn phái cần kiểm và dùng ngũ hành tương ứng nếu màn hình tạo có lựa chọn đó. Ghi lại lựa chọn và kết quả thực tế.
- Ngày, tiểu yêu: 19/11/2026 — TS-03.

## Tiếp tục TS-03 — 19/11/2026

- Điều học được: [ĐÃ XÁC MINH] Kiểm cầu đã qua nhưng chưa thể kiểm tạo nhân vật vì form đang lưu tài khoản khác `tester01`. Nhân vật hiện sẵn trên ảnh đầu không chứng minh đã tạo nhân vật cho tài khoản được giao.
- Bằng chứng: `JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03/ket-qua.jsonl:1–3,11–14`; [ảnh form đã che ô mật khẩu](../dang-nhap/TS-03/06-tai-khoan-khong-khop.jpg).
- Cách dùng lại: Sau khi Tổng quản chuẩn bị đúng tài khoản, đăng nhập rồi mới xác định ô tạo nhân vật và đối chiếu bảng môn phái/ngũ hành. [CHƯA KIỂM] Màn tạo, lựa chọn hệ, khả năng tạo thêm và kết quả tạo; không thay kết luận nguồn tĩnh ở ghi nhận trước.
- Ngày, tiểu yêu: 19/11/2026 — TS-03. Chưa tạo, xóa hay sửa nhân vật.


## Lượt 3 thực chạy TS-03 — 19/11/2026, 13:08–13:12 (UTC+7)

- Điều học được: [ĐÃ XÁC MINH] Màn tạo có Kim/Mộc/Thủy/Hỏa/Thổ; ảnh sau tap(960,855) Thổ cho thấy hình mẫu đổi. [CHƯA XÁC MINH] Hệ đã lưu/gia nhập phái. Thổ lấy từ bảng Võ Đang/Côn Lôn tại KIEN-THUC/mon-phai-ngu-hanh/README.md:17–18, chưa đối chiếu lại dữ liệu game gốc.
- Bằng chứng: [trước chọn](../dang-nhap/TS-03-L3-1305/08.jpg), [sau chọn](../dang-nhap/TS-03-L3-1305/10.jpg), [cảnh báo](../dang-nhap/TS-03-L3-1305/11.jpg); ../dang-nhap/TS-03-L3-1305/ket-qua.jsonl:8–11; [ID/băm](../dang-nhap/TS-03-L3-1305/bang-chung.tsv).
- Điều chưa rõ: Ảnh 08 tên là placeholder, ảnh 10 T36nv2, ảnh 11 Tsbaone/cảnh báo; worker chưa gửi text/key hoặc tap Xác định. [GIẢ THUYẾT] Có tác động ngoài chuỗi lệnh, chưa xác minh nguồn/chưa tái hiện có kiểm soát.
- Cách dùng lại: Xác nhận một đầu điều khiển rồi chụp trạng thái mới; giữ T36nv1, so danh sách trước/sau. Không nhận tạo đạt từ việc ô tên có chữ. Chuỗi lệnh worker chưa tạo/xóa nhân vật.
- Ngày, tiểu yêu: 19/11/2026 — TS-03. [Quan sát cần kiểm lại](../../LOI/tao-nhan-vat/2026-11-19-ten-doi-ngoai-chuoi-lenh.md).
