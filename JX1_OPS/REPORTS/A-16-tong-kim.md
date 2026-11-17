TÓM TẮT 5 DÒNG
1. [NGUỒN] Bảng mission gốc trỏ ID 11 tới Tống Kim nhánh tnlteam: 100 người/phe, chênh lệch 2; nhánh battles cũ đặt 150 người/phe.
2. [NGUỒN] Trần chiến báo là 10 hạng; đây không phải trần người tham chiến, số bản đồ hay số hoạt động.
3. [NGUỒN] Đếm 249 file dữ liệu bản đồ: 233 bảng tọa độ có tiêu đề với 16.906 dòng dữ liệu, 15 MapInfo và 1 bảng khác 19 dòng.
4. [CHƯA BIẾT] Không tìm thấy JoinActivityGroup trong văn bản đã quét; có JoinMission/AddMSPlayer, chưa chứng minh tương đương API hay runtime.
5. DONE khảo sát tĩnh ngày 2026-11-17; đã lưu nháp trước bản cuối, không sửa mã, không mạng/VM/exe; ca test giao TESTER chưa chạy.

## Phạm vi và cách đọc bằng chứng

- Task `A-16`, worktree `D:\JX-wt\A-16`, nhánh đã kiểm tra `task/A-16`. Task ban đầu là file untracked; giữ nội dung gốc và chỉ thêm mục Kết quả theo yêu cầu trực tiếp trong task.
- `S` = `D:\JX-source\server\jxOnline\gameserver` (mã server).
- `G` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs` (script/settings bản gói gốc, không phải VM).
- `C` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` (client gốc).
- Các dẫn chiếu dạng `G/script/...:268` là file:dòng, số dòng vật lý bắt đầu từ 1. Chỉ trích symbol, số liệu và vài mẫu; không sao chép nguyên bảng/source. Nhãn [NGUỒN] xác nhận nội dung tĩnh đã đọc, không khẳng định binary đang chạy dùng đúng nội dung đó.
- Đếm trực tiếp byte bằng Python `-I`, không chạy/import script của gói game. Phân loại bảng theo dòng đầu `XPOS<TAB>YPOS`, `TRAPX<TAB>TRAPY` hoặc `[MapInfo]`; loại tiêu đề và dòng trắng khi đếm dữ liệu. File còn lại không tự suy đoán có tiêu đề. Không bung PAK, không tìm kiếm tài khoản/khóa, không đọc SQL/dump.

## ĐÃ XÁC MINH

### 1. Dữ liệu gốc và số lượng

| Nguồn | Số lượng đo trực tiếp | Diễn giải / bằng chứng |
|---|---:|---|
| `G/settings/Task/missions.txt` | 33 mục, 33 khóa khác nhau | Tiêu đề dòng 1; dữ liệu dòng 2–34. Dòng 12: ID `11` → `script/tnlteam/mission/battlesongjin/butcher/mission.lua`. Đây là toàn bảng mission, không phải 33 hoạt động Tống Kim. |
| `G/settings/TimerTask.txt` | 47 mục, 47 khóa khác nhau | Dòng 1 là tiêu đề; dòng 40, 41: timer `39`, `40` trỏ nhánh `tnlteam/mission/battlesongjin`. Không suy ra timer đang được kích hoạt. |
| `G/settings/RankSetting.txt` | 100 khóa; 89 khóa có nhãn, 11 khóa không có nhãn | Dòng 2–101: ID 1–100; ví dụ ID 1 tại dòng 2, ID 90 chỉ có khóa tại dòng 91. Đây là danh mục rank chung, không phải danh sách 100 người hay 100 hạng chiến báo. |
| `G/settings/battles/maps` | 249 file `.txt`, 16 thư mục bản đồ | Tổng toàn cây, không quy đổi thành số map ID đang nạp. |
| Bảng `XPOS/YPOS` trong cây trên | 171 file, 13.980 dòng dữ liệu | Ví dụ `boss/bossµã2.txt:1`: 10 dòng dữ liệu; dòng 2 có `(1720,3046)`. |
| Bảng `TRAPX/TRAPY` trong cây trên | 62 file, 2.926 dòng dữ liệu | Ví dụ `desert/´óÓª2.txt:1`: 29 dòng dữ liệu; dòng 2 có `(64288,109408)`. Giữ nguyên tên file legacy trên đĩa. |
| File `[MapInfo]` mang đuôi `.txt` | 15 file | Ví dụ `boss/mapinfo.txt:1`, dòng 3 `Area_Count=2`; đây là dạng INI, không đếm thành hàng tọa độ. |
| Bảng khác `lingyuguan/trap_1.txt` | 1 file, 19 dòng không trắng | Dòng 1 bắt đầu bằng `0`, có 4 cột; không thấy tiêu đề `XPOS/YPOS` hoặc `TRAPX/TRAPY`, nên giữ đủ 19 dòng, không trừ nhầm một dòng. |

Kiểm tra cộng: `171 + 62 + 15 + 1 = 249`; bảng tọa độ có tiêu đề: `233` file và `13.980 + 2.926 = 16.906` dòng. Đây là số dòng dữ liệu, chưa khử tọa độ trùng và không phải số NPC được sinh đồng thời. Ví dụ `lingyuguan/trap_1.txt:1` và `:2` có cùng các cột tọa độ đầu.

Lua cũ đọc các bảng này theo chiều cao trừ tiêu đề: `G/script/battles/battlehead.lua:345` (`bt_addtrap`, vòng `1..count-1` tại dòng 351), `:367` (`bt_getadata`, chọn hàng ngẫu nhiên sau tiêu đề tại dòng 368–371). Việc có bảng trong gói không chứng minh nhánh Tống Kim hiện tại sử dụng tất cả bảng.

### 2. Các nhánh hoạt động và điều kiện tham gia

Nhánh có liên kết trực tiếp từ bảng mission:

`G/settings/Task/missions.txt:12` → `tnlteam/.../butcher/mission.lua:3` include `head.lua` → `head.lua:5` đặt `MISSION_ID = 11`. `S/Sources/Core/Src/KCore.cpp:908` nạp bảng mission qua `TASK_MISSION_SETTING_TABFILE`; `ScriptFuns.cpp:22738` tra script theo ID mission. Đây là liên kết nguồn và dữ liệu, chưa xác minh đường dẫn bảng được binary chọn thực tế.

| Điều kiện / cấu hình | Nhánh `G/script/tnlteam/mission/battlesongjin` | Nhánh `G/script/battles` cũ |
|---|---|---|
| Thêm người vào phe | `butcher/head.lua:380`: `AddMSPlayer(MISSION_ID, n_camp)`; trước đó chỉ nhận phe 1 hoặc 2 tại dòng 327 | `battlejoin.lua:268`: `JoinMission(GAME_RULEID, bt_ncamp)` |
| Trần người/phe | `battlehead.lua:180`: 100; `butcher/head.lua:333` từ chối khi số hiện tại `>= 100` | `marshal/head.lua:31`, `butcher/head.lua:29`, `guozhan/head.lua:33`: 150; kiểm tra lần lượt tại `:440`, `:454`, `:418` |
| Chênh quân | `battlehead.lua:182`: 2; `butcher/head.lua:345`, `:351` từ chối phe đang hơn `>= 2` | `battlehead.lua:244`: 5; `battlejoin.lua:362`, `:365` kiểm tra chênh `>= 5`. Quốc chiến có nhánh đặc biệt tại `:353` và ngưỡng 100 tại `battlehead.lua:245`, không được gọi chung là trần cứng 100. |
| Phí | `butcher/head.lua:9`: 200.000; kiểm tra tiền tại `:310`, gọi `Pay` tại `:400` | `battlejoin.lua:427` kiểm tra 3.000 ở nhánh kiểm tra quốc chiến; không áp thành phí mọi chế độ |
| Map báo danh / chiến trường | `battlehead.lua:100`: 3 map 323/324/325; `:138`: 1 nhóm chứa 3 map 378/379/380 | `battlehead.lua:273`: 3 map báo danh 323/324/325 |
| Phân cấp | `battlehead.lua:238`: `>40 && <80` → 1; `:240`: 80–119 → **3**; `:242`: từ 120 → 3; còn lại → 0 | `battlejoin.lua:39` chặn dưới 40; 40–79 → 1, 80–119 → 2, từ 120 → 3 |
| Thời gian cấu hình | `battlehead.lua:13`: báo danh 10 phút; `:14`: trận 30 phút | Không gộp lịch giữa các nhánh |

Điểm cần lưu ý từ nguồn: cấp đúng 40 trả 0 ở hàm phân cấp TNL; cấp 80–119 trả 3 dù comment nhắc trung cấp. Chưa kết luận giao diện/NPC thực tế có gọi hàm này trong mọi đường vào. `butcher/head.lua:95` đến `:101` của TNL mở riêng phần tử map thứ 3 trong `but_battlestart()`, còn `but_battlestart__()` ở dòng 71 duyệt cả nhóm. Không được kết luận 3 map đều đang mở.

Nhánh thứ ba `G/script/header/tongkim.lua` tồn tại: `:14` có 3 kiểu, `:21` có 3 cặp giờ `{13,1}`, `{19,1}`, `{21,2}`, `:27` có 5 mốc rank, `:35` có 6 nhãn. Tuy nhiên include tại dòng 3 trỏ `script/feature/tongkim/LIMITED_1_ACCOUNT.lua`, trong khi cây `G/script/feature/tongkim` không tồn tại ở bản gói đã đọc. Xếp nhánh này là nội dung có sẵn chưa xác nhận sử dụng, không lấy lịch của nó làm lịch hoạt động chính thức.

`G/script/servertimer.lua:52` comment lời gọi `active_tongkim()`; hàm ở `:141` include nhánh TNL tại `:144` và có điều kiện phút 50 tại `:148`. Chưa tìm toàn bộ scheduler/caller, nên chỉ xác nhận lời gọi ở vị trí này bị comment, không kết luận hoạt động chắc chắn tắt.

### 3. JoinActivityGroup: kết quả tìm và API thực sự thấy

[NGUỒN] Tìm không phân biệt hoa thường cả `JoinActivityGroup` và `JoinActivity` trong các file `.cpp/.h/.c/.lua/.txt/.ini`, bỏ `.git_old`:

| Cây đã quét | File văn bản thuộc bộ lọc | Kết quả |
|---|---:|---|
| `D:\JX-source\server\jxOnline` | 2.417 | 0 dòng khớp |
| Client gốc `.../Client` | 5.253 | 0 dòng khớp |
| `G` | 6.136 | 0 dòng khớp |

Đây là kết quả âm trong phạm vi cụ thể, không chứng minh API vắng mặt trong binary, thư viện đóng gói, PAK hay biến thể source khác. Không tự thay `JoinActivityGroup` bằng API khác.

Luồng có bằng chứng: `G/script/battles/battlejoin.lua:268` gọi `JoinMission`; `S/Sources/Core/Src/ScriptFuns.cpp:22708` (`LuaJoinMission`) kiểm tra player/subworld/mission/phe, tra script ở `:22738`, gọi `KMission::JoinMission` tại `:22740`; `KMission.cpp:86` lấy script và `:107` gọi callback Lua tên `JoinMission`. Với TNL đã thấy đường trực tiếp `but_join` → `AddMSPlayer` ở mục 2. Hai đường có cấu trúc khác nhau; chưa chứng minh một đường là wrapper của đường kia.

### 4. Trần hiển thị và các đường dữ liệu khác nhau

| Tầng | Giới hạn / bằng chứng | Ý nghĩa |
|---|---|---|
| Client: dữ liệu chiến báo | `C/gamecore/GameDataDef.h:428`: `MISSION_STATNUM = 10` | Có 10 slot hạng mission |
| Client: nhận từng hạng | `C/gamecore/KProtocolProcess.cpp:2283` (`s2csyncrankdata`); `:2297` chặn index ngoài `[0,9]`, `:2306` chép một phần tử | Index 10 không được ghi vào mảng mission |
| Client: đọc/UI | `C/gamecore/CoreShell.cpp:1251` chặn index ngoài giới hạn; `C/vn/gameui/KuiCometoMapVN.cpp:1396` duyệt `i < MISSION_STATNUM` | Chiến báo VN vẽ tối đa 10 hạng; header `C/gameui/KuiCometoMap.h:173` khai báo mảng tương ứng |
| Gói ladder chung | `S/Headers/KProtocol.h:2535` và `C/gamecore/KProtocol.h:2393`: `StatData[10]` | Chứa tối đa 10 `TRoleList` trong khai báo nguồn |
| Client: nhận ladder chung | `C/gamecore/KProtocolProcess.cpp:5328` (`LadderResult`), `:5333` cấp 10 phần tử, `:5336` duyệt đủ 10, `:5345` phát thông báo 10 mục | Đây là đường rank chung, không tự động đồng nghĩa cập nhật `m_MissionRank` chiến báo |
| Server: ladder Tống Kim riêng | `S/Sources/Core/Src/ScriptFuns.cpp:24639` kiểm tra kích thước `>10`; `:24722` chặn `count>=10` trong `SendRank` | Có ý định cắt top 10; cần kiểm tra lỗi tĩnh bên dưới trước thử đông người |

Số điểm cũng có giới hạn biểu diễn ở một đường: `S/Sources/Core/Src/KMission.h:198` và `S/Headers/KProtocol.h:2539` dùng `unsigned short point`; client tương ứng tại `C/gamecore/KProtocol.h:2397`. Với kiểu 16 bit, miền biểu diễn là 0–65.535. Chưa xác minh ABI/binary hoặc phép xử lý tràn thực tế; không áp mốc này thành giới hạn điểm gameplay của mọi nhánh, đặc biệt đường `SetPlayerParam`/mission.

### 5. Rủi ro phát hiện qua source, chưa tái hiện runtime

1. **Vượt top 10 truy cập iterator `end()`:** `S/Sources/Core/Src/ScriptFuns.cpp:24639` kiểm tra `size()>10`, dòng 24641 gán `it = ...end()`, dòng 24642 `delete (*it)`, dòng 24643 `erase(it)`. Với `std::set` được khai báo ở `KMission.h:281`, `end()` không trỏ phần tử hợp lệ. Lỗi tĩnh rõ tại nhánh này; chưa chứng minh phiên game hiện tại đi qua nhánh hoặc crash. Không sửa theo phạm vi task.
2. **Hạng đồng điểm có thể bị gộp:** `KMission.h:174` (`PlayerRank::Compare`) so điểm rồi số giết player; tại dòng 187 kiểm tra `npc == src->npc`, bên trong dòng 189 lại yêu cầu `npc > src->npc`; nhánh đó không thể đúng. Comparator không có khóa ID cuối cùng. Trong `std::set`, các player khác ID có cùng điểm/số giết có thể bị coi tương đương. Cần tester dùng dữ liệu tách biệt và đồng hạng.
3. **Gói rank có trường chưa được gán:** `ScriptFuns.cpp:24701` khai báo `LADDER_DATA LadderData` không zero-init. Vòng tại `:24724` gán tên `StatData[count]`, nhưng không gán `nValue`/`bySort`; phía client vẫn đọc chúng tại `KProtocolProcess.cpp:5342`. Khi ít hơn 10 tên, client vẫn đọc đủ 10 slot tại `:5336`. Cần kiểm tra dữ liệu thừa/rác hoặc chuỗi thiếu kết thúc; chưa xác minh hành vi binary.
4. **Không đồng nhất đường chiến báo:** server `SendRank` gửi `s2c_ladderresult` tại `ScriptFuns.cpp:24702`; client xử lý nó bằng `LadderResult`, trong khi UI chiến báo đọc `m_MissionRank` được cập nhật bởi `s2csyncrankdata`. Không có bằng chứng ở các hàm này cho phép gộp hai đường thành một. Một số API `LuaBT_*` còn là stub `return 0`, ví dụ `BT_ViewBattleStart` tại `:24592`, `BT_BroadAllLadder` tại `:24597`, `BT_BroadView` tại `:24612`, dù vẫn đăng ký ở `:26876`, `:26877`, `:26880`.

## CHƯA XÁC MINH

- Chưa chạy client/server, chưa build, chưa thử đăng nhập/hoạt động/gửi gói, chưa đo hiệu năng. Các ca bên dưới đều **CHƯA CHẠY** đúng giới hạn khảo sát tĩnh.
- Binary đang dùng bản script/settings nào, có override từ PAK hay thư viện Lua khác không; source `D:\JX-source` có khớp binary không; nhánh TNL/cũ/header nhánh nào thực sự được gọi.
- Định nghĩa/ý nghĩa thực của `JoinActivityGroup`; cần người giao task chỉ file/module hoặc bộ dữ liệu khác chứa symbol nếu muốn theo tiếp chính API này. Không coi thiếu symbol là blocker của báo cáo khảo sát hiện tại.
- Chưa khẳng định đầy đủ điều kiện tham chiến, lịch mở, giới hạn tổng người, bảo đảm cân bằng khi nhiều người vào đồng thời, phí thật bị trừ, hay mọi tài nguyên của 249 file đều được dùng.
- Chưa xác minh encoding tiếng Việt legacy và hiển thị font. Số liệu đếm theo byte; tên hiển thị diễn giải bằng tiếng Việt, không chuyển mã/sửa file gốc.

## Ca test cho TESTER

Chỉ thực hiện sau khi được giao quyền chạy trên môi trường thử riêng; task này không khởi động môi trường. Dùng nhân vật giả, giữ bản gốc, không ghi log tài khoản thật. Mỗi ca cần ghi bản binary/script/settings, số người từng phe, log đã lọc và ảnh chiến báo; phân biệt đường TNL, Lua BT cũ và ladder chung.

| Ca | Thiết lập / thao tác | Đối chiếu và kết quả cần ghi |
|---|---|---|
| TK-01 | Kiểm tra loader bảng mission, NPC báo danh và scheduler trong bản thử | Xác nhận mission 11 có thực sự dùng TNL; gọi từ đâu; map thứ 3 hay cả 3 map mở. Không lấy comment làm bằng chứng runtime. |
| TK-02 | Nhân vật cấp 39, 40, 41, 79, 80, 119, 120 | Đối chiếu TNL cấp 40 → 0 và 80–119 → 3; ghi cấp bị từ chối/map nhận. So với nhánh cũ tách riêng. |
| TK-03 | TNL phe nhận có 99 rồi 100 người; giữ cân bằng bằng phe kia | Ngưỡng `>=100` phải chặn người kế tiếp theo source; không dùng top 10 để kết luận đã đầy chiến trường. |
| TK-04 | TNL chênh trước khi vào là 1 rồi 2; thử vào phe ít và phe nhiều | Source chặn phe nhiều khi chênh đã `>=2`. Kiểm tra cả hai phe và các yêu cầu gần đồng thời. |
| TK-05 | TNL tiền 199.999 / 200.000 / 200.001, phe hợp lệ và người mới camp 0 | Kiểm tra từ chối/tiền thực trừ và không trừ khi thất bại; đối chiếu `but_join` và `PHIBAODANH`. |
| TK-06 | Chiến báo với 0, 1, 9, 10, 11 người đủ điều kiện; điểm khác nhau | Chỉ 10 slot hiển thị; người thứ 11 vẫn có thể tham chiến theo trần phe. Theo dõi rủi ro iterator trước ca 11 nếu đường `RankCalculator` được dùng; cần reviewer xử lý lỗi đó trước khi thử. |
| TK-07 | Hai nhân vật khác ID cùng điểm và số giết; thay số NPC/đổi điểm | Xác minh có mất một người do comparator hay không; không coi bảng ngắn là thiếu người trong mission. |
| TK-08 | Trong harness thử được duyệt, gói mission index 0, 9, 10; ladder chung 1 và 10 mục | Index mission 10 bị bỏ qua theo guard; kiểm tra dữ liệu cũ/rác ở slot còn lại. Không gửi gói thử vào server thật. |
| TK-09 | Điểm 65.534 / 65.535 / 65.536 ở từng đường dữ liệu riêng | Ghi giá trị server, giá trị trong gói và hiển thị; xác định đường 16 bit có tràn hay không, không áp kết quả cho đường mission khác. |
| TK-10 | Kết thúc trận, vào lại, đổi phe ở lượt mới, đóng/mở chiến báo | Kiểm tra reset dữ liệu cá nhân/top 10 và phân biệt gói `s2csyncrankdata` với `s2c_ladderresult`; xác minh các API stub có tác động không. |

## Lỗi công cụ, khắc phục và giới hạn bàn giao

- Lần đọc đầu dùng encoding mặc định bị mojibake; đã đọc lại UTF-8 đúng file task. Không thay nội dung gốc vì lỗi hiển thị terminal.
- `Get-ChildItem ... D:\JX-wt\A-16\Folder`: `Cannot find path ... because it does not exist.` Đã dùng đường gói gốc được bản đồ dự án chỉ ra dưới `C:\Jx1CocoV3\Folder`; chỉ đọc.
- `rg`: `The term 'rg' is not recognized ...`. Chuyển PowerShell/Python `-I`, không cài thêm công cụ, không đổi PATH.
- Python: `UnicodeEncodeError: 'charmap' codec can't encode ...`; đặt `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` trong tiến trình. Một truy vấn khoảng dòng vượt cuối file gây `IndexError: list index out of range`; lần sau chặn theo `len(lines)` và đọc tiếp các đoạn phụ thuộc bị bỏ dở. Không ảnh hưởng file nguồn.
- Số đếm sơ bộ từng trừ tiêu đề cho mọi file có tab; đã thay bằng phân loại tiêu đề tường minh, giữ riêng 19 dòng của `lingyuguan/trap_1.txt`. Các tổng trong báo cáo cuối là số đã hiệu chỉnh.
- Một vài truy vấn nguồn trả output dài bị cắt; đã thu hẹp tới file/symbol/khoảng dòng làm bằng chứng cuối, không dùng phần output bị cắt để khẳng định số liệu.
- Kiểm tra cấu trúc lần đầu gặp `AssertionError` khi so literal tiếng Việt truyền qua pipe PowerShell. File UTF-8 không có BOM; dùng Unicode escape trong biểu thức kiểm tra rồi chạy lại: PASS (5 dòng tóm tắt, 2 mục xác minh, 10 ca TESTER và mục Kết quả). Đếm lại `RankSetting`: 100 khóa/89 nhãn. Quét mẫu gán bí mật, khóa riêng và địa chỉ IPv4 trong báo cáo: không có kết quả; đây là kiểm tra mẫu, không thay cho review thủ công.
- Kiểm tra thực hiện: đọc source, đếm byte/bảng, đối chiếu tổng và phạm vi file báo cáo; không có test/build runtime đạt để báo cáo.
- Trạng thái nội dung: **DONE** cho khảo sát tĩnh đã duyệt; các mục runtime và symbol thiếu được ghi rõ, không được coi là đã xác minh.
- Commit SHA: **chưa có**. `.git` của worktree trỏ `D:/jx1-reports/.git/worktrees/A-16`, nằm ngoài vùng được ghi `D:\JX-wt\A-16`; không stage/commit vì cần ghi metadata ngoài sandbox, không thử vượt quyền. Hai file kết quả giữ local để PM có quyền phù hợp commit. **BỊ CHẶN – CHƯA PUSH**: chỉ thị không dùng mạng; không có bằng chứng GitHub và không tuyên bố đã push.
- Bước tiếp theo: PM/reviewer L3 kiểm tra các rủi ro source, xác nhận nhánh thực dùng và giao TESTER các ca phù hợp; nếu cần đào sâu `JoinActivityGroup`, cung cấp vị trí module chứa symbol. Không sửa mã trong A-16.
