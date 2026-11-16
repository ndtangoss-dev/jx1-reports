TÓM TẮT 1: Boss xanh được nhận diện bằng GoldType 2–4; nhánh ngẫu nhiên chọn 2–4, client tô tên RGB 100,100,255 (S/KNpcGold.cpp:326–350; C/KNpc.cpp:5342–5343).
TÓM TẮT 2: Điểm gắn khi chết là KNpc::OnDeath trước RecoverBackData; OnGoldDeath hiện có thân hoàn toàn comment, nhánh đồng bạn kết liễu không gọi callback này (S/KNpc.cpp:2590–2635,2668; G/script/global/golddeath.lua:110–431).
TÓM TẮT 3: Lửa mẫu là NPC 2078, skill 1705; sống 1800/3600 giây, có nhánh kéo dài; 120 giây là yêu cầu mới (G/script/item/huozhong.lua:71–83; G/script/task/gouhuo.lua:27–32; N:44–47,102).
TÓM TẮT 4: Có effect EXP cố định và callback theo GouHouTime=10, nhưng Skills.txt rời thiếu ID 1705/1706; chưa chứng minh aura gần lửa, x2 đội hoặc 0,5%/giây hoạt động (K:8; S/KNpc.cpp:1801–1817; G/Settings/gamesetting_gs001.ini:503; E01).
TÓM TẮT 5: Nướng cá chưa có luồng kiểm cá trong túi và tăng thân mật; chỉ có callback giao đồ bị đóng và ăn cá nhận EXP (F:48–91; G/script/item/caoyu.lua:3–21); toàn bộ khảo sát là tĩnh, xem Chưa kiểm.

# A-10 — Lửa trại từ boss tinh anh

Ngày khảo sát: 17/11/2026. Nội dung khảo sát: **DONE**; trạng thái bàn giao: **PARTIAL — commit BLOCKED**. Đây là bản đồ tích hợp, chưa triển khai tính năng và không xác nhận runtime từ source.

## Worker kiểm tra trước khi làm

- Đã đọc task trước; `Get-Location` = `D:\JX-wt\A-10`, `git branch --show-current` = `task/A-10-codex`, `git status --short` rỗng. Khớp `JX1_OPS/TASKS/A-10.md:7–8`.
- Chỉ tạo báo cáo trong `vung_file`; cập nhật mục Kết quả của chính task theo yêu cầu trực tiếp của người dùng. Cây `C:\Jx1CocoV3` chỉ đọc. Không chạy exe/build/test game, không kết nối VM/SQL/server, không ghi bí mật (task:14–18,23–28).
- Đã đối chiếu các báo cáo A-08a..d, tập trung A-08c và A-08d; không lặp kiểm kê toàn repository. Tài liệu thiết kế/owner-inputs không có tại các đường tương ứng trong worktree này; đọc bản có sẵn tại `D:\jx1-ops-wt\JX1_OPS` theo đường dẫn trong báo cáo nền, chỉ đọc.
- Yêu cầu boss xanh, x2 cùng party, 0,5% EXP cấp hiện tại/giây, cá trong người → nướng → tăng thân mật nằm ở `O:3`; 120 giây và cấu hình INI nằm ở `D:24–26`. Ý nghĩa x2 vẫn được chính bản nháp để mở; không tự chốt thành hành vi có sẵn (`D:24`).

## Quy ước nguồn

| Ký hiệu | Gốc/đường dẫn |
| --- | --- |
| `S/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\` |
| `G/` | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\` |
| `C/` | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\` |
| `K` | `G/script/skill/special/óô»ð.lua` (tên logic `篝火.lua`) |
| `N` | `G/script/Á½ºþÇø/npc/óô»ð.lua` (tên logic `两湖区/npc/篝火.lua`) |
| `F` | `G/script/Á½ºþÇø/npc/¿¾Óã.lua` (tên logic `两湖区/npc/烤鱼.lua`) |
| `D` | `D:/jx1-ops-wt/JX1_OPS/DESIGN/HAO-HUU-CUNG.md` |
| `O` | `D:/jx1-ops-wt/JX1_OPS/owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md` |

Số dòng vật lý từ 1, giữ dòng trống. Markdown/client đọc UTF-8; C++/Lua legacy đọc CP936/GBK, riêng goldacition.lua và golddeath.lua đối chiếu UTF-8. Lua có cả byte Việt legacy nên không dùng chữ Việt hiển thị sai để suy chức năng; kết luận dựa symbol và số. Giữ nguyên tên vật lý mojibake K/N/F; chưa xác nhận loader nối được tên đó với đường Hán tự trong SetNpcScript (`G/script/item/huozhong.lua:83`; `JX1_OPS/REPORTS/A-08c-lua-trai-nuong-ca.md:21–35`).

## Boss xanh: nơi sinh và nơi chết

| Điểm | Bằng chứng tĩnh và ý nghĩa tích hợp |
| --- | --- |
| Nhận diện | `GetGoldType()` trả 0 khi chưa `m_nIsGolding`; setter nhận type 1..16. Điều kiện đề xuất cho boss xanh là `kind_normal` và type từ 2 đến 4, không dùng tên/màu chuỗi để nhận diện (`S/KNpcGold.cpp:479–498`; `S/KNpc.cpp:6963–6965`; `C/KNpc.cpp:5342–5343`). |
| Sinh loại ngẫu nhiên | `RandChangeGold` đọc khóa `<MapID>_AutoGoldenNpc`, so ngẫu nhiên với nMapAutoGoldNpcRank; nhánh bGold=1 chọn `GetRandomNumber(2,4)` ở cả hai vế. Nhánh BossType>0 gán type được truyền. Không suy tỷ lệ spawn chính xác từ tên biến (`S/KNpcGold.cpp:233–255,326–350`). |
| Điểm gọi lúc tạo/nạp | Nhánh kind_normal gọi `m_cGold.RandChangeGold(1,nBoss,nSubWorld)`; KNpcSet còn có đường gọi khi khóa AutoGoldenNpc âm và type hiện tại ≤0 (`S/KNpc.cpp:6961–6965`; `S/KNpcSet.cpp:620–626`). |
| Điểm gọi khi tái xuất | Khi kind_normal, xóa bộ tính EXP và có thể RandChangeGold lại nếu không m_IsNoCreatGoldNpc. Đây là ứng viên nếu chọn sinh lửa lúc boss xuất hiện; cần chống cùng NPC bị xử lý ở nhiều điểm gọi (`S/KNpc.cpp:13941–13947`). |
| Callback chết do người chơi | Sau WaitForFrame, khi kẻ kết liễu là player, có nIdx và nạn nhân không phải partner/dialoger: gọi `golddeath.lua/OnGoldDeath`, rồi action script riêng `OnDeath`. Đây là điểm móc, chưa có lệnh tạo lửa ở khối C++ đó (`S/KNpc.cpp:2571–2575,2590–2624`). |
| Callback chung hiện tại | Đọc toàn đoạn 110–431: bỏ dòng trống và dòng bắt đầu `--` chỉ còn khai báo hàm và end. Vì vậy thân OnGoldDeath hiện không sinh lửa; cả GetPos/GetNpcSettings lấy boss type đều bị comment (`G/script/global/golddeath.lua:110–126,418–431`). |
| Đồng bạn kết liễu | Nhánh kẻ kết liễu kind_partner tìm chủ rồi gọi `NPC_PARTNER_SCRIPT/OnDeath`; không đi qua OnGoldDeath ở nhánh player. Chỉ thêm Lua vào OnGoldDeath sẽ bỏ sót đường này (`S/KNpc.cpp:2627–2635`). |
| Trước mất dữ liệu boss | Callback chết nằm trước `m_cGold.RecoverBackData()` và đoạn DoRevive/xóa NPC. Phải chụp type/vị trí/định danh trước khôi phục, không dùng type sau đó để quyết định (`S/KNpc.cpp:2620–2623,2657–2687`). |

**Đề xuất, chưa sửa:** chọn một thời điểm sinh lửa (chết hoặc xuất hiện), không gắn đồng thời cả hai. Nếu chọn chết, dùng một hàm chung cho player và partner kết liễu, giữ liên kết chủ hảo hữu; lọc type 2..4 trước khôi phục dữ liệu, ghi nhận một lần cho mỗi vòng đời NPC. Lua có thể lấy type bằng giá trị trả thứ 4 của `GetNpcSettings(nNpcIdx)`; `GetPos(nNpcIdx)` trả tọa độ MPS và map ID ở giá trị thứ 3. Đổi map ID thành subworld index khi AddNpc, tránh coi map ID là index (`S/ScriptFuns.cpp:19436–19453,7031–7042`; `G/script/item/huozhong.lua:75–76`). Luật chống trùng và kết liễu bởi môi trường chưa được triển khai/kiểm thử.

## Tạo đối tượng lửa và giữ đúng 120 giây

Mẫu có sẵn dùng `AddNpc(2078,90,subworldIndex,x,y,...)`, sau khi index >0 mới gán thời hạn, ActiveForever, series, skill 1705 cấp 50 và script tương tác. Item lấy vị trí **người dùng**, đổi `(x+1)*32,(y+1)*32`; nếu sinh tại xác boss phải dùng vị trí boss và thống nhất đơn vị, không sao chép phép đổi tọa độ này vào kết quả GetPos MPS (`G/script/item/huozhong.lua:45,67–83`; `S/ScriptFuns.cpp:7035–7042`). Đây là NPC lửa, không phải bằng chứng có một đối tượng map độc lập hay asset đã hiển thị đúng.

Item gốc chặn state 1705/1706, vùng cấm và trạng thái chiến đấu, nên không gọi nguyên main của item từ death hook: luật này có thể ngăn lửa ngay tại nơi boss chiến đấu. Cần tách phần spawn dùng chung và luật vùng được duyệt; trong phạm vi này chỉ đề xuất (`G/script/item/huozhong.lua:35–65,74–83`).

| Thời hạn gốc | Điểm cần chú ý khi triển khai luật 120 giây |
| --- | --- |
| Item: 1800 giây; task: 3600 giây | Với nhánh lửa boss mới, điểm gán là `SetNpcLiveTime(newIndex,120,0,0)` sau AddNpc thành công; chưa áp dụng, không sửa toàn bộ lửa sự kiện (`G/script/item/huozhong.lua:77–83`; `G/script/task/gouhuo.lua:27–32`; `D:24`). |
| API và đếm thời gian | LuaSetNpcLiveTime ghi thẳng m_GameliveTime; KNpc giảm khi game-time chia hết FRAME2TIME và có nhánh xóa lúc hết hạn. 120 là số giây theo nhịp game, chưa đo giây thật dưới tải (`S/ScriptFuns.cpp:21619–21650`; `S/KNpc.cpp:1442,1462–1463,1483–1487,1533–1552`). |
| Gia hạn có sẵn | JIHUO đặt 5400 giây và đổi skill 1706; GOUHUO cộng nNum*60 giây. Phải chặn/tách các callback này trên lửa boss nếu 120 là trần tuyệt đối; chỉ đổi literal lúc spawn chưa đủ (`N:44–47,95–108`). |
| Tồn dư effect | m_ExpState có thời hạn riêng từ addexp_v. Không mặc định xóa NPC lửa lập tức xóa buff; lượt cấp EXP phải kiểm hạn lửa, khoảng cách và liên kết còn hợp lệ (`S/KNpcAttribModify.cpp:3106–3113`; `S/KNpc.cpp:1801–1817`). |

## EXP theo timer, người gần lửa và tổ đội

**Đường hiện có:** K/gouhuo.addexp_v ghi lượng cố định theo cấp skill: 5000 ở cấp 1, 10400 ở cấp 30, 15000 ở cấp 50; hai tham số sau là 18*5. KNpcAttribModify chép ba giá trị vào m_ExpState và đặt nTime bằng nValue[1]*2. Vòng KNpc chỉ xử lý player có lượng và thời hạn dương; điều kiện modulo là `m_LoopFrames % (nTimeval*18)`, với nTimeval lấy từ NpcInfo, được nạp bằng GouHouTime (mặc định 90, file gs001 đặt 10). Khi m_IsDoing==0 mới gọi OnDoAcition → AddOwnExp. Đây là chu kỳ ứng viên 10 giây game, không phải bằng chứng +0,5% mỗi giây (`K:8`; `S/KNpcAttribModify.cpp:3106–3113`; `S/KNpc.cpp:1801–1817`; `S/KGameglobalSet.cpp:88`; `G/Settings/gamesetting_gs001.ini:503`; `G/script/global/goldacition.lua:7–15`).

**E01 — thiếu liên kết skill:** đã đọc header Skills.txt, cột SkillId có index 1 (đếm từ 0), duyệt 1720 dòng dữ liệu: không có ID 1705/1706, không có gouhuo/addexp_v/篝火 trong bảng rời. Kết quả phù hợp A-08c E02. Vì vậy chưa nối được `NPC lửa → aura 1705/1706 → addexp_v → người gần lửa`; chưa xác định bán kính, lọc party hay ai thực nhận buff. Không dùng bán kính chia EXP tổ đội làm bán kính lửa (`G/Settings/Skills.txt:1–1721`; `G/script/item/huozhong.lua:82`; `JX1_OPS/REPORTS/A-08c-lua-trai-nuong-ca.md:34,58–67`).

**Chia tổ đội hiện có:** AddOwnExp chỉ cấp cho KPlayer hiện tại qua DirectAddExp, không duyệt đội. AddExp(exp,level,1) gọi KPlayer::AddExp, xét thành viên cùng subworld, khoảng cách tối đa 768 từ người được gọi API; công thức k=100+15*N rồi chia theo tỷ lệ cấp. Với 5 người cùng cấp, mỗi người nhận đầu vào 35% trước hệ số AddSelfExp, tổng 175%; không phải mỗi người x2. Mảng đội dùng Player index, không tự bao gồm hảo hữu NPC (`S/ScriptFuns.cpp:15888–15918`; `S/KPlayer.cpp:63,2948–3056`; đối chiếu `JX1_OPS/REPORTS/A-08d-kinh-nghiem.md:53–57`).

**Điểm gắn đề xuất cho 0,5%/giây:** phần quyết định cấp thưởng có thể tách từ OnDoAcition, nhưng phải lọc riêng loại effect lửa boss, không đổi thưởng của mọi người đang dùng callback chung. Mỗi lượt kiểm lửa còn sống, cùng map, trong bán kính được chốt, điều kiện đội và chống nhận trùng; tính riêng từng người `floor(GetNextExp()/200)` theo ngưỡng cấp **hiện tại**, không theo GetExp hoặc lượng còn thiếu. API GetNextExp trả m_nNextLevelExp; DirectAddExp lên cấp gọi LevelUp đặt EXP về 0, nên cần xử lý phần vượt ngưỡng và trần cấp trước khi triển khai. Phép floor ở cấp thấp cần chính sách giữ phần lẻ (`G/script/global/goldacition.lua:7–15`; `S/ScriptFuns.cpp:15862–15884,15908–15918`; `S/KPlayer.cpp:3232–3273`; `O:3`).

**Nhịp 1 giây:** thay GouHouTime toàn cục thành 1 ảnh hưởng mọi effect dùng cùng vòng, nên đề xuất timer riêng hoặc bộ điều phối cho lửa boss. Timer người chơi có SetTimer(interval,id), mốc theo game-time và tự lặp; 18 tick/giây là quy ước source. Mỗi lần SetTimer ghi đè interval/id, cần phối hợp timer khác và cấp ID trong TimerTask.txt; chưa tạo timer mới (`S/ScriptFuns.cpp:5473–5480`; `S/KTaskFuns.h:54–65`; `S/KTaskFuns.cpp:118–130`; `JX1_OPS/REPORTS/A-08d-kinh-nghiem.md:79–89`).

**Điểm gắn x2 cần quyết định:** nếu x2 lượng EXP lửa mỗi giây, nhân 2 vào grant riêng sau kiểm điều kiện đội; nếu x2 EXP đánh quái trong vùng, cần cơ chế trạng thái riêng tại AddSelfExp và hoàn nguyên khi rời/hết lửa. Hiện AddSelfExp có ServerExp+mission27 và cờ m_CurrentUpExp nhân 2, nhưng DirectAddExp không đi qua đó. Không dùng cờ có sẵn như bằng chứng x2 party và không ghi đè trạng thái x2 vật phẩm (`S/KPlayer.cpp:3113–3142,3232–3250`; `D:24`). 120 lượt ×0,5%=60% chỉ là phép tính khi ngưỡng cấp cố định, đủ mọi lượt và không làm tròn; nếu nhân grant lên 2 thì là 120% cùng điều kiện, chưa phải tổng EXP runtime.

## Cá trong túi, nướng và biến thân mật

ID cá có trong bảng câu cá: 192–198, mực 200, tôm 201; callback câu cá cấp item genre 4 khi trúng. Đây là ứng viên để lập whitelist cá, chưa chứng minh tất cả item đó có trong túi người chơi hay được gán script ăn nào (`G/script/tnlteam/cauca/lib_huyhoang.lua:30–38`; `G/script/tnlteam/cauca/quahuyhoang.lua:115–122`; `JX1_OPS/REPORTS/A-08c-lua-trai-nuong-ca.md:73–91`).

NPC nướng F/ZHUYU chỉ Talk; Give mở giao diện ZHUYUA bị comment. Thân callback cũ kiểm genre 4/detail 408 (củi), không phải whitelist cá; DelIdItem nằm ngoài điều kiện, có thể xóa cả vật phẩm sai khi callback được gọi. Không có lệnh tăng biến thân mật trong toàn thân 53–91. Nhánh caoyu khác chỉ kiểm cấp >=60, AddOwnExp ngẫu nhiên 4000–10000 và JIANGLI; xóa item bị comment. Vì vậy chưa có luồng đang bật “có cá trong túi → tiêu hao cá → tăng thân mật” (`F:48–91`; `G/script/item/caoyu.lua:3–21`).

**Đề xuất, chưa sửa:** thêm kiểm đúng cá/số stack trong inventory ngay trước tiêu hao; chỉ sau tiêu hao thành công mới tăng thân mật cho đúng hảo hữu thuộc chủ. Cần định danh hảo hữu, trường lưu bền, giới hạn thân mật và công thức ảnh hưởng EXP riêng; không dùng m_nExp người chơi hay bộ đếm củi làm thân mật. Khảo sát đồng bạn A-08b chưa tìm được API/trường thân mật trong tập đã đọc; kết luận giới hạn ở tập đó, không phủ định toàn bộ PAK/source khác (`F:67–91`; `JX1_OPS/REPORTS/A-08b-dong-ban.md:60–62`; `O:3`).

## Chưa kiểm

- Binary gs/client khớp source; ưu tiên đĩa/PAK, skill 1705/1706 ở archive/PAK, template 2078 và asset lửa thực tế; loader tên Hán tự/mojibake. Chưa khẳng định aura hay bán kính nhận EXP hoạt động (E01).
- Toàn bộ action/death script riêng, mọi bản đồ/boss spawn; nhánh môi trường/partner kết liễu, bảo đảm callback chỉ một lần mỗi vòng đời; mối liên hệ drop owner và đội được hưởng.
- Ý nghĩa x2, thời điểm xuất hiện/chết, bán kính lửa, số người tối thiểu, người ngoài đội, hảo hữu NPC có tính slot đội/hưởng EXP, chết/rời map/rời đội/đăng xuất; các luật này chưa chốt hoặc chưa kiểm runtime.
- 120 lượt chính xác, thời điểm lượt đầu/cuối, lag, buff còn sau xóa lửa, nhiều lửa chồng nhau, cooldown/trần ngày; không công bố đã chống lạm dụng.
- Phần EXP vượt cấp, làm tròn, tràn int, trần cấp; lưu timer qua đăng nhập và va chạm timer hoạt động khác. Chưa có test game hay thử compiler Lua.
- Whitelist/mapping item cá thực nạp, giao dịch/stack, schema lưu thân mật và đồng bộ client; EXP/cấp riêng của hảo hữu chưa nối hoàn chỉnh.
- Theo task không build, chạy exe, kết nối VM/SQL/server. Kiểm chứng chỉ đọc nguồn, đối chiếu dòng, tự đọc báo cáo và kiểm tra khoảng trắng Git.

## Lỗi công cụ và kiểm chứng

- `rg : The term 'rg' is not recognized ...`: thử một lần, chuyển Select-String và đọc trực tiếp PowerShell; không cài công cụ.
- Get-Content mặc định làm lỗi hiển thị UTF-8 ở AGENTS nguồn; dùng UTF-8 cho Markdown, CP936 cho legacy và chỉ dựa token ASCII/số ở chuỗi Việt hỗn hợp. Đầu ra gộp nền bị rút gọn; đã thu hẹp đọc lại A-08c, thiết kế, owner-inputs và các đoạn nguồn quyết định. Không tạo parser/script phụ trên đĩa.
- Đã tự đọc lại báo cáo qua diff một lần, rà đủ 5 dòng TÓM TẮT, các mục tiêu và mục Chưa kiểm; `git diff --check` và kiểm khoảng trắng file mới không có chẩn đoán lỗi. Lệnh diff file mới trả 1 vì có khác biệt với /dev/null, không phải lỗi nội dung. Không sửa source, cấu hình, BAI_HOC hay báo cáo nền.

## Git và bước tiếp tục

**BỊ CHẶN – CHƯA PUSH.** Đã thử stage đúng hai file một lần, exit 1 tại lệnh shell; Git báo:

~~~text
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-10/index.lock': Permission denied
~~~

Git metadata nằm ngoài writable root `D:\JX-wt\A-10`; phiên không cho nâng quyền. Stage chưa thành công nên lệnh commit có điều kiện chưa chạy; **chưa có commit SHA hoặc link GitHub**. Không thử lại cùng lỗi, không đổi ACL/config/credential, không dùng index thay thế để vượt quyền. Không push vì yêu cầu chỉ gồm commit. Đây là blocker Git, không phải thiếu nội dung khảo sát.

PM tiếp tục bằng phiên có quyền ghi Git metadata, giữ nguyên nhánh đã xác nhận:

~~~powershell
git -C "D:\JX-wt\A-10" add -- JX1_OPS/REPORTS/A-10-lua-trai-boss.md JX1_OPS/TASKS/A-10.md
git -C "D:\JX-wt\A-10" commit -m "A-10 Khao sat lua trai tu boss tinh anh"
~~~
