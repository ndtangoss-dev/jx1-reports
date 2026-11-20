# Bản đồ mã đã kiểm + bẫy đã gặp (số dòng theo QH-B035; bản khác lệch — luôn mở file thật)

## Chuỗi cường hóa (đã đo trong game 20/11)
Nút "Cường hóa" client → `__opensysui(2,1)` (KgameWorld.cpp ~14135) → server `opensysui.lua` gọi `Give(...,"sysqianghua","sysError",...)`
(LuaGive ScriptFuns.cpp:24381) → `s2c_opengive` → client `KuiGive_New` → `c2s_playergiveback` nKind=3
→ server `c2sGiveBack` (KProtocolProcess.cpp:9262; ô rỗng → sysError) → `ExecuteScriptD` (KPlayer.cpp:8098)
→ `qianghua.lua` `sysqianghua` → `SetItemEnChance` → `KItem::EnChance` (KItem.cpp ~3800, +5%/cấp từ gốc `m_TempMagicAttrib`).
Đồ VÀNG đi `EnChanceRong` (KItem.cpp ~3860–3910, cũ +25%/cấp, lọc cột ForBitEn `Settings\ForbititMap.txt`), gọi từ
KProtocolProcess.cpp:1686, KItemList.cpp:4404/4907/5119.
Mặc/tháo: `KItemList::Equip` :1621 → `ApplyMagicAttribToNPC`; `UnEquip` :2155 → `RemoveMagicAttribFromNPC`.
Tài phú: dòng ảo `nEnChance×100` (KItem.cpp ~194/293); client đọc bộ đệm chat `g_qhWealth` (dòng `[QH]|W|` từ Lua).

## Lưu / nạp nhân vật
Lưu: KPlayerDBFuns.cpp :1626–1724 (Goddess). Nạp: `LoadPlayerItemList` :818–1150, sinh lại từng món bằng `Gen_*`
(KItemGenerator.CPP `Gen_ExistEquipment` :3201); món sinh lại thất bại bị BỎ IM LẶNG (log khi `gameItemInfo.nshowinfo=1`).
Cấp đồ từ Lua: `LuaAddItem` ScriptFuns.cpp:8980–9100 — 15 tham số ⇒ ngày sinh = 0, IsWhere = 0; ≥21 tham số mới có ngày.
Đồ cấp bằng cách thiếu tham số có thể MẤT sau đăng nhập lại (TN1 20/11: 10/10 đồ xanh mất).

## Nạp Lua nóng
Lệnh bài GM → nút ReloadScript (`gmroleitem.lua` ~1552, `tb_LocalScript`) → `LuaLocalScript` ScriptFuns.cpp:20470
→ `ReLoadScript` KSortScript.cpp:444. Sống trong tiến trình gs001 tới khi restart; file trên đĩa mới là bản lâu dài.
Chi tiết: `JX1_OPS/HIEU-GAME/09-cong-cu-gm/LOADSCRIPT-NAP-LUA-NONG.md`.

## Bẫy đã trả giá
1. Sửa C++ ở đường mới song song (B-040) → gs001 sập 0xC0000005. Sửa trong hàm gốc, có công tắc.
2. Sửa công thức ở server nhưng client có BẢN SAO (EnChanceRong client `KItem.cpp:3565`, KProtocolProcess.cpp:1644) → tooltip vẫn sai.
3. Lua sửa trên đĩa nhưng gs001 vẫn chạy bản cũ trong bộ nhớ → phải ReloadScript hoặc restart.
4. Đồ thị src18 lệch số dòng so với QH-B035 (QiangHua 5393 vs 5487).
5. Không phải dòng thuộc tính nào cũng được nhân: chỉ loại nằm trong `JxQhScalable` (KItem.cpp ~3802) / cột ForBitEn.
6. Bảng loại thuộc tính số → tên: `JX1_OPS/DU-LIEU/VAT-PHAM/BANG-LOAI-THUOC-TINH.csv` (enum MAGIC_ATTRIB, KMagicAttrib.h:6). Loại 30 hiển thị là "Né tránh".

## Bẫy: mất đồ sau đăng xuất/nhập lại (Test-36, 20/11/2026)
`OnLine` (online.lua) chạy TRƯỚC `KPlayer::LoadPlayerItemList`. Lệnh cấp đồ trong OnLine (JXGive282, AddItem, QHBV_Book) xung đột với nạp túi/trang bị: túi chỉ còn ~10 món cơ bản dù Goddess lưu đúng. Cách sửa: không cấp đồ trong OnLine; chỉ cấp ở hook SAU đăng nhập (menu sách). Không đổ lỗi C++ trước khi soát online.lua. Sửa .lua GBK bằng Latin1 (28591), không cp936. (A-B.md #B-063/#321; BAI_HOC.md 20/11.)
