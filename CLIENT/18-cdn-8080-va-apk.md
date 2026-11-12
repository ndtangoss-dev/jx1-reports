# CDN cổng 8080 và APK mới

## TÓM TẮT 5 DÒNG
1. `cdn_server.py` chạy ở `<TAILSCALE-IP>:8080`, chỉ cho `<TAILSCALE-IP>`. Điện thoại tải được `paklist.ini` (200, 1,51 KB). `ReportServer` không bị đụng.
2. Bản copy client `D:\Android\b\Client\Resources\package.ini` chỉ đổi đúng dòng `down=`, kích thước vẫn 591 byte, giải mã ngược ra `http://<TAILSCALE-IP>:8080/`.
3. Build APK mới thành công, `--offline --no-daemon`, 52 giây (cả lệnh 53 giây), heap như cũ.
4. APK mới ở `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` (78.901.355 byte). APK cũ trong `D:\Android\b\apk\` không đổi.
5. Chưa cài APK, chưa xóa dữ liệu app, chưa đổi VM hay dịch vụ. Chưa thử đăng nhập bằng APK mới.

Cần tôi quyết định: có

## Bằng chứng
- Log `docs-analysis/out/cdn-8080.log` (Git bỏ qua): `<TAILSCALE-IP> GET /data/paklist.ini 200`. Từ máy thật: GET/HEAD trả 403, POST trả 501.
- Sao lưu `D:\Android\b\backup-cdn8080\package.ini.orig`, SHA256 `D1F47009...1CA3`. Diff: một dòng khác nhau, `down=M0SaSKz...` thành `down=rWEX92Qf...`.
- APK: SHA256 `82674B16...`, `assets/package.ini` có `down=rWEX92QfGSUKJNhKAGUEw10kYam_IIBZ`, id `com.jxclient.hoiuctruyenky` versionCode 17, chỉ `arm64-v8a`, ký debug, không có keystore trong gói, `network_security_config.xml` còn 3 miền cho phép HTTP không mã hóa.

## Chưa kiểm tra
- Client mở được CDN qua `:8080` thật. Mã nguồn cho thấy địa chỉ ghép thành `http://<down>/`, chưa chạy thử.
- File `data/package.ini` cũ trong bộ nhớ app có bị bản mới ghi đè khi cài đè không. Có thể phải xóa dữ liệu app.

## Bước kế
Chủ máy duyệt gửi APK qua Taildrop và cài đè. Nếu lỗi: khôi phục `package.ini.orig` và dùng lại `jx-tailscale.apk`, CDN cổng 80 cần dừng `ReportServer`.

## Bổ sung: kiểm tra trước khi cài (2026-11-11)
- Chữ ký: `jx-tailscale.apk`, `jx-lan.apk` và `jx-tailscale-8080.apk` cùng chứng chỉ debug, SHA-256 `a48601f73930bf6a560e14d2b6b116f5fc578d15b7daeb13f9b78806d76af2d7`. Cùng id và versionCode 17, ký bằng scheme v2. Có thể cài đè không gỡ.
- ABI: chỉ `arm64-v8a`, minSdk 25, targetSdk 34.
- `package.ini`: ứng dụng dùng `KUpdateLayerVN` (`AppDelegate.cpp:183`). Mỗi lần mở app, `copyData("package.ini")` đọc bản trong APK và ghi đè `data/package.ini` ở thư mục ghi của app (`KUpdateLayerVN.cpp:145`, `KUpdateLayer.cpp:629-669`, mở bằng `wb+`). Vì vậy cài đè là đủ, không phải xóa dữ liệu app.
- Nhân vật nằm ở `roledb` trong VM. Tài khoản đã nhớ nằm ở `accinfo.ini` trong dữ liệu app, được giữ khi cài đè.
- Gửi qua Taildrop: `tailscale file cp` đến `xiaomi-13t-pro`, thoát mã 0 sau 186 giây, Tailscale ghi tx khoảng 84 MB. Chưa xác nhận máy điện thoại đã nhận.
- Chưa kiểm tra: trình cài đặt của máy Xiaomi có cho cài đè khi versionCode giữ nguyên 17 không.
