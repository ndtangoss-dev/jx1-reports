# AMOLX-05 — Smoke-test APK AMOLX-04 trên LDPlayer 9

- Task: `AMOLX-05-LDPLAYER9-SMOKE-TEST-20261115`.
- Ngày thực hiện: 15/11/2026, múi giờ máy chủ tác vụ Asia/Bangkok (UTC+7).
- Prompt: `PROMPTS/AMOLX-05-LDPLAYER9-SMOKE-TEST-20261115.md`, blob đã đọc `f69f55831ed9dd31d910894722fef69040704edc`.
- **Trạng thái: DONE — đã thực hiện smoke-test cài/mở; INSTALL-OK; LAUNCH-OK.**
- **Kết quả giao diện còn lỗi:** tới màn hình tải với nền nhân vật và hộp thoại chữ sai mã hóa, tiến độ khoảng 6%; chưa tới login. Đây chưa phải ứng dụng đã qua kiểm thử chức năng.
- **Network/game-server/login: NOT-TESTED.** Không thao tác chọn server, không gửi login, không nhập tài khoản hoặc mật khẩu.
- Cần tôi quyết định: **không** trong phạm vi smoke-test đã duyệt; sửa lỗi cần task tiếp theo.

## Tóm tắt năm dòng

1. Nhận diện đúng một ADB device `emulator-5554` và đối chiếu với LDPlayer 9 đang chạy trước khi cài.
2. APK AMOLX-04 khớp SHA-256; package chưa có, cài mới thành công, không dùng replace/upgrade/uninstall/clear-data.
3. App mở thành công, PID `4840`, nạp được ba thư viện ARM64 qua native bridge và khởi tạo Axmol/OpenGL ES.
4. Màn hình nền dựng được nhưng kẹt ở tải khoảng 6%, có hộp thoại lỗi sai mã hóa và cảnh báo EGL; không ghi nhận crash/ANR trong cửa sổ quan sát.
5. Đã đóng riêng app sau khi thu bằng chứng; giữ app và dữ liệu. Chỉ báo cáo đã lọc được công bố; không upload APK, ảnh, source hoặc log thô.

## Thiết bị và nhận diện đích

| Thuộc tính | Bằng chứng thực tế |
|---|---|
| SDK ADB | `D:\Android\sdk\platform-tools\adb.exe` |
| Danh sách thiết bị | Chỉ một dòng device: `emulator-5554 device product:XQ-BE42 model:XQ_BE42 device:marlin transport_id:4` |
| LDPlayer UI | Tiến trình `dnplayer`, PID `37144`, đường dẫn `C:\LDPlayer\LDPlayer9\dnplayer.exe` |
| Backend emulator | `Ld9BoxHeadless`, PID `22596`, đường dẫn `C:\Program Files\ldplayer9box\Ld9BoxHeadless.exe` |
| Đối chiếu ADB | `netstat -ano -p tcp`: cổng ADB `5555` do PID `22596` lắng nghe và có kết nối loopback từ ADB; cấu hình instance duy nhất là `leidian0.config`, VM XML có tên `leidian0` |
| Android | Android `9`, SDK/API `28` |
| ABI được emulator khai báo | `x86_64,x86,arm64-v8a,armeabi-v7a,armeabi` |
| Native bridge | `ro.dalvik.vm.native.bridge=libnb.so`; log Houdini khởi tạo thành công cho ARM64 |
| Màn hình quan sát | Landscape, PNG `1920×1080`; không thay cấu hình màn hình hoặc ép xoay emulator |

Các giá trị SONY/XQ-BE42/marlin là thông tin Android mà emulator trả về; việc xác định LDPlayer dựa thêm vào tiến trình, đường dẫn và PID sở hữu cổng ADB, không dựa riêng tên model.

### Lỗi ADB ban đầu và cách xử lý

Hai lệnh ban đầu `adb version` và `adb devices -l` trong quyền mặc định cùng dừng với:

```text
adb_utils.cpp:315 Cannot mkdir '\.android': Permission denied
```

Sau đó chạy lại `adb devices -l` bằng cơ chế duyệt quyền lệnh được công cụ hỗ trợ: thành công ngay và thấy đúng một device. Đây là bằng chứng lỗi phụ thuộc môi trường quyền của tiến trình; chưa xác định nguyên nhân sâu hơn của việc ADB chọn `\.android`. Không thay biến môi trường toàn hệ thống, không chỉnh/xóa/tạo lại khóa ADB, không thay credential và không tắt các biện pháp bảo vệ. Không lặp lại quá ba lần cùng lỗi.

## APK và cài đặt

| Mục | Kết quả |
|---|---|
| APK local | `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk` |
| Dung lượng | `60600580` bytes |
| SHA-256 kiểm lại trong AMOLX-05 | `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1` — khớp checkpoint |
| Package từ aapt | `com.kull.jx1client` |
| Version | `1.0`, versionCode `1` |
| minSdk/targetSdk | `17` / `34` |
| APK ABI | `arm64-v8a` |
| Activity từ aapt | `org.axmol.app.AppActivity` |
| Package trước cài | `pm path com.kull.jx1client` không trả đường dẫn; package chưa có |
| Package sau cài | `pm path` có `base.apk`; dumpsys xác nhận version và `primaryCpuAbi=arm64-v8a` |
| Chữ ký/ZIP | Đã xác minh trong AMOLX-04; không chạy lại trong task này, dùng APK có hash khớp |

Lệnh thực tế:

```powershell
& 'D:\Android\sdk\platform-tools\adb.exe' -s emulator-5554 install 'C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk'
```

Kết quả: exit `0`, `Performing Streamed Install`, `Success` → **INSTALL-OK**. Không có `-r`, không gỡ hoặc ghi đè package cũ; không cài lên thiết bị khác.

## Khởi chạy và thời gian quan sát

```powershell
& 'D:\Android\sdk\platform-tools\adb.exe' -s emulator-5554 shell am start -W -n com.kull.jx1client/org.axmol.app.AppActivity
```

Kết quả thực tế: exit `0`.

```text
Status: ok
Activity: com.kull.jx1client/org.axmol.app.AppActivity
TotalTime: 3877
WaitTime: 3900
Complete
```

- Bắt đầu theo đồng hồ Android: `11-15 23:48:29`; kết thúc/đóng app: `11-15 23:51:36` (cửa sổ khoảng 3 phút 7 giây; không xác minh riêng độ lệch đồng hồ Android).
- PID `4840` còn tồn tại ở các lần kiểm tra sau mở; kiểm tra cuối trước đóng lúc `23:50:51` vẫn có PID và `mResumedActivity`/`mCurrentFocus` là AMOLX.
- `dumpsys activity lastanr`: `<no ANR has occurred since boot>`.
- Log riêng PID từ mốc mở không có `FATAL EXCEPTION`, `Fatal signal` hoặc `UnsatisfiedLinkError` (`APP_FATAL_COUNT=0`). Crash buffer từ cùng mốc không trả dòng liên quan target/crash theo bộ lọc đã dùng.
- **LAUNCH-OK; không quan sát thấy crash hoặc ANR trong khoảng kiểm thử.** Điều này không chứng minh ổn định dài hạn, không thay cho kiểm thử trên điện thoại ARM64.
- Không bấm nút `Ok` của hộp thoại không đọc được, không thao tác tiếp sang login/chọn server.
- Sau thu bằng chứng, gọi `am force-stop com.kull.jx1client`. Lệnh `pidof` cuối không trả PID và exit `1` theo trạng thái không còn tiến trình; đó là kết quả mong đợi sau đóng app, không phải app crash. App vẫn được cài và giữ dữ liệu đã tạo.

## Native libraries và renderer

Các dòng log cùng PID `4840` xác nhận lần lượt:

```text
11-15 23:48:29.910 D houdini : [4840] Initialize library(version: 9.0.7a_z.38597 RELEASE)... successfully.
11-15 23:48:30.672 V libnb : enter native_bridge3_loadLibraryExt .../lib/arm64/libc++_shared.so, 2, 0x3
11-15 23:48:30.705 V libnb : native_bridge3_loadLibraryExt: 0x76388bc1dac0
11-15 23:48:30.706 V libnb : enter native_bridge3_loadLibraryExt .../lib/arm64/libopenal.so, 2, 0x3
11-15 23:48:30.799 V libnb : native_bridge3_loadLibraryExt: 0x76388bc1e580
11-15 23:48:30.875 V libnb : enter native_bridge3_loadLibraryExt .../lib/arm64/libjx1client.so, 2, 0x3
11-15 23:48:31.452 V libnb : native_bridge3_loadLibraryExt: 0x76388bc20060
11-15 23:48:31.453 D main : axmol_android_app_init
11-15 23:48:31.810 I axmol : Load GLES success, version: 30001
```

Đường dẫn cài ngẫu nhiên được rút gọn bằng `...`; không thay nội dung symbol hoặc thời điểm. Thông tin engine/renderer trong log:

```text
axmol.version: axmol-2.1.5
axmol.build_type: DEBUG
version: OpenGL ES 3.1 v1
glsl: OpenGL ES GLSL ES 3.10
renderer: Adreno (TM) 640
vendor: Qualcomm
```

Đây là chuỗi renderer do môi trường giả lập trả về, không kết luận đó là GPU vật lý của Windows. Ảnh màn hình xác nhận nền nhân vật, chữ tải, thanh tiến độ và hộp thoại được dựng; không chỉ có màn hình đen.

## Giao diện, lỗi và giới hạn kết luận

### Lỗi có ý nghĩa đầu tiên ở cấp ứng dụng

Ảnh local cho thấy màn hình tải đứng ở khoảng **6%**, dòng `package_vn.ini:545`, phía trên có hộp thoại lỗi chữ bị sai mã hóa, tiêu đề và nội dung không đọc được đáng tin cậy do sai mã hóa, nút `Ok`. Chưa thấy màn hình login, server list hoặc nhân vật. Không có hộp thoại cấp quyền Android được quan sát; không tự cấp quyền thêm.

Log tối thiểu liên quan:

```text
11-15 23:48:31.924 4840 4899 D axmol debug info: start KUpdateLayer
11-15 23:48:31.924 4840 4899 D axmol debug info: end KUpdateLayer
11-15 23:48:32.952 4840 4899 D axmol debug info: /data/user/0/com.kull.jx1client/files/data/package_vn.ini
```

Không có stack trace crash để đính kèm. Log hiện có chưa nêu rõ lỗi tải dữ liệu nào tạo hộp thoại; không khẳng định PAK thiếu hoặc CDN lỗi chỉ từ ảnh. `package_vn.ini:545` là nội dung UI nhìn thấy, không phải bằng chứng tải từ server thành công.

Đã đọc chọn lọc bản copy AMOLX-04 nhằm hiểu hành vi lúc mở, không chạy lại protocol audit:

- `client/Source/AppDelegate.cpp:85`: scene đầu là `KUpdateLayer`.
- `client/Source/gamecore/KCore.cpp:96`: `_clientNoNetWork=false`.
- `client/Source/gamescene/KUpdateLayer.cpp:126`: nhánh khởi tạo updater; `:140–147` tạo downloader và gọi `startload()`; `:440` xử lý các trạng thái lỗi; `:685–687` có đường tải danh sách PAK.

Các đoạn này cho thấy startup có cơ chế updater tự chạy. Không kiểm thử hoặc chứng nhận kết nối updater; không thu packet hay thử endpoint. Chưa xác định chắc chắn nhánh runtime nào sinh hộp thoại, vì chữ lỗi hỏng và log còn thiếu. Không sửa source hoặc dữ liệu để vượt màn hình này.

### Cảnh báo emulator/đồ họa

```text
11-15 23:48:29.803 W nativebridge: Failed to bind-mount /data/local/cfg-nzgah/ as /proc/cpuinfo: Not a directory
11-15 23:48:31.694 E eglCodecCommon: glUtilsParamSize: unknow param 0x000082da
11-15 23:48:31.792 E EGL_emulation: tid 4900: eglSurfaceAttrib(1493): error 0x3009 (EGL_BAD_MATCH)
11-15 23:48:31.792 W OpenGLRenderer: Failed to set EGL_SWAP_BEHAVIOR on surface ..., error=EGL_BAD_MATCH
D HostConnection: glGetError exceeded.
```

Các cảnh báo xuất hiện trong môi trường LDPlayer nhưng native init và màn hình nền vẫn hoạt động. Chưa có bằng chứng chúng là nguyên nhân hộp thoại updater; không đổi renderer hoặc cấu hình emulator để thử sửa trong task này.

## Bằng chứng local và bảo vệ dữ liệu

- Ảnh đã xem trực tiếp: `C:\Jx1CocoV3\amolx-work\AMOLX-05-20261115\launch-screen.png`, PNG `1920×1080`, `1484031` bytes.
- Ảnh được lấy bằng SDK ADB `exec-out screencap -p`, ghi file local từ byte PNG; không ghi file tạm vào vùng dữ liệu Android và không upload ảnh.
- Logcat đọc có mốc bắt đầu và lọc package/PID/native crash; không chạy `logcat -c`, không xóa log thiết bị. Báo cáo chỉ trích dòng cần thiết, không chứa account/password/token hoặc dữ liệu ứng dụng khác.
- Không uninstall, clear-data, xóa cache, factory-reset, sửa file dữ liệu emulator hoặc thay phiên bản LDPlayer.
- Không sửa source AMOLX/Cocos/server, không build lại APK, không tác động Main VM/production, firewall, Tailscale, router, Dispatcher/Scheduler hoặc cấu hình model.
- Git workspace trước khi ghi: nhánh `master`, `docs-analysis/BAI_HOC.md` đã modified và có nhiều file untracked từ task trước. Giữ nguyên toàn bộ; không stage/commit chúng. Repository báo cáo `jx1-reports/main` được cập nhật riêng bằng kết nối GitHub hiện có.

## Phần chưa thử và task tiếp theo

| Phần | Trạng thái / lý do |
|---|---|
| Network/game server/handshake/login | **NOT-TESTED**, ngoài phạm vi được duyệt; không gọi là kết nối thành công |
| Login UI / server selection | Chưa tới; dừng ở hộp thoại updater, không bấm tiếp |
| Chọn nhân vật / vào bản đồ / gameplay | Chưa thử, ngoài smoke-test |
| Toàn bộ asset/PAK | Chưa xác minh; mới thấy tài nguyên màn hình khởi tạo |
| Âm thanh phát thực tế | Chưa thử; chỉ xác nhận libopenal load được |
| Xoay portrait/landscape | Chưa thử; giữ màn hình landscape sẵn có, không thay cấu hình |
| Thiết bị ARM64 thật / LDPlayer khác | Chưa thử; chỉ cài đúng một LDPlayer 9 |
| Ổn định dài hạn hoặc restart/reboot | Chưa thử; một lượt launch và quan sát hữu hạn |
| Sửa mã hóa / updater / EGL | Chưa thực hiện; task này chỉ ghi nhận lỗi |

Task tiếp theo nên khoanh vùng `KUpdateLayer`/`downloadFile`, cấu hình và tài nguyên updater, đồng thời truy nguyên chuyển mã chuỗi thông báo. Cần một nhiệm vụ được duyệt riêng nếu muốn bổ sung log hoặc sửa bản copy source để hiển thị lỗi rõ ràng/đạt màn hình login. Giữ kết nối game và credential ngoài bước đó trừ khi được cho phép riêng.

## Công bố và bàn giao

- Chỉ file `TEST_RESULTS/AMOLX-LDPLAYER9-SMOKE-20261115.md` thuộc thay đổi GitHub của task.
- Nhánh đích: `ndtangoss-dev/jx1-reports/main`.
- Main trước công bố: `b69d6c1f42dc2c5dde0ee71bbc4d1f0da0270226`.
- Link báo cáo: https://github.com/ndtangoss-dev/jx1-reports/blob/main/TEST_RESULTS/AMOLX-LDPLAYER9-SMOKE-20261115.md
- SHA commit mới được GitHub cấp khi ghi báo cáo; phản hồi bàn giao cuối cung cấp SHA và kết quả đọc lại nội dung từ GitHub. Không tự điền SHA chưa tồn tại vào báo cáo.
