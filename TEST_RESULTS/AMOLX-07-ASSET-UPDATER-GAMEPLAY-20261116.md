# AMOLX-07 — Asset, updater và gameplay

- Ngày: 16/11/2026.
- Prompt đã thực hiện: `PROMPTS/AMOLX-07-ASSET-UPDATER-GAMEPLAY-20261116.md`, blob `a7c3a55db52e5e373d762bd845cb86ef6e7f53d2` trên `main`.
- Trạng thái: **PARTIAL**.
- Kết luận: đã build APK debug mới và xác minh package/ABI/hash. Chưa cài APK mới lên LDPlayer, chưa chạy updater, chưa đến login và không kết nối server game. Hai lượt duyệt tự động để chạy script ADB có điều kiện đều hết thời gian; không có kết quả từ script.

## Kết quả từng mốc

| Mốc | Trạng thái | Bằng chứng |
|---|---|---|
| Asset/manifest | Chưa hoàn tất | Không tạo manifest giả và không copy PAK. Checkpoint đọc-only trước đó xác nhận CDN Cocos có `data/paklist.ini` (HTTP 200, khớp hash với manifest local), còn `data/paklist_vn.ini` (HTTP 404). Tương thích PAK AMOLX/Cocos và tập nhỏ nhất đủ cho bản đồ chưa được chứng minh. |
| Sửa updater | Đã sửa trong bản sao AMOLX | Đồng bộ state tải thành công với state 5 mà vòng PAK chờ; thêm log HEAD/GET đã lọc host, HTTP/CURL, content length, số byte ghi, lỗi mở/ghi; giới hạn thử lại manifest và PAK ở 3 lần. Chỉ kiểm tra tĩnh/biên dịch, chưa có log runtime mới. |
| Build APK | Đạt | Gradle 8.7, `assembleDebug`, offline; `BUILD SUCCESSFUL` trong 1 phút 27 giây, 65 tác vụ (13 chạy, 52 up-to-date). CMake đã biên dịch mã nguồn AMOLX. |
| Cài APK mới | Bị chặn | ADB `get-state` xác nhận serial đã dùng ở AMOLX-05 trả `device`. Lệnh đọc package trong sandbox tiếp tục bị chặn khi ADB tạo thư mục `.android`. Script kiểm tra hash APK AMOLX-04 trước khi cài đè đã được viết và kiểm tra cú pháp, nhưng hai lần yêu cầu chạy ngoài sandbox hết thời gian duyệt tự động; script không chạy. Không gỡ app, không xóa hay sửa app data. |
| Launch/updater | Chưa kiểm thử | APK mới chưa được cài/mở. Không tuyên bố đã vượt updater. |
| Login/server list/nhân vật/map/gameplay | Chưa thực hiện | Không có phiên đăng nhập, không dùng credential, không gửi kết nối gameplay tới server. |

## Thay đổi trong workspace

- `amolx-work/AMOLX-04-20261115/client/Source/engine/KDownLoadFile.cpp`: sửa trạng thái hoàn tất GET; log lỗi HEAD/GET, HTTP/CURL và ghi file, không ghi URL/host vào log.
- `amolx-work/AMOLX-04-20261115/client/Source/engine/KDownLoadFile.h`: giữ hợp đồng enum trạng thái hoàn tất ở giá trị 5.
- `amolx-work/AMOLX-04-20261115/client/Source/gamescene/KUpdateLayer.cpp`: kiểm tra số mục manifest, log kết quả parse và dừng sau tối đa 3 lần thử manifest/PAK.
- `amolx-work/AMOLX-04-20261115/client/Content/package_vn.ini`: bản sao AMOLX trỏ đến CDN Cocos đã được xác minh ở checkpoint; địa chỉ đã lược khỏi báo cáo. Không sửa CDN hay asset gốc.
- `amolx-work/AMOLX-04-20261115/build-amolx04.ps1`: dùng Gradle cache, temp và Android user-home trong thư mục task; build offline, không đổi biến môi trường toàn hệ thống.
- `amolx-work/AMOLX-04-20261115/build/run-amolx07-smoke.ps1`: script có điều kiện để xác minh emulator và SHA APK AMOLX-04 trước khi cài đè bảo toàn dữ liệu, mở app, lọc log và chụp màn hình. Script chưa được thực thi.

Các thay đổi trên chỉ nằm trong bản sao AMOLX/build của workspace. Cocos canonical, source server, CDN gốc, VM/Main VM, firewall và cấu hình mạng không bị sửa hoặc khởi động lại. Không PAK nào được tải hoặc chép vào emulator.

## Build và APK

- Log build thành công: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\rebuild-20261116-024246.log`.
- APK: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\proj.android\app\build\outputs\apk\debug\jx1client-debug.apk`.
- Kích thước: 60,602,044 byte.
- SHA-256: `7FC4CCBC1B7DCFE1806E474888169239519B713D2C681A45F8E371389659E7B1`.
- Package/version: `com.kull.jx1client`, `1.0`, versionCode `1`; ABI `arm64-v8a`; minSdk 17, targetSdk 34.
- `aapt dump badging` xác nhận package, activity và ABI. Kiểm tra ZIP xác nhận APK không chứa `.pak` hay `paklist`; asset vẫn phụ thuộc updater.
- Build thành công nhưng còn cảnh báo định dạng `%u` với `size_t` tại `KUpdateLayer.cpp:611,620` và `sleep(0.5)` bị đổi thành 0 trên nhánh Android/Linux tại các dòng 738, 754, 841. Không sửa các cảnh báo ngoài mục tiêu chính trong lượt này.

## Lỗi và giới hạn

- Lỗi native-platform của Gradle được xử lý bằng Gradle user-home/temp riêng trong workspace. Sau đó lỗi cấu hình Android preferences do đồng thời đặt `ANDROID_SDK_HOME` và `ANDROID_USER_HOME` được xử lý bằng cách chỉ dùng `ANDROID_USER_HOME` riêng. Cache dependency còn thiếu được bổ sung từ cache Gradle có sẵn; không tải dependency qua mạng.
- Checkpoint updater cho thấy AMOLX yêu cầu manifest tiếng Việt không có trên CDN Cocos đã kiểm tra. Chưa đổi sang manifest đầy đủ vì sẽ kéo theo nhiều PAK, trong khi chưa xác minh tương thích và chưa chọn được tập nhỏ nhất đủ login/map.
- Không thu được HTTP/CURL status, byte count, ảnh màn hình hay log updater của APK mới vì bài smoke-test chưa chạy. Các mã 200/404 ở trên là kết quả kiểm tra checkpoint trước runtime, không phải kết quả chạy APK mới.
- Không xác định/kiểm tra lại endpoint server game trong lượt này. Không thử host/cổng phỏng đoán, không kết nối VM/server và không dùng credential.
- Báo cáo này là đầu ra tổng hợp duy nhất của AMOLX-07. APK, cache, log build, script test và ảnh (nếu có sau này) không được đưa lên GitHub.

## Bàn giao

- Phần đạt: sửa lỗi state/log/retry trong bản sao AMOLX; build APK ARM64 thành công; xác minh hash và metadata.
- Phần còn dang dở: cài/mở APK mới và thu bằng chứng updater bị chặn ở bước runtime. Do đó login, server selection, nhân vật và map chưa được thử.
- Commit SHA tạo bản báo cáo đầu tiên: `5b9717c4329452621e70426fdef0ac7e1041bb5b`. Commit cuối cùng của bản cập nhật metadata được bàn giao trong phản hồi vì SHA mới tự tham chiếu không thể nhúng vào chính commit đó.
- Link GitHub đã xác minh: https://github.com/ndtangoss-dev/jx1-reports/blob/main/TEST_RESULTS/AMOLX-07-ASSET-UPDATER-GAMEPLAY-20261116.md
- Chỉ báo cáo này được push. Bản sao source AMOLX, script kiểm thử, APK, build cache và log vẫn ở workspace; không đẩy cả source tree hoặc artifact vào repository báo cáo.
- Cần tôi quyết định: **có** — cho phép chạy script ADB đã kiểm tra cú pháp ngoài sandbox nếu lượt duyệt tự động tiếp tục hết thời gian; script chỉ thao tác trên LDPlayer 9 đã xác định, không xóa app data và dừng nếu hash ứng dụng cài không khớp AMOLX-04.
