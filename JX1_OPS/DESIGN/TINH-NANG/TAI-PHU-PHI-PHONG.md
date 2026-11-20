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
