# VK-04 — Sét +15 của vũ khí hai tay (chùy, thích) chỉ chạy một bên (#225 / Q-64)

**TÓM TẮT 5 DÒNG**
1. [THẤY ảnh] `ANH/t36-vu-khi-chuy-8-huong.png`: chùy +15 chỉ có MỘT cụm sét ở mỗi hướng (E, SE, W, NW), cụm kia không có; thích tương tự (ảnh #219). Một tay (kiếm/đao/thương/bổng) một cụm là đúng.
2. [THẤY mã] Gốc: `vn/gamecore/KNpcResVN.cpp:~547-585` chọn DUY NHẤT một section trội `domSec` (nhiều điểm mask nhất) rồi chỉ vẽ sét khi `k == domSec` (`~:597`). Đoạn `[clip2]` còn dồn mask về section đó (`memmove`) nên mask/rect của section kia bị bỏ. `jxDrawBolts` (`KgameWorld.cpp:15025+`) đọc mask toàn cục `g_jxMaskX/Y/N` và rect của một section.
3. [SUY RA, CHƯA KIỂM] Vũ khí hai tay vẽ thành ≥2 section vũ khí (hai lớp tay phải/trái). Chưa đo số section thật của chùy/thích: cần bật `g_jxTrace` (log `SEC dir n idx0 idx1 dom mask` mỗi giây) trên LD; chưa làm.
4. Đề xuất (CHƯA SỬA, chờ Chat duyệt; hook chặn `KNpcRes*`): giữ lượt đo nhưng lưu `secH/secM0/secM1/secR` của MỌI section có `cnt ≥ 8`; không `memmove`, mà tại mỗi `k` đủ điều kiện nạp lại mask riêng của k vào `g_jxMask*` + rect rồi gọi `jxDrawBolts`. Rủi ro: trung bình (đụng đường vẽ mỗi khung; thêm một lần `jxDrawBolts` cho tay thứ hai ≈ gấp đôi chi phí sét chỉ với vũ khí hai tay; guard R<8, lưới>200 giữ nguyên). Công tắc: cờ `/sdcard/jxbolt2` hoặc `g_jxTrace`-style.
5. Cần tôi quyết định: có (Chat duyệt sửa mã hiệu ứng; mã chỉ sửa sau `JX1_EFFECT_OK=1`).

Đối chiếu một tay: một section vũ khí → `domSec` = nó → một cụm: đúng. Hai tay: hai section nhưng `domSec` chỉ một → thiếu một bên: khớp ảnh.
Việc kế (sau duyệt): đo `SEC n` bằng trace để xác nhận n=2, sửa theo (4), quay lại 8 hướng chùy/thích, so trước/sau.

## Bước (a) #226 — đo thật trên LD `T36-tester01` (19/11 10:21) — KẾT QUẢ: GIẢ THUYẾT "hai tay = 2 section" CHƯA ĐƯỢC XÁC NHẬN
Bật `/sdcard/jxtrace`, `logcat -s JXTRC`, mặc lần lượt 5 vũ khí +15 trong túi (kiếm bạc, kiếm đỏ, 2 loại còn lại, chùy, song đao; hướng 0): mọi loại đều `SEC dir=0 n=2 idx0=7 idx1=10 dom=1`, mask 99–113 (số điểm mask của section trội SAU `memmove`; mask section kia không được log).
- Kết luận: n=2 cũng xảy ra với vũ khí MỘT tay, nên n không phân biệt hai tay. Hai section (sort 7 và 10) nhiều khả năng là lớp trước/sau thân, không phải tay trái/phải. Đề xuất sửa ở mục 4 dựa trên giả thuyết đó nên **chưa được phép áp dụng**.
- Còn thiếu: số mask THEO TỪNG section và rect từng section (log hiện chỉ in sau khi dồn về `domSec`). Cần thêm dòng trace trong `KNpcResVN.cpp` (chỉ dưới `g_jxTrace`, không đổi hành vi) rồi build bản thử; sửa này cần `JX1_EFFECT_OK=1` cho riêng commit trace (Chat #226 đã duyệt hướng sửa, chưa nói riêng về commit chỉ-trace).
- Khả năng khác cần loại trừ: hai chùy nằm chung MỘT section ảnh, nên mask phủ cả hai nhưng sét chỉ đi theo một trục/rect (PCA) → sét cả hai bên cần chia mask thành hai cụm, không phải lặp theo section.
