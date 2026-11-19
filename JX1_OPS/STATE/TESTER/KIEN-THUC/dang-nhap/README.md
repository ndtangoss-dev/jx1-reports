# KIẾN THỨC: dang-nhap
## Cần làm gì (từng bước, ai đọc cũng làm lại được)
(chưa có)
## Đã biết (kèm nguồn: ảnh/log/file:dòng)
(chưa có)
## Chưa hiểu
(chưa có)

## Ghi nhận TS-03 từ tài liệu

- Điều học được: Hướng dẫn Cầu Nối yêu cầu chụp màn hình và chạm một nút vô hại trước khi bắt đầu kiểm đăng nhập.
- Bằng chứng: `JX1_OPS/STATE/TESTER/CAU-NOI.md:30` (đã đối chiếu tài liệu; CHƯA KIỂM trên phiên TS-03).
- Cách dùng lại: Gửi `screenshot`, dùng ảnh để chọn vị trí `tap` vô hại, rồi xác nhận `ok:true` trước khi kiểm đăng nhập.
- Ngày, tiểu yêu: 19/11/2026 — TS-03.

## Tiếp tục TS-03 — 19/11/2026, 11:53–11:59 (UTC+7)

- Điều học được: [ĐÃ XÁC MINH] Cầu trong worktree nhận được `screenshot` và `tap`; chạm biểu tượng túi tại (680,52) mở Hành trang. Ảnh ban đầu có nhân vật `T36nv1` cấp 1; chưa xác minh tài khoản của phiên đó.
- Bằng chứng: [ảnh trước](TS-03/01-hien-trang.jpg), [ảnh sau](TS-03/02-mo-hanh-trang.jpg), `JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03/ket-qua.jsonl:1–3`.
- Điều học được: [ĐÃ XÁC MINH] Sau khi về form đăng nhập, tên đang lưu là `testa`, khác `tester01` được giao. Một lần chạm mũi tên (1166,565) chưa hiện danh sách tài khoản; không kết luận app không hỗ trợ danh sách.
- Bằng chứng: [form đã che ô mật khẩu](TS-03/06-tai-khoan-khong-khop.jpg), [sau chạm mũi tên](TS-03/07-sau-cham-mui-ten.jpg), `JX1_OPS/STATE/TESTER/KIEN-THUC/dang-nhap/TS-03/ket-qua.jsonl:11–14`.
- Cách dùng lại: Kiểm đúng tên tài khoản trên form trước khi bấm Đăng nhập. Đường vừa quan sát: Cài đặt (1193,52) → Đăng xuất (1176,955) → Bắt đầu trò chơi (960,588) → máy chủ (500,298). Chỉ dùng trong phiên Test-36 được giao, kiểm ảnh ở mỗi màn.
- Ngày, tiểu yêu: 19/11/2026 — TS-03. Chưa bấm Đăng nhập; không nhập, lấy hay suy đoán mật khẩu. Điểm dừng ở form đang lưu `testa`; cần Tổng quản lưu sẵn đúng `tester01` trong ứng dụng.

## Sonnet kiểm qua cầu ld_bridge (19/11 13:00-13:20, tester01 emulator-5558) [ĐÃ KIỂM]
- Đăng nhập testa → danh sách nhân vật (T36nv1 Nam lv1 Kim) → Tạo mới → chọn làng Ba Lăng huyện → màn "Lựa chọn hệ phái" hiện được.
- Tật giao diện: chạm đầu tiên vào nút/ô sau khi gõ chữ chỉ bỏ tiêu điểm ô nhập; phải chạm LẦN 2 mới có tác dụng. Đăng nhập kẹt 4 lần → stop/start ứng dụng.
- Xóa ô tên: chạm ô 2 lần rồi DEL nhiều lần (DEL khi ô chưa có tiêu điểm không làm gì).
- Tạo nhân vật: tên "T36nv2" và cả "Tsbaone" (chỉ chữ cái) đều bị báo "Tên nhân vật chứa ký tự đặc biệt, hoặc các ký tự không được phép!" dù Bishop (PlayerCreator.cpp:440) cho phép 0-9A-Za-z. [CHƯA RÕ NGUYÊN NHÂN] nghi kiểm ở client hoặc m_UTF8Code/m_InvalidName; đã thử 2 tên, dừng theo luật 3 lần. Bot tạo vai bằng bot_tao_role.py vẫn được.
