# A-01 Bản đồ tiến trình server

**TÓM TẮT**
1. Chuỗi khởi động bắt buộc: SQL Server (1433) → `Sword3PaySys` (5002) → `Goddess` (5001, bấm Start) → `S3Relay` (5003-5005, 7776; đăng nhập root) → `Bishop` (56722 cho client, 56732 cho game server; Login rồi Startup) → `gs001` (51189).
2. Thao tác tay trong exe có giao diện (Goddess Start, S3Relay root, Bishop Login/Startup) đã được script hóa bằng task `JX-ChainUp` trong VM thử; cần phiên desktop mu1 đang đăng nhập.
3. `gs001` nạp ~7 phút (~805 dòng log); không được mở kết nối tới 51189 trong lúc nạp (crash do con trỏ NULL, báo cáo 29).
4. Cổng 7777 (`RELAY_ROUTE_PORT`) chưa có tiến trình nghe, chưa rõ ảnh hưởng.
5. Nhãn tin cậy: toàn bộ bảng dưới là **tổng hợp từ `docs-analysis/BAI_HOC.md` và `CLAUDE.md`**, mỗi dòng đã được kiểm lúc dựng Main VM; **chưa kiểm lại trên VM thử trong A-01** (VM thử đang treo, xem TRANG-THAI 0-07).

## Tiến trình và cổng

| Thứ tự | Tiến trình | Cổng | Vai trò | Ghi chú vận hành | Log |
|---|---|---|---|---|---|
| 1 | SQL Server (`SQLEXPRESS`) | 1433 | DB `account` | Chỉ nội bộ VM | SQL |
| 2 | `Sword3PaySys` | 5002 | Tài khoản, đăng nhập dịch vụ | Tài khoản chơi cần `Account_Info` và `Account_Habitus` còn hạn | `gw\payserver_log` |
| 3 | `Goddess` | 5001 | Lưu nhân vật (`Goddess/DBTable.cpp`, `IDBRoleServer.cpp`) | Phải bấm Start; tiêu đề `[Enable DB]` là đã chạy | `gw\goddes_log` |
| 4 | `S3Relay` | 5003, 5004, 5005, 7776 | Transfer, Chat, Tong (bang hội, bạn bè); 7776 = `RELAY_SIBLING_PORT` | Hộp thoại `login root` | `gw\relay_log` |
| 5 | `Bishop` | 56722 (client), 56732 (game server) | Cổng vào, định tuyến (`Bishop/GameServer.cpp`, `SmartClient.cpp`, `Intercessor.cpp`) | Login rồi Startup; 56722 mã cứng trong client | `gw\bishop_log` |
| 6 | `gs001` | 51189 (`gs002` trở đi: cổng kế tiếp) | Game server; kết nối tới 5001, 5003, 5004, 5005, 56732 | Địa chỉ gửi client lấy từ `gs001_cfg.ini` `[GameServer] Ip` (phải chứa `localIp`) | `gs\gameser_log` + console |

## File cấu hình chính
`gs001_cfg.ini` (cổng relay, Ip), `gs\Settings\MapList.ini`, `gs\maps\WorldSet_gs001.ini`, `Resources/package.ini` phía client (địa chỉ tải), `data/paklist.ini`.

## Bẫy đã biết
- Hộp thoại tường lửa chiếm focus khi exe mở cổng: tạo luật Inbound Block theo exe trước khi chạy.
- Nút không bấm được khi cửa sổ không ở phía trước: đưa cửa sổ lên (Alt+Tab hoặc `AppActivate`) rồi gửi Space.
- Luật `portproxy` còn không có nghĩa là cổng đang nghe: kiểm `netstat -ano | Select-String LISTENING`.
- 28 bản đồ của `gs001` không nạp được vì thiếu `.wor` trong PAK server.

## Chưa kiểm
- Kiểm lại cổng và tiến trình trên VM thử sau khi nó hoạt động lại (`jx_env_up.ps1` in danh sách cổng đang nghe).
- Ảnh hưởng của cổng 7777; mã nguồn server có khớp exe đang chạy hay không.
