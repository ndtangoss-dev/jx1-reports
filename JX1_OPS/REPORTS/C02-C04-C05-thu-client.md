# C02 / C04 / C05 — thử client thật trên Test-36 (#216, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] C02: sai mật khẩu và tài khoản lạ đều bị từ chối ở màn đăng nhập (ảnh `ANH/t36-c02-1-sai-mk.png`, `t36-c02-2-tk-la.png`); đăng nhập đúng (`testa`) vào được chọn nhân vật rồi vào game (`t36-c02-3-dang-nhap-dung.png`). Hai ca CẦN CHỦ (tài khoản hết hạn, lệch version) **CHƯA LÀM**.
2. [ĐÃ KIỂM] C04: bấm Send "Notify all player" ở Bishop (kiểu không dấu `*`, "Delivered to all servers") với câu ASCII; client hiện một dòng đỏ "Công bố: …" trong khung chat dưới màn hình, không có banner giữa màn (`ANH/t36-c04-cong-bo-ascii.png`). Client thứ hai (Bot) **CHƯA quan sát**: mới có một client thật online.
3. [ĐÃ KIỂM] C05: câu có dấu gửi từ ô Announcer bị vỡ (`Th? ti?ng Vi?t cú d?u: é?i hi?p, chổ m?ng!`, ảnh `ANH/t36-c05-cong-bo-dau.png`). Nguyên nhân khả dĩ [GIẢ THUYẾT]: Bishop là ứng dụng ANSI, hệ thống VM không phải mã trang Việt nên ký tự ngoài bảng mã thành `?`; chưa thử đổi locale.
4. Bằng chứng: client = APK debug SHA-256 `7894c22d08491facbe909c17f00fd31b034a89eeb4894730f0d3f1ad57cec2d8` (bản qh9A), LDPlayer `T36test` (bản copy), CDN tạm + DNAT trong LD tới host-only 192.168.56.101; không động tới Main VM. Lúc đầu cài nhầm bản release `47EB28E3` có nối 103.228.37.206:80 một thời gian ngắn, đã gỡ.
5. Cần tôi quyết định: không.

## Cách làm
- Bấm Send không qua ảnh chụp: tác vụ lập lịch tương tác chạy bằng user `mu1` (chủ phiên desktop VM) gửi `WM_SETTEXT` vào ô 1020, chọn nút 1023 "Notify all player" + 1018, `WM_COMMAND` tới nút 1021 Send. Tác vụ `JX-Lietke`/`JX-Gui` tạo trong Test-36 (gỡ khi dọn).
- Kết quả dùng chung nhịp gs001; không có lỗi, gs001 vẫn chạy.
