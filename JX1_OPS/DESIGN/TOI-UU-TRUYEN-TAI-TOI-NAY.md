# Tối ưu truyền tải — kế hoạch tối nay (#252 + #253, 19/11/2026)

Phạm vi: Test-36 + LD. Không Server D, không sửa mã hiệu ứng vũ khí (Q-52), không APK cho chủ. Mọi thay đổi có công tắc, đo trước/sau cùng B (`A-B.md`).

## Đã kiểm trong lượt này
- `tcp_forwarder.py` (máy thật, đường Tailscale): dùng asyncio; asyncio đặt TCP_NODELAY mặc định, đọc 64 KB, có `drain` → [CHƯA ĐO] nhưng không thấy lỗi đệm. Có sẵn số đo `gap_max`, `drain_max` trong log → dùng làm số đo đường dài.
- `gs001_cfg.ini` Test-36 `[GameServer]`: chỉ có localIp/Ip/Port/ClientKey; **không có khóa nhịp**. Kiểm lại mã: `KSOServer.cpp:90` là `#define GAME_FPS 18` cứng, grep `LogicFps` không ra → **không có đòn bẩy cấu hình cho nhịp**; đổi nhịp phải sửa mã + dựng lại gs001 (Test-36 thôi).
- Số gốc P-02 (1 bot): tick phía bot 32,9 ms TB, p95 109 ms, max 125 ms; rx ~216 kbps.

## Chỗ nghẽn, xếp theo tác dụng / rủi ro
| # | Chỗ nghẽn | Đường | Cách thử | Rủi ro | Trạng thái |
|---|---|---|---|---|---|
| 1 | Gom gói chỉ xả ở vòng lẻ (18 Hz → pha trễ TB ~28 ms) | server-client | xả mỗi vòng (H-13) | vừa (mã server) | chưa đo |
| 2 | Nhịp logic 18 Hz (hằng số cứng) | server-client | sửa `GAME_FPS` + dựng gs001 cho Test-36 | vừa (mã) | cần dựng lại exe |
| 3 | Khựng khi nạp spr/map/âm thanh đổi cảnh | dữ liệu | khảo sát: đọc đồng bộ ở luồng chính? bộ đệm? | cần khảo sát | giao tiểu yêu |
| 4 | Nhiều thực thể: gói + vẽ | cả hai | bộ lọc hiển thị B-02 (`visibility.ini`, mặc định tắt) | thấp (cờ) | build OK, chưa chạy |
| 5 | Client vẽ theo bước 18 Hz, không nội suy | client | đã có kế hoạch TOI-UU-120FPS (tích lũy, nội suy) | cao (mã) | để sau, đo trước |
| 6 | Đồng bộ HP/số sát thương lẻ tẻ (`s2c_syncnpcmin`) | server-client | khảo sát tần suất gói | thấp | giao tiểu yêu |
| 7 | Đường dài: Tailscale ~150 ms + forwarder | mạng | đọc log DRAIN-CHAM | ngoài tầm | chỉ đo |

## Thứ tự làm
1. Đo gốc: 1 bot rồi 10 bot (`bench/bot_ladder.py`), cộng log forwarder; B lo đo CPU gs001 (B-04a). Lưu bảng "trước".
2. Cờ trước: #4 (B-02 `visibility.ini`) trên bản LD thử; rồi #1/#2 là sửa mã server có công tắc, chỉ exe Test-36, có `.bak`, hoàn tác nếu tệ hơn.
3. Bật #4 trên bản thử của LD, đo.
4. #1 chỉ khi #2 chưa đủ.
5. #3/#5/#6: khảo sát (tiểu yêu), chưa sửa mã.

## Tiêu chí
Tick bot p95 giảm, max giảm, không tăng rx quá 20%, không rớt kết nối, chủ cảm nhận mượt khi chạy/đánh. Kết quả ghi vào `BAO-CAO-CHU.md` (bảng trước/sau + hướng dẫn 5 phút).
