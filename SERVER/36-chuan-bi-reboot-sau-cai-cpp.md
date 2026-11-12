# 36 - Chuẩn bị khởi động lại Windows sau khi cài C++ Build Tools

## TÓM TẮT 5 DÒNG
1. C++ Build Tools đã cài (mã 3010 = cần khởi động lại, `cl.exe` đã thấy). Tôi chưa khởi động lại máy.
2. `JX-Server-D` đang chạy (6 thành phần). Chưa tắt; sẽ tắt bằng ACPI khi chủ máy bảo, mất khoảng 90 giây.
3. CDN (PID 4612, `<TAILSCALE-IP>:8080`) và forwarder (PID 16736, cổng 56722/51189) đang chạy; cả hai có task đăng nhập `PC`, sẽ tự lên sau reboot nếu `PC` đăng nhập và Tailscale có địa chỉ.
4. 6 exe trong VM KHÔNG tự lên sau reboot (task không có trigger, autologon tắt): bật lại VM và từng exe cần chủ máy duyệt, gs001 nạp khoảng 7 phút, không được nối cổng 51189 trong lúc nạp.
5. Không đổi cấu hình, không tắt VM, không commit.

Cần tôi quyết định: có - thời điểm tắt `JX-Server-D` (ACPI) rồi reboot. Chủ máy báo "tắt VM" thì tôi chạy ACPI và chờ `poweroff`.

## 1. Trạng thái hiện tại (đọc lúc chuẩn bị, chưa thay đổi gì)
| Mục | Trạng thái | Bằng chứng |
|---|---|---|
| `JX-Server-D` | `running`, ACPI bật; là VM duy nhất đang chạy | `VBoxManage list runningvms`, `showvminfo` |
| `JX-Server` (lưu trữ) | không chạy | không có trong `runningvms` |
| Task `JX-CDN-8080` | Running, trigger đăng nhập, user `PC`, Interactive | `Get-ScheduledTask` |
| Task `JX-Forwarder-Tailscale` | Running, trigger đăng nhập, user `PC`, Interactive | như trên |
| Cổng nghe | 8080 (PID 4612), 56722 và 51189 (PID 16736) trên `<TAILSCALE-IP>`; cổng 80 do PID 4 (`ReportServer`, không đụng) | `netstat -ano` |
| Windows chờ reboot | khóa `RebootPending` của Component Based Servicing = False; nhưng installer VS đã trả 3010 | registry, log cài |
| Ổ đĩa | C: trống 151,1 GB, D: trống 1.491 GB | `[IO.DriveInfo]` |
| File CDN cần có | `docs-analysis/out/tailscale/update10.pak` (10.882.596 byte) và `data_cdn` có thật | `Get-Item` |

**Chưa kiểm tra:** bên trong VM có người chơi nào đang online không, và console `gs001` có đang ghi dữ liệu không. Tôi không có mật khẩu WinRM của `<vm-admin>` nên không vào VM được (đã thử mở phiên, bị hỏi mật khẩu, tôi đã hủy). Trước khi ACPI, chủ máy nên đảm bảo điện thoại đã thoát game.

## 2. Tắt `JX-Server-D` an toàn
- Lệnh: `VBoxManage controlvm JX-Server-D acpipowerbutton`, rồi chờ `VMState="poweroff"` (lần trước 92 giây, Windows trong VM tự chạy shutdown đầy đủ, SQL Server đóng sạch; xem báo cáo 26 mục 3).
- Không dùng `savestate` (từng làm `VBoxSVC` crash) và không dùng `poweroff` cưỡng bức, trừ khi chủ máy duyệt sau khi ACPI quá 5 phút.
- Rủi ro: ACPI đóng cả 5 exe game cùng lúc; Goddess có thể đang ghi nhân vật. Cách giảm: thoát game trên điện thoại trước, đợi khoảng 1 phút rồi mới ACPI.
- Tôi chỉ chạy lệnh khi chủ máy xác nhận. Không tạo snapshot (dự án đang tạm dừng snapshot).

## 3. Sau khi Windows bật lại
Tự động (nếu `PC` đăng nhập): `JX-CDN-8080` và `JX-Forwarder-Tailscale`. Hai script chờ địa chỉ Tailscale tối đa 180 giây, bỏ qua nếu cổng đã có người nghe, ghi log vào `docs-analysis/out/khoi-dong-cdn.log` và `khoi-dong-forwarder.log`. Forwarder đã qua một lần reboot trước đó (báo cáo 26/28). CDN: task có trigger đăng nhập, chưa có bằng chứng đã qua reboot.

Không tự động (cần chủ máy):
1. Bật `JX-Server-D` (`autostart` tắt).
2. Đăng nhập `<vm-user>` trong VM, chạy theo thứ tự SQL Server, `Sword3PaySys`, `Goddess` (Start), `S3Relay`, `Bishop` (Login, Startup), `gs001`. Chủ máy đã cho phép chạy 6 thành phần theo thứ tự này, tôi vẫn báo trước từng bước. Không chạy `S3RelayServer.exe`.
3. Đợi console `gs001` hiện "Server start succeeded" (khoảng 7 phút) mới được nối cổng 51189 hay mở game (báo cáo 29).

## 4. Khôi phục phiên làm việc
- Lệnh sau reboot: `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Jx1CocoV3\docs-analysis\scripts\quay_lai_jx1.ps1`
- Lời nhắc `quay_lai_jx1_prompt.txt` đã được viết lại cho đúng tình hình này (đọc báo cáo 36 mục 5, kiểm tra chỉ đọc, hỏi trước khi bật VM).

## 5. Việc làm tiếp sau reboot (chỉ đọc trước)
1. `Get-Item` tìm `cl.exe` và `where cl` trong "x64 Native Tools" để xác nhận trình biên dịch dùng được; kiểm tra Windows SDK, toolset v140, ATL/MFC có mặt.
2. CDN và forwarder: PID mới, cổng 8080/56722/51189 `LISTENING`, nội dung hai log khởi động.
3. `JX-Server-D` đang `poweroff`; `JX-Server` vẫn `poweroff`.
4. Hỏi chủ máy trước khi bật VM. Sau đó quay lại hai việc đang mở: nhánh biên dịch server 18/36 Hz (`D:\JX-build\src18`) và lỗi giật hình khi cưỡi ngựa với minimap (xem `HANDOVER-FIX34.md`).

## 6. Không làm trong bước này
Không khởi động lại máy, không tắt VM, không dừng CDN/forwarder, không đổi task, firewall, VirtualBox, WinRM, TrustedHosts, không xóa dữ liệu, không sửa source, không commit. Chỉ thêm báo cáo này và sửa `quay_lai_jx1_prompt.txt`.
