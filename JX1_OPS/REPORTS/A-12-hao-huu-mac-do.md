TÓM TẮT 1: [NGUỒN] Đồ đồng bạn đang mặc nằm ở pos_dazao/X=53–77: 5 nhóm ngũ hành × 5 vị trí; room_equipmentex chỉ là kho chung của player (S/KItemList.cpp:354–368,438–441; S/KNpc.cpp:7301–7341).
TÓM TẮT 2: [NGUỒN] TonEquip → ApplyMagicAttribToNPC → ModifyAttrib → UpdataNpcCurData/ReCalcNpcEquip/UpMagicAttrib cộng lại đồ vào NPC; máu/phòng thủ có handler, nhưng bốn điểm cơ bản và allskill loại NPC không phải player (S/KItemList.cpp:1451–1481; S/KNpcAttribModify.cpp:632–636,1307–1315,1362–1369,2158–2165,2194–2201).
TÓM TẮT 3: [NGUỒN] CanTonEquip đòi thuộc tính needtongban, nhưng EnoughAttrib kiểm sức mạnh/thân pháp/sinh khí/nội công/cấp/giới tính của CHỦ; không dùng nguyên hàm để kiểm riêng hảo hữu (S/KItemList.cpp:1095–1139,1229–1279).
TÓM TẮT 4: [NGUỒN] Item được lưu theo ilocal/ix/iy, chưa có companion ID; mở 10 bộ đồ phải đổi ánh xạ. Ngoài buffer role 128 KiB còn có nTaskCount BYTE cần kiểm giới hạn 255 (S/KPlayerDBFuns.cpp:1651–1653,1844–1863; L/S3DBInterface.h:193; S/KPlayer.h:284).
TÓM TẮT 5: [NGUỒN]/[CHƯA KIỂM] Có data áo/giáp/vũ khí theo cấp/giới tính và bảng rơi boss; chưa chứng minh UI mặc đồ đồng bạn, ngoại hình đổi theo đồ, thưởng nhiệm vụ đồ thường hay round-trip DB đang hoạt động (G/Settings/item/armor.txt:2–4,11,81; G/script/task/bigboss.lua:16–28,87–96; mục d/f).

# A-12 — Hảo hữu mặc đồ

Ngày khảo sát: 17/11/2026. Nội dung khảo sát tĩnh: **DONE** cho sáu câu hỏi; phần không đủ bằng chứng được đánh dấu. Trạng thái bàn giao/Git ghi cuối báo cáo. Không sửa source, không chạy exe/build/test game, không kết nối VM/SQL/server và không tải dữ liệu dự án ra ngoài.

## Worker kiểm tra trước khi làm

- Đã đọc task trước. `Get-Location` = `D:\JX-wt\A-12`; `git status --short --branch` = `## task/A-12-hao-huu-mac-do`, có sẵn `?? JX1_OPS/TASKS/A-12.md`. Khớp worktree/branch được giao; giữ nguyên nội dung task ngoài mục Kết quả. Task vốn chưa được theo dõi, vì vậy stage nó sẽ đưa cả nội dung task có sẵn vào commit theo yêu cầu người dùng.
- Chỉ ghi báo cáo này và mục Kết quả trong task. Canonical `C:\Jx1CocoV3` chỉ đọc; không sửa Cocos, cấu hình, credential hay dữ liệu tài khoản.
- Đọc nền A-08a/b/c/d, A-09 và A-05. Đầu ra gộp ban đầu bị rút gọn; đọc riêng A-08b/A-09 và các đoạn liên quan của báo cáo còn lại. Kết luận mới dưới đây dựa trên canonical đọc trực tiếp, không lấy đường src18 của A-08b làm bằng chứng canonical.
- Phạm vi là khảo sát, không thiết kế/triển khai đầy đủ 10 slot. Yêu cầu đồ không theo phái được giữ làm luật đích; khả năng engine kiểm phái không được biến thành đề xuất chia đồ theo phái.

## Gốc bằng chứng

| Tiền tố | Đường tuyệt đối |
| --- | --- |
| S/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/Core/Src/` |
| L/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Lib/` |
| C/ | `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes/` |
| G/ | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/` |

[NGUỒN] Số dòng vật lý từ 1. Markdown đọc UTF-8; source legacy đọc CP936, bảng có chuỗi Việt legacy đối chiếu token/cột số, không suy tên từ mojibake. Không khẳng định source khớp exe/PAK. `[ĐỀ XUẤT]` là hướng xử lý sau khảo sát, chưa có mã; `[CHƯA KIỂM]` không đồng nghĩa không tồn tại.

## a) Kho, vị trí mặc/tháo và giao diện

[NGUỒN] Cần tách hai lớp:

| Thành phần | Điều đã xác định |
| --- | --- |
| Kho `room_equipmentex` / `pos_equiproomex` | Một kho của KItemList player, Init bằng REPOSITORY_ROOM_WIDTH/HEIGHT; Add dùng PlaceItem(x,y,width,height). Không phải mảng các bộ đồ theo companion (S/KItemList.cpp:354–368,1050–1056). Client có enum tương ứng (C/gamecore/GameDataDef.h:250,272). |
| Đồ đồng bạn đang mặc | `m_ItemBox[nEquipPlace]`, `pos_dazao`, X=vị trí, Y=0; Add chỉ gọi TonEquip nếu X 53..77 (S/KItemList.cpp:438–441,1417–1421). |
| 25 vị trí | Kim 53–57, Mộc 58–62, Thủy 63–67, Hỏa 68–72, Thổ 73–77. Khi không truyền vị trí, ReCalcNpcEquip chọn nhóm theo template đối chiếu FuMoNpcSet/Mo_0..Mo_4; khi truyền vị trí thì chọn nhóm chứa vị trí đó (S/KNpc.cpp:7265–7341). **Không phải 25 món đồng thời cộng vào cùng một con**: hàm chỉ quét 5 ô của nhóm được chọn. |
| Cách mặc/tháo | Nhánh di chuyển đồ gỡ món cũ bằng UnTonEquip, gọi CanTonEquip/TonEquip cho đồ trên tay, nếu không đạt thử mặc lại đồ cũ; gửi PLAYER_MOVE_ITEM_SYNC (S/KItemList.cpp:7261–7290). Remove của pos_dazao cũng gọi UnTonEquip ở dải 53..77 (S/KItemList.cpp:793–803). |
| Chọn con nhận đồ | CanTonEquip/TonEquip/UnTonEquip đều giải một DWID `m_TongBanNum` của chủ qua NpcSet.SearchID; đòi con đang triệu hồi, không có tham số companion ID/roster slot (S/KItemList.cpp:1100–1112,1380–1394,1968–1976). |

[NGUỒN] Luật vừa vị trí gốc `Fit` và tự chọn vị trí trong CanTonEquip/TonEquip đang bị comment; thay bằng requirement `magic_item_needtongban` và kiểm `nPlace == nValue[0]` tại EnoughAttrib (S/KItemList.cpp:1114–1127,1341–1354,1403–1412). Vì vậy chưa thể đưa đồ thường vào ô cũ chỉ bằng thao tác UI. Đã thấy một dòng PlantItem mang cặp requirement `47,62` tại phần cuối record, tương ứng enum needtongban=47 theo phép đếm enum; đây là ví dụ đồ chuyên dụng legacy, không phải luật đích cho đồ người chơi tự kiếm (G/Settings/item/PlantItem.txt:49; S/KMagicAttrib.h:7–60).

[CHƯA KIỂM] Chưa đặt tên chắc chắn cho từng ô trong 5 ô (vũ khí/áo/mũ...): source đang chứng minh **mã vị trí và nhóm**, không có đủ ánh xạ nhãn UI. Không tự gán 5 ô thành bộ đồ người chơi hoặc thành 10 hảo hữu.

[NGUỒN] Client có logic CanTonEquip/TonEquip/UnTonEquip và thao tác dải 53..77 (C/gamecore/KItemList.cpp:823,1051–1140,1502–1545,3638–3655); có lệnh mở/chuyển đồ vào kho phụ room_equipmentex (C/gameui/KuiItem.cpp:497; C/gameui/KuiItem_New.cpp:862,1218; C/gameui/KuiItemEx_old.cpp:253,474). Đây chứng minh đường kho/UI hỗ trợ item, **chưa chứng minh panel mặc đồ riêng cho đồng bạn đang được mở và hoạt động**. Tìm các token fumo/tongban/GOI_*PARTNER trong `.cpp` của gameui không ra panel tương ứng; tìm kiếm có giới hạn, chưa kiểm bản VN, resource UI hay cấu hình biên dịch.

## b) Đường cộng chỉ số thực tế

[NGUỒN] Chuỗi đã nối trực tiếp:

`KItemList::TonEquip` chọn NPC → `KItem::ApplyMagicAttribToNPC` duyệt base/magic/thuộc tính phụ → `KNpc::ModifyAttrib` → `g_NpcAttribModify.ModifyAttrib` dispatch handler; sau đó `UpdataNpcCurData(owner,place)` reset current từ base và `ReCalcNpcEquip` → `UpMagicAttrib` đọc lại 5 ô từ item list của chủ rồi áp từng item vào chính NPC (`S/KItemList.cpp:1380–1394,1451–1481`; `S/KItem.cpp:140–255`; `S/KNpc.cpp:4458–4461,7081–7128,7261–7394`; `S/KNpcAttribModify.cpp:322–332`).

[NGUỒN] Không được cộng riêng lần đầu và lần tính lại thành “nhân đôi”: ở giữa có reset current. Cũng không được suy tất cả base attribute đều có tác dụng: dispatch bỏ loại ngoài miền hoặc handler NULL (S/KNpcAttribModify.cpp:329–332).

| Nhóm chỉ số | Handler/giới hạn đã kiểm |
| --- | --- |
| Máu tối đa | LifeMaxV cộng vào m_CurrentLifeMax; LifeMaxP tính từ m_LifeMax, không có guard player ở đây (S/KNpcAttribModify.cpp:1606–1627). Không đồng nghĩa tự hồi đầy m_CurrentLife. |
| Phòng thủ/né tránh | magic_armordefense_v và magic_adddefense_v trỏ ArmorDefenseV, cộng m_CurrentDefend (S/KNpcAttribModify.cpp:34,39,2355–2361). Không đánh đồng với toàn bộ kháng/hấp thụ. |
| Sát thương | magic_physicsdamage_v trỏ AddPhysicsMagic, cộng m_CurrentPhysicsMagicDamageV (S/KNpcAttribModify.cpp:78,2596–2602). Có đường cộng damage; **chưa bảo đảm mọi loại vũ khí/skill dùng đủ chỉ số đó**. Khối gọi SetNpcDamageAttrib cho vũ khí trong TonEquip bị comment (S/KItemList.cpp:1463–1472). Không thấy đăng ký magic_weapondamagemin_v/max_v trong file dispatch đã tìm, nên chưa kết luận damage trắng của mọi vũ khí áp dụng giống player. |
| Sức mạnh/thân pháp/sinh khí (Vitality)/nội công (Energy) | StrengthV, DexterityV, VitalityV, EnergyV đều return khi kind != kind_player; chúng đi vào ChangeCur* của KPlayer. Partner là kind_partner nên không nhận bốn điểm qua handler gốc này (S/KNpcAttribModify.cpp:1307–1315,1362–1369,2158–2165,2194–2201; S/KNpcSet.cpp:882). |
| Cấp kỹ năng từ đồ | AllSkillV return khi !IsPlayer, vì thế thuộc tính +tất cả kỹ năng không tự tăng level partner (S/KNpcAttribModify.cpp:632–636). KItem có sinh allskill cho vũ khí +12/+15 nhưng vẫn gặp guard này (S/KItem.cpp:183–191). |
| Passive | Sau mặc, server duyệt skill 1..5 và cast lại skill kiểu SKILL_SS_PassivityNpcState (S/KItemList.cpp:1484–1507). Đây không phải chứng minh mọi bonus skill từ đồ được áp dụng; buff/aura/từng handler khác chưa kiểm hết. |
| Tháo | RemoveMagicAttribFromNPC rồi xóa ô, UpdataNpcCurData tính lại từ các món còn lại; không chỉ đổi hình hiển thị (S/KItemList.cpp:1999–2014; S/KItem.cpp:265). |

[ĐỀ XUẤT] Dùng lại đường reset/tính lại chỉ số, nhưng tách danh sách đồ của **đúng con** và xác định danh sách handler hỗ trợ partner. Không coi câu “mặc đồ tăng chỉ số” là bằng chứng bốn điểm cơ bản, damage trắng và +skill đã hoàn chỉnh. Chưa thay đổi logic gốc trong task này.

## c) Điều kiện mặc riêng hảo hữu

[NGUỒN] KNpc có `m_Level` và `m_nSex` (0 nam/1 nữ), Load lấy level từ template; AddTongBan tạo kind_partner và gắn chủ (S/KNpc.h:340,736; S/KNpc.cpp:11155–11158; S/KNpcSet.cpp:858–893). **Có trường sex không chứng minh từng template hảo hữu được gán đúng giới tính**: chưa nối toàn bộ đường khởi tạo sex theo 10 con.

[NGUỒN] Bốn điểm gốc/current của người chơi nằm ở KPlayer (`S/KPlayer.h:369–380`). Trong KNpc.h đã tìm các token m_nStrength/m_nDexterity/m_nVitality/m_nEngergy/m_nCurEngergy không thấy bộ tương ứng; KNpc có current combat stats và m_CurrentAddDexterity, nhưng không thay thế bộ bốn điểm để xét điều kiện (S/KNpc.cpp:7113–7128). Ngoại công/nội công sát thương, sinh lực và bốn điểm phân bổ không nên coi là một trường.

[NGUỒN] `CanTonEquip` gọi chung `EnoughAttrib`; hàm đó kiểm STR/DEX/VIT/ENG từ Player[m_PlayerIdx], cấp/giới tính/ngũ hành từ **NPC của chủ**, không từ nTonNpcIdx. Nhánh needtongban chỉ kiểm có con và mã vị trí (S/KItemList.cpp:1131–1138,1229–1279,1341–1354). Do đó một chủ đủ cấp không chứng minh con đủ cấp; một chủ nam có thể ảnh hưởng kiểm đồ cho con nữ theo code hiện tại.

[NGUỒN] Engine còn có handler điều kiện môn phái/ngũ hành/skill/chuyển sinh/bang chủ và nhánh item GetUseKind()==1/GetUseMapIdx()>0 bỏ qua yêu cầu (S/KItemList.cpp:1215–1223,1261–1340). Đây là khả năng của engine, không phải khẳng định đồ thường theo phái và không đổi yêu cầu task. Các mẫu đồ thường mục f chỉ thấy điều kiện cấp, điểm, giới tính.

[ĐỀ XUẤT] Dùng chung bộ so sánh điều kiện với một context nhận companion ID, sex, level, STR/DEX/VIT/ENG của con; giữ luật đích không theo phái. Cần thêm/persist bốn điểm cho roster hoặc chốt công thức tăng trưởng riêng; chỉ thay m_PlayerIdx không biến NPC thành KPlayer hợp lệ. Tách base/current khi xét đồ và chính sách tháo đồ phụ thuộc để tránh vòng tự đáp ứng requirement; chưa triển khai hoặc chốt công thức.

## d) Ngoại hình client

[NGUỒN] TonEquip của cả server/client chỉ cập nhật item position, áp stats và tính lại; trong thân đã đọc không có gán m_ArmorType/m_HelmType/m_WeaponType hoặc SetArmor/SetWeapon cho con (S/KItemList.cpp:1374–1514; C/gamecore/KItemList.cpp:1051–1143). Comment “đổi ngoại hình” không phải lệnh thực thi.

[NGUỒN] NPC có đường dựng tài nguyên ngoại hình, nhưng gói NPC_SYNC đã đọc gửi kind, series, ID, MAKELONG(level,template), tên, không có ba trường item hình như nhánh PLAYER_SYNC. Nhánh player lại gửi HelmType/ArmorType/WeaponType (S/KNpc.cpp:7664–7709,8083–8087; C/gamecore/KNpc.cpp:701–704). Vì vậy **chưa có bằng chứng mặc đồ trên partner đổi ngoại hình trên client theo đường TonEquip hiện tại**. Không suy từ việc NPC renderer có SetArmor rằng đồ đã nối vào nó.

[CHƯA KIỂM] Packet phụ/thay template, model human NPC, bộ sprite nam/nữ, animation từng vũ khí, bản client khác và PAK. Nếu yêu cầu hiện hình món đồ, cần task riêng nối appearance server→wire→client và kiểm viewer/spawn/đổi map; A-05 là nền các đường đồng bộ, không sửa chúng trong khảo sát này.

## e) Lưu/tải khi có 10 hảo hữu

[NGUỒN] Save duyệt item list của player và ghi loại/tier/series, ilocal/ix/iy, seed/thuộc tính...; load dựng NewItem rồi m_ItemList.Add tại tọa độ lưu (S/KPlayerDBFuns.cpp:1620–1668,1112–1119). Đồ partner hiện lưu như một item pos_dazao với X 53..77, không thấy khóa roster slot/companion ID tại đường đó (S/KItemList.cpp:1417–1421; L/S3DBInterface.h:213–280). iid có tồn tại nhưng không được đồng nhất với companion ID, iequipcode đang ghi 0 (S/KPlayerDBFuns.cpp:1644–1645).

[NGUỒN] Add gọi TonEquip cho đồ đã lưu nhưng TonEquip từ chối nếu chưa có NPC triệu hồi (S/KItemList.cpp:438–441,1382–1394). Điều này chứng minh chưa thể kết luận login tự áp đầy đủ stats. Cần thứ tự khôi phục roster→item mapping→spawn→tính lại, không lưu DWID phiên cũ. Nền A-09 đã ghi m_TongBanNum là scalar và AI từng con ghi đè nó (JX1_OPS/REPORTS/A-09-dong-ban-nhieu-slot.md, mục 2); kiểm trực tiếp TonEquip xác nhận chọn con qua scalar.

[ĐỀ XUẤT] Giữ một bản vật phẩm thuộc chủ, gắn companion ID bền + equip slot riêng cho từng con; 10 roster khác số active NPC. Mặc/tháo phải kiểm chủ, slot đã mở, item không đang giao dịch/đang mặc nơi khác; khi despawn vẫn giữ mapping, spawn tính lại từ base + đúng bộ đồ. Không nhân bản vật phẩm vào task values. Chưa chốt schema, chưa sửa room enum/DB/packet.

[NGUỒN] Hai rào dung lượng cần xem cùng nhau:

- Buffer cả role `m_GaemSaveBuffer[128*1024]`; item/task/base/skill dùng chung, không có buffer riêng mỗi con (S/KPlayer.h:284; S/KPlayerDBFuns.cpp:1622–1624,1844–1863).
- `TRoleData.nTaskCount` trong canonical Lib là **BYTE**, nItemCount là short; save tăng nTaskCount cho mỗi task khác 0 rồi gán vào trường này. Vì vậy nếu hợp đồng đúng header này, hơn 255 task khác 0 có nguy cơ thu hẹp số đếm, dù vẫn còn buffer (L/S3DBInterface.h:191–201; S/KPlayerDBFuns.cpp:1846–1863). Headers/S3DBInterface.h:85 và Sources/Core/lib/s3dbinterface.h:85 cũng khai báo BYTE nhưng là bản khác. KPlayerDBFuns include Lib ở nhánh không _STANDALONE, nhánh còn lại dùng include path (S/KPlayerDBFuns.cpp:8–15). ABI/header thực dựng và gateway chưa kiểm.

[ĐỀ XUẤT] Nếu chỉ tham khảo ví dụ A-09 16 int/con + 6 int chung: 10 con = 166 record = 1328 byte payload task khi tất cả khác 0; **chỉ còn tối đa 89 record khác 0 cho mọi task khác nếu trần đếm là 255**. Ví dụ 15 con = 246 record còn 9; không phê chuẩn phương án này. Đây là phép tính từ L/S3DBInterface.h:193,205–210, không phải đo save thực. Riêng trang bị 10×5=50 item nếu giữ 5 ô/con; 5 là nền legacy, chưa phải số ô đích đã duyệt. Dung lượng item = số item × sizeof(TDBItemData theo ABI thực), cộng toàn role và mapping; không công bố số byte chính xác khi chưa build/kiểm packing và gateway. Cần cập nhật thiết kế nối A-09 với rào nTaskCount trước triển khai; không sửa báo cáo A-09 ngoài phạm vi.

[CHƯA KIỂM] Round-trip DB, item-limit của inventory, khóa bền chống trùng, save lỗi/rollback, reconnect/chuyển GS, giới hạn gateway/Goddess và migration dữ liệu có sẵn. Không có test DB theo task.

## f) Data trang bị và nguồn kiếm đồ

[NGUỒN] Bảng TAB có header loại, tier, base attributes và 6 cặp requirement; tier của món không đồng nghĩa cấp người mặc. Ví dụ mã requirement 36=level,32=STR,33=DEX,38=sex theo enum (S/KMagicAttrib.h:7–52); số dòng là vị trí vật lý, không gọi là item ID.

| Data có sẵn | Mẫu điều kiện đã trích |
| --- | --- |
| G/Settings/item/armor.txt:2–4 | Tier 1/2/3, level mặc 1/7/13, STR 30/50/70, sex 0; base mã 30/31 có giá trị. |
| G/Settings/item/armor.txt:11,81 | Cùng tier 10, level mặc 60; mẫu nam sex 0 STR 210, mẫu nữ sex 1 STR 150. Không yêu cầu phái trong các cặp requirement của hai dòng này. |
| G/Settings/item/helm.txt:2,11 | Mũ tier 1/10, level 1/60, STR 30/210, sex 0. |
| G/Settings/item/meleeweapon.txt:2–4 | Vũ khí gần tier 1/2/3; level 0/9/18, STR 20/20/30, DEX 0. Có base damage min/max mã 28/29, chưa chứng minh partner nhận đủ như player. |
| G/Settings/item/rangeweapon.txt:2 | Level 0, STR 0, DEX 30. |
| G/Settings/item/belt.txt:2; boot.txt:2; cuff.txt:2 | Có đai/giày/hộ uyển; mẫu level 1, điểm yêu cầu khác nhau; giày sex 0, hộ uyển sex 1. |
| G/Settings/item/ring.txt:2; pendant.txt:2; horse.txt:2 | Có nhẫn (level 1), bội (level 1/sex 1), ngựa (level 20). Sự có mặt data không chứng minh ô partner hỗ trợ mặc chúng. |

[NGUỒN] Đồ thường trong các mẫu trên không có requirement needtongban; CanTonEquip hiện bắt buộc requirement đó (S/KItemList.cpp:1120–1127). Do đó **data đồ người chơi có sẵn nhưng đường mặc đồng bạn legacy chưa dùng được nguyên trạng cho mục tiêu này**. Không đề xuất tạo đồ theo phái hoặc bắt người chơi dùng đồ pet chuyên dụng trái yêu cầu.

| Nguồn kiếm | Bằng chứng và giới hạn |
| --- | --- |
| Quái/drop bảng thường | G/Settings/droprate/npcdroprate40.ini:1–22 có mức item 2..3, các entry Genre=0/Detail=0/Particular=0; engine có LoseSingleItem (S/KNpc.cpp:11899,12606). Đây là bảng và đường sinh item, chưa xác nhận quái nào đang gắn đúng file trong binary. |
| Boss | G/script/task/bigboss.lua:16–28 cấu hình nhiều boss trỏ Settings/mapdroprate/sjboss/putong.ini; lấy nSdropRate tại :48 và gọi LoldDropRate sau AddNpc tại :87–96. Bảng putong.ini:2–30 có Count=59, MagicRate=50, mức 10, nTypeNum=30, entry Genre=0/Detail=0. Có chuỗi script→bảng đồ, không tuyên bố tỉ lệ thực/30 món luôn rơi. |
| Đường chết | NPC thường có thể gọi DropRate trong drop script; NPC lấy m_pDropRate từ template (S/KNpc.cpp:2483–2488,11176–11182). Ở loader template, đọc DropRateFile từ Npcs.txt bị comment trong khối đã xem, nên không chỉ dựa cột header để xác nhận gắn bảng; đường script LoldDropRate là bằng chứng riêng (S/KNpcTemplate.cpp:697–724). |
| Hoạt động/nhiệm vụ | G/script/missions/°ÍÁê»î¶¯/°ÍÁêÈë³¡.lua:29–39 có AddItem(0,14,0,...), mức ngẫu nhiên 5..10, gán map; **đây là vật phẩm trang bị loại 14 tạm theo hoạt động, không phải bằng chứng thưởng áo/vũ khí thường giữ lâu dài**. Không suy mọi AddItem trong script là trang bị phù hợp hảo hữu. |

[CHƯA KIỂM] Danh sách nhiệm vụ thưởng đồ thường, lịch/tính hoạt động của bigboss, xác suất drop chuẩn hóa, bao đồ boss xanh/vàng, PAK thực nạp, loot ownership và khả năng chuyển món thưởng tạm sang hảo hữu. Đã tìm AddItem cho các loại đồ thường 0/1/2/5/7/8/9/10 trong missions Lua rời bằng mẫu số trực tiếp chưa thấy; mẫu dùng biến/helper có thể không khớp. Không khẳng định game không có thưởng nhiệm vụ. Có nền boss để khảo sát tiếp, chưa có catalog loot hoàn chỉnh.

## Kết luận triển khai sau khảo sát

[ĐỀ XUẤT] Với 10 hảo hữu, phần dùng lại được là item data/generator và chuỗi modifier/tính lại có chọn lọc. Phần cần bổ sung: roster ID và bộ đồ mỗi con; context kiểm cấp/sex/bốn điểm của con theo luật không phái; hỗ trợ bonus cơ bản/skill/vũ khí cần thiết; UI chọn con và ô; save có version/capacity; appearance nếu yêu cầu. Không chỉ nhân 25 ô cũ hoặc đổi m_TongBanNum thành count. Các giới hạn nTaskCount, handler player-only và needtongban cần được giải quyết trước task triển khai.

## Kiểm chứng, lỗi thao tác và Git

- Đã đối chiếu trực tiếp các đoạn source/data có số dòng và phân biệt code/comment. Không chạy build, test game, compiler, DB hay exe theo phạm vi khảo sát. Kiểm Markdown/diff thực hiện khi bàn giao, không gọi đó là test runtime.
- `rg : The term 'rg' is not recognized ...`: một lần thử, chuyển sang Select-String/ReadAllLines PowerShell, không cài công cụ hay tạo parser/script phụ. Đọc task lần đầu mặc định lỗi dấu, đọc UTF-8 lại; đầu ra gộp dài bị rút gọn, thu hẹp đọc các đoạn cần thiết.
- Các đường đoán `Core/Src/KMagicAttrib.cpp`, `Core/Src/GameDataDef.h`, `script/lib/award.lua` không tồn tại; không thử lặp, chuyển đúng KNpcAttribModify.cpp, header client đã xác nhận và script missions thực có. Không dùng lỗi thiếu file để kết luận thiếu chức năng. Một lệnh Select-String dù có ErrorAction vẫn hiện lỗi đường thiếu; không có sửa nguồn.
- Chưa xác minh runtime/ABI/header biên dịch; các kết luận bất lợi đều là rủi ro source, không phải lỗi đã tái hiện.

Trạng thái cuối: **PARTIAL — khảo sát DONE, commit BLOCKED. BỊ CHẶN – CHƯA PUSH.** Đã xem diff toàn bộ hai file một lần; kiểm `git diff --no-index --check` báo trailing whitespace ở dòng cuối do CR ghép riêng, đã chuẩn hóa LF và kiểm lại không còn lỗi. Mã thoát 1 của `git diff --no-index` khi có khác biệt là bình thường; không nhận đó là build/test.

Một lần stage đúng hai file thất bại:

~~~text
git add -- JX1_OPS/REPORTS/A-12-hao-huu-mac-do.md JX1_OPS/TASKS/A-12.md
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-12/index.lock': Permission denied
~~~

Git metadata ngoài writable root; không nâng quyền, đổi ACL/config/credential hoặc dùng index thay thế. Chưa stage được, commit chưa chạy, **chưa có commit SHA/link**. Không push vì chưa có commit và người dùng chỉ yêu cầu commit. Giữ hai file local; PM tiếp tục tại worktree/nhánh đã xác nhận bằng phiên có quyền ghi metadata:

~~~text
git -C "D:\JX-wt\A-12" add -- JX1_OPS/REPORTS/A-12-hao-huu-mac-do.md JX1_OPS/TASKS/A-12.md
git -C "D:\JX-wt\A-12" commit -m "A-12 Khao sat hao huu mac do va luu trang bi 10 slot"
~~~
