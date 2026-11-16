Tóm tắt 1: Đã lập 27 mục hoạt động/nhánh script từ gói gs và đối chiếu source; mọi kết luận là kiểm tra tĩnh, runtime chưa kiểm.
Tóm tắt 2: Phân loại 5 trạng thái: có script đầy đủ 0; script thiếu hoặc lỗi 24; có dữ liệu không có script 1; chỉ có tham chiếu 1; không thấy 1.
Tóm tắt 3: servertimer.lua:125 thiếu dấu nháy đóng; 8 lời gọi mở hoạt động tại dòng 38–52 đều bị comment; chưa kết luận lịch nào chạy trên VM.
Tóm tắt 4: Có script/cấu hình trong Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs; kết quả Lua=0 của A-03 chỉ thuộc cây source jxOnline.
Tóm tắt 5: Đã kiểm bằng đọc báo cáo; không build/test game hoặc kết nối VM/SQL/server; commit BỊ CHẶN do quyền Git metadata, chưa có SHA, chưa push.

# D-01 — Bảng hoạt động theo 5 trạng thái

Ngày khảo sát: 17/11/2026. Trạng thái task: **PARTIAL** — nội dung DONE, commit BLOCKED. Phạm vi là các nhánh hoạt động trong bảng dưới, không phải kiểm kê toàn bộ NPC, vật phẩm, nhiệm vụ môn phái hay mọi biến thể script.

## Worker kiểm tra trước khi làm

- Đọc `JX1_OPS/TASKS/D-01.md` trước khi điều tra. Working directory của lệnh là `D:\JX-wt\D-01`; `git status --short --branch` trả `## task/D-01-codex`, không có thay đổi local, khớp worktree/branch của task.
- Chỉ tạo báo cáo này và cập nhật mục `Kết quả` trong task theo yêu cầu trực tiếp của người dùng. Nguồn `C:\Jx1CocoV3` chỉ đọc; không sửa cấu hình/source, không chạy binary game, không kết nối VM/SQL/server.
- Đã đọc phần liên quan của bốn báo cáo nền: A-01 là bằng chứng vận hành lịch sử, chưa kiểm lại VM (`JX1_OPS/REPORTS/A-01-ban-do-tien-trinh.md:9`); A-02 mô tả đăng nhập (`JX1_OPS/REPORTS/A-02-luong-dang-nhap.md:1`); A-03 chỉ đếm cây source jxOnline (`JX1_OPS/REPORTS/A-03-kiem-ke-cau-hinh.md:9`); A-06 cảnh báo lệch protocol/ABI, không xác nhận runtime (`JX1_OPS/REPORTS/A-06-bang-goi-tin.md:3–5`).

## Gốc bằng chứng và quy ước

| Ký hiệu | Đường dẫn thật |
| --- | --- |
| `G/` | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\` |
| `S/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\` |
| `R` | `JX1_OPS/REPORTS/D-01-bang-hoat-dong.md` (báo cáo này; dùng dẫn kết quả tìm kiếm không có file để trích) |

Số sau dấu `:` tính từ dòng 1, gồm cả dòng trống. Các đường Lua trong cấu hình là đường logic tính từ G; đường file thiếu được kiểm bằng `Test-Path -LiteralPath`, không tự sửa tên hoặc chuyển mã tên file. Cùng tên hoạt động có thể có nhiều bản legacy/tnlteam; bảng phân biệt nhánh khi bằng chứng khác nhau.

Đọc báo cáo Markdown bằng UTF-8; đọc mã legacy bằng CP936 để giữ các token ASCII và đếm dòng. Chuỗi tiếng Việt và một số tên thư mục trong gói có dấu hiệu hỏng mã hóa; không sửa/chuẩn hóa chúng. Nhận xét thiếu dấu nháy dưới đây dựa trên ký tự ASCII thực trong dòng, không dựa vào cách hiển thị dấu tiếng Việt; chưa chạy Lua compiler.

| Trạng thái bắt buộc | Điều kiện dùng trong báo cáo | Số mục |
| --- | --- | ---: |
| Có script đầy đủ | Phải nối được entrypoint, xử lý, kết thúc/phần thưởng và phụ thuộc cần thiết; có file không đủ để xác nhận. Chưa có nhánh nào trong bảng đạt bằng chứng này. | 0 |
| Script thiếu hoặc lỗi | Có thân script nhưng thấy lỗi văn bản, thiếu phụ thuộc/file rời hoặc chuỗi kích hoạt lịch bị ngắt. Lịch bị comment được ghi riêng, không coi là lỗi cú pháp của thân hoạt động. | 24 |
| Có dữ liệu không có script | Có bảng dữ liệu vật lý, chưa thấy script gắn với bảng qua literal đã tìm; không khẳng định không có cách nạp động. | 1 |
| Chỉ có tham chiếu | Chỉ thấy lời gọi/tên, chưa thấy định nghĩa triển khai tương ứng trong phạm vi đã tìm. | 1 |
| Không thấy | Không tìm thấy theo tập từ khóa công bố; là kết quả tìm kiếm có giới hạn, không phải kết luận hoạt động không tồn tại trong game. | 1 |

## Bằng chứng filesystem và tìm kiếm

Không có file thì không thể gán số dòng cho file đó. Các dòng E01–E06 là bằng chứng lệnh trong phiên; cột bằng chứng của bảng dẫn tới chính dòng ghi nhận tương ứng ở báo cáo.

E01 — `Test-Path` trả False cho `G/script/tnlteam/missions/liendau/dondau/npc_liendau.lua`, đúng literal tại `G/script/System/serverscript.lua:10`; `G/script/tnlteam/mission/liendau/dondau/head.lua` và `mission.lua` có tồn tại. Không tự thay `missions` bằng `mission`.
E02 — `Test-Path` trả False cho các literal `script/missions/擂台赛/擂台赛.lua`, `攻城战/攻城战.lua`, `渡船/渡船.lua`, `宋金战场pk战/宋金战场pk大战.lua`, `过关斩将/过关斩将.lua`, `封神竞技/封神竞技.lua`, `攻城拔寨/攻城拔寨.lua`, `襄阳/襄阳.lua`, `巴陵活动/巴陵.lua` dưới G; một số thư mục tên gần giống nhưng bị lỗi mã hóa có hiện diện. Chỉ kết luận thiếu file rời theo literal, chưa kiểm đường bytes trên VM/PAK.
E03 — Tìm literal không phân biệt hoa/thường bằng `Select-String -SimpleMatch` trong toàn bộ `G/script/**/*.lua`: `baihutang`=0, `bach_ho`=0, `bai_hu`=0. Chưa tìm tên Hán tự/alias khác hoặc nội dung PAK; mục Bạch Hổ Đường chỉ phản ánh ba khóa này.
E04 — `Test-Path` trả False cho `G/script/tnlteam/qua_huy_hoang/lib_huyhoang.lua`, `G/script/activitysys/g_activity.lua`, `G/script/activitysys/playerfunlib.lua`, `G/script/activitysys/config/1005/partysupport.lua`; đây là các Include thật ở nhánh Kiếm Môn Quan/Viêm Đế.
E05 — `Test-Path` trả False cho `G/script/missions/bw/bwmission.lua`, `bwtimer.lua`, `bwtotaltimer.lua`; trong thư mục bw chỉ thấy ba file manager khi liệt kê file trực tiếp. Chưa kiểm bản đóng trong PAK.
E06 — Tìm literal trong toàn bộ `G/script/**/*.lua`: `zhongqiudengmi`=0; `active_somayman`=1, duy nhất ở `G/script/servertimer.lua:50` là comment. Tìm kiếm không xác nhận các đường nạp động hoặc hàm nằm trong PAK.

## Các điểm chung ảnh hưởng cách thử D-02

- Source nạp thư mục Lua và danh sách `script.txt`, nên thiếu file rời chưa đủ chứng minh thiếu trong runtime/PAK (`S/Core/Src/KSortScript.cpp:219–242`). D-01 chưa giải nén PAK.
- `CoreServerShell::OnLunch` gọi `StartGame`; script khởi động Include đường Liên đấu không có file theo E01 trước khi gọi `createnpc`. Đây là nguy cơ làm gián đoạn nạp script; chưa đo tác động runtime (`S/Core/Src/CoreServerShell.cpp:2203–2215`; `G/script/System/serverscript.lua:9–18`).
- Timer C++ gọi `Main` khi đạt điều kiện game-time và giây hệ thống bằng 0; file Lua đọc được có chuỗi bắt đầu bằng dấu nháy kép ở dòng 125 nhưng không đóng trước xuống dòng. Dòng này có đúng 1 dấu nháy ASCII; cần xác minh bản mà exe thực sự nạp trước khi thử lịch (`S/Core/Src/CoreServerShell.cpp:2231–2246`; `G/script/servertimer.lua:123–128`).
- `SERVER_MODE=0`; `Main` chỉ gọi bảng xếp hạng đua top khi mode=1. Các lệnh mở boss tiểu, Huy Hoàng, vượt ải, Liên đấu, Phong Lăng Độ, hoa đăng, số may mắn và Tống Kim đều đang comment (`G/script/lib/worldlibrary.lua:8`; `G/script/servertimer.lua:36–58`).
- `Settings/Task/tasklist.ini` có Count=1, chỉ Refresh NPC; hai lời gọi nạp scheduler trong source đang comment. Không suy ra file `script/task/*.lua` tự chạy chỉ vì file tồn tại (`G/Settings/Task/tasklist.ini:1–13`; `S/Core/Src/KCore.cpp:688–692`).

## Bảng hoạt động và cách thử D-02

Tất cả cách thử dưới đây là đề xuất cho task D-02, **chưa thực hiện**. D-02 cần dùng bản copy trên VM thử, nhân vật/GM thử, xác định map đã nạp và đúng phiên bản script trước khi gọi hàm; thu console/log đã lọc, trạng thái trước/sau, ảnh kết quả và khả năng kết thúc hoạt động. Không cần sửa gói gốc để thực hiện D-01.

| ID | Tên hoạt động / nhánh | Trạng thái | Bằng chứng file:dòng và lý do | Cách thử D-02 |
| --- | --- | --- | --- | --- |
| 01 | Tống Kim — tnlteam, mission 11 | Script thiếu hoặc lỗi | `G/script/servertimer.lua:10,17,52,141–164`: lời gọi lịch bị comment; thân có `but_battlestart`. `G/script/tnlteam/mission/battlesongjin/butcher/head.lua:91–119,234`: có mở/đóng/gameover, chưa đủ chứng minh toàn chuỗi. | Sau xử lý điểm timer chung, chọn map 380 đã nạp; thử báo danh hai phe, mở trận, tính điểm và đóng/nhận thưởng; đối chiếu mốc phút 50 của lịch. |
| 02 | Phong Lăng Độ — tnlteam, mission 10 | Script thiếu hoặc lỗi | `G/script/servertimer.lua:11,18,46,167–183`: lịch bị comment. `G/script/tnlteam/mission/fenglingdu/head.lua:6–18,43–58`: có mở/đóng, thời gian báo danh 5 phút và trận 25 phút. | Map 337: mở `fld_start_mission` đúng SubWorld, thử báo danh, chuyển thuyền, các đợt thủy tặc và `fld_close_mission`; kiểm mốc lịch phút 00. |
| 03 | Vượt ải / Thách thức thời gian — mission 9, nhánh 17 | Script thiếu hoặc lỗi | `G/script/servertimer.lua:12,19,42,187–207`: lịch bị comment. `G/script/tnlteam/mission/challangeoftime/head.lua:4–28,653–693`: có mission 9/17 và hàm mở/đóng. | Dùng đội thử trên map 464–471 đã nạp; thử `start_mission`, tiến ải, thất bại/hết giờ và thưởng. Thử nhánh 17 riêng, không trộn timer 37 với timer nhánh khác. |
| 04 | Liên đấu đơn — mission 12/13 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:13–14`; `G/Settings/TimerTask.txt:45–48`; `G/script/servertimer.lua:44,210–228`: lịch bị comment; Include khởi động sai đường, `G/script/System/serverscript.lua:10` và `R:41`. | Xác minh đường Include và map 396 trên bản copy; thử báo danh hai người, ghép cặp, tính thắng/thua, hết giờ và nhận thưởng; giữ bằng chứng lỗi nạp nếu còn. |
| 05 | Hoa đăng — subject | Script thiếu hoặc lỗi | `G/script/servertimer.lua:48,230–234`: lịch bị comment. `G/script/subject/hoadang/lib.lua:64–89`: có cửa sổ giờ, tạo NPC và timeout 15 phút. | Thử `release_hoadang` trong cửa sổ cấu hình, tương tác NPC, trả lời đúng/sai, giới hạn lượt và biến mất đúng hạn; xác minh một giờ có tạo lặp nhiều đợt hay không. |
| 06 | Đêm Huy Hoàng | Script thiếu hoặc lỗi | `G/script/servertimer.lua:40,245–265`: lịch bị comment. `G/script/subject/demhuyhoang/event.lua:192–218`: `addhhh` tạo NPC có timeout. | Thử một đợt `addhhh`, thu hoạch/giới hạn nhận và hết hạn; kiểm riêng các mốc 12:30/40/50 và 19:30/40/50 sau khi timer hợp lệ. |
| 07 | Boss tiểu Hoàng Kim — subject | Script thiếu hoặc lỗi | `G/script/servertimer.lua:38,236–243`: lịch bị comment. `G/script/subject/bosstieuhk/bosstieuhk.lua:49–60`: có `releasebosstieu`, timeout 30 phút. | Tạo một đợt trên map đã nạp, kiểm vị trí, death/drop và thu hồi; đối chiếu mốc 18:10/22:10, không kết luận drop từ lệnh tạo NPC. |
| 08 | Đua top / xếp hạng thế giới | Script thiếu hoặc lỗi | `G/script/servertimer.lua:55–58,79–137`: có cập nhật/thông báo, nhưng chuỗi dòng 125 không đóng; mode hiện đọc là 0 (`G/script/lib/worldlibrary.lua:8`). | Xác minh script nạp được; dùng dữ liệu thử kiểm cập nhật level/exp, thứ hạng và thông báo đầu giờ; thay mode chỉ trong phạm vi D-02 được duyệt. |
| 09 | Nhiệm vụ hằng ngày tại Lễ Quan | Script thiếu hoặc lỗi | `G/script/tnlteam/task_hang_ngay/lib_hang_ngay.lua:12–21,54–124`: có nhận/kiểm điều kiện/thưởng; dòng 17 thiếu dấu `/` ngăn nhãn menu với `NhanHDNVHNGAY`, trong khi dòng 18 có `/ThuongHDNVHNGAY`. `G/script/lib/lib_ham.lua:85–102` chuyển nguyên lựa chọn sang `Say`, không bổ sung dấu phân cách. Hành vi menu runtime chưa kiểm. | Thử menu nhận thực sự đi vào callback; hoàn thành 8 boss sát thủ, 750 điểm TK, 1 PK, 1 vượt ải, 1 PLĐ; thử thiếu từng điều kiện và nhận thưởng lần hai. |
| 10 | Thiên Bảo Khố | Script thiếu hoặc lỗi | `G/script/subject/thien_bao_kho/thienbaokho.lua:16–24,55–73`: có map 395, NPC/rương/trap nhưng dòng 16 có 3 dấu nháy, thiếu đóng tên NPC; `G/script/subject/thien_bao_kho/dichquan.lua:120,128` cũng có chuỗi chưa đóng. `G/script/subject/thien_bao_kho/baoruong.lua:22–69` có tiến độ đúng/sai thứ tự. | Lưu lỗi nạp trước; trên bản copy đã được xử lý lỗi, thử đội trưởng nhận nhiệm vụ, mở đúng/sai thứ tự, chết/thoát và trả thưởng; kiểm reset nhiệm vụ. |
| 11 | Vận tiêu — subject | Script thiếu hoặc lỗi | `G/script/subject/van_tieu/tieudau.lua:6–24`: có menu và `vantieu`, nhưng dòng 16 mở chuỗi `Say` không đóng trước xuống dòng (1 dấu nháy); `G/script/subject/van_tieu/head.lua:4,12` có script tiêu xa/vị trí. | Xác minh tải script; nhận tiêu, hộ tống tới đích, tiêu bị phá, hết giờ và trả thưởng; kiểm phí/hoàn trả bằng nhân vật thử. |
| 12 | Câu cá — tnlteam | Script thiếu hoặc lỗi | `G/script/tnlteam/cauca/luoica.lua:12,43–65`: dòng 12 thiếu nháy đóng; `main` có lệnh thêm item thử ở dòng 47, lệnh mở tiến độ dòng 59 và callback thu hoạch từ dòng 62 đang comment. | Chưa dùng trực tiếp làm hoạt động hoàn chỉnh; xác minh script nạp, đường dùng cần câu/lưới và callback thu hoạch trên copy; kiểm nhận vật phẩm trước khi đủ điều kiện. |
| 13 | Nhận thưởng hoạt động/online — System/activity | Script thiếu hoặc lỗi | `G/script/System/activity.lua:28–37,43–60`: `main` chỉ Talk bảo trì; xử lý thưởng nằm ở `main11`, chưa chứng minh nơi gọi `main11`. | Đi theo giao diện/người chơi tới entrypoint thật; kiểm có vào `main11` không, phần thưởng từng nhánh và giới hạn mỗi ngày; không gọi thưởng trực tiếp rồi ghi hoạt động đạt. |
| 14 | Kiếm Môn Quan — mission 31 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:33`; `G/Settings/TimerTask.txt:42`; `G/script/tnlteam/kiem_mon_quan/mission.lua:3–4,6–24` và `timerboard.lua:2–5`: Include thư viện Huy Hoàng thiếu theo `R:44`. | Xác minh phụ thuộc/PAK trước; thử mở mission, tiến đợt, timer, chết/rời và `kmq_gameover`, kiểm thưởng và dọn NPC. |
| 15 | Viêm Đế Bảo Tàng — yandibaozang | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:21–32`; `G/Settings/TimerTask.txt:35–37`; `G/script/missions/yandibaozang/npc_death.lua:11–16,52,197`: thiếu ba Include activitysys theo `R:44`, hai lệnh `tbAwardTemplet:Give` đang comment. Có luồng trận nhưng không xếp đầy đủ. | Kiểm map chờ 851/852 và map trận 853–862, phụ thuộc, đăng ký đội, các đợt/boss, chuyển giai đoạn và kết thúc; đối chiếu EXP và vật phẩm thưởng riêng. |
| 16 | Lôi đài — legacy mission 1/2 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:2–3`; `G/Settings/TimerTask.txt:2–4`: literal trỏ `擂台赛`, file mission không tồn tại theo `R:42`. | Đối chiếu tên byte/PAK và bộ script trên VM; sau khi nối đúng file, thử đăng ký hai bên, đếm giờ, thắng/thua và kết thúc. |
| 17 | Công thành chiến — legacy map 221 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:4`; `G/Settings/TimerTask.txt:16–17`: thiếu file literal `攻城战/攻城战.lua` theo `R:42`. Không gộp với nhánh `feature/congthanh` chưa kiểm. | Kiểm map 221 và đường script thực; thử phe công/thủ, điều kiện chiếm, hết giờ và reset trên dữ liệu thử. |
| 18 | Tống Kim PK — legacy map 378 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:6`; `G/Settings/TimerTask.txt:5–6`: thiếu file literal `宋金战场pk战/宋金战场pk大战.lua` theo `R:42`; khác nhánh Tống Kim mục 01. | Kiểm đúng biến thể và map 378; thử timer/điểm/phe riêng, tránh dùng kết quả mission 11 thay cho nhánh này. |
| 19 | Quá Quan Trảm Tướng — legacy map 515 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:7`; `G/Settings/TimerTask.txt:21–22`: thiếu file literal `过关斩将/过关斩将.lua` theo `R:42`. | Xác định file thật và map; thử lần lượt các cửa, chết/hết giờ, điều kiện qua cửa cuối và thưởng. |
| 20 | Phong Thần thi đấu — legacy mission 7 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:8`; `G/Settings/TimerTask.txt:23–25`: thiếu file literal `封神竞技/封神竞技.lua` theo `R:42`. | Kiểm phụ thuộc, mở báo danh, timer và kết quả từng phe; ghi chính xác lỗi nếu mission chưa thể tạo. |
| 21 | Công Thành Bạt Trại — legacy mission 8 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:9`; `G/Settings/TimerTask.txt:26–28`: thiếu file literal `攻城拔寨/攻城拔寨.lua` theo `R:42`. | Sau đối chiếu file/PAK, thử báo danh, chiếm mục tiêu, chốt kết quả và đóng mission; phân biệt công thành map 221. |
| 22 | Tương Dương — nhóm mission bản đồ legacy | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:15–20`; `G/Settings/TimerTask.txt:32–34`: các map 78/1/11/37/80/162 cùng trỏ file `襄阳/襄阳.lua` thiếu theo `R:42`. | Xác minh đây là mission nào trong bộ VM, chọn một map có tải, thử đăng ký/timer/kết thúc; tên hoạt động người chơi còn chưa kiểm. |
| 23 | Hoạt động boss Ba Lăng — task legacy | Script thiếu hoặc lỗi | `G/script/task/balinboss.lua:5–16`: Include `巴陵活动/巴陵.lua` không có file literal theo `R:42`, thân gọi `makeDL` trên map 53; `G/Settings/TimerTask.txt:29–31` có timer Ba Lăng. | Kiểm file phụ thuộc và map 53; thử mở một đợt, spawn boss, death/drop, báo danh và dọn đợt. |
| 24 | Thi đấu bw — mission 32 | Script thiếu hoặc lỗi | `G/Settings/Task/missions.txt:34`; `G/Settings/TimerTask.txt:43–44`: cả mission và hai callback timer thiếu file rời theo `R:45`. Tên Việt chính xác chưa kiểm. | Xác minh script PAK/bộ triển khai trước; chưa có entrypoint đủ để gọi an toàn. Khi có, thử manager → báo danh → thi đấu → kết thúc. |
| 25 | Bộ câu đố hoa đăng legacy zhongqiudengmi | Có dữ liệu không có script | `G/Settings/event/hoadang/zhongqiudengmi.txt:1–4`: có header/câu hỏi/đáp án; không có literal sử dụng trong Lua theo `R:46`. Nhánh hoa đăng subject ở mục 05 có bảng câu hỏi riêng, không mặc định dùng bảng này. | Tìm chỗ nạp động/PAK và mã item/NPC gắn bảng trước; sau đó thử đổi câu/đáp án trên copy và xem giao diện có dùng đúng bảng không. |
| 26 | Số may mắn — active_somayman | Chỉ có tham chiếu | `G/script/servertimer.lua:49–50`: chỉ có lời gọi bị comment; toàn cây Lua chỉ có 1 lần xuất hiện literal, không thấy định nghĩa theo `R:46`. Không đồng nhất với các file lucky/xingyun khác khi chưa nối được hàm. | Tìm implementation/alias trong bộ VM và PAK; chưa có hàm triển khai để thử. Giữ trạng thái chưa kiểm cho luật chọn số/thưởng. |
| 27 | Bạch Hổ Đường — mục đối chiếu bổ sung theo khóa ASCII | Không thấy | `R:43`: không tìm thấy ba literal đã nêu trong cây Lua rời; chưa kiểm tên Hán tự, tên Việt có dấu, alias hoặc PAK. Không kết luận game không có hoạt động này. | Xác định tên/script từ giao diện hoặc cấu hình VM trước; chưa có file/hàm/map đủ bằng chứng để đề xuất lệnh mở. |

## Chưa kiểm

- Toàn bộ runtime: bản script được exe nạp, ưu tiên PAK/đĩa, encoding tên đường trên VM, các map thực sự tải và lỗi nạp Lua. Không suy kết quả chạy từ source hoặc từ báo cáo A-01.
- Chưa biên dịch/kiểm cú pháp bằng Lua engine đúng phiên bản; các lỗi nháy là quan sát văn bản. Chưa phân tích toàn bộ phụ thuộc Include bắc cầu hoặc API mà binary thực sự cung cấp.
- Chưa xác minh hoàn chỉnh việc đăng ký, giá/phí, giới hạn ngày, phối hợp đội/phe, timer, phần thưởng, chống nhận trùng, khôi phục khi chết/thoát và dọn NPC cho từng dòng.
- Các thư mục khác như nhiệm vụ môn phái, sát thủ, sự kiện Tết/Giáng sinh, `feature/congthanh`, các biến thể task/battles chưa truy hết luồng; không dùng bảng này làm danh sách toàn bộ tính năng của gói.
- Mục 25–27 chỉ phản ánh dữ liệu/tìm kiếm đã mô tả; cách nạp động, tên khác và script trong PAK đều chưa kiểm. Nhánh nào chưa đủ bằng chứng không được ghi thành có script đầy đủ.
- Build/test game: không chạy theo task. Chỉ kiểm bằng đọc lại tài liệu; không có kết quả build/test game đạt.

## Lỗi công cụ đã gặp và cách xử lý

| Lỗi / giới hạn | Cách đã thử và kết quả |
| --- | --- |
| `Get-Content : An object at the specified path ... A-01*.md does not exist` (tương tự A-02/A-03/A-06) | Lần đầu dùng wildcard với `-LiteralPath`, nên không mở được. Liệt kê tên trong thư mục REPORTS một lần rồi dùng đúng tên file; đọc được. Không coi lỗi này là thiếu báo cáo nền. |
| `rg : The term 'rg' is not recognized as the name of a cmdlet, function, script file, or operable program.` | Một lần thử; chuyển sang `Get-ChildItem`, `Select-String` và đọc file trực tiếp. Không cài công cụ hoặc đổi cấu hình môi trường. |
| Đọc Markdown bằng encoding mặc định bị lỗi hiển thị; đầu ra đọc gộp quá dài bị rút gọn | Dùng UTF-8 cho Markdown, lấy lại các đoạn cần thiết; CP936 cho token source legacy. Không chuyển mã/ghi lại file nguồn. |
| Kiểm tra dẫn nguồn ban đầu nhận nhầm hậu tố `S/` trong `JX1_OPS/REPORTS` là alias source | Đó là 4 kết quả nhận nhầm của biểu thức kiểm tra, không phải file nền bị thiếu. Bổ sung ranh giới alias rồi đối chiếu lại các dẫn nguồn; không sửa đường báo cáo đúng. |

## Kiểm chứng và bàn giao

- Đã đọc lại nội dung và rà diff: 5 dòng tóm tắt, đủ 5 nhãn trạng thái, 27 dòng có bằng chứng file:dòng (kết quả vắng mặt dẫn về E01–E06), cột cách thử D-02 và mục Chưa kiểm. Đối chiếu 64 dẫn nguồn G/S: file tồn tại và số dòng đầu hợp lệ; 0 lỗi sau sửa bộ nhận diện alias. Đây là kiểm tra tài liệu, không phải test game.
- Chỉ có một báo cáo tổng hợp này; không sửa `docs-analysis/BAI_HOC.md`, không tạo script/parser phụ hoặc tài liệu kết quả riêng.
- **Commit: BLOCKED. BỊ CHẶN – CHƯA PUSH.** Chưa có commit SHA; không có link GitHub mới. Chỉ được yêu cầu commit, không chạy push.

Lệnh đã thử một lần, exit 128:

~~~text
git add -- JX1_OPS/REPORTS/D-01-bang-hoat-dong.md JX1_OPS/TASKS/D-01.md
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/D-01/index.lock': Permission denied
~~~

Git metadata ở ngoài writable root `D:\JX-wt\D-01`; phiên này không được nâng quyền. Chưa stage được nên lệnh commit chưa chạy. Không đổi ACL/config/credential, không dùng index/repository thay thế để vượt sandbox; giữ nguyên hai file local. Không còn bước kỹ thuật an toàn trong quyền hiện tại để tạo commit trên nhánh này.

Bước tiếp theo: PM gộp hoặc dùng phiên có quyền ghi metadata để stage đúng hai file và tạo commit trên `task/D-01-codex`:

~~~text
git -C "D:\JX-wt\D-01" add -- JX1_OPS/REPORTS/D-01-bang-hoat-dong.md JX1_OPS/TASKS/D-01.md
git -C "D:\JX-wt\D-01" commit -m "D-01 Lap bang hoat dong 5 trang thai tu script va cau hinh"
~~~

Sau đó ghi SHA vào bàn giao; D-02 tiếp tục từ bảng hoạt động và các điểm chưa kiểm trong báo cáo này.

