1. [ĐỀ XUẤT] Trước mắt lưu danh sách bot trong file riêng do gs001 nạp; tra theo khu vực + tài khoản + nhân vật tại `CoreServerShell::AddCharacter`, giữ cờ trong RAM của `KPlayer`.
2. [NGUỒN] `AddCharacter` đã nhận `TRoleData`, chép tài khoản/tên và giữ blob trước bước nạp NPC (`GS/Core/Src/CoreServerShell.cpp:423-453`).
3. [NGUỒN] `KPlayer::m_GaemSaveBuffer` có dung lượng 128 KiB; blob có version/offset/độ dài, không phải mọi bản ghi đều dài 128 KiB (`GS/Core/Src/KPlayer.h:284`; `GS-lib/S3DBInterface.h:184-201`).
4. [ĐỀ XUẤT] `IsBotPlayer(playerIdx)` chỉ kiểm slot và đọc cờ RAM; từ KNpc lấy `GetPlayerIdx()`, không thêm cờ vào packet/blob, không dùng trạng thái offline/autoplay làm danh tính bot.
5. [CHƯA KIỂM] Đây là khảo sát tĩnh, chưa sửa mã/schema/config, chưa build/test/runtime; triển khai cần kiểm vòng đời slot, đăng nhập lại và chuyển GS.

# C-02 — Chỗ lưu và điểm đọc cờ is_bot

Ngày khảo sát: 17/11/2026. Phạm vi: thiết kế, chưa sửa mã. Kết quả Git/commit nằm trong mục **Kết quả** của `JX1_OPS/TASKS/C-02.md`.

## Worker kiểm tra trước khi làm

- Đã kiểm tra trước khi ghi: `Get-Location` trả `D:\JX-wt\C-02`; `git status --short --branch` trả `## task/C-02-isbot`, không có thay đổi ban đầu. Khớp worktree/branch trong task.
- Đã đọc đầu vào A-02-luong-dang-nhap.md, A-05-diem-tuong-tac-gs001.md và B-01-LOC-HIEN-THI.md; đối chiếu thêm đúng các file nguồn liên quan nạp/lưu nhân vật và vòng đời slot.
- Chỉ ghi báo cáo này và mục Kết quả trong task. Nguồn `C:\Jx1CocoV3` chỉ đọc. Không chạy exe, VM, mạng, DB; không đọc dữ liệu tài khoản/roledb thực tế, không ghi thông tin đăng nhập thật.

## Quy ước bằng chứng

| Tiền tố | Gốc đường dẫn |
|---|---|
| `GS/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\` |
| `GS-lib/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\lib\` |
| `PAY/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\Sword3PaySys\S3AccServer\` |
| `Goddess/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\MultiServer\Goddess\` |

[NGUỒN] Dẫn `GS/` và `GS-lib/` là dòng nguồn đọc trực tiếp trong lượt này. Dẫn `PAY/`, `Goddess/` dưới đây được kế thừa từ `JX1_OPS/REPORTS/A-02-luong-dang-nhap.md`, các mục “Các bảng SQL”, “Goddess roledb” và “Đề xuất lưu cờ is_bot”; không khẳng định đã kiểm schema/runtime hiện tại. Các symbol mới như `m_bIsBot`/`BotRegistry` dưới đây đều là [ĐỀ XUẤT], chưa tồn tại do task này tạo.

## So sánh nơi lưu

| Phương án | Ưu điểm | Nhược điểm / điểm đọc cần thêm | Kết luận |
|---|---|---|---|
| `Account_Info.is_bot` mới | Cờ cấp tài khoản tập trung, dễ quản trị cùng danh tính. | Cần migration, rà tool/import và đường truyền sang GS; không phân biệt bot/người trong cùng tài khoản. GS không tự nhận cột mới qua blob. | [ĐỀ XUẤT] Có thể làm dài hạn, không phải đường ít thay đổi nhất. A-02: `PAY/S3PAccount.cpp:50-99,532,561`. |
| `Account_Habitus.is_bot` mới hoặc tái dùng cột | Thêm cột mới vẫn có thể quản trị tập trung. | Bảng đang phục vụ hạn/điểm; `iFlag`, `iLeftSecond`, `nExtPoint`, `iClientID` đã có nghĩa. Tái dùng có thể đổi tính phí/phiên, thêm cột mới vẫn cần truyền metadata. | [ĐỀ XUẤT] Không chọn bảng tính phí; tuyệt đối không mượn cột. A-02: `PAY/S3PAccount.cpp:64-124,351,546,593-640`. |
| Bảng SQL mới `Account_BotMetadata` | Tách nghiệp vụ bot khỏi xác thực/tính phí; phù hợp hướng A-02. Có thể thêm metadata theo nhân vật nếu cần. | Cần kiểm khóa/collation/schema, migration, cache và đồng bộ tới mọi GS; không query DB trên đường broadcast. | [ĐỀ XUẤT] Nguồn quản trị dài hạn; có thể xuất danh sách được duyệt cho GS, chỉ một nguồn có thẩm quyền. |
| `roledb` / chỉ mục hoặc DB metadata riêng phía Goddess | Gần dữ liệu nhân vật, hỗ trợ cờ theo nhân vật. | DB chính hiện lấy tên nhân vật làm khóa, giá trị blob; thêm DB phụ cần quản lý save/delete/rename/backup và truyền metadata. Không thể chỉ thêm một “cột is_bot” vào B-tree hiện hữu. | [NGUỒN] A-02: `Goddess/IDBRoleServer.cpp:65-74,798,876`; `Goddess/DBTable.cpp:107-128,199-218`. [ĐỀ XUẤT] Không chọn vòng đầu. |
| Trường “rảnh” trong `TRoleData.BaseInfo` hoặc nối byte vào blob | Có thể đi theo luồng nạp/lưu/chuyển GS sẵn có nếu thật sự có trường được dành riêng. | Chưa chứng minh trường nào rảnh; version/offset/layout dùng nhiều nơi. `iRoleParm6` là chuyển server, `isWaiGua` là khu vực; nhiều parm khác chứa thời gian/đổi tên/cấp. | [NGUỒN] `GS/Core/Src/KPlayerDBFuns.cpp:603-604,759-782`; `GS-lib/S3DBInterface.h:167-201`. [ĐỀ XUẤT] Loại khỏi phương án ít rủi ro. |
| File riêng `Settings/bots.ini` do GS nạp (tên đề xuất) | Không migration SQL/roledb/protocol; dễ hoàn tác danh sách, tra một lần rồi đọc RAM; chỉ cần thay đổi trong GS. | Phải quản lý quyền sửa, nhất quán phiên bản giữa GS; tên đổi/xóa/tái tạo cần cập nhật. File sai/thiếu không được âm thầm cấp quyền bot. | [ĐỀ XUẤT] Chọn vòng đầu cho B-01; cần triển khai loader mới, chưa có bằng chứng file này đang được hỗ trợ. |

[ĐỀ XUẤT] Chốt semantics: `is_bot` là danh tính thực thể do người vận hành chỉ định, khác quyền GM, loại VIP, autoplay và trạng thái offline. Mặc định chọn khóa đầy đủ `(khu vực, tài khoản, tên nhân vật)` để tránh đánh dấu toàn bộ tài khoản có nhân vật người thật. Nếu chủ dự án chỉ dùng tài khoản chuyên bot, có thể chọn cờ cấp tài khoản sau khi chốt riêng; không trộn hai quy tắc ưu tiên ngầm.

[NGUỒN] GS đã có tài khoản/tên ở `AddCharacter` (`GS/Core/Src/CoreServerShell.cpp:444-445`); khu vực được nạp vào `m_CurSerVer` từ `BaseInfo.isWaiGua` (`GS/Core/Src/KPlayerDBFuns.cpp:603`). [CHƯA KIỂM] Chuẩn hóa hoa/thường/encoding và phạm vi duy nhất của tên cần kiểm xuyên PaySys/Bishop/Goddess trước khi viết loader; không dùng hash tên làm khóa duy nhất. `KPlayerSet::Add` hiện dùng `g_FileName2Id(szPlayerID)` (`GS/Core/Src/KPlayerSet.cpp:508-511`), không chứng minh hash không va chạm.

## Luồng GS nạp nhân vật và chỗ chèn

| Bước | [NGUỒN] Hàm và bằng chứng | [ĐỀ XUẤT] Xử lý cờ |
|---|---|---|
| Khởi tạo GS | `KPlayerSet::Init`, khởi tạo slot và các bảng có sẵn: `GS/Core/Src/KPlayerSet.cpp:35-84,102`. | Nạp registry một lần trước khi nhận nhân vật; dùng loader riêng, không mượn danh sách GM. Chưa xác định thứ tự khởi động đầy đủ, cần rà trong task triển khai. |
| Nhận blob từ gateway | `KSwordOnLineSever::GatewayLargePackProcess`, lấy `tagGuidableInfo`, GUID và `TRoleData`, gọi `AddCharacter`: `GS/MultiServer/GameServer/KSOServer.cpp:3917,3940-3949,3972-3992`. | Không tin cờ do client gửi; lấy khóa từ dữ liệu đường gateway phía server. Cờ bot không thay thế xác thực/GUID. |
| Cấp slot, có danh tính | `CoreServerShell::AddCharacter`: `PlayerSet.Add`, kiểm index, chép account/name, blob và con trỏ load: `GS/Core/Src/CoreServerShell.cpp:423-453`. Slot lưu GUID và vào use-set: `GS/Core/Src/KPlayerSet.cpp:573-580`. | Sau khi slot hợp lệ và đã có account/name, reset false rồi resolve khóa từ `BaseInfo` qua registry RAM; gắn `KPlayer::m_bIsBot` server-only hoặc sidecar cùng vòng đời. Đây là điểm chính, sớm hơn NPC/map publication. |
| Client nối bằng GUID | `KSwordOnLineSever::ProcessLoginProtocol` gọi `AttachPlayer` bằng GUID: `GS/MultiServer/GameServer/KSOServer.cpp:5031,5072-5087`. | Giữ nguyên cờ đã resolve, không lấy lại từ packet client hay suy theo IP/net index. |
| Nạp DB từng bước | `SendGameDataToClient → PlayerDbLoading → KPlayer::LoadDBPlayerInfo → LoadPlayerBaseInfo`: `GS/MultiServer/GameServer/KSOServer.cpp:5115-5138`; `GS/Core/Src/CoreServerShell.cpp:496-509`; `GS/Core/Src/KPlayerDBFuns.cpp:174-198`. | Cờ đã sẵn trước bước này; không resolve muộn sau khi NPC đã tạo. |
| Tạo và liên kết NPC | `LoadPlayerBaseInfo` tạo NPC ở 548, gán `kind_player`, `SetPlayerIdx(m_nPlayerIndex)` ở 576-579; account còn dùng để kiểm GM ở 591-594: `GS/Core/Src/KPlayerDBFuns.cpp`. | Giữ một nguồn cờ trong KPlayer, KNpc truy ngược qua `GetPlayerIdx()`; không cần thêm bản sao IsBot trong KNpc. |
| Vào thế giới | `enumPlayerSyncEnd` nhận sync reply rồi `AddPlayerToWorld`: `GS/MultiServer/GameServer/KSOServer.cpp:3768-3772`; shell gọi `LaunchPlayer`: `GS/Core/Src/CoreServerShell.cpp:514-517`. | Không chờ tới Lua login/LaunchPlayer mới đánh dấu; có thể quá muộn cho đồng bộ trước đó. |
| Chuyển GS | Có call `AddCharacter` ở nhánh trao đổi: `GS/MultiServer/GameServer/KSOServer.cpp:3168`; tham số `isExTrans` và nhánh tương ứng ở `GS/Core/Src/CoreServerShell.cpp:423-424,474-478`. | Resolve lại trên GS đích bằng cùng registry/version, không cần truyền cờ trong blob. [CHƯA KIỂM] Cần đọc đầy đủ các nhánh exchange và chính sách lệch phiên bản trước triển khai. |

## Bảo toàn định dạng lưu và vòng đời

[NGUỒN] Header GS dùng `#pragma pack(push, 1)` (`GS-lib/S3DBInterface.h:15`), `TRoleData` có các offset task/skill/item/friend và `dwDataLen` (`:184-201`). `KPlayer::Save` zero buffer rồi gọi `UpdateDBPlayerInfo` (`GS/Core/Src/KPlayer.cpp:917-947`); hàm cập nhật gọi lần lượt các serializer, không ghi nguyên đối tượng KPlayer (`GS/Core/Src/KPlayerDBFuns.cpp:410-434`). A-02 ghi Goddess từ chối blob dài **từ 128 KiB trở lên**, không phải cho phép ghi tùy ý hết buffer (`Goddess/IDBRoleServer.cpp:591-607`).

[ĐỀ XUẤT] Chỉ thêm trạng thái RAM phía server; không đổi `TRoleData`, `BaseInfo`, pack, version, offset, `dwDataLen`, buffer, serializer hoặc packet. Nếu thêm member vào `KPlayer`, phải build đồng bộ mọi module dùng layout của lớp; đây không phải khẳng định tương thích ABI với DLL cũ. Sidecar theo player slot là phương án tránh đổi layout nếu task triển khai phát hiện ràng buộc ABI, nhưng phải có generation/danh tính để chống cờ sót khi slot tái sử dụng.

[NGUỒN] Constructor gọi `Release`, hàm này reset trạng thái (`GS/Core/Src/KPlayer.cpp:85-104,139`); `RemoveInGame` xóa NPC rồi gọi `Release` trước trả slot (`GS/Core/Src/KPlayerSet.cpp:1095-1123`). Nhánh timeout gọi `LoginTimeOut` (`:1170-1195`), và `LoginTimeOut` gọi `Release` (`GS/Core/Src/KPlayer.cpp:907-914`).

[ĐỀ XUẤT] Reset false ở khởi tạo/Release và trước mỗi lần gán danh tính trong AddCharacter, cả khi lookup không trúng. Rà thêm quit/exchange/load failure để không giữ cờ của nhân vật trước. Mất kết nối đơn thuần không đồng nghĩa xóa danh tính bot: phân biệt “IsBot” với “connected/active/targetable”. Với bot Dormant chưa có slot, helper không tạo thực thể hoặc tự đăng nhập; bot chung của B-01 vẫn là một NPC/player server có trạng thái gameplay chung.

## Hợp đồng IsBotPlayer cho B-01

[ĐỀ XUẤT] `IsBotPlayer(playerIdx)` là helper server chỉ đọc: index trong `(0, MAX_PLAYER)`, slot còn thuộc nhân vật hợp lệ, trả cờ RAM của slot. Với call từ NPC, kiểm NPC hợp lệ, `kind_player`, lấy `GetPlayerIdx()` và kiểm liên kết ngược `Player[playerIdx].m_nIndex == npcIdx` trước gọi helper. `m_nIndex` của KPlayer là NPC index, không phải player index (`GS/Core/Src/KPlayerDBFuns.cpp:548,576-579`); member NPC chứa player index (`GS/Core/Src/KNpc.h:882`), getter khai báo tại `:1184`.

[ĐỀ XUẤT] Không gộp `m_nNetConnectIdx >= 0` vào định nghĩa danh tính bot; caller kiểm kết nối/mục tiêu tùy việc. Không đọc file/SQL, không so chuỗi, không chạy Lua tại mỗi broadcast. Lua `IsBotPlayer(playerIdx)` chỉ là wrapper đọc của cùng helper, không cung cấp setter để client/script thường tự nhận bot. Phân loại NPC thường/quái và hảo hữu theo thứ tự policy B-01, không gọi helper với NPC index.

[NGUỒN] B-01 mục 2/4/7 yêu cầu Bot chung, API IsBotPlayer và đọc cờ trong bộ nhớ; A-05 mục “Đồng bộ thực thể” ghi broadcast đã có lọc connection nhưng các đường direct khác nhau. [ĐỀ XUẤT] `IsBot=true` chỉ phân loại cho visibility/interaction, không tự bỏ qua PK, trade, quyền truy cập, khoảng cách hay các kiểm tra gameplay gốc.

[ĐỀ XUẤT] Registry chỉ nạp lúc khởi động trong vòng đầu; bản thiếu/sai bị từ chối dùng để bật visibility, hoặc giữ công tắc B-01 tắt và báo lỗi đã lọc danh tính. Không tự coi mọi nhân vật là bot khi file lỗi. Nếu hỗ trợ reload sau này, cần snapshot nhất quán, cập nhật slot trong tick an toàn và gọi refresh REMOVE/ADD theo B-01 mục 6; không thay cờ nóng giữa lúc broadcast mà không làm mới hiển thị. Nhiều GS phải dùng cùng bản registry trước khi cho chuyển GS.

## Việc tiếp theo có thứ tự

1. [ĐỀ XUẤT] Chốt cờ theo tài khoản hay nhân vật, khóa khu vực và quy tắc đổi tên/xóa/tái tạo; mặc định vòng đầu dùng khóa ba thành phần, không có account wildcard.
2. [ĐỀ XUẤT] Trên bản copy source được duyệt riêng, xác minh ABI/module và thứ tự init; thêm registry loader, cờ server-only hoặc sidecar; gắn ở AddCharacter, reset đủ mọi đường trả slot. Giữ nguyên blob/protocol/schema.
3. [ĐỀ XUẤT] Thêm helper C++ và wrapper Lua chỉ đọc; tích hợp B-01 sau kiểm index/liên kết hai chiều; không sửa GetRelation toàn cục. Chốt xử lý file lỗi trước khi bật công tắc.
4. [ĐỀ XUẤT] Khi được phép build/test: dùng dữ liệu giả kiểm bot/người cùng tài khoản, lookup không trúng, file lỗi/trùng khóa, slot tái dùng bot→người, timeout/load failure/relogin, chuyển GS; đối chiếu blob round-trip về layout/offset/độ dài (không yêu cầu byte bằng nhau ở trường thời gian vốn thay đổi). Chạy bộ B-01/B-03 với hai người và một bot, kiểm bot chết chung, REMOVE/ADD, công tắc tắt.
5. [ĐỀ XUẤT] Khi cần quản trị tập trung, làm task metadata SQL theo A-02; kiểm schema/collation và cơ chế xuất registry có phiên bản. Không đồng thời cho file và DB tự quyết trái nhau; chuyển nguồn có thẩm quyền bằng quy trình riêng.

## Giới hạn, kiểm chứng và lỗi thao tác

- [CHƯA KIỂM] Chưa build/test/runtime, chưa đối chiếu binary gs001 với source, schema SQL thực, cấu hình đường dẫn/encoding loader, thứ tự init đầy đủ và mọi nhánh chuyển GS. Đây là thiết kế ít thay đổi bề mặt dữ liệu, chưa phải kết quả nghiệm thu vận hành.
- [NGUỒN] Chỉ đọc mã/tài liệu và kiểm Git local; không kết nối mạng/VM/SQL, không chạy exe. Không có thay đổi canonical hay dữ liệu thật.
- [NGUỒN] `rg` không có trong PATH; dùng `Select-String` và đọc dòng PowerShell. Đường thử ban đầu `jxOnline\Sources\Core\Src\KPlayer.cpp` không tồn tại; đã dùng đúng gốc `gameserver\Sources` được A-05 ghi. Lượt đọc đầu bị console giải mã sai dấu, đã đọc UTF-8; đầu ra hai báo cáo gộp bị cắt, đã đọc bổ sung phần cần thiết. Không còn blocker khảo sát từ các lỗi này.
- [NGUỒN] Khảo sát DONE; **BỊ CHẶN – CHƯA PUSH** ở Git: lệnh stage đúng hai file thất bại một lần với `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/C-02/index.lock': Permission denied`. Không đổi quyền/config hay retry; chưa có commit SHA. PM commit hai file local được giao. Đã chạy `git diff --check` không lỗi khoảng trắng; `git diff --no-index` cho file mới trả 1 vì có khác biệt và đầu ra console bị cắt, không phải lỗi Git. Không push theo ràng buộc cấm mạng.
