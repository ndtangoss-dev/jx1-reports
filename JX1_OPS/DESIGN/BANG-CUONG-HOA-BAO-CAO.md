# BẢNG CƯỜNG HÓA + PHI PHONG (báo cáo Chat, B, 20/11)

Nguồn: `QH-B035-qianghua.lua` (qh_price/qh_rate/qh_wealth), `KItem.cpp` JxQhScale, `KItemList.cpp` QhPifengWealthOK. Trạng thái: gs001 pf3 đã dựng; A mới chạy thử +0→+8 trên LDPlayer; +9..+15 và phi phong CHƯA chạy trong game.

## 1. Cường hóa +1..+15 (tất cả 10 ô: mũ, áo, đai, vũ khí, giày, tay, bùa, nhẫn 1, nhẫn 2, ngọc bội)
Thủy tinh: mỗi loại hồng/lục/lam cùng số lượng, kẹp 1000/loại (từ +11). Bạc kẹp 20 ức (từ +11). Thất bại: giữ cấp, mất nguyên liệu và bạc. Chỉ số dòng ma thuật = gốc × (1 + 5% × cấp), cộng thẳng.

| Lên cấp | Tỉ lệ | Thủy tinh mỗi loại | Bạc | Tài phú +1 món (X=100) | Tài phú cả bộ 10 món đạt cấp này | Dòng kỹ năng |
|---|---|---|---|---|---|---|
| +1 | 100% | 1 | 200 vạn | +100 | 1000 | - |
| +2 | 95% | 2 | 400 vạn | +100 | 2000 | - |
| +3 | 90% | 4 | 800 vạn | +100 | 3000 | - |
| +4 | 85% | 8 | 1600 vạn | +100 | 4000 | - |
| +5 | 80% | 16 | 3200 vạn | +100 | 5000 | - |
| +6 | 75% | 32 | 6400 vạn | +100 | 6000 | - |
| +7 | 70% | 64 | 1,28 ức | +100 | 7000 | - |
| +8 | 65% | 128 | 2,56 ức | +100 | 8000 | - |
| +9 | 60% | 256 | 5,12 ức | +100 | 9000 | - |
| +10 | 55% | 512 | 10,24 ức | +100 | 10000 | - |
| +11 | 50% | 1000 | 20 ức | +100 | 11000 | - |
| +12 | 45% | 1000 | 20 ức | +100 | 12000 | - |
| +13 | 40% | 1000 | 20 ức | +100 | 13000 | - |
| +14 | 35% | 1000 | 20 ức | +100 | 14000 | +1 tất cả kỹ năng (chỉ vũ khí) |
| +15 | 30% | 1000 | 20 ức | +100 | 15000 | +2 tất cả kỹ năng (chỉ vũ khí) |

Chỉ số tăng: +n = +5n% giá trị gốc dòng ma thuật (+15 = +75%). Dòng gốc nhỏ làm tròn xuống (gốc 1 không tăng). Cộng dồn nguyên liệu để lên +15 từ +0 (mỗi loại): 6023 thủy tinh; bạc ≈ 120,46 ức (kỳ vọng thực còn cao hơn do thất bại: tỉ lệ thấp ở cấp cao).

## 2. Phi phong 11 cấp (điều kiện mặc theo tài phú)
Tài phú = 100 × tổng cấp +N các món đang mặc (N=10 ô). Ngưỡng cấp k = 100×10×(6+9(k−1)/10) = 6000 + 900(k−1). Chưa đủ: không mặc được, báo `[QH]|D|k|cần|có`. Đang mặc mà tài phú tụt dưới ngưỡng: server tự tháo phi phong về túi (QhCheckPifeng; hành vi khi túi đầy CHƯA kiểm).

| Cấp | Ngưỡng tài phú | Tương đương bộ | Sinh lực | Nội lực | Thể lực | Kháng tất cả | Tốc chạy |
|---|---|---|---|---|---|---|---|
| 1 | 6000 | +6 cả bộ | 200 | 200 | 100 | 4 | 5 |
| 2 | 6900 | +6.9 cả bộ | 400 | 400 | 200 | 8 | 10 |
| 3 | 7800 | +7.8 cả bộ | 600 | 600 | 300 | 12 | 15 |
| 4 | 8700 | +8.7 cả bộ | 800 | 800 | 400 | 16 | 20 |
| 5 | 9600 | +9.6 cả bộ | 1000 | 1000 | 500 | 20 | 25 |
| 6 | 10500 | +10.5 cả bộ | 1200 | 1200 | 600 | 24 | 30 |
| 7 | 11400 | +11.4 cả bộ | 1400 | 1400 | 700 | 28 | 35 |
| 8 | 12300 | +12.3 cả bộ | 1600 | 1600 | 800 | 32 | 40 |
| 9 | 13200 | +13.2 cả bộ | 1800 | 1800 | 900 | 36 | 45 |
| 10 | 14100 | +14.1 cả bộ | 2000 | 2000 | 1000 | 40 | 50 |
| 11 | 15000 | +15 cả bộ | 2200 | 2200 | 1100 | 44 | 55 |

Ghi chú: ánh xạ GoldId 3465..3475 = cấp 1..11, 3476..3490 là bản biến thể cấp 7..11 (cùng bảng chỉ số). Tên cấp phi phong gốc (Lăng Vân … Cao cấp) CHƯA đối chiếu trong game. File dữ liệu: `QH-B035-deploy/phiphong/`.

## 3. Chưa xác minh (nói rõ với chủ)
- Chưa chạy trong game: cường hóa +9..+15, dòng kỹ năng +14/+15 (tăng cấp kỹ năng thật), bảng chỉ số phi phong (offset id GoldMagic = dòng−1 là SUY RA), tự tháo phi phong, lưu cường hóa khi thoát/vào lại.
- Giá bạc kẹp 20 ức do tiền 32 bit (Q-87); công thức gốc của chủ +15 = 327,68 ức không đạt được.
