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
