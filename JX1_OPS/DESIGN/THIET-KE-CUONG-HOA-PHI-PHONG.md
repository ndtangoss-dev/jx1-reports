# THIẾT KẾ CƯỜNG HÓA + PHI PHONG + TÀI PHÚ (Chat, 20/11 01:00; chủ chốt 00:48, Q-86)
Chủ ĐÃ CHỐT, giao A và B làm ngay, "bằng mọi giá", sửa cả server nếu cần. Phạm vi: Test-36 + APK thử (Server D vẫn Đỏ). Chủ nhắc: tiền tệ dùng đơn vị bạc, vạn, ức (1 vạn = 10.000 bạc; 1 ức = 100.000.000 bạc).

## 1. Cường hóa (áp dụng cho TẤT CẢ vũ khí và trang bị trên người)
- Cấp tối đa +15. Từ +(n-1) lên +n cần, mỗi loại: 2^(n-1) hồng thủy tinh, 2^(n-1) lục thủy tinh, 2^(n-1) lam thủy tinh, và 2^(n-1) × 200 vạn bạc.
- Tỉ lệ thành công +n = 100 − 5×(n−1) (%): +1 100, +2 95, … +15 30. Thất bại: giữ nguyên cấp, chỉ mất nguyên liệu và bạc.
- Chỉ số cộng thêm (các dòng khoanh trắng trong tooltip: thế lực, sát thương nội/ngoại công, độ chính xác, kháng độc, tốc độ đánh...) = chỉ số gốc ở +0 × (1 + 0,05 × n), CỘNG THẲNG (+15 = +75%). Đồ +cao phải có chỉ số tăng dần theo cấp.
- +14: thêm dòng "+1 tất cả điểm kỹ năng vốn có". +15: dòng "+2 tất cả điểm kỹ năng vốn có". Chủ nói dòng này đã tương tác với hệ thống skill rồi: kiểm id thuộc tính đúng trong Settings và xác nhận có tăng cấp kỹ năng thật.
- Bỏ vũ khí +15 phát thử (online.lua JXGiveWeapons/JXGive269) để khỏi lẫn: gỡ phát, đặt lại về +0 cho tài khoản thử.
- Bảng giá mỗi cấp (mỗi loại thủy tinh / bạc): +1: 1 / 200 vạn; +2: 2 / 400 vạn; +3: 4 / 800 vạn; +4: 8 / 1600 vạn; +5: 16 / 3200 vạn; +6: 32 / 6400 vạn; +7: 64 / 1,28 ức; +8: 128 / 2,56 ức; +9: 256 / 5,12 ức; +10: 512 / 10,24 ức; +11: 1024 / 20,48 ức; +12: 2048 / 40,96 ức; +13: 4096 / 81,92 ức; +14: 8192 / 163,84 ức; +15: 16384 / 327,68 ức.
- RỦI RO TIỀN: ô tiền thường là số nguyên 32 bit, tối đa ≈ 2.147.483.647 bạc ≈ 21,47 ức; từ +12 trở lên vượt. CHƯA KIỂM (Q-52: đọc mã trước). Chủ yêu cầu SỬA ĐƯỢC, kể cả server: truy suốt chuỗi tiền (lưu Goddess/DB, KPlayer, giao thức s2c/c2s, client hiển thị, trao đổi/cửa hàng) và mở rộng lên 64 bit hoặc cách tương đương; hiển thị đơn vị bạc / vạn / ức ở client. Nếu thật sự bất khả: báo Chat kèm phương án, KHÔNG dừng các việc khác.
- UI cửa sổ cường hóa: dùng bộ asset gốc của game, tự thiết kế (A).

## 2. Điểm tài phú + phi phong
- Điểm tài phú = X × (tổng cấp cường hóa của các món đang mặc). Mỗi +1 trên một món = X điểm. Đề xuất X = 100.
- N = số ô trang bị cường hóa được (A/B xác nhận từ dữ liệu; dự kiến ~10). K = số cấp phi phong (khảo sát; dữ liệu dự đoán cho thấy 11 phi phong vàng Lăng Vân…Cao cấp, cần kiểm trong game thật).
- Ngưỡng mặc phi phong cấp k (k=1..K) = X × N × (6 + 9×(k−1)/(K−1)), làm tròn. Bộ đồ +6 (Y = X×N×6) mặc được cấp 1; bộ +15 (X×N×15) mặc được cấp K; các cấp giữa chia đều. Ví dụ N=10, X=100, K=11: 6000, 6900, 7800, … 15000.
- Phi phong: kiểm có bao nhiêu cấp, thiết kế chỉ số tăng dần theo cấp, mở khóa (hiện bị khóa?); điều kiện mặc = điểm tài phú ≥ ngưỡng; tooltip/thông báo khi chưa đủ; client hiển thị điểm tài phú (A).

## 3. Chia việc
- B (server): logic cường hóa (nhận yêu cầu, kiểm nguyên liệu + bạc, tỉ lệ, đổi cấp, chỉ số 5% cộng thẳng, dòng kỹ năng +14/+15); chuỗi tiền 64 bit/ức; điểm tài phú + điều kiện phi phong + bảng 11 cấp phi phong; giao thức mới giữa client–server (soạn hợp đồng cho A trong A-B.md trước khi A dựng UI).
- A (client + test): cửa sổ cường hóa (asset gốc), hiển thị tooltip +N/dòng chỉ số/ức, điểm tài phú, thông báo phi phong; dựng APK thử mới; test trên LDPlayer bằng TÀI KHOẢN TEST RIÊNG của A; tiếp lỗi cũ (đánh thường, khựng 4–5 s, quái hiện muộn).
- Tiểu yêu: việc khảo sát tĩnh (số cấp phi phong và chỉ số, danh sách ô trang bị, id thuộc tính kỹ năng +N, chuỗi kiểu dữ liệu tiền) giao qua Tổng quản bằng TASKS/<mã>.md.
- Xong mục được giao thì làm tiếp hàng đợi; không chờ chủ, không chờ Chat duyệt (chủ: "bằng mọi giá").

## 4. QUYỀN QUYẾT ĐỊNH VỀ GIÁ (chủ 20/11 00:59, Q-87) — KHÔNG MÁY MÓC, KHÔNG DỪNG TIẾN ĐỘ
Chủ: nếu tiền tệ không cho phép thì Chat được GIẢM GIÁ cường hóa cho hợp lý với game, không để tiến độ dừng; thứ chủ cần là chức năng cường hóa XÂY XONG và chạy. Chat quyết sẵn phương án để A/B không phải chờ:
- Ưu tiên 1: mở rộng tiền lên 64 bit CHỈ NẾU làm gọn (không quá ~1 giờ công, không phá giao thức/lưu DB). Không thì sang ưu tiên 2 NGAY.
- Ưu tiên 2 (mặc định nếu tiền là 32 bit): giá bạc mỗi cấp = min(2^(n−1) × 200 vạn, 20 ức); nguyên liệu hồng/lục/lam VẪN gấp đôi mỗi cấp. Tức +1..+11 đúng công thức chủ (+11 = 20,48 ức → kẹp 20 ức), +12..+15 giữ 20 ức bạc (nguyên liệu vẫn 2048/4096/8192/16384). 20 ức = 2.000.000.000 < 2.147.483.647.
- B/A tự áp dụng và ghi vào báo cáo "đã giảm giá vì ..."; sau khi xong mới báo Chat/chủ. Mọi quyết định tương tự (đổi tham số cho vừa game: giới hạn kiểu dữ liệu, kích thước ô, ngưỡng) được tự quyết theo hướng "chức năng chạy được, đúng tinh thần chủ", ghi rõ lý do; chỉ Vùng Đỏ mới hỏi.

## 5. CHỐT THỦY TINH (Chat 20/11 01:52, theo quyền Q-87)
Thủy tinh chồng tối đa 200/ô nên 16384 viên (+15) = 82 ô túi mỗi loại: không chơi được. Chốt: số thủy tinh mỗi loại ở cấp +n = min(2^(n−1), 1000) → +1..+10 đúng công thức chủ (…512), +11..+15 giữ 1000 mỗi loại (5 chồng/loại, 15 ô cho 3 loại). Bạc vẫn kẹp 20 ức. KHÔNG đổi MAX_STACKNUM (đụng cả client, rủi ro). Độ khó +11..+15 còn lại nằm ở tỉ lệ (xuống 30%) và chỉ số 5%/cấp. Ghi vào báo cáo lý do thay đổi.
