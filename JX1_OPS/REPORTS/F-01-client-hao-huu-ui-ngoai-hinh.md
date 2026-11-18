TÓM TẮT 1: [NGUỒN] Có UI chọn thành viên đội người chơi trong KuiTeam, chưa chứng minh panel chọn hảo hữu; dùng mẫu ListView, không dùng TeamOperation làm roster (C/gameui/KuiTeam.cpp:182–216,751–786).
TÓM TẮT 2: [NGUỒN]/[ĐỀ XUẤT] KuiRoleState có ô đồ, tooltip và tháo bằng AutoChangeItem; cần panel/context CompanionId riêng, không lấy GDI_EQUIPMENT của chủ cho con (C/gameui/KuiRoleState.cpp:44–61,2175,2208–2223).
TÓM TẮT 3: [NGUỒN] PLAYER_MOVE_ITEM_COMMAND/SYNC chỉ mang vị trí/cờ; TonEquip tìm một con qua m_TongBanNum, chưa đáp ứng 10 bộ theo ID bền (C/gamecore/KProtocol.h:1140–1166; C/gamecore/KItemList.cpp:1051–1064).
TÓM TẮT 4: [NGUỒN]/[ĐỀ XUẤT] NPC_SYNC thiếu áo/mũ/vũ khí; renderer có ChangeFeature → SetPartInfo → sprite, cần appearance riêng theo NPC phiên và revision (C/gamecore/KProtocol.h:293–312; C/gamecore/KNpcRes.cpp:1703–1726,1792–1799).
TÓM TẮT 5: DONE cho khảo sát tĩnh; đề xuất 5 nhóm việc client, khoảng 10–14 file mới/sửa và 6–10 ngày công sơ bộ; runtime/resource/ABI/build đều [CHƯA KIỂM], không sửa source hoặc chạy game/VM/mạng.

# F-01 — Client: chọn hảo hữu, mặc/tháo và ngoại hình

Ngày: 17/11/2026. Trạng thái **DONE — khảo sát tĩnh**, không phải tính năng đã triển khai. Đã đọc `JX1_OPS/REPORTS/A-12-hao-huu-mac-do.md` và `JX1_OPS/REPORTS/A-14-hao-huu-trang-bi-thiet-ke.md`. Mọi tên gói/API mới dưới đây là **[ĐỀ XUẤT]**, chưa cấp opcode hoặc sửa ABI.

## Phạm vi, đường dẫn và cách kiểm

- Task ghi `REPORTS/A-12...`, `REPORTS/A-14...`; hai file thực có trong `JX1_OPS/REPORTS/`. Task ghi source `D:\Jx1CocoV3\Folder\Client2912-...`; thư mục `D:\Jx1CocoV3\Folder` không tồn tại. Đối chiếu bản C được A-12 dẫn, không tự thay bằng bản `D:\JX-source` của A-14.
- Tiền tố **C/** trong báo cáo này = `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes/`, chỉ đọc. Không khẳng định đây là source của binary đang dùng. Số dòng theo LF vật lý từ 1; source có encoding hỗn hợp, kết luận dựa trên token/symbol và ranh giới comment, không suy từ chữ lỗi dấu.
- Chỉ tìm tên file liên quan trong `gameui`, token `tongban|partner|fumo|GOI_.*(PET|PARTNER)` trong `.cpp/.h` ngay `gameui`, các callback trong `gamescene/KgameWorld.cpp`, rồi đọc các đoạn `gamecore` trực tiếp phục vụ packet/render/item. Tìm token không ra panel không có nghĩa toàn bộ client/resource/bản VN đều không có.
- Git đầu lượt: `## task/F-01`, có sẵn `?? JX1_OPS/TASKS/F-01.md`. Chưa có báo cáo F-01 khi kiểm checkpoint. Giữ task gốc, chỉ thêm `## Kết quả` theo chỉ thị cuối task; không sửa frontmatter dù `vung_file` chỉ liệt kê report.
- Không sửa mã/config; không chạy exe game/server, build/test game, VM, DB hay mạng thật; không tạo parser/script phụ trên đĩa. Python chỉ chạy `python -I`, dùng đọc đoạn source và kiểm đầu ra báo cáo.

## 1. UI chọn con/đội đang có

| Đường có thật | Bằng chứng và ý nghĩa |
| --- | --- |
| Mở đội | C/gamescene/KgameWorld.cpp:1203 gắn `mTeamCallback`; :2506–2518 mở `KuiTeam`, cờ `m_teamPadIsOpen`, node `OBJ_NODE_TEAM` và callback đóng. Có mẫu lifecycle cho cửa sổ hảo hữu. |
| Danh sách chọn | C/gameui/KuiTeam.cpp:182–216 tạo hai `ListView` cho thành viên đội và người chơi gần, gắn listener; :557–566 lấy selected index. Dữ liệu :783–786 là `KUiPlayerItem` từ `TEAM_OI_GD_MEMBER_LIST`; :807 gắn tag bằng NPC index. Đây là đội player, không phải danh sách sở hữu hảo hữu. |
| Thao tác đội | C/gameui/KuiTeam.cpp:426–470 xử lý tạo/mời/kick/bổ nhiệm/rời bằng `TeamOperation`. Không dùng các lệnh này để chọn, gọi hoặc đổi đồ con. |
| HUD đội | C/gameui/KuiTeamInfo.cpp:97–157 tạo ảnh/tên/thanh máu/mana; :195–241 lấy thông tin/member list từ `TeamOperation`. C/gamescene/KgameWorld.cpp:14421–14457 cập nhật panel đội/HUD. Có thể tham khảo hình thức hiển thị con active, không dùng dữ liệu đội cho roster. |

[CHƯA KIỂM] Không tìm thấy token hảo hữu nêu trên trong phạm vi `gameui/*.cpp,*.h`; chưa chứng minh có panel 10 con, chưa rà bản VN, Lua/resource UI hoặc nút được mở ở binary thực. Không tự đồng nhất “hảo hữu” trong task với hệ thống bạn bè xã hội.

[ĐỀ XUẤT] Thêm `KuiCompanion` riêng với danh sách tối đa 10 con, ID bền do server cấp, trạng thái ô khóa/đã sở hữu/đang active; bên phải là cấp, sex, điểm xét mặc, điểm chiến đấu và bộ đồ. Dùng mẫu ListView của KuiTeam nhưng mỗi dòng giữ `CompanionId`; selected index hoặc NPC index chỉ là vị trí tạm. Con chưa spawn vẫn được xem và thay đồ theo hợp đồng A-14. Nếu cần thao tác gọi/thu hồi hoặc đội con active, tách lệnh đó khỏi việc chỉ chọn dòng để xem đồ.

## 2. Màn hình trang bị và đường mặc/tháo

| Thành phần hiện có | File:dòng và giới hạn |
| --- | --- |
| Mở trang bị chủ | C/gamescene/KgameWorld.cpp:2694–2716 tắt touch menu, đặt `BTN_ITME_ZHUANGBEI`, mở `KuiRoleState`, node `OBJ_NODE_STATE`; :2719 trở đi phục hồi khi đóng. Panel mới cần lifecycle tương ứng để không để menu bị khóa sau khi đóng. |
| Ô đồ | C/gameui/KuiRoleState.cpp:44–61 là bảng `CtrlItemMap`: Cap, Cloth, Sash, Weapon, Shoes, Bangle, Necklace, Ring1/2, Pendant và các ô đặc biệt. C/gamecore/GameDataDef.h:211–227 có enum tương ứng. Đây là bộ player; 10 ô đầu theo A-14 chỉ là phương án, không chứng minh partner hỗ trợ toàn bộ. |
| Lấy bộ đang mặc | C/gameui/KuiRoleState.cpp:2208–2223 gọi `GetGameData(GDI_EQUIPMENT, ..., 0)` rồi `UpdateEquip`; :2240–2245 lấy kích thước và image path của item. Không có tham số CompanionId trong lời gọi đã đọc. |
| Màu điều kiện/tooltip | C/gameui/KuiRoleState.cpp:2316–2329 hỏi `GDI_ITEM_IN_ENVIRO_PROP` với `UOC_EQUIPTMENT`; :2526 là callback đóng desc. Điều kiện UI hiện thuộc ngữ cảnh đồ chủ, phải đổi context khi xem con. |
| Tháo bằng nút/kéo | C/gameui/KuiRoleState.cpp:2138–2178 chọn item rồi `AutoChangeItem(m_CurSelItemIndex)`; :2408–2419 kéo ra ngoài cũng gọi AutoChangeItem. Chưa có target con trong hai lời gọi này. |
| Kho và UI item khác | C/gameui/KuiItem.cpp:169–178 đọc đồ mang theo; :497 chuyển vào `room_equipmentex`. C/gameui/KuiItem_New.cpp:425–435 gửi `GOI_USE_ITEM` với item/region và `UOC_ITEM_TAKE_WITH`; :862,1218 dùng kho phụ. Kho phụ không phải 10 bộ của 10 con. |
| Di chuyển item qua wire | C/gameui/KuiItem.cpp:1069–1090 lấy vị trí item và gửi `SendClientCmdMoveItem`; C/gamecore/KProtocol.cpp:655–671 đóng gói tọa độ/cờ và gửi. C/gamecore/KProtocolProcess.cpp:1397–1417 giải sync rồi `ExchangeItem`. |
| Nhánh đồng bạn legacy | C/gamecore/KItemList.cpp:1051–1064 tìm con bằng `Npc[owner].m_TongBanNum`; :1087–1089 ghi `pos_dazao/X=place/Y=0`, :1112–1114 áp thuộc tính và :1140–1141 tính lại. Không thấy gán mũ/áo/vũ khí trong thân hàm này. |

**Đối chiếu A-14:** C/gameui/KuiItem.cpp:670,688 nằm trong khối comment bắt đầu :657; không dùng chúng làm bằng chứng lệnh gửi đang thực thi. Lời gọi :1090 là điểm thực thi đã đọc. Một số số dòng của A-14 thuộc bản `D:\JX-source`, ví dụ `ChangeFeature` được dẫn :723 trong A-14 nhưng ở bản C là :698. Không sửa hai báo cáo nền ngoài phạm vi.

[ĐỀ XUẤT] Mượn cách dựng icon/tooltip/ô đồ, thêm context riêng `(CompanionId, equipSlot, snapshotRevision)`; không nhân bản toàn bộ KuiRoleState và không đưa bộ con vào `GDI_EQUIPMENT` của chủ. UI mặc/tháo gửi operation riêng với đích đã chụp lúc bấm. Đổi dòng đang chọn khi chờ ACK chỉ đổi màn xem, không đổi đích request cũ. Khóa các thao tác liên quan tới item/con đang pending, áp kết quả nguyên khối; lỗi hoặc timeout lấy lại snapshot. Tooltip hiển thị điều kiện của con và bonus chưa hỗ trợ; server vẫn quyết định hợp lệ, slot trống và chỗ trả đồ.

## 3. Đường ngoại hình NPC khác và điểm nối

Chuỗi source đã xác định, không phải bằng chứng chạy thực:

`NPC_SYNC → KProtocolProcess::SyncNpc → SearchID / AddServerNpcA → KNpc state/template → ChangeFeature → SetPartInfo → sprite parts → KNpc::Paint → KNpcRes::Draw`.

| Mắt xích | Bằng chứng |
| --- | --- |
| Đăng ký nhận | C/gamecore/KProtocolProcess.cpp:56 gắn `s2c_syncnpc` tới `SyncNpc`; :102 gắn move-item. Đây là điểm đăng ký handler mới, không đổi handler player để dùng chung cưỡng ép. |
| Spawn/cập nhật NPC | C/gamecore/KProtocolProcess.cpp:2157–2174 tìm ID hoặc tạo bằng template/kind; :2191–2192 lấy template và cấp. C/gamecore/KProtocol.h:293–312 có ID/template/kind/tên/trạng thái, không có HelmType/ArmorType/WeaponType. |
| Đối chiếu player khác | C/gamecore/KProtocolProcess.cpp:2937–2953 nhận `PLAYER_SYNC`, gán áo/mũ/vũ khí và **gán kind_player**. Vì vậy không gọi SyncPlayer để đổi hình partner. |
| Đổi feature theo state | C/gamecore/KNpc.cpp:695–705 gọi `ChangeFeature` với các trường ngoại hình; `SetArmor/SetHelm/SetWeapon` ngay dưới nằm trong comment. :10575–10615 `ResetRes` chọn lại resource/template, Init rồi ChangeFeature; có nguy cơ reset đè hình mới nếu state chuẩn chưa cập nhật. |
| Chọn bộ phận/tài nguyên | C/gamecore/KNpcRes.cpp:1703–1726 `ChangeFeature` đòi resource node và gọi `SetPartInfo` cho mũ/áo/vũ khí/ngựa/áo choàng. :1744–1752 kiểm miền và node; :1760–1769 bỏ qua part không đổi hoặc cập nhật action vũ khí; :1792–1799 tìm filename/frames/dirs/interval rồi SetSprFile hoặc Release. |
| Vẽ | C/gamecore/KNpc.cpp:5853 là `Paint`, :5915–5916 đặt doing và gọi `m_DataRes.Draw`; C/gamecore/KNpcRes.cpp:241–252 `Draw` kiểm frame và resource/world trước vẽ. |

[ĐỀ XUẤT] Handler appearance riêng tìm đúng NPC qua `(NpcNetId, SpawnGeneration)`, loại revision cũ, ghi trường appearance được server xác thực rồi đi qua đường ChangeFeature đang có. Khi đổi model phải dùng khởi tạo resource phù hợp; khi chỉ đổi đồ không reset template chiến đấu hoặc kind. Bản ngoại hình đầy đủ phải tới viewer mới/spawn lại/đổi map; tháo về mặc định của profile. Gói đến trước spawn chỉ cache có giới hạn, xóa khi despawn, tránh reuse NetId. Không gửi bộ đồ riêng của owner cho mọi viewer.

[CHƯA KIỂM] Từng model con có part áo/mũ/vũ khí và animation tương ứng hay không; PAK/SPR, nam/nữ, hướng/động tác, thứ tự main loop với ResetRes/LoadDataFromTemplate và ngoại hình sau chuyển map. Có renderer không chứng minh mọi NPC mặc đồ human được. Khi thiếu tài nguyên, thiết kế A-14 cho phép giữ hình mặc định và thông báo giới hạn; chưa triển khai hoặc kiểm fallback.

## 4. Gói tin cần thêm và luồng dữ liệu

[NGUỒN] C/gamecore/KProtocol.h:1140–1166 có tọa độ, container và cờ của `PLAYER_MOVE_ITEM_COMMAND/SYNC`, thiếu CompanionId/requestId/revision; `NPC_SYNC` thiếu appearance. C/gamecore/KProtocol.cpp:28 ghi NPC sync dài biến đổi (`-1`), :74 dùng `sizeof(PLAYER_MOVE_ITEM_SYNC)`; sửa struct một phía có thể phá parser. Không chọn opcode hoặc công bố size/packing từ suy đoán.

| Gói logic mới — [ĐỀ XUẤT] | Dữ liệu tối thiểu / nơi nối |
| --- | --- |
| `C2S_COMPANION_QUERY` | Version/length/requestId, revision đã có; xin roster/bộ đồ khi mở panel hoặc resync. Đây là phần bổ sung luồng query cho snapshot của A-14, không khẳng định gói đã tồn tại. |
| `S2C_COMPANION_SNAPSHOT` | RosterRevision, tối đa 10 con, ID bền, khóa/active, template/sex/cấp/điểm, slot và item handle của owner; snapshotId/chunk nếu cần. Handler mới trong KProtocolProcess, cache riêng trước khi thông báo panel. |
| `C2S_COMPANION_EQUIP_OP` | Version/length/requestId, CompanionId, op mặc/tháo/swap, equipSlot, itemHandle+generation, source/destination, expectedRosterRevision/InventoryRevision. Đích lấy từ context panel; owner lấy từ phiên, không tin điểm/sex do client khai. Nối hàm gửi gần đường SendClientCmdMoveItem nhưng không nhét ID vào X/Y hoặc m_IsComp. |
| `S2C_COMPANION_EQUIP_RESULT` | RequestId/resultCode/revisions, delta item-location/slot/stats/appearance; chỉ áp nguyên khối. ACK trả đúng con kể cả panel đã chọn con khác; duplicate cùng ID không đổi đồ lần nữa. Mất/lệch revision xin snapshot. |
| `S2C_COMPANION_APPEARANCE` | Version/length, NpcNetId+SpawnGeneration, appearanceRevision, model/sex và helm/armor/weapon resource cần thiết; broadcast đúng viewer và gửi lại trạng thái đầy đủ khi vào vùng. Không dùng ID bền riêng tư thay NetId để tìm NPC vẽ. |
| `C2S_COMPANION_ACTIVE_OP` + kết quả | Chỉ cần nếu UI có gọi/thu hồi/đổi đội con: requestId, CompanionId, action/active slot, expectedRosterRevision; server trả kết quả và snapshot/delta roster. Chọn dòng để xem không gửi lệnh thay active. [CHƯA KIỂM] Chính sách số con active và protocol gọi legacy; chưa chốt payload/opcode. |

[ĐỀ XUẤT] Thêm capability/version handshake trước khi bật UI; kiểm length/count/enum/giới hạn trước parse, dùng kiểu wire xác định độ rộng và byte order. Phân biệt ID bền con với NPC/item handle phiên. Đồng bộ owner inventory và bộ con cùng revision, không chạy ExchangeItem cũ trước rồi vá bộ con sau. Server/DB phải hoàn tất ownership, requirement, atomic item save của A-14 trước khi nghiệm thu UI mặc đồ. F-01 không khảo sát thêm server hoặc chốt lưu DB.

## 5. Điểm chèn và kích thước triển khai

Ước lượng **[ĐỀ XUẤT, CHƯA KIỂM bằng build/prototype]** cho một lập trình viên quen Cocos/engine, tính ngày công 8 giờ, chưa gồm server/DB, tạo sprite, dịch đầy đủ UI, kiểm thiết bị/binary. Các file mới là tên đề nghị, số dòng dưới là điểm neo file hiện có, không phải patch được duyệt.

| Nhóm | File/điểm chèn cụ thể | Cỡ việc sơ bộ |
| --- | --- | --- |
| Panel roster + bộ đồ | Mới `gameui/KuiCompanion.cpp/.h`; tham khảo `KuiTeam.cpp:182,557,751` và `KuiRoleState.cpp:44,2208,2316`. Danh sách 10 con, ô khóa, trạng thái, tooltip, mặc/tháo/pending. | 2 file mới, 2–3 ngày. |
| Mở/đóng + cập nhật UI | `gamescene/KgameWorld.cpp:1203,2506,2704,13603,14421`; bổ sung khai báo/state tương ứng ở KgameWorld.h (số dòng header [CHƯA KIỂM]). Mới callback/node tag độc lập, phục hồi touch, cập nhật theo ID. | Khoảng 2–3 file sửa, 0,5–1 ngày; file chứa tag [CHƯA KIỂM]. |
| Chọn món từ kho | `gameui/KuiItem.cpp:1069–1090` và `KuiItem_New.cpp:425–435`; adapter nhận target context trước gửi, hiển thị lỗi/đang chờ. Nhánh kho phụ :497/:862 không dùng làm equip-set. | 1–2 file sửa, 0,5–1 ngày; nhánh UI thực dùng [CHƯA KIỂM]. |
| Cache roster + protocol | Mới `gamecore/KCompanionClient.cpp/.h`; `KProtocol.h:293,1140`, `KProtocol.cpp:28,74,655`, `KProtocolProcess.cpp:56,102,2157` và header handler tương ứng (dòng [CHƯA KIỂM]). Snapshot/chunk/revision/duplicate, query và kết quả. | 2 file mới + khoảng 4 file sửa, 2–3 ngày; API CoreShell/registry có thể tăng phạm vi. |
| Appearance viewer | `gamecore/KNpc.cpp:698,10575–10615`, `KNpcRes.cpp:1703–1726,1760–1769,1792–1799`; handler trong nhóm trên và state generation/revision. Giữ renderer nếu tài nguyên đã đáp ứng, sửa khi có ca chứng minh cần. | Khoảng 1–2 file sửa thêm, 1–2 ngày; sprite/animation mới ngoài ước lượng. |

Tổng sơ bộ **10–14 file mới/sửa, 6–10 ngày công** có giao nhau giữa nhóm; không cộng lại file protocol hai lần. Đây là cỡ client, không cam kết tính năng toàn hệ thống chỉ mất khoảng đó. UI chỉ đọc có thể làm trước; mặc/tháo phụ thuộc hợp đồng server/item, appearance phụ thuộc model/resource. Cần chốt schema số ô (A-14 đề nghị 10 ô đầu, tối đa 100 item cho 10 con), số con active và nhánh UI đang build trước lập kế hoạch patch cuối.

## 6. Kiểm chứng tiếp theo — chưa chạy

Tất cả dưới đây **[CHƯA KIỂM]**, là tiêu chí cho task triển khai sau có quyền build/runtime:

- Mở/đóng panel, touch không kẹt; roster 0/1/10 con, con khóa/chưa spawn, đổi thứ tự không đổi ID; hai con cùng template vẫn có bộ đồ độc lập.
- Mặc/tháo/swap đúng con, sai sex/cấp/điểm/slot, kho đầy/item đã chuyển; đổi con trong khi chờ ACK, timeout/ACK lặp/đảo thứ tự/reconnect không mất hoặc nhân đồ.
- Parse gói thiếu/thừa length, count quá lớn, enum sai, phiên bản cũ; snapshot chia chunk thiếu không áp một phần. Client chưa hỗ trợ không mở tính năng.
- Owner/viewer khác/viewer vào sau đều nhận hình cùng revision; gói trước spawn, despawn rồi reuse NetId, ResetRes, chuyển map, tháo về mặc định.
- Ma trận model/sex × mũ/áo/vũ khí × đứng/chạy/đánh/cast; thiếu sprite có fallback, stats không phụ thuộc sprite. So source với binary/config build thực trước khẳng định đường UI đang chạy.

## Kiểm chứng và bàn giao

- Đã đọc trực tiếp callback/list/slot/item packet và đường NPC/renderer được dẫn; chỉ ghi báo cáo F-01 và thêm mục Kết quả task. Không sửa A-12/A-14/BAI_HOC/source; không tạo script phụ hoặc kết nối ngoài.
- Lỗi/khắc phục trong cùng lượt: đọc mặc định lần đầu làm lỗi dấu task, đã đọc lại UTF-8; hai đường `REPORTS/...` và source ổ D trả `PathNotFound`, dùng đúng hai file dưới JX1_OPS và bản C được A-12 dẫn. `rg` không có (`The term 'rg' is not recognized`), chuyển Select-String; không cài công cụ. Đọc KCoreShell.cpp qua đường C một lần báo không tìm thấy; không dùng làm bằng chứng hoặc tiếp tục dò rộng. Python truyền `-c` gặp mất dấu nháy (`SyntaxError`), chuyển stdin với `python -I -`; đầu ra tiếp gặp `UnicodeEncodeError` cp1252, đặt stdout UTF-8 rồi đọc thành công. Một số batch dài bị rút gọn, thu hẹp đoạn cần kết luận. Get-Content mặc định cho số dòng khác do encoding legacy; dùng byte split LF/Python và Select-String cho dẫn chứng vật lý.
- Kiểm đầu ra: báo cáo có đúng 5 dòng tóm tắt đầu, đủ UI/packet/renderer/điểm chèn/cỡ việc và các dấu [CHƯA KIỂM]; xem diff hai file một lần và kiểm whitespace. Đây là kiểm tài liệu, không phải test/build game.
- Trạng thái cuối **DONE** cho phạm vi khảo sát. Không còn blocker giao báo cáo; các mục runtime/resource/ABI và server/DB nêu trên vẫn chưa xác minh theo phạm vi cho phép.
- Commit SHA/link: **không có**. Không stage/commit/push vì người dùng chỉ yêu cầu khảo sát và ghi file theo task, chưa yêu cầu công bố Git; giữ kết quả local để duyệt.

## Đối chiếu checkpoint ngày 18/11/2026

- Trạng thái đầu lượt: task đã `done`, báo cáo đã có đủ năm dòng tóm tắt; `git status --short --branch` trả `## task/F-01`, không có thay đổi local. Tiếp tục từ kết quả ngày 17/11, giữ nguyên bằng chứng khảo sát đã ghi.
- Đã đọc task, báo cáo F-01 và hai báo cáo nền A-12/A-14. Đối chiếu đủ các mục được giao: UI đội/chọn con, ô trang bị và mặc/tháo, đường ngoại hình NPC khác, điểm chèn `file:dòng`, packet đề nghị và cỡ việc client. Không phát hiện thiếu mục cần khảo sát bổ sung. Phân biệt nguồn C của A-12/F-01 với nguồn D của A-14 đã được báo cáo nêu rõ.
- Lỗi trong lượt đối chiếu và cách xử lý: đọc task mặc định hiển thị lỗi dấu, đọc lại bằng `-Encoding UTF8` thành công; hai đường literal `REPORTS/A-12-hao-huu-mac-do.md` và `REPORTS/A-14-hao-huu-trang-bi-thiet-ke.md` báo `PathNotFound`, chuyển đúng hai file dưới `JX1_OPS/REPORTS/` đã được checkpoint chỉ dẫn. Đầu ra gộp A-12/A-14 bị rút gọn, đọc riêng các đoạn còn thiếu để hoàn tất đối chiếu. Các lỗi đọc đã xử lý, không còn blocker bàn giao tài liệu.
- Phạm vi xác nhận lần này là độ phủ và tính nhất quán của tài liệu. Độ mới của source so với checkpoint, build/runtime/resource/ABI và server/DB vẫn **[CHƯA KIỂM]**; bước tiếp theo là task triển khai/kiểm chứng riêng được cấp quyền tương ứng.
- Trạng thái cuối **DONE** cho F-01. Chỉ bổ sung ghi nhận vào báo cáo này và mục Kết quả của task; không sửa source, không chạy exe, VM, build/test hoặc mạng. Không stage/commit/push trong lượt này; không có SHA/link Git mới.
