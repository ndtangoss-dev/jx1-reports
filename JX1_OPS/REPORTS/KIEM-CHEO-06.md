# V-01 — kiểm chéo R-07a với mã `D:/JX-build/qh9A` (19/11/2026, lượt 5/5, đóng V-01)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] `AppDelegate.cpp:53,56`: dòng 53 là `curSalx = 0.58`, dòng 56 là `mediumResolutionSize = Size(1040, 1040*curSalx)` = 1040 × 603,2: khớp.
2. [ĐÃ KIỂM] `L02RenderTrial.h:6` là `#define JX_L02_SUBPIXEL 1`: khớp ghi chú "mặc định 1".
3. [ĐÃ KIỂM] `KNpcResVN.cpp:560` (`g_jxAdditive = true`) và `:618` (gọi `jxDrawBolts`): khớp; `goldacition.lua` có ở server Folder/ServerNew (dòng 15 và `gucaxia.lua:80` chưa mở).
4. SỬA SAI CỦA CHÍNH THUỘC HẠ: KIEM-CHEO-03 lúc đầu ghi H-04 "lệch 1 dòng" cho `KgameWorld.cpp:15025` và `KNpcResVN.cpp:618`; đọc lại thì cả hai đúng. Đã sửa tệp 03.
5. Tổng V-01: 5 báo cáo (E-01, H-04, A-05, K-02-nhan-vat, R-07a), không phát hiện sai nội dung; lệch dòng thật chỉ ở E-01 (2 mốc). Chưa kiểm: số liệu runtime/APK. Cần tôi quyết định: không.
