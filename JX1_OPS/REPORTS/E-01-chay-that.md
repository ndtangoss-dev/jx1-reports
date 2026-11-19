# E-01 — Bot chạy thật trên Test-36 (#216, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] 1 Bot (tài khoản thử `botlab01`, nhân vật `BotLb02`) đăng nhập Bishop 56722 → chọn nhân vật → permit → nối gs001 51189 → nhận đồng bộ → `IN_GAME`; giữ 60 giây, thoát mã 0 (61 s). Log: `E-01-chay-that-log.txt`.
2. [ĐÃ KIỂM] Gửi lệnh `--run` và `--skill` sau khi vào game, giữ 20 s, thoát 0 (`E-01-chay-that-log2.txt`). **Hiệu ứng của lệnh (nhân vật có thật sự đi/đánh) CHƯA KIỂM**: chưa có quan sát phía server.
3. Khóa client chỉ truyền qua biến môi trường `JX_BOT_CLIENT_KEY` (nguồn giá trị: `gs001_cfg.ini` mục `[GameServer]` khóa `ClientKey` trên Test-36, và hằng `curMobileKey` ở `KCore.cpp:62`); mật khẩu tài khoản thử chỉ ở tệp tạm ngoài kho. Không có bí mật trong kho.
4. Sửa Bot để khớp exe thật (bảng dưới); test đơn vị 79/79 OK: `python -X utf8 -m unittest discover -s JX1_OPS/BOT -p "test_*.py"`.
5. Cần tôi quyết định: không.

## Khác biệt giữa nguồn server và exe thật (bằng chứng: frame thật, 19/11)
| Mục | Nguồn/bảng cũ | Exe gs001 thật | Cách xử lý |
|---|---|---|---|
| Permit trả IP | IP VM | IP công khai gs (cfg `Ip`) | Bot luôn nối vào VM thử; vẫn chặn khi permit trỏ Main VM |
| ID 70 (CURPLAYER_NORMAL) | 55 byte (int64) | 31 byte (int32) | `LIVE_ALT_SIZES`, ưu tiên size nhỏ, kiểm biên record kế |
| ID 77 (NPC_NORMAL) | 227 | 223 | như trên; chỉ tin id, x, y |
| ID 220 | không có | 9 byte (REF_ITEM_SYNC) | thêm vào `CLIENT_FIXED_SIZES` [CHƯA KIỂM đủ] |
| ID 250–254 (extend) | không có | biến độ dài 1+WORD (`KProtocol.cpp:179-183`), đuôi frame có rác bộ nhớ | tách như biến; sau record extend, ID lạ ở đuôi bị bỏ như client thật (`KgameWorld.cpp:5134`) |
| 68 ID S2C khác | thiếu | kích thước suy từ `KProtocol.cpp`/`KProtocol.h` | `CLIENT_FIXED_SIZES`; bảng cũ thắng khi trùng |

## Việc phụ đã làm
- `JX1_OPS/TOOLS/bot_tao_role.py`: tạo nhân vật qua Bishop (mật khẩu từ `JX_BOT_PASSWORD`). Bản đồ khởi đầu nhân vật mới lấy từ `settings\player\revivalid.ini`, chỉ có `native_place` 53 hoặc 54 (1 không có map hồi sinh, Bishop không trả lời).
- Luật tường lửa tạm `JX1-AUTO-T36-56722-51189-host` (chỉ cho 192.168.56.101) cần gỡ khi xong.

## Còn lại [CHƯA KIỂM]
- Hành vi gameplay (đi/đánh có hiệu lực không), nhiều Bot, các ID chưa suy ra kích thước (99, 100, 102, 106, 134, 179, 180, 183, 187, 190, 208, 209).
- Bảng client lệch 1 ở đuôi (217–221) so với enum; 220 lấy theo `REF_ITEM_SYNC`.
