# V-01 — kiểm chéo báo cáo A-05 (điểm tương tác gs001) với mã server (19/11/2026, lượt 3/5)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] Lấy 6 mốc file:dòng của A-05 (ScriptFuns.cpp:6784, 6865; KNpcSet.cpp:1813, 2042; KNpc.cpp:1677, 10365) đối chiếu `gameserver/Sources/Core/Src`: cả 6 đúng với mô tả (đầu hàm `LuaGetAroundNpcList`, `GetRelation`, khối aura `m_ActiveAuraID`, `SetStateSkillEffect`).
2. [ĐÃ KIỂM] 6/6 mốc khớp, 0 lệch dòng, 0 sai tên hàm.
3. [CHƯA KIỂM] Các mốc còn lại của A-05 (KMissle, KSkills, KRegion, KObj, KPlayerTeam, KPlayer; ~12 mốc) và các nhận định "Trung bình-cao" về rủi ro (là đánh giá, không phải dữ kiện mã).
4. Giới hạn: mã nguồn server có thể không khớp exe đang chạy (CLAUDE.md), nên báo cáo đúng với nguồn chứ chưa chứng minh với exe.
5. Cần tôi quyết định: không. Còn 2 báo cáo V-01 (K-02-nhan-vat, R-07a).
