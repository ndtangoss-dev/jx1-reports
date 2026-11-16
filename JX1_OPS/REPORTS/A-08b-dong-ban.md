TÓM TẮT 1: Đồng bạn gốc là thực thể NPC/pet kiểu `kind_partner`, được tạo bằng `AddTongBan`; gắn với một người chơi qua `Partner._npcIndex/_npcDwid` và `m_TongBanNum`.
TÓM TẮT 2: Đồng bạn không phải người chơi online riêng; nó chiếm một ô trong pool NPC (`MAX_NPC`), còn người chơi vẫn ở pool `MAX_PLAYER`.
TÓM TẮT 3: AI theo chủ: cùng map thì bám theo, chủ bật chiến đấu thì tìm địch trong bán kính và đánh bằng skill; khác map thì chuyển tới chủ.
TÓM TẮT 4: Có nền skill, cấp kỹ năng, cấp/EXP và trang bị trong C++/Lua, nhưng phần EXP/cấp đồng bạn chưa thấy đường gọi hoàn chỉnh; không thấy cơ chế độ thân mật.
TÓM TẮT 5: Chết/offline/đổi map có nhiều nhánh xử lý khác nhau; callback death và script gán trong Lua lệch nhau, nên hành vi runtime cuối cùng chưa xác minh.

# A-08b – Đồng bạn (同伴)

Ngày kiểm tra: 2026-11-17. Phạm vi: đọc tĩnh các file runtime `gs\script\skill\partner\*`, `gs\Settings\maps\partner\*`, `gs\script\deadth\*`, mã C++ server `SwordOnline\SwordOnline\jxOnline\gameserver\Sources` và client `Client\Classes`. Không chạy exe, build, VM, SQL hoặc server.

## Worker kiểm tra trước khi làm

- Đã đọc `JX1_OPS/TASKS/A-08b.md` trước khi điều tra. Thư mục hiện tại `D:\JX-wt\A-08b` khớp `worktree`; nhánh `task/A-08b-codex` khớp `branch` trong task.
- Phạm vi ghi chỉ gồm `JX1_OPS/REPORTS/A-08b-dong-ban.md` và mục `Kết quả` của task. Nguồn `C:\Jx1CocoV3` chỉ đọc; không sửa source/runtime, không chạy exe, không kết nối VM/SQL/server.
- Đã đọc các nền được task yêu cầu: `JX1_OPS/REPORTS/A-03-kiem-ke-cau-hinh.md`, `JX1_OPS/REPORTS/D-01-bang-hoat-dong.md`, `D:\jx1-ops-wt\JX1_OPS\owner-inputs\08-HAO-HUU-CUNG-VA-LUA-TRAI.md` và `D:\jx1-ops-wt\JX1_OPS\DESIGN\HAO-HUU-CUNG.md`.
- File legacy có tên tiếng Trung hiển thị mojibake khi liệt kê; nội dung được đọc theo UTF-8 trước, rồi CP936/GBK khi cần. Kết luận dưới đây dựa trên token và số dòng trong nội dung, không dựa riêng vào tên hiển thị.

## Quy ước bằng chứng

Mọi kết luận hành vi là **[NGUỒN]**, chưa xác nhận runtime. `G/` = `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/`; `S/` = `D:/JX-build/src18/jxOnline/`; `C/` = `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes/`. Dẫn `gameserver/...` không có prefix cũng tính từ S; `gs/...` tính từ G bỏ phần `gs/`; `Client/Classes/...` tính từ C bỏ phần `Client/Classes/`. Số dòng bắt đầu từ 1, gồm dòng trống. Giữ nguyên tên vật lý mojibake để tra file; đường Hán tự bên trong Lua có thể không khớp tên vật lý trên Windows. Chỉ dùng bản src18 cho dẫn C++, chưa khẳng định giống bản canonical hay binary.

## Hệ thống gốc và loại thực thể

`LuaAddyabiao` chọn nhánh `nReg==2` để gọi `NpcSet.AddTongBan` (`gameserver/Sources/Core/Src/ScriptFuns.cpp:12997-13035`). `AddTongBan` kiểm tra chủ phải là NPC người chơi, tạo một server NPC, đặt `m_Kind = kind_partner`, gắn `m_GuiShuDwid` với DWID của chủ và lưu chỉ số chủ trong `Partner._npcIndex` (`gameserver/Sources/Core/Src/KNpcSet.cpp:858-893`). Vì vậy đồng bạn gốc là NPC/pet server thuộc người chơi, không phải một player/account online.

Header client tách `kind_partner` khỏi `kind_player` (`C/gamecore/GameDataDef.h:358-367`). Pool người chơi được cấp bởi `KPlayerSet` với `MAX_PLAYER` (`gameserver/Sources/Core/Src/KPlayerSet.cpp:43-51`), còn NPC được cấp bằng `FindFreeNpcSet`; khi hết ô NPC thì `AddServerNpcB` báo “NPC đã đầy” và trả 0 (`gameserver/Sources/Core/Src/KNpcSet.cpp:902-916`). Do đó đồng bạn không chiếm một chỗ online người chơi, nhưng chiếm một ô NPC; giới hạn đồng bạn thực tế là số NPC còn trống và cờ một đồng bạn của mỗi chủ, không phải một con số partner riêng được thấy trong source. Server dùng `MAX_NPC=nMaxNpcCount`; client dùng 256 (`S/gameserver/Sources/Core/Src/KNpc.h:24-29`). Chưa đọc giá trị cấu hình đang có hiệu lực.

## Sinh ra, sở hữu và giới hạn

Lua mẫu GM `OPENTONGBAN` chặn nếu `GetTonBanNun()>0`, chọn template/level/series, gọi `Addyabiao(...,2)`, gán script chết, đặt `m_TongBanNum` về DWID NPC, camp, thời gian sống 7200 giây, bốn skill và khóa map (`gs/script/item/gm.lua:345-386`). API `GetTonBanNun`/`SetTonBanNun` đọc/ghi trực tiếp `Npc[player].m_TongBanNum` (`gameserver/Sources/Core/Src/ScriptFuns.cpp:12860-12936`). C++ cũng kiểm tra `nRindexid` là player trong `AddTongBan` (`gameserver/Sources/Core/Src/KNpcSet.cpp:861-869`). Đây là mô hình mỗi chủ giữ một DWID NPC đang gọi; không có bằng chứng về nhiều partner đồng thời cho một player trong nhánh này.

Cờ tồn tại/được phép gọi được lưu cùng dữ liệu nhân vật: `IsCreatTongBan` được nạp từ `pRoleData->BaseInfo.isCreatTongBan` và ghi ngược khi lưu (`gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:678,1513-1516`). `cpartnercode` dễ gây nhầm: tại `S/gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:1490-1497` nó nhận tên đổi của nhân vật, không phải bằng chứng lưu partner; struct `TongBanInfo` gồm năm số trong `S/gameserver/Lib/S3DBInterface.h:41-51` bị comment. `m_TongBanNum` được khởi tạo 0 dưới chú thích biến tạm không vào DB (`S/gameserver/Sources/Core/Src/KNpc.cpp:180-183`); getter/setter Lua đọc/ghi trường C++ này, không phải biến Lua lưu bền. Chỉ xác nhận cờ `IsCreatTongBan` được serialize vào dữ liệu role; chưa xác minh round-trip DB thực tế.

## Chiến đấu theo người chơi

AI server gọi `ProcessCompanion` khi `m_btRankFFId==99` (`gameserver/Sources/Core/Src/KNpcAI.cpp:53-82,3282-3289`). Hàm tìm chủ bằng tên/mã, cập nhật `m_TongBanNum`, nếu khác map hoặc quá xa thì `ChangeWorld` về map/toạ độ chủ; nếu chủ không chiến đấu hoặc partner cách chủ hơn 400 thì `FollowCompanion` (`gameserver/Sources/Core/Src/KNpcAI.cpp:3294-3337`). Khi chủ chiến đấu, partner lấy địch gần nhất, chọn skill 1–4 và gọi `FollowAttackCompanion` (`gameserver/Sources/Core/Src/KNpcAI.cpp:3393-3417`). Hàm follow đứng khi cách chủ dưới 180, ngoài ra `do_run` tới chủ (`S/gameserver/Sources/Core/Src/KNpcAI.cpp:2941-2959`). `FollowAttackCompanion` chỉ gửi `do_skill` khi trong `m_CurrentAttackRadius`; đoạn đuổi địch ngoài tầm bị comment (`S/gameserver/Sources/Core/Src/KNpcAI.cpp:2989-3007`). Đường va chạm đạn còn trả false khi partner đánh player: không được suy rằng có thể dùng ngay cho PvP/Tống Kim (`S/gameserver/Sources/Core/Src/KMissle.cpp:1378-1380`). Client cũng có các nhánh `kind_partner`, AI theo chủ và script chết partner (`Client/Classes/gamecore/KNpcAI.cpp:3530-3563,3928-3935`).

## Skill, cấp, EXP và trang bị

Thư mục `skill/partner` có 95 file: 10 file mỗi hệ `earth/fire/gold/water/wood`, 5 file `resistance`, 40 file `expansion`; các file skill định nghĩa bảng `SKILLS`, hàm `SkillExpFunc` và dữ liệu mức skill (ví dụ `G/script/skill/partner/earth/³¤ºÓÂäÈÕ.lua:1-37,181-212`). Các file `_升级.lua` gọi `PARTNER_GetLevel` và `PARTNER_AddSkill` khi skill đạt điều kiện (`G/script/skill/partner/earth/³¤ºÓÂäÈÕ_Éý¼¶.lua:1-10`; cùng kiểu callback trong bốn hệ còn lại). Lua GM truyền cấp ngẫu nhiên 85–95 vào mẫu NPC (`G/script/item/gm.lua:357-361`); `AddServerNpcB` lấy cấp từ `LOWORD` và gọi `Npc.Load` (`S/gameserver/Sources/Core/Src/KNpcSet.cpp:929-936`). Đây là cấp khởi tạo, chưa chứng minh tự luyện cấp. C++ có struct `CFuMoInfo` với `nNowLevel`, `nNowExp`, `nNpcSkill`, `nSkillLevel` (`gameserver/Sources/Core/Src/KNpc.h:170-181`), nhưng `KPartnerSkill.cpp` hiện chỉ là phần bị comment (`gameserver/Sources/Core/Src/KPartnerSkill.cpp:1-32`). Tôi không thấy trong phạm vi đã đọc API `PARTNER_GetLevel`/`PARTNER_AddSkill` được định nghĩa ở C++ hoặc một đường gọi tăng `nNowExp` cho level partner; vì vậy chỉ có thể kết luận nền dữ liệu/skill tồn tại, chưa kết luận hệ thống luyện cấp/EXP đang chạy. `nNowLevel/nNowExp` thuộc struct thần tướng `CFuMoInfo`, chưa chứng minh đó là tăng trưởng của NPC đang theo chủ. Đường lấy `ifumo` từ role cũng bị comment (`S/gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:722-728`). Luồng damage tích EXP chỉ ghi nhận attacker `kind_player`, rồi bộ phân EXP gọi `Player.AddExp`; chưa thấy partner nhận EXP riêng (`S/gameserver/Sources/Core/Src/KNpc.cpp:5680-5702`; `S/gameserver/Sources/Core/Src/KNpcDeathCalcExp.cpp:190,215`).

Trang bị có đường C++ riêng: `TonEquip` lấy partner đang triệu hồi từ `m_TongBanNum`, từ chối nếu chưa gọi, rồi áp dụng magic item lên NPC partner (`gameserver/Sources/Core/Src/KItemList.cpp:1374-1394,1451-1460`). Client/server có kho `room_equipmentex`/`pos_equiproomex` cho “đồng bạn” và điều kiện `magic_item_needtongban` (`Client/Classes/gamecore/GameDataDef.h:250,272`; `Client/Classes/gamecore/KItemList.cpp:1026-1062`; server `S/gameserver/Sources/Core/Src/KMagicAttrib.h:60`). Danh sách vật phẩm của người chơi được serialize trong `S/gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:1620-1667`; chưa thấy một bảng partner equipment độc lập ngoài item list này.

## Dữ liệu maps/partner và các phần legacy

Đã đọc 11 bảng `G/Settings/maps/partner`: tất cả chỉ có hai cột `Xpos`, `Ypos`; dòng 2–6 là tọa độ, không phải thuộc tính/EXP/giới hạn đồng bạn. Cụ thể `enter.txt:1-23`, `exit.txt:1-260`, `middle.txt:1-100`, `northeast_1.txt:1-55`, `northeast_2.txt:1-74`, `northwest_1.txt:1-66`, `northwest_2.txt:1-57`, `southeast_1.txt:1-79`, `southeast_2.txt:1-82`, `southwest_1.txt:1-76`, `southwest_2.txt:1-65`. Tìm literal đường `maps/partner` với cả hai kiểu dấu phân cách trong Lua gs và C++ src18/client không có kết quả; chưa biết luồng nạp động/mục đích map. Không dùng các bảng tọa độ để suy ra số partner.

`S/gameserver/Sources/Core/Src/KPlayerPartner.cpp:3` đặt class dưới `#ifdef _PARTNER`; header client-core có enum cho kỹ năng/task/điều khiển partner (`S/gameserver/include/client_core/coreshell.h:585-598`), nhưng đây chưa phải bằng chứng triển khai tính năng có hiệu lực. Tìm hai tên API `PARTNER_GetLevel`/`PARTNER_AddSkill` trong `.cpp/.h` src18 và client không thấy định nghĩa; chỉ Lua nâng skill gọi. Tìm `nNowLevel/nNowExp` chỉ thấy khai báo trong KNpc.h của server/client, chưa thấy phép tăng. Đây là bằng chứng tìm kiếm có giới hạn, không khẳng định binary/thư viện ngoài không hỗ trợ.

## Chết, đổi map, offline

Script vật lý `G/script/deadth/Í¬°éËÀÍö/tongyong.lua:4-15` có `OnDeath` gọi `SetTonBanNun(0)` và `DelNpc`; `OnDeathTar` chỉ `DelNpc`. Script chung `G/script/deadth/tongyong.lua:4-8` chỉ `DelNpc`. C++ khi partner chết gọi `NPC_PARTNER_SCRIPT` callback `OnDeath` cho chủ nếu chủ còn online (`gameserver/Sources/Core/Src/KNpc.cpp:2590-2616,2638-2647`), sau đó nhánh partner không hồi sinh mà remove khỏi region/NPC set (`gameserver/Sources/Core/Src/KNpc.cpp:2671-2698`). Khi hết lifetime, partner bị xoá và `m_TongBanNum` của chủ được đặt về 0 (`gameserver/Sources/Core/Src/KNpc.cpp:1462-1514`); mẫu Lua đặt 7200 giây (`gs/script/item/gm.lua:369`).

Khi partner bị khóa map và phát hiện đang ở map khác, C++ gọi `OnDeathOther`, xoá khỏi region và remove (`gameserver/Sources/Core/Src/KNpc.cpp:1442-1459`). Khi chủ logout/không còn NPC player, `ProcessCompanion` xoá partner khỏi region/NPC set (`gameserver/Sources/Core/Src/KNpcAI.cpp:3428-3446`). Đoạn chuyển thành NPC thường “叛变的(宠物)” và lifetime 60 nằm sau `return` vô điều kiện ở dòng 3446, vì thế không tới được trên nhánh này; không coi đó là hành vi offline đang chạy (`S/gameserver/Sources/Core/Src/KNpcAI.cpp:3428-3465`).

Có một lệch quan trọng: header C++ định nghĩa `NPC_PARTNER_SCRIPT` là `script/global/partner.lua` (`S/header/CoreUseNameDef.h:11`), file này có các callback rỗng (`gs/script/global/partner.lua:1-12`), trong khi Lua triệu hồi thường gán `script/deadth/同伴死亡/tongyong.lua` (`gs/script/item/gm.lua:361-364`). Vì vậy không thể khẳng định callback death nào được exe thực tế dùng nếu chưa kiểm đúng gói/PAK và runtime.

Khi chủ chết, đoạn player death chỉ chạy death-script riêng hoặc `OnPlayerDeath` toàn cục (`S/gameserver/Sources/Core/Src/KNpc.cpp:2583-2587`); `ProcessCompanion` kiểm chủ tồn tại/map/FightMode chứ chưa có nhánh chủ `do_death` trực tiếp trong phần đã đọc (`S/gameserver/Sources/Core/Src/KNpcAI.cpp:3294-3344`). Chưa đủ bằng chứng kết luận partner biến mất hay còn đánh trong lúc chủ chết. Cũng cần lưu ý khi `_lockMap>0`, việc xóa `m_TongBanNum`/gọi callback xảy ra trước phép so map, mỗi giây ngay cả chưa chuyển map (`S/gameserver/Sources/Core/Src/KNpc.cpp:1442-1459`).

## Độ thân mật

Không tìm thấy biến, trường DB, API Lua/C++ hoặc script partner triển khai “độ thân mật”/intimacy trong tập source đã đọc. Các lần xuất hiện “亲密” chỉ là câu thoại tình cảm bị comment trong script NPC (`G/script/Î÷ÄÏ±±Çø/½­½ò´å/Ö°ÄÜnpc/ÔÂÀÏ.lua:635,658,676`), không liên quan partner. Yêu cầu nướng cá tăng thân mật trong `owner-inputs/08` vì vậy chưa có bằng chứng hệ thống gốc.

## Chưa kiểm

- Chưa chạy Lua/compiler, exe hoặc VM; chưa xác nhận bản PAK mà server thực tế nạp, nên chưa biết đường dẫn Hán tự và callback `partner.lua`/`tongyong.lua` nào có hiệu lực.
- Chưa xác minh runtime có nối các API `PARTNER_GetLevel`, `PARTNER_AddSkill`, `nNowExp` vào luồng EXP; chưa xác minh cách lưu/khôi phục đầy đủ level, skill practice, task value và item partner qua roledb.
- Chưa xác nhận độ thân mật của partner. Lửa trại/nướng cá/EXP theo giây không thuộc phân tích triển khai của A-08b; không kết luận chúng có hay không từ tập file partner.
- Chưa đo giới hạn `MAX_NPC` thực tế của build, số partner đồng thời trên map, hành vi khi chủ chết, chuyển map bằng client, timeout 7200 giây và khả năng trở lại game sau offline.
- Nguồn có bản backup/legacy và tên file GBK; cần đối chiếu đúng binary/PAK trước khi dùng kết luận này để thiết kế thay đổi.

## Kiểm chứng và lỗi thao tác

Đã tự đọc lại báo cáo, đối chiếu dẫn chứng quan trọng và sửa các chỗ dễ nhầm: tổng là 95 file skill; `cpartnercode` phục vụ đổi tên nhân vật; đoạn phản bội offline không tới được; di chuyển đuổi địch ngoài tầm bị comment. Không build/test theo task. `rg` không được nhận diện trong PowerShell; chuyển sang Node filesystem trong phiên, không tạo script phụ. Lần đầu PowerShell đọc Markdown theo encoding mặc định hiển thị lỗi dấu; đọc lại UTF-8 thành công. Không sửa dữ liệu nguồn.

Trạng thái cuối: **PARTIAL — nghiên cứu DONE, commit BLOCKED. BỊ CHẶN – CHƯA PUSH.** Một lần `git add -- JX1_OPS/REPORTS/A-08b-dong-ban.md JX1_OPS/TASKS/A-08b.md` thất bại (exit 128):

~~~text
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-08b/index.lock': Permission denied
~~~

Không stage/commit được, chưa có SHA. Metadata Git ngoài writable root, không nâng quyền/đổi ACL/config. Giữ hai file local. PM tiếp tục bằng `git add` đúng hai đường trên rồi `git commit -m "A-08b Phan tich he thong dong ban goc"` trên `task/A-08b-codex`. Chưa push vì người dùng chỉ yêu cầu commit.
