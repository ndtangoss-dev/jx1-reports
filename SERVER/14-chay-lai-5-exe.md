# Chạy lại 5 exe sau lần tắt cứng VM

## TÓM TẮT 5 DÒNG
1. Cả 5 exe đã chạy lại theo yêu cầu của chủ máy. 8 cổng cần kiểm tra đều đang nghe.
2. `gs001` báo `Server start succeeded`, địa chỉ gửi cho client là địa chỉ Tailscale máy thật, nối gateway qua `<LAN-IP>`.
3. Vẫn 772 bản đồ nạp được, 28 lỗi như trước.
4. Không exe JX nào bị chặn ra Internet trong 20 phút gần nhất, Defender 0 phát hiện.
5. Chưa mở cổng Tailscale, không tạo snapshot, chưa có client thật kết nối.

Cần tôi quyết định: có

## Đã làm
- Thêm scheduled task `JX-Sword3PaySys` và luật `JX no-in Sword3PaySys`, để exe này khởi động giống các exe khác, không hiện hộp thoại tường lửa.
- Thứ tự: `Sword3PaySys`, `Goddess` (Start), `S3Relay` (login root, `<service-account>`), `Bishop` (Login `<service-account>`, Startup bằng `WM_COMMAND`), `gs001`.

## Bằng chứng
- `Sword3PaySys`: nghe 5002, 1000 kết nối tới SQL 1433.
- `Bishop` Established tới 5001, 5002; `S3Relay`: `Initialize OK`, `gateway client create`.
- `gs001` Established tới 5001, 5003, 5004, 5005, 56732 tại `<LAN-IP>`.
- Cổng đang nghe: 5001, 5002, 5003, 5004, 5005, 51189, 56722, 56732.
- Sự kiện 5157: 0 dòng của exe JX. `Get-MpThreatDetection`: 0.

## Lỗi đã gặp
Không có.

## Bước kế
Chủ máy chạy `tailscale_mo_cong.ps1 -WithCdn`; chạy `cdn_server.py` khi được cho phép; cài APK lên điện thoại.
