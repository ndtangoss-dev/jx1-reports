TÓM TẮT 1: [NGUỒN] Với tham số server gs001, source chọn MAX_NPC=100000 từ [Gameconfig], không phải 150000 hay 60000; chưa xác nhận binary thực chạy (S/KCore.cpp:262–292; G/Settings/gamesetting_gs001.ini:548–557).
TÓM TẮT 2: [NGUỒN] m_TongBanNum là một DWID; mở 4 đồng bạn phải thay quản lý slot, Lua, AI, trang bị, thu hồi và đồng bộ client, không chỉ đổi phép so sánh (S/KNpc.h:398; S/KNpcAI.cpp:3303; S/KItemList.cpp:1382–1394; H/KProtocol.h:350).
TÓM TẮT 3: [NGUỒN] Chỉ thấy lưu cờ gọi và item list, TongBanInfo bị comment; task có 10000 ID nhưng dùng chung buffer role 128 KiB, chưa có roster 10–15 hảo hữu hoàn chỉnh (L/S3DBInterface.h:41–51,161; S/KPlayerTask.h:13; S/KPlayer.h:284).
TÓM TẮT 4: [NGUỒN] Có đường gán/cast skill môn phái cho NPC; kiểm vũ khí/ngựa chỉ áp player, partner không bị kiểm tại đây; va chạm đạn partner đánh player bị chặn (S/KSkillList.cpp:64–111; S/KSkills.cpp:267–358; S/KMissle.cpp:1378–1380).
TÓM TẮT 5: [NGUỒN] Hook chọn vai nằm trước SetActiveSkill và tại FollowAttackCompanion; đổi map có teleport/xóa theo lockMap, offline xóa NPC, chủ chết chưa có chính sách trực tiếp trong AI (S/KNpcAI.cpp:3312–3344,3405–3446; S/KNpc.cpp:1442–1459).

# A-09 — Đồng bạn nhiều slot

Ngày khảo sát: 2026-11-17. Trạng thái cuối: **PARTIAL — nghiên cứu DONE, commit BLOCKED**. Không triển khai tính năng, không build/test game, không chạy exe, không kết nối VM/SQL/server.

## Worker kiểm tra trước khi làm

- Đã đọc task trước; `Get-Location` = `D:\JX-wt\A-09`, `git branch --show-current` = `task/A-09-codex`; `git status --short` không có thay đổi. Khớp `JX1_OPS/TASKS/A-09.md:7–8`.
- Chỉ tạo báo cáo được giao và cập nhật mục Kết quả của task theo yêu cầu trực tiếp của người dùng. `C:\Jx1CocoV3` chỉ đọc; không thay cấu hình, source, bảo mật hoặc tài nguyên chạy.
- Đọc nền A-08a/b/c/d, thiết kế và chỉ thị 08. Hai đường `DESIGN/…`, `owner-inputs/…` trong task được đối chiếu tại `JX1_OPS/DESIGN/HAO-HUU-CUNG.md` và `JX1_OPS/owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md`; đường DESIGN tại gốc không tồn tại. Yêu cầu là tối đa 4 đi cùng, roster theo phái; không coi đây là tính năng đã có (`JX1_OPS/DESIGN/HAO-HUU-CUNG.md:6–10`; `JX1_OPS/owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md:3`).

## Quy ước và giới hạn bằng chứng

| Tiền tố | Gốc đường dẫn |
| --- | --- |
| S/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/Core/Src/` |
| P/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/Core/` |
| H/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Headers/` |
| L/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Lib/` |
| J/ | `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/` |
| G/ | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/` |

Số dòng từ 1, gồm dòng trống. Markdown đọc UTF-8, đoạn legacy đọc CP936/GBK; dữ liệu một số file pha mã hóa nên kết luận dựa symbol ASCII, số và cấu trúc code, không suy từ chữ hỏng. Tên vật lý mojibake được giữ để tra lại. [NGUỒN] là đọc tĩnh; [ĐỀ XUẤT] là thiết kế suy từ các điểm nghẽn có dẫn nguồn, chưa triển khai. Phạm vi tìm symbol gồm `.cpp/.h` trong gameserver/Sources, header dùng chung, Lib/include và `.lua` rời dưới G/script; không phủ client Cocos riêng, PAK hoặc thư viện đóng.

## 1. MAX_NPC của cấu hình bản dựng

[NGUỒN] Project server định nghĩa `_SERVER`, đưa `KNpc.cpp`, `KSkills.cpp`, `KPlayer.cpp` vào danh sách biên dịch; vì thế nhánh server của `KNpc.h` dùng `MAX_NPC=nMaxNpcCount`, nhánh client dùng 256. Không dùng comment `100000 30000` để suy giá trị (`P/Core.vcxproj:424,540,684,704,748`; `S/KNpc.h:24–29`).

[NGUỒN] `CoreGetServerShell(gamePass)` chuyển tham số vào `g_InitCore`; hàm này dựng `\Settings\gamesetting_%s.ini` rồi đọc `[Gameconfig] MaxNpcCount` vào `nMaxNpcCount`, mặc định khóa thiếu là 1. Với tên `gs001`, **giá trị cấu hình là 100000**, pool có các chỉ số dùng được `1..99999`, vì `KNpcSet::Init` không đưa ô 0 vào free list (`S/CoreServerShell.cpp:227–230`; `S/KCore.cpp:249–265,278–295`; `G/Settings/gamesetting_gs001.ini:548–557`; `S/KNpcSet.cpp:53–64`). Đây là pool chung của core, không phải quota riêng từng map hay đồng bạn.

| File/section rời | MaxNpcCount | Ý nghĩa |
| --- | ---: | --- |
| `gamesetting_gs001.ini`, `[Gameconfig]` | 100000 | Giá trị theo đường nạp khi tên server là gs001 (`G/Settings/gamesetting_gs001.ini:548–557`). |
| `gamesetting.ini`, `[Gameconfig]` | 60000 | File khác; không có nhánh fallback sang file này trong đoạn loader đã đọc (`G/Settings/gamesetting.ini:527–533`; `S/KCore.cpp:262–265`). |
| `gamesetting.ini`, `[ServerConfig]` | 150000 | Khóa cùng tên nhưng khác section; không phải khóa `Gameconfig` mà loader trên đọc (`G/Settings/gamesetting.ini:400,438,527–530`). |

[ĐỀ XUẤT] 500 người × 4 = 2000 NPC đồng bạn là phép tính ngân sách, không phải năng lực đã đo; riêng cấu hình gs001 đang đặt `MaxPlayerCount=200` nên không gán nhầm con số 500 từ file chung. Phải trừ NPC player/quái/NPC thường, dự phòng spawn và đạn trước khi chốt tải (`G/Settings/gamesetting_gs001.ini:555–560`; `G/Settings/gamesetting.ini:529`; `S/KNpcSet.cpp:57–64,867–869`). Chưa xác nhận command line, exe/source khớp, ưu tiên đĩa/PAK hay bộ nhớ/tải thực; không công bố 100000 là số đã quan sát trong tiến trình.

## 2. Bản đồ toàn bộ m_TongBanNum / GetTonBanNun / SetTonBanNun

[NGUỒN] Trường `UINT m_TongBanNum` chỉ giữ **một DWID**, dù tên/comment gọi là “số lượng”: getter trả nguyên giá trị; setter ghi đối số trực tiếp; nơi dùng gọi `NpcSet.SearchID`. `AddTongBan` tạo NPC mới và gắn chủ, không có kiểm đếm 1 con ngay trong thân hàm; rào một con nằm tại các script/giao diện và trạng thái scalar (`S/KNpc.h:398`; `S/ScriptFuns.cpp:12859–12869,12927–12936`; `S/KItemList.cpp:1382–1394`; `S/KNpcSet.cpp:858–893`).

### C++ trong cây được giao

| File và tất cả dòng khớp | Tác dụng / cần xử lý khi mở 4 slot |
| --- | --- |
| `S/KNpc.h:398`; `S/KNpc.cpp:183` | Khai báo/reset một DWID; cần danh sách active slot và count riêng. Trường nằm dưới nhóm biến tạm không vào DB (`S/KNpc.cpp:181–183`). |
| `S/KNpc.cpp:1449,1505` | Lock map/hết lifetime xóa scalar của chủ; phải chỉ xóa slot chứa chính companion đó, không xóa trạng thái của ba con còn lại. |
| `S/KNpcAI.cpp:3303` | Mỗi companion tick ghi DWID của mình lên chủ; nếu chỉ bỏ chặn Lua thì các con ghi đè nhau. Thay bằng đăng ký/kiểm tra quan hệ slot, không ghi “con cuối tick”. |
| `S/ScriptFuns.cpp:12868,12935,26176–26177` | Getter/setter và đăng ký tên Lua. Cần API có slot/companion ID, getter danh sách/count; không đổi âm thầm ý nghĩa getter cũ thành count vì script dùng kết quả làm DWID. |
| `S/KItemList.cpp:1104,1106,1342,1344,1382,1384,1970,1972` | `CanTonEquip`, kiểm `magic_item_needtongban`, `TonEquip`, `UnTonEquip` chọn duy nhất một NPC. Cần chọn companion rõ ràng cho kiểm điều kiện, áp/gỡ stats và cập nhật trang bị. |
| `S/KNpc.cpp:7990`; `S/KProtocolProcess.cpp:2703` | Serialize/nhận một `nTongBanNum`; phải mở hợp đồng dữ liệu nhiều slot hai đầu. Trường wire hiện cũng chỉ một UINT (`H/KProtocol.h:350`). |
| `S/CoreShell.cpp:819,823` | UI lấy lucky của một companion; cần selection/slot. |
| `S/KPlayer.cpp:4669,4672` | Nhánh UI thần tướng kiểm một companion trước khi đặt đồ tại vị trí 53–77; cần companion đang chọn (`S/KPlayer.cpp:4662–4686`). Không coi nhánh `CLIENT_PLAYER_INDEX` này là logic server thuần. |
| `S/CoreShell.cpp:1164,1168,1175` | Nằm trong block comment `1155–1186`; chưa có hiệu lực tại đây. Chỉ rà nếu khôi phục panel FuMo. |
| `S/KNpcAI.cpp:3729,3750,3759`; `3969,3988,3997`; `4208,4229,4238`; `4455,4476,4485`; `4677,4698,4707`; `4922,4943,4952` | Sáu khối bắt pet trong `ProcessAIType01..06`, **đều bị comment**: `3720–3780`, `3959–4017`, `4200–4259`, `4446–4506`, `4669–4728`, `4914–4973`. Không tính thành sáu rào đang hoạt động; nếu mở lại cần cùng API slot. |
| `S/KNpc_backup.cpp:182,1411,1456,5653,8572`; `S/KPlayer - Copy - Copy.cpp:4729,4732` | File backup/copy cũng có symbol; không có trong danh sách ClCompile đã đối chiếu của Core.vcxproj. Không sửa chúng như bản runtime mặc định; cần xác định lại nếu dùng project khác (`P/Core.vcxproj:704,748`). |

Các dòng đọc và ghi trong cùng một hàm được liệt kê riêng để rà không sót. Symbol `GetTonBanNun`/`SetTonBanNun` xuất hiện trong tên đăng ký Lua và wrapper `LuaGetTonBanNun`/`LuaSetTonBanNun` như trên; không thấy wrapper thứ hai trong tập C++ đã tìm. Đây là độ phủ cây source đã nêu, không tuyên bố bao phủ mọi bản fork/binary.

### Lua rời: tất cả 10 file có token

Mỗi dòng dưới là điểm phải rà/di trú; sự hiện diện hàm chưa chứng minh menu, Include hoặc callback thực tế gọi nó.

| File dưới G/script và dòng khớp | Vai trò trong đoạn đọc |
| --- | --- |
| `deadth/Í¬°éËÀÍö/tongyong.lua:8` | OnDeath xóa trạng thái toàn chủ, cần release đúng companion (`:4–15`). |
| `item/34.lua:481,486,489,513,519,530,551,587` | Thu hồi/thu cất, kiểm đã có, triệu hồi; cần slot và giới hạn count thay vì boolean/DWID đơn. |
| `item/3434.lua:390,395,398,422,428,439,460,496` | Bản luồng tương tự 34.lua; tránh bỏ sót đường menu cũ. |
| `item/gm.lua:347,366,2353,2372` | Hai đường summon: OPENTONGBAN dùng GetNpcDwidx; TONGBAN lại truyền nNpcid trực tiếp. |
| `item/gm(¿ª·þ).lua:1306,1325` | Chặn đã có; setter nhận index từ Addyabiao, cần chuẩn hóa DWID (`:1304–1326`). |
| `item/yanniandan.lua:3` | Gia hạn lifetime cho con tìm được từ DWID; thêm lựa chọn con (`:3–14`). |
| `mineitem/gmroleitem.lua:738` | Ghi DWID sau summon; đăng ký đúng slot. |
| `missions/·âÉñ¾º¼¼/·âÉñ¾º¼¼Èë³¡.lua:50` | Cấm vào hoạt động nếu có pet; chính sách mới kiểm count/thu hồi tất cả, không dựa scalar. |
| `System/player/levelup.lua:40` | Hàm TONGBAN ghi index trực tiếp; LevelUp đọc ở `:9–18` không gọi hàm này, không suy tự summon khi lên cấp (`:21–45`). |
| `Î÷ÄÏÄÏÇø/´óÀí¸®/´óÀí¸®/trap/´óÀí¸®toÇ§Ñ°ËþÒ»²ã.lua:48,72` | Getter ở dòng 48 đã comment; setter dòng 72 dùng GetNpcDwidx. Cần kiểm đường trap trước khi cho phép nhiều con. |

[NGUỒN] Index NPC khác DWID: `AddTongBan` trả index, Lua mẫu chuẩn đổi qua `GetNpcDwidx` trước SetTonBanNun, còn getter được giải bằng SearchID ở C++. Các nhánh truyền thẳng index là rủi ro cũ cần sửa khi di trú; không gọi đó là lỗi runtime đã tái hiện (`S/KNpcSet.cpp:869–893`; `G/script/item/gm.lua:361–366,2372`; `S/KItemList.cpp:1382–1384`).

[ĐỀ XUẤT] Tạo một bộ quản lý `active[4]` theo chủ với companion ID bền, DWID và kiểm chủ; API summon/despawn/equip đều nhận slot hoặc companion ID. Giữ adapter getter cũ cho con đang chọn nếu cần tương thích, nhưng bắt buộc thay mọi script quản lý nhiều con. Không lưu DWID qua logout; khi spawn phải cấp DWID mới. Cơ sở: scalar bị ghi đè mỗi tick, chỉ gắn chủ trong AddTongBan và reset về 0 (`S/KNpcAI.cpp:3303`; `S/KNpcSet.cpp:877–890`; `S/KNpc.cpp:181–183`).

## 3. Dữ liệu lưu/khôi phục và roster 10–15 hảo hữu

### Những gì thật sự được serialize ở source

| Thành phần | Kết luận có bằng chứng |
| --- | --- |
| `isCreatTongBan` | Một BYTE trong role base; load sang `IsCreatTongBan` và save ngược. Không phải mảng companion, cấp/EXP/thân mật (`L/S3DBInterface.h:161`; `S/KPlayerDBFuns.cpp:678,1515`). |
| `TongBanInfo` | Struct năm int `inum1..inum5` ở trong `/* … */`, không thể coi là roster được lưu (`L/S3DBInterface.h:41–51`). |
| `m_TongBanNum` | Biến tạm reset 0; không có đường lưu/khôi phục danh sách của nó trong các symbol đã tìm (`S/KNpc.cpp:181–183`; `S/ScriptFuns.cpp:12868,12935`). |
| `cpartnercode`, `ifumo` | `cpartnercode` đang nhận tên đổi nhân vật; không tái sử dụng để nhét roster. Load `ifumo` vào trường thần tướng bị comment; không xem đó là hệ tăng trưởng đã nối (`S/KPlayerDBFuns.cpp:1490–1497,722–728`; `L/S3DBInterface.h:158`). |
| `room_equipmentex` | **Kho chung thuộc KItemList của player**, được Init một lần; `pos_equiproomex` đặt item vào kho đó. Không có khóa companion ID ở đường này (`S/KItemList.cpp:354–366,1050–1056`). |
| Đồ đang mặc của đồng bạn | TonEquip ghi `m_ItemBox[nEquipPlace]`, vị trí `pos_dazao`, X=vị trí mặc, Y=0 rồi áp stats cho NPC lấy qua scalar. UnTonEquip quét 53..77; đây là một bộ dùng chung, khác kho room_equipmentex (`S/KItemList.cpp:1380–1394,1417–1421,1451–1459,1970–1983`). |
| Vật phẩm qua role data | Save item list ghi loại/thuộc tính và `ilocal/ix/iy`; load lấy lại tọa độ/vị trí rồi `m_ItemList.Add`. Có nền khôi phục item, nhưng chưa có ánh xạ mỗi vật phẩm sang một trong 15 companion (`S/KPlayerDBFuns.cpp:1618–1656,895–897,1112–1119`; `S/KItemList.cpp:354–366,1418–1421`). Chưa xác minh SQL round-trip hay áp lại stats sau login. |

### Biến task: giới hạn thật và cách dùng khả thi

[NGUỒN] `MAX_TASK=10000`, `MAX_TEMP_TASK=10000`; GetSaveVal/SetSaveVal chấp nhận **ID 0..9999**, giá trị C++ `int`, lưu trong unordered_map. Lua SetTask/GetTask chuyển số sang int và dùng save value. Task tạm là map riêng, bị ClearTempVar xóa, không dùng cho roster bền (`S/KPlayerTask.h:13–14,53–60`; `S/KPlayerTask.cpp:69–91,104–109`; `S/ScriptFuns.cpp:4001–4056`).

[NGUỒN] Save duyệt toàn 10000 ID, chỉ ghi giá trị khác 0 thành `TDBTaskData{int id,int value}` và đặt nTaskCount; load đọc nTaskCount, bỏ ID >=MAX_TASK, khôi phục các giá trị khác 0. Vì vậy “10000 task” là miền ID, **không phải 10000 ô tự do**, không phải cam kết lưu được 10000 biến cộng mọi item. Buffer save toàn role là 128*1024 byte; riêng 10000 record hai int trong ABI Windows int 32 bit đã khoảng 80000 byte, còn phải chứa base, skill, item… (`S/KPlayerDBFuns.cpp:1361–1382,1844–1863`; `L/S3DBInterface.h:205–210`; `S/KPlayer.h:284`). Chưa kiểm hết các chặn kích thước gateway/DB; không tuyên bố có thể tăng trần an toàn.

[ĐỀ XUẤT — phương án task cho bản thử nhỏ] Dành một dải ID được kiểm tra chưa chiếm, có schema version và công thức offset cố định. Ví dụ mỗi hảo hữu 16 int: mở khóa, phái, template, cấp, EXP thấp/cao, thân mật, vai, bốn skill ID và bốn skill level; thêm 6 int chung cho version/count/bốn lựa chọn active. 10–15 con dùng **166–246 biến**, khoảng **1328–1968 byte** payload task nếu tất cả khác 0, chưa gồm item/base/overhead. Đây là ví dụ thiết kế, chưa cấp dải ID hay chốt format; giá trị 0 cần có nghĩa mặc định khi load vì không được serialize. EXP rộng hơn int phải có codec kiểm miền, không nhét số lớn vào một SetTask (`S/KPlayerTask.cpp:86–109`; `S/KPlayerDBFuns.cpp:1852–1863`; `S/ScriptFuns.cpp:4048–4056`).

[ĐỀ XUẤT — hướng đầy đủ] Ưu tiên bảng roster mới theo `(ownerRoleId, companionId)` với version, phái/template, level, EXP 64 bit, thân mật, vai; bảng skill theo companion/skill slot; quan hệ trang bị theo companion/equip slot và ID item bền. Bốn active slot tham chiếu companionId; DWID chỉ tồn tại trong phiên. Cần sửa chuỗi load/save gameserver–role service–DB, migration và giao thức/UI, giao dịch chống nhân đôi đồ và autosave/logout thống nhất. Lý do chọn: base hiện chỉ có flag, TongBanInfo không hoạt động, đồ mặc/kho chưa phân chủ con (`L/S3DBInterface.h:41–51,161`; `S/KPlayerDBFuns.cpp:678,1515,1651–1653`; `S/KItemList.cpp:1417–1421`). Đây là kiến nghị kiến trúc, **chưa có schema/bảng mới được tạo**.

[ĐỀ XUẤT] Không coi task là thay thế trọn vẹn DB cho đồ: task chỉ phù hợp metadata/ID ánh xạ khi đã có cơ chế sở hữu item bền. Không tự nhân bản `room_equipmentex` hoặc nhét companion ID vào X/Y đang dùng cho tọa độ; phải định nghĩa vị trí lưu mới và đồng bộ hai đầu (`S/KItemList.cpp:354–366`; `S/KPlayerDBFuns.cpp:1651–1653,895–897`).

## 4. NPC dùng kỹ năng môn phái và hạn chế vũ khí

[NGUỒN] `SetNpcSkill(npc,slot,skillId,level)` gọi skill list chung; SetNpcSkill kiểm số slot/ID/cấp và tra SkillManager, không có kiểm faction trong thân hàm. Do đó có đường gán skill môn phái hợp lệ cho kind_partner; không bị giới hạn vào thư mục `skill/partner`. Hàm ghi skill trước, chỉ trả TRUE cho aura ở cuối; **FALSE cuối hàm không đồng nghĩa skill thường chưa được gán**. Wrapper chỉ gọi SetAuraSkill khi TRUE (`S/ScriptFuns.cpp:11142–11154`; `S/KSkillList.cpp:64–111`).

[NGUỒN] `SetActiveSkill` nhận **chỉ số slot**, lấy ID/cấp từ list và cập nhật attack radius. `DoSkill` còn kiểm vùng, đang do_skill/do_hurt, cooldown và `CanCastSkill`; vì vậy không thể gọi slot rỗng hoặc chỉ set một ID rồi khẳng định chiêu chạy được (`S/KNpc.cpp:7046–7067,3609–3674`).

[NGUỒN] `CanCastSkill` kiểm quan hệ mục tiêu enemy/ally/self; khối `EqtLimit` và `HorseLimit` nằm hoàn toàn trong `if (Npc[nLauncher].IsPlayer())`. IsPlayer trên server yêu cầu kind_player và player index hợp lệ, nên kind_partner bỏ qua các kiểm vũ khí/ngựa này; Cost cũng trả TRUE ngay cho non-player. Đây là **hành vi source**, không có nghĩa đồ partner tự thỏa đúng luật môn phái (`S/KSkills.cpp:221–267,279–358`; `S/KNpc.cpp:15174–15180,6711–6714`). Muốn giữ luật vũ khí cho hảo hữu phải bổ sung đọc bộ đồ của chính companion, không dùng vũ khí của chủ.

[NGUỒN] Gán chiêu và gây sát thương là hai bước khác nhau: `KMissle` trả false khi launcher kind_partner và mục tiêu IsPlayer; vậy khả năng dùng AOE trong Tống Kim/PvP **chưa sẵn sàng** trên đường đạn này. Chưa kiểm hết chiêu state/melee/child-event để kết luận mọi dạng đều bị chặn hoặc đều chạy (`S/KMissle.cpp:1378–1380`; `S/KSkills.cpp:239–260`).

[BÁO CÁO] A-08a đã phân biệt attack radius với vùng AOE và số đạn với số mục tiêu; sử dụng bộ ánh xạ skill đã xác minh, không gán vai đơn/AOE chỉ theo tên môn phái (`JX1_OPS/REPORTS/A-08a-mon-phai-ky-nang.md:53–59`). Chưa chứng minh mọi skill, passive, hiệu ứng phụ hoặc animation của mọi template dùng được trên NPC.

## 5. Hook AI để chọn kỹ năng theo vai

| Điểm móc | Hiện tại [NGUỒN] | Thay đổi đề xuất, chưa triển khai |
| --- | --- | --- |
| Trước dispatch companion | RankFFId 99 vào ProcessCompanion, nhưng các guard AI trước đó có thể return (`S/KNpcAI.cpp:53–81`). | Giữ owner/slot hợp lệ, không gắn logic vào ProcessAIType01..06 vốn không phải đường tick partner này. |
| Xác định chủ và trạng thái | Tìm chủ bằng mã tên, ghi scalar, kiểm map/khoảng cách/FightMode (`S/KNpcAI.cpp:3294–3337`). | Kiểm companion ID + owner DWID/session, loại stale index; thêm chính sách chủ chết và formation bốn con trước khi tìm mục tiêu. |
| Chọn mục tiêu | Lấy địch gần nhất; địch cách >400 thì quay theo chủ (`S/KNpcAI.cpp:3291,3393–3403`). | Vai đơn ưu tiên boss/mục tiêu chủ; vai AOE chấm cụm địch, lọc camp/map/hoạt động; support chọn ally/self thay vì luôn enemy. |
| Chọn skill | Random slot 1..4, SetActiveSkill thất bại thì CommonActionCompanion (`S/KNpcAI.cpp:3405–3417`). | Thay đúng khối này bằng bảng vai → danh sách slot hợp lệ, xét cooldown, loại mục tiêu, tầm, trạng thái buff và luật vũ khí mới; có fallback chiêu cơ bản. |
| Phát lệnh trong FollowAttackCompanion | Chỉ kiểm region địch và distance <=m_CurrentAttackRadius rồi SendSerCommand(do_skill, active ID,-1,target). Đuổi địch ngoài tầm bị comment (`S/KNpcAI.cpp:2989–3007`). | Kiểm lại mục tiêu còn sống/cùng map/owner còn hợp lệ trước gửi, hỗ trợ point/self/ally theo kiểu skill; định nghĩa đuổi/kite/leash. Tham số juli hiện không có tác dụng trong phép so sánh đã comment. |

[ĐỀ XUẤT] Nên tách lựa chọn `target + skill slot` khỏi phát lệnh; engine vẫn quyết định cast thành công qua cooldown/CanCastSkill. Giới hạn bốn con/roster không biến chúng thành KPlayer trong tổ đội: AddTongBan tạo kind_partner, còn thiết kế yêu cầu party năm kể cả chủ; cần quản lý đội hình riêng và sửa các phép đếm/chia EXP/hoạt động theo companion ID, chưa chứng minh hệ party player gốc tự tính pet (`S/KNpcSet.cpp:877–890`; `S/KNpc.cpp:3673–3684`; `JX1_OPS/DESIGN/HAO-HUU-CUNG.md:8`).

## 6. Chủ chết, đổi map, offline và NPC chết

| Tình huống | Hành vi source / hệ quả nhiều slot |
| --- | --- |
| Chủ chết | Player death gọi script riêng hoặc global OnPlayerDeath. ProcessCompanion chỉ kiểm chủ tìm thấy, map/khoảng cách/FightMode; đoạn do_death/do_revive kiểm **địch**, không phải chủ. Chưa có chính sách trực tiếp “chủ chết thu tất cả” trong đoạn AI này; phải truy script/binary để chốt (`S/KNpc.cpp:2583–2587`; `S/KNpcAI.cpp:3294–3344`). |
| Chủ qua map cùng core hoặc xa >800 | Companion ChangeWorld tới map và tọa độ chủ rồi return. Không coi đó là hỗ trợ chuyển GS: nếu chủ không tìm thấy tại core thì vào nhánh xóa (`S/KNpcAI.cpp:3294–3317,3429–3446`). |
| Companion có `_lockMap>0` | Mỗi nhịp FRAME2TIME, xóa scalar/callback OnDeathOther **trước khi so map**, kể cả đang đúng map; khi lệch map thì remove. Đây là xung đột rõ với nhiều slot. AddTongBan mặc định lock=0 nhưng mẫu gm đặt lock map hiện tại (`S/KNpc.cpp:1442–1459`; `S/KNpcSet.cpp:890`; `G/script/item/gm.lua:378`). |
| Chủ offline/không tìm được mã tên | ProcessCompanion gỡ region/ref và NpcSet.Remove, return. Đoạn “phản bội”, kind_normal, lifetime 60 phía sau return không tới được; không có lưu roster tại nhánh này (`S/KNpcAI.cpp:3429–3465`). |
| Hết lifetime | Giảm thời gian, rank99 tìm chủ và đặt scalar=0 rồi remove NPC. Cần release riêng từng slot, không mất lựa chọn các con còn sống (`S/KNpc.cpp:1462–1463,1483–1513`). |
| Companion bị giết | Gọi NPC_PARTNER_SCRIPT OnDeath cho chủ khi tìm được, sau đó partner bị remove, không DoRevive như NPC thường (`S/KNpc.cpp:2600–2616,2638–2647,2671–2698`). |
| Callback khác nhau | Hằng NPC_PARTNER_SCRIPT trỏ global/partner.lua, cả ba callback hiện rỗng. Mẫu summon gán death/同伴死亡/tongyong.lua có SetTonBanNun(0)/DelNpc; không mặc định callback gán riêng thay thế hằng global trên đường death (`J/header/CoreUseNameDef.h:11`; `G/script/global/partner.lua:2–11`; `G/script/item/gm.lua:363`; `G/script/deadth/Í¬°éËÀÍö/tongyong.lua:4–15`). |
| Đăng nhập lại | Load được flag và item list; chưa thấy chuỗi khôi phục 10–15 bản ghi, tạo lại bốn active NPC và gắn đồ từng con. Không khôi phục DWID cũ vào phiên mới (`S/KPlayerDBFuns.cpp:678,895–897,1119`; `S/KNpc.cpp:181–183`; `L/S3DBInterface.h:41–51`). |

[ĐỀ XUẤT] Một hàm release theo owner + companion ID + DWID dùng chung cho death/lifetime/map/logout; lưu level/EXP/thân mật/đồ trước xóa thực thể theo chính sách đã chốt. Re-login chỉ phục hồi roster rồi cấp NPC mới; các tình huống reconnect, chuyển GS, chết đồng thời và slot bị tái sử dụng cần test riêng. Đề xuất này giải quyết các nhánh xóa/ghi scalar hiện có, chưa xác nhận giao dịch hoặc autosave runtime (`S/KNpc.cpp:1449,1505`; `S/KNpcAI.cpp:3303,3444`; `S/KPlayerDBFuns.cpp:1515,1651–1653`).

## Chưa kiểm

- MAX_NPC trong bộ nhớ của exe triển khai; tên server truyền vào core, bản cấu hình thực nạp/PAK, binary khớp source. 100000 là kết quả source + cấu hình gs001 rời, không phải phép đo runtime.
- Tải 4 con/người, CPU/AI/đồng bộ, client 256 NPC nhìn thấy, quota NPC/đạn khi spawn đông; không có benchmark hoặc build/test.
- Tất cả bản client Cocos và giao thức của chúng, thư viện đóng/PAK; bảng symbol ở trên chỉ đầy đủ trong phạm vi source/runtime rời đã ghi. Project khác có thể biên dịch backup/copy.
- Dải task ID thật sự còn trống; giới hạn role/task/item ở gateway/Goddess/SQL và ABI/header cuối cùng của bản dựng. Chưa chứng minh round-trip flag/item/roster qua DB, giới hạn 128 KiB phải được kiểm toàn chuỗi trước triển khai.
- Mọi skill môn phái trên từng NPC: animation, damage vật lý/vũ khí, aura/passive, buff đồng đội, child skill và PvP/Tống Kim. Chưa kiểm toàn bộ callsite NewCanCastSkill hoặc các hiệu ứng ngoài đường đã nối.
- Mọi death/login/logout/map script tùy biến, chuyển GS, tìm chủ trùng mã tên, callback có thực nạp không; không kết luận chắc pet còn đánh hay bị thu khi chủ chết.
- Chưa triển khai/schema migration, luật trang bị từng con, EXP/thân mật, chống trùng vật phẩm, party 1+4, cơ chế chọn vai và chính sách chết/reconnect. Những phần gắn [ĐỀ XUẤT] cần thiết kế/phê duyệt trong task tiếp theo.

## Kiểm chứng, lỗi công cụ và bàn giao

- Đối chiếu source có số dòng, phân biệt code hoạt động/comment/backup, so section cấu hình, tự đọc lại báo cáo; chỉ tài liệu được thay đổi. Không build/test/Lua compiler theo task.
- `rg : The term 'rg' is not recognized ...`: các lần gọi đầu trong cùng batch đều thất bại; chuyển sang Select-String/ReadAllLines, không cài công cụ. Đọc Markdown mặc định làm lỗi dấu và đầu ra gộp bị rút gọn: đọc UTF-8, thu hẹp các đoạn quyết định, dùng CP936 cho legacy. Không sử dụng chữ lỗi để suy chức năng.
- `Cannot find path 'D:\JX-wt\A-09\DESIGN\HAO-HUU-CUNG.md'`: tìm tại vị trí JX1_OPS đã có theo tài liệu nền và đọc được. Không sửa đường nguồn/task ngoài mục Kết quả.
- Đã xem diff từng file một lần và chạy `git diff --check`, không báo lỗi whitespace. Một lần stage đúng hai file thất bại; commit chưa chạy, chưa có SHA. **BỊ CHẶN – CHƯA PUSH.** Git metadata ngoài writable root; không nâng quyền, đổi ACL/config/credential hay dùng index thay thế. Không chạy push vì người dùng chỉ yêu cầu commit.

~~~text
git add -- JX1_OPS/REPORTS/A-09-dong-ban-nhieu-slot.md JX1_OPS/TASKS/A-09.md
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-09/index.lock': Permission denied
~~~

Giữ hai file local. PM dùng phiên có quyền ghi Git metadata, tại worktree/nhánh đã xác nhận, tiếp tục:

~~~text
git -C "D:\JX-wt\A-09" add -- JX1_OPS/REPORTS/A-09-dong-ban-nhieu-slot.md JX1_OPS/TASKS/A-09.md
git -C "D:\JX-wt\A-09" commit -m "A-09 Khao sat dong ban nhieu slot va luu roster"
~~~
