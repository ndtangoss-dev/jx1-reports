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

## Luật tên vai (B, 19/11 18:20, đã đối chiếu mã)
- Client `KuiNewPlayer.cpp:558-560`: 6..24 byte; máy chủ Bishop `GamePlayer.cpp:1942-1944`: 6..16 byte → tên hợp lệ cả hai phía: 6..16 byte, chữ cái ASCII thuần (không số, không khoảng trắng, không ký hiệu). Ghi chú A "12–24" chưa khớp mã; tên 13 chữ `tsvkbonenamea` đã tạo được trên Test-36 (16:51).
- Tên không hề tồn tại trong kho vai (vm_chay.py ten-co): Tsbaone, Tsalphaone, T36nv2, Cctesterone → các lần tạo trước đều chưa tới máy chủ (client im lặng).

## TẠO VAI THÀNH CÔNG (B, 19/11 16:58 giờ máy) — luồng đúng, có bước THÔN
1. Menu đầu: "Bắt đầu trò chơi" (960,588) → chọn máy chủ "JX1 Mobile TEST" (498,298) → form có tài khoản đã lưu `testa` + mật khẩu đã lưu: bấm "Đăng nhập" (840,772) KHÔNG cần gõ mật khẩu (~12 giây tới danh sách vai).
2. Danh sách vai: "Tạo nhân vật mới" (857,1016).
3. **Hộp "Chọn Tân thủ thôn"** hiện ra: chạm "Ba Lăng huyện" (1322,246) rồi "Xác nhận" (1265,736). BỎ BƯỚC NÀY thì CreateRole thoát im lặng (region ≤ 0, KuiNewPlayer.cpp:616-660) — đây là nguyên nhân "bấm Xác định không phản ứng" của các lần trước.
4. Chọn hệ (Mộc 960,565), chạm ô tên (870,1020) hai lần, gõ tên, "Xác định" (1070,1018) → vào game (loading).
5. LỖI GÕ: lệnh `text` giao chữ chậm/lộn xộn (gõ "Tsmocnamebravo" ra "TsmocnamebravTsm"); ô tên chỉ hiện vài chữ cũ. Chia nhỏ, chờ lâu, và đối chiếu bằng `vm_chay.py ten-co`.
