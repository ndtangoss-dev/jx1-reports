# 21 - Đăng ký tự khởi động TCP Forwarder

Ngày: 2026-11-11

## TÓM TẮT 5 DÒNG
1. Đã đăng ký tác vụ `JX-Forwarder-Tailscale` bằng `dang_ky_forwarder.ps1`, một lần thử, không cần Admin.
2. Tác vụ chạy dưới tài khoản `<hostname>\PC`, LogonType Interactive, RunLevel Limited, kích hoạt khi tài khoản này đăng nhập.
3. Sửa 2 lỗi trong script trước khi đăng ký: thêm `Wait-Process` để tác vụ ở lại chờ forwarder, và cho phép chạy khi dùng pin.
4. Forwarder PID 18888 và CDN PID 18284 vẫn chạy, 3 cổng vẫn nghe đúng địa chỉ Tailscale, không có listener 0.0.0.0, portproxy không đổi.
5. Chưa reboot thử: tác vụ chưa từng chạy (`LastRun` trống, kết quả 267011 = chưa chạy).

**Cần tôi quyết định: không.**

## Giai đoạn 1-2: kiểm tra script
- Cú pháp: cả 3 script và `dung_forwarder.ps1` không lỗi (`Parser::ParseFile`).
- Không có `netsh`, `NetFirewall`, `portproxy` (chỉ trong chú thích và thông báo), `RunLevel Highest`, `SYSTEM`, `Stop-Service`, `Restart-Service`.
- Phiên hiện tại không phải Admin (`IsInRole(Administrator)` = False).
- Chờ Tailscale: vòng lặp `ipconfig` tìm `<TAILSCALE-IP>`, 5 giây một lần, tối đa 180 giây, quá hạn thì thoát mã 2 và ghi log.
- Chống chạy trùng: nếu `<TAILSCALE-IP>:56722` hoặc `:51189` đã LISTENING thì thoát mã 3. Đã đối chiếu biểu thức này với `netstat` hiện tại: cả hai cổng đang nghe, nên script sẽ chặn. Tác vụ cũng đặt `MultipleInstances IgnoreNew`.
- Log: `docs-analysis/out/khoi-dong-forwarder.log` (script) và `forwarder.log`, `forwarder.err.log` (forwarder). Chú ý: mỗi lần script khởi động forwarder, `forwarder.log` bị ghi đè.
- Điều kiện kết nối trong script: bind `<TAILSCALE-IP>`, chỉ nhận `<TAILSCALE-IP>`, chuyển tiếp 56722→`<LAN-IP>:56722`, 51189→`<LAN-IP>:51189`. `tcp_forwarder.py` từ chối bind `0.0.0.0` hoặc `::` (dòng 106-107) và đóng nguồn khác (dòng 50-53).
- Dừng: `dung_forwarder.ps1` đọc PID trong `docs-analysis/out/forwarder.pid`, chỉ dừng tiến trình có dòng lệnh chứa `tcp_forwarder.py`.

## Lỗi đã sửa trước khi đăng ký
- Script cũ chỉ `Start-Process` rồi thoát. Task Scheduler có thể dọn tiến trình con khi tác vụ kết thúc, nên forwarder có thể chết ngay. Đã thêm `$p | Wait-Process`: tác vụ ở trạng thái Running chừng nào forwarder còn sống. Điều này chưa kiểm chứng bằng reboot.
- Đã thêm `-AllowStartIfOnBatteries -DontStopIfGoingOnBatteries` vào cài đặt tác vụ.

## Giai đoạn 3-4: đăng ký và kiểm tra
- Tên: `JX-Forwarder-Tailscale`. Trạng thái `Ready`, `Enabled`. Đúng 1 tác vụ tên `JX-Forwarder*`.
- Trigger: `MSFT_TaskLogonTrigger`, user `<hostname>\PC`, bật.
- Action: `powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Jx1CocoV3\docs-analysis\scripts\khoi_dong_forwarder.ps1"`. Script tồn tại.
- Quyền: Principal `PC`, Interactive, Limited. ExecutionTimeLimit `PT0S`, StartWhenAvailable bật.
- Log khởi động: chưa có file vì tác vụ chưa chạy.
- Tiến trình: 18888 (forwarder, từ 10:10:37) và 18284 (CDN, từ 09:37:00) vẫn chạy. `netstat` thấy `<TAILSCALE-IP>` nghe cổng 8080 (18284), 51189 và 56722 (18888). Không có listener `0.0.0.0` trên 3 cổng. `forwarder.log` vẫn ghi phiên điện thoại lúc 10:52-10:55 (phiên 51189 dài 181,2 giây).
- `portproxy` không đổi (hai luật cũ). Không đụng Firewall, SQL, 5 exe, VM, VM cũ, snapshot.

## Hoàn tác
- Chạy `docs-analysis\scripts\huy_dang_ky_forwarder.ps1`: xóa tác vụ `JX-Forwarder-Tailscale`. Không dừng forwarder đang chạy.
- Dừng forwarder: `docs-analysis\scripts\dung_forwarder.ps1`.

## Chưa kiểm tra
- Hành vi thật sau khi Windows khởi động lại và đăng nhập: có chờ được Tailscale, có thoát mã 3 nếu portproxy tự nghe, tác vụ có giữ forwarder sống hay không.
- Nếu forwarder hiện tại (18888) còn chạy lúc tác vụ kích hoạt, tác vụ sẽ thoát mã 3 và không làm gì.
