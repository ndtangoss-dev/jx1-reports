# Nút giao diện: đăng nhập → tạo nhân vật (màn 1920×1080 của LD tester01) — Sonnet kiểm qua cầu 19/11
Toạ độ là pixel ảnh chụp từ cầu (cùng hệ với lệnh `tap`). Nhãn: [ĐÃ KIỂM] thấy ảnh thật; [CHƯA KIỂM] chưa thử.

| Màn | Nút / ô | Toạ độ | Bấm ra gì |
|---|---|---|---|
| Đăng nhập | ô tài khoản / mật khẩu | xem ảnh s1.png (`D:\JX-ldbridge\t01\ket-qua`) | tiêu điểm vào ô; gõ bằng lệnh `text` ASCII. KHÔNG nhập mật khẩu hộ: lấy từ chủ |
| Đăng nhập | nút đăng nhập | (960,588) | sang menu chính [ĐÃ KIỂM, cần chạm 2 lần] |
| Menu chính | chọn máy chủ | ảnh d2.png | danh sách máy chủ |
| Danh sách nhân vật | T36nv1 Nam lv1 Kim; "Tạo mới" | ảnh e3.png | sang chọn làng |
| Chọn làng | Ba Lăng huyện | ảnh f2.png | sang "Lựa chọn hệ phái" |
| Lựa chọn hệ phái | Kim (960,469) · Mộc (960,565) · Thủy (960,661) · Hỏa (960,759) · Thổ (960,857) | như tọa độ | chọn xong, mô hình nhân vật đổi (ảnh p4.png: hình Mộc) [ĐÃ KIỂM] |
| Tạo nhân vật (đáy) | ô "Tên nhân vật" | (870,1020) | nhập tên |
| Tạo nhân vật (đáy) | Xác định | (1070,1018) | gửi tạo vai |
| Tạo nhân vật (đáy) | Hủy bỏ | (1237,1018) | quay lại [CHƯA KIỂM] |

## Tật đã biết [ĐÃ KIỂM]
1. Chạm đầu tiên vào nút/ô sau khi gõ chỉ bỏ tiêu điểm; phải chạm LẦN 2.
2. Xóa ô tên: chạm ô 2 lần rồi DEL nhiều lần; DEL khi chưa có tiêu điểm vô tác dụng.
3. Đăng nhập kẹt (nút không phản hồi 4 lần): `stop` rồi `start` ứng dụng.
4. Tạo vai với `T36nv2` và `Tsbaone` đều báo "Tên nhân vật chứa ký tự đặc biệt, hoặc các ký tự không được phép!" (cửa sổ đè giữa màn hình). Nguyên nhân CHƯA RÕ: Bishop `PlayerCreator.cpp:440` cho phép chữ+số; nghi bộ lọc client hoặc m_InvalidName/m_UTF8Code. Cần thử tên khác (có dấu tiếng Việt, tên ngắn hơn/dài hơn) hoặc đọc client.
5. Bot tạo vai bằng `bot_tao_role.py` qua Bishop vẫn được (không qua bộ lọc client).

## QUY TẮC TÊN NHÂN VẬT — ĐÃ ĐỌC MÃ (B, 19/11 15:40)
- Client chặn tên TRƯỚC khi gửi server: `D:\JX-source\client\Classes\gameui\KuiNewPlayer.cpp:554-604`. Độ dài `strlen` phải 6–24 byte (dòng 559); đếm ký tự trên chuỗi "check"+tên (dòng 568-591): **có chữ số (0-9), khoảng trắng hoặc ký tự ASCII không phải chữ → báo "chứa ký tự đặc biệt hoặc ký tự không được phép"** (dòng 599-604). Byte ≥0x80 (chữ có dấu/Hán) được coi hợp lệ ở bước này.
- Vì vậy `T36nv2` bị chặn do có chữ số "36", "2". KHÔNG phải lỗi game; server (`PlayerCreator.cpp:440-457`) lại cho cả số và chữ.
- Tên thử an toàn: chỉ chữ cái a-z A-Z, 6–24 ký tự, không số, không cách. Ví dụ: `Tsalphaone`, `Tsbetatwo`.
- `Tsbaone` (7 chữ, đúng luật) vẫn bị báo (TS-03 ảnh 11): CHƯA RÕ nguyên nhân. Giả thuyết: ô nhập còn sót chữ/số cũ (ảnh 10 hiện `T36nv2` sẵn) nên chuỗi thật là `T36nv2Tsbaone`, hoặc bàn phím ảo chèn ký tự. Cách kiểm: xóa sạch ô trước khi gõ (giữ nút xóa/chọn tất cả), chụp ảnh ô tên TRƯỚC khi bấm tạo.
