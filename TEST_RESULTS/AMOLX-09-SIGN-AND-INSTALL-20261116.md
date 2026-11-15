# AMOLX-09 - Ký APK và cập nhật trên LDPlayer 9

**Trạng thái: PARTIAL / BLOCKED tại updater**  
**Ngày:** 2026-11-16 (Asia/Bangkok)

## Kết quả

- Đã đọc prompt AMOLX-09 tại commit/blob `97e690695d28ffcbca1ddaf8ff614a65b2d09725`.
- APK AMOLX-04 đang cài được kéo từ emulator trong lượt trước và xác minh certificate SHA-256: `84341660dceade5c34308f2780a840fe87dfebf6be9d3edafec64e784fe85b7d`.
- Tìm thấy khóa Android debug tại `C:\Users\PC\.android\debug.keystore`; fingerprint certificate trùng khớp APK AMOLX-04. Hai debug keystore khác đã kiểm tra trong thư mục AMOLX và `D:\Android\user` không khớp. Không ghi mật khẩu hay private key vào log/báo cáo.
- Ký một bản sao APK AMOLX-07, không sửa APK gốc: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx07-signed-amolx04-20261116.apk`. `apksigner verify` xác nhận chữ ký APK mới; certificate SHA-256 khớp chính xác fingerprint AMOLX-04 ở trên. Package vẫn là `com.kull.jx1client`; SHA-256 APK đã ký: `EFBB58B19C586EEC708B8791F31F9A24115047550D902AB3BDE78935299A18C0`.
- `adb install -r` trên LDPlayer 9 `emulator-5554` thành công. Không gỡ cài đặt, xóa dữ liệu hay reset emulator. Activity `com.kull.jx1client/org.axmol.app.AppActivity` khởi động thành công.

## Quan sát khi chạy

- Game khởi tạo Axmol và mở giao diện splash/loading. Sau 25 giây, updater chưa tải được manifest; thanh tiến trình hiển thị 0% và có hộp thoại trong ảnh chụp màn hình. Không bấm nút hộp thoại.
- Log ghi ba lần `AMOLX_UPDATER stage=head file=data/paklist_vn.ini ... http=404`, sau đó `stage=manifest_fetch result=aborted attempts=3 state=3`.
- Log runtime đã lọc, che host/IP: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-runtime-filtered.log`.
- Ảnh chụp màn hình: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-screen.png`.
- Chưa đến login/gameplay. Không kết nối game server và không thay đổi server, VM, CDN hay mạng.

## Bước tiếp theo

Cần sửa nguồn phục vụ manifest để `data/paklist_vn.ini` trả về thành công cho client, hoặc cập nhật cấu hình client trỏ đến đường dẫn manifest đúng; sau đó lặp lại smoke test updater. Trong AMOLX-09 không thay đổi endpoint hay server.

**Hoàn tất:** tìm đúng signing identity, ký bản sao APK, xác minh certificate, cập nhật giữ dữ liệu, mở game, thu log và chụp màn hình.  
**Bị chặn:** updater dừng tại manifest HTTP 404; login và gameplay chưa được kiểm thử.