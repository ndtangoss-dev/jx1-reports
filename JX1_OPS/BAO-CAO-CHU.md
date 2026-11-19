# BÁO CÁO CHỦ — việc cần đại vương mới tới 100% (19/11, 02:40)

Các mục dưới đây không tính được "xong" nếu thiếu đại vương; thuộc hạ KHÔNG hạ mẫu số, chỉ ghi rõ chờ ai.

| Mục | Cần gì từ đại vương | Vùng |
|---|---|---|
| CL-01 (C-02, C-04, C-05) | Duyệt từng bước cường hóa (chưa duyệt) | Đỏ |
| B-05 | Quyết định/duyệt | Đỏ |
| X-05 | Quyết định/duyệt | Đỏ |
| 0-07 (bước Main VM) | Duyệt chạm Main VM | Đỏ |
| P-01 | Duyệt | Đỏ |
| 0-08 | Duyệt | Đỏ |
| #134 | Đăng nhập ndtan48 rồi chạy `claude -p --model claude-sonnet-5-5 "ping"` | Chủ |
| Nhân vật thứ 4 | Chủ thử | Chủ |

[CHƯA KIỂM] Nội dung chi tiết từng mục lấy từ BACKLOG/TASKS, thuộc hạ chưa đọc lại từng tệp ở đợt này.

## 03:52 19/11 — số thật sau #211
- Số THẬT 74/101 = 73,3%; số bảng cũ 78%. Chi tiết: `STATE/BANG-DONG-VIEC-CHA.md`.
- Việc cần sáng mai để lên 100%: E-01/E-09 (Bot thật đăng nhập–đi–đánh trên Test-36, cần bật VM và nối giao thức thật; ước nhiều giờ), A-07/A-07b (thiếu dump/PDB), B-04 (đo 9 pha cần VM), CL-01 C02/C04/C05 (chủ), B-05, X-05 (tạm dừng).

## 05:20 — B-05 Tống Kim: chuẩn bị xong, chờ chủ đặt giới hạn (D4)
- Báo cáo `REPORTS/XD-B05.md` mục 6: 8 câu hỏi 2–3 lựa chọn kèm khuyến nghị. Tóm lại: mở thủ công một trận trên bản copy thử trước (Q2-B), lịch baseline 11:50 + 20:50 (Q3-A), trần 100/phe chênh 2 (Q4-A), phí 200.000 giữ nguồn (Q6-A). Chưa bật gì.
- Cần chủ chỉ cho đường dẫn chính xác của "D4" nếu muốn khép nguồn.

## 08:25 19/11 — kiểm thứ tự vẽ khi đi 8 hướng (#216, CHỈ KIỂM, không sửa)
- Ảnh ghép 8 hướng (vuốt cần điều khiển trên LD, nhân vật `T36nv1` Kim, cầm kiếm): `ANH/t36-thu-tu-ve-8-huong.png`. Các khung N, NE, E, SE, S, NW: tay/vũ khí/thân vẽ liền, không thấy vũ khí lệch lớp rõ ràng [ĐÃ XEM BẰNG MẮT, chưa đo từng điểm ảnh]. SW và W: nhân vật bị tán cây che (che theo cảnh, không phải lỗi thứ tự vẽ).
- **CHƯA KIỂM giáo**: nhân vật thử không có giáo, nên chưa trả lời được câu hỏi "giáo, 8 hướng". Cần cấp một giáo cho nhân vật thử (sửa DB/lệnh GM trên Test-36), thuộc hạ sẽ làm khi có việc kế. Vuốt cần theo màn hình nên 8 hướng chưa chắc khớp 8 hướng trong game.
- Vì vậy bước mở Server D + LDPlayer-D để chủ thử bằng điện thoại vẫn đang chờ kiểm này (thuộc hạ chưa mở D).

## 09:25 19/11 — #219 (Q-61): kiểm vũ khí cận chiến +15, đi 8 hướng (CHỈ KIỂM, không sửa)
Test-36, nhân vật `T36nv1`, mỗi loại +15 (cấp 1), trang bị rồi đứng im chạy 8 hướng, chụp ghép 4×2 (khung 420×420 quanh nhân vật). Ảnh trong `ANH/t36-vu-khi-<loại>-8-huong.png`.

| Loại (vật phẩm) | N | NE | E | SE | S | SW | W | NW | Hiệu ứng +15 |
|---|---|---|---|---|---|---|---|---|---|
| Kiếm (Thiết Trủy Thủ) | ổn | che cảnh (cổng) | ổn | ổn | ổn | che cảnh (cây) | ổn | ổn | có (tia sét trắng) |
| Đao (Yêu Đao) | ổn | che cảnh (cây) | ổn | ổn | ổn | che cảnh (cây) | ổn | ổn | có |
| Thương (Thiết Thương) | ổn | che cảnh (cổng) | ổn | ổn | ổn (mái nhà che phần dưới) | che cảnh (cây) | ổn | ổn | có |
| Chùy (Toán Đầu Chùy) | ổn | che cảnh (cổng) | ổn | ổn | ổn | che cảnh (cây) | ổn | ổn | có |
| Song đao (Nga Mi Thích) | ổn | che cảnh (cổng) | ổn | ổn | ổn | che cảnh (cây) | ổn | ổn | có |
| Bổng (Thiêu Hỏa Côn) | ổn | che cảnh (cổng) | ổn | ổn | ổn (mái nhà che) | che cảnh (cây) | ổn | ổn | có |

- Kết quả: bằng mắt trên ảnh, KHÔNG thấy hướng nào vũ khí vẽ sai thứ tự so với thân (N/NW vũ khí nằm sau/bên thân, các hướng còn lại ở trước/bên đúng hướng cầm). Giới hạn: chụp một khung/hướng khi đang đi, chưa xét đứng im tĩnh từng góc, chưa xét đòn đánh/cưỡi ngựa. "Che cảnh" = vật cảnh (cổng, cây, mái) che nhân vật, không phải lỗi vẽ vũ khí; các ô đó CHƯA KIỂM được vũ khí.
- Dùng được cả 6 loại (đủ sức mạnh/thân pháp cho Thương: đã thấy "Đã trang bị"). Cần ghi chú: +15 chỉ hiện sau khi vào lại game (client nạp lại từ DB).
- Server D chưa khởi động (làm tiếp theo #216 mục 3).

## 10:40 19/11 — VK-04 (#225): sét hai tay chỉ một bên
Ảnh trước: `ANH/t36-vu-khi-chuy-8-huong.png` (một cụm sét). Nguyên nhân [THẤY mã]: `KNpcResVN.cpp` chỉ vẽ sét ở section trội `domSec`, bỏ section kia. Đề xuất: vẽ sét cho mọi section có mask ≥ 8 (xem `REPORTS/VK-04-set-hai-tay.md`). Chưa sửa; chờ Chat duyệt. [CHƯA KIỂM] số section thực của chùy/thích.

## 10:50 19/11 — BOT GĐ0 (#220): đề xuất hướng A
1 Bot đo thật: RX ~216 kbps, khung S2C TB 32,9 ms. Chưa đo nhiều Bot / tick 18 Hz (chưa có số). Hướng B cần sửa và dựng lại server (chưa từng làm). Đề xuất: A + thang thử tải 1→100 trên Test-36 ở GĐ1. Xin Chat/chủ duyệt. Chi tiết `REPORTS/BOT-GD0-khao-sat-A-B.md`.

## GIAO APK CHO CHỦ (#228) — 19/11 11:05 — chưa giao gì, chỉ trả lời câu hỏi
**Cần tôi quyết định: có (khi chủ muốn nhận APK sét mới — vùng Đỏ).**
1. **APK trên điện thoại chủ [ĐÃ KIỂM bằng log tải]:** lần tải cuối của điện thoại (100.123.183.6) là `jx-qh9-A3a.apk` lúc 22:05 17/11. SHA-256 `7894c22d…ec2d8`, package `com.jxclient.hoiuctruyenky`, versionCode 20. Khóa ký là khóa debug chung `a48601f7…2d7` (cùng khóa mọi bản dựng từ `ANDROID_USER_HOME=D:\Android\user`), nên **cài đè được, không mất dữ liệu**, miễn bản mới có versionCode >20 (bản VK-04 đặt 21). Chưa kiểm được máy chủ có cài bản nào sau đó hay không (log chỉ ghi tải, không ghi cài). Bản sét mới sẽ dựng từ đúng nền qh9A, không trộn fix36/T36test.
2. **Sét là sửa phía client hay server [ĐÃ KIỂM mã]:** hiệu ứng chùy/thích nằm ở `Classes/vn/gamecore/KNpcResVN.cpp` (client). Chỉ cần APK mới, **server D không phải đổi**.
3. **Tài khoản/nhân vật chủ trong DB Server D [CHƯA KIỂM]:** `JX-Server-D` đang tắt (luật L11: tắt khi 0 người chơi). Chỉ đọc DB cần bật D; theo lệnh #216 bật D sau khi xong VK-04 và BOT. Sẽ kiểm chỉ sự tồn tại và tên nhân vật, không đọc mật khẩu, rồi bổ sung vào đây.
4. **Cách giao APK không qua git (kho công khai):** (A) tải qua mạng Tailscale: máy thật phát `http://100.95.186.86:8091/<tên>.apk`, chỉ điện thoại chủ truy cập được; chủ mở link, bấm tải. (B) Chép qua cáp USB/Zalo cá nhân: PM đặt file vào thư mục riêng ngoài kho, chủ tự chép. Hướng dẫn cài đè: ① tải xong, mở file trong "Tải xuống"; ② bấm "Cập nhật/Cài đặt" (đừng gỡ bản cũ, gỡ sẽ mất dữ liệu cục bộ); ③ nếu Android chặn thì bật "cho phép cài từ nguồn này" cho trình duyệt; ④ mở game, đăng nhập như thường. Link gửi dạng hộp copy có SHA256 (khi chủ đồng ý nhận).
