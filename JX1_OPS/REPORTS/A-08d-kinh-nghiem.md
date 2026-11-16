TÓM TẮT 1: [NGUỒN] AddOwnExp → LuaAddOwnExp → DirectAddExp chỉ cộng cho người chơi hiện tại; không tự chia tổ đội (S/Core/Src/ScriptFuns.cpp:15908–15918,26232).
TÓM TẮT 2: [NGUỒN] AddExp(exp,level,1) đi qua chia đội theo cấp, cùng subworld và khoảng cách 768; AddSelfExp áp dụng hệ số riêng (S/Core/Src/ScriptFuns.cpp:15888–15903; S/Core/Src/KPlayer.cpp:63,2936–3056,3099–3179).
TÓM TẮT 3: [NGUỒN] GetNextExp() là ngưỡng EXP của cấp hiện tại, lấy cột 2 level_exp.txt; GetExp() là tiến độ trong cấp (S/Core/Src/ScriptFuns.cpp:15862–15884; S/Core/Src/KPlayerSet.cpp:1291–1299,1329–1333).
TÓM TẮT 4: [NGUỒN] SetTimer(18,id) là 18 tick theo quy ước 18 tick/giây; callback OnTimer tự lặp. servertimer.Main còn bị chặn ở giây hệ thống bằng 0 (S/Core/Src/KSubWorldSet.cpp:28; S/Core/Src/KTaskFuns.cpp:118–130,190–195; S/Core/Src/CoreServerShell.cpp:2227–2240).
TÓM TẮT 5: [NGUỒN] DirectAddExp làm mất phần EXP vượt ngưỡng khi lên cấp; toàn bộ kết luận là đọc tĩnh, chưa xác minh binary/nhịp thời gian thực (S/Core/Src/KPlayer.cpp:3244–3250,3264–3273; mục Chưa kiểm).

# A-08d — Kinh nghiệm người chơi, tổ đội và điểm gắn timer

Ngày khảo sát: 17/11/2026. Trạng thái: **PARTIAL** — nội dung nghiên cứu DONE, commit BLOCKED; kết quả Git ghi ở cuối báo cáo và mục Kết quả của task.

## Worker kiểm tra trước khi làm

- [XÁC MINH] Đọc task trước; `Get-Location` trả `D:\JX-wt\A-08d`, `git status --short --branch` trả `## task/A-08d-codex`, không có thay đổi local. Khớp worktree/branch trong `JX1_OPS/TASKS/A-08d.md:7–8`.
- Chỉ tạo báo cáo này; cập nhật các mục bàn giao trong file task theo yêu cầu trực tiếp của người dùng. Không sửa source/cấu hình trong `C:\Jx1CocoV3`, không chạy exe/build/test, không kết nối VM/SQL/server.
- [BÁO CÁO] Đọc A-03 và D-01: thống kê thiếu Lua của A-03 thuộc cây source cũ, không áp dụng cho gói gs hiện có; D-01 đã ghi nguy cơ lỗi nháy ở `servertimer.lua:125` (`JX1_OPS/REPORTS/A-03-kiem-ke-cau-hinh.md:9,25–28`; `JX1_OPS/REPORTS/D-01-bang-hoat-dong.md:3–4`).
- [BÁO CÁO] Đã đọc tài liệu chủ dự án: yêu cầu 0,5% EXP cấp hiện tại/giây và x2 khi đốt cùng đội; bản thiết kế nháp ghi 120 giây và còn bỏ ngỏ ý nghĩa x2 (`D:/jx1-ops-wt/JX1_OPS/owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md:3`; `D:/jx1-ops-wt/JX1_OPS/DESIGN/HAO-HUU-CUNG.md:24–26`). Báo cáo này khảo sát điểm tích hợp, chưa triển khai hay chốt cách nhân đôi.

## Quy ước bằng chứng

| Tiền tố | Gốc đường dẫn |
| --- | --- |
| `S/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\` |
| `H/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\header\` |
| `G/` | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\` |

Số dòng tính từ 1, gồm dòng trống. Markdown đọc UTF-8; source/bảng legacy đọc CP936/GBK, không chuyển mã file. Một số chuỗi tiếng Việt trong Lua vẫn có dấu hiệu lỗi mã hóa; chỉ dùng symbol ASCII và giá trị số làm bằng chứng, không suy tên chức năng từ chữ lỗi. [NGUỒN] là hành vi trong văn bản source, không xác nhận exe triển khai khớp source.

## API cộng EXP và các chỗ gọi

| API / symbol | Hành vi và điều kiện | Bằng chứng |
| --- | --- | --- |
| Lua `AddOwnExp(exp)` | Cần ít nhất 1 đối số và player index > 0; ép số sang `int`, chỉ chuyển giá trị không âm vào `DirectAddExp`; không có đối số chia đội. | `S/Core/Src/ScriptFuns.cpp:15908–15918,26232` |
| C++ `DirectAddExp(int)` | Bỏ qua EXP bằng 0, cấp ≥ MAX_LEVEL hoặc cấp ≥ `_gameGlobalSet.PlayerInfo.nMaxLevel + m_nLimitMaxLevel`; sau đó cộng thẳng `m_nExp`. Trong hàm không áp dụng ServerExp, cờ x2, kiểm tra chết hay giới hạn task EXP như AddSelfExp. | `S/Core/Src/KPlayer.cpp:3232–3258`; đối chiếu `3099–3154` |
| Lua `AddExp(exp,targetLevel,allTeam)` | Đối số 3 mặc định 0 → `AddSelfExp`; khác 0 → `KPlayer::AddExp` để xét tổ đội. `targetLevel` là đầu vào điều chỉnh chênh lệch cấp, không phải cấp muốn nâng người chơi tới. | `S/Core/Src/ScriptFuns.cpp:15887–15905,26230`; `S/Core/Src/KPlayer.cpp:3095–3135` |
| Lua `AddSumExp(exp)` | Chia phần thưởng theo `m_nNextLevelExp - m_nExp`, gọi DirectAddExp từng đoạn để giữ phần còn lại qua nhiều cấp; không chia đội. Chưa nên dùng mù ở trần cấp: vòng while không kiểm tiến triển sau khi DirectAddExp từ chối. | `S/Core/Src/ScriptFuns.cpp:15921–15947,26233`; `S/Core/Src/KPlayer.cpp:3235–3242` |
| Nguồn EXP đánh NPC | Hai nhánh trong tính EXP khi NPC chết gọi `Player[...].AddExp(...)`, truyền EXP NPC, hệ số và cấp NPC. | `S/Core/Src/KNpcDeathCalcExp.cpp:186–190,208–215` |
| Nguồn C++ trực tiếp khác | Nhánh nhận vật phẩm phân hủy gọi `DirectAddExp(nLevel * ...nInFenJie[1])`; không phải mọi DirectAddExp đều đến từ Lua. | `S/Core/Src/KPlayer.cpp:6308–6313` |

[NGUỒN] `DirectAddExp` khi `m_nExp >= m_nNextLevelExp` gọi `LevelUp()` đúng một lần; `LevelUp` đặt `m_nExp = 0`, tăng cấp một lần rồi nạp ngưỡng cấp mới. Vì vậy phần vượt bị bỏ, không tự cộng dồn qua nhiều cấp. Ví dụ ngưỡng 100, đang 90, thưởng 20 → cấp kế, EXP 0 theo luồng này; đây là minh họa suy từ source, chưa phải kết quả chạy (`S/Core/Src/KPlayer.cpp:3244–3256,3264–3273`). Giá trị `int` cũng đòi hỏi kiểm miền đầu vào trước khi cấp thưởng; không coi literal Lua lớn là được C++ hỗ trợ nguyên vẹn (`S/Core/Src/ScriptFuns.cpp:15914–15916`; `S/Core/Src/KPlayer.cpp:3232,3244`).

[XÁC MINH] Tìm literal `\bAddOwnExp\s*\(` bằng `Select-String` trên file `.lua` rời trong `G/script` thu được 398 dòng khớp trong 175 file, gồm cả comment; không phải số đường gọi hoạt động. Các mẫu đã đọc thân:

| Chỗ gọi | Dữ liệu đưa vào | Bằng chứng |
| --- | --- | --- |
| Rương `shenmibox` | Nhánh `award_list[a_lvl][1] == "addexp"`, chọn bảng thưởng rồi gọi AddOwnExp. | `G/script/class/shenmibox.lua:195–203` |
| Callback `OnDoAcition` | Từ chối nExp âm rồi gọi AddOwnExp(nExp); chưa truy nơi đăng ký callback này. | `G/script/global/goldacition.lua:7–15` |
| Thưởng định kỳ flower | OnTimer → returnForEveryTime → addExpForLvl → AddOwnExp(rExp), tính rExp từ bảng cấp và ExpX/sb. | `G/script/class/flower/flower1.lua:1–13`; `G/script/class/flower/flowerhead.lua:468–480,502–511` |
| Script GM (cảnh báo miền số) | Có literal `AddOwnExp(9999999999)` vượt miền số nguyên có dấu 32 bit; chưa xác minh kiểu Lua_Number và kết quả cast trong binary. | `G/script/gm a phuong.lua:461`; `S/Core/Src/ScriptFuns.cpp:15914–15916` |

## EXP tổ đội và hệ số

[NGUỒN] `KPlayer::AddExp` bỏ qua riêng `nExp == 1`; nếu không ở đội thì chuyển AddSelfExp. Nếu ở đội, xét đội trưởng và thành viên trong cùng subworld, khoảng cách bình phương ≤ 768² tính từ người nhận lời gọi AddExp; không phải mặc định tính từ vị trí NPC bị giết. Không có người/cấp hợp lệ thì return; chỉ 1 người hợp lệ thì AddSelfExp trực tiếp (`S/Core/Src/KPlayer.cpp:63,2936–3023`).

[NGUỒN] Với N > 1 người hợp lệ, tổng cấp L, người i cấp Li: `k = 100 + 15*N`, tỷ trọng `p_i = k*Li/L` (nếu ≤ 0 thì gán 1), EXP truyền cho AddSelfExp là `int(nExp*p_i/100)`. Đây chưa phải EXP cuối cùng. Đội 5 người bằng cấp nhận đầu vào mỗi người 35% EXP gốc, tổng 175% trước hiệu chỉnh và làm tròn; không phải mỗi người x2. Đội trưởng còn nhận LeadExp theo công thức riêng (`S/Core/Src/KPlayer.cpp:3026–3056`).

[NGUỒN] `AddSelfExp` xử lý tiếp theo thứ tự (`S/Core/Src/KPlayer.cpp:3099–3179`):

1. Từ chối EXP ≤ 0, trạng thái chết/hồi sinh (`3101–3105`).
2. Khi tính chênh lệch, chặn cấp người chơi dùng so sánh ở 100; nhân EXP đầu vào với `ServerExp + g_GlobalMissionArray.GetMissionValue(27)` (`3109–3116`). Đây là phép cộng hệ số, không tự hiểu mission 27 là nhân 2.
3. Nếu cấp thật người chơi ≥ cấp mục tiêu và mục tiêu ≥ 100: `E - E*d/200`; các trường hợp còn lại: d ≤ 5 giữ E, 6–15 dùng `E*(295-19*d)/200`, d > 15 cho 1; kết quả ≤ 0 cũng chặn về 1 (`3118–3139`).
4. Nếu `m_CurrentUpExp` khác 0 thì nhân 2; kiểm task `TASKVALUE_LIMIT_EXP` với điều kiện `nLeftExp > ServerExpLimit` rồi mới cộng. Đây không phải phép cắt thưởng vừa đủ trần: lần cộng có thể vượt trần (`3141–3154`; `S/Core/Src/KTaskFuns.h:21`).
5. Có nhánh thêm EXP kỹ năng theo Skill120Rate, rồi xét lên cấp/đồng bộ. Không mặc định áp các bước này cho AddOwnExp (`3156–3179`; `3232–3258`).

## Tổng EXP cần cho cấp hiện tại và công thức 0,5%

[NGUỒN] `PLAYER_LEVEL_EXP_FILE` trỏ `\settings\npc\player\level_exp.txt`; KLevelAdd::Init đọc cột 2, dòng `i+2` vào `m_nLevelExp[i]`; `GetLevelExp(level)` trả `m_nLevelExp[level-1]` hoặc 0 khi ngoài miền. Không tính bằng cộng tất cả các cấp trước (`H/CoreUseNameDef.h:110`; `S/Core/Src/KPlayerSet.cpp:1291–1299,1329–1333`).

| Đại lượng | Cách lấy | Ý nghĩa / bằng chứng |
| --- | --- | --- |
| E(level) | Lua `GetNextExp()` | Trả `m_nNextLevelExp`, được cập nhật theo cấp mới khi LevelUp (`S/Core/Src/ScriptFuns.cpp:15862–15871,26228`; `S/Core/Src/KPlayer.cpp:3271–3273`). |
| EXP đang có trong cấp | Lua `GetExp()` | Trả `m_nExp`; LevelUp đặt lại về 0 (`S/Core/Src/ScriptFuns.cpp:15875–15884,26229`; `S/Core/Src/KPlayer.cpp:3266`). |
| Còn thiếu tới cấp kế | `GetNextExp() - GetExp()` | Script datau đã dùng phép trừ này; không dùng lượng còn thiếu làm mẫu số cho yêu cầu 0,5% toàn cấp (`G/script/global/npcchucnang/datau.lua:1188–1198`). |
| EXP tích lũy từ cấp 1 | Nếu cần: tổng E(k) cho k < level cộng EXP hiện tại | Công thức suy từ việc reset EXP mỗi cấp; chưa tìm/kiểm API trả thẳng tổng tích lũy, không phải mục tiêu thưởng lửa trại (`S/Core/Src/KPlayer.cpp:3266–3273`; `S/Core/Src/KPlayerSet.cpp:1333`). |

[NGUỒN] Bảng rời hiện đọc được: cấp 1 → 100, cấp 10 → 10.900, cấp 50 → 2.000.000, cấp 100 và 200 → 2.000.000.000 EXP cho cấp đó (`G/Settings/npc/player/level_exp.txt:2,11,51,101,201`). Chưa xác minh đây là bảng exe nạp do ưu tiên đĩa/PAK chưa kiểm.

[GIẢ THUYẾT — đề xuất tích hợp] Mỗi lần hưởng hợp lệ tính `grant = floor(GetNextExp()/200)` để biểu diễn 0,5%; đọc lại GetNextExp sau lần lên cấp, không giữ ngưỡng cũ cho cả 120 giây. Ví dụ cấp 50 là 10.000/lần, cấp 100 là 10.000.000/lần theo bảng rời; cấp 1 cho 0 sau floor, nên chính sách tích lũy phần lẻ/làm tròn phải chốt. Công thức dựa trên API/bảng trên và yêu cầu chủ dự án, chưa có code mới hay test (`S/Core/Src/ScriptFuns.cpp:15862–15880`; `G/Settings/npc/player/level_exp.txt:2,51,101`; `D:/jx1-ops-wt/JX1_OPS/owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md:3`).

## Tick, timer Lua và nơi gắn được

| Điểm gắn | Luồng đã nối bằng source | Giới hạn và đề xuất |
| --- | --- | --- |
| Timer người chơi | `SetTimer(time,id)` → Player.SetTimer → m_TimerTask.SetTimer; `KPlayer::Active` gọi Activate; đến hạn tra TASK/SCRIPT rồi `ExecuteScriptA(...,"OnTimer",0)`. | Điểm gắn Lua có sẵn; thời gian tính bằng tick game, không phải trực tiếp mili giây (`S/Core/Src/ScriptFuns.cpp:5473–5480,25834`; `S/Core/Src/KPlayer.cpp:339,1591–1599`; `S/Core/Src/KTaskFuns.h:54–65`; `S/Core/Src/KTaskFuns.cpp:118–130,178–195`). |
| Bảng định tuyến timer | `TIMERTASK_SETTINGFILE` = `\settings\TimerTask.txt`; GetTimerTaskScript tra ID ở cột TASK, lấy SCRIPT. | Cần ID mới được duyệt và file Lua có OnTimer; không ghi đè ID hiện có. Ví dụ ID 7/8/9 đã dành cho flower (`S/Core/Src/KTaskFuns.h:14`; `S/Core/Src/KTaskFuns.cpp:105–114,178–186`; `G/Settings/TimerTask.txt:1,8–10`). |
| Tick lõi | GetGameTime trả `m_nLoopRate`; MainLoop tăng bộ đếm một đơn vị; chú thích source quy ước 18 frame/giây. | SetTimer(18,id) tương ứng một giây game theo quy ước; nhịp giây thật khi lag/chạy binary khác chưa kiểm (`S/Core/Src/KSubWorldSet.h:68`; `S/Core/Src/KSubWorldSet.cpp:28,505–507`). |
| Lịch server `servertimer.Main` | Breathe kiểm game-time mod 18 bằng 0, rồi `GetSystemTime().wSecond == 0` mới gọi Main. | Chỉ có cửa ở giây 0 mỗi phút; không bảo đảm chính xác một lần/phút khi lag, và không phải callback mỗi giây. Lua còn có dấu nháy mở chưa đóng ở dòng 125 (`S/Core/Src/CoreServerShell.cpp:2227–2246`; `G/script/servertimer.lua:23–25,123–128`). |

[NGUỒN] Timer người chơi **tự lặp**: Activate đặt hạn mới bằng thời gian game hiện tại + interval trước khi gọi callback. Không cần bắt buộc SetTimer lại trong mỗi OnTimer; mẫu flower chủ động StopTimer rồi SetTimer lại sau khi kiểm điều kiện. Mỗi KPlayer có một `m_TimerTask`, nên dùng chung SetTimer sẽ thay ID/interval hiện tại, có thể đụng timer hoạt động khác (`S/Core/Src/KTaskFuns.cpp:120–129`; `S/Core/Src/KTaskFuns.h:63–65`; `S/Core/Src/KPlayer.h:269`; `G/script/class/flower/flower1.lua:3–12`). Khi trễ, code hẹn từ thời điểm hiện tại, không có vòng bù số lần đã trễ (`S/Core/Src/KTaskFuns.cpp:120–129`).

[GIẢ THUYẾT — đề xuất tích hợp] Nếu dùng timer người chơi cho lửa trại, cần bộ điều phối chung để không chiếm mất timer khác; OnTimer kiểm đủ điều kiện rồi mới tính 0,5% và gọi API cấp thưởng đã chọn. AddOwnExp không tự nhân x2 hoặc duyệt đội, nên phải chủ động cấp từng người đủ điều kiện, đúng một lần mỗi nhịp; AddExp(...,...,1) lại chia theo công thức đội và áp hệ số đánh quái, không bảo đảm mỗi người nhận đúng 0,5% cấp riêng. Các điều kiện khu vực, hết 120 giây, rời đội, chết, thoát game, chống trùng phải được thiết kế trước triển khai (`S/Core/Src/ScriptFuns.cpp:15888–15918`; `S/Core/Src/KPlayer.cpp:2948–3056,3099–3154`; `S/Core/Src/KTaskFuns.h:63–65`; `D:/jx1-ops-wt/JX1_OPS/DESIGN/HAO-HUU-CUNG.md:24–26`).

## Chưa kiểm

- Binary gs có khớp source này hay không; file level_exp.txt thực nạp, dữ liệu trong PAK, cấu hình hệ số và trần cấp có hiệu lực. Chưa kiểm VM/SQL/server, không suy runtime từ source.
- Nhịp 18 tick có đạt một giây thật dưới tải, callback mất/trễ/trùng, chi phí cấp EXP và đồng bộ gói mỗi giây cho nhiều người chơi.
- Lua engine thực nạp được script/timer không, lỗi nháy servertimer có xuất hiện trong bản triển khai không; chưa chạy Lua compiler.
- Toàn bộ 398 dòng khớp AddOwnExp chưa truy bắc cầu; chỉ các mẫu công bố đã đọc thân. Tên Hán tự/chuỗi tiếng Việt hỏng mã hóa và script nằm trong PAK chưa chuẩn hóa/giải nén.
- Nhánh AddSumExp ở trần cấp/ngưỡng không hợp lệ, miền số khi cast Lua → int, tràn số nhân/cộng trong công thức EXP; chỉ nhận diện nguy cơ từ source, chưa có test tái hiện.
- Cách x2 tác động lên EXP mỗi giây hay EXP đánh quái, giữ/mất phần thưởng vượt cấp, làm tròn ở cấp thấp, trần số lần và chống nhiều lửa chồng nhau chưa được chốt.
- EXP riêng cho thực thể hảo hữu/NPC/pet, lưu/khôi phục timer qua đăng nhập và tương tác với các hoạt động đang chiếm timer chưa kiểm; không mặc định AddOwnExp dùng được cho NPC không có KPlayer.
- Build/test game không chạy theo task; kiểm chứng chỉ bằng đọc source, đối chiếu dẫn nguồn và tự đọc báo cáo.

## Lỗi công cụ và xử lý

- `rg : The term 'rg' is not recognized ...`: thử một lần; chuyển sang Select-String/đọc trực tiếp, không cài công cụ.
- Markdown đọc bằng encoding mặc định bị lỗi hiển thị; đã dùng UTF-8 cho đoạn cần đối chiếu, CP936 cho legacy. Lần lấy gộp quá nhiều dòng bị rút gọn; đã đọc lại các đoạn quyết định ngắn có số dòng.
- `Get-ChildItem -LiteralPath ... -Include` không lọc tên như dự kiến, đầu ra dài; đã lọc Name bằng Where-Object. Không dùng danh sách đó làm thống kê repository.
- `ReadAllLines` báo không tìm thấy `G/script/class/ontime_notify.lua` (đường được tham chiếu tại `G/Settings/TimerTask.txt:7`). Vòng đọc PowerShell còn giữ biến đoạn trước nên in lại dòng flower dưới nhãn đường thiếu; đã loại toàn bộ kết quả gán nhãn đó. Dùng `flower1.lua`/`flowerhead.lua` có tồn tại để nối timer–EXP; không kết luận có OnTimer trong file thiếu.

## Kiểm chứng và Git

- Đã tự đọc nội dung, phân biệt dữ liệu rời/source với runtime; không tạo script/parser phụ, không sửa BAI_HOC hoặc source.
- Đã xem diff một lần, `git diff --check` không báo lỗi; sửa dẫn nguồn thiết kế từ 25–28 thành 24–26 sau khi đối chiếu. Build/test không chạy theo task.
- **Commit BLOCKED. BỊ CHẶN – CHƯA PUSH.** Đã thử stage đúng hai file một lần, exit 128:

~~~text
git add -- JX1_OPS/REPORTS/A-08d-kinh-nghiem.md JX1_OPS/TASKS/A-08d.md
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-08d/index.lock': Permission denied
~~~

Git metadata ở ngoài writable root `D:\JX-wt\A-08d`; không được nâng quyền trong phiên này. Chưa stage được, lệnh commit chưa chạy, chưa có SHA/link GitHub. Không sửa ACL/config/credential hoặc dùng index thay thế để vượt quyền. Không chạy push vì người dùng chỉ yêu cầu commit.

PM tiếp tục từ hai file local bằng phiên có quyền ghi Git metadata, trên nhánh đã xác nhận `task/A-08d-codex`:

~~~text
git -C "D:\JX-wt\A-08d" add -- JX1_OPS/REPORTS/A-08d-kinh-nghiem.md JX1_OPS/TASKS/A-08d.md
git -C "D:\JX-wt\A-08d" commit -m "A-08d Khao sat kinh nghiem va diem gan timer Lua"
~~~
