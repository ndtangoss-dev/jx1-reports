# Dọn dữ liệu thật trong VM và danh sách thay đổi Tailscale

## TÓM TẮT 5 DÒNG
1. Đã xóa 2 dòng `Account_History`, 1522 file log cũ, `account.sql` trong VM. Server vẫn chạy đủ 5 exe, đủ 8 cổng.
2. `roledb` chưa thay: `Goddess` đang giữ file, phải tắt và chạy lại nhiều exe, cần duyệt.
3. Mã nguồn cho thấy `Goddess` tự tạo `roledb` rỗng khi file không có, không cần cấu trúc sẵn.
4. Phía server chỉ cần đổi `gs\gs001_cfg.ini`, 2 khóa. `Bishop` không kiểm tra `gs` theo IP nên không cần đổi thêm.
5. File client cho Tailscale đã sinh, `pak_verify` DAT. Chưa sửa cấu hình, chưa khởi động lại, chưa mở cổng.

Cần tôi quyết định: có

## Đã làm
- Snapshot: `truoc-don-du-lieu-that` (UUID <uuid>).
- `DELETE FROM Account_History`: 2 dòng.
- Xóa file log không nằm trong thư mục `2026_11_10`, ở `gw\payserver_log`, `goddes_log`, `relay_log`, `relayserver_log`, `bishop_log`, `gs\gameser_log`, `gs\Logs`: 1522 file, 0 lỗi. Giữ log hôm nay vì exe đang ghi.
- Xóa `C:\JX\ServerNew\_bin_v2_\account.sql`.
- Sinh file trong `docs-analysis\out\tailscale\` (không commit).

## Bằng chứng
- `Account_History=0`, `Account_Info=1`.
- 5 exe `responding=True`. Cổng 5001, 5002, 5003, 5004, 5005, 51189, 56722, 56732 đang nghe.
- `gs001` Established tới 5001, 5003, 5004, 5005, 56732.
- `simply_crypt dec` trên `FsjxClient.ini` và `package.ini` ra đúng địa chỉ Tailscale máy thật. `pak_verify: KET QUA: DAT`.

## roledb (chưa thực hiện)
- `DBTable.cpp:40`: môi trường DB mở với `DB_CREATE`, `DB_RECOVER`.
- `DBTable.cpp:110`: bảng chính mở với `DB_CREATE`. `:125`: bảng chỉ mục mở với giá trị `DB_BTREE`, bằng số `1`, trùng `DB_CREATE`.
- `DBTable.cpp:25`: tự tạo thư mục. `IDBRoleServer.cpp:334`: tên bảng `database/roledb`.
- Kết luận từ mã nguồn: không cần cấu trúc sẵn, xóa file thì `Goddess` tạo mới. Exe có thể khác mã nguồn, chưa thử.
- Phải xóa cùng lúc `roledb`, `roledb.0`, `log.*`, vì `DB_RECOVER` đọc lại log cũ, và log cũng chứa dữ liệu thật.
- Cần tắt `gs001`, `Bishop`, `S3Relay`, `Goddess`, rồi chạy lại.

## Dữ liệu thật còn lại
- 37 thư mục sao lưu trong `gw\database`: 74 file, 10,4 MB.
- `gs\DumpInfo` (13 file, 155 MB), `gw\bishopDump`: bản chụp bộ nhớ có thể chứa dữ liệu người chơi.
- `gw\dbfriend`, `gs\TongSet`, dữ liệu bang hội (log hôm nay của `S3Relay` có in tên chủ bang).
- `gw\mysql account\jx_account.sql` (3 dòng `INSERT`).
- Snapshot cũ, lịch sử git.

## Danh sách đổi phía server (chưa thực hiện)
- `gs\gs001_cfg.ini`, `[GameServer] Ip` và `[GameServer] localIp`: từ `<LAN-IP>` sang địa chỉ Tailscale máy thật.
- Không đổi: `[Gateway]`, `[Database]`, `[Transfer]`, `[Chat]`, `[Tong]`, `[TransServer]`, `[GameServer] Port`, `gs002` đến `gs005`, `Bishop.cfg`, `relay_config.ini`, `database.ini`, bảng `ServerList`, tường lửa VM.

## Bishop có nhận gs theo IP không
- Không tìm thấy kiểm tra IP khi `gs` kết nối. `Intercessor.cpp:323` mở cổng cho mọi địa chỉ.
- `GameServer.cpp:132`, `:660-684`: `gs` tự báo địa chỉ, `Bishop` lưu lại.
- `Bishop.cfg` `GameSvrIP` không được đọc trong mã nguồn (`Network.cpp:60-73` chỉ đọc `RoleSvrIP`, `AccSvrIP`, `GameSvrOpenPort`).
- Bảng `ServerList` kiểm tra đăng nhập dịch vụ của `Bishop`, `S3Relay` với `Sword3PaySys`, theo địa chỉ kết nối (`S3PAccount.cpp:409-456`), không theo `[GameServer] Ip`.
- Kết nối `gs` tới `Bishop` vẫn từ `<LAN-IP>`. Kết luận dựa trên mã nguồn, chưa thử với exe.

## Phía client (đã sinh, chưa áp dụng)
- `FsjxClient.ini`, `package.ini`, `network_security_config.xml`, `update10.pak` trong `docs-analysis\out\tailscale\`.

## Bước kế
Chủ máy duyệt, sau đó sửa cấu hình và khởi động lại. Script mở cổng chạy sau cùng.
