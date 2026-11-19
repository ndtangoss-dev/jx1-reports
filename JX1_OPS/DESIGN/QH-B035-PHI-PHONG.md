# QH-B035 — Phi phong vàng + điểm tài phú (B, 20/11)

## Luật đã cài (mã, build chạy ở D:\JX-wt\QH-B035, KItemList.cpp `QhPifengWealthOK`)
- Phi phong **vàng** = item_equip, Detail 12 (equip_pifeng), GoldId > 0. Cấp k = `Item.GetLevel()` (1..11; khớp cột `cap_lua_mau` trong TEST/DU-DOAN/phi-phong-vang-ho-tro.tsv và đoạn mã gán hình ở KItemList.cpp ~1688).
- Phi phong thường (GoldId = 0, PiFeng.txt, 10 mẫu trắng) KHÔNG bị chặn.
- Điểm tài phú = X × Σ cấp cường hóa (`GetEnChance`) của 10 ô 0..9 (đầu, áo, đai, vũ khí, giày, tay, bùa, nhẫn 1, nhẫn 2, ngọc bội). X=100, N=10, K=11 (mặc định #B-035c; QH-01 báo enum có 15 ô nhưng ngựa/mặt nạ/phi phong/ấn/thức phẩm không phải món cường hóa).
- Ngưỡng mặc cấp k = X·N·(6 + 9(k−1)/(K−1)).
- Chặn đặt trong `CanEquip` (cả hai bản) — chỉ đường người chơi tự mặc (chuột phải, kéo thả). Không chặn lúc đăng nhập nạp đồ; không tự tháo phi phong nếu sau đó tháo bớt đồ cường hóa (ghi nhận, chưa làm).
- Từ chối: server gửi `[QH]|D|k|can|co` (cấp phi phong, điểm cần, điểm đang có) qua kênh thông báo hệ thống. A hiển thị: "Cần X điểm tài phú để mặc, hiện có Y".

## Bảng ngưỡng
| Cấp | Phi phong | Điểm tài phú cần | Tương đương tổng cấp +N (cần/100) |
|---|---|---|---|
| 1 | Phi phong Lăng Vân | 6000 | 6.0 |
| 2 | Phi phong Tuyệt Thế | 6900 | 6.9 |
| 3 | Phi phong Phá Quân | 7800 | 7.8 |
| 4 | Phi phong Ngạo Tuyết | 8700 | 8.7 |
| 5 | Phi phong Kinh Lôi | 9600 | 9.6 |
| 6 | Phi phong Ngự Phong | 10500 | 10.5 |
| 7 | Phi phong Phệ Quang | 11400 | 11.4 |
| 8 | Phi phong Khấp Thần | 12300 | 12.3 |
| 9 | Phi phong Kình Thiên | 13200 | 13.2 |
| 10 | Phi phong Vô Cực | 14100 | 14.1 |
| 11 | Phi phong Cao cấp | 15000 | 15.0 |

Ví dụ: bộ 10 món +6 mặc cấp 1; bộ +15 mặc cấp 11 (cần 150 tổng cấp).

## Chỉ số tăng dần theo cấp
Dữ liệu GoldItem hiện có (Lăng Vân…Cao cấp) đã có magic riêng từng mẫu; việc chỉnh bảng chỉ số để tăng đều theo cấp = việc dữ liệu (cần QH-02 + Test-36). CHƯA làm; không đổi Settings.

## CHƯA XÁC MINH
Chưa chạy. Cần: gs001 mới (build đang chạy), A cho vai thử có phi phong vàng cấp 1 và cấp 11, mặc khi chưa đủ điểm (kỳ vọng bị chặn + dòng [QH]|D) và sau khi cường hóa đủ.
