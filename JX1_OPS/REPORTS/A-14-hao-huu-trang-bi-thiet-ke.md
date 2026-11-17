TÓM TẮT 1: [NGUỒN]/[ĐỀ XUẤT] Bốn handler thuộc tính đang chỉ nhận player; thêm context và phép quy đổi riêng cho kind_partner, không gọi ChangeCur* của chủ (S/KNpcAttribModify.cpp:1307–1315,1362–1369,2158–2165,2194–2201; mục 1).
TÓM TẮT 2: [NGUỒN]/[ĐỀ XUẤT] CanTonEquip/EnoughAttrib hiện dùng con đang gọi và chỉ số chủ; thay bằng CanCompanionEquip kiểm ID, cấp, giới tính, bốn điểm riêng của con, không chia đồ theo phái (S/KItemList.cpp:1095–1139,1229–1279; mục 2).
TÓM TẮT 3: [NGUỒN]/[ĐỀ XUẤT] Lưu một bản item với CompanionId + EquipSlot trong hợp đồng save có version cho 10 bộ; không nhồi đồ vào task BYTE hoặc dùng DWID phiên làm ID bền (S/KPlayerDBFuns.cpp:1112–1119,1644–1653,1852–1863; L/S3DBInterface.h:193–220; mục 3).
TÓM TẮT 4: [NGUỒN]/[ĐỀ XUẤT] Move-item chỉ có tọa độ; NPC_SYNC chưa mang áo/mũ/vũ khí. Cần UI chọn con, request/ack có revision và đồng bộ appearance riêng tới người quan sát (H/KProtocol.h:304–323,1195–1221; C/gamecore/KProtocolProcess.cpp:1399–1420; mục 4).
TÓM TẮT 5: [CHƯA KIỂM] Chưa triển khai, build, chạy exe, thử DB/network/ngoại hình hoặc chốt hệ số cân bằng; mỗi mục dưới đây có rủi ro và tiêu chí kiểm cho task triển khai sau (mục 1–4, bàn giao).

# A-14 — Thiết kế trang bị cho Hảo hữu (tĩnh)

Ngày: 17/11/2026. Trạng thái: **DONE — khảo sát và đề xuất thiết kế**, không phải tính năng đã triển khai. Đã đọc `JX1_OPS/REPORTS/A-12-hao-huu-mac-do.md` trước task A-14. Chỉ khảo sát source tại `D:\JX-source`; không sửa source, không build, không chạy exe, không kết nối VM/server/DB. Không đưa dữ liệu dự án lên dịch vụ ngoài.

## Phạm vi và cách dẫn chứng

| Tiền tố | Gốc đường dẫn chỉ đọc |
| --- | --- |
| S/ | `D:/JX-source/server/jxOnline/gameserver/Sources/Core/Src/` |
| H/ | `D:/JX-source/server/jxOnline/gameserver/Headers/` |
| L/ | `D:/JX-source/server/jxOnline/gameserver/Lib/` |
| C/ | `D:/JX-source/client/Classes/` |

[NGUỒN] Số dòng vật lý tính từ 1, lấy trực tiếp ở source hiện tại; không sao chép số dòng canonical cũ của A-12. Ví dụ `UpdataNpcCurData` hiện ở S/KNpc.cpp:7372, `ReCalcNpcEquip` ở :7556; `m_nSex` ở S/KNpc.h:747. Markdown đọc UTF-8; source legacy đọc CP936 khi trích đoạn, dựa symbol/code thực thi, không suy nghĩa từ chuỗi lỗi dấu. Không khẳng định source khớp binary hay tài nguyên đang triển khai.

[ĐỀ XUẤT] Các tên `CompanionId`, `CanCompanionEquip`, các record/gói tin mới dưới đây là hợp đồng thiết kế, **chưa tồn tại theo thiết kế này trong source đã kiểm**. Mục tiêu là 10 hảo hữu có 10 bộ độc lập; số hảo hữu đang hiện trên bản đồ là vấn đề khác. Dùng trang bị thường người chơi tự kiếm, điều kiện theo chính hảo hữu, không tạo bộ đồ chia theo phái. Chưa khảo sát lại loot/data vì A-14 chỉ yêu cầu bốn đường thiết kế.

## 1. Thuộc tính cơ bản và tác dụng chiến đấu

### Hiện trạng có bằng chứng

- [NGUỒN] Partner được tạo với `kind_partner` (S/KNpcSet.cpp:858–893). `StrengthV`, `DexterityV`, `VitalityV`, `EnergyV` trả về khi kind khác player, rồi gọi `Player[pNpc->m_nPlayerIdx].ChangeCur*` (S/KNpcAttribModify.cpp:1307–1315,1362–1369,2158–2165,2194–2201). Bỏ guard mà giữ lời gọi này có thể sửa chỉ số player thay vì con.
- [NGUỒN] Bốn điểm base/current thuộc KPlayer (S/KPlayer.h:369–380). KNpc có cấp/giới tính (S/KNpc.h:351,747); tìm các tên bốn điểm tương ứng trong KNpc.h chưa thấy bộ như KPlayer. [CHƯA KIỂM] Không khẳng định mọi cấu trúc phụ trong toàn repo đều thiếu chúng.
- [NGUỒN] Luồng mặc gọi `ApplyMagicAttribToNPC`, rồi `UpdataNpcCurData` (S/KItemList.cpp:1451–1481). Reset current từ template tại S/KNpc.cpp:7404–7419, gọi `ReCalcNpcEquip` tại :7552; hàm sau chọn một nhóm trong 53–77 rồi `UpMagicAttrib` lấy item của chủ (:7556–7644), áp lại vào NPC (:7675–7681). Đây chưa phải lookup theo ID hảo hữu.
- [NGUỒN] Player đổi Vitality thì cộng max life/stamina, đổi Energy thì cộng max mana (S/KPlayer.cpp:2772–2796). Damage vật lý thực thi lấy damage vũ khí, cộng Strength cho vũ khí gần hoặc Dexterity cho vũ khí xa (:2859–2876). Khối Energy gây damage ở :2814–2857 là comment; không coi đó là công thức đang chạy. `AllSkillV` cũng chặn NPC không phải player (S/KNpcAttribModify.cpp:632–636).

### Thiết kế đề nghị

[ĐỀ XUẤT] Thêm `CompanionAttributeContext` theo `(OwnerRoleId, CompanionId)` gồm `Base[STR,DEX,VIT,ENG]`, `EquipBonus[4]`, `BuffBonus[4]`, `Current[4]`, `Level`, `Sex`, `GrowthProfileVersion`. Base là điểm bền từ tăng trưởng/phân bổ đã xác thực; current là kết quả suy ra, không lưu lại thành base. KNpc active giữ liên kết tới context đúng con; không dùng `m_nPlayerIdx` như một KPlayer của con.

[ĐỀ XUẤT] Nhánh xử lý partner chỉ nhận các modifier đã hỗ trợ rõ ràng. Bốn handler cộng vào scratch của context partner; nhánh player giữ hành vi cũ. Không mở mọi handler player-only cho partner. Thuộc tính +skill chưa hỗ trợ phải hiển thị rõ “chưa áp dụng cho Hảo hữu” trong thông tin món; cần task riêng nếu muốn mở, không báo đã cộng.

| Điểm | Tác dụng đề nghị trong profile của hảo hữu |
| --- | --- |
| STR — sức mạnh | Tăng damage vật lý của đòn/skill dùng vũ khí gần theo hệ số profile. |
| DEX — thân pháp | Tăng attack rating và phòng thủ/né; thêm damage cho vũ khí xa theo profile. |
| VIT — sinh khí | Tăng max life và max stamina. |
| ENG — nội công | Tăng max mana; tăng thành phần damage skill nội công được profile cho phép, cần nối tới phép tính damage thực tế. |

[ĐỀ XUẤT] Công thức xác định, không tự chọn hệ số cân bằng: `Current = clamp(Base + EquipBonus + BuffBonus)`; `Combat = TemplateCombat + [F_profile(Current) - F_profile(Base)] + DirectItemCombat + DirectBuffCombat`. Hiệu `F(Current)-F(Base)` tránh cộng lần nữa phần base đã nằm trong template; khi thiết kế lại template phải ghi rõ baseline và version. Damage trắng vũ khí phải lấy đúng bộ của con và nối vào damage min/max một lần, không chỉ cộng magic damage. Không dùng chỉ số hay phái của chủ làm hệ số.

[ĐỀ XUẤT] `RebuildCompanionStats(owner, id)` thực hiện một lượt: lấy snapshot bộ đồ → reset scratch → gom bốn điểm và modifier trực tiếp → quy đổi điểm sang combat → áp trực tiếp/% theo thứ tự cố định → phục hồi trạng thái buff/passive còn hiệu lực đúng một lần → clamp current life/mana theo max mới. Mặc đồ không tự hồi đầy; giữ số hiện tại và cắt xuống khi vượt max. Không “áp trước rồi reset rồi áp lại” như đường cũ. Gọi cùng phép rebuild khi mặc/tháo, đổi cấp, spawn, phục hồi buff hoặc load xong; despawn giữ dữ liệu bền, bỏ cache phiên.

### Rủi ro và cách kiểm

| Rủi ro | Cách kiểm dự kiến — tất cả [CHƯA KIỂM], chưa chạy trong A-14 |
| --- | --- |
| Cộng nhầm chủ, con khác hoặc cộng lặp qua reset | Hai con cùng template có đồ khác nhau; chụp số chủ/con trước–sau. Rebuild lặp phải cho cùng kết quả; mặc rồi tháo trả về baseline khi không có buff thay đổi. |
| Template đã chứa điểm base, bonus/% tính hai lần | Fixture base cố định, riêng từng +STR/+DEX/+VIT/+ENG và món chỉ tăng combat trực tiếp; so công thức độc lập với kết quả. Đổi thứ tự mặc không đổi tổng. |
| Điểm trên panel tăng nhưng damage thật không tăng | Đánh mục tiêu kiểm soát bằng skill gần/xa/nội công tương ứng; kiểm cả damage trắng và magic, làm tròn, hệ số 0, min/max, overflow. |
| Đổi đồ hồi máu vô hạn hoặc mất buff/passive | Mặc/tháo khi thiếu máu, giảm max, đang có buff; số hiện tại không tăng do đổi đồ và buff còn thời hạn không mất/nhân đôi. |

[CHƯA KIỂM] Hệ số tăng trưởng/cân bằng, baseline template của từng con, cách mọi skill dùng Energy, toàn bộ handler/buff và công thức damage cuối. Đây là điểm cần chốt trước triển khai combat, không phải lỗi runtime đã tái hiện.

## 2. Kiểm điều kiện mặc bằng chính hảo hữu

### Hiện trạng có bằng chứng

[NGUỒN] `CanTonEquip` chọn một con qua `m_TongBanNum`, đòi đã triệu hồi và bắt `magic_item_needtongban`; nhánh `Fit` bị comment (S/KItemList.cpp:1095–1139). `EnoughAttrib` lấy STR/DEX/VIT/ENG của chủ, cấp/sex từ NPC chủ (:1229–1279). Nhánh đồ hoạt động có thể bỏ qua requirement (:1215–1223), còn `needtongban` đối chiếu vị trí số (:1341–1354). Không dùng nguyên hàm này cho đồ thường của 10 con.

### Thiết kế đề nghị

[ĐỀ XUẤT] Hàm thuần `CanCompanionEquip(owner, CompanionId, ItemRef, EquipSlot, ExpectedRevision) -> {allowed, reason, actual, required}`; server là nơi quyết định. Không truyền mỗi NPC index, không tự tìm con qua scalar đang triệu hồi. Có thể thay đồ cho con đã sở hữu nhưng chưa spawn; chỉ rebuild NPC ngay khi nó active.

[ĐỀ XUẤT] Thứ tự kiểm, mọi thất bại giữ nguyên toàn bộ đồ:

1. Xác thực phiên/chủ; ID thuộc roster của chủ, ô roster đã mở, slot trang bị trong schema, revision còn đúng.
2. Resolve item từ kho server của chủ; kiểm đúng bản vật phẩm, vị trí nguồn hiện tại, không giao dịch/khóa thao tác/đang mặc cho chủ hay con khác; không nhận thuộc tính do client gửi.
3. Kiểm loại vật phẩm và bảng `detailType -> allowed EquipSlot`, durability/hạn dùng/binding/giới hạn bản đồ theo quy tắc item hiện có đã rà soát; không mang ngoại lệ bỏ qua mọi requirement của đồ hoạt động sang nhánh mới.
4. So sex, level và STR/DEX/VIT/ENG của **context con**. Dùng `RequirementStats = Base` (đã gồm tăng trưởng/phân bổ bền), không tính đồ hoặc buff tạm. Đây là chính sách đề nghị chặt hơn player: không tự đáp ứng điều kiện, không tạo vòng hai món hỗ trợ nhau; UI ghi rõ điểm xét mặc khác điểm chiến đấu hiện tại.
5. Không xét môn phái chủ/con cho danh mục đồ thường được hỗ trợ. Record mang requirement môn phái hoặc loại requirement chưa hỗ trợ phải trả `UNSUPPORTED_REQUIREMENT`, không âm thầm bỏ qua. `needtongban` chỉ thuộc nhánh legacy, không bắt đồ thường mới mang mã đó. Danh mục hỗ trợ không chia theo phái; ngũ hành nếu có hiệu ứng là cơ chế bonus riêng, không tự biến thành khóa mặc theo phái.
6. Lập trạng thái sau swap/unequip; kiểm chỗ cho món cũ theo kích thước item. Nếu kho đầy trả `NO_SPACE`, không thả đất/xóa. Commit một lần cả vị trí lẫn bộ đồ, tăng revision, rebuild và trả snapshot kết quả.

[ĐỀ XUẤT] Mã lỗi tối thiểu: `NOT_OWNER`, `COMPANION_LOCKED`, `STALE_REVISION`, `ITEM_MOVED`, `ITEM_BUSY`, `WRONG_SLOT`, `SEX_MISMATCH`, `LEVEL_TOO_LOW`, `STAT_TOO_LOW`, `UNSUPPORTED_REQUIREMENT`, `NO_SPACE`. Client chỉ dự báo bằng snapshot, server vẫn kiểm lại. Nếu điểm bền/cấp thay đổi làm đồ mất điều kiện: đánh dấu ô bất hoạt, giữ nguyên bản item và cho tháo an toàn; không xóa vật phẩm hoặc áp bonus sai. Chính sách này tránh buộc trả đồ vào kho đang đầy.

### Rủi ro và cách kiểm

| Rủi ro | Cách kiểm dự kiến — [CHƯA KIỂM] |
| --- | --- |
| Chủ đủ nhưng con thiếu; sai giới tính | Bảng ca đúng ngưỡng, thiếu 1 điểm/cấp, sex khác nhau; đổi chỉ số chủ không thay kết quả cho cùng con. Kiểm template sex chưa được khởi tạo thì từ chối theo trạng thái dữ liệu không hợp lệ. |
| Món tự nâng điểm để được mặc; buff hết hạn | Ca món +STR yêu cầu STR lớn hơn điểm bền và cặp món tạo vòng phải bị từ chối; buff không đổi điều kiện mặc. |
| Giả ID/slot/item và race với trade | Gửi ID người khác, slot ngoài miền, item đã chuyển, hai request cùng revision; chỉ tối đa một thao tác hợp lệ, tổng item giữ nguyên. |
| Swap thất bại làm mất đồ | Kho đầy, món cũ kích thước khác, item bị khóa/hết hạn: lỗi không đổi item location, revision, stats hay appearance. |

[CHƯA KIỂM] Toàn bộ chính sách binding/đồ tạm/requirement đặc biệt và sex thực của từng template. Không diễn giải “chưa kiểm” thành cho phép bỏ qua.

## 3. Lưu đồ có ID hảo hữu cho 10 bộ

### Hiện trạng có bằng chứng

[NGUỒN] `TonEquip` ghi `pos_dazao`, X=vị trí, Y=0 (S/KItemList.cpp:1417–1421). 25 ô legacy là 5 nhóm × 5, không phải 10 bộ (S/KNpc.cpp:7562–7633). Save duyệt item list và ghi tọa độ, `iequipcode` đang bằng 0 (S/KPlayerDBFuns.cpp:1633–1653); load dựng item rồi Add (:1112–1119). `TDBItemData` có `iid`, tọa độ và dữ liệu item nhưng chưa có trường CompanionId/EquipSlot (L/S3DBInterface.h:213–280). `GetID()` trả `m_dwID` dùng trao đổi client/server (S/KItem.h:222–236); chưa chứng minh đó là khóa bền qua login.

[NGUỒN] Role có `dwVersion`, offsets, `nTaskCount` BYTE và `nItemCount` short (L/S3DBInterface.h:184–202). Task khác 0 đều tăng count rồi gán về BYTE (S/KPlayerDBFuns.cpp:1844–1863); buffer player là 128 KiB (S/KPlayer.h:284). Include thay đổi theo `_STANDALONE` (S/KPlayerDBFuns.cpp:8–15). Không nhét mapping lớn vào task chỉ vì còn byte trong buffer.

### Hợp đồng lưu đề nghị

[ĐỀ XUẤT] Chọn snapshot role có version mới, chứa roster và item-location trong **cùng một đơn vị lưu nguyên tử**. Không lưu một file phụ riêng hay hai bản payload vật phẩm. Hợp đồng logic sau là mới, chưa phải DDL/ABI đã triển khai:

| Record | Khóa/trường bền và invariant |
| --- | --- |
| RosterHeader | `SchemaVersion`, `RosterRevision`, `CompanionCount <= 10`, độ dài từng block; đủ kiểm giới hạn trước khi đọc/ghi. |
| CompanionRecord | `(OwnerRoleId, CompanionId)` duy nhất; `RosterIndex` 0..9 là vị trí UI có thể đổi; template, sex, level, điểm bền và growth version. CompanionId do server cấp, không tái dùng khi xóa con. |
| ItemRecordV2 | `ItemUid` bền do server cấp + payload item hiện có một lần; `LocationKind = Inventory/PlayerEquip/CompanionEquip/...`. Nếu CompanionEquip: `CompanionId`, `EquipSlot`; nếu nơi khác: không mang mapping con. |
| Cache runtime | `CompanionId -> NpcNetId + SpawnGeneration`, `ItemUid -> item index/DWID` của phiên; không persist cache này. |

[ĐỀ XUẤT] Các ràng buộc: item thuộc đúng owner; duy nhất `(owner, companion, equipSlot)`; một ItemUid chỉ ở một location; CompanionId tham chiếu roster hiện hữu; một con có thể tồn tại khi chưa có NPC active. Không dùng template ID làm CompanionId vì hai con có thể cùng template. Không đổi `iid`, `iequipcode`, `ix/iy` hay task value thành khóa mới nếu chưa đổi rõ hợp đồng mọi bên đọc/ghi.

[ĐỀ XUẤT] Schema slot độc lập roster: mặc định thiết kế pha đầu là 10 ô đồ thường `head, body, belt, weapon, foot, cuff, amulet, ring1, ring2, pendant`, tham khảo enum C/gamecore/GameDataDef.h:213–222. Đây là **đề xuất**, không phải ánh xạ 5 ô legacy đã xác nhận. Chưa đưa horse/mask/pifeng hay ô đặc biệt vào pha đầu; mỗi loại cần luật riêng. Với lựa chọn này 10 bộ tối đa 100 item; nếu chủ dự án chốt S ô khác thì là `10 × S`, không hard-code 50 từ A-12. Phải kiểm `MAX_PLAYER_ITEM` và mọi chỗ duyệt/tính capacity; macro client phụ thuộc nhiều thành phần (C/gamecore/GameDataDef.h:108), chưa xác minh giới hạn thực cho 100 item.

[ĐỀ XUẤT] Serialize từng trường bằng độ rộng xác định; kiểm tổng độ dài bằng phép cộng chống overflow trước ghi, kiểm số item/task/các offset và capacity toàn role. Không tự nới BYTE nTaskCount trong header cũ. Chi phí tăng = metadata roster + UID/location mới của item + phần payload item tăng thực sự; nếu đồ đã nằm trong inventory thì chuyển location không tạo thêm bản payload. Chưa đưa số byte chính xác khi packing/ABI và consumer chưa kiểm.

[ĐỀ XUẤT] Thứ tự load: xác thực version/length → đọc roster → dựng tất cả item một lần → resolve mapping và kiểm invariant → tính stats offline → spawn nếu cần rồi gắn cache phiên → gửi snapshot owner/appearance. Không gọi TonEquip cũ trong lúc Add khi roster/NPC chưa sẵn sàng. Bản item trùng UID, mapping mồ côi hoặc dữ liệu không hợp lệ phải giữ trong vùng cách ly có log đã lọc và chặn lưu phá hủy; không bỏ record rồi lưu đè bản duy nhất.

[ĐỀ XUẤT] Save/swap chạy tuần tự theo owner, dùng snapshot/revision nhất quán. ACK thành công chỉ sau khi cơ chế commit bền xác nhận snapshot; lỗi lưu giữ trạng thái trước và trả lỗi. Nếu hạ tầng hiện tại chỉ lưu định kỳ/không có xác nhận commit nguyên tử thì đây là **điều kiện chặn triển khai** cần bổ sung, không được hứa chống mất/nhân đồ sau crash chỉ bằng mutex RAM. Khi chuyển GS phải chuyển cùng revision, roster và item, ngăn hai GS đồng thời ghi bản cũ.

[ĐỀ XUẤT] Migration một lần có marker/version và bản sao dữ liệu nguồn: inventory/player-equip giữ nguyên; 25 ô legacy chỉ gắn vào con khi có quan hệ xác định duy nhất, không chọn bừa con đầu tiên/cùng ngũ hành. Trường hợp mơ hồ để chờ đối chiếu, giữ item và chặn ghi mất. Consumer cũ phải từ chối version mới trước khi thay đổi dữ liệu; rollback cần binary tương thích hoặc phục hồi snapshot cũ theo quy trình riêng, không hạ version tại chỗ. DB/gateway/Goddess phải cùng hỗ trợ hợp đồng mới trước khi bật tính năng.

### Rủi ro và cách kiểm

| Rủi ro | Cách kiểm dự kiến — [CHƯA KIỂM] |
| --- | --- |
| Đồ lẫn giữa 10 con hoặc ID phiên thay đổi | 10 con, có hai con cùng template, mỗi bộ khác nhau; save/load, reorder roster, despawn/spawn và login mới vẫn đúng ItemUid/CompanionId. |
| Tràn count/buffer/header không đồng nhất | Fixture role gần đầy item/task, cả 100 ô, giá trị biên và offset hỏng; reject an toàn trước ghi, không truncate. Kiểm ABI từng producer/consumer khi được phép build sau này. |
| Crash/đồng thời tạo hai bản đồ | Chèn lỗi trước/sau commit, mất ACK, retry request, reconnect/chuyển GS; chỉ phục hồi toàn snapshot trước hoặc sau, tổng ItemUid duy nhất giữ nguyên. |
| Migration xóa/đổi nhầm vật phẩm | Dữ liệu cũ không có đồ, 25 ô, mapping mơ hồ/trùng; chạy lại migration không tạo thêm item. Consumer cũ đọc version mới phải từ chối an toàn. |

[CHƯA KIỂM] Schema DB thật, tính bền của `iid`, khóa item hiện có, packing, gateway/Goddess, giới hạn inventory và hỗ trợ atomic save. Thiết kế không tuyên bố có sẵn bảng/transaction đó; cần khảo sát consumer trước khi viết migration.

## 4. UI, gói tin mặc/tháo và ngoại hình

### Đường hiện có đã nối

| Đoạn | Bằng chứng |
| --- | --- |
| UI gửi di chuyển | [NGUỒN] KuiItem gọi `SendClientCmdMoveItem` (C/gameui/KuiItem.cpp:670,688); hàm đóng `PLAYER_MOVE_ITEM_COMMAND` rồi gửi (C/gamecore/KProtocol.cpp:738–764). |
| Server nhận | [NGUỒN] Dispatch `c2s_playermoveitem` tới `PlayerMoveItem` (S/KProtocolProcess.cpp:237,5724–5733); `ServerMoveItem` giải tọa độ và gọi ExchangeItem (S/KPlayer.cpp:6018–6046). Nhánh ô 53–77 gọi CanTonEquip/TonEquip và gửi sync (S/KItemList.cpp:7261–7290). |
| Owner nhận | [NGUỒN] `s2cMoveItem` giải tọa độ rồi gọi ExchangeItem ở client (C/gamecore/KProtocolProcess.cpp:1399–1420). Command/sync chỉ có vị trí và cờ, không có ID hảo hữu/revision (H/KProtocol.h:1195–1221; C/gamecore/KProtocol.h:1140–1166). |
| Ngoại hình | [NGUỒN] NPC_SYNC không có HelmType/ArmorType/WeaponType (H/KProtocol.h:304–323; C/gamecore/KProtocol.h:293–312). Server gửi ID/template/level/tên tại S/KNpc.cpp:7957–8009; nhánh player có ArmorType/HelmType/WeaponType (:8027–8028,8088). |
| Client renderer | [NGUỒN] SyncNpc tìm/tạo NPC từ ID/template (C/gamecore/KProtocolProcess.cpp:2159–2178). Renderer gọi `ChangeFeature` với các trường ngoại hình (C/gamecore/KNpc.cpp:723–726); các lệnh SetArmor/SetHelm/SetWeapon ngay dưới :727–733 nằm trong comment. TonEquip client chưa gán các trường appearance (:1051–1141 của C/gamecore/KItemList.cpp). Không coi comment “đổi ngoại hình” là xử lý thật. |

[CHƯA KIỂM] Panel trang bị hảo hữu đang được mở trong bản game nào, resource UI/PAK, mọi packet mở rộng và khả năng từng model hảo hữu mặc đồ human. A-12 chưa chứng minh panel; A-14 xác nhận đường item chung, không kết luận client hoàn toàn không có panel khác.

### Giao diện và hợp đồng mới đề nghị

[ĐỀ XUẤT] Panel danh sách 10 con dùng CompanionId bền, hiển thị ô chưa mở, con active, cấp/sex/điểm xét mặc và điểm chiến đấu. Chọn con → xem bộ đồ từ snapshot server → kéo món thường vào slot hoặc chọn tháo về inventory. Preview nêu thiếu cấp/điểm/sex và bonus chưa hỗ trợ. Trong khi chờ ACK khóa thao tác liên quan; thay lựa chọn không đổi đích request đã gửi. Lỗi/timeout lấy lại snapshot rồi mở khóa, không tự gửi một thao tác mới với requestId khác để thử lại mù.

| Gói logic mới — tất cả [ĐỀ XUẤT] | Nội dung và xử lý |
| --- | --- |
| `C2S_COMPANION_EQUIP_OP` | `version, length, requestId, CompanionId, op(equip/unequip/swap), EquipSlot, itemHandle + generation, sourceLocation, destinationLocation, expectedRosterRevision, expectedInventoryRevision`. Owner lấy từ phiên xác thực; không nhận combat/sex/level do client khai. ItemHandle ánh xạ server tới ItemUid, không là quyền sở hữu. |
| `S2C_COMPANION_EQUIP_RESULT` | `requestId, resultCode, revisions mới`, bộ delta item location + ô bị đổi + stats/appearance revision; thất bại trả lý do và revision hiện tại, không áp nửa delta. Request lặp cùng ID/nội dung trả cùng kết quả; cùng ID khác nội dung bị từ chối. |
| `S2C_COMPANION_SNAPSHOT` | `version, length, rosterRevision`, 0..10 con và bộ slot/stat, item handle của owner; dùng khi mở panel, login, reconnect hoặc revision lệch. Chia chunk có snapshotId nếu vượt giới hạn packet, chỉ apply sau khi đủ snapshot. |
| `S2C_COMPANION_APPEARANCE` | `version, length, NpcNetId, SpawnGeneration, appearanceRevision, model/sex, helmRes, armorRes, weaponRes` cùng trường hiệu ứng thực sự cần. Gửi người quan sát vùng và người vừa thấy NPC; không gửi nguyên inventory/UID bền riêng của chủ cho tất cả. |

[ĐỀ XUẤT] Cấp opcode bằng rà soát registry và capability/version handshake của hai bên; không chọn số trống theo đoán hoặc nhét CompanionId vào `m_IsComp`, X/Y của gói cũ. Serialize wire với độ rộng/endianness/length rõ; kiểm count, enum, length và giới hạn trước parse. Giữ protocol legacy cho đường cũ; client không hỗ trợ không được gửi thao tác mới, không tự mở tính năng bằng sửa packet-size một phía.

[ĐỀ XUẤT] Server map đồ → resource bằng quy tắc item/giới tính/model, tính appearance cùng revision commit đồ. Tháo trả default từ template/profile, không để sprite của món cũ. Broadcast bản ngoại hình đầy đủ khi spawn/đổi vùng/viewer mới; delta sau mỗi đổi đồ. Client chỉ gán các trường appearance đã xác thực rồi làm mới `ChangeFeature`; không biến partner thành kind_player hoặc gọi nhánh sync player để được mặc đồ. Gói tới trước spawn: cache có giới hạn theo `(NpcNetId, SpawnGeneration)`, áp khi spawn đúng generation; bỏ revision cũ, xóa cache lúc despawn để tránh gán vào NPC tái sử dụng ID.

[ĐỀ XUẤT] Đồ thường vẫn tăng chỉ số dù model chưa hỗ trợ biến hình; trong trường hợp resource chưa có, dùng appearance mặc định có thông báo giới hạn rõ, không cam kết mọi vũ khí đã có animation. Kiểm khả năng model và sprite nam/nữ trước khi chốt danh mục appearance hỗ trợ. Thay appearance không đổi template chiến đấu, CompanionId hay ownership.

### Rủi ro và cách kiểm

| Rủi ro | Cách kiểm dự kiến — [CHƯA KIỂM] |
| --- | --- |
| UI đổi con giữa request, ACK lặp/đảo thứ tự | Chọn A, gửi mặc, chuyển B; ACK chỉ cập nhật A. Ca ACK mất/lặp, revision cũ phải resync, không chuyển đồ hai lần. |
| Packet sai ABI/giả mạo, client cũ làm hỏng state | Fixture bytes hai phía, length thiếu/thừa/count quá lớn/slot sai; từ chối trước parse sâu. Client cũ không hiểu capability phải bị chặn tính năng an toàn. |
| Owner thấy đổi nhưng người khác không thấy | Hai client ở cùng/khác vùng, viewer vào sau, spawn lại, đổi map, reconnect: ngoại hình cuối cùng cùng revision với server. Stats vẫn do server quyết định. |
| Thiếu sprite hoặc animation; tái dùng NetId | Ma trận model/sex × mũ/áo/vũ khí × đứng/chạy/đánh/cast; tháo về mặc định. Gói cũ từ NPC đã despawn không thay NPC mới cùng NetId. |

[CHƯA KIỂM] Số opcode, size/packing packet thực, handshake, queue/cache, renderer/resource của từng con và khả năng client tương thích. Chưa chạy network/viewer hoặc kiểm hình trực tiếp.

## Thứ tự triển khai và điều kiện nghiệm thu sau khảo sát

[ĐỀ XUẤT] Triển khai theo phụ thuộc: (1) chốt schema ID/slot/điểm và consumer save version mới; (2) context thuộc tính, hàm kiểm và phép rebuild độc lập; (3) thao tác item nguyên tử + round-trip/migration; (4) protocol/UI owner rồi appearance viewer. Chỉ bật khi các ca kiểm tương ứng đạt; không coi sửa riêng handler StrengthV hay thêm panel là hoàn tất tính năng. Các phần này là kế hoạch kỹ thuật cho task khác, không có mã được viết trong A-14.

## Kiểm chứng và bàn giao

- [NGUỒN] Trước khi ghi kiểm Git một lần: branch `task/A-14-hao-huu-trang-bi`; có sẵn `?? JX1_OPS/TASKS/A-14.md`. Báo cáo A-14 chưa tồn tại. Giữ nguyên task ngoài mục Kết quả cuối file.
- [NGUỒN] Chỉ tạo báo cáo này và thêm mục Kết quả vào task; không tạo script/parser phụ, không sửa A-12/BAI_HOC/source/config. Đã đối chiếu trực tiếp các symbol, struct và đoạn code/comment dẫn ở bốn mục. Đã xem diff đầy đủ hai file một lần; `git diff --no-index --check` không báo lỗi, kiểm cấu trúc đạt 5 dòng tóm tắt và 4 mục chính. Exit 1 của lệnh xem diff là có khác biệt, không phải test thất bại; không gọi kiểm Markdown là test game.
- [NGUỒN] Lỗi công cụ: `rg : The term 'rg' is not recognized ...` một lần, chuyển sang `Select-String`/`ReadAllLines`. Đọc A-12 lần đầu mặc định lỗi dấu, đọc lại UTF-8; đầu ra batch dài bị rút gọn, thu hẹp trích đoạn. Dùng khoảng dòng A-12 cho KNpc.cpp thấy lệch, đã tìm lại symbol và dẫn số dòng hiện tại. Không có sửa source do các lỗi này.
- [CHƯA KIỂM] Toàn bộ test/build/runtime/DB/network/PAK nêu trên chưa chạy theo phạm vi tĩnh. Không có bằng chứng source khớp exe đang dùng; không công bố hệ số, size ABI hay đảm bảo atomic save khi chưa kiểm consumer.
- Trạng thái cuối: **DONE** cho toàn bộ bốn mục khảo sát/thiết kế, mỗi mục có rủi ro và cách kiểm. Không có blocker cho việc giao báo cáo; các điểm chưa kiểm là điều kiện của task triển khai sau.
- Commit SHA/link: **không có**. Không stage/commit/push vì lượt này chỉ cho phép ghi hai file được chỉ định và không yêu cầu công bố Git; giữ kết quả local để duyệt.
