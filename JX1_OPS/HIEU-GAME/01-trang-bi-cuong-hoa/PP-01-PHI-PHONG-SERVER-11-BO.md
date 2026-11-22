# PP-01 Phi phong server: 11 bộ, giới tính, dòng ẩn (B, 22/11/2026, đọc tĩnh)
Nhãn: DỮ LIỆU = đọc file trong repo `DU-LIEU/VAT-PHAM` (bản sao, CHƯA đối chiếu bản trên VM Test-36); MÃ = đọc mã SC-006B; CHƯA KIỂM = chưa chạy.

## 11 bộ trong GoldItem (DỮ LIỆU, item_004/GoldItem.csv dòng 3467–3477)
- 11 dòng liên tiếp, ItemGenre 0, DetailType 12 (phi phong), ParticularType 0, động ảnh `pifengtubiao\pifeng_01..11.spr`, nSeries 5, giá 999, nLevel 1,1,2,3,3,4,4,4,5,5,5 (tên: Lăng Vân, Tuyệt Thế, Phá Quân, Ngạo Tuyết, Kình Lôi, Ngự Phong, Phệ Quang, Khấp Thần, Kình Thiên, Vô Cực, cao cấp).
- Yêu cầu mặc: cột Require chỉ có loại 36 = 60 (không có yêu cầu giới, không có yêu cầu hệ phái). => "11 bộ theo giới" KHÔNG có trong dữ liệu server: cả nam lẫn nữ cùng một món, cùng một ảnh biểu tượng. Nếu cần ảnh khác giới thì phải làm ở client (PaintPifeng/PiFengRes), không phải GoldItem.
- Chỉ dòng đầu (Lăng Vân) có 6 mã GoldMagic 418,354,320,88,6,423; 10 dòng sau để trống => theo ghi nhận A-B (B-080) bản triển khai cho 11 mẫu dùng chung 6 dòng của mẫu đầu. Mã 5 dòng sinh lực/nội lực/thể lực/kháng/tốc chạy: xem TAI-PHU-PHI-PHONG.md mục f.
- Dòng 3478 "Phi Phong Phệ Quang" nLevel 7 là mẫu biến thể thứ 12, KHÔNG thuộc 11 bộ.

## Hình theo cấp (DỮ LIỆU)
`PiFengRes.csv`: Line 0 → ResId -1; Line 1..n → ResId = Line (đồng nhất, 27 dòng). Client dùng `GetPifengRes` (KItemList.cpp:1310) với nhánh×10+cấp+2; không phụ thuộc giới.
`mantle.csv` chỉ có 3 dòng mẫu "Phá cũ phi phong" (cấp 1–3) từ bản gốc, không liên quan 11 bộ vàng.

## Dòng ẩn (MÃ)
Giữ nguyên BANG-DONG-AN-KICH-HOAT.md: QH_PIFENG_ALL_LINES=0 = luật gốc (dòng 1/3/5 theo nActive, tối đa 3); =1 = áp mọi dòng. Chủ chốt 0/1 là quyết định của chủ (chưa có).

## Kế hoạch nạp + đo (CHƯA LÀM, chờ 3 bên L22)
1. Nạp chung b113 + b119c (CoreServer.dll) khi chủ duyệt; QH_PIFENG_ALL_LINES theo chủ.
2. Đo: mặc từng bộ k1..k11 bằng atestqhhai, đọc `[pifeng-active]` (nActive/hệ/kháng/né) và so sinh lực/nội lực/thể lực với bảng +200k/+100k của A.
3. Hoàn tác: backup CoreServer.dll/GameServer.exe *.bak-b113, Stop-Process gs001, chép lại, schtasks /run JX-ChainUp.

## CHƯA KIỂM
- GoldItem/GoldMagic trên VM có giống bản repo không (cần SHA-256 đối chiếu khi được phép đọc VM).
- 5 dòng thuộc tính server thực sự áp khi mặc (kháng tất cả 114 không đổi theo A: chưa rõ nguyên nhân).

## Đối chiếu VM Test-36 (B-121, 22/11 07:36, chỉ đọc)
- DA XAC MINH: `gs\Settings\item\GoldItem.txt` trên VM (5946 dòng, SHA-256 0C81979D…3EB5) TRÙNG bản `DESIGN/QH-B080-deploy/phiphong/GoldItem.txt`, KHÔNG phải bản `DU-LIEU/VAT-PHAM/item_004` ở trên (bản đó là bản gốc cũ: tên khác nhau từng bộ). Trên VM, dòng 3467–3477 cùng tên "Phi phong Lăng Vân", ảnh pifeng_01..11, nLevel 1,1,2,3,3,4,4,4,5,5,5, yêu cầu loại 36=60 + 6 mã GoldMagic của mẫu đầu; dòng 3478 là mẫu biến thể. Vẫn không có yêu cầu giới.
- DA XAC MINH: menu `hotrotanthu.lua` (dòng 113–162) 11 lựa chọn phi phong gọi AddGoldItem(3465..3475) = dòng 3467–3477; hook `qh_bothu.lua` #376 `qhbv_pf` thêm AddGoldItem(3464+k) cùng 11 bộ (dòng 198–206).
- CHUA KIEM: nhãn [cấp N] (phía client) và hiển thị trong game.

## PP-B1 (B-128, 22/11 09:21) Vì sao 10 bộ không có dòng thuộc tính + GoldItem đúng
ĐÃ ĐỌC SỔ TAY: PP-01-PHI-PHONG-SERVER-11-BO.md, TAI-PHU-PHI-PHONG.md mục (f), SO-TAY-NHAN-CAP.md.
- DA XAC MINH (đọc 3 bản trong kho, byte TCVN3): GỐC (`GoldItem.txt.bak-goc`) chỉ dòng "Lăng Vân" có 6 mã DefMagic 418,354,320,88,6,423; 10 dòng sau TRỐNG => đúng lỗi chủ thấy ("10 bộ không có dòng thuộc tính"). B080 (đang chạy trên VM, SHA 0C81979D…) sửa bằng cách chép 6 mã của Lăng Vân vào cả 11 dòng (dùng chung) và đặt cả 11 tên là "Phi phong Lăng Vân". B035 (QH-B035-deploy) làm đúng thiết kế: mỗi bộ k có 5 dòng riêng DefMagic 4361+5(k-1)..+4 (GoldMagic QHPP01..11: sinh lực/nội lực/thể lực/kháng/tốc chạy, bảng mục (f)), không có mã thứ 6.
- Tên thiếu dấu: cột tên (cột 1) của bản gốc/B035 viết "Ngao tuyết", "Kinh Lôi" (không dấu) trong khi cột mô tả szIntro có dấu "Ngạo", "Kình"; dòng "Khấp Thần" B035 có hai khoảng trắng ở dòng 3475 szIntro. Tooltip LD dùng cột tên => "Phi Phong Ngao tuyết" (A báo 08:14).
- NLevel 1,1,2,3,3,4,4,4,5,5,5 đã đúng ở cả ba bản (nhãn "[cấp 1]" cho mọi bộ là phía client, PP-A2 của A).
- GoldItem.txt MỚI = `DESIGN/QH-B128-deploy/phiphong/GoldItem.txt` (SHA-256 dbd525b8…): lấy B035, chỉ sửa 3 dòng (3470 Ngạo Tuyết, 3471 Kình Lôi, 3475 bỏ khoảng trắng thừa) + bảo đảm tên = mô tả có dấu cho 11 dòng; kèm `GoldMagic.txt` = B035 (có 55 dòng QHPP, SHA e676190a…). KHÔNG đổi dòng khác (so với B035: đúng 3 dòng khác).
- Kế hoạch nạp (CHƯA LÀM, chờ 3 bên + phép chủ restart gs001, chủ thoát game ~5 phút): backup *.bak-b128 cả 2 file + SHA; chép GoldItem.txt + GoldMagic.txt vào `gs\Settings\item\` (đúng thư mục VM, kiểm lại đường dẫn; HUONG-DAN-A ghi `item`); nạp CHUNG checkpoint-b119c (b113); sau restart đọc [pifeng-active], mặc từng bộ (SetTestWealth) so bảng (f); hoàn tác = chép .bak, Stop-Process gs001, schtasks /run JX-ChainUp.
- DA XAC MINH (VM, chỉ đọc 22/11): `gs\Settings\item\GoldMagic.txt` trên VM chỉ 3821 dòng (151142 byte, SHA 3B2BF8A5…A318) => KHÔNG có 55 dòng QHPP (4361+). Vì vậy nạp GoldItem B128 BẮT BUỘC kèm GoldMagic B128 (4417 dòng), nếu không DefMagic 4361+ trỏ ra ngoài bảng.
- CHUA KIEM: client có cần cùng cột tên (tooltip có thể dùng dữ liệu client riêng của A).
