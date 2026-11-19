# VK-04 — Sét +15 của vũ khí hai tay (chùy, thích) chỉ chạy một bên (#225 / Q-64)

**TÓM TẮT 5 DÒNG**
1. [THẤY ảnh] `ANH/t36-vu-khi-chuy-8-huong.png`: chùy +15 chỉ có MỘT cụm sét ở mỗi hướng (E, SE, W, NW), cụm kia không có; thích tương tự (ảnh #219). Một tay (kiếm/đao/thương/bổng) một cụm là đúng.
2. [THẤY mã] Gốc: `vn/gamecore/KNpcResVN.cpp:~547-585` chọn DUY NHẤT một section trội `domSec` (nhiều điểm mask nhất) rồi chỉ vẽ sét khi `k == domSec` (`~:597`). Đoạn `[clip2]` còn dồn mask về section đó (`memmove`) nên mask/rect của section kia bị bỏ. `jxDrawBolts` (`KgameWorld.cpp:15025+`) đọc mask toàn cục `g_jxMaskX/Y/N` và rect của một section.
3. [SUY RA, CHƯA KIỂM] Vũ khí hai tay vẽ thành ≥2 section vũ khí (hai lớp tay phải/trái). Chưa đo số section thật của chùy/thích: cần bật `g_jxTrace` (log `SEC dir n idx0 idx1 dom mask` mỗi giây) trên LD; chưa làm.
4. Đề xuất (CHƯA SỬA, chờ Chat duyệt; hook chặn `KNpcRes*`): giữ lượt đo nhưng lưu `secH/secM0/secM1/secR` của MỌI section có `cnt ≥ 8`; không `memmove`, mà tại mỗi `k` đủ điều kiện nạp lại mask riêng của k vào `g_jxMask*` + rect rồi gọi `jxDrawBolts`. Rủi ro: trung bình (đụng đường vẽ mỗi khung; thêm một lần `jxDrawBolts` cho tay thứ hai ≈ gấp đôi chi phí sét chỉ với vũ khí hai tay; guard R<8, lưới>200 giữ nguyên). Công tắc: cờ `/sdcard/jxbolt2` hoặc `g_jxTrace`-style.
5. Cần tôi quyết định: có (Chat duyệt sửa mã hiệu ứng; mã chỉ sửa sau `JX1_EFFECT_OK=1`).

Đối chiếu một tay: một section vũ khí → `domSec` = nó → một cụm: đúng. Hai tay: hai section nhưng `domSec` chỉ một → thiếu một bên: khớp ảnh.
Việc kế (sau duyệt): đo `SEC n` bằng trace để xác nhận n=2, sửa theo (4), quay lại 8 hướng chùy/thích, so trước/sau.
