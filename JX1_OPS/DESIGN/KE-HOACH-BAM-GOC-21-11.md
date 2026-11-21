# KẾ HOẠCH BÁM LOGIC GỐC — Chat 21/11 09:25 (chủ duyệt: "gom thông tin, tìm cách sửa cho đúng, cho A B làm, test hoàn chỉnh rồi báo ta vào test lại")

NGUYÊN TẮC (chủ chốt): bám logic GỐC trước, chỉ thêm phần mới SAU khi gốc chạy đúng. Không sửa phần nổi (tooltip/hiển thị) để che; mỗi việc phải đo từ DỮ LIỆU GỐC. Số thiết kế riêng của mình (bảng 11 cấp tăng đều, ngưỡng tài phú 6000+900(k-1), +5%/cấp) CHỈ là lớp phát triển thêm, phải tách công tắc, mặc định = gốc.

## A. CƯỜNG HÓA (mọi loại trang bị đều cường hóa được)
1. B: sửa `gs/script/System/qianghua.lua` dòng 44: `kind==0 and (a8==1 or a6>0)` → `kind==0` (nhận đồ trắng/tạp hóa). Giữ bản gốc `.bak-qh-filter`. Rà thêm mọi điều kiện loại món khác (loại vũ khí/giáp/nhẫn/dây/ngọc bội/giày/nón/găng/…): bảng "loại trang bị → cường hóa được/không" có số thật. Lua nạp lại không cần restart thì dùng; nếu phải restart gs001 thì BÁO Chat trước (chủ không đang trong game).
2. A đo trên LD: mỗi loại trang bị (tối thiểu 1 món/loại: vũ khí, áo, nón, giày, găng, nhẫn, dây chuyền, ngọc bội, bao tay…) cường hóa 0→1 bằng 3 đá mỗi loại 1 viên, chụp thông báo + số trước/sau. Đồ tạp hóa trắng PHẢI thành công (tỷ lệ cấp 1 = 100%).
3. B: đọc logic cường hóa GỐC (kho gốc, bản chủ test trước: qianghua cũ, EnChance gốc) → bảng đối chiếu: nguyên liệu, tỷ lệ, hạ/mất cấp, tăng chỉ số. Phần nào mình tự đặt (+5%/cấp, Q-104) ghi rõ "thiết kế mình", có công tắc.

## B. PHI PHONG — dựng lại từ DỮ LIỆU GỐC
Bằng chứng đã có: server gốc `mantle.txt` (3 món Phá Cựu cấp 1–3, hình giữ chỗ), `PiFeng.txt` 14 mẫu (HP/MP khoảng theo cấp, KHÔNG yêu cầu giới tính), client có 11 bộ hình mỗi giới (nam 01–10+22, nữ 01–10+21) trong update.pak, bảng hình client `男主角披风.txt`, `FortuneRank` trong `npcbobo.ini` (cần đủ 11 khóa) — nghi đây là LIÊN KẾT GỐC giữa điểm tài phú và hình phi phong.
1. A: bung `npcbobo.ini` + bảng nữ từ PAK (update.pak/PAK client): đọc `FortuneRank` (11 khóa?), cách client chọn hình phi phong theo tài phú/giới. Nếu thiếu công cụ bung PAK báo ngay (không đoán).
2. B: đọc server gốc cách tính điểm tài phú → hạng → phi phong (m_nWealth, magic_special_point, FortuneRank, mantle) và vì sao "chỉ mở 3 cấp" (mantle.txt 3 món). Lập BẢNG GỐC: hạng ↔ ngưỡng ↔ hình ↔ dòng chỉ số.
3. Dữ liệu đích (theo ý chủ, bản chủ từng test): mọi phi phong cùng tên/dòng/cấp mô tả như gốc, chỉ khác hình theo giới (client), tên nhãn cạnh nhân vật theo gốc; mặc tăng chỉ số, tháo mất; thiếu tài phú tự tháo (theo ngưỡng GỐC nếu có, không thì giữ ngưỡng mình ở công tắc).
4. Dòng ẩn: luật gốc (ngũ hành) — build 13 `QH_PIFENG_ALL_LINES=0`. Giữ.
5. A: gộp bản sửa nhãn tên (qh9A, `[pfl]`) vào cây repo KHÔNG ghi đè nội suy #255; build APK vc32, thử trên LD: đổi phi phong → nhãn đổi NGAY. APK chỉ cài LD cho chủ; chưa phát máy thật.
6. Menu hotrotanthu "Phi phong 1/2/3…" chỉ để thử, gỡ trước máy thật.

## C. THỨ TỰ + NGHIỆM THU
- Giai đoạn 1 (đọc gốc, không đổi): A mục B1, B mục A3 + B2 → bảng gốc vs đang chạy, báo Chat.
- Giai đoạn 2 (sửa): B mục A1 (filter) + build mới (phi phong gốc, 13+), A mục B5. Chat duyệt bảng gốc trước khi sửa dữ liệu phi phong.
- Giai đoạn 3 (test): A đo bằng SỐ THẬT/ẢNH trên LD cho từng mục A2, B3, B5; ghi TU-SONNET; gõ `A Chat`. Chỉ khi đạt thì Chat báo chủ vào test lại. Việc chưa có số/ảnh = CHƯA KIỂM.
- LD hiện trả lại cho A (chủ đã giao việc, chờ báo vào test lại). B được nạp build khi Chat báo `NAP`.
