# V-01 — kiểm chéo báo cáo H-04 (hiệu ứng vũ khí) với mã `D:/JX-build/qh9A` (19/11/2026, lượt 2/5)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] H-04 dẫn `KNpcResVN.cpp:514-556` cho ba mốc +6/+12/+15: đúng (514 `s_wLevel >= 6`; 517-520 chọn cường độ/màu theo 6/12/15; 556 nhánh `>= 12`).
2. [ĐÃ KIỂM] `KgameWorld.cpp:15025` cho `jxDrawBolts`: đúng (định nghĩa ở dòng 15025; bản đầu của báo cáo này ghi lệch 1 là đọc nhầm, đã sửa 19/11).
3. [ĐÃ KIỂM] `KNpcResVN.cpp:618` cho điểm gọi sét: đúng (lệnh gọi `jxDrawBolts` ở dòng 618; đã sửa nhầm lệch 1).
4. [ĐÃ KIỂM] `GameDataDef.h:1516` cho `itempart_pifeng` (披风): đúng.
5. [CHƯA KIỂM] APK qh1–qh8, FPS, trên điện thoại (chính H-04 cũng ghi chưa phủ). Cần tôi quyết định: không. Còn 3 báo cáo trong V-01 (A-05, K-02-nhan-vat, R-07a).

Ghi chú: mã nguồn trích ở `D:/JX-build/qh9A`, không ở repo chính; repo chính chưa có hệ glow/bolt.
