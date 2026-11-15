# AMOLX-05 — Cài và kiểm thử khởi động APK trên LDPlayer 9

Task ID: AMOLX-05-LDPLAYER9-SMOKE-TEST-20261115
Executor: Codex CLI trực tiếp trong phiên hiện tại. Giữ nguyên Sol Max.
Mục tiêu: dùng LDPlayer 9 đã được người dùng xác nhận đang cài và đã khởi động để kiểm tra APK AMOLX-04. Người dùng đã cho phép Codex tự thao tác kiểm thử trên emulator này.

## Nguồn đã có — không làm lại

Báo cáo build: `TEST_RESULTS/AMOLX-CONNECT-APK-20261115.md`

APK đã build thành công:
- File: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk`
- Package: `com.kull.jx1client`
- Version: 1.0 / versionCode 1
- ABI: arm64-v8a
- SHA-256: `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1`
- APK đã verify chữ ký debug và ZIP integrity.
- APK này chưa được cài/mở trên LDPlayer; báo cáo AMOLX-04 không thấy LDPlayer process tại thời điểm kiểm tra.

## Phạm vi được phép

Người dùng xác nhận LDPlayer 9 đã cài và đang chạy, đồng ý để Codex tự kiểm thử trên emulator đó. Được phép:
- Dùng ADB chính thức đã có trong Android SDK để liệt kê thiết bị, nhận diện đúng instance LDPlayer 9, cài APK, mở app, thu thập logcat và ảnh/log cần thiết.
- Kiểm tra ABI/Android version/package hiện có.
- Nếu package `com.kull.jx1client` đã được cài: kiểm tra version/signature và dữ liệu hiện có trước; KHÔNG uninstall, clear data, replace/upgrade hoặc ghi đè app hiện có nếu có nguy cơ mất dữ liệu. Nếu cùng package đã tồn tại và việc cập nhật có thể ảnh hưởng dữ liệu, dừng trước thao tác ghi đè, báo người dùng.
- Nếu không có package đó, cài APK bằng ADB vào đúng LDPlayer 9.
- Mở app, chờ khởi tạo, kiểm tra màn hình đầu/login, crash/ANR, native library load, renderer và logcat. Thử portrait/landscape chỉ nếu app tự hỗ trợ; không thay cấu hình emulator tùy tiện.
- Nếu app tự kết nối tới game server khi khởi động, không gửi login hoặc credential; không tiếp tục sang kết nối game. Có thể kiểm tra UI tới màn hình login nhưng dừng trước thao tác đăng nhập.

## Rào chắn

- Chỉ thao tác trên LDPlayer 9 đã được người dùng xác nhận. Không dùng Main VM, production server, thiết bị Android thật hoặc emulator khác.
- Không kết nối TCP tới server game, không gửi packet, không login, không nhập account/password, không thử server selection có thể tạo kết nối.
- Không thay đổi firewall, port forwarding, Tailscale, router, VM, server process/config, Windows global settings hoặc credential.
- Không cài APK lên nhiều thiết bị. Nếu ADB có nhiều device và không nhận diện chắc chắn instance LDPlayer 9, chỉ báo serial và dừng; không chọn đại.
- Không gỡ app, clear data, xóa cache/user data, sửa dữ liệu emulator hoặc factory reset.
- Không tự cài thêm emulator hoặc thay đổi phiên bản LDPlayer.
- Không sửa Cocos canonical hoặc server. Không sửa source AMOLX trong smoke-test này; nếu phát hiện lỗi, ghi log/bằng chứng và đề xuất patch task kế tiếp.
- Không kiểm tra/sửa model/provider/reasoning/CODEX_HOME/CLI config. Không Dispatcher/Scheduler.

## Các bước thực hiện

1. Kiểm tra đúng một lần Git status nếu cần ghi file; giữ nguyên thay đổi local cũ.
2. Dùng `D:\Android\sdk\platform-tools\adb.exe` nếu tồn tại; nếu không, tìm ADB SDK đã dùng trong AMOLX-04, không cài lại toolchain.
3. `adb devices -l`; đối chiếu device với LDPlayer 9 đang chạy. Nếu nhiều instance hoặc không chắc chắn, dừng trước cài đặt.
4. Xác minh APK path, SHA-256 và package metadata; không build lại.
5. Kiểm tra package đã cài trên đúng emulator. Nếu chưa cài, cài APK. Nếu đã có, không ghi đè nếu có nguy cơ mất dữ liệu.
6. Khởi chạy app bằng package/activity đã xác minh (đọc manifest/aapt nếu cần). Thu thập logcat có lọc package và native crash. Đợi app ổn định; không lặp vô hạn.
7. Kết luận rõ:
   - INSTALL-OK / INSTALL-FAILED
   - LAUNCH-OK / CRASH / ANR / BLOCKED
   - UI tới được màn hình nào
   - Native renderer/library có load hay không
   - Lỗi đầu tiên có ý nghĩa, file/log/stack chính xác
   - Có yêu cầu quyền hoặc tài nguyên thiếu nào không
8. Không gọi đây là “kết nối server thành công”; phần network/login luôn ghi NOT-TESTED trong task này.

## Báo cáo cuối

Tạo đúng một báo cáo:
`TEST_RESULTS/AMOLX-LDPLAYER9-SMOKE-20261115.md`

Ghi:
- Emulator serial, Android version, ABI (không đưa thông tin cá nhân/credential).
- APK SHA-256, package/version.
- Lệnh install/launch và exit/result.
- Kết quả install, launch, UI, native libs, crash/ANR.
- Logcat/stack trace đã lọc secret.
- Package đã tồn tại hay chưa; nếu không cài do bảo vệ dữ liệu, ghi rõ.
- Các bước chưa thử và lý do.
- Trạng thái DONE/PARTIAL/BLOCKED/FAILED.
- Commit SHA/link.

Push duy nhất báo cáo đã lọc secret lên `ndtangoss-dev/jx1-reports` nhánh `main`. Không upload APK, source, log thô hoặc dữ liệu emulator. Không stage/commit file khác.

## Điều kiện hoàn tất

Hoàn thành smoke-test cài/mở trên đúng LDPlayer 9 hoặc nêu blocker chính xác. Không dừng chỉ để báo tiến độ/lỗi trung gian; xử lý lỗi an toàn trong phạm vi, tối đa 3 lần mỗi lỗi.