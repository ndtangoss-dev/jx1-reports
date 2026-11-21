# Dòng ẩn (dòng lẻ 1/3/5) và điều kiện kích hoạt — B đọc mã server (CHỈ ĐỌC MÃ, CHƯA CHẠY)

Nguồn: KItemList.cpp `GetEquipEnhance` (~2808), `ms_ActivedEquip` (~54), `InfectionNextEquip` (~1987), `Equip` (~1859); KItem.cpp `ApplyMagicAttribToNPC` (~148).

## Luật gốc
- Mỗi món có 6 dòng magic, đánh số từ 0. Dòng 0/2/4 (chẵn) LUÔN áp. Dòng 1/3/5 (lẻ, "ẩn") chỉ áp khi được kích hoạt.
- nActive = min(3, T). T = (1 nếu ngũ hành NHÂN VẬT sinh ra ngũ hành MÓN) + (số món đang mặc trong 3 ô "kích hoạt" của ô này mà ngũ hành món đó sinh ra ngũ hành MÓN này).
- Khi mặc món: áp dòng chẵn + nActive dòng lẻ đầu tiên (1, rồi 3, rồi 5). Khi mặc/tháo món khác: InfectionNextEquip thêm/bớt dòng lẻ thứ (2n-1) của món láng giềng.
- Quan hệ sinh: g_nAccrueSeries (nạp từ file cấu hình lúc chạy; thường Kim→Thủy→Mộc→Hỏa→Thổ→Kim, CHƯA XÁC MINH trong bản này).

## Bảng ô → 3 ô kích hoạt nó (ms_ActivedEquip)
| Ô (số) | Ba ô kích hoạt (món ở các ô này sinh ra ngũ hành món ở ô trái thì mở dòng lẻ) |
|---|---|
| Mũ (0) | Áo, Dây chuyền, Hộ uyển |
| Áo (1) | Nhẫn dưới, Đai, Giày |
| Đai (2) | Ngọc bội, Hộ uyển, Nhẫn dưới |
| Vũ khí (3) | Dây chuyền, Áo, Mũ |
| Giày (4) | Vũ khí, Mũ, Ngựa |
| Hộ uyển (5) | Giày, Nhẫn trên, Vũ khí |
| Dây chuyền (6) | Đai, Nhẫn dưới, Nhẫn trên |
| Nhẫn trên (7) | Vũ khí, Mũ, Đai |
| Nhẫn dưới (8) | Hộ uyển, Ngọc bội, Dây chuyền |
| Ngọc bội (9) | Giày, Nhẫn trên, Mặt nạ |
| Ngựa (10) | Mặt nạ, Ấn kiếm, Trang sức |
| Mặt nạ (11) | Ấn kiếm, Trang sức, Phi phong |
| **Phi phong (12)** | **Ngựa, Mặt nạ, Ngọc bội** |
| Ấn kiếm (13) | Phi phong, Trang sức, Áo |
| Trang sức (14) | Ngựa, Phi phong, Ấn kiếm |

## Phi phong trong game gốc
- Phi phong KHÔNG có ngoại lệ: dùng đúng luật trên (ô 12). Ngũ hành của phi phong vàng trong GoldItem.csv = 5 (cột nSeries), CHƯA XÁC MINH giá trị 5 ứng hành nào ở server (cần xem bảng series).
- Nhân vật (hệ X) mặc phi phong: dòng lẻ mở khi hệ X sinh hệ phi phong; mỗi món trong {Ngựa, Mặt nạ, Ngọc bội} có hệ sinh ra hệ phi phong mở thêm 1 dòng (tối đa 3).
- Dữ liệu: các dòng của phi phong cấp 1..11 KHÔNG nằm ở cột DefMagic của GoldItem.csv (hầu hết trống) → sinh ở nơi khác (CHƯA XÁC MINH); cần log `[qh_dump equip]` mỗi cấp để biết dòng nào là lẻ.

## Việc đã làm
- Build 3..11 của B ép phi phong áp MỌI dòng (bỏ luật lẻ ẩn). Chủ chỉ ra có thể sai logic gốc. Build 12 (sc-006b12): công tắc `QH_PIFENG_ALL_LINES` mặc định 0 = TRẢ VỀ LUẬT GỐC. Đổi sang 1 chỉ cần định nghĩa lại rồi build.
- Rủi ro đã thấy của kiểu ép: dòng lẻ bị áp 2 lần (khi mặc, rồi InfectionNextEquip của Ngựa/Mặt nạ/Ngọc bội cộng thêm dòng lẻ) và lệch khi tháo.
- Số HP 4528 / 1668 A đo ở build 11 là THEO KIỂU ÉP; build 12 sẽ cho số khác (nhỏ hơn hoặc bằng), A đo lại.

## Phi phong trong chuỗi tương sinh (trả lời A 08:28)
- CÓ. ms_ActivedEquip[12] (ai kích hoạt phi phong) = {Ngựa, Mặt nạ, Ngọc bội}; ms_ActiveEquip[12] (phi phong kích hoạt ai) = {Trang sức, Ấn kiếm, Mặt nạ}. (ĐÃ ĐỌC MÃ KItemList.cpp ~34-70)
- Dữ liệu server: mỗi phi phong cấp g có 5 dòng: Sinh lực 85, Nội lực 89, Thể lực 93, Kháng tất cả 114, Tốc chạy 111 (DESIGN/TINH-NANG/TAI-PHU-PHI-PHONG.md mục f). KHÔNG có dòng Né tránh hay Kỹ năng +3 trong dữ liệu server mà B đọc → hai dòng đó trên tooltip nhiều khả năng đến từ dữ liệu CLIENT riêng (CHƯA XÁC MINH; cần A đối chiếu GoldItem/GoldMagic client với server).
- Kháng tất cả (114): handler AllresP có (KNpcAttribModify.cpp ~336) và cộng vào m_Temp*Resist; A đo kháng không đổi → CHƯA RÕ lý do (nghi cần tính lại ở UpdataCurData, hoặc dòng 114 là dòng lẻ). Build 13 thêm log `[pifeng-active]` để biết.
## Đề xuất "đầy đủ dòng" (chờ chủ chọn, đều có số thật sau khi A đo)
1. Giữ luật gốc (build 13 mặc định): dòng lẻ mở theo ngũ hành + 3 món Ngựa/Mặt nạ/Ngọc bội. Ưu: đúng gốc, an toàn. Nhược: có thể thiếu dòng.
2. Phi phong luôn mở hết (nActive=3) NHƯNG làm ở MỘT chỗ: GetEquipEnhance trả 3 cho ô phi phong và InfectionNextEquip bỏ qua phi phong (tránh cộng 2 lần). Cần build mới, không dùng kiểu ép trong Apply của build 3-11.
3. Theo ngũ hành như gốc, nhưng chủ tự chỉnh hệ phi phong để dễ mở.
