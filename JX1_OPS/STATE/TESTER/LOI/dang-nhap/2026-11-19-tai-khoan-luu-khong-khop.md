# LOI-dang-nhap-001 — Tài khoản lưu trên form không khớp tài khoản được giao

- Mục: dang-nhap; TS-03. Ghi nhận điều kiện bàn giao, chưa kết luận lỗi mã nguồn hoặc lỗi xác thực.
- Mức độ: chặn lượt kiểm `tester01` và bước tạo nhân vật phụ thuộc.
- Các bước tái hiện:
  1. Trên phiên cầu được giao, chụp ảnh: đang có nhân vật trong game. Chạm túi (680,52), xác nhận Hành trang mở; đóng tại (1553,957).
  2. Mở Cài đặt (1193,52), chọn Đăng xuất (1176,955).
  3. Chọn Bắt đầu trò chơi (960,588), máy chủ (500,298), chụp form.
  4. Quan sát tên tài khoản; chạm mũi tên (1166,565) một lần và chụp lại. Không sửa ô tài khoản/mật khẩu, không bấm Đăng nhập.
- Kết quả thực tế: tên đang lưu là `testa`; sau một lần chạm mũi tên vẫn chưa thấy danh sách chọn `tester01`. Không suy tài khoản của phiên ban đầu từ tên nhân vật; chưa có lỗi xác thực vì chưa gửi đăng nhập.
- Kết quả mong đợi: có sẵn đúng `tester01` và thông tin xác thực tương ứng trong app như `JX1_OPS/TASKS/TS-03.md:16`; worker không nhận hay ghi mật khẩu.
- Ảnh/log: [form đã che ô mật khẩu](../../KIEN-THUC/dang-nhap/TS-03/06-tai-khoan-khong-khop.jpg), [sau chạm mũi tên](../../KIEN-THUC/dang-nhap/TS-03/07-sau-cham-mui-ten.jpg); `JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03/ket-qua.jsonl:7–14`; tọa độ và dấu thời gian trong `JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03/bang-chung.tsv:8–15`.
- Tái hiện được mấy lần / mấy: 1/1 lượt đi từ game về form; không thử lại đăng xuất, không thử đăng nhập sai và không khẳng định mũi tên hỏng.
- Tiểu yêu, LD, giờ: TS-03; đích được giao `T36-tester01`; 19/11/2026, ảnh form 11:58:34 và 11:59:18 (giờ cầu, UTC+7 theo môi trường). Chưa đối chiếu độc lập serial/đích cấu hình cầu.
- Trạng thái: mới; đã ghi vào hồ sơ bàn giao, chưa gửi Sonnet/Tổng quản qua kênh ngoài.
- Cách báo cáo/xử lý tiếp: Tổng quản chuẩn bị sẵn tài khoản `tester01` trong đúng app/LD rồi giao tiếp từ form đăng nhập. Không gửi mật khẩu qua file/chat; không tự thay thông tin xác thực hay dùng mật khẩu của tài khoản khác.
