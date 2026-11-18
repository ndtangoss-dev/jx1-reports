TÓM TẮT 1 [THẤY] Server gọi Main của servertimer.lua khi game-time chia hết cho 18 và giây hệ thống bằng 0 (S/Core/Src/CoreServerShell.cpp:2227–2246).
TÓM TẮT 2 [THẤY] Timer người chơi đếm theo GetGameTime, lưu ID/thời gian còn lại và gọi OnTimer; đơn vị chưa quy đổi (S/Core/Src/KTaskFuns.h:12–15,54–66; S/Core/Src/KTaskFuns.cpp:118–131,141–174,190–196).
TÓM TẮT 3 [TÀI LIỆU] Báo cáo nền có mẫu nhiệm vụ ngày và sự kiện theo giờ; cấu hình timer không chứng minh lịch đang chạy (I-08:35–38,137–142; D-01:62–70).
TÓM TẮT 4 [CHƯA KIỂM] Chưa xác minh nhiệm vụ tuần, reset ngày, múi giờ, lịch ngày lễ và cấu hình thực được nạp (I-08:38; D-01:90–97).
TÓM TẮT 5 [THẤY] Chỉ đọc tĩnh, không build/chạy game, exe, VM hay mạng theo task (JX1_OPS/TASKS/SO-10.md:27–31).

# SO-10 — Sổ tay thời gian, lịch và sự kiện trong Lua

Loại: khảo sát
Chủ đề: Bằng chứng tĩnh về vòng lịch server, timer người chơi và nhiệm vụ/sự kiện có liên quan thời gian.
Từ khóa: thời gian, lịch, timer, Lua, nhiệm vụ ngày, nhiệm vụ tuần, Hoa đăng, servertimer
Trạng thái: DONE — tổng hợp bằng chứng hiện có, nêu rõ nội dung chưa kiểm.
Độ phủ: đã phân loại 7/7 câu hỏi; 2 mục có source trực tiếp, 3 mục dựa báo cáo nền, 2 mục chưa xác minh.
Liên quan: JX1_OPS/REPORTS/K-02-script-lua.md; JX1_OPS/REPORTS/I-08-he-thong-nhiem-vu.md; JX1_OPS/REPORTS/D-01-bang-hoat-dong.md; JX1_OPS/DESIGN/CHUAN-BAO-CAO.md.
Cần tôi quyết định: không.

G/ là cây script/config server theo K-02: C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/. S/ là server source theo task: C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources/. C/ là client Classes theo task: C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes/.

~~~mermaid
flowchart TD
    B["Server Breathe / game-time"] --> C{"game-time % 18 = 0<br/>và wSecond = 0?"}
    C -->|đúng| M["servertimer.lua: Main"]
    M --> E["Sự kiện toàn server<br/>activation chưa xác minh"]
    P["Timer người chơi"] --> G["GetGameTime + ulTime"]
    G --> A["Activate đến hạn"]
    A --> O["Lua OnTimer"]
    P -.-> S["Lưu ID / thời gian còn lại"]
    D["Dữ liệu nhiệm vụ ngày"] --> Q["Script và bộ đếm"]
    Q -.-> R["Reset tuần/ngày lễ<br/>chưa xác minh"]
~~~

## Vòng thời gian của server

- [THẤY] CoreServerShell::Breathe lấy script servertimer.lua. Khi GetGameTime() chia hết cho GAME_FPS=18, code đọc SYSTEMTIME và gọi Main nếu wSecond bằng 0 (S/Core/Src/CoreServerShell.cpp:2227–2246). Đây là điều kiện trong source, không phải phép đo runtime.
- [CHƯA KIỂM] Đoạn source này không thể hiện chuyển múi giờ hoặc lịch ngày. Không gán mốc trong Lua thành giờ địa phương hay lịch âm/dương khi chưa xác minh hàm ngày/giờ trong script thực nạp.
- [TÀI LIỆU] D-01 ghi Phong Lăng Độ ở phút 00, Tống Kim phút 50, Hoa đăng và các đợt Đêm Huy Hoàng; đồng thời ghi một số lệnh mở sự kiện đang comment (D-01:52–70). Đây là dấu vết lịch, chưa xác nhận hoạt động đã chạy.

## Timer và callback Lua

- [THẤY] KTimerTaskFun::SetTimer đặt hạn bằng GetGameTime()+ulTime và lưu khoảng lặp/ID (S/Core/Src/KTaskFuns.h:54–66). Activate kiểm hạn, đẩy mốc kế tiếp theo khoảng lặp rồi gọi callback (S/Core/Src/KTaskFuns.cpp:118–131).
- [THẤY] Callback người chơi gọi hàm Lua OnTimer; timer lưu/khôi phục ID và thời gian còn lại (S/Core/Src/KTaskFuns.cpp:135–174,190–196). Các khóa task là 220 và 221; đường cấu hình khai báo là \settings\TimerTask.txt (S/Core/Src/KTaskFuns.h:12–15).
- [CHƯA KIỂM] ulTime và GetGameTime chưa được quy đổi ra giây/phút thực. Không suy đơn vị timer người chơi từ GAME_FPS=18.
- [THẤY] TimerTaskFun::Init đọc bảng cấu hình, GetTimerTaskScript lấy cột SCRIPT theo ID (S/Core/Src/KTaskFuns.cpp:104–114,178–186). Điều này không chứng minh số lịch nào đang chạy.
- [TÀI LIỆU] I-08 đếm 47 bản ghi TimerTask; tasklist.ini có Count=1 còn tasklist_default.ini có Count=39, nhưng chưa xác định loader dùng file nào (I-08:37–38). D-01 ghi lịch sử timer nhưng chưa xác nhận callback runtime (D-01:62–70).

## Nhiệm vụ ngày, tuần và lịch lặp

- [TÀI LIỆU] I-08 ghi taskguide.txt:6–8 là nhóm daily; dailytask/killmonster.txt:2 có 17 TaskId và mỗi KillCount là 20. Đây là mẫu cấu hình, không có nghĩa mọi nhiệm vụ đều mở hoặc nhận được runtime (I-08:35,142).
- [TÀI LIỆU] I-08 dẫn tiến độ daily kill ở DLY:124,150,177,184,188 và gather ở DLH:19,29. Báo cáo cho biết NPC daily mẫu không có đoạn reset ngày trong 267 dòng được đọc; nơi reset có thể ở thành phần khác nhưng chưa xác minh (I-08:134–142).
- [TÀI LIỆU] I-08 mô tả random/task_head.lua giới hạn 10 random và 8 scroll mỗi ngày, kèm các dòng được trích tại :50,68,76,174,214,253,185,225. SO-10 không mở lại file Lua này (I-08:137,287–288).
- [CHƯA KIỂM] Không có đủ bằng chứng cho chu kỳ tuần, ngày bắt đầu tuần, reset theo ngày mới hay khớp đồng hồ máy chủ với giờ người chơi. Không kết luận hệ thống không có quest tuần.
- [THẤY] Client source gọi khởi tạo Lua ở thư mục Ui (C/gamecore/KCore.cpp:392). Nội dung UI script rời hoặc trong gói không được kiểm trong task này.

## Sự kiện và ví dụ Lua để tra cứu

Đường G và dòng Lua dưới đây được trích từ báo cáo nền, chưa mở lại trực tiếp trong lượt SO-10.

| Chủ đề | Tệp Lua và dòng theo báo cáo | Nội dung được ghi | Mức |
|---|---|---|---|
| Bộ gọi sự kiện theo giờ | G/script/servertimer.lua:36–58,79–137 | Dấu vết lịch và lệnh kích hoạt; D-01/K-02 có ghi nhận khác nhau về dòng 125 | TÀI LIỆU |
| Nhiệm vụ hằng ngày | G/script/tnlteam/task_hang_ngay/lib_hang_ngay.lua:12–21,54–124 | Có luồng nhận/điều kiện/thưởng; menu/runtime chưa kiểm | TÀI LIỆU |
| Random có quota ngày | G/script/task/random/task_head.lua:50,68,76,174,214,253; :185,225 | Mốc ngày/quota theo I-08; reset thực tế chưa xác minh | TÀI LIỆU |
| Hoa đăng | G/script/subject/hoadang/lib.lua:64–89 | Có cửa sổ giờ và timeout 15 phút theo D-01; không chứng minh lịch ngày lễ | TÀI LIỆU |
| Đêm Huy Hoàng | G/script/subject/demhuyhoang/event.lua:192–218 | Có NPC timeout; các mốc được ghi cần kiểm activation | TÀI LIỆU |
| Boss tiểu Hoàng Kim | G/script/subject/bosstieuhk/bosstieuhk.lua:49–60 | Tạo đợt với timeout 30 phút theo D-01 | TÀI LIỆU |
| Timer theo nhân vật | S/Core/Src/KTaskFuns.cpp:118–131,190–196 | Source C++ gọi callback OnTimer | THẤY |

### Ngày lễ

- [TÀI LIỆU] Hoa đăng là ví dụ sự kiện có cửa sổ giờ trong script mà D-01 dẫn (G/script/subject/hoadang/lib.lua:64–89; D-01:66).
- [CHƯA KIỂM] Chưa có bằng chứng về ngày âm lịch, ngày lễ hằng năm, thứ trong tuần, mùa hoặc quy tắc đổi lịch theo năm. Tên sự kiện không đủ để suy ngày chạy.

## Sắp theo cấu trúc game

1. Vòng server: Breathe → servertimer.lua::Main (S/Core/Src/CoreServerShell.cpp:2227–2246).
2. Sự kiện toàn server và nội dung theo giờ: servertimer cùng các thư mục subject/tnlteam; activation còn cần kiểm (D-01:52–70).
3. Timer theo nhân vật: TimerTask → Activate → OnTimer; dùng GetGameTime, lưu ID/thời gian còn lại (S/Core/Src/KTaskFuns.h:54–66; S/Core/Src/KTaskFuns.cpp:118–196).
4. Nhiệm vụ ngày/random: dữ liệu Settings/Task → script → biến tiến độ/quota; không đồng nhất bộ đếm này với timer sự kiện (I-08:35–38,134–142).
5. Nhiệm vụ tuần/lịch ngày lễ: chưa đủ dữ liệu để xếp vào chu kỳ thực tế.

## Phạm vi và độ phủ

| Câu hỏi | Độ phủ | Bằng chứng / giới hạn |
|---|---|---|
| Vòng server gọi lịch Lua | Đã xác minh tĩnh | S/Core/Src/CoreServerShell.cpp:2227–2246 |
| Timer, callback, lưu thời gian còn lại | Đã xác minh tĩnh | S/Core/Src/KTaskFuns.h:12–15,54–66; S/Core/Src/KTaskFuns.cpp:104–131,135–196 |
| Đơn vị, giờ địa phương và múi giờ | Chưa phủ | Chưa đo hoặc xác minh hàm thời gian trong Lua thực nạp |
| Mẫu nhiệm vụ ngày | Đã đối chiếu tài liệu | I-08:35,134–142; reset/runtime chưa kiểm |
| Nhiệm vụ tuần | Chưa phủ | Nguồn đã chỉ định không cung cấp bằng chứng đủ |
| Sự kiện theo giờ/ngày lễ | Đã đối chiếu tài liệu một phần | D-01:52–70; activation và ngày lịch chưa xác minh |
| Danh sách Lua tiêu biểu có dòng | Đã lập | Dòng G lấy từ báo cáo nền, chưa mở trực tiếp trong SO-10 |

liên quan: JX1_OPS/REPORTS/K-02-script-lua.md; JX1_OPS/REPORTS/I-08-he-thong-nhiem-vu.md; JX1_OPS/REPORTS/D-01-bang-hoat-dong.md.

## Giải mã tên

ID ASCII được giữ nguyên. Nhãn tiếng Việt lấy từ báo cáo nền, không phải giải mã byte hoặc xác nhận tên hiển thị trong game.

| Tên gốc | Mã hóa | Chữ đúng / nhãn tài liệu | Nguồn |
|---|---|---|---|
| servertimer | ASCII | Bộ gọi sự kiện theo giờ | S/Core/Src/CoreServerShell.cpp:2231; D-01:52–53 |
| task_hang_ngay | ASCII | Nhiệm vụ hằng ngày | D-01:70 |
| hoadang | ASCII | Hoa đăng | D-01:66 |
| demhuyhoang | ASCII | Đêm Huy Hoàng | D-01:67 |
| bosstieuhk | ASCII | Boss tiểu Hoàng Kim | D-01:68 |
| battlesongjin | ASCII | Nhánh Tống Kim | D-01:62 |
| fenglingdu | ASCII | Nhánh Phong Lăng Độ | D-01:63 |
| TimerTask | ASCII | Bảng cấu hình timer người chơi | S/Core/Src/KTaskFuns.h:14 |

## Mục sổ thông số

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---:|---|---|---|---|
| Vòng server | GAME_FPS | S/Core/Src/CoreServerShell.cpp:2227 | 18 | khung trong phép chia | Điều kiện gọi Main; không quy đổi thành giây | CẨN THẬN | Đọc source |
| Vòng server | wSecond | S/Core/Src/CoreServerShell.cpp:2236–2240 | 0 | giây | Điều kiện gọi Main | CẨN THẬN | Đọc source |
| Timer | ulTime | S/Core/Src/KTaskFuns.h:54–66 | tham số gọi | đơn vị GetGameTime chưa rõ | Thời gian đến hạn/lặp | KHÔNG tự đổi | Đọc source |
| Lưu timer | task key | S/Core/Src/KTaskFuns.h:12–14 | 220 / 221 | khóa task | Lưu timer ID và thời gian còn lại | KHÔNG tự đổi | Đọc source |
| Random ngày | quota random/scroll | I-08:287–288; G/script/task/random/task_head.lua:185,225 | 10 / 8 | lượt/ngày | Mô tả báo cáo, runtime chưa kiểm | CẨN THẬN | Dẫn lại báo cáo |

## Đã xác minh / Chưa xác minh

**ĐÃ XÁC MINH:** Đọc tĩnh source server S/Core/Src/CoreServerShell.cpp:2227–2246, KTaskFuns.h:12–15,54–66 và KTaskFuns.cpp:104–131,135–196; đọc dấu vết gọi loader client C/gamecore/KCore.cpp:392. Đọc ba báo cáo Lua/task/sự kiện được task chỉ định.

**CHƯA XÁC MINH:** Nội dung G Lua được liệt kê chưa mở lại trực tiếp; các dòng Lua lấy từ báo cáo nền. Không xác minh file thực được nạp, múi giờ, quy đổi tick, reset ngày/tuần, lịch lễ, PAK hoặc runtime.

## Đề xuất tối ưu

1. Khi có task chỉ đọc riêng cho lịch, đối chiếu file TimerTask và tasklist mà loader thực dùng trước khi lập lịch biểu hoàn chỉnh.
2. Giữ ulTime theo đơn vị source đến khi GetGameTime và call site được xác minh; không đổi thành giây từ GAME_FPS.
3. Xác minh reset ngày/tuần và ngày lễ trong nguồn được nạp hoặc fixture được duyệt trước khi mô tả lịch thực tế.

## Phát hiện khi tổng hợp

- [CHƯA KIỂM] D-01 ghi servertimer.lua:125 có một dấu nháy, còn K-02 ghi kiểm tra sau thấy hai dấu nháy. Giữ nguyên khác biệt, không tự chọn kết luận hay xác nhận cú pháp (D-01:52; K-02:4).
- [CHƯA KIỂM] Các dòng Lua dưới G được dẫn lại từ K-02/I-08/D-01, chưa mở tệp Lua trực tiếp trong lượt SO-10.

## Bàn giao

- Đầu ra chính: JX1_OPS/DESIGN/SO-TAY-THOI-GIAN-SU-KIEN.md.
- Chỉ mục đề xuất PM gộp: file=JX1_OPS/DESIGN/SO-TAY-THOI-GIAN-SU-KIEN.md; loại=khảo sát; chủ đề=thời gian, lịch, sự kiện Lua; từ khóa=thời gian, timer, nhiệm vụ ngày, tuần, Hoa đăng, servertimer; trạng thái=DONE; độ phủ=7 câu hỏi đã phân loại; liên quan=K-02,I-08,D-01.
- Không commit/push theo yêu cầu task; chưa có SHA. Không ghi được nhịp D:/JX-wt/SO-10.nhip do sandbox từ chối quyền ghi ngoài worktree; không thử vượt quyền.
- Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
