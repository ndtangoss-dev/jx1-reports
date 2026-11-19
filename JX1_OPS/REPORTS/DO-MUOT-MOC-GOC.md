# Mốc gốc độ mượt (B, 19/11 ~18:15) — Test-36, CHƯA có tải Bot

## TÓM TẮT 5 DÒNG
1. PARTIAL: mốc gốc lúc rỗi (0 Bot, 1 LD) đã đo; mốc 5/10/20 Bot CHƯA đo vì Bot cần tài khoản test mà `vm_chay.py` chưa có lệnh tạo (xin A ở `A-B.md`).
2. Thêm lệnh đọc-chỉ `vm_chay.py do-gs [giây]`: CPU% gs001, RAM, thread, kết nối TCP, byte/giây NIC.
3. gs001 rỗi: CPU ≈ 25,9% của 4 CPU (≈ đúng 1 nhân đầy, nghi vòng lặp bận) — mốc để A so trước/sau.
4. Màn hình LD tester01 (b300): HUD hiện ping 158 ms, FPS 44; hộp "Kết nối lần thứ 83 thất bại… Đang giải kết tài khoản" (nối lại liên tục).
5. Chưa có số tick, trễ đòn→số nổi, nạp map/spr: gs log không in tick; cần B-04a (chưa chạy) hoặc A thêm log.

## Số đo (ĐÃ KIỂM = chạy thật)
| Đại lượng | Giá trị | Nguồn |
|---|---|---|
| gs001 CPU (rỗi, 13 s) | 25,9% /4 CPU | `vm_chay.py do-gs 10` |
| gs001 RAM / thread / handle | 240,6 MB / 24 / 215 | cùng lệnh |
| NIC gửi/nhận | 0 / 0 B/s | cùng lệnh |
| TCP 56722 / 51189 established | 0 / 1 | cùng lệnh |
| Ping / FPS phía LD | 158 ms / 44 | ảnh `b300.png` hòm cầu CC-01 (không đưa vào kho) |
| Nối lại | lần thứ 83 thất bại (tài khoản đang "giải kết") | ảnh b300 |

## Việc kế (để đo 5/10/20 Bot)
1. Tài khoản test Bot (A thêm `tao-tk-test`, hoặc chủ duyệt) → chạy `BOT/cli.py` 5→10→20, mỗi bậc gọi `do-gs 30` + chụp HUD ping/FPS tester01.
2. Đường dữ liệu (nạp map/spr, khựng): đo thời gian từ vào map đến hết khựng bằng ảnh HUD FPS theo mốc thời gian qua cầu; cần cổng log client (A).
3. Tick/gói/độ trễ đòn: cần `b04a_metrics.py` với nguồn tick thật (chưa có định dạng log).

## Đo lại 19:08 (sau khi gs001 nạp xong map, 0 người chơi → 1 kết nối 51189)
gs001 CPU 2,54% / 4 CPU (33 s), RAM 2145,5 MB, 24 thread, 199 handle, NIC 0. So với mốc 18:xx (CPU 25,9%, 240 MB): mốc cũ là gs001 vừa khởi động chưa nạp hết, không phải nhàn rỗi; mốc nhàn rỗi đúng là ~2,5%. (B)

## Mốc RỖI 19/11 19:44–19:47 (gs001, 0 người chơi, 5 lần × 30 s) — #B-022 mục 1
| Giờ | CPU % (4 CPU) | RAM WS (MB) | thread | handle | NIC gửi/nhận | TCP 56722/51189 |
|---|---|---|---|---|---|---|
| 19:44:02 | 0,19 | 30,9 | 24 | 202 | 0/0 | 0/0 |
| 19:44:49 | 0,19 | 30,9 | 24 | 202 | 0/0 | 0/0 |
| 19:45:34 | 0,16 | 30,3 | 24 | 202 | 0/0 | 0/0 |
| 19:46:21 | 0,30 | 30,3 | 24 | 202 | 0/0 | 0/0 |
| 19:47:08 | 0,22 | 30,4 | 24 | 202 | 0/0 | 0/0 |
Rỗi thật: CPU ~0,2%, ổn định. RAM "working set" chỉ 30 MB vì Windows đã đẩy trang ra (lúc 19:08 là 2145 MB khi mới nạp map): khi chủ vào, working set sẽ tăng lại → chính là độ khựng lần đầu nạp trang, đo `do-gs` lúc chủ vào để thấy. SvrFPS chưa đọc được (console gs001 do A giữ). (B)

## Kịch bản Bot 5/10/20 (soạn sẵn, CHƯA thả — chờ lệnh Chat, không thả khi chủ đang chơi)
1. Tạo 20 tk mẫu: `vm_chay.py tao-tk-test tkbotmau01 … tkbotmau20` (mật khẩu ra %LOCALAPPDATA%\jx1-secrets, không in).
2. Mỗi tk một vai: `bot_tao_role.py tkbotmauNN <tên chữ cái 6–16> 1 0 53` (script nạp mật khẩu từ tệp; người chạy là A hoặc người được chủ giao).
3. Bậc 5 → 10 → 20 Bot, mỗi bậc 3 phút: Bot vào map cùng điểm chủ đứng, đi lại; trong lúc đó `vm_chay.py do-gs 30` ×6, ghi CPU/RAM/NIC/TCP và hỏi chủ ba câu: khựng khi vào map? khi đánh? khi đông người?
4. So mỗi bậc với mốc rỗi ở trên; dừng Bot, đợi CPU về ~0,2% rồi qua bậc kế.
5. Hoàn tác: `xoa-tk-test` các tk tkbotmau*.
