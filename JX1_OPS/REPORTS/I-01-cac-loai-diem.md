# TÓM TẮT 5 DÒNG
1. Khảo sát tĩnh I-01: EXP, kỹ năng, tiềm năng và danh vọng có mã xử lý, lưu role buffer và đồng bộ Coco.
2. Bảng EXP gốc có 200 mục nhưng source server MAX_LEVEL=500; chưa xác nhận dữ liệu chạy thực tế.
3. Lên cấp cộng 5 tiềm năng, 1 kỹ năng; LevelUp xóa EXP dư; chia đội có hệ số và khoảng cách riêng.
4. Có lời gọi hệ hoạt động HuoYueDu nhưng thiếu script đích trong cây gốc; hạn ngày/tuần và bảng thưởng chưa xác minh.
5. Hoàn tất khảo sát tĩnh; HuoYueDu thiếu dữ liệu, lửa trại thiếu SkillId 1705/1706; không mạng/VM, không chạy binary game.

## Phạm vi và nguồn

- Ngày khảo sát: 2026-11-17. Nhánh `task/I-01`, worktree `D:\JX-wt\I-01`; kiểm tra Git ban đầu chỉ có task chưa được track, không có thay đổi tracked.
- `S` = `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src`.
- `H` = `D:\JX-source\server\jxOnline\header`.
- `GS` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs`.
- `C` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` (Coco gốc).
- Nhãn [NGUỒN]/[XÁC MINH] chỉ xác nhận nội dung file và phép đếm tĩnh, không xác nhận exe đang chạy khớp source.
- Đối chiếu thêm `D:\JX-source\client\Classes`: KProtocol.h, KPlayerRepute.cpp và KuiRoleStateVN.cpp giống byte với Coco gốc; CoreShell.cpp khác, nên báo cáo dẫn dòng Coco gốc, không coi hai cây hoàn toàn giống nhau.
- I-01 không có mã trong bản `TASKS/BACKLOG.md` tại worktree; task có phạm vi/đầu ra rõ và được người dùng giao trực tiếp nên thực hiện đúng task này, không sửa backlog. Không thấy quyết định liên quan các loại điểm trong lần lọc `STATE/QUYET-DINH.md`.

## ĐÃ XÁC MINH

### Kinh nghiệm

- `H/CoreUseNameDef.h:110` chọn `settings/npc/player/level_exp.txt`; `S/KPlayerSet.cpp:1291` đọc cột 2, theo vị trí dòng, tối đa MAX_LEVEL; `S/KPlayerSet.h:6` đặt 500.
- Bảng gốc có 200 dòng dữ liệu + header. Ví dụ cấp 1=100, 2=500, 10=10.900, 50=2.000.000, 100 và 200=2.000.000.000. Dòng file tương ứng 2, 3, 11, 51, 101, 201.
- `S/KPlayer.cpp:2936`: không đội gọi AddSelfExp; đội chỉ chia người cùng subworld và cách người nhận gốc tối đa 768 đơn vị (hằng ở dòng 63). N người đủ điều kiện: k=100+15N; phần người i trước AddSelfExp là E*k*Li/(100*sum(L)). Có làm tròn khi truyền float về int.
- Riêng AddExp trả ngay nếu đầu vào E==1 (`S/KPlayer.cpp:2938`); không nhầm với mức tối thiểu 1 EXP do AddSelfExp tính ra sau giảm chênh cấp. Nhánh đội chỉ còn 1 người đủ điều kiện gọi AddSelfExp nguyên E, không cộng 15%.
- `S/KPlayer.cpp:3099`: bỏ EXP không dương, chết/hồi sinh; E nhân `(ServerExp + mission[27])`, rồi áp chênh cấp; cấp người chơi dùng trong abs bị chặn trên 100. Sau đó tối thiểu 1, trạng thái CurrentUpExp nhân 2.
- `S/KPlayer.cpp:3145`: task 170 (`S/KTaskFuns.h:21`) đếm EXP cho đường AddSelfExp; chỉ chặn khi số cũ `> ServerExpLimit`, nên có thể vượt hạn ở lần nhận cuối. `GS/Settings/GameOption.ini:2`, `:4`, `:16` lần lượt ServerExp=1, ServerExpLimit=10.000.000, Skill120Rate=1. Chưa tính mission[27] thực tế.
- Reset task 170 có trong `GS/script/System/player/playerlogin.lua:108`: RLTask so ngày trong tháng `%d` với TASK_TODAY=1100, khác thì xóa task 170 ở `:125`; main gọi RLTask ở `:12`. Đây là reset khi chạy login script, chưa chứng minh reset lúc online qua nửa đêm; có rủi ro quay lại sau một tháng cùng số ngày không reset.
- `S/KPlayer.cpp:3232`: DirectAddExp bỏ hệ số/chia đội/chênh cấp và task 170; có kiểm MAX_LEVEL và giới hạn cấu hình. `S/ScriptFuns.cpp:15909` là Lua AddOwnExp; `:15922` có đường cộng dồn chia từng ngưỡng.
- `S/KPlayer.cpp:3264`: LevelUp đặt EXP=0, tăng đúng một cấp, cộng 5 tiềm năng và 1 kỹ năng. Không bảo toàn EXP dư ở đường gọi thông thường.
- Nguồn EXP quái: `S/KNpcDeathCalcExp.cpp:132`/`:190`/`:215`, E trước chia đội là `m_Experience * IsJinYan * nExpSale`; nExpSale đọc `ServerConfig/ExpRate` tại `S/KGameglobalSet.cpp:117`. Có kiểm NO_DROP_EXP, cự ly đến quái, người đại diện đội gần quái; không suy ra EXP chỉ chia theo tỉ lệ sát thương vì hai lời gọi hiện hành dùng toàn bộ tích trên. Đây là lớp trước công thức chia đội, không thay thế nó.
- Đội trưởng còn nhận kinh nghiệm thống soái ở `S/KPlayer.cpp:3043`, qua GetLeadExpShare (bảng ngũ hành). `level_lead_exp.txt` có 100 mục; ví dụ cấp 1: EXP=100/số người=3; cấp 50: 11.065.600/7; cấp 100: 4.139.977.600/10 (`GS/settings/npc/player/level_lead_exp.txt:2`, `:51`, `:101`). Giá trị cuối vượt signed int 32-bit; loader đi qua GetInteger rồi DWORD (`S/KPlayerSet.cpp:1490`), cần tester xác nhận chuyển đổi.

### Kỹ năng và tiềm năng

- `S/KPlayer.cpp:61`/`:62`: hằng cộng mỗi cấp là 5/1; phân phối tiềm năng yêu cầu nData>0 và không vượt số dư (`:2571`, `:2615`, `:2659`, `:2700`).
- Sức mạnh: sát thương cận chiến cộng current strength/5; thân pháp: sát thương vũ khí xa cộng current dexterity/5 (`:2859`, `S/KPlayer.h:37`). Mã cũ phía trên nằm trong comment, không dùng làm công thức hiện hành.
- Thân pháp: base hit=4*base dexterity-28, base defence=base dexterity/4 (`S/KPlayer.cpp:2884`). Sinh khí/nội công dùng hệ số theo ngũ hành ở `GS/settings/npc/player/level_add.txt`, 5 mục; loader `S/KPlayerSet.cpp:1303`.
- `S/KPlayer.cpp:5460`: tăng kỹ năng cần tìm thấy skill, đủ điểm, giới hạn cấp kỹ năng và script `main_Skillset`; nhánh thành công trừ điểm ở `:5545` hoặc `:5575`, đồng bộ `:5604`.
- Script được gọi thực tế `GS/script/global/global_setting.lua:5` (`main_Skillset`) chỉ `return 1`; hook tiềm năng `main_attributeSet` ở `:10` cũng `return 1`. Các điều kiện C++ vẫn tồn tại.
- EXP luyện kỹ năng khác điểm kỹ năng chưa phân phối: `S/KPlayer.cpp:3156` gọi AddSkillExp với `nGetExp * Skill120Rate / MAX_PERCENT`; `:3183` chỉ xét skill đủ điều kiện GetIsExpSkill và không TargetEnemy. Cấp/EXP từng skill lưu TDBSkillData, danh sách tại `S/KPlayerDBFuns.cpp:1198`/`:1252`/`:1742`; không gộp chúng vào ileftfight.

### Danh vọng và lưu trữ

- `S/KPlayerRepute.cpp:44`/`:67`: giá trị chặn trong 0..100.000 (`H/GameDataDef.h:42`), gửi REPUTE_VALUE_SYNC.
- `GS/script/header/repute_head.lua:15`: 11 mốc cấp danh vọng 0..10; các mốc ví dụ 80, 300, 750, 36.000. Không đồng nhất mốc cấp 10 với trần 100.000.
- Nguồn ví dụ: túi tiểu/trung/đại cộng 10/20/50 (`GS/script/mineitem/tuidanhvong_tieu.lua:2`, `tuidanhvong_trung.lua:2`, `tuidanhvong_dai.lua:2`); nhiệm vụ laotou cộng 1 (`script/laotou/quest_exp.lua:34`). Đây là nhánh script có mã, chưa kiểm việc gắn item/NPC và phát thưởng runtime.
- Cách tiêu: mua hàng loại `moneyunit_repute` kiểm số dư rồi trừ giá (`S/KPlayer.cpp:1325`, `:1444`); bản đồ có phí danh vọng kiểm/trừ tại `S/KNpc.cpp:1871`. Không thấy hạn ngày/tuần chung trong KPlayerRepute; script riêng có thể áp giới hạn.
- Sai khác cần thử, chưa sửa: wrapper `Repute_Set(value)` ở `GS/script/header/repute_head.lua:92` gọi `AddRepute(-value)`; trong khi Lua AddRepute thực chất cộng số truyền vào (`S/ScriptFuns.cpp:472`, `:483`). Vì vậy wrapper Repute_Add/Reduce không có nghĩa gán như tên hàm, có thể xóa số dư; không áp kết luận này cho lời gọi AddRepute trực tiếp.
- Load/save `S/KPlayerDBFuns.cpp`: EXP `:637`/`:1433`, tiềm năng `:608`/`:1417`, kỹ năng `:609`/`:1418`, danh vọng `:746`/`:1604`. Trường BaseInfo lần lượt fightexp, ileftprop, ileftfight, ireputevalue; thuộc tính ipower/iagility/iouter/iinside.
- Task lưu qua `KPlayerTask::m_Tasklate`, GetSaveVal/SetSaveVal (`S/KPlayerTask.cpp:84`/`:104`); đồng bộ tùy isSyn qua s2c_taskcallback, không tự chứng minh một task cụ thể là điểm hoạt động.
- Role buffer dùng dwTaskOffset/nTaskCount và TDBTaskData (ID/value); load `S/KPlayerDBFuns.cpp:1368`/`:1382`, save `:1844`/`:1852` chỉ ghi giá trị khác 0. Đây là mapping source, không đọc DB hay dump nhân vật thật.

### Điểm hoạt động

- `GS/script/battles/guozhan/head.lua:408`: game_level=3 và PL_TOTALPOINT>=100 gọi script `\\script\\huoyuedu\\huoyuedu.lua`, hàm `tbHuoYueDu:AddHuoYueDu`, khóa `tianziguozhan`.
- File đích không tồn tại trong cây Lua gốc đã đọc. Hai lời gọi killer ở `script/task/tollgate/killer/lib_killlevel.lua:26`/`:38` là comment.
- Không đủ bằng chứng để gán task ID, nguồn nhận đầy đủ, cách tiêu, giới hạn ngày/tuần hoặc bảng thưởng HuoYueDu.
- Phép tìm chuỗi `huoyuedu` trên 4.029 file Lua của GS cho đúng 3 dòng nêu trên (1 dòng lệnh, 2 comment). Không coi đây là bằng chứng hoạt động đang bật.
- Không nhầm UI Activity cũ với HuoYueDu: `GS/script/System/activity.lua:28` hàm main chỉ báo bảo trì; main11 ở `:34` có nhánh thưởng bạc/EXP (`:44`/`:45`), phúc duyên+danh vọng (`:48`/`:49`), xu theo giờ (`:52`), task 192 Tống Kim (`:59`). Chưa chứng minh main11 được UI gọi hiện hành.
- Biến 2920/2921/2922/2926/2927 tại `script/System/activity.lua:21` chỉ là khai báo tên (online time/date/daily limit/gift/rose); không đủ để nhận là số dư, hạn ngày hay điểm hảo hữu của HuoYueDu. Bảng `Settings/choujianglist.txt` có 16 mục (ví dụ pháo hoa ItemInfo=234 ở dòng 2), dùng cho nhánh quay thưởng tại activity.lua:67, không phải bảng đổi điểm hoạt động đã xác minh.
- Ví dụ hoạt động ngày riêng: `script/tnlteam/task_hang_ngay/lib_hang_ngay.lua:69` kiểm cờ đã nhận, 8 boss, 750 điểm Tống Kim, PK>=1, vượt ải>=1, PLD>=1, rồi thưởng 1–3 hộp item (6,1,1743), thời hạn item 7 ngày và khóa; cờ nhận ở `:119`. Task nhận/thưởng 1554/1555 (`script/header/taskid.lua:186`). Thời hạn item 7 ngày không phải hạn tuần của hệ điểm hoạt động.

### Bảng số liệu rút gọn

Không xuất nguyên bảng dài; các hàng sau là ví dụ phục vụ đối chiếu, không cần tạo bản dữ liệu riêng tư bổ sung.

| Bảng/công thức | Số mục / ngưỡng | Ví dụ hoặc kết quả tĩnh |
|---|---:|---|
| level_exp.txt | 200 cấp, 0 mục EXP=0 | Cấp 1=100; 50=2.000.000; từ 99 đến 200=2.000.000.000 |
| level_add.txt | 5 hệ | Kim: mỗi cấp +4 HP/+1 stamina/+1 MP; mỗi sinh khí +9 HP/+1 stamina; mỗi nội công +1 MP (dòng 2) |
| level_add.txt | 5 hệ | Thổ: mỗi cấp +1 HP/+1 stamina/+3 MP; mỗi sinh khí +4 HP/+1 stamina; mỗi nội công +4 MP (dòng 6) |
| level_lead_exp.txt | 100 cấp | Cấp 1/50/100: sức chứa 3/7/10 người |
| Chênh cấp d=abs(min(Lplayer,100)-Ltarget), nhánh thường | d=0..5 / 6 / 10 / 15 / >15 | 100% / 90,5% / 52,5% / 5% / 1 EXP trước x2 |
| Nhánh đặc biệt: Lplayer thật>=Ltarget>=100 | riêng | E - floor(E*d/200); ví dụ Lplayer=120,target=110: d=10, 95% |
| Đội cùng cấp đủ cự ly, N>=2 | 2 / 3 / 6 người | Mỗi người 65% / khoảng 48,33% / khoảng 31,67% E trước chênh cấp và nhân hệ số |
| Điểm lên cấp | 2 loại | +5 tiềm năng; +1 kỹ năng; EXP dư về 0 |
| Danh vọng | 11 mốc cấp, trần 100.000 | cấp 1 cần 80, cấp 10 cần 36.000; túi +10/+20/+50 |
| HuoYueDu | 1 lời gọi, 2 comment | Không có dữ liệu để đếm nguồn, thưởng, hạn ngày/tuần |

Ví dụ tĩnh: E=1.000, ServerExp=1, mission[27]=0, không x2/không vượt hạn; d=6 nhận 905, d=10 nhận 525, d=15 nhận 50, d=16 nhận 1. Đây là phép thế công thức, chưa phải kết quả game. C++ int làm tròn về 0; tích int và m_nExp gần 2 tỷ có nguy cơ tràn, chưa chạy để xác nhận.

### Gói tin và Coco

`P` = `D:\JX-source\server\jxOnline\gameserver\Headers\KProtocol.h`. Chỉ đối chiếu trường khai báo; không bắt gói và không kiểm ABI/runtime.

| Nội dung | Gói / trường chính | Bằng chứng server → Coco gốc |
|---|---|---|
| EXP | s2c_playerexp / PLAYER_EXP_SYNC: int m_nExp | P:551; C/gamecore/KProtocol.h:535; KProtocolProcess.cpp:508 → s2cSetExp |
| Lên cấp, điểm còn | s2c_playerlevelup / WORD level, int EXP/attribute/skill, UINT HP/stamina/MP | P:833; C/gamecore/KProtocol.h:823; KProtocolProcess.cpp:1391; KPlayer.cpp:4554/4568 cập nhật số dư |
| Tiềm năng đã cộng | s2c_playersyncattribute / byte loại, int base/current/leave | P:866; C/gamecore/KProtocol.h:856; KProtocolProcess.cpp:96 đăng ký handler |
| Kỹ năng | s2c_playerskilllevel / ID, level, EXP, leave, add, type | P:875; C/gamecore/KProtocol.h:865; KProtocolProcess.cpp:1275 cập nhật m_nSkillPoint |
| Danh vọng | s2c_reputesyncreputevalue / int value | P:213; C/gamecore/KProtocol.h:203; KProtocolProcess.cpp:5033 |
| Task | s2c_taskcallback / int ID, UINT dwid, int value | P:1133; C/gamecore/KProtocol.h:1078; KProtocolProcess.cpp:1548 |
| Yêu cầu cộng điểm | PLAYER_ADD_BASE_ATTRIBUTE_COMMAND / PLAYER_ADD_SKILL_POINT_COMMAND | P:852/859; C/gamecore/KProtocol.h:842/849 |

- Coco **có lõi dữ liệu** EXP/tiềm năng/kỹ năng/danh vọng: `C/gamecore/CoreShell.cpp:1572`, `:1578`, `:1703`, `:2370`; UI VN hiện danh vọng/điểm tiềm năng tại `C/vn/gameui/KuiRoleStateVN.cpp:904`/`:911`, gửi yêu cầu cộng thuộc tính tại `:462`.
- UI kỹ năng chung có tăng kỹ năng/đọc điểm dư (`C/gameui/KuiSkill.cpp:636`/`:647`). Chưa xác minh màn hình VN sử dụng đúng UI chung này: không thấy hai token GOI_TONE_UP_SKILL/GDI_FIGHT_SKILL_POINT trong `vn/gameui/KuiSkillVN.cpp`; không suy ra chức năng VN thiếu chỉ từ phép tìm đó.
- Coco gốc đặt MAX_LEVEL=500 trong gamecore/KPlayerSet.h:6, đọc level_exp từ loader KPlayerSet.cpp:247; bảng EXP client đang đóng gói/chọn lúc chạy chưa xác minh. Tìm file rời level_exp/level_add trong Resources và data gốc không có; không giải PAK.
- Tìm token HuoYue/huoyue/ActivityPoint/ActivePoint trong 459 file .cpp/.h thuộc gamecore, gameui, vn của Coco gốc và 460 file của snapshot D:\JX-source\client: 0 hit. **Chưa thấy triển khai HuoYueDu riêng trong phạm vi này**; Lua có thể dựng UI động nên không kết luận tuyệt đối Coco thiếu mọi hình thức hiển thị hoạt động.

### Liên hệ lửa trại (G-01) và hảo hữu

- Không có `JX1_OPS/TASKS/G-01.md` tại worktree để đối chiếu kết quả của worker G-01. Bằng chứng bàn giao tĩnh: `GS/script/item/huozhong.lua:35` chặn trạng thái 1705/1706, kiểm vùng và fight state tại `:60`, tạo NPC 2078/cấp 90 tại `:76`, sống 1800 và gán skill 1705/cấp 50 ở `:79`/`:82`. Lửa trại lịch `script/task/gouhuo.lua:27` dùng skill 1705/cấp 30, sống 3600; `dahuo.lua:22` dùng cấp 50.
- Script skill tên vật lý `GS/script/skill/special/óô»ð.lua` (tên byte GBK của 篝火.lua): dòng 8 có **50 mức** EXP (mức 1=5.000, 10=6.400, 30=10.400, 50=15.000); hai cấu hình thấp/cao ở dòng 6/10 là comment. Không coi bảng mức này tự chứng minh skill đã liên kết thành công.
- `S/KNpcAttribModify.cpp:3106` nhận addexp_v vào m_ExpState; `S/KNpc.cpp:1801` dùng chu kỳ nTimeval*18 frame, giảm thời gian, khi m_IsDoing==0 gọi `script/global/goldacition.lua/OnDoAcition`; script này gọi AddOwnExp tại dòng 15. GouHouTime=10 trong `GS/Settings/gamesetting.ini:485`, đọc tại `S/KGameglobalSet.cpp:88`. Đây là biểu thức frame nguồn, không xác nhận thời gian thật trên server 36 Hz.
- `goldacition.lua:17` còn có nhánh `random(1,100)<3`, chọn dòng 2..10 của `settings/dropitem/huodong.txt` (9 mục dữ liệu); ví dụ dòng 2 là item đá, dòng 3/4 là không có vật phẩm. Nhánh `<3` không nên gọi là 3% nếu chưa xác minh semantics random; với phân phối đều 1..100 thì là 2% trước chọn mục. Đây là quà kèm EXP, không phải đổi HuoYueDu.
- **Lệch dữ liệu cần G-01/tester xử lý:** `GS/Settings/Skills.txt` có 1.720 dòng dữ liệu, 1.719 SkillId duy nhất; **0 dòng SkillId=1705 hoặc 1706**, trong khi Lua gán chúng. `S/KSkillManager.cpp:65` tra cột SkillId, không lấy số thứ tự dòng làm ID. Không sửa bảng, chưa kết luận lửa trại runtime hỏng vì exe có thể nạp bản PAK/overlay khác.
- Hảo hữu: AddExp/AddSelfExp và công thức chia đội đã đọc không kiểm Friend/độ thân mật; ở đó chỉ có cấp, đội, subworld/cự ly, trạng thái và hệ số. `S/KPlayerChat.h:62` CChatFriend có ID/index/tên, không có điểm thân mật; `S/KPlayerDBFuns.cpp:1765` lưu danh sách tên vào dwFriendOffset/nFriendCount. Coco có quy trình thêm bạn (`S/KPlayer.cpp:6447`, nhánh client `:4863`), nhưng chưa chứng minh thưởng EXP hay quan hệ điểm hoạt động chỉ vì là bạn.

### Dấu vân tay dữ liệu để tái lập

SHA-256 tính trực tiếp trên file gốc, không chạy file game:

| File GS | SHA-256 |
|---|---|
| Settings/npc/player/level_exp.txt | `afec7335884f8194073267d42cb150ff0604b8e8dac1367a1abbbc131b648424` |
| Settings/npc/player/level_add.txt | `3edfb2d16180f13bf724c9f9c4bbc4a3902a306fc89042e2d951b307b27baeca` |
| Settings/Skills.txt | `823e2d18eaea394a92e76257528d01040aa4687c669719e1fd3c4f57a82cfc48` |

## CHƯA XÁC MINH

- Source và cây dữ liệu có khớp binary, overlay/PAK và cấu hình được nạp trên server thật hay không; không truy cập VM/server.
- HuoYueDu: thiếu script đích; chưa xác định role/task số dư, API gói riêng, nguồn nhận đầy đủ, tiêu điểm, hạn ngày/tuần, bảng thưởng. Cần bổ sung đúng bộ script/data của bản đích để khảo sát tiếp.
- EXP cấp 201..500 thiếu hàng trong file rời, xử lý GetInteger fallback thực tế; AddSelfExp không dùng guard PlayerMaxLevel như DirectAddExp. Cấu hình gốc có PlayerMaxLevel=200 tại gamesetting.ini:448, loader `S/KGameglobalSet.cpp:126`; không bảo đảm mọi đường EXP tôn trọng 200.
- Thứ tự/chu kỳ reset online, task 170, nguy cơ vượt hạn/tràn int; ABI/size/wire ID gói không được biên dịch hay bắt gói.
- Kỹ năng riêng, tẩy điểm, thưởng nhiệm vụ và trang bị có thể cộng thêm điểm ngoài +5/+1 cơ bản; không phải kiểm kê tất cả nguồn cộng bù toàn game.
- Cơ chế thân mật phía relay hoặc Lua ngoài đường đã đọc; không có cơ sở nói mọi hệ hảo hữu đều không thưởng EXP.
- Không chạy build, unit test hay test game; chỉ phép đếm/tìm chuỗi/hash/đối chiếu source. Không mạng thật/VM, không mở exe/dll game, không đọc mật khẩu/khóa/DB/log cá nhân.

## Ca test cho TESTER (chưa chạy)

Chỉ thực hiện ở môi trường thử được chủ dự án/PM cho phép; dùng dữ liệu thử, ghi source/data revision, EXP trước/sau, task trước/sau và ảnh/gói đã lọc. Không coi bảng này là cấp quyền chạy VM trong task I-01.

| ID | Thiết lập và thao tác | Kỳ vọng theo source / điểm phải quan sát |
|---|---|---|
| I01-T01 | Cấp 1, EXP=0, thêm 99/100/101 bằng AddOwnExp, từng trạng thái độc lập | 99 chưa lên; 100/101 lên 1 cấp, EXP=0, +5 tiềm năng/+1 skill; xác nhận mất 1 EXP dư |
| I01-T02 | E=1000, hệ số 1, mission27=0, không x2; lần lượt d=5,6,10,15,16 | 1000/905/525/50/1, không lẫn DirectAddExp |
| I01-T03 | Người cấp 120, quái 110; so người 120/quái 90, E=1000 và hệ số 1 | Nhánh 110 dùng min(level,100), ra 950; nhánh 90 có d=10, ra 525; kiểm lựa chọn nhánh và clamp |
| I01-T04 | 2 người cùng cấp, cùng đội, gần nhau; rồi xa >768/khác subworld | Mỗi người khoảng 65% E trước các hệ số; ngoài cự ly không chia; kiểm mốc biên 768 và cự ly tới quái riêng |
| I01-T05 | task170=L-1, L, L+1; thêm EXP một lần; so AddOwnExp | AddSelfExp cho nhận khi <=L rồi mới chặn lần sau; AddOwnExp không tăng task170 |
| I01-T06 | Online qua nửa đêm; đăng nhập ngày khác; cùng ngày tháng sau | Ghi reset thực tế; RLTask chỉ so `%d`, không tự giả định reset online đúng |
| I01-T07 | Cộng từng loại thuộc tính 1 điểm với các mốc dex chia hết/không hết cho 4/5 | Số dư giảm 1, strength/5 hoặc dex/5 theo vũ khí, hit/dodge và HP/MP theo hệ; yêu cầu 0/âm/vượt số dư bị chặn ở đường thuộc tính |
| I01-T08 | Tăng skill hợp lệ, chưa mở, thiếu điểm, vượt yêu cầu cấp; relog | Chỉ thành công khi đủ điều kiện, điểm dư/skill được sync và lưu; không nhầm EXP luyện skill với điểm dư |
| I01-T09 | Danh vọng 0/79/80/35999/36000/99999; dùng túi và mua hàng | Clamp 0..100000, mốc cấp đúng; mua thiếu điểm không trừ, mua đủ trừ giá; relog giữ số dư |
| I01-T10 | Gọi wrapper Repute_Add/Reduce trên dữ liệu thử riêng | Đối chiếu AddRepute trực tiếp; phát hiện wrapper trừ sai, không dùng nhân vật thật |
| I01-T11 | Kiểm nguồn skill1705/1706 trước; đặt lửa trại với nhân vật thử, thay ServerExp | Nếu dữ liệu liên kết đầy đủ, EXP đi AddOwnExp không theo ServerExp/task170; đo tick thực tế, quà kèm, trạng thái và thời gian sống |
| I01-T12 | 2 người cùng đội/cấp/cự ly; thử kết bạn và bỏ bạn, giữ yếu tố khác | Không thấy bonus hảo hữu ở công thức đã đọc; nếu runtime khác thì thu đúng script/relay gây khác |
| I01-T13 | Quốc chiến level3, điểm 99/100; theo dõi call HuoYueDu | Với cây hiện có báo thiếu file là điểm cần xử lý; chỉ kiểm reset/tiêu/thưởng sau khi có đúng implementation |
| I01-T14 | Điểm EXP sát 2 tỷ, thưởng lớn; cấp199/200/201 trên server thử | Xác định overflow, giới hạn cấp theo từng đường, dữ liệu EXP client/server và UI đồng bộ |

## Lỗi công cụ, cách xử lý và kết quả

- `rg : The term 'rg' is not recognized...`: không cài công cụ/không sửa PATH; chuyển sang Python chuẩn `python -I -` đọc file. Lệnh Get-ChildItem -LiteralPath -Recurse -Include trả tập rộng hơn dự kiến, output bị cắt; sau đó chỉ dùng tên file/đường dẫn hẹp với pathlib.
- PowerShell mặc định hiển thị UTF-8 thành mojibake: đọc lại task với `-Encoding UTF8`. Python stdout mặc định gây `UnicodeEncodeError: 'charmap' codec can't encode...`; đặt `sys.stdout.reconfigure(encoding='utf-8')`, lần sau thành công.
- Chuỗi Unicode chèn qua stdin PowerShell bị thay thành `?`, gây `re.error: nothing to repeat at position 59` và `OSError: [Errno 22] Invalid argument` ở tên Lua: dùng Unicode escape và chọn tên có sẵn bằng pathlib, không đổi tên file gốc. Nội dung Lua trộn GBK/Vietnamese legacy vẫn có ký tự khó đọc; kết luận dựa symbol/cột số/byte, không dịch suy đoán toàn văn.
- Một lần trích đoạn vượt cuối file gây `IndexError: list index out of range`; dùng enumerate/min giới hạn rồi đọc đúng phần còn thiếu. Đây là lỗi trích xuất, không phải lỗi game. Mỗi lỗi cụ thể không thử quá 3 lần.
- Nhận diện skill phải dùng cột SkillId (cột 2), không dùng dòng file hay SkillName; phép đếm cuối đã dùng đúng cột, xác nhận 1705/1706 không có.
- Lần quét mẫu IPv4 ban đầu bắt nhầm số EXP có dấu chấm phân nhóm (`AssertionError: possible sensitive content`); chuyển sang kiểm địa chỉ IPv4 hợp lệ bằng ipaddress, quét lại cả task và báo cáo đạt. Không có địa chỉ mạng hay giá trị credential trong hai file bàn giao.
- Kiểm tra cuối đã chạy: UTF-8 không ký tự thay thế, tóm tắt đúng 5 dòng, đủ 14 mã ca TESTER, quét mẫu gán secret/private key/IPv4 hợp lệ; đạt. Đây là kiểm tài liệu, không phải test phần mềm game.
- Git stage thử đúng hai file bị sandbox chặn: `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/I-01/index.lock': Permission denied`. Không thử vượt quyền, không đổi credential/config, không có commit được tạo. Báo cáo và task vẫn ở worktree; cần PM chạy stage/commit từ phiên có quyền ghi metadata Git.

## Kết quả bàn giao

- Trạng thái: **PARTIAL – khảo sát tĩnh DONE, bàn giao Git bị chặn**; các khoảng trống dữ liệu đã nêu ở CHƯA XÁC MINH; không có thay đổi code/cấu hình.
- Một báo cáo tổng hợp này và mục Kết quả trong task; không xuất bảng gốc dài, không ghi file ngoài vùng được giao.
- Bước tiếp theo: PM/tester bổ sung bộ HuoYueDu và nguồn dữ liệu skill lửa trại thực sự được nạp, sau đó chạy các ca phù hợp; chưa có đủ dữ liệu để triển khai hệ điểm hoạt động.
- Commit SHA: **không có – stage bị chặn quyền ghi metadata Git** như lỗi trên. **BỊ CHẶN – CHƯA PUSH**; ngoài lỗi stage, người dùng cũng cấm mạng trong task. Không có bằng chứng GitHub, không tuyên bố đã công bố.
