# Bảng chỉ số 11 cấp phi phong (B, 20/11) — A chép lên Test-36
Phạm vi: CHỈ Test-36 (VM 192.168.56.150). KHÔNG Server D.

## Chỉ số (cộng thẳng, tăng đều theo cấp g=1..11)
Sinh lực 200g | Nội lực 200g | Thể lực 100g | Kháng tất cả 4g | Tốc chạy 5g
(cấp 1: 200/200/100/4/5 ... cấp 11: 2200/2200/1100/44/55). 11 phi phong vàng gốc (GoldItem dòng 3467-3477) và các bản biến thể (3478-3492, trừ dòng 3487 đã có chỉ số riêng) dùng chung bảng theo cấp: Phá Quang=7, Khắp Thần=8, Kình Thiên=9, Vô Cực=10, Cao cấp=11.

## File chép (GBK, CRLF, ghi đè trên Test-36)
- `GoldItem.txt`  -> `gs\Settings\item\004\GoldItem.txt`   SHA-256 2FA5AA2C...
- `GoldMagic.txt` -> `gs\Settings\item\004\GoldMagic.txt`  (thêm 55 dòng ở cuối, id 4361-4415) SHA-256 E676190A...
Cách làm: tắt gs001, chép .bak của 2 file cũ cạnh nó (GoldItem.txt.bak-pp, GoldMagic.txt.bak-pp), chép 2 file mới, bật lại gs001 (nạp lại ~10 phút). Hoàn tác = chép .bak về.
Chưa chạy thử trong game: việc kiểm (mặc phi phong cấp k, xem tooltip) là của A sau khi chép.

## Điều kiện mặc (server, bản pf3)
Ngưỡng tài phú cấp k = 100*10*(6+9(k-1)/10) = 6000,6900,...,15000. Không đủ -> không mặc được, báo `[QH]|D|k|can|co`. Đang mặc mà tài phú tụt dưới ngưỡng (tháo/đổi đồ +N) -> server TỰ THÁO phi phong về túi (cũng báo `[QH]|D`). Túi đầy -> giữ nguyên, kiểm lại ở lần đổi đồ sau.
