TÓM TẮT 5 DÒNG
1. DONE — hoàn tất khảo sát tĩnh và đề xuất thiết kế; không sửa mã server/script.
2. Lửa tồn tại 120 giây logic, thưởng mỗi giây tối đa 120 lần; x2 EXP chiến đấu cho từng người đủ điều kiện trong tầm.
3. Thưởng riêng floor(EXP hiện tại / 200), không nhân x2; EXP hiện tại là tiến độ cấp, sẽ về 0 khi lên cấp trong mã đã đọc.
4. Đề xuất manager riêng ở vòng lặp server; không dùng Main theo phút hoặc ghi đè timer nhân vật.
5. [CHƯA KIỂM] runtime/binary và test; đã ghi file:dòng, cấu hình, rủi ro và tiêu chí xác minh.

# G-01 — Thiết kế lửa trại

- Trạng thái: **DONE** trong phạm vi khảo sát tĩnh và thiết kế. Đây là đề xuất, chưa triển khai.
- Ngày khảo sát: 17/11/2026. Workspace: `D:\JX-wt\G-01`; nhánh được kiểm tra một lần: `task/G-01`.
- Git ban đầu: `?? JX1_OPS/TASKS/G-01.md`. Giữ nội dung task có sẵn; chỉ bổ sung mục kết quả theo chỉ thị cuối task.
- Phạm vi ghi: báo cáo này và mục `## Kết quả` trong task. Không sửa source, cấu hình, bài học hay file khác.
- Không kết nối mạng/VM, không chạy game/server, không build/test thực thi. Không dùng Python, không đọc hoặc ghi khóa/mật khẩu.

## Nguồn và giới hạn bằng chứng

Đường dẫn task `D:\JX-source\SwordOnline` không tồn tại. Kiểm tra trực tiếp thư mục cha tìm thấy `server\jxOnline\gameserver\Sources`; dùng nhánh server này để khảo sát. Không lấy source từ Internet.

Quy ước đường dẫn trong bảng:

- `CORE` = `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src`.
- `GS` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs`.

Đã tìm tên file Lua liên quan EXP/timer/camp/fire trong `GS\script`, rồi đọc các file liên quan và tìm nội dung theo từ khóa lửa trại/campfire/bonfire/camp/fire/0.005. Không xác nhận được một script lửa trại hiện hữu. `camp` có kết quả chỉ phe chiến trường; `0.005` ở `tnlteam\mission\fenglingdu\npcdeath.lua:7` là xác suất rơi vật phẩm (dòng 8–10), không phải thưởng EXP. Kết quả tìm không chứng minh tính năng không tồn tại: tên/nội dung dùng bảng mã cũ hoặc dữ liệu khác có thể không khớp từ khóa. [CHƯA KIỂM] script lửa trại ngoài các kết quả này, dữ liệu NPC/skill liên quan và nguồn gốc chính xác của bản GS.

[CHƯA KIỂM] source có tương ứng binary đang dùng hay không; script được nạp thực tế, cấu hình server thực tế, hệ số thời gian thực tế và hành vi client. Không suy diễn kết quả runtime từ mã.

## Bằng chứng và điểm chèn

| File:dòng | Điều quan sát trực tiếp | Ý nghĩa thiết kế / điểm chèn đề xuất |
|---|---|---|
| `CORE\CoreServerShell.cpp:2232`, `:2237`, `:2238`, `:2263` | `Breathe()` có nhánh LogicFps=36 chạy `JxHalfLoop()` rồi return; nhánh đầy đủ gọi `g_SubWorldSet.MainLoop()` | Chèn lời gọi manager ở nhánh đầy đủ sau MainLoop, có chặn trùng giây logic; không đặt ở trước nhánh half-loop |
| `CORE\CoreServerShell.cpp:2227`, `:2244`, `:2248`, `:2250` | GAME_FPS=18; gọi `servertimer.lua::Main` khi modulo game time bằng 0 và giây hệ thống bằng 0 | Main hiện hữu không phải callback mỗi giây; không gắn payout 1 Hz vào Main |
| `GS\script\servertimer.lua:23`, `:25`, `:68`, `:69` | Main đọc thời gian; tác vụ khác duyệt 1..1199 và đổi `PlayerIndex` | Không sao chép giới hạn player cố định hoặc ngữ cảnh PlayerIndex vào manager mới |
| `CORE\KPlayer.cpp:261`, `:339` | Active bỏ qua kết nối -1/đổi server; kích hoạt `m_TimerTask` | Tham khảo điều kiện phiên; không chiếm timer chung |
| `CORE\KPlayer.h:269`; `CORE\ScriptFuns.cpp:5474`, `:5480`, `:5495` | Mỗi player có `m_TimerTask`; Lua SetTimer/StopTimer tác động timer đó | SetTimer riêng cho lửa có thể thay thế timer nhiệm vụ |
| `CORE\KTaskFuns.h:14`, `:54`, `:63`, `:64`; `CORE\KTaskFuns.cpp:118`, `:123`, `:129` | Timer ánh xạ qua settings/TimerTask.txt; hạn = game time + interval; callback đặt lịch tiếp từ thời điểm hiện tại | Timer tính theo game time, có độ trôi khi chậm; không tự bảo đảm 120 callback theo thời gian thực |
| `GS\script\header\timerhead.lua:4`, `:8` | FramePerSec=18, chia GetRestTime cho 18 | Tham khảo 18 tick/giây logic; [CHƯA KIỂM] nhịp runtime |
| `CORE\KPlayer.cpp:2936`, `:2943`, `:3040`, `:3056` | AddExp phân chia tổ đội rồi gọi AddSelfExp cho người nhận | Áp x2 theo người nhận sau chia tổ đội, tránh người ngoài tầm hưởng từ người hạ quái |
| `CORE\KPlayer.cpp:3099`, `:3104`, `:3115`, `:3116` | AddSelfExp chặn chết/hồi sinh; dùng ServerExp và mission value 27 | Giữ điều kiện này; không đổi hệ số toàn server để làm aura cục bộ |
| `CORE\KPlayer.cpp:3141`, `:3142`, `:3145`, `:3151`, `:3154` | m_CurrentUpExp hiện nhân 2; sau đó kiểm ServerExpLimit, cộng bộ đếm và m_nExp | Điểm chèn aura sau block x2 hiện hữu, trước kiểm giới hạn; cần phép tính rộng và giới hạn chính xác |
| `CORE\KPlayer.cpp:3157`, `:3159` | Skill120Rate dùng nGetExp để cộng EXP skill | Nếu x2 đặt trước đây, EXP skill cũng bị ảnh hưởng; cần chính sách và test rõ ràng |
| `CORE\KPlayer.h:387`, `:388`; `CORE\ScriptFuns.cpp:15876`, `:15881` | m_nExp/m_nNextLevelExp là int; GetExp trả m_nExp | Không hiểu 0,5% là EXP trọn đời hay EXP cần lên cấp |
| `CORE\ScriptFuns.cpp:15889`, `:15902`, `:15904`, `:15909`, `:15917` | AddExp Lua đi qua luồng combat; AddOwnExp gọi DirectAddExp | Không gọi AddExp cho thưởng định kỳ vì sẽ ăn hệ số combat/độ lệch cấp |
| `CORE\KPlayer.cpp:3232`, `:3235`, `:3241`, `:3244`, `:3249` | DirectAddExp kiểm cấp trần rồi cộng int, có LevelUp; không có kiểm chết/hạn ngày trong hàm này | Không gọi trần API này từ payout; bọc bằng kiểm điều kiện, hạn mức và chống tràn |
| `CORE\KPlayer.cpp:3264`, `:3266`, `:3271`, `:3273` | LevelUp đặt m_nExp=0, tăng một cấp rồi tính ngưỡng mới | EXP dư có thể mất khi cộng vượt ngưỡng bằng DirectAddExp |
| `CORE\ScriptFuns.cpp:15922`, `:15933`, `:15935`, `:15945` | AddSumExp lặp từng ngưỡng và gọi DirectAddExp | Tham khảo ý tưởng chia phần qua cấp; chưa đủ bảo vệ tiến triển/giới hạn cấp để dùng nguyên trạng |
| `CORE\ScriptFuns.cpp:5361`, `:5372`, `:5379`, `:5383`, `:5384` | GetWorldPos lấy GetMpsPos, trả map ID và tọa độ chia 32 | Aura native nên dùng MPS và subworld instance, tránh trộn đơn vị tọa độ/map ID |
| `GS\script\skill\special\expbonus.lua:3`, `:4` | Script trả tham số expenhance_p theo level*100 và thời lượng 64800 | Có dữ liệu buff EXP, chưa xác nhận nó tương ứng hệ số combat trên; không tái dùng skill này như tính năng hoàn chỉnh |

Các dòng trên thuộc bản source đã đọc, không phải cam kết offset cho bản khác. File manager, helper và cấu hình lửa mới bên dưới là tên đề xuất, chưa tồn tại/được đăng ký qua khảo sát này.

## Hợp đồng hành vi đề xuất

1. Một lần kích hoạt hợp lệ tạo một lửa cố định, tồn tại 120 giây logic. Không hiểu yêu cầu này thành tự tạo lại lửa vô hạn sau mỗi 120 giây. Lần tiếp theo cần kích hoạt mới hợp lệ.
2. X2 áp dụng EXP chiến đấu theo luồng AddSelfExp cho người nhận ở trong tầm tại lúc nhận EXP; không nhân EXP nhiệm vụ, vật phẩm, thưởng trực tiếp hoặc chính thưởng 0,5%. Vì Lua AddExp cũng vào AddSelfExp, khi triển khai phải bổ sung nguồn EXP hoặc tách wrapper combat để Lua thưởng nhiệm vụ không vô tình hưởng aura. [CHƯA KIỂM] toàn bộ call site ngoài các file đã đọc.
3. EXP hiện tại là `m_nExp` tại đầu lần thưởng: `delta = floor(max(0, m_nExp) / 200)`. Tính lại mỗi giây, không chụp cố định lúc vào lửa. Ví dụ 10.000 EXP cho 50 ở lần đầu; lần sau tính trên 10.050. Nếu dưới 200 thì thưởng 0; không ép tối thiểu 1 và không giữ phần lẻ giữa lần thưởng.
4. Mỗi giây tối đa một thưởng cho một nhân vật, dù có nhiều lửa chồng nhau. Vào/ra tầm, đăng nhập lại hoặc đổi lửa không tạo thưởng tức thì hay đặt lại lịch.
5. Đủ điều kiện: phiên đang kết nối, không chuyển server, NPC hợp lệ, còn sống/không hồi sinh, cùng subworld instance, bản đồ cho phép, nằm trong bán kính, chưa đạt giới hạn cấp/EXP/ngày. Điều kiện cấp/hạn mức chặn payout; aura combat vẫn tuân thủ điều kiện của luồng combat.
6. X2 của lửa không cộng dồn với lửa khác. Đề xuất mặc định không chồng với `m_CurrentUpExp`: hệ số nhóm x2 là max(buff hiện có, aura), do đó đang có buff x2 vẫn là x2. ServerExp/mission giữ nguyên như hiện tại. Đây là chính sách đề xuất, không phải chứng cứ về behavior hiện tại.
7. Đề xuất EXP skill giữ kết quả theo chính sách cũ, không nhận thêm phần aura. Cần lưu nGetExp trước aura cho phần Skill120Rate; không đặt nhân x2 vào một biến dùng chung rồi vô tình nhân EXP skill.
8. Khi lên cấp, dùng EXP hiện tại của cấp mới ở lần kế tiếp. Không có EXP chiến đấu bổ sung thì m_nExp=0 dẫn đến payout 0. Không đổi nghĩa sang 0,5% ngưỡng cấp hoặc tổng EXP khi chưa có yêu cầu mới.

Không chạm cấp và bỏ qua làm tròn, sau 120 lần: `E120 = E0 * 1.005^120 ≈ 1,8194 * E0`, tức tăng khoảng 81,94%. Đây là tính chất công thức, không phải kết quả test; không phải tăng tuyến tính 60%. EXP combat làm thay đổi nền tính; lên cấp làm chuỗi tính trên tiến độ cấp mới.

## Vòng lặp và vòng đời

Đề xuất `CampfireManager` sở hữu các instance `{id, generation, subworldInstance, mpsX, mpsY, startTick, endTick, nextOrdinal}`. Mỗi instance có endTick = startTick + 120 * ticksPerSecond; cấu hình mặc định 18 dựa trên source. Dùng thời gian logic cùng engine và phép so sánh chống wrap; [CHƯA KIỂM] 120 giây logic tương đương đúng 120 giây đồng hồ khi lag/tạm dừng. Nếu sản phẩm đòi thời gian thực phải chọn monotonic clock rõ ràng và test riêng.

- Gọi Update sau `MainLoop()` ở nhánh đầy đủ của Breathe, trước return tại `CoreServerShell.cpp:2264`. Đặt chặn theo slot thời gian, không theo số lần Breathe được gọi.
- X2 có hiệu lực trong `[startTick, endTick)`. Lịch thưởng là start+1 giây đến start+120 giây, tối đa 120 lần. Ở mốc cuối, chỉ cho phép xử lý lần thưởng thứ 120 khi đúng hạn và đủ điều kiện, rồi hủy lửa; kiểm combat ở endTick đã không còn x2. Quy định này loại bỏ nhập nhằng giữa cleanup và lần thưởng cuối.
- Khi callback đến muộn: nếu đã quá endTick thì hủy ngay, không trả bù. Nếu còn sống, xử lý tối đa một lần cho slot hiện tại, đánh dấu các slot đã bỏ lỡ và lập nextOrdinal theo thời gian gốc; không dịch endTick và không burst nhiều thưởng trong một vòng.
- Dùng một bảng xét người nhận chung mỗi giây trên các lửa trong cùng instance. Khóa chống trùng là định danh nhân vật ổn định + epoch slot server, không chỉ player index có thể tái sử dụng, cũng không chỉ campfireId. Đánh dấu và ghi EXP trong cùng lượt logic server; callback trùng không thể thưởng lại.
- Kiểm tra membership ở thời điểm payout; phép tính native `dx*dx + dy*dy <= radiusMps*radiusMps` dùng số nguyên rộng. X2 phải tra membership tại sự kiện EXP hoặc kiểm lại vị trí; cache một giây không được để người đã ra ngoài vẫn hưởng.
- Hủy khi hết hạn, unload map, xóa lửa hoặc shutdown. Mặc định restart không phục hồi lửa/thưởng lỡ; trạng thái kích hoạt/cooldown phải có cơ chế chống dùng lại sau reconnect/restart nếu dùng vật phẩm. [CHƯA KIỂM] hook unload, lưu cooldown, giao dịch vật phẩm và vòng đời NPC; cần đọc đúng các symbol đó trong task triển khai tiếp.
- Chia chỉ mục theo subworld/region để không quét mọi player × mọi lửa mỗi frame. Chỉ payout một lần/giây; số lửa tối đa phải bị chặn ở lúc tạo.

Không triển khai bằng chuỗi SetTimer của mỗi player; không dùng LuaSetSubTimer ở `ScriptFuns.cpp:5484` vì đoạn đã đọc chỉ tạo biến timer local, chưa có bằng chứng lưu/activate timer đó.

## Cộng EXP an toàn

Đề xuất helper native mới `GrantCampfireExp`, đặt cạnh `DirectAddExp` (`KPlayer.cpp:3232`) và khai báo cạnh API EXP trong KPlayer.h khi triển khai sau:

- Tính delta bằng số nguyên rộng trước khi nhân/chia, chặn âm, chặn vượt miền int, chặn cả tổng hiện có + delta. Với tỷ lệ mặc định có thể chia 200 trực tiếp để tránh nhân trung gian.
- Hạn ngày dùng phần còn lại thật sự: `accepted = min(delta, dailyRemaining, tickCap, numericRemaining)`; bộ đếm tăng theo số đã nhận. Luồng AddSelfExp hiện chỉ kiểm `nLeftExp > g_ExpLimit` trước cộng (`:3148`), nên không được coi nó đã bảo đảm không vượt hạn ở biên.
- Nếu chia phần để bảo toàn EXP dư khi lên cấp, luôn kiểm cấp trần và bảo đảm phần còn lại giảm hoặc dừng có lý do. Không gọi vòng lặp vô hạn khi DirectAddExp không tiến triển do chạm cấp trần. Không sửa LevelUp toàn hệ thống trong phạm vi tính năng này.
- Tái dùng đồng bộ EXP/cấp của server; không tự gán m_nExp từ Lua, không nhận số EXP/vị trí/hạn giờ do client gửi.
- Payout không đi qua team share, ServerExp, mission bonus, buff x2 hay Skill120Rate. Nếu muốn thưởng cũng trừ hạn ngày dùng bộ đếm có thẩm quyền chung đã chọn; không tự lấy task ID mới hoặc ghi đè mission value 27.

## Cấu hình đề xuất

Tất cả khóa dưới đây là mới, chưa xác nhận có trong GS. Nên đặt namespace `[Campfire]` trong cấu hình tính năng riêng, load một lần/refresh có kiểm tra; không đọc INI cho từng người từng frame.

| Khóa | Giá trị đề xuất | Ràng buộc |
|---|---|---|
| Enabled | 0 khi bàn giao code | Chỉ bật ở đợt triển khai được duyệt |
| DurationSeconds / IntervalSeconds | 120 / 1 | Cố định cho yêu cầu này; không nhận giá trị từ client |
| CombatMultiplier / RewardBasisPoints | 2 / 50 | 50 basis points = 0,5%; thưởng không chịu multiplier |
| ExpBasis / Rounding | CurrentLevelProgress / Floor | Tính lại mỗi payout |
| RadiusMps | 320, chỉ là đề xuất | Tương đương 10 đơn vị GetWorldPos; cần đo cảm giác chơi, [CHƯA KIỂM] |
| StackPolicy | MaxWithinDoubleGroup | Hai lửa không x4; buff x2 hiện có không x4 |
| AffectsSkillExp | 0 | Tách phần aura khỏi EXP skill |
| CountTowardDailyExpLimit | 1 | Đồng bộ hạn ngày với chiến đấu; không vượt phần còn lại |
| AllowedMaps | Rỗng mặc định | Bật theo danh sách; so thêm instance khi xét người nhận |
| MaxActivePerMap / MaxActivePerCharacter | 4 / 1 | Đề xuất ban đầu, cần đánh giá tải |
| ActivationCooldownSeconds | 300 | Đề xuất chống spam, lưu theo nhân vật nếu dùng vật phẩm |
| TickCap / DailyCap | Chưa chốt | Không bật khi chưa có hạn mức hợp lệ và được duyệt cân bằng |
| CatchUp / PersistActiveFire | 0 / 0 | Không trả bù, không phục hồi lửa sau restart |

Nguồn kích hoạt (NPC/vật phẩm/sự kiện), vật phẩm bị tiêu hao, map được phép và mức trần cụ thể chưa được task quy định. Thiết kế API tạo lửa server có kiểm quyền; [CHƯA KIỂM] đường nối script kích hoạt và NPC hiển thị. Không tự bịa ID NPC, skill, timer hoặc task save.

## Rủi ro lạm dụng và biện pháp

| Rủi ro | Biện pháp đề xuất |
|---|---|
| Nhiều lửa, ra/vào biên, reconnect để nhận nhiều lần | Khóa nhân vật + slot toàn server, không reset khi đổi lửa; một giao dịch logic cho payout |
| Buff dính sau ra tầm/đổi map hoặc player index tái dùng | Kiểm vị trí tại sự kiện; định danh ổn định + generation; cleanup map/session |
| X2 lây sang cả tổ đội hoặc thưởng nhiệm vụ | Xét từng người sau team share; nguồn EXP tường minh; audit call site trước triển khai |
| Nhân chồng buff x2 thành x4/x8 | Nhóm max x2, không đụng trực tiếp m_CurrentUpExp để tránh xóa buff khác |
| AFK/multi-account nhận EXP lãi kép | Hạn ngày, số lửa, cooldown; xác định rõ chính sách AFK. Không tự theo dõi IP/thiết bị trong task này |
| Tràn int, mất EXP dư, vòng lặp tại cấp trần | Số rộng, clamp trước cộng, chia phần có tiến triển, dừng tại max level |
| Lag tạo burst hoặc kéo dài lửa | endTick cố định, không catch-up, chặn slot trùng, log slot bỏ lỡ |
| Spam tạo NPC/lửa làm tăng tải | Hạn số lửa, chỉ mục không gian, cooldown và kiểm kích hoạt server |
| Log nhạy cảm | Chỉ log ID nội bộ cần thiết, fireId, slot, EXP trước/thực nhận và lý do từ chối; không account/password/token |

## Ma trận test cho đợt triển khai sau — tất cả [CHƯA KIỂM]

Không chạy test/build trong task khảo sát. Các ca sau là tiêu chí cần kiểm trong môi trường thử riêng khi được duyệt:

| Ca | Kỳ vọng |
|---|---|
| 120 giây, callback lặp cùng tick | Không quá 120 payout, slot trùng không đổi EXP; hết hạn không còn x2 |
| Biên 0/1/119/120/>120 giây | Không payout tại tạo; lần 1 ở giây 1; lần cuối đúng hạn ở 120 rồi hủy; đến muộn sau hạn không bù |
| EXP 0, 199, 200, 10.000 | Delta lần đầu lần lượt 0, 0, 1, 50; lần sau dùng EXP mới |
| Cùng map khác instance; đúng biên/ngoài bán kính | Chỉ cùng instance và khoảng cách <= R hưởng; không trộn MPS với tọa độ /32 |
| Tổ đội có người trong/ngoài tầm | Chỉ người nhận trong tầm được x2 sau phân phối; không đổi phần cơ sở của đồng đội |
| Combat so với quest/AddExp Lua/direct/tick | Chỉ nguồn combat được aura; tick luôn đúng 0,5%, không chịu ServerExp/x2/chia đội |
| Buff x2 sẵn có + hai lửa | Hệ số nhóm là 2; bỏ aura không làm mất buff cũ |
| Skill120Rate bật | Phần EXP skill giữ chính sách đã chọn; aura không làm tăng ngoài dự kiến |
| EXP sát ngưỡng, nhiều cấp, max level | Lên cấp đồng bộ; phần dư theo helper; không lặp kẹt; payout kế dùng tiến độ cấp mới |
| INT_MAX, hạn ngày -1/đúng hạn/còn ít | Không âm/tràn; thực nhận <= phần còn lại; bộ đếm khớp |
| Chết/hồi sinh/offline/exchange server | Không payout; reconnect không reset slot/cooldown |
| Lag 3 giây, pause, restart, unload | Không burst/bù; không kéo dài deadline; không orphan aura; lửa không tự phục hồi |
| LogicFps 18/36 | Một slot logic chỉ một lần; đo đủ 120 giây đồng hồ riêng để xác nhận yêu cầu thời gian thực |
| Tải nhiều player và lửa đạt giới hạn | Đo thời gian Update, số xét membership, log từ chối; không quét N×F mỗi frame |

## Lỗi, cách xử lý và phần chưa xác minh

- `Cannot find path 'D:\JX-source\SwordOnline' because it does not exist.` Đã kiểm tra cha một lần, dùng `D:\JX-source\server\jxOnline` có cấu trúc gameserver/Sources. Sai lệch đường dẫn được giữ trong báo cáo, không sửa task gốc.
- `rg : The term 'rg' is not recognized ... CommandNotFoundException`. Không cài hay đổi môi trường; chuyển sang Get-ChildItem có giới hạn nhánh/file và Select-String. Không thử lại rg.
- Lần đọc đầu task thiếu chỉ định UTF8 làm tiếng Việt hiển thị sai; đã đọc lại đúng Encoding UTF8. Source/script legacy có comment sai bảng mã; bằng chứng hành vi lấy từ symbol/câu lệnh ASCII, không dịch đoán comment.
- Tra các đường dẫn AGENTS/file báo cáo tùy chọn chưa tồn tại không tạo chúng. Không có checkpoint/báo cáo G-01-campfire-design.md để ghi đè tại thời điểm kiểm tra.
- [CHƯA KIỂM] runtime/binary, build, benchmark, nhịp đồng hồ, script lửa trại có tên/bảng mã khác, call site EXP toàn hệ thống, lifecycle unload, giao dịch kích hoạt và dữ liệu cooldown. Không coi đây là tính năng đã chạy.
- Bước tiếp tục: khi được giao triển khai riêng, xác nhận bản source/binary mục tiêu, nguồn kích hoạt/map/radius/hạn mức; đọc đúng call site và lifecycle còn thiếu, rồi triển khai trên copy với test ở trên.

- Kiểm tra diff phát hiện CR cuối dòng cuối bị báo `trailing whitespace` ở hai file; đã chuẩn hóa phần xuống dòng được thêm và kiểm tra lại. Không thay nội dung task ban đầu.

## Bàn giao và Git

Chỉ tạo báo cáo và bổ sung kết quả task. Không stage/commit/push vì task không yêu cầu công bố Git và không cho phép mạng thật. Commit SHA: không có commit mới. Link GitHub: không có. Chưa push: giữ bản local theo phạm vi khảo sát, không gặp lỗi xác thực hoặc tự thay cấu hình/credential.
