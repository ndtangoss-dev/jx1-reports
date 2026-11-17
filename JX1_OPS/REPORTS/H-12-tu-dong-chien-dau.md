# TÓM TẮT 5 DÒNG
1. DONE khảo sát tĩnh: Client2912/Coco có mã chọn mục tiêu, dùng skill, nhặt, uống thuốc, phù về và xử lý trong thành; chưa xác minh runtime.
2. Đếm được 11 dòng phái auto (10 có skill), 25 dòng thuốc, 66 tuyến; bảng Skills có 1.720 dòng, 1.719 ID khác nhau.
3. Auto người chơi nằm phía client; `Kautoai.cpp` có `#ifndef _SERVER`, còn nhánh player server chỉ xử lý trap trong đoạn đã kiểm.
4. BOT E-02 có vòng săn offline, thiếu hồi máu/nhặt/phù về; AI NPC nên dùng lõi server, không chép nguyên UI auto người chơi.
5. Chỉ ghi báo cáo và mục Kết quả task; không sửa mã, mạng/VM/exe/build/test; chưa commit/push vì không được yêu cầu và task cấm mạng thật.

## Phạm vi, nguồn và cách đếm

Ngày 17/11/2026; worktree `D:\JX-wt\H-12`, nhánh `task/H-12` đúng task.
Git status ban đầu chỉ có `JX1_OPS/TASKS/H-12.md` untracked; giữ nội dung gốc.
Chỉ tạo báo cáo này và bổ sung `## Kết quả` vào task theo chỉ định trực tiếp.
Đã kiểm mã H-12 có trong backlog; tiêu chí đầu ra lấy trực tiếp từ task.
Không đọc nội dung file tài khoản/khóa hoặc các profile auto cá nhân; không ghi bí mật vào báo cáo.

Đường dẫn viết tắt dưới đây là đường dẫn local, không phải dữ liệu đã đưa lên dịch vụ ngoài:

| Ký hiệu | Gốc |
| --- | --- |
| C | `D:\JX-source\client\Classes` |
| S | `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src` |
| F | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client` |
| G | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs` |

Nhãn [XÁC MINH] là kết quả đọc/đếm/so byte trực tiếp; [NGUỒN] là hành vi được viết trong source,
không chứng minh binary đang chạy; [BÁO CÁO] là kết quả lượt khác chưa chạy lại; [GIẢ THUYẾT] là đề xuất.
"Bản gốc" ở đây là bộ Folder được task chỉ định. Client2912 này tự nó đã là cây Cocos;
không đủ bằng chứng để gán tính năng cho mọi phiên bản PC JX1 lịch sử.

Đếm offline bằng Python `python -I -` đọc byte/tab, không tạo script phụ. Bảng có header tính số dòng
không rỗng trừ 1; danh sách `jx50ai/*.txt` không có header thì tính toàn bộ dòng không rỗng.
Giữ byte khi đếm để không lệ thuộc giải mã tên tiếng Việt cũ. Đây là số dòng cấu hình,
không phải số đối tượng đang spawn hoặc số mục server thực tế nạp thành công.

## ĐÃ XÁC MINH

### 1. Bản gốc và Coco có gì

[XÁC MINH] So byte trực tiếp `F/Classes` với C:

| File | Kết quả | Số dòng Folder / C |
| --- | --- | ---: |
| `gameui/KuiAutoPlay.cpp` | Trùng toàn bộ byte | 6.987 / 6.987 |
| `gamecore/KNpcAI.cpp` | Trùng toàn bộ byte | 5.811 / 5.811 |
| `gameui/Uiglobaldata.h` | Trùng toàn bộ byte | 647 / 647 |
| `vn/gamescence/KgameWorldVN.cpp` | Khác byte; cả hai vẫn có tạo UI và bật/tắt auto | 7.135 / 7.314 |

Điểm tạo `KuiAutoPlay::create`: `F/Classes/vn/gamescence/KgameWorldVN.cpp:2832`, `:2894`;
bản C ở `C/vn/gamescence/KgameWorldVN.cpp:2966`, `:3028`.
Bật/tắt gọi `setAutoPlay(false/true)` tại Folder `:2034`, `:2040`, bản C `:2168`, `:2174`.
Chưa truy nguyên toàn bộ chênh lệch của file scene; không gọi toàn cây C là bản sao y Folder.

| Khả năng | Bằng chứng mã hiện có và giới hạn |
| --- | --- |
| Chọn mục tiêu | `C/gameui/KuiAutoPlay.cpp:5010` `RefreshNpcs`: index hợp lệ, tên không rỗng, HP > 0, `kind_normal`, loại 3 mục tiêu lag và vùng lag. `:5125` `SearchNearestNpc`: lấy gần nhất với khoảng cách **nhỏ hơn** range; khi đủ 3 mục tiêu lag có nhánh chọn xa hơn. `:4753` kiểm `relation_enemy` trước đánh. Không đồng nhất mọi NPC normal với quái được phép đánh. |
| Đi tới/đánh lặp | `:4727` `ProcessAttack`, `:4786` dùng tầm skill để di chuyển, `:4853`/`:4854` gửi lệnh skill local và C2S theo world ID. `:5236` yêu cầu fight mode và checkbox đánh NPC. Có bộ đếm bỏ mục tiêu không mất máu/chạy quá lâu (`:4762`, `KuiAutoPlay.h:298`, ngưỡng 100 lần gọi). |
| Skill công kích/hỗ trợ | `:4695` chọn left skill; `:4702` giới hạn tầm đánh gần theo tầm thật, tối thiểu 75 trong nhánh chỉnh. `:6608` `CastStateSkill`: 3 slot hỗ trợ, kiểm CanCast, cost, có skill, chưa có state; bỏ ID 1/2/3/53. `:3326` có buff theo bảng phái, được gọi từ VLRecover tại `:3955`; phái 4 còn có DoNgaMiBuff (`:3952`). |
| Nhặt đồ | `:4353` `VLCollect`: checkbox, fight mode hoặc cho nhặt trong thành. `:4032` `SearchObj`: chọn vật gần, `PickUpObj` khi < 48 (`KuiAutoPlay.h:24`), đi tới nếu cần, bỏ đối tượng chờ quá 150 lượt. `:4119` `CheckObj`: loại object không hợp lệ, lọc loại/tên, blacklist, kích thước túi. Có lọc thuộc tính/giá/giữ trang bị sau nhặt (`:4188`, `:4217`). |
| Uống thuốc | `:3580` `VLRecover`, `:3747` HP và `:3806` MP: đọc runtime info, ngưỡng phần trăm, thuốc trong túi/ô nhanh, gọi `ApplyUseItem`. HP nhận blood/both/allboth, MP nhận mana/both/allboth. Hai ngưỡng cùng loại được OR, không chứng minh chọn hai loại thuốc khác nhau. |
| Phù về | `:3666` HP dưới ngưỡng; `:3686` hết thuốc HP; `:3716` hết thuốc MP; `:3909` độ bền thấp; `:3994` thiếu chỗ túi. `:3540` `UseTDP`: phải bật yêu cầu, đang fight mode, có townportal hoặc mine particular 162/163/164; `ApplyUseItem`, cờ `nIsReTurn`, bộ chờ. |
| Trong thành/quay lại bãi | `:6223` `VLMap`: không fight + AIFullAuto, lựa chọn xa phu; gọi bán, kho, mua/sửa, thuốc rồi xa phu (`:6261`, `:6288`, `:6321`). Có mã `VLMove:5367` cho di chuyển. Đây là chuỗi điều kiện, chưa chứng minh vòng về thành → tiếp tế → quay đúng bãi hoàn tất. |

### 2. Điều kiện bật, phân chia client/server và dữ liệu cấu hình

- [NGUỒN] `C/gameui/KuiAutoPlay.cpp:239` đăng ký `scheduleUpdate`; `:6915` dùng `isOpen`,
  `m_bIsAutoInitDone`, core/world và `GetAutoplayid()`. `:6926` dừng khi đang pathfinding (`g_fp`)
  hoặc trading. Các lượt gọi dùng modulo bộ đếm update, không dùng `delta` để định thời.
  Không lấy comment “100ms/5s” làm số đo; không quy nhịp client này sang 18 Hz server.
- [NGUỒN] `:6890` `setAutoPlay` có tham số tên `colse`: true là tắt, false là bật;
  `OpenAutoPlay:6904` có lệnh bật bị comment. Việc gọi OpenAutoPlay không đủ chứng minh auto đã bật.
- [NGUỒN] `C/gamecore/CoreShell.cpp:3790` → `SendClientAutoPlay`; `C/gamecore/KProtocol.cpp:478`
  tạo `c2s_autoplay`. Khi `cishu==-1`, bật còn yêu cầu nạp `update10/settings/mappos/biao_pos.txt:516`,
  `update10/settings/Ai/skill.txt:522`, `MagicDesc.ini:538`; thiếu thì return trước gửi ở `:587`.
  Chế độ tuyến còn cần `%u_Pos.txt` nếu `nAutoModel==1` (`:544`).
- [XÁC MINH] Không có file rời ở bốn đường dẫn đã kiểm: `F/Resources/update10/settings/Ai/skill.txt`,
  `F/Resources/settings/Ai/skill.txt`, `F/data/update10/settings/Ai/skill.txt`,
  `F/Resources/update10/settings/mappos/biao_pos.txt`. **Không kết luận thiếu khỏi PAK/APK**;
  thứ tự mount/override chưa kiểm. Đường bảng skill UI (`settings/Ai`) khác đường bật (`update10/settings/Ai`).
- [NGUỒN] `S/KProtocolProcess.cpp:292`, `:6007`: nhận autoplay, kiểm index player/NPC;
  `ncishu>=0` dùng cho việc khác, còn nhánh âm gọi `SAutoplay`. `S/KPlayer.cpp:10694` chỉ đặt cờ
  `m_AutoplayId` nếu button 0/1 và nhận 7 trường lọc/nhặt, rồi gọi `script/system/autoplayer.lua:10721`.
  `C/gamecore/KProtocolProcess.cpp:3102` nhận lại `AutoplayId` từ sync.
- [NGUỒN] `G/script/system/autoplayer.lua:7`: button 0/1 return sớm, các lệnh `SetPlayFF` tương ứng
  đã comment; cờ được đặt bởi C++. `:19` chặn truyền tống khi `GetPlayFF()>0`, `:72` nhánh button 2
  có yêu cầu tiền và truyền tống. `G/script/system/autoPlayecloser.lua:3` gọi `SetPlayFF(0)`.
  Không nhầm tên script với vòng tự chiến đấu server.
- [NGUỒN] `S/KNpcAI.cpp:771`: nhánh `_SERVER` của `ProcessPlayer` chỉ gọi `TriggerMapTrap`,
  comment `:776` nói có thể thêm offline AI. `S/Kautoai.cpp:8` là `#ifndef _SERVER`:
  có `RunNormal:332`, `RunAutoAttack:362` gọi Lua AutoAi, nhưng không phải bằng chứng auto server.
  `ReturnCity:508` còn ghi chú protocol đã bỏ. Không thấy bằng chứng treo máy khi client tắt trong đường đã kiểm.
- [NGUỒN] `C/vn/gameui/UiglobaldataVN.h:13` profile `jx50ai/autoset/%u_set.ini`, `%u` từ hash tên
  (`KuiAutoPlay.cpp:266`); `UiglobaldataVN.cpp:9` `InitAuto` copy `jx50ai/autobasic.ini` nếu chưa có,
  và 6 danh sách nếu thiếu. Chưa có cơ chế cập nhật profile cũ từ default mới trong đoạn này.

[XÁC MINH] Một số giá trị **file default** `F/Resources/jx50ai/autobasic.ini`:

| Nhóm | Giá trị | File:dòng |
| --- | --- | --- |
| HP | LifeCK=1; Life1=50, Life2=20, Life3=1000 | `autobasic.ini:2`, `:4` |
| MP | ManaCK=1; Mana1=50, Mana2=20, Mana3=1000 | `:3`, `:7` |
| Phù | HP thấp/hết thuốc HP/hết MP tắt; TPLifeEdit=30; độ bền bật, ngưỡng 5; đầy túi tắt | `:10`, `:11`, `:12`, `:13`, `:14`, `:15`, `:18` |
| Tiếp tế toàn phần | AIFullAutoCK=0 | `:25` |
| Đánh | RadiusEdit=800; FightNearCK=1; FightNearEdit=75 | `:49`, `:50`, `:51` |
| Nhặt | AutoPickUpCK=1; PickUpRange=400 | `:71`, `:73` |

Các default trong hàm tạo UI có thể khác file: `KuiAutoPlay.cpp:578` Mana1 fallback 20,
`:1579` PickUpRange fallback 800. Khi có profile/default file thì không được báo fallback là giá trị đang dùng.
HP/MP interval được mã quy đổi từ mili giây bằng `*60/1000` (`:3779`, `:3841`),
nhưng counter chỉ giảm trong nhánh dưới ngưỡng; cần đo thực ở 30/60 FPS và khi app chạy nền.

### 3. Bảng số liệu và ví dụ tối thiểu

| Dữ liệu gốc | Số mục/dòng dữ liệu | Ví dụ/cột dùng | Bằng chứng |
| --- | ---: | --- | --- |
| `G/Settings/Ai/skill.txt` | 11 dòng; 16 cột; 40 ô skill khác 0 trong 7 slot/dòng | Số phái 1..11; dòng phái 11 có toàn bộ slot 0; Thiếu Lâm có skill_1=15, skill_2=273, Left_0=318; Thiên Vương có 33/42/322 | `skill.txt:1`, `:2`, `:3`, `:12`; loader theo dòng phái+2 tại `C/gameui/KuiAutoPlay.cpp:3347` |
| `G/Settings/item/potion.txt` | 25; 28 cột header | DetailType 0..4, mỗi loại 5 dòng; dòng 2 genre/detail/particular=1/0/0, dòng 3=1/0/0 (khác level/giá); dùng cả stack/type, không chỉ tên | `potion.txt:1`, `:2`, `:3`; `VLRecover:3766` |
| `G/Settings/autopathfindroutes.txt` | 66; 12 cột | ROUTE_ID, NODE_0..9, DESCRIPTION; route 0 nối map 37→38→39→40; route 1 bắt đầu 37→41→42 | `autopathfindroutes.txt:1`, `:2`, `:3`; chưa chứng minh UI auto đang dùng chính bảng tuyến này |
| `G/Settings/Skills.txt` | 1.720; 116 cột; 1.719 SkillId khác nhau | ID 1 AttackRadius=100, ID 2=320; có TargetEnemy/TargetAlly/TargetSelf, cost, TimePerCast, HorseLimit | `Skills.txt:1`, `:2`, `:3`; ID 521 lặp ở `:522`, `:523`, chưa xác định ưu tiên loader |
| `G/Settings/Npcs.txt` | 2.435; 106 cột | Kind=0: 1.412; Kind=3: 958; Kind=4: 23; Kind=5: 23; Kind rỗng: 19. Có Skill1..4/Level1..4, VisionRadius, ActiveRadius, AIMode | `Npcs.txt:1`; template STT 1 AIMode=3, STT 2 AIMode=6 (`:2`, `:3`). Không coi 2.435 dòng là quái săn được |
| `F/Resources/jx50ai/itemName.txt` | 2, không header | Thanh long đao/series 3; Điêu bì diện tráo/series 5 | `itemName.txt:1`, `:2` |
| `itemDontNeedName.txt` cùng thư mục | 11, không header | hoa tán; độc tán | `itemDontNeedName.txt:1`, `:2` |
| `itemNameAttr.txt` cùng thư mục | 40, không header | 85=Sinh lực; 88=Phục hồi sinh lực | `itemNameAttr.txt:1`, `:2`; giới hạn 40 tại `KuiAutoPlay.h:25` |
| `itemSellName.txt` cùng thư mục | 13, không header | Cẩm nang hoàng kim; Hoa hồng | `itemSellName.txt:1`, `:2` |
| `itemUseName.txt` cùng thư mục | 8, không header | Người tuyết choàng khăn xanh (thường) | `itemUseName.txt:1` |
| `teamAvoidName.txt` cùng thư mục | 0 byte, 0 mục | Danh sách rỗng | đọc kích thước và đếm trực tiếp |

Sáu danh sách trên có tổng 74 mục, loader `KuiAutoPlay.cpp:293`–`:368` dùng dòng i+1,
giới hạn 64 cho các danh sách tên (`KuiAutoPlay.h:26`). Không dán toàn bảng.
`potion.txt` có dòng 19 hoặc 28 cột khi tính cả phần đuôi trống;
không suy đây là lỗi nạp, chỉ ghi nhận không nên ép mọi dòng có đủ cột đuôi.
Tên tiếng Việt trong một số bảng gốc không giải đúng bằng UTF-8/GB18030 đơn thuần;
ví dụ số/ID/cột ASCII phía trên không phụ thuộc suy đoán encoding tên.

### 4. Giới hạn phía server ảnh hưởng auto

- [NGUỒN] `S/KGameglobalSet.cpp:108` nạp `ServerConfig/AutoPlayForBitItem`.
  `G/Settings/gamesetting.ini:479` và `gamesetting_gs001.ini:497` đều có `1,0,8`.
  `S/KNpc.cpp:12747`, `:13173` kiểm cờ auto, bật hạn chế và giờ server `>=0 && <8`;
  chỉ return bỏ item nếu `CheckAllItem(3, genre, detail, particular)` khớp.
  Đây là hạn chế **một nhóm item**, không phải cấm auto hay cấm toàn bộ drop 0–8h.
  Danh sách nhóm 3 và file settings thật được binary chọn chưa được xác minh.
- [NGUỒN] `S/KNpc.cpp:2491`: quái kind_normal có GoldType 1..4,
  last damager là player auto=1 và `nIsNoBlue!=0` thì không gọi DeathPunish trong nhánh đó;
  các nhánh khác vẫn gọi. Tên cờ/comment không đủ khẳng định toàn bộ hiệu ứng gameplay.
- [NGUỒN] `S/KNpc.cpp:12498` trở đi còn lọc loại tool/equipment/tupu theo cờ auto trước tạo drop.
  Không coi bật checkbox nhặt ở client là đảm bảo server sẽ tạo/rơi vật phẩm đó.
- Trong handler bật đã đọc không có gate cấp/VIP/thời lượng; **không kết luận toàn game không có gate**.

### 5. Khoảng trống Coco và đối chiếu BOT E-02

Không thiếu nguyên khối auto trong source Coco đã kiểm. Khoảng trống là chứng minh tích hợp,
asset/profile, độ đúng các điều kiện và độ ổn định; có các điểm mã cần theo dõi nhưng task này không sửa:

| Điểm | Kết luận tĩnh và việc còn thiếu |
| --- | --- |
| Bật và sync | Có đường UI→C2S→server→sync; thiếu một lần quan sát runtime xác nhận cờ và lệnh skill sau bật. OpenAutoPlay tự bật đang comment; các tài nguyên update10 có thể làm return sớm. |
| Nhịp hành động | Phụ thuộc số update; thuốc giả định 60 FPS. Chưa đo spam/cooldown ở 30/60 FPS, nền, reconnect. |
| An toàn HP/MP | Phép chia `Info.nLifeFull`/`Info.nManaFull` tại `:3754`, `:3813` không có guard zero ngay tại biểu thức; đây là rủi ro cần dữ liệu runtime, chưa gọi là crash đã tái hiện. |
| Tự phù do đầy túi | `CheckInventory:3994` kiểm kích thước theo chọn, nhưng `:4019` ghi đè `bHaveRoom` bằng FindRoom(1,1); bằng chứng source cho việc lựa chọn kích thước không quyết định kết quả cuối. |
| Vòng tiếp tế | `CheckReady:6102` trả true vô điều kiện. Trong VLRecover có nhánh mua thuốc bị comment (`:3643`, `:3784`); VLMap vẫn có chuỗi mua thuốc riêng. Không kết luận toàn bộ mua thuốc bị tắt hoặc full auto đã đủ điều kiện quay lại bãi. |
| Hai họ logic client | `KNpcAI::FollowCharacter:1573`, `AutoMovePickUp:2014`, `MoveJiaoBen:917` và UI `KuiAutoPlay` cùng tồn tại. Nhiều guard dùng `__open_autoact` ở `KNpcAI.cpp:629`, `:684`; chưa chốt mọi call site/giá trị cờ nên không cộng tính năng của hai họ thành một pipeline chạy thực. |

[NGUỒN] Đọc trực tiếp `JX1_OPS/BOT/behavior.py`, kèm [BÁO CÁO]
`JX1_OPS/REPORTS/E-02-hanh-vi-bot.md`:

| Hành vi | Coco/Folder | BOT E-02 hiện tại |
| --- | --- | --- |
| Chọn/đi/đánh | Npc/scene local, lọc quan hệ, range, xử lý lag, lệnh skill | `behavior.py:166` `Hunt.step`: gần nhất trong allowlist, kind=0, range, skill level >0, interval; trả Action run/attack. Chọn lại từ candidates mỗi bước, không giả định giữ target đến chết. |
| Xác nhận chết | Kiểm death/revive/HP trong bảng client | `:135` feed 69/76/77/91/92; chỉ death 92 tạo tombstone; `:109` kill credit vẫn chưa kiểm. Không suy hurt=kill. |
| Nhặt | Có Object_, inventory, filter, PickUpObj | Hunt không có nhặt/object policy. |
| Thuốc | Có runtime HP/MP, thuốc/slot, ApplyUseItem | `:200` heal luôn raise ProtocolError TODO; chưa có packet/điều kiện/data HP bản thân đủ bằng chứng. |
| Phù/tiếp tế/quay bãi | Có UseTDP/VLMap/VLMove; cần kiểm runtime | Hunt chưa triển khai vòng này. |
| Mạng và điều phối | UI client có gửi C2S | `:100`–`:105` module offline không socket/vòng nền; chưa nối executor/busy/ACK với E-03 theo báo cáo E-02. |

E-02 báo 65/65 test offline ở lượt của nó; **H-12 không chạy lại** và không dùng số đó chứng minh
gameplay, cooldown, hostility, pathfinding hoặc ABI runtime. Có thể dùng chung bảng skill/thuốc/range
và test policy sau khi chuẩn hóa ID/đơn vị/context, nhưng không copy layout packet/giá trị không rõ
từ Coco sang BOT. BOT có allowlist tường minh là điều nên giữ khi mở rộng săn NPC.

### 6. Hảo hữu cứng / AI công kích NPC có dùng lại được không?

**[GIẢ THUYẾT] Dùng lại nguyên tắc và lõi hành động server được; không gọi nguyên `KuiAutoPlay`
hoặc `AutoAi g_cAutoAi` cho NPC.** Hai mã này phụ thuộc player hiện tại, scene/UI,
inventory và gửi C2S. NPC server phải phát lệnh bằng context NPC, quan hệ server và skill của chính nó.

[NGUỒN] Đường gần nhất đã có là companion, không phải bằng chứng hảo hữu đã triển khai:

- `S/KNpcAI.cpp:48` phân nhánh theo actor; `:77` rank 99 → `ProcessCompanion:3282`.
- `:3291` tìm enemy; `:3294` tìm chủ qua `m_IsRevive`, cập nhật owner companion ID.
  Khác map hoặc cách chủ >800 thì `ChangeWorld:3312`; chủ không fight thì theo, không đánh (`:3322`).
  Cách chủ >400 thì ưu tiên theo (`:3332`); enemy death/revive bị bỏ (`:3340`).
- Enemy >400 thì bỏ; chọn ngẫu nhiên slot 1..4 bằng SetActiveSkill (`:3393`, `:3408`),
  `FollowAttackCompanion:2989` chỉ đánh khi vào attack radius. Lệnh chạy tới enemy trong hàm này đang comment
  (`:3004`); chưa thể nói companion luôn tiếp cận quái ngoài tầm skill dù còn trong 400.
- `GetNearestCharacter:2248` quét region, `KRegion::FindNpcAuto` tại `:2307`, bỏ mục tiêu ẩn;
  đây là tìm theo ô, không chứng minh tối ưu khoảng cách Euclid toàn cục như BOT.
- Không tìm được owner thì nhánh `:3429` loại NPC khỏi region và NpcSet (`:3444`).
  NPC hảo hữu độc lập không thể dùng nguyên lifecycle này.

Hướng dùng lại khi có task triển khai: tách policy chọn mục tiêu/skill/giới hạn hoạt động ra khỏi UI;
adapter player phát C2S, adapter NPC dùng `SendSerCommand` và dữ liệu Npcs/Skills.
Với hảo hữu đi cùng chủ có thể mở rộng companion; với NPC độc lập cần origin/leash riêng, lịch AI,
hostility allowlist, đường chạy/chống kẹt, lifecycle, quyền sở hữu loot/EXP/kill và hồi phục riêng.
Không mặc định NPC có túi/thuốc/tiền/phù như player; không tạo tài khoản BOT thật chỉ để điều khiển NPC.
Việc sinh NPC, schema, thưởng/kill credit và tải đông người đều ngoài khảo sát này.

## CHƯA XÁC MINH

1. Binary/APK thật khớp cây source nào, bộ file PAK nạp theo thứ tự nào, settings/profile nào đang có hiệu lực.
2. Auto chạy đủ năm hành vi trên map thực; treo khi tắt app/mất mạng; xử lý reconnect, đổi map/ID tái sử dụng.
3. Thời gian cooldown/frame thực, hạn chế cấp/VIP/map/script ngoài handler đã đọc; quy tắc thuốc và quyền nhặt server.
4. Hoàn tất vòng phù về/tiếp tế/quay đúng điểm; hành vi khi hết phù, hết tiền, kho/túi đầy, đường bị chặn.
5. Nhóm item cấm số 3, thưởng EXP/loot/kill credit cho companion/hảo hữu; quan hệ PvP/PvE đầy đủ.
6. Build/test/runtime/ABI và test E-02 không chạy trong H-12. Không có test/build được phép nhưng bị bỏ sót.

## Ca test bàn giao TESTER (chưa chạy)

Chỉ thực hiện trong task kiểm thử được duyệt riêng, dùng dữ liệu thử và môi trường thử của dự án.

| ID | Ca kiểm | Kết quả/tiêu chí cần quan sát |
| --- | --- | --- |
| H12-T01 | Bật/tắt auto, profile mới/cũ; lần lượt thiếu biao_pos, skill, MagicDesc | Cờ server và sync đổi đúng; thiếu dữ liệu phải báo rõ, không báo bật thành công khi return sớm. |
| H12-T02 | 2 quái hợp lệ, NPC trung lập, player, quái chết/ẩn, biên search range | Chỉ đánh mục tiêu được phép; xác nhận biên `<range`, quan hệ enemy, chuyển target sau chết; không coi tên là ID. |
| H12-T03 | Địch ngoài/trong attack radius, tường, mục tiêu không mất máu | Di chuyển trước đánh; không gửi dồn vô hạn, bỏ kẹt đúng bộ đếm; đo request/giây. |
| H12-T04 | Left skill hợp lệ/không học, thiếu MP, hồi chiêu, cưỡi ngựa; buff 3 slot | Server chỉ nhận skill hợp lệ; buff không lặp khi có state; không lấy ngưỡng UI làm cooldown server. |
| H12-T05 | HP/MP quanh ngưỡng, thuốc đơn/kép, không có thuốc, MaxHP/MP=0 | Dùng đúng thuốc/slot; không chia zero; đo ở 30/60 FPS và sau chuyển nền. |
| H12-T06 | Nhặt gần/xa, blacklist, không đủ chỗ, ngoài fight/in-town; object biến mất | Chỉ nhặt hợp lệ, kiểm inventory/owner, bỏ object cũ; bật/tắt không bỏ target vì nhặt thất bại. |
| H12-T07 | Phù do HP thấp/hết thuốc/độ bền; không phù hoặc đang trong thành | Phù đúng điều kiện, không spam dùng item; quan sát thứ tự thuốc/phù khi cùng ngưỡng. |
| H12-T08 | Túi còn 1×1 nhưng không đủ 2×2; so TPFullRespos lựa chọn 1/4 | Tái hiện ảnh hưởng `:4019`; ghi expected theo yêu cầu sản phẩm trước khi sửa. |
| H12-T09 | AIFullAuto + xa phu, thiếu tiền/thuốc/kho đầy, đổi scene | Có điều kiện ready thật, không quay bãi thiếu tiếp tế, về đúng map/điểm và tự tiếp tục có kiểm soát. |
| H12-T10 | Cờ auto, nIsNoBlue, GoldType 1..4; giờ 07:59/08:00 và item nhóm 3 | So loot/EXP với auto tắt; chỉ item/nhánh điều kiện tương ứng bị hạn chế; ghi giờ server. |
| H12-T11 | Companion: chủ fight on/off, khoảng cách 400/800, khác map, chủ rời game | Ưu tiên theo/đổi map đúng; không đánh sai quan hệ; kiểm enemy ngoài tầm skill và lifecycle không owner. |
| H12-T12 | BOT offline vectors, đổi context, stale sync/death, thêm policy NPC sau này | Giữ tombstone/allowlist/interval, không gán kill credit từ death; thuốc/nhặt/phù vẫn TODO đến khi có bằng chứng giao thức. |

## Lỗi công cụ, kiểm chứng và bàn giao

- Lần đọc đầu task thiếu `-Encoding UTF8` gây sai dấu; đọc lại UTF-8 một lần, không sửa vì lỗi hiển thị.
- `rg : The term 'rg' is not recognized ...`: một lần; chuyển `Select-String`/đọc trực tiếp, không cài công cụ.
- Một lệnh `Get-ChildItem -LiteralPath ... -Include ... -Recurse` không lọc đúng như dự kiến,
  liệt kê tên file quá rộng và output bị cắt; không đọc nội dung các file đó. Đổi sang thư mục đích nhỏ
  và `Where-Object Name`. Các lần trích đoạn bị cắt được thay bằng đoạn ngắn/đếm có lọc;
  không dùng phần output bị cắt làm bằng chứng kết luận.
- Một lượt Python xuất Unicode bị `UnicodeEncodeError: 'charmap' codec can't encode characters`;
  thêm `sys.stdout.reconfigure(encoding='utf-8')`, lượt sau thành công.
- Một lượt đếm danh sách rỗng gặp `IndexError: list index out of range` ở truy cập header;
  đếm riêng file rỗng và dùng bảng có header được xác định, lượt sau thành công (0 byte/0 mục).
  Không sửa nguồn, không có lỗi nào thử quá 3 lần.
- Đã lưu nháp vào chính báo cáo này trong quá trình khảo sát. Không tạo báo cáo bước riêng,
  không sửa BAI_HOC, không dùng mạng/VM, không chạy binary game/server, không build/test.
- Kiểm chứng thực hiện: đọc source với số dòng, so byte các file nêu trên, đếm bảng/danh sách offline.
  Các ca TESTER là bàn giao, không có tuyên bố PASS runtime.
- Rà diff hai file đầu ra một lượt; kiểm whitespace bằng `git diff --no-index --check -- NUL <file>`
  không có chẩn đoán. Exit 1 của no-index phản ánh file mới khác NUL, không phải test thất bại.

## Bước tiếp theo

**DONE** toàn bộ phạm vi khảo sát tĩnh H-12. Không có blocker đọc nguồn còn tồn tại.
Bước tiếp theo cho PM: review báo cáo rồi giao TESTER xác minh mount/profile và H12-T01..T12;
nếu triển khai hảo hữu thì mở task riêng cho policy actor server và kill/loot ownership.

Commit SHA: chưa có; không stage/commit vì người dùng chưa yêu cầu. Push/GitHub link: chưa có;
không push vì chưa được yêu cầu và task cấm mạng thật. Hai file đầu ra giữ local tại worktree.
