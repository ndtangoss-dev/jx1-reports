TÓM TẮT 1 — [NGUỒN][THẤY] Có 7 nhánh lệnh GM trực tiếp trong server; không thấy kiểm cờ GM ngay trong hàm nhận: `S/Core/Src/KProtocolProcess.cpp:8185-8238`.
TÓM TẮT 2 — [NGUỒN][THẤY] Client VN nhận tiền tố `#gm?` từ ô chat rồi gửi gói GM riêng: `C/vn/gamescence/KgameWorldVN.cpp:4500-4512`, `C/gamecore/KProtocol.cpp:1208-1216`.
TÓM TẮT 3 — [NGUỒN][THẤY] Bảng văn bản có 9 tên `Fs…`, nhưng nhiều đường thực thi đã bị chú thích; Lua có nhóm 9 tên `gm_*`: `S/Core/Src/KGMCommand.cpp:9-25,128-159`, `S/Core/Src/ScriptFuns.cpp:26451-26459`.
TÓM TẮT 4 — [NGUỒN][CHƯA KIỂM] Chưa xác nhận tập lệnh console gs001: thiếu `C:/JX/sql/console.ps1` và D-02; vòng lặp đã đọc không có bộ phân tích lệnh nhập: `S/MultiServer/GameServer/GameServer.cpp:183-215`.
TÓM TẮT 5 — [CHƯA KIỂM] Chỉ đọc tĩnh ngày 19/11/2026; chưa build, chạy exe, VM, mạng hoặc thử lệnh; chưa nối mã trên đĩa với binary đang chạy. Phạm vi duyệt: `JX1_OPS/TASKS/HG-13.md:26-31`.

# HG-13 — Hiểu lệnh GM và công cụ quản trị trong server

Loại: khảo sát
Chủ đề: Những đường gọi lệnh quản trị, tác dụng thấy trong mã và chỗ kiểm quyền đã đối chiếu.
Từ khóa: lệnh GM, Game Master, console, gs001, Lua, gm_operation, c2s_gmcommand, jxadm, jxweb
Trạng thái: DONE — hoàn tất tài liệu khảo sát tĩnh; các mắt xích thiếu nguồn được ghi CHƯA KIỂM, không xác nhận vận hành.
Độ phủ: xử lý 6/6 nhóm câu hỏi; nhóm Lua liên GS và console còn mắt xích chưa kiểm; không kiểm kê toàn bộ API Lua của game.
Liên quan: `JX1_OPS/REPORTS/HG-13.md`, `JX1_OPS/REPORTS/C-01-jxadm.md`, `JX1_OPS/REPORTS/C-03-jxweb.md`, `JX1_OPS/DESIGN/CHUAN-BAO-CAO.md`
Cần tôi quyết định: không

## Cách đọc bằng chứng

- [THẤY] = ĐÃ XÁC MINH bằng đọc mã tại dòng dẫn, chỉ đúng bản trên đĩa; [TÀI LIỆU] = báo cáo cũ nói, chưa tự thử lại; [CHƯA KIỂM] = còn thiếu nguồn hoặc phép thử.
- Gốc `S` = `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; gốc `C` = `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes`. Mọi dẫn `S/...:dòng` và `C/...:dòng` đều nối với hai gốc này.
- [THẤY] Tên lệnh và ký hiệu C++ dùng ASCII. Đoạn chú thích Hán cần đọc GBK/CP936; không dùng chữ lỗi khi mở bằng mã hóa mặc định làm bằng chứng ý nghĩa. Client VN có chú thích đã hỏng chữ; tài liệu chỉ suy từ câu lệnh, không tự phục hồi tên game: `C/vn/gamescence/KgameWorldVN.cpp:4359-4384,4500-4512`.

## Sơ đồ chính

```mermaid
flowchart TD
    A[Ô chat client VN] --> B[Nhận tiền tố GM]
    B --> C[Gói c2s_gmcommand]
    C --> D[GMCommand: 7 nhánh trực tiếp]
    E[Script Lua do server nạp] --> F[GameScriptFuns]
    F --> G[9 hàm gm_*]
    G --> H[Gateway: tuyến trung gian chưa đối chiếu]
    H -.-> I[GS nhận thông điệp quản trị]
    I --> J[gm_OperationRequest]
    J --> K[gm_operation.lua: chưa có nội dung để đối chiếu]
    L[Bộ từ vựng Fs cũ] -. Đường chat và relay bị chú thích .-> M[TextMsgProcessGMCmd]
    N[Console gs001] -. Thiếu console.ps1 và D-02 .-> O[Chưa xác nhận lệnh vận hành]
```

[THẤY] Các cạnh liền dựa trên `C/vn/gamescence/KgameWorldVN.cpp:4500-4512`, `C/gamecore/KProtocol.cpp:1208-1216`, `S/Core/Src/KProtocolProcess.cpp:323,8185-8238`, `S/Core/Src/KSortScript.cpp:161-166`, `S/Core/Src/ScriptFuns.cpp:20612-20761,26451-26459`, `S/MultiServer/GameServer/KSOServer.cpp:4167-4180`, `S/Core/Src/CoreServerShell.cpp:316-325`. Các cạnh đứt không chứng minh tuyến chạy thông suốt.

## Phạm vi và độ phủ

| Nhóm cần trả lời | Độ phủ | Căn cứ và giới hạn |
|---|---|---|
| Lệnh GM trực tiếp từ client | Đã phủ tĩnh 7/7 nhánh của hàm nhận | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8185-8238`; chưa thử tác dụng thực tế |
| Bộ lệnh văn bản `Fs…` | Đã phủ tĩnh 9/9 tên trong bảng | [THẤY] `S/Core/Src/KGMCommand.cpp:9-25,88-165`; phân biệt mã hoạt động, hàm rỗng và chú thích |
| Lua và thao tác liên GS | Một phần: 9/9 tên nhóm `gm_*`, 5 API hỗ trợ và một số API thế giới | [THẤY] `S/Core/Src/ScriptFuns.cpp:26345-26349,26451-26459,26931-27048`; [CHƯA KIỂM] script triển khai, tuyến gateway và toàn bộ thư viện Lua |
| Quyền GM | Đã đối chiếu các điểm kiểm trong đường đã đọc | [THẤY] `S/Core/Src/KCore.h:308-321`, `S/Core/Src/KPlayerDBFuns.cpp:591-594`, `S/Core/Src/KPlayer.cpp:6054-6069`; chưa đọc danh sách tài khoản hay kiểm runtime |
| Công cụ ngoài game | Dẫn lại đúng 2 báo cáo hiện có | [TÀI LIỆU] `JX1_OPS/REPORTS/C-01-jxadm.md:13,29-37`, `JX1_OPS/REPORTS/C-03-jxweb.md:14-23,53-57`; không chạy công cụ |
| Console gs001 | Một phần; tập lệnh vận hành CHƯA KIỂM | [THẤY] `S/MultiServer/GameServer/GameServer.cpp:183-215`; [CHƯA KIỂM] không thấy báo cáo D-02 theo bộ lọc tên và không có `C:/JX/sql/console.ps1` khi kiểm ngày 19/11/2026 |

## Giải mã tên

[THẤY] Không trích tên riêng của kỹ năng, trang bị, quái, NPC hoặc bản đồ trong phạm vi này; vì vậy không có tên Hán/TCVN3 cần đoán lại. Những tên công cụ và định danh cần giữ nguyên được giải nghĩa dưới đây. Bảng lệnh ở phần sau giữ đủ tên gốc, không đổi tên trong mã.

| Tên gốc | Mã hóa | Chữ đúng / cách hiểu UTF-8 | Nguồn file:dòng |
|---|---|---|---|
| `GM`, `c2s_gmcommand`, `GMCommand` | ASCII | Game Master; gói và hàm xử lý lệnh quản trị | [THẤY] `S/Core/Src/KProtocolProcess.cpp:323,8185-8238` |
| `Lua`, `GameScriptFuns`, `WorldScriptFuns` | ASCII | Hệ script; tập hàm game và tập hàm thế giới | [THẤY] `S/Core/Src/KSortScript.cpp:164`, `S/Core/Src/KGMCommand.cpp:102-108` |
| `gs001` | ASCII | Tên đích build của một cấu hình dự án GameServer; chưa đối chiếu binary | [THẤY] `S/MultiServer/GameServer/GameServer.vcxproj:107` |
| `jxadm` | ASCII | Công cụ lập kế hoạch quản trị tài khoản ngoại tuyến | [TÀI LIỆU] `JX1_OPS/REPORTS/C-01-jxadm.md:11-13` |
| `jxweb` | ASCII | Trang quản trị nội bộ dùng dữ liệu dry-run/giả | [TÀI LIỆU] `JX1_OPS/REPORTS/C-03-jxweb.md:12-18` |

## Sắp theo cấu trúc game

[THẤY] Tài liệu xếp theo nơi tác động: nhân vật và tiền → hoạt động liên GS → script/thế giới → quyền → công cụ vận hành. Không xếp theo thứ tự file. Cơ sở chia nhóm là nhánh xử lý trong `S/Core/Src/KProtocolProcess.cpp:8206-8235` và bảng đăng ký Lua tại `S/Core/Src/ScriptFuns.cpp:26451-26459,26931-27048`.

## 1. Người quản trị gọi lệnh từ đâu?

[THẤY] Ở client VN, nút gửi chat đi vào `KgameWorldVN::onsendCallback`. Hàm lấy chữ trong ô nhập; gặp tiền tố `#gm?` ở đầu chuỗi thì bỏ bốn ký tự đầu, bỏ khoảng trắng đầu phần còn lại, gửi bằng `SendClientCmdGMCommand`, xóa ô nhập rồi dừng đường gửi chat thường. Không thấy kiểm `m_isGm` trong phần đầu và nhánh gửi này. Có chặn riêng kênh `ch_GM`, nên không được suy rằng mọi kênh đều tới được nhánh đó: `C/vn/gamescence/KgameWorldVN.cpp:4359-4387,4451-4464,4500-4512`.

[THẤY] Hàm gửi tạo gói `GM_COMMAND` mang loại `c2s_gmcommand`. Server đăng ký loại gói này vào `KProtocolProcess::GMCommand`; bộ phân phối đã đọc chuyển theo loại gói và chỉ mục người chơi, không thấy phân nhánh theo quyền GM tại đây: `C/gamecore/KProtocol.cpp:1208-1216`, `S/Core/Src/KProtocolProcess.cpp:323,349-362`.

[CHƯA KIỂM] Chưa chứng minh client VN này là bản client đang dùng; chưa chứng minh mọi lớp nhận gói phía trước đều cho phép tới hàm trên. Kết luận “tài khoản thường thực sự gọi được” cần một nhiệm vụ kiểm thử riêng, không suy từ tên gói hoặc việc thiếu kiểm quyền tại một hàm. Căn cứ giới hạn: `C/vn/gamescence/KgameWorldVN.cpp:4500-4512`, `S/Core/Src/KProtocolProcess.cpp:349-362,8185-8238`.

### Bảy nhánh trực tiếp vào nhân vật hoặc tiến trình GS

[THẤY] Server tách chuỗi theo dấu phẩy, lấy phần đầu làm tên lệnh và đổi phần sau thành số bằng `atoi`; tên so sánh đúng hoa/thường. Bảng chỉ mô tả hành vi mã, không cung cấp chuỗi lệnh để thao tác server: `S/Core/Src/KProtocolProcess.cpp:8191-8206`.

| Tên gốc | Tác dụng thấy trong hàm nhận | Phạm vi | Bằng chứng |
|---|---|---|---|
| `Earn` | Gọi hàm cộng tiền `Earn(value)` | Người gửi | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8206-8209` |
| `EarnAll` | Lặp các ô người chơi và gọi `Earn(value)` | Vòng lặp từ 0 đến trước `MAX_PLAYER`; không lọc online tại đây | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8210-8214` |
| `EarnXu` | Gọi hàm cộng Xu `EarnXu(value)` | Người gửi | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8215-8218` |
| `EarnXuAll` | Lặp các ô người chơi và gọi `EarnXu(value)` | Cùng giới hạn `MAX_PLAYER` | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8219-8223` |
| `SetLevel` | Gọi hàm đặt cấp `SetLevel(value)` | Người gửi | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8224-8227` |
| `SetLevelAll` | Lặp các ô người chơi và gọi `SetLevel(value)` | Cùng giới hạn `MAX_PLAYER` | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8228-8232` |
| `TatGS` | Gọi `exit(0)` trực tiếp | Tiến trình GS đang xử lý | [THẤY] `S/Core/Src/KProtocolProcess.cpp:8233-8235` |

[CHƯA KIỂM] Không dùng bảng trên để khẳng định tiền/cấp được lưu bền, mọi người online đều nhận, giá trị âm bị chặn hay tắt GS có lưu an toàn. Task chỉ đối chiếu hàm gọi, chưa khảo sát toàn bộ hàm tiền/cấp, lưu dữ liệu và quá trình thoát: `S/Core/Src/KProtocolProcess.cpp:8206-8235`.

## 2. Bộ văn bản `Fs…` còn làm việc không?

[THẤY] Bộ lọc cũ kiểm ký tự đầu `?`, rồi so bốn byte tương ứng `?gm ` hoặc `?GM ` trên kiến trúc little-endian. Chú thích trong mã lại ghi `/gm`; không dùng chú thích đó làm cú pháp đúng. Sau tiền tố, tên trong bảng được so bằng `strcmp`: `S/Core/Src/KGMCommand.cpp:6-7,37-42,79-82`.

| Tên gốc trong bảng | Ý nghĩa thiết kế | Trạng thái thấy trong mã |
|---|---|---|
| `FsDoSct`, `Fsds` | Chạy đoạn Lua theo người chơi | [THẤY] Gọi `DoScript`, nhưng hàm này trả TRUE ngay, phần chạy Lua bị chú thích: `S/Core/Src/KGMCommand.cpp:11-12,114-125`, `S/Core/Src/KPlayer.cpp:8752-8782` |
| `Fsdw` | Chạy đoạn Lua theo thế giới | [THẤY] Nhánh tạo môi trường Lua, đăng ký `WorldScriptFuns`, nạp và chạy đoạn mã còn hiện hữu; đường gọi vào bộ lọc chưa thấy hoạt động: `S/Core/Src/KGMCommand.cpp:14,94-110` |
| `FsRunSctFile`, `FsRSF` | Chạy một file script | [THẤY] Tên còn trong bảng, nhánh xử lý nằm trong chú thích: `S/Core/Src/KGMCommand.cpp:16-17,128-145` |
| `FsReLoadSct`, `FsRLS` | Nạp lại một script | [THẤY] Tên còn trong bảng, nhánh xử lý nằm trong chú thích: `S/Core/Src/KGMCommand.cpp:19-20,146-155` |
| `FsReLoadAllSct`, `FsRLAS` | Nạp lại toàn bộ script | [THẤY] Tên còn trong bảng, nhánh xử lý nằm trong chú thích: `S/Core/Src/KGMCommand.cpp:22-23,156-159` |

[THẤY] Không thể gọi đây là bộ lệnh vận hành đã sẵn sàng: lời gọi `TextGMFilter` từ chat bị bọc trong chú thích; phần thực thi của `P_ProcessGMExecute` và `ExecuteLocalServer` cũng bị chú thích. Bảng đăng ký giao thức relay vẫn có tên các hàm đó, nhưng đăng ký không làm phần thân rỗng hoạt động: `S/Core/Src/KPlayerChat.cpp:491-496`, `S/Core/Src/KGMProcess.cpp:32-40,82-93`, `S/Core/Src/KNewProtocolProcess.cpp:15-16`.

[THẤY] Relay còn một hàm tìm người chơi `P_ProcessGMFindPlayer`, chuẩn bị thông tin vị trí để trả về. [CHƯA KIỂM] Xác thực ở đầu tuyến relay và khả năng dùng thực tế chưa đối chiếu; không gộp chức năng tìm người với quyền thực thi Lua: `S/Core/Src/KGMProcess.cpp:42-80`.

## 3. Lua và công cụ quản trị trong thế giới game

[THẤY] Khi nạp script, server đăng ký `GameScriptFuns` vào môi trường Lua. Hàm `ExecuteScriptA` tìm script đã nạp rồi chuyển sang `ExecuteScriptB`; phần sau gán bối cảnh người chơi và thế giới trước khi gọi hàm Lua. Đây là hạ tầng chung, không riêng GM: `S/Core/Src/KSortScript.cpp:161-166`, `S/Core/Src/KPlayer.cpp:7997-8016,8020-8055`.

### Nhân vật trên GS khác và quản trị theo khu

[THẤY] Chín tên dưới đây được đăng ký trong bảng hàm game; ý nghĩa ghi theo thông điệp mà hàm C++ tạo ra, chưa khẳng định thay đổi cuối cùng đã xảy ra: `S/Core/Src/ScriptFuns.cpp:26451-26459`.

| Tên Lua gốc | Mục đích / hành vi gửi yêu cầu | Bằng chứng phần thân |
|---|---|---|
| `gm_Money` | Gửi yêu cầu xử lý tiền cho tên nhân vật | [THẤY] `S/Core/Src/ScriptFuns.cpp:20656-20676` |
| `gm_Xu` | Gửi yêu cầu xử lý Xu cho tên nhân vật | [THẤY] `S/Core/Src/ScriptFuns.cpp:20678-20697` |
| `gm_Level` | Gửi yêu cầu xử lý cấp cho tên nhân vật | [THẤY] `S/Core/Src/ScriptFuns.cpp:20634-20654` |
| `gm_TaskId` | Gửi ID nhiệm vụ và giá trị cho tên nhân vật | [THẤY] `S/Core/Src/ScriptFuns.cpp:20699-20721` |
| `gm_ForbitChat` | Gửi yêu cầu cấm chat; giữ nguyên cách viết `Forbit` của mã | [THẤY] `S/Core/Src/ScriptFuns.cpp:20724-20742` |
| `gm_KickOutPlayer` | Gửi yêu cầu xử lý ngắt người chơi theo tên và chế độ | [THẤY] `S/Core/Src/ScriptFuns.cpp:20745-20761` |
| `gm_MoveTo` | Gửi yêu cầu định vị/di chuyển liên quan hai tên nhân vật | [THẤY] `S/Core/Src/ScriptFuns.cpp:20612-20631` |
| `gm_LocalScript` | Gửi thông điệp nạp lại script theo khu | [THẤY] `S/Core/Src/ScriptFuns.cpp:6348-6365` |
| `gm_AddNpc` | Gửi thông điệp thêm NPC theo khu và chỉ số máy chủ | [THẤY] `S/Core/Src/ScriptFuns.cpp:6329-6346` |

[THẤY] Phía gửi dùng `g_pGateWayClient`. Phía GS có nhánh nhận nhóm yêu cầu quản trị, chuyển vào `gm_OperationRequest`; hàm này tìm nhân vật theo tên rồi gọi `\script\system\gm_operation.lua`, hàm `gm_operation`. Một số mã nhận còn liên quan phúc duyên, danh vọng, kinh nghiệm, nhưng chưa lần được đầy đủ đường tạo các yêu cầu đó: `S/Core/Src/ScriptFuns.cpp:20620-20629,20642-20651`, `S/MultiServer/GameServer/KSOServer.cpp:4090-4112,4167-4180`, `S/Core/Src/CoreServerShell.cpp:316-325`.

[CHƯA KIỂM] Chưa đọc nội dung `gm_operation.lua`, script/menu GM gọi các hàm trên hoặc phần trung gian gateway. Không biết script có kiểm thêm quyền, giới hạn giá trị, ghi nhật ký hay trả kết quả thế nào. Các đường dẫn Lua là tham chiếu lấy từ mã, không được coi là file đã kiểm tồn tại: `S/Core/Src/CoreServerShell.cpp:325`, `S/Core/Src/ScriptFuns.cpp:26451-26459`.

### Nạp lại script và điều khiển thế giới

| Nhóm | Tên API đã thấy | Mức xác minh |
|---|---|---|
| Gọi/nạp lại script cục bộ | `ExeScript`, `LocalScript`, `LocalAllScript` | [THẤY] Đăng ký tại `S/Core/Src/ScriptFuns.cpp:26345-26347`; phần thân gọi script/nạp lại tại `:20250-20262,20462-20501`. `ExeScript` lấy tên hàm từ tham số thứ hai, không mặc định rằng luôn gọi `main` theo chú thích cũ |
| Nạp lại cấu hình | `LocalSerIni`, `LocalSerTxt` | [THẤY] Đăng ký tại `S/Core/Src/ScriptFuns.cpp:26348-26349`; nhánh `LocalSerTxt` số 4 nạp `g_GMSetting`, số 18 nạp `g_gmList`: `:20337-20342,20443-20448`. Chưa kiểm mọi lựa chọn |
| Thông báo | `AddLocalNews`, `AddSysNews`, `AddGlobalNews_All` | [THẤY] Có tên trong tập hàm thế giới, chưa khảo sát mọi tham số/phạm vi phát: `S/Core/Src/ScriptFuns.cpp:26934-26940` |
| NPC và bản đồ | `AddNpc`, `DelNpc`, `ClearMapNpc`, `ClearMapTrap`, `ClearMapObj` | [THẤY] Có tên trong tập hàm thế giới; chưa xác nhận tác dụng từng hàm bằng runtime: `S/Core/Src/ScriptFuns.cpp:26963-26964,26990-26992` |
| Phiên người chơi | `KickOutPlayer`, `KickOutAccount`, `ShutDownClient` | [THẤY] Đăng ký trong tập hàm thế giới; không phải bằng chứng đây là lệnh console: `S/Core/Src/ScriptFuns.cpp:26984-26986` |
| Hoạt động | `OpenMission`, `RunMission`, `CloseMission`, `StartMissionTimer`, `StopMissionTimer` | [THẤY] Đăng ký trong tập hàm thế giới, chưa kiểm quyền ở mọi caller: `S/Core/Src/ScriptFuns.cpp:27014-27018` |

[THẤY] Không phải mọi gói có chữ “script” đều là cửa chạy lệnh GM tùy ý. Chẳng hạn `c2splayerdoScript` dẫn tới các đường script hoạt động/rèn cố định trong mã; cần đọc riêng từng tuyến trước khi gọi là công cụ GM: `S/Core/Src/KProtocolProcess.cpp:8652-8689`.

## 4. Quyền GM được kiểm thế nào?

| Điểm quan sát | Điều mã thực sự kiểm | Kết luận có giới hạn |
|---|---|---|
| Khi nạp dữ liệu nhân vật | Dùng `checkGmList` với trường tài khoản, đặt `m_isGm` bằng 1 hoặc 0 | [THẤY] Có cờ GM; tham số helper tên `roleName` nhưng caller đưa tài khoản: `S/Core/Src/KPlayerDBFuns.cpp:591-594`, `S/Core/Src/KCore.h:308-321` |
| Danh sách nền | `g_gmList` nạp `settings/gmgamelist.txt`; `g_GMSetting` nạp qua hằng `GAME_GM_FILE` | [THẤY] Có hai đối tượng bảng; không đọc nội dung tài khoản và chưa giải hằng đường dẫn thứ hai: `S/Core/Src/KCore.cpp:596-597,658-659` |
| `CheckGmName` | So tài khoản với cột đầu `g_GMSetting`, không phân biệt hoa/thường qua `stricmp` | [THẤY] Có hàm kiểm riêng, nhưng việc tồn tại hàm không chứng minh mọi lệnh đều gọi nó: `S/Core/Src/KPlayer.cpp:6054-6069` |
| Bảy lệnh trực tiếp | Chỉ thấy kiểm chỉ mục người chơi trong khoảng hợp lệ rồi phân tích chuỗi | [THẤY] Không thấy `CheckGmName`, `checkGmList` hoặc `m_isGm` trong toàn hàm nhận; chưa chứng minh bảo vệ đầu tuyến: `S/Core/Src/KProtocolProcess.cpp:8185-8238` |
| Chín wrapper Lua `gm_*` | Kiểm số đối số và kiểm con trỏ kết nối trước gửi ở các hàm đã đọc | [THẤY] Không thấy chốt quyền GM trong những thân hàm này; quyền ở script gọi và gateway CHƯA KIỂM: `S/Core/Src/ScriptFuns.cpp:6329-6365,20612-20761` |
| Lua gọi/nạp lại cục bộ | `ExeScript`, `LocalScript`, `LocalAllScript` kiểm chỉ mục/ID người chơi | [THẤY] Kiểm bối cảnh người chơi không đồng nghĩa kiểm quyền GM: `S/Core/Src/ScriptFuns.cpp:20250-20262,20462-20501` |
| Giao diện client | Có chỗ dùng `m_isGm` để bật/tắt thống kê hiển thị | [THẤY] Đây là điều kiện giao diện, không phải bằng chứng server chặn lệnh GM: `C/vn/gamescence/KgameWorldVN.cpp:2855-2869` |

[CHƯA KIỂM] Chưa có bằng chứng về các cấp GM nhiều tầng, ai đang được cấp quyền, thay đổi danh sách có cần đăng nhập lại, cơ chế xác thực của gateway hay nhật ký đủ để truy vết người ra lệnh. Không đọc file chứa danh sách tài khoản để trả lời các câu hỏi đó. Điểm định vị: `S/Core/Src/KPlayerDBFuns.cpp:591-594`, `S/Core/Src/KCore.h:308-321`, `S/Core/Src/CoreServerShell.cpp:316-325`.

## 5. Console gs001 và công cụ quản trị ngoài game

[THẤY] Dự án GameServer có tên đích `gs001` ở một cấu hình. Đoạn `main` đã đọc nhận một đối số làm cổng, khởi tạo server, lặp `Breathe`, cuối cùng có `getchar`; không thấy bộ nhận câu lệnh quản trị trong đoạn đó. `MultiServer/Common/Console.cpp` chỉ có tiện ích xóa màn hình, vị trí con trỏ và màu chữ, không phải danh mục lệnh: `S/MultiServer/GameServer/GameServer.vcxproj:107`, `S/MultiServer/GameServer/GameServer.cpp:183-215`, `S/MultiServer/Common/Console.cpp:12-147`.

[CHƯA KIỂM] Không tìm thấy `C:/JX/sql/console.ps1` và không thấy D-02 khi lọc tên trong `JX1_OPS/REPORTS/` ngày 19/11/2026. Vì vậy không đưa ra danh sách lệnh gõ trong console, cú pháp chạy console hay cách kiểm quyền của công cụ đó. Không suy rằng mọi bản gs001 đều không có console từ một đoạn `main`. Nguồn cần bổ sung đã được chỉ rõ tại `JX1_OPS/TASKS/HG-13.md:23-25`.

| Công cụ | Điều báo cáo cũ đã nói | Giới hạn được giữ nguyên |
|---|---|---|
| `jxadm` | Có `create`, `lock`, `unlock`, `reset-password`, `online`, `mark-bot`, `backup-characters` | [TÀI LIỆU] CLI chỉ dry-run, sinh kế hoạch; không có adapter thật hoặc bằng chứng hiệu lực trên server. Chỉ liệt kê tên, không nêu dữ liệu xác thực: `JX1_OPS/REPORTS/C-01-jxadm.md:13,29-37,51-55` |
| `jxweb` | Trang trạng thái, API trạng thái và kiểm tra tiến trình; dùng nguồn jxadm dry-run hoặc dữ liệu giả | [TÀI LIỆU] Chưa có write adapter thật, chưa xác minh trạng thái server/account thực. Không xem nó là bảng điều khiển đã có quyền sửa game: `JX1_OPS/REPORTS/C-03-jxweb.md:14-23,53-57` |

[TÀI LIỆU] Các test ngoại tuyến C-01/C-03 là kết quả lịch sử của hai báo cáo; HG-13 không chạy lại và không nâng kết luận thành đã kiểm trên server: `JX1_OPS/REPORTS/C-01-jxadm.md:71`, `JX1_OPS/REPORTS/C-03-jxweb.md:43-57`.

## Mục sổ thông số

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Gói GM trực tiếp | `m_szString` cục bộ | `S/Core/Src/KProtocolProcess.cpp:8191-8193` | 256; sao chép tối đa 255 | byte | Giới hạn bản sao phía nhận; không chứng minh mọi tầng đều an toàn | KHÔNG trong task này | Đọc tĩnh; chưa đo runtime |
| Bộ văn bản cũ | `szCmd` | `S/Core/Src/KGMCommand.cpp:64-76` | 20 | byte | Không thấy chốt độ dài trước các lệnh sao chép ở đoạn phân tích này | KHÔNG trong task này | Đọc tĩnh; không thử chuỗi bất thường |
| Lua văn bản cũ | `nLen` | `S/Core/Src/KGMCommand.cpp:96-100,116-123` | Lớn hơn 0, nhỏ hơn 300 | byte | Giới hạn đoạn mã nhận ở hai nhánh | KHÔNG trong task này | Đọc tĩnh; chưa xác nhận đường gọi hoạt động |
| Nạp lại cấu hình | Nhánh `LocalSerTxt` | `S/Core/Src/ScriptFuns.cpp:20337-20342,20443-20448` | 4 / 18 | mã lựa chọn | Nạp lại hai bảng GM đã nêu; không phải cấp quyền mới đã kiểm | KHÔNG trong task này | Đọc tĩnh; không nạp lại cấu hình |

## Đã xác minh / Chưa xác minh

- [THẤY] Đã kiểm file thật và dòng hiện tại của đường gửi client VN, bảy nhánh GM trực tiếp, chín tên `Fs…`, chín wrapper Lua `gm_*`, điểm nạp/so bảng GM và đường chuyển vào `gm_operation.lua`: các bảng ở mục 1–4.
- [TÀI LIỆU] Đã giữ nguyên các giới hạn dry-run, thiếu adapter và chưa đo server trong C-01/C-03; không sửa hai báo cáo cũ: `JX1_OPS/REPORTS/C-01-jxadm.md:13,51-65`, `JX1_OPS/REPORTS/C-03-jxweb.md:53-57`.
- [CHƯA KIỂM] Chưa có D-02, `console.ps1`, nội dung Lua GM triển khai, xác thực gateway, quyền thực tế của tài khoản, tập API đầy đủ hoặc mapping source–binary. Không dùng sơ đồ/Graphify thay bằng chứng source.
- [CHƯA KIỂM] Không chạy test nghiệp vụ, build, exe, VM, mạng hoặc lệnh quản trị. Kiểm tra đã thực hiện chỉ là đọc tĩnh và kiểm tra tài liệu; quyền task: `JX1_OPS/TASKS/HG-13.md:26-31`.

## Phát hiện khi đối chiếu và đề xuất tối ưu

- [THẤY] Tên lệnh còn trong bảng không đủ chứng minh lệnh chạy: có nhánh bị chú thích và có hàm trả thành công ngay. Cần giữ dấu phân biệt này khi viết hướng dẫn vận hành: `S/Core/Src/KGMCommand.cpp:128-159`, `S/Core/Src/KPlayer.cpp:8752-8782`.
- [THẤY] Chốt quyền chưa xuất hiện trong hàm nhận GM trực tiếp và các wrapper Lua đã đọc. Đề xuất PM mở nhiệm vụ rà soát phân quyền theo toàn tuyến; đây là phát hiện tĩnh, không phải xác nhận khai thác được: `S/Core/Src/KProtocolProcess.cpp:8185-8238`, `S/Core/Src/ScriptFuns.cpp:20612-20761`.
- [THẤY] Hai bảng `g_gmList` và `g_GMSetting` được sử dụng riêng; nhánh nạp lại số 18 dùng `GAME_GM_FILE`, còn nạp đầu của `g_gmList` dùng đường dẫn literal. Chưa đối chiếu định nghĩa hằng nên không kết luận lệch file: `S/Core/Src/KCore.cpp:596,658`, `S/Core/Src/ScriptFuns.cpp:20443-20447`.
- [TÀI LIỆU] Kết luận C-01/C-03 được giữ nguyên. Không chuyển kết quả test giả thành chứng nhận công cụ quản trị thật: `JX1_OPS/REPORTS/C-01-jxadm.md:53-65`, `JX1_OPS/REPORTS/C-03-jxweb.md:53-57`.

## Bàn giao

[THẤY] HG-13 chỉ thêm tài liệu này, báo cáo `JX1_OPS/REPORTS/HG-13.md` và mục Kết quả của task theo yêu cầu. Không stage/commit/push; Tổng quan chịu trách nhiệm gộp. Các giới hạn nguồn và lỗi ghi nhịp được bàn giao trong báo cáo HG-13.

[CHƯA KIỂM] Bước tiếp theo nếu PM cần hướng dẫn vận hành: bổ sung đúng D-02 và `console.ps1` đã lọc dữ liệu nhạy cảm; cấp phạm vi đọc script GM/gateway; chỉ kiểm thử trong nhiệm vụ được duyệt riêng. Không có thao tác chạy nào được cấp bởi tài liệu này.

liên quan: `JX1_OPS/REPORTS/HG-13.md`; `JX1_OPS/REPORTS/C-01-jxadm.md`; `JX1_OPS/REPORTS/C-03-jxweb.md`.

Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
