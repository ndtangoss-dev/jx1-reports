# Thử client thật trên điện thoại qua Tailscale

## TÓM TẮT 5 DÒNG
1. Điện thoại đã tải dữ liệu, đăng nhập `<test-account>` và chơi trong game qua Tailscale.
2. Server ghi 2 phiên: 19:30:27 đến 19:40:46 và 19:41:22 đến 19:43:41, `gs001` có `Online = 1`.
3. Ba lỗi đã sửa trên đường đi: cổng 80 bị `ReportServer` giữ, gốc CDN sai, thiếu `Account_Habitus`.
4. Không exe JX nào bị chặn ra Internet trong 1 giờ gần nhất, Defender 0 phát hiện. Server vẫn chạy đủ 5 exe.
5. `roledb` vẫn 8192 byte, nên chưa xác nhận được nhân vật đã lưu xuống đĩa.

Cần tôi quyết định: có

## Bằng chứng
- `Sword3PaySys`: `User <test-account> Login nVipType:0 ... Login Suc` lúc 19:30:27 và 19:41:22, `Logout: Success` lúc 19:40:46 và 19:43:41.
- Console `gs001`: `[Online= 1]` lúc 19:42, 19:43; `[Online= 0]` lúc 19:44.
- Log CDN: 34 yêu cầu `.pak` của điện thoại, không có lỗi 4xx hay 5xx (kiểm tra lúc trước khi đăng nhập).
- Chủ máy xác nhận đã chơi khoảng 5 phút trong game.

## Lỗi đã sửa
- Cổng 80 trên máy thật do `ReportServer` giữ: chủ máy tạm dừng dịch vụ.
- CDN đặt gốc `data_cdn\data` trong khi client gọi `/data/...`: đổi gốc thành `data_cdn`.
- `<test-account>` thiếu dòng `Account_Habitus` (`No Money`): thêm dòng, hạn 365 ngày.

## Chưa kiểm tra
- Nhân vật có được lưu qua lần khởi động lại `Goddess` không.
- 28 bản đồ thiếu dữ liệu, cổng root 7777: chưa có hiện tượng lỗi nào được ghi nhận, chưa thử riêng.

## Hiện trạng
- `cdn_server.py` vẫn chạy (PID 25728), sau khi tác vụ nền hết hạn. Game cần CDN mỗi lần khởi động.
- Cổng 56722, 51189, 80 mở cho đúng địa chỉ điện thoại. `ReportServer` đang tắt.
- `S3RelayServer.exe` chưa chạy.
