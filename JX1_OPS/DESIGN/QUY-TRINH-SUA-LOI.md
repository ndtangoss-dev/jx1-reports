# QUY TRÌNH SỬA LỖI (để người sau không phải đọc lại mã từ đầu)

Mục đích: mọi lỗi chủ báo hoặc tự phát hiện đều đi qua cùng một đường, và để lại dấu vết đủ để AI thay thế tiếp tục ngay. Đồ thị Graphify và báo cáo cũ có sẵn chính là để tra nhanh, không đọc mã từ đầu.

## Bước 1. Ghi nhận lỗi (1 phút)
- Mở một mục trong `JX1_OPS/BUGS/BUG-<số>.md` (mẫu bên dưới). Ghi nguyên văn lời chủ, ảnh chụp (đường dẫn), bản/phiên bản đang chạy (vd A2, versionCode 19), máy (điện thoại thật / LD).

## Bước 2. TRA TRƯỚC KHI ĐỌC MÃ (bắt buộc)
1. Tra đồ thị Graphify đúng gốc (client: `graphify-out/` của client; server: của `src18`): tìm hàm/lớp liên quan (caller, callee).
2. Tra `REPORTS/` bằng từ khoá (grep) và `DESIGN/`: lỗi này đã có báo cáo nào chưa (vd lớp vẽ/hiệu ứng vũ khí: H-04, L-01, L-02, L-03; mạng: K-01, A-06; hoạt động: D-01).
3. Tra `STATE/BAI_HOC` và `BUGS/` cũ: lỗi giống thế đã gặp chưa, đã sửa thế nào.
4. Ghi vào mục "ĐÃ TRA GÌ" của bug: file đồ thị/báo cáo đã dùng, và kết quả (tìm thấy / không).
- Đồ thị có thể cũ: sau khi tra, MỞ file thật tại dòng chỉ tới để xác nhận trước khi kết luận.

## Bước 3. Tái hiện và khoanh vùng
- Tái hiện bằng cách ngắn nhất (LD hoặc máy thật); chụp trước/sau. So bản có lỗi với bản trước (A/B qua công tắc) để biết bản nào gây.
- Ghi: "gây bởi X" kèm bằng chứng (ảnh, log, số đo), không đoán.

## Bước 4. Sửa nhỏ nhất, có công tắc
- Chỉ đổi chỗ cần đổi; giữ công tắc/hoàn tác (patch hoàn tác được). Không đụng logic/server nếu lỗi là hiển thị.
- Không đổi thứ không liên quan.

## Bước 5. Kiểm
- Chạy lại đúng cảnh tái hiện; chụp sau; kiểm các hướng/trạng thái lân cận (vd 8 hướng × đứng/chạy/đánh/cưỡi).
- Đo FPS/ms nếu động tới vẽ.

## Bước 6. Để lại tri thức (làm xong mới tính là xong)
- Hoàn thành mục bug: nguyên nhân gốc, file:dòng, cách sửa, cách kiểm, ảnh trước/sau, commit/patch.
- Thêm 1–3 dòng vào `STATE/BAI_HOC` nếu lỗi có thể lặp lại.
- Nếu phát hiện chỗ trong báo cáo/đồ thị sai hoặc thiếu: sửa báo cáo (dòng "cập nhật <ngày>"), hoặc ghi vào bug để cập nhật đồ thị sau.
- Cập nhật `STATE/TRANG-THAI.md` một dòng.

## Mẫu `BUGS/BUG-<số>.md`
```
# BUG-<số> — <tên ngắn>
- Ngày/giờ, người báo (chủ/Chat/Sonnet), bản đang chạy, máy
- Lời chủ (nguyên văn) + ảnh
- ĐÃ TRA GÌ: đồ thị <file>, báo cáo <ID>..., bug cũ <số>... (kết quả)
- Tái hiện: <các bước>
- Nguyên nhân gốc: <file:dòng, bằng chứng>
- Cách sửa: <patch/commit, công tắc>
- Kiểm: <cảnh, ảnh trước/sau, FPS>
- Bài học / việc còn lại:
```
