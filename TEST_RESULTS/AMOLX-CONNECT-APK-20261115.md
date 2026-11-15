# AMOLX-04 — Bàn giao APK debug ARM64; kết nối chưa được phép thử

- Task: `AMOLX-04-CONNECT-AND-APK-20261115`.
- Ngày: 15/11/2026, múi giờ Asia/Bangkok.
- Prompt đọc trên `ndtangoss-dev/jx1-reports`, nhánh `main`: `PROMPTS/AMOLX-04-CONNECT-AND-APK-20261115.md`, blob `a6da4335b7bc3eea6580c8aadd4c2cf9491630c1`. Người dùng không ghim commit cho task này.
- Baseline: AMOLX-03, báo cáo tại commit `79981adf1aba9062e7919fb6614398681427635f`; không chạy lại audit enum.
- **Trạng thái tổng thể: PARTIAL. Build APK: ĐẠT. Kết nối: NOT-TESTED, bị chặn bởi xác nhận môi trường và protocol contract.**

## Kết quả cần bàn giao

Đã build APK debug thực tế bằng Gradle/CMake/NDK, có thư viện native của AMOLX; đây chưa phải client đã xác minh kết nối hoặc gameplay với server hiện tại.

| Thuộc tính | Kết quả đã đo |
|---|---|
| APK bàn giao | `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk` |
| APK gốc từ build | `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\proj.android\app\build\outputs\apk\debug\jx1client-debug.apk` |
| Dung lượng | 60.600.580 bytes |
| SHA-256 | `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1` |
| Package / phiên bản | `com.kull.jx1client`, versionCode `1`, versionName `1.0` |
| ABI | `arm64-v8a` theo `aapt2 dump badging` và các thư viện trong APK |
| SDK theo cấu hình/metadata | compile/target 34; minSdkVersionForDexing 17. Chưa nghiệm thu khả năng chạy trên các Android khác nhau |
| Chữ ký | `apksigner verify --verbose --print-certs`: Verifies; v1=true, v2=true; một signer Android Debug |
| Tính toàn vẹn ZIP | `zipfile.testzip()` trả None; bản bàn giao có cùng SHA-256 với output build |
| Thư viện native | `libc++_shared.so`, `libjx1client.so`, `libopenal.so`, đều trong `lib/arm64-v8a/` |
| Tệp nhạy cảm dạng file | Không có `accinfo.ini`, `.jks`, `.keystore` trong danh sách entry APK; không phải chứng nhận đã audit mọi asset/string |

File SHA-256 đi kèm APK ở cùng thư mục. APK/source/log chỉ giữ local, không tải lên dịch vụ ngoài hoặc GitHub. Báo cáo đã lọc dữ liệu nội bộ mới được đưa lên repository báo cáo.

## Kết nối và protocol contract

Kết luận cho mốc kết nối: **NOT-TESTED**. Tài liệu trạng thái hiện có chỉ xác nhận VM vận hành client thật; handover trước cũng chưa xác nhận môi trường test riêng. Không có bằng chứng đủ chắc chắn để coi endpoint đó là test endpoint được phép cho AMOLX-04. Không ghi địa chỉ, tên tài khoản hoặc dữ liệu xác thực vào báo cáo này.

Đã đọc chọn lọc `docs-analysis/reports/22-tong-ket-trang-thai.md`, `13-dung-apk-debug.md` và checkpoint handover. Không kết nối socket game, không gửi packet, không truy cập/điều khiển VM, không đổi endpoint, firewall, forwarder hoặc cấu hình server.

**Chưa chọn protocol contract cho server đang chạy.** Checkpoint AMOLX-03 vẫn còn mâu thuẫn Gateway↔GameServer và chưa có manifest/artifact liên hệ bộ header với binary thực tế. Theo điều kiện trong prompt, chưa sửa enum, packet layout, framing, dispatch hay Bishop handoff bằng một contract suy đoán. Các bất tương thích đã xác minh ở AMOLX-03 vẫn tồn tại trong APK này, gồm va chạm ID 95 và layout handoff khác Cocos tham chiếu. Build thành công không giải quyết chúng.

| Tầng runtime | Kết quả |
|---|---|
| TCP tới endpoint game | NOT-TESTED |
| Handshake | NOT-TESTED |
| Login | NOT-TESTED |
| Chọn server / nhân vật | NOT-TESTED |
| Vào world / gameplay | NOT-TESTED |
| Cài APK / mở app trên LDPlayer 14 | Chưa thực hiện |

Kiểm tra tiến trình không thấy `dnplayer`, `ldplayer`, `LdVBoxHeadless`, `Ld9BoxHeadless` đang chạy; chỉ thấy ADB của một ứng dụng khác. Không dùng ADB đó, không tự mở emulator. Checkpoint yêu cầu chỉ chạy APK khi đích đã xác nhận là VM thử nghiệm riêng; vì vậy không khởi động app có thể tự liên hệ endpoint sẵn có.

## Bản sao, dependency và thay đổi local

Bản gốc AMOLX: `C:\JX1\jx1client-axmol-main\jx1client-axmol-main`. Bản task: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client`.

Đã chép 1.277 file gốc khoảng 90,8 MB theo kiểm kê ban đầu; robocopy thực hiện với loại trừ `.git`, `.gradle`, `.cxx`, `build`, `accinfo.ini`, keystore và `local.properties`. Không sửa source AMOLX gốc, Cocos canonical hoặc server. Hash `MainLogin.cpp` gốc sau build vẫn là `B4E9D53ABB...E6D8CDA`, khớp trước sửa; đối chiếu các file bản sao với bản gốc được lưu local trong `handover-checks.json`.

| Dependency | Phiên bản / vị trí / tình trạng |
|---|---|
| Axmol | Mới tải 2.1.5 từ release chính thức vào `C:\Jx1CocoV3\amolx-work\deps\axmol-2.1.5-unpacked\axmol-2.1.5` |
| Kiểm gói Axmol | MD5 `D42B00A4FBFEF44E8AB38A56C2028A5E` khớp release; SHA-256 `657B2BD0177364D664695A8654D469519DBE93E5F40DC156A01C46190D5512AB` |
| glslcc | Mới tải 1.9.5 từ release `axmolengine/axslcc`, thư mục `tools/external/glslcc` trong Axmol riêng |
| Kiểm gói glslcc | SHA-256 `3FE71F88D9CC5A864994ECFCD45350D431EEBEC8A6C83157391F28C0B19081A9` khớp digest release |
| NDK | Gradle cài thêm 23.2.8568313 side-by-side tại `D:\Android\sdk\ndk\23.2.8568313`, user-scope, dùng cho build thành công |
| Toolchain tái sử dụng | Temurin JDK 17.0.21 tại `D:\Android\jdk`; Gradle 8.7; CMake 3.30.5; SDK/build-tools 34 tại `D:\Android\sdk` |
| Android Gradle Plugin | Bản sao đổi từ 8.4.0 sang 8.5.0 có sẵn trong cache; build đã dùng 8.5.0 theo cấu hình rõ ràng |
| Phụ thuộc phát sinh không dùng | Setup Axmol tải CMake 3.23.0 và Ninja 1.10.0 vào `tools/external` riêng; build cuối dùng CMake 3.30.5 và Ninja của SDK |

Không chạy `setup.ps1` tổng quát để sửa profile/global environment. Biến AX_ROOT/JAVA_HOME/ANDROID_HOME/GRADLE_OPTS chỉ đặt trong tiến trình build. Không thay model/provider/reasoning/CODEX_HOME hay config Codex, không Dispatcher/Scheduler.

Các file thay đổi:

| File (đều trong bản task/dependency riêng) | Mục đích |
|---|---|
| `client/Source/gamescene/MainLogin.cpp` | Bỏ đọc/ghi account/password từ `accinfo.ini`, để ô nhập trống; giữ phép hash mật khẩu trong bộ nhớ để tạo yêu cầu login |
| `client/proj.android/build.gradle` | AGP 8.4.0 → 8.5.0 phù hợp cache/toolchain hiện có |
| `client/proj.android/local.properties` | Tệp mới trỏ SDK local để build bản copy |
| `client/proj.android/app/src/org/axmol/lib/SharedLoader.java` | CMake sinh lại; hash byte khác, nội dung diff sau chuẩn hóa newline không khác |
| Axmol riêng `core/ui/UIButton.h` | Thêm bốn accessor custom state/item ID theo yêu cầu README AMOLX |
| Axmol riêng `core/ui/UIButton.cpp` | Khởi tạo hai trường mới false/0, tránh giá trị chưa khởi tạo |
| `build-amolx04.ps1` trong thư mục task | Lưu lệnh build có environment chỉ trong tiến trình; tạo sau build, chưa chạy lại script này |

Có `client-changes.patch`, `axmol-button-compat.patch` và manifest hash local để tiếp tục công việc. Các output/cache/build, không phải bản source canonical, nằm trong thư mục task/deps. Không upload patch/source vì prompt cấm đưa source dự án lên dịch vụ ngoài và cho phép giữ source local, chỉ push báo cáo đã lọc.

## Build thực tế và kiểm tra

Lệnh thành công chạy trong `client\proj.android` với AX_ROOT trỏ Axmol riêng, JAVA_HOME `D:\Android\jdk`, ANDROID_HOME/ANDROID_SDK_ROOT `D:\Android\sdk`, GRADLE_USER_HOME `D:\Android\gradle`, GRADLE_OPTS `-Xmx512m`, CMAKE_BUILD_PARALLEL_LEVEL `4`:

```powershell
& 'D:\Android\gradle-8.7\bin\gradle.bat' --no-daemon --max-workers=4 '-Dorg.gradle.jvmargs=-Xmx4096m' -P__1K_ARCHS=arm64-v8a assembleDebug
```

Kết quả nguyên văn: `BUILD SUCCESSFUL in 3m 57s`, `65 actionable tasks: 64 executed, 1 up-to-date`, exit 0. Log cuối: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\build-attempt-4.log`.

Kiểm tra đã chạy: native/Java compile và đóng gói APK qua Gradle; aapt2 badging; apksigner; CRC/ZIP; SHA-256 bản build và bàn giao; kiểm source tĩnh loại bỏ persistence trong MainLogin nhưng giữ hash login; hash file gốc không đổi. Không chạy unit test protocol, sizeof/offset test, runtime login/UI, LDPlayer hay gameplay. Không coi các mục chưa chạy là đạt.

Mục tiêu thời gian 10+30 phút **không đạt đầy đủ**: bản copy được tạo 22:28:13; log build đầu 22:34:26; build cuối từ 23:13:08 đến 23:17:05 ngày 15/11/2026. Dependency, setup và xử lý lệnh/quyền đã kéo dài quá timebox. Không gọi thời gian compile 3m57 là tổng thời gian task. Tất cả giờ theo Asia/Bangkok.

## Các lỗi gặp và xử lý

1. Download Axmol trong quyền mặc định báo `An attempt was made to access a socket in a way forbidden by its access permissions.` Đã dùng quy trình duyệt quyền chạy/tải được hỗ trợ, tải thành công và kiểm hash; không đổi chính sách bảo mật hoặc credential.
2. Lệnh PowerShell tạo local.properties gặp lỗi here-string, chưa thực thi; sửa cú pháp rồi ghi vào bản copy. Lệnh patch nhiều dòng qua batch Windows gặp lỗi định dạng; sau đó áp dụng thành công bằng helper patch trực tiếp, không thay config CLI.
3. Build 1, offline: `No cached version of com.android.tools.build:gradle:8.4.0 available for offline mode.` Đổi rõ AGP trong bản copy sang 8.5.0. Có một thao tác trung gian chép cache 8.5 vào nhãn 8.4 sai cách; thư mục tạm đó đã xóa khỏi cache riêng, trước mọi build tiếp theo. Không dùng dependency giả nhãn để build.
4. Build 2: cài được NDK 23.2, sau đó `Please run setup.ps1 again to download glslcc, and run CMake again.` Đã bổ sung đúng glslcc 1.9.5, kiểm SHA-256 release.
5. Setup `1k/1kiss.ps1 -setupOnly` chạy từ workspace không nhận diện đầy đủ app, tải thêm CMake/Ninja rồi dừng ở symbolic link: `Administrator privilege required for this operation.` Không nâng Admin/UAC, không cố chạy lại lệnh tạo symlink. Chuyển sang đặt glslcc portable trực tiếp trong dependency riêng; build cuối dùng CMake/Ninja SDK đã có, không cần symlink đó.
6. Build 3: PowerShell truyền sai tham số không quote, `Task '.gradle.jvmargs=-Xmx4096m' not found`. Quote toàn bộ `-Dorg.gradle.jvmargs=...`; build 4 thành công.
7. Một yêu cầu chạy build ngoài quyền mặc định bị auto-review timeout trước khi chạy, được thông báo cho phép thử lại một lần; lần thử lại thành công. Không có kết luận đây là hành động bị cấm và không tắt cơ chế kiểm soát quyền.
8. Kiểm hash sau build có câu lệnh dùng `Get-Content -Encoding Byte` không phù hợp PowerShell 7; phép kiểm đó không được nhận là đạt. Đã kiểm lại đúng bằng Python read_bytes và SHA-256 so với manifest trước sửa: đạt.
9. Truy vấn metadata glslcc cũ gặp redirect/404/endpoint connector không hỗ trợ; đã đọc đúng release `axmolengine/axslcc` và xác minh asset SHA-256, không dùng nguồn tải tùy ý.
10. Build có cảnh báo mã nguồn kế thừa, gồm so sánh `this` với null và API deprecated/unchecked; chưa sửa ngoài phạm vi. apksigner có cảnh báo một số entry META-INF không được bảo vệ riêng theo JAR v1; kết quả verify APK v1/v2 vẫn đạt. Không gọi APK đã audit bảo mật toàn diện.

## Git và bước tiếp tục

Git workspace kiểm trước sửa: `master`; có BAI_HOC.md đã sửa cùng nhiều untracked cũ. Giữ nguyên; không stage/reset/clean hay đổi remote. Repository workspace và repository báo cáo có lịch sử khác nhau. Commit lên `ndtangoss-dev/jx1-reports/main` bằng connector chỉ chứa báo cáo này, không source, APK, log, cache hoặc credential. SHA và link của commit chứa chính báo cáo sẽ được xác minh và cung cấp ở bàn giao cuối, không chèn SHA tự tham chiếu vào file.

Để tiếp tục runtime, cần người dùng xác nhận nhãn môi trường test và bộ artifact/build tương ứng Gateway/Bishop/GameServer. Sau đó mới giải quyết contract, patch protocol trên bản copy và chạy từng tầng; APK hiện tại chỉ dùng kiểm thử khi đích đã được xác nhận an toàn. Không yêu cầu mở Main VM hoặc thay server cho phù hợp client.

Sau xác nhận môi trường, có thể cài từ máy đang có ADB chính thức và emulator đúng ABI bằng lệnh dưới; serial lấy từ thiết bị thực tế, không tự chọn nếu có nhiều thiết bị. Lệnh chưa chạy trong task này:

```powershell
& 'D:\Android\sdk\platform-tools\adb.exe' -s '<serial-LDPlayer-đã-xác-minh>' install 'C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk'
```

Không dùng tùy chọn ghi đè bản cài sẵn; nếu package đã tồn tại, cần bảo toàn dữ liệu trước. Chưa mở app, chưa cung cấp tài khoản test và chưa có bằng chứng endpoint đủ an toàn cho runtime.
