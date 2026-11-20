# BẢN ĐỒ CHUỖI CƯỜNG HÓA — PHẦN SERVER (B, 20/11, #B-045)
Nguồn: đồ thị Graphify dựng lại từ `D:\JX-wt\QH-B035\...\Sources\Core\Src` (AST, 12034 nút) + đọc mã. A giữ phần client. Số dòng theo QH-B035 (base B-039). **CHỈ ĐỌC MÃ, CHƯA CHẠY.**

| Bước | Hàm | file:dòng |
|---|---|---|
| 1. Mở UI Give | `opensysui(2,1)` → Lua `Give(mô tả,nÔ,nÔCallback,"sysqianghua","sysError",title)` | gs\script\System\opensysui.lua:25 (gốc) |
| 2. Đóng gói | `LuaGive` (đối số 2 = số ô, 3 = số ô callback ≠0, 4 callback, 5 lỗi, 6 title); gửi `s2c_opengive` (`PLAYER_GIVE`, m_szName[256]); `ClearRoom(room_give)` | ScriptFuns.cpp:24381 (`LuaGiveItemUI` 24321 cùng giao thức, thứ tự đối số khác) |
| 3. Client khóa món | `c2s_lockitem` → `KProtocolProcess::c2slockitem` | KProtocolProcess.cpp:323 (đăng ký) |
| 4. Xác nhận | `c2s_playergiveback` → `c2sGiveBack`; nhánh callback kiểm `m_nGiveCallBackScript && m_nGiveCallBackNum` | KProtocolProcess.cpp:291, 9214; gọi script 9242; lỗi 9250/9327 |
| 5. Chạy Lua | `KPlayer::ExecuteScriptD` (tìm script theo id, nIsGive → gán `Npc.m_ActionScriptID`, gọi `sysqianghua(chuỗi id, parm, nNum)`) | KPlayer.cpp:8098 |
| 6. Lua cường hóa | `sysqianghua` (gốc: đá 403/404/405 + 200000; B-043: luật Q-86) | System\qianghua.lua:10 (gốc); DESIGN/QH-B044-deploy/qianghua.lua |
| 7. API | `LuaItemQiangHua` → `KItemList::QiangHua` | ScriptFuns.cpp:7927; KItemList.cpp:5487 |
| 8. Đổi giá trị | xanh/tím `KItem::EnChance` (+5% từ gốc `m_TempMagicAttrib`); vàng `EnChanceRong/Bao` (gộp, khác) | KItem.cpp:3820 / 3880; gọi ở KItemList.cpp:5572–5601 |
| 9. Đồng bộ | `SynPlayerItem(idx)` | cuối QiangHua; `LuaSetItemEnChance` ScriptFuns.cpp:~10963 |
| 10. Mặc | `KItemList::Equip` (nActive=`GetEquipEnhance`, `ApplyMagicAttribToNPC` 1547/1852) | KItemList.cpp:1619 |
| 11. Tháo | `KItemList::UnEquip` (`RemoveMagicAttribFromNPC` 2208) | KItemList.cpp:2155 |
| 12. Áp/gỡ thuộc tính | `KItem::ApplyMagicAttribToNPC` / `RemoveMagicAttribFromNPC`; dòng ảo kỹ năng +14/+15 và tài phú ở 184–198 / 283–297 | KItem.cpp:140 / 275 |

Quan sát: (a) QiangHua không kiểm đồ đang mặc; UI Give chỉ cho đồ trong túi ⇒ cường hóa gốc làm trên túi. (b) `m_ActionScriptID` chỉ chắc chắn được gán khi callback chạy qua `ExecuteScriptD(...,TRUE)` (9242); lúc mở UI nó phụ thuộc script đang chạy ⇒ B-044 thêm `Include qianghua.lua` vào opensysui. (c) Chưa xác minh: baseline `m_TempMagicAttrib` sau nạp DB (xem A-B.md #B-043 mục 1).
