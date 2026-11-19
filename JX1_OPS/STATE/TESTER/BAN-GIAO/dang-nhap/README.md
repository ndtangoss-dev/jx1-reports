# BÀN GIAO — dang-nhap
(Chỉ tiểu yêu giữ mục này ghi. Mỗi lần dừng/đổi tiểu yêu: cập nhật.)
- Bước hiện tại: TS-03 dừng trước khi gửi lệnh kiểm Cầu Nối cho `T36-tester01`.
- Đã thử (kèm ảnh/log): Kiểm tra hai thư mục hòm đều hiện diện. Chưa gửi lệnh do hòm nằm ngoài vùng ghi; chưa có ảnh/log của TS-03.
- Việc dở: Chụp màn hình, chạm một nút vô hại và xác nhận đăng nhập trên phiên được giao. Ghi nhận đăng nhập ở `JX1_OPS/STATE/TESTER/TRANG-THAI.md:24` thuộc lượt trước của Sonnet.
- Bước kế: Khi môi trường cho phép, gửi `screenshot`, kiểm ảnh và kết quả, rồi `tap` nút vô hại. Kiểm đăng nhập bằng thông tin đã lưu trong ứng dụng sau khi cầu trả `ok:true` (`JX1_OPS/STATE/TESTER/CAU-NOI.md:30`).
- Cập nhật lúc: 19/11/2026 — TS-03, BLOCKED. [Báo cáo](../../../../REPORTS/TS-03.md).

## Cập nhật tiếp tục — 19/11/2026, sau ảnh 11:59:18 (UTC+7)

- Bước hiện tại: PARTIAL — kiểm cầu đạt; dừng ở form đăng nhập đang lưu `testa`, chưa đăng nhập `tester01`. Mục BLOCKED ở trên là lịch sử lượt trước, giữ nguyên.
- Đã thử (kèm ảnh/log): 7 lệnh `tap` và 7 lệnh `screenshot`, cả 14 trả `ok:true`. Đã thấy Hành trang mở sau chạm (680,52); đã về form bằng Cài đặt → Đăng xuất → Bắt đầu trò chơi → chọn máy chủ. [Bằng chứng](../../KIEN-THUC/dang-nhap/TS-03/bang-chung.tsv), [kết quả cầu](../../KIEN-THUC/dang-nhap/TS-03/ket-qua.jsonl).
- Điểm chặn: tên lưu khác tài khoản được giao; một lần chạm mũi tên chưa hiện lựa chọn khác. [Ảnh cuối đã che ô mật khẩu](../../KIEN-THUC/dang-nhap/TS-03/07-sau-cham-mui-ten.jpg), [ghi nhận LOI-dang-nhap-001](../../LOI/dang-nhap/2026-11-19-tai-khoan-luu-khong-khop.md).
- Việc dở: Tổng quản chuẩn bị sẵn đúng `tester01` trong app. Worker chưa bấm Đăng nhập, chưa nhập hay đổi thông tin xác thực, chưa xác minh chủ tài khoản của nhân vật có sẵn.
- Bước kế: Chụp lại form, xác nhận hiện `tester01`, dùng thông tin đã lưu để đăng nhập; sau đó mới kiểm tạo nhân vật. Dùng hòm `.ldbridge` trong worktree theo task; đường hòm ở PHAN-CONG đang là thông tin cũ, không dùng thay cho task.
- Trạng thái phiên khi dừng: đang ở form đăng nhập; phiên game ban đầu đã đăng xuất trong quá trình kiểm. Không chạy `start`, `stop`, `dnat`, adb hay exe; không thay mạng/VM.
