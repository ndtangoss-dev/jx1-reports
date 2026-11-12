# 19 - CDN cổng 8080, TCP Forwarder và tác vụ JX-UI

Ngày: 2026-11-11

## TÓM TẮT 5 DÒNG
1. CDN chuyển sang `<TAILSCALE-IP>:8080` vì `http.sys` (dịch vụ `ReportServer`, chủ máy cấm dừng) giữ cổng 80; APK mới `jx-tailscale-8080.apk` đã gửi qua Taildrop.
2. Sau khi máy thật khởi động lại, 2 luật `portproxy` 56722/51189 vẫn còn trong cấu hình, `iphlpsvc` vẫn Running, nhưng không có socket nào nghe nên điện thoại kẹt ở bước chọn máy chủ.
3. Forwarder Python tạm (`tcp_forwarder.py`, PID 18888) bind đúng 2 cổng trên địa chỉ Tailscale, chỉ nhận `<TAILSCALE-IP>`; điện thoại qua được chọn máy chủ.
4. Chủ máy xác nhận chơi thực tế tốt: đăng nhập, vào gs001, ping khoảng 150 ms. Log `payserver` ghi `<test-account> Login Success` lúc 10:18:53 và `Logout` lúc 10:19:30.
5. Task `JX-UI` bị đổi hành động nhiều lần để đọc console; ghi nhận ở mục 4. Không đụng Firewall, cấu hình server, VM cũ.

**Cần tôi quyết định: có** - xem mục 5 (đăng ký tự khởi động forwarder) và `20-van-hanh-on-dinh-o-d.md`.

## 1. CDN cổng 8080
- Nguyên nhân: cổng 80 do `http.sys` giữ độc quyền, Python bind chung báo `WinError 10013`. Chủ máy cấm dừng/đổi `ReportServer`.
- Client ghép `http://<down>/` (`KUpdateLayer.cpp:355`). Chỉ cần đổi `down=` trong `Resources/package.ini` thành `<TAILSCALE-IP>:8080` (mã hóa, 18 ký tự đúng giới hạn).
- Bản gốc `package.ini` lưu ở `D:\Android\b\backup-cdn8080\package.ini.orig`. APK: `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk`, 78.901.355 byte, SHA256 `82674B16…`, ký cùng khóa debug với các APK trước.
- CDN chạy PID 18284, bind `<TAILSCALE-IP>:8080`, `--allow <TAILSCALE-IP>`. Nguồn khác nhận 403, POST nhận 501. Log `docs-analysis/out/cdn-8080.log` (git bỏ qua).

## 2. Lỗi kết nối sau reboot
- Dữ kiện đo được: `netsh interface portproxy show all` vẫn liệt kê <TAILSCALE-IP>:56722 và :51189 → <LAN-IP>; `iphlpsvc` Running/Automatic; nhưng kết nối từ máy thật tới hai cổng đó bị từ chối ("actively refused"); Bishop không thấy gói nào.
- Cổng 8080 (Python) nghe bình thường, nên đường Tailscale và địa chỉ đều đúng.
- Nguyên nhân gốc: **chưa kiểm chứng**. Giả thuyết: `iphlpsvc` khởi động trước khi adapter Tailscale có địa chỉ `<TAILSCALE-IP>` nên không bind lại. Chữa bằng `Restart-Service iphlpsvc` cần Admin, chủ máy không có mặt và dặn không tự chuyển sang sửa `iphlpsvc`, nên không làm.

## 3. Forwarder tạm
- `docs-analysis/scripts/tcp_forwarder.py`: asyncio, từ chối bind `0.0.0.0`/`::`, chỉ nhận đúng `--allow`, không ghi nội dung gói. Khởi chạy lúc 10:10:37.
- Kiểm tra từ máy thật: nguồn khác bị từ chối (#1). Điện thoại: #2, #3 (cổng 56722) sống 0,2 s, điện thoại gửi 0 byte, VM trả 34 byte (ACCOUNT_BEGIN).
- Phiên đăng nhập thật: #4 (56722) 10:18:48, 7,5 s, 663 byte lên / 520 byte xuống; #5 (51189) 10:18:55, 32,4 s, 6.841 byte lên / 992.799 byte xuống.
- Đối chiếu log VM: `payserver_log` 10:18:53 `User <test-account> ... Login Success!`; 10:18:59 `Freeze Account: Success`; 10:19:30 `Logout: Success`; `relay_log` 10:19:31 `<test-account>` thoát game.
- Dừng: `docs-analysis/scripts/dung_forwarder.ps1` (chưa chạy). **Forwarder và CDN đang chạy, theo lệnh chủ máy không dừng.**

## 4. Tác vụ JX-UI (VM `JX-Server-D`)
- Trạng thái hiện tại: `Ready`, user `<vm-user>`, `LogonType Interactive`, lần chạy cuối 10:16:16, kết quả 0. Hành động hiện tại: `powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File C:\JX\sql\console.ps1 -TargetPid 7600` (7600 = `S3Relay`).
- Ghi nhận: đây là tác vụ dùng chung để chạy việc cần phiên desktop. Hành động đã bị đổi nhiều lần trong phiên này sang các script trợ giúp trong `C:\JX\sql`: `ui-dump.ps1`, `ui.ps1`, `ui2.ps1`, `ui3.ps1`, `ui4.ps1`, `console.ps1`. Chỉ `console.ps1` còn được trỏ tới.
- Mã băm SHA256 (12 ký tự đầu): console 4ACFC0333649, ui-dump 1E9B8EB7AC8C, ui A8B7E0B9C70A, ui2 6D0260D4DCD0, ui3 3F5B3455140B, ui4 2CE1E8D6EEB4.
- `console.ps1` chỉ gắn vào console của PID đích, đọc buffer màn hình và ghi `C:\JX\sql\console.txt`. Không mở cổng, không sửa file server. Với `Sword3PaySys`/`Goddess`/`S3Relay` (ứng dụng GUI) nó trả "attach failed 6".
- Các tác vụ `JX-Bishop`, `JX-Goddess`, `JX-gs001`, `JX-S3Relay`, `JX-Sword3PaySys` đang `Running`, cùng user `<vm-user>`, Interactive; `JX-Bishop` có `ExecutionTimeLimit` = `PT0S`.
- **Mâu thuẫn chưa giải quyết:** lần kiểm tra ở bước nhân bản VM ghi mỗi tác vụ có 1 trigger; lần đọc hôm nay (`Get-ScheduledTask`/`Export-ScheduledTask` qua WinRM) không trả trigger nào. Chưa biết tác vụ có tự chạy khi VM khởi động hay không. Phải đọc lại trực tiếp hoặc thử khởi động VM (cần chủ máy duyệt) mới chắc.
- Đề xuất: sau khi test xong, đặt lại hành động `JX-UI` về trạng thái trung tính (hoặc xóa) và xóa các script `ui*.ps1`; chưa làm vì cần hỏi chủ máy.

## 5. Chưa kiểm tra / còn mở
- Nguyên nhân thật của việc không có listener sau reboot.
- Tại sao #2/#3 bị đóng sau 0,2 s (Bishop, client hay forwarder).
- Có trigger khởi động cho 6 tác vụ `JX-*` hay không (mục 4).
- Tác vụ Xiaomi cài đè cùng versionCode: điện thoại đã chạy được, coi như đạt.
