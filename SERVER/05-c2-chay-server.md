# C2 – Chạy server trong VM

## TÓM TẮT 5 DÒNG
1. Cả 5 exe đã chạy trong VM: `Sword3PaySys`, `Goddess`, `S3Relay`, `Bishop`, `gs001`. 8 cổng cần kiểm tra đều đang nghe.
2. `gs001` báo `Server start succeeded`, nối đủ Database, Transfer, Chat, Tong, Gateway. Online = 0.
3. Lỗi của `gs001`: 28/800 bản đồ không nạp được, 1 script lỗi tên file, và đường dẫn log cứng `E:/_bin_v2_/gs/Logs/`.
4. Không exe JX nào bị ghi nhận cố ra Internet trong các lần đo bằng audit. Defender: 0 phát hiện.
5. Từ máy thật đã kết nối được 56722 và 51189; cổng nội bộ vẫn bị chặn. Chưa thử đăng nhập bằng client, chưa mở cho điện thoại.

Cần tôi quyết định: có

## Đã làm
| Exe | Snapshot trước khi chạy | Thao tác thêm | Kết quả |
|---|---|---|---|
| `gw\Sword3PaySys.exe` | `c2-truoc-chay-exe` | Đóng hộp thoại tường lửa, không cho phép | Nghe 5002 |
| `gw\Goddess.exe` | `c2-truoc-goddess` | Bấm **Start** | Nghe 5001 |
| `gw\S3Relay.exe` | `c2-truoc-s3relay` | Điền `<service-account>` vào **login root** | Nghe 5003, 5004, 5005, 7776 |
| `gw\Bishop.exe` | `c2-truoc-bishop` | Điền `<service-account>` vào **Login**, bấm **Startup** | Nghe 56722, 56732 |
| `gs\gs001.exe` | `c2-truoc-gs001` | Không | Nghe 51189 |

Mỗi exe được chủ máy duyệt riêng trước khi chạy. Nhập `<service-account>` được duyệt riêng cho `S3Relay` và cho `Bishop`.

## Bằng chứng
- `Get-NetTCPConnection -State Listen`: 5001, 5002, 5003, 5004, 5005, 51189, 56722, 56732.
- `gs001` Established tới 5001, 5003, 5004, 5005, 56732. Console: `Server start succeeded`, `[Online= 0]`.
- `Bishop` Established tới 5001 và 5002; giao diện `Bishop - [enable]`, danh sách GameServer có <LAN-IP>.
- `S3Relay`: `Initialize OK`, `gateway client create: <LAN-IP>` sau khi `Bishop` chạy.
- `Sword3PaySys`: 1000 phiên `<sql-admin>` vào DB `account`, không có dòng `Login failed` trong errorlog SQL.
- Sự kiện 5157 (audit bật lúc 09:47): không có dòng nào của exe JX. Các tiến trình bị chặn: `onedrive.exe`, `svchost.exe`, `msmpeng.exe`, `System`.
- `Get-MpThreatDetection`: 0.

## Lỗi và điểm chưa rõ
1. **28 bản đồ không nạp được** (`NpcNum:-1`), ID: 63, 64, 88, 89, 95, 96, 97, 98, 107, 108, 133, 134, 156, 157, 159, 191, 192, 334, 335, 356, 592, 598, 599, 600, 601, 602, 603, 604. Nạp được 772 bản đồ, 75 053 NPC. Chưa rõ nguyên nhân.
2. **Một script không nạp được**: tên file có ký tự `?` trong thư mục script. Thư mục tiếng Trung lưu dưới dạng GBK; nghi một ký tự trong tên bị hỏng khi sao chép. Chưa xác minh.
3. **Đường dẫn cứng**: `Failed to open file: E:/_bin_v2_/gs/Logs/script_errors.txt`. VM không có ổ E:, nên không ghi được ra ngoài thư mục.
4. **S3Relay root 7777**: không có tiến trình nào nghe. Chưa rõ có ảnh hưởng không. Không chạy `S3RelayServer.exe` vì chưa được duyệt.
5. **Trước lúc bật audit (09:47)** có các gói ra Internet bị chặn, chưa truy được tiến trình. Đích là các dải IP của Microsoft và mạng nhà cung cấp; `Sword3PaySys` lúc đó chỉ có kết nối tới 1433.

## Kết quả tìm nguyên nhân (chỉ đọc, không sửa gì)
- **28 bản đồ: thiếu file `.wor` trong PAK của server**, không phải lỗi mã hóa tên. `LoadMapS` trả `-1` khi không mở được `.wor` (`KSubWorld.cpp:925-929`). Tính ID băm theo `g_FileName2Id` rồi dò chỉ mục `maps.pak`, `maps01.pak`: 772/772 bản đồ nạp được có trong PAK, 0/28 bản đồ lỗi có trong PAK.
- Trong 40 PAK của client (`data_cdn\data`): 5/28 có mặt (ID 107, 108, 156, 157 ở `map.pak`; 356 ở `image2.pak`). 23 bản đồ còn lại không có ở đâu. Đối chứng: 50/50 bản đồ nạp được có trong PAK client.
- Theo tên trong `MapList.ini`, nhóm lỗi gồm phòng trong môn phái, khách điếm tân thủ, bản đồ bang hội, đấu trường. Vào các bản đồ này có thể lỗi; chưa thử.
- **Script lỗi**: bản gốc đã có hai file `...5石?对话.lua` khác nhau ở một ký tự, `U+0086` (187 byte) và `U+2020` (126 byte), nội dung khác nhau. Không phải do sao chép vào VM. Chưa xác định vì sao exe báo lỗi nạp (tên file hay cú pháp Lua).
- **Đường dẫn `E:`**: ghi cứng trong mã nguồn (`KPlayer.cpp:8171`, `KObj.cpp:436`), chỉ dùng khi một script lỗi. VM không có ổ E:, nên chỉ in `Failed to open file`. Vô hại.

## Mở cổng cho máy thật
- Snapshot: `c2-truoc-mo-lan` (UUID <uuid>).
- Theo quyết định của chủ máy: chỉ cho `<LAN-IP>` vào TCP 56722 (`Bishop`) và 51189 (`gs001`).
- Từ máy thật: 56722 và 51189 mở. 56732, 5001, 5002, 5003, 1433, 7776 bị chặn.

## Hiện trạng để lại trong VM
- 5 exe đang chạy trong phiên desktop của `<vm-user>`, khởi động bằng scheduled task `JX-Goddess`, `JX-S3Relay`, `JX-Bishop`, `JX-gs001`. `Sword3PaySys` khởi động từ cửa sổ PowerShell.
- Task phụ `JX-UI` và các script trong `C:\JX\sql` (`ui*.ps1`, `console.ps1`), không chứa mật khẩu.
- Luật tường lửa: `JX block ra ngoai LAN`, `JX no-in Goddess`, `JX no-in S3Relay`, `JX in Bishop 56722 may that`, `JX in gs001 51189 may that`; và 2 luật Block `sword3paysys` do hộp thoại tường lửa tạo.
- Bật ghi log gói bị chặn và audit Filtering Platform Connection (failure).

## Bước kế
Chờ chủ máy quyết định. Phần CDN, `package.ini`, APK để sau khi chủ máy duyệt báo cáo này.
