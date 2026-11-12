# Bước 3 – Chuẩn bị client

## TÓM TẮT 5 DÒNG
1. **Chưa dựng được APK**: máy thật không có JDK, Android SDK, NDK, CMake. Đã dừng ở đây theo yêu cầu.
2. Đã có script sinh `FsjxClient.ini`, `package.ini`, `network_security_config.xml`, `update10.pak` theo địa chỉ Tailscale.
3. Chạy thử với địa chỉ giả `<TAILSCALE-IP>`, ra scratchpad: `pak_verify` DAT, `package.ini` đổi đúng 1 dòng, file gốc không đổi.
4. Đã có `cdn_server.py` chỉ đọc, bind vào địa chỉ Tailscale, chỉ nhận điện thoại. Chưa chạy.
5. Chờ địa chỉ Tailscale và quyết định cài công cụ Android.

Cần tôi quyết định: có

## Đã làm
- Snapshot: `buoc3-chuan-bi-client`. Bước này không đổi VM.
- `docs-analysis\scripts\tao_client_tailscale.py <HostTs>`: ghi vào `docs-analysis\out\tailscale\` (không commit), không sửa file gốc.
  - Chỉ nhận IPv4 Tailscale, không cổng, tối đa 18 ký tự.
  - Mã hóa bằng `simply_crypt.py`, giải mã lại để đối chiếu.
  - `package.ini` lấy từ `Resources`, không phải `data/data`.
  - `update10.pak` tạo bằng `pak_replace.py`, kiểm tra bằng `pak_verify.py`.
- `docs-analysis\scripts\cdn_server.py`: chỉ GET và HEAD, không liệt kê thư mục, có Range vì client tải tiếp bằng `CURLOPT_RESUME_FROM` (`KDownLoadFile.cpp:189`), thay `update10.pak` bằng bản đã sửa mà không chép `data_cdn` (3,22 GB).

## Bằng chứng
- `python compile` và PowerShell parser: 0 lỗi trên các script.
- Chạy thử: `pak_verify: KET QUA: DAT`, `update10.pak` 10 882 596 byte.
- `network_security_config.xml` có thêm đúng một dòng domain.
- `git status`: không có file gốc nào thay đổi.

## Thiếu để dựng APK
Không tìm thấy các mục sau trên máy thật:
- JDK (`java`, `JAVA_HOME`).
- Android SDK với `platforms;android-34` và build-tools.
- NDK `25.2.9519653` (`app/build.gradle:15`).
- CMake `3.30.5` (`app/build.gradle:41`).
- `sdk.dir` trong `local.properties` đang trỏ tới máy khác.

Gradle 8.7 sẽ được wrapper tải về. Ổ C còn 67,9 GB, ổ D còn 1686 GB, nên đặt SDK và bản copy client ở D:.

## Khi có công cụ
1. Chép client (1,11 GB) sang bản copy.
2. Chép `package.ini` và `network_security_config.xml` đã sinh vào bản copy.
3. Bỏ comment `PROP_APP_ABI`, chạy `gradlew assembleDebug`. Không dùng keystore trong repo.

## CDN (chưa chạy)
```powershell
python -I docs-analysis\scripts\cdn_server.py --bind <HostTs> --allow <PhoneTs> --root data_cdn\data --override update10.pak=docs-analysis\out\tailscale\update10.pak
```
Cần chạy `tailscale_mo_cong.ps1 -WithCdn` để có luật tường lửa cổng 80. Tải 3,22 GB qua Tailscale, có thể chậm nếu không nối trực tiếp.

## Chưa kiểm tra
- `cdn_server.py` chưa chạy thật, vì chưa được phép chạy web server.
