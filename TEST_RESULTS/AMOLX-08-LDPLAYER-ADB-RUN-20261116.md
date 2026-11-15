# AMOLX-08 - Chạy ADB trên LDPlayer 9

**Trạng thái: PARTIAL / BLOCKED**  
**Ngày:** 2026-11-16 (Asia/Bangkok)

## Đã thực hiện

- Đọc prompt `PROMPTS/AMOLX-08-LDPLAYER-ADB-RUN-20261116.md` từ `ndtangoss-dev/jx1-reports` (blob `6edbc3a3d03732a16273a573296e8b04cda7f456`).
- Kiểm tra script đã chuẩn bị tại `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\run-amolx07-smoke.ps1`. Prompt ghi một vị trí dưới `client\build`, nhưng script thực tế nằm trong thư mục `build` cạnh `client`; đường dẫn APK trong script vẫn trỏ đúng APK AMOLX-07.
- Chỉ chạy script trên. Script xác nhận tiến trình LDPlayer 9 tại `C:\LDPlayer\LDPlayer9\dnplayer.exe`, ADB serial `emulator-5554` ở trạng thái `device`, và SHA-256 APK AMOLX-07 khớp giá trị được duyệt: `7FC4CCBC1B7DCFE1806E474888169239519B713D2C681A45F8E371389659E7B1` (60,602,044 bytes).
- Package `com.kull.jx1client` đã được cài trước đó. Script kéo `base.apk` từ emulator vào `amolx-work\AMOLX-04-20261115\build\amolx07-installed-before.apk` và xác nhận SHA-256 khớp APK AMOLX-04 đã biết: `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1`. Tệp backup được giữ lại và không đưa lên GitHub.

## Kết quả chạy

- Cập nhật bằng `adb install -r` thất bại: `INSTALL_FAILED_UPDATE_INCOMPATIBLE: Package com.kull.jx1client signatures do not match previously installed version`.
- Không gỡ cài đặt, không xóa/clear dữ liệu và không thử vượt kiểm tra chữ ký. Lệnh cài đặt báo thất bại; trạng thái package sau đó không được truy vấn riêng. Không có lệnh nào trong script xóa dữ liệu ứng dụng.
- Script dừng sau lỗi cài đặt nên chưa mở game. Updater, đăng nhập và gameplay chưa được quan sát; không kết nối server.
- Log runtime chưa được tạo. Đường dẫn dự kiến: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx07-runtime-filtered.log`.
- Ảnh màn hình chưa được tạo. Đường dẫn dự kiến: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx07-screen.png`.
- Không build lại, sửa source hoặc thay đổi server, VM hay mạng.

## Trở ngại và bước tiếp theo

APK AMOLX-07 có chữ ký khác với bản AMOLX-04 đang cài, nên Android từ chối cập nhật khi giữ nguyên dữ liệu ứng dụng. Bước tiếp theo an toàn là chuẩn bị APK cùng application ID và được ký bằng cùng chứng chỉ với bản đang cài, rồi chạy lại cập nhật giữ dữ liệu. Chưa thể kết luận updater hoạt động từ lượt này.

**Chưa hoàn thành:** cài APK AMOLX-07, mở game, thử updater, đăng nhập/gameplay, thu log runtime và ảnh màn hình.  
**Cần người dùng quyết định:** có - cung cấp/cho phép dùng khóa ký tương thích để tạo APK cùng chữ ký, hoặc phê duyệt phương án cài riêng sau khi đánh giá việc giữ dữ liệu.