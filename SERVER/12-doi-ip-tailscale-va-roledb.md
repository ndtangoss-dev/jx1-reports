# Đổi IP gs001 sang Tailscale, thay roledb rỗng

## TÓM TẮT 5 DÒNG
1. `gs001_cfg.ini` đã đổi đúng 2 dòng `Ip` và `localIp` sang địa chỉ Tailscale máy thật.
2. `gs001` khởi động thành công, `public net IP` là địa chỉ mới, vẫn nối gateway qua `<LAN-IP>`.
3. `roledb` đã thay bằng bản rỗng; `Goddess` tự tạo (8 KB), khớp mã nguồn.
4. Server chạy đủ 5 exe, đủ 8 cổng. Không exe JX nào bị chặn ra Internet, Defender 0 phát hiện.
5. Chưa mở cổng Tailscale. Chưa thử client vì chưa có APK.

Cần tôi quyết định: có

## Đã làm
- Snapshot: `truoc-doi-ip-roledb` (UUID <uuid>).
- Chủ máy duyệt phương án "Làm cả hai".
- Tắt `gs001`, `Bishop`, `S3Relay`, `Goddess`. `Sword3PaySys` giữ nguyên.
- Sửa `gs\gs001_cfg.ini` theo byte, bản trước khi sửa ở `gs001_cfg.ini.truoc-tailscale`.
- Xóa `gw\database\roledb`, `roledb.0`, `log.0000000004`.
- Chạy lại `Goddess` (Start), `S3Relay` (login root), `Bishop` (Login, Startup), `gs001`.

## Bằng chứng
- So sánh trước và sau: khác đúng 2 dòng, L22 `localIp`, L23 `Ip`.
- `gw\database` sau khi `Goddess` Start: `roledb` 8192 byte, `roledb.0` 8192 byte, `log.0000000001`.
- Console `gs001`: `virtual IP` và `public net IP` là địa chỉ mới; `Gateway IP : <LAN-IP>`; `Connect to Gateway server OK`; `Server start succeeded`.
- `gs001` Established tới 5001, 5003, 5004, 5005, 56732 tại `<LAN-IP>`.
- `Map Load Sucessed: 772`, `Map Load Failed: 28`, giống trước.
- Cổng đang nghe: 5001, 5002, 5003, 5004, 5005, 51189, 56722, 56732.
- Sự kiện 5157: 0 dòng của exe JX. `Get-MpThreatDetection`: 0.

## Lỗi đã gặp
- Nút Startup của `Bishop` bấm bằng `BM_CLICK` 2 lần không có tác dụng: các ô trạng thái không đổi, nên hàm xử lý chưa chạy. Cửa sổ không ở phía trước.
- Sửa: gửi `WM_COMMAND` với mã của nút (1073) tới cửa sổ cha. Thành công ở lần thứ 3.
- `Bishop` kết nối lại `Sword3PaySys` liên tục trước khi Startup. Log lần chạy đầu cũng có hiện tượng này, không phải lỗi mới.

## Chưa kiểm tra
- Chưa có client kết nối thật. `portproxy` và tường lửa máy thật chưa áp dụng.

## Bước kế
Chủ máy duyệt và chạy `docs-analysis\scripts\tailscale_mo_cong.ps1`. Cần APK để thử game.
