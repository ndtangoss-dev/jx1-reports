# V-01 — kiểm chéo K-02-nhan-vat với mã `D:/JX-build/qh9A` (19/11/2026, lượt 4/5)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] `KNpcResNode.cpp:365-369`: đúng, đọc khóa bảng thứ tự vẽ từ file loại rồi `m_cSortTable.GetcTable(...)`.
2. [ĐÃ KIỂM] `CoreUseNameDef.h:8-10`: đúng, `enum KE_NPCRES_PART` bắt đầu bằng `emNPCRES_PART_HELM`.
3. [ĐÃ KIỂM] `KPakFile.cpp:37` đúng là `SprGetHeader(...)`; dòng 90 là đóng khối, nằm trong phạm vi 37-90.
4. [CHƯA KIỂM] `XPackFile.cpp:597-705`, `KNpcResNode.cpp:612-630, 1390-1480` và các giá trị từng sprite (báo cáo cũng ghi chưa đo).
5. Cần tôi quyết định: không. Còn R-07a.
