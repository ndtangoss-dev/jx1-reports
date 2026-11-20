# HỒ SƠ TÍNH NĂNG: TÀI PHÚ + PHI PHONG (Q-99, khuôn như CUONG-HOA.md)
Chủ hồ sơ: B (server) + A (client, kiểm). Chat duyệt. Sau cường hóa (CUONG-HOA tiêu chí 1–8 đạt).

## (a) Yêu cầu chủ đã chốt
- Q-86/Q-90: điểm tài phú = X×(tổng cấp cường hóa các món đang mặc), X=100, N=10 ô (0..9); là THUỘC TÍNH NHÂN VẬT (chủ yêu cầu hiện trong khung); phi phong cấp k (K=11, GoldId 1..11) mặc được khi tài phú ≥ 6000+900(k−1) (=X×N×(6+9(k−1)/10)): 6000, 6900, … 15000. Tụt dưới ngưỡng thì tự tháo; đổi ngay khi mặc/tháo, không cần đăng nhập lại.

## (b) Bản đồ chuỗi (server, file:dòng; QH-B035 HEAD=B-042, nên số dòng KItemList.cpp có thể lệch ~+40 so với bản B-039 đang chạy)
ĐÃ TRA ĐỒ THỊ: `graphify explain ".Equip()"` → KItemList.cpp:L1619; `".UnEquip()"` → L2155 (đồ thị Core/Src QH-B035). Còn lại đọc mã (cạnh gọi gián tiếp không có trong đồ thị):
1. Điểm tài phú lưu `KPlayer::m_nWealth` (KPlayer.h:386; khởi tạo KPlayer.cpp:157).
2. Cộng/trừ qua thuộc tính `magic_special_point`: handler KNpcAttribModify.cpp:3407–3408 (kẹp ≥0). Dòng ảo `±100×nEnChance` cho món ô 0..9 sinh trong `Apply/RemoveMagicAttribToNPC` KItem.cpp:194/293 ⇒ mặc cộng, tháo trừ qua đường gốc (Equip 1619 / UnEquip 2155).
3. Đổi cấp cường hóa khi món trong túi không đổi tài phú (từ chối đồ đang mặc, Q-95).
4. Điều kiện phi phong: `KItemList::QhPifengWealthOK` KItemList.cpp:1149 (đọc `m_nWealth` 1161), chặn mặc ở 1248/1282; `EnoughAttrib` yêu cầu `magic_item_reserve8` 1349–1350 (tooltip điều kiện); báo `[QH]|D`. Tự tháo khi tụt: 1211–1219.
5. Dữ liệu: bảng phi phong vàng (DESIGN/QH-B035-deploy/phiphong/GoldItem.txt, GoldMagic.txt, HUONG-DAN-A.md; SHA256-pf*.txt).
Rủi ro: phần 4 (tự tháo, QhPifengWealthOK) là logic mới không có trong gốc; đã build, CHƯA CHẠY toàn bộ (B-035/pf đã nạp ở Test-36 từ trước nhưng A chưa ghi bằng chứng ảnh trong hồ sơ).

## (c) Tiêu chí nghiệm thu (đo được)
1. Mặc món +N (ô 0..9): khung nhân vật có dòng tài phú tăng đúng +100×N (số thật, ảnh).
2. Tháo: trừ lại đúng +100×N; tháo hết → 0.
3. Mặc 2 món +3 và +5: tài phú 800.
4. Tài phú 5999 + phi phong cấp 1: từ chối kèm thông báo thiếu; 6000: mặc được.
5. Phi phong cấp k=11 cần 15000: đủ mới mặc; từ cấp 1 đến 11 mỗi cấp đúng ngưỡng.
6. Đang mặc phi phong, tháo món cường hóa làm tài phú dưới ngưỡng: phi phong tự tháo + thông báo.
7. Thoát/vào lại: tài phú giữ đúng (tính lại theo đồ đang mặc, không nhân đôi/mất).
8. Chỉ số phi phong tăng dần theo cấp (so GoldMagic.txt).

## (d) Các bước và trạng thái
| Bước | Ai | Trạng thái | Bằng chứng |
|---|---|---|---|
| 1 CUONG-HOA tiêu chí 1–8 đạt | A | CHƯA KIỂM | |
| 2 Tiêu chí 1–3 tài phú | A | CHƯA KIỂM | |
| 3 Tiêu chí 4–6 phi phong (ngưỡng, tự tháo) | A | CHƯA KIỂM | |
| 4 Tiêu chí 7 đăng nhập lại | A | CHƯA KIỂM | |
| 5 Làm mới đồ thị + bản đồ chuỗi | B | CHƯA KIỂM | |

## (e) Việc kế
A: bước 1→4 sau cường hóa. B: sẵn sàng sửa nếu tiêu chí 7 lệch (`m_nWealth` lúc nạp: tính lại từ đồ đang mặc khi vào game — cần kiểm Equip lúc login có chạy lại Apply không).

## (f) Bang gia tri theo cap (B kiem 21/11 tu GoldMagic.txt dong 4361-4415, CHI DOC MA)

Moi phi phong goc cap g=1..11 co du 5 dong (DefMagic1-5), tang NGHIEM NGAT theo g o ca 5 dong. Nguong tai phu = 6000+900(g-1).

| Cap g | Sinh luc (85) | Noi luc (89) | The luc (93) | Khang tat ca % (114) | Toc chay (111) | Can tai phu |
|---|---|---|---|---|---|---|
| 1 | 200 | 200 | 100 | 4 | 5 | 6000 |
| 2 | 400 | 400 | 200 | 8 | 10 | 6900 |
| 3 | 600 | 600 | 300 | 12 | 15 | 7800 |
| 4 | 800 | 800 | 400 | 16 | 20 | 8700 |
| 5 | 1000 | 1000 | 500 | 20 | 25 | 9600 |
| 6 | 1200 | 1200 | 600 | 24 | 30 | 10500 |
| 7 | 1400 | 1400 | 700 | 28 | 35 | 11400 |
| 8 | 1600 | 1600 | 800 | 32 | 40 | 12300 |
| 9 | 1800 | 1800 | 900 | 36 | 45 | 13200 |
| 10 | 2000 | 2000 | 1000 | 40 | 50 | 14100 |
| 11 | 2200 | 2200 | 1100 | 44 | 55 | 15000 |

Bien the (dong GoldItem 3478-3492): dung bo chi so cua cap tuong ung (7..11) NGOAI TRU dong 3487 (phi phong Vo Cuc dich chuyen toc thoi, cap 10) co chi so rieng (GoldMagic 3814..3854, loai 233/227...): KHONG nam trong bang tren, chu can biet neu muon dong deu. Hinh phi phong lay theo nLevel (1,1,2,3,3,4,4,4,5,5,5 cho 11 cap goc) nen cap 1 va 2 cung hinh.

