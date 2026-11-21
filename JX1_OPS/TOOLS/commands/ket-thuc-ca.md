---
description: Dừng ca làm việc an toàn để chủ dự án tắt máy
---
Chủ dự án sắp tắt máy. Làm đúng các bước "/ket-thuc-ca" trong `JX1_OPS/QUY-TAC-VAN-HANH.md` mục 7:

Theo `JX1_OPS/STATE/QUY-TRINH-TAT-BAT-MAY.md` phần I ("tắt máy" = DỪNG HẾT, kể cả Tổng quản và worker):

1. Không giao việc mới (không đặt task `ready` mới).
2. Chủ thoát nhân vật; A dừng gs001 rồi VM Test-36 đúng thứ tự (Online=0 trước), không cắt ngang. Main VM: không đụng.
3. **TẮT TỔNG QUẢN TRƯỚC**: `schtasks /End /TN JX-TongQuan` rồi `schtasks /Change /TN JX-TongQuan /DISABLE`; kiểm `Status: Disabled`; ghi giờ vào `TRANG-THAI.md`.
4. Liệt kê worker: `schtasks /Query /FO CSV /NH` lọc `JX-codex-*` đang `Running` + `STATE/TIEU-YEU.md`, `KHOA.md`; ghi `STATE/DANG-CHAY-TRUOC-TAT.md` (cả bộ canh LD, cầu LD, người gác, Bot, forwarder).
5. Dừng từng worker: chờ điểm dừng an toàn tối đa 10 phút; quá thì `schtasks /End /TN JX-codex-<ID>`, commit phần dở `WIP` trên `task/<ID>`, ghi "Bước tiếp theo", đặt task về `ready`, gỡ khóa `KHOA.md`.
6. Dừng tiến trình nền khác theo danh sách đã ghi (ghi trước khi dừng).
7. Cập nhật `STATE/TRANG-THAI.md`, `BAN-GIAO.md`/`BAN-GIAO-B.md`, báo cáo ngày `REPORTS/daily/YYYY-MM-DD.md` (7 câu); commit, đẩy `jx1-ops` và branch task; KIỂM GitHub có commit.
8. Chỉ khi đủ bốn điều mới nói "Đã lưu. Có thể tắt máy.": (a) VM/gs001 đã tắt, (b) `JX-TongQuan` Disabled, (c) không còn `JX-codex-*` Running, (d) GitHub có commit cuối. Thiếu điều nào thì nói rõ thiếu gì và KHÔNG nói tắt máy được. Trả lời chủ tối đa 6 dòng.

$ARGUMENTS
