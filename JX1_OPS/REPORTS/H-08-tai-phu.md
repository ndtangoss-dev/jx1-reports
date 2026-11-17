TÓM TẮT 5 DÒNG
1. [NGUỒN] Nhánh DB backup tính giàu có bằng `iservermon + isavemoney`, xếp Xu riêng; chưa thấy công thức cộng tài phú từ trang bị.
2. [NGUỒN] Bảng tiền trong nhánh này có 10 người và 11 nhóm môn phái; comment nói 100 không khớp hằng số hiện có.
3. [NGUỒN] `FortuneRank` trong client chọn sprite theo loại phi phong, không đủ bằng chứng coi là điểm tài phú.
4. [NGUỒN] Đã lần theo DB → thống kê → cache gameserver → gói ladder → UI Coco; có bất nhất chỉ số môn phái và nhánh Xu cần TESTER kiểm tra.
5. [CHƯA BIẾT] Chưa xác minh runtime, dữ liệu trong PAK và tính tương ứng với binary; không dùng mạng/VM, không chạy game/server.

# H-08 — Khảo sát tĩnh hệ tài phú

- Ngày: 2026-11-17. Trạng thái: DONE — hoàn tất khảo sát tĩnh, các giới hạn xác minh ghi riêng bên dưới.
- Worktree `D:\JX-wt\H-08`, nhánh `task/H-08`, khớp task; task có trong `JX1_OPS/TASKS/BACKLOG.md:89`.
- Chỉ ghi báo cáo này và mục `## Kết quả` mà task yêu cầu ở cuối `JX1_OPS/TASKS/H-08.md`; không sửa mã/config.
- Bước tiếp theo cho PM/TESTER: kiểm tra các ca H08-T01…T12 trong môi trường thử được phê duyệt; không coi báo cáo là kết quả runtime.

## ĐÃ XÁC MINH

### Quy ước nguồn

- `S/` = `D:\JX-source\server\jxOnline/`.
- `C/` = `D:\JX-source\client\Classes/`.
- `O/` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client/` (bản Coco tại máy, không khẳng định là upstream nguyên thủy).
- `P/` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_/`.
- `[NGUỒN]` chỉ là xác minh mã/tài nguyên tĩnh, không xác nhận server đang chạy đúng mã này.

### 1. Định nghĩa và cách tăng/giảm

[NGUỒN] Có ba dấu vết khác nhau, cần giữ riêng khi thiết kế gameplay:

| Dấu vết | Giá trị/đầu vào thực tế thấy trong nguồn | Kết luận trong phạm vi đọc |
|---|---|---|
| Giàu có / `MoneyStat`, `TopTenRich` | Tiền mang theo + tiền trong rương | Có công thức và đường truyền bảng hạng |
| `[FortuneRank]` | `m_PifengType`, dùng chọn đường sprite | Là nhánh vẽ tên/hiệu ứng phi phong; chưa thấy tính điểm từ tổng tiền |
| `G_ITEM_FORTUNE_VALUE` | Chuỗi “兵甲财富值:<c=green>%d<c>” | Có nhãn giá trị tài phú trang bị; chưa tìm được nơi tính/gọi nhãn này trong source đã khảo sát |

Công thức có đường gọi từ Goddess là `Money = BaseInfo.iservermon + BaseInfo.isavemoney`; Xu riêng là `BaseInfo.iclientx`. Bằng chứng: `S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:130` (`RoleDataCopy`), `:135`, `:139`, `:509`. Hàm `KItemList::GetMoneyAmount` cũng cộng tiền ở `room_equipment` và `room_repository`: `S/gameserver/Sources/Core/Src/KItemList.cpp:3368`.

[NGUỒN] Đường tăng/giảm tiền đã xác định:

- `KPlayer::Earn` từ chối số âm rồi gọi `AddmServer(room_equipment, nMoney)` (`S/gameserver/Sources/Core/Src/KPlayer.cpp:7381`); `KItemList::AddmServer` thêm tiền và gọi đồng bộ (`S/gameserver/Sources/Core/Src/KItemList.cpp:3391`). Nhặt tiền gọi `Earn` tại `S/gameserver/Sources/Core/Src/KPlayer.cpp:5890`.
- Lua `Earn` đăng ký ở `S/gameserver/Sources/Core/Src/ScriptFuns.cpp:26338`, handler ở `:20181` nhận số dương và gọi `Player.Earn`. Đây là API tăng tiền, chưa kiểm kê mọi script thưởng nhiệm vụ/sự kiện.
- `KPlayer::Pay` gọi `CostMoney` (`S/gameserver/Sources/Core/Src/KPlayer.cpp:7334`); `CostMoney` chỉ kiểm tra và trừ tiền mang theo (`S/gameserver/Sources/Core/Src/KItemList.cpp:3421`). Có tiền trong rương không đồng nghĩa lệnh này tự rút từ rương.
- Gửi/rút giữa túi và rương chuyển cùng lượng và hoàn lại nguồn nếu đích không nhận được (`S/gameserver/Sources/Core/Src/KItemList.cpp:3329`). [SUY LUẬN TỪ NGUỒN] Nếu chuyển thành công giữa hai nơi này, tổng dùng xếp hạng không đổi; nhận thêm tiền tăng tổng, chi tiền giảm tổng. Bảng hạng còn phụ thuộc thời điểm lưu nhân vật/thống kê/cache.

Không tìm được công thức cộng tài phú theo giá bán, cấp cường hóa, phẩm chất trang bị, mặt nạ, trang sức hay phi phong trong các đường trên. Đây là giới hạn của kết quả tìm kiếm, không phải khẳng định toàn bộ gói game không có hệ đó. Nhãn tài phú trang bị có tại `P/gs/Settings/lang/zh/stringtable_core.txt:1107` và `P/gs/Settings/lang/vn/stringtable_core.txt:1079`.

### 2. Bảng số liệu và quy tắc xếp hạng

| Hạng mục | Giá trị trong nguồn | Bằng chứng |
|---|---:|---|
| Top tiền toàn thế giới (`CDBBackup`) | 10 | `S/gateway/Sources/MultiServer/Goddess/DBBackup.h:16`, `:39` |
| Top Xu toàn thế giới | 10 | Cùng file `:41`, dùng `MONEYSTATNUM` |
| Số nhóm môn phái trong cấu trúc | 11 | Cùng file `:19`, `:42` |
| Số người mỗi nhóm | 10 | Cùng file `:18` |
| Mỗi kết quả ladder gửi client | 10 bản ghi | `S/gameserver/Headers/KProtocol.h:2535` |
| Dữ liệu một người gửi trên mạng | `Name[20]`, `int nValue`, `BYTE bySort` | Cùng file `:2481` |
| Cờ biến động hạng | 1 lên/mới; 255 xuống; 0 giữ | `S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:734` |
| Giá trị mặc định hiển thị phi phong | `count=11`, `nTime=20` | `C/gamescene/KgameWorld.cpp:11240`; là mặc định đọc INI, không phải 11 mốc tài phú đã xác minh |
| Ngưỡng hạn chế query tại UI | `GET_RANK_TIME_OUT=10000` | `C/gameui/KuiCometoMap.h:25`, điều kiện `C/gameui/KuiCometoMap.cpp:1414`; chưa quy đổi đơn vị thời gian runtime |

`GetMin` chọn ô trống trước hoặc người có tiền nhỏ nhất (`S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:47`); chỉ thay nếu tiền mới lớn hơn, dùng so sánh `<` ở `:510`. `ListSort` sắp giảm dần theo tiền, dùng so sánh `>` (`:93`, `:124`, gọi tại `:680`). Không thấy quy tắc phụ theo tên/thời gian cho người bằng tiền; không bảo đảm thứ tự đồng hạng ổn định giữa các lần duyệt DB. Người có tổng 0 không vượt được ngưỡng 0 của ô trống.

| ID ladder theo enum hiện có | Ý nghĩa | Đường trả dữ liệu |
|---|---|---|
| 2 | Tiền thế giới | `MoneyStat` |
| 4 | Xu thế giới | `XuStat` |
| 16 | Tiền nhóm không môn phái | `TopTenFacRich(-1)` → nhóm 0 |
| 17…26 | Tiền các môn phái 0…9 | `TopTenFacRich(0…9)` → nhóm 1…10 |
| 27…37 | Enum dành Xu môn phái | Hàm hiện có vẫn rơi vào nhánh `TopTenFacRich`, tham số 10…20, bị guard từ chối |

Bằng chứng enum: `S/gameserver/Sources/Core/Src/KLadder.h:7`, `:11`, `:17`; getter và guard: `S/gameserver/Sources/Core/Src/KLadder.cpp:39`, `:95`, `:113`, `:121`. Bản Coco dùng cùng cách rẽ nhánh (`C/gamecore/KLadder.cpp:89`). Không suy ra các ID này đều được menu UI công khai; cần file ánh xạ INI.

Ví dụ số liệu giả lập dưới đây chỉ minh họa phép cộng, **không phải test đã chạy hoặc dữ liệu nhân vật thật**:

| Ca | Tiền mang theo | Tiền rương | Xu | Giá trị bảng tiền suy ra | Giải thích |
|---|---:|---:|---:|---:|---|
| A | 1.000 | 2.000 | 0 | 3.000 | Tổng hai nơi |
| A sau gửi 500 vào rương | 500 | 2.500 | 0 | 3.000 | Chuyển nội bộ không tăng tài sản |
| A sau nhận thêm 200 | 700 | 2.500 | 0 | 3.200 | Tăng tiền mang theo |
| B | 100 | 100 | 999.999 | 200 | Xu không cộng vào bảng tiền |
| C | 0 | 0 | 100 | 0 | Có thể không được đưa vào top tiền do so sánh nghiêm ngặt |

### 3. Lưu DB và chu kỳ cập nhật

[NGUỒN] `S/gameserver/Lib/S3DBInterface.h:107` định nghĩa `isavemoney`, `:108` `iservermon`, `:109` `iclientx`, đều là `int`. Khi nạp nhân vật, `KPlayerDBFuns` lấy Xu và tiền túi/rương vào `m_ItemList` (`S/gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:686`, `:693`, `:701`). Khi ghi nhân vật, lấy hai room và Xu rồi ghi lại ba trường trên (`:1522`). Không cần cột `wealth` riêng để tạo `MoneyStat` trong nhánh đã lần.

Lớp `ZDBTable` dùng API Berkeley DB/B-tree (`S/gateway/Sources/MultiServer/Goddess/DBTable.cpp:107`, `:110`); `add` ghi khóa tên nhân vật và blob dữ liệu qua `primary_db->put(..., DB_AUTO_COMMIT)` (`:199`, `:208`, `:218`). `StartBackupTimer` tạo `CDBBackup("database", "roledb", db_table)` (`S/gateway/Sources/MultiServer/Goddess/IDBRoleServer.cpp:1648`). Đây là bằng chứng lưu role trong nguồn, không khẳng định schema SQL hoặc DB hiện đang chạy.

Thống kê được tạo khi `CDBBackup::Backup` duyệt role; lọc một số tên trước khi đưa vào top (`S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:495`), tính tiền ở `:509`, tính Xu riêng ở `:503`, sắp xếp tại `:680`. Snapshot thứ hạng đọc/ghi `StatData.dat` (`:702`, `:705`, `:830`, `:834`); `MakeSendStatData` chuyển Money thành `nValue` và Sort thành `bySort` (`:923`, `:935`). Không đọc file DB hoặc `StatData.dat` thực tế trong task này.

Lúc mở, `Open(aTime)` lấy `aTime % 24`, tạo timer rồi đọc `StatData.dat` và tạo cache gửi (`S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:198`, `:222`, `:233`). Timer kiểm tra giờ local bằng `BackupTime`, ngủ 30 phút giữa vòng (`:307`, `:314`, `:324`); còn có đường backup thủ công (`:285`, `:331`). Đây không phải bằng chứng rằng bảng tiền cập nhật mỗi 30 phút: timer chỉ thực hiện backup trong giờ cấu hình. Gameserver có đường yêu cầu lại thống kê ở timer case 8 (`S/gameserver/Sources/MultiServer/GameServer/KSOServer.cpp:5579`); chưa xác minh lịch gọi case đó hoặc cấu hình giờ thực tế.

Một nhánh khác là `TGameStatistic`: `S/gateway/Sources/MultiServer/Goddess/GameStatistic.cpp:80` dùng **`imoney + isavemoney`**, `:103` giữ 100 người. Header `S/gameserver/Headers/S3DBInterface.h:50` cũng còn `imoney`, khác bản `Lib/`. Đường `GetGameStat` đã theo thực tế gọi `DBBackup->GetSendStatData` (`S/gateway/Sources/MultiServer/Goddess/IDBRoleServer.cpp:1707`), vì vậy không dùng nhánh 100 người để kết luận nhánh DB backup. Chưa build để chốt include paths và mã nào được đưa vào binary.

### 4. Gói tin và đường tới UI

| Chặng | Symbol/gói tin | Bằng chứng |
|---|---|---|
| Gameserver xin thống kê từ Goddess | `c2s_gamestatistic` | `S/gameserver/Sources/MultiServer/GameServer/KSOServer.cpp:5585` |
| Goddess lấy cache trả gói lớn | `CClientNode::_GetGameStat`, `s2c_gamestatistic`, `s2c_gamestatistic_bigpackage` | `S/gateway/Sources/MultiServer/Goddess/ClientNode.cpp:754`, `:772`, `:778`, `:784` |
| Gameserver kiểm tra kích thước và nạp bảng | `SetLadder` → `Ladder.Init` | `S/gameserver/Sources/MultiServer/GameServer/KSOServer.cpp:2997`, `:3002`; `S/gameserver/Sources/Core/Src/CoreServerShell.cpp:3199` |
| UI xin bảng cụ thể | `GOI_QUERY_RANK_INFORMATION` → `SendClientCmdQueryLadder` | `C/gameui/KuiCometoMap.cpp:1412`; `C/gamecore/CoreShell.cpp:3010` |
| Client gửi query ID | `LADDER_QUERY`, `c2s_ladderquery` | `C/gamecore/KProtocol.cpp:769` |
| Server trả 10 người | `LadderQuery` → `Ladder.GetTopTen` → `LADDER_DATA`, `s2c_ladderresult` | `S/gameserver/Sources/Core/Src/KProtocolProcess.cpp:6241`, `:6253`, `:6265` |
| Client chuyển từng dòng sang UI | `LadderResult`, `KRankMessage`, `GDCNII_RANK_INFORMATION_ARRIVE` | `C/gamecore/KProtocolProcess.cpp:5352`, `:5364`, `:5370` |
| UI nhận và hiển thị | `NewRankArrive` → `KuiCometoMap::NewRankArrive`, `AddRank`, cache tạm | `C/gameui/GameSpaceChangedNotify.cpp:49`; `C/gamescene/KgameWorld.cpp:11193`; `C/gameui/KuiCometoMap.cpp:1001` |

`TRoleList` chỉ có tên, giá trị, cờ biến động; `TGAME_STAT_DATA` chứa bảng tiền/Xu/thống kê môn phái (`S/gameserver/Headers/KProtocol.h:2481`, `:2488`). `LADDER_QUERY` chỉ mang ID (`:2565`); `LADDER_DATA` còn có các trường mở rộng phục vụ nội dung khác (`:2531`). Chưa đo byte size, packing hay opcode của binary, không đưa số byte ước đoán làm đặc tả giao thức.

`LuaShowLadder` có thể gửi danh sách ID bằng `s2c_ladderlist` (`S/gameserver/Sources/Core/Src/ScriptFuns.cpp:23516`); client nhận thành `KRankIndex` (`C/gamecore/KProtocolProcess.cpp:5331`). Không xác minh script đang gọi hàm này. UI còn tự đọc danh sách mặc định từ `\\update10\\Ui\\排名ID.ini` (`C/gameui/KuiCometoMap.cpp:36`, `:961`), lấy `ID` từng mục (`:983`). Cache UI là `index_and_rank_datatmp.ini` (`:35`), giá trị hiển thị được nối từ `nValueAppend` cùng đơn vị nếu có (`:2088`, `:2092`, `:2119`). Tên mục giàu có/đơn vị thật phụ thuộc INI chưa có bản rời được tìm thấy; không coi source là ảnh chụp UI chạy thật.

Tiền thường được đồng bộ riêng với bảng hạng: `SendMoneySync` dùng `s2c_syncmonfs`, mang tiền túi/rương/giao dịch (`S/gameserver/Sources/Core/Src/KItemList.cpp:3522`); Xu dùng `s2c_syncqianfs` (`:3532`). Vì vậy thấy tiền trên UI thay đổi ngay chưa chứng minh bảng hạng đã được tính lại.

### 5. Gameplay, trang bị, phi phong và đối chiếu Coco

[NGUỒN] Phần xếp hạng đã lần chỉ đọc tiền/role, tạo cache và gửi UI; chưa thấy nó cộng chỉ số chiến đấu, khóa mặc trang bị, cấp danh hiệu hoặc phát phần thưởng. Không có căn cứ đặt mốc “đủ X tài phú thì được phi phong cấp Y”.

Đường ngoại hình phi phong đi từ trang bị: `S/gameserver/Sources/Core/Src/KItemList.cpp:1673` ưu tiên `GetItemResIdx`; nếu không có thì dùng GoldId/cấp hoặc `GetPifengRes`. Cấp trên 10 dùng `%10` (`:1690`, `:1699`). NPC đồng bộ `PifengType` (`S/gameserver/Sources/Core/Src/KNpc.cpp:8030`, `:8382`); client nhận ở `C/gamecore/KProtocolProcess.cpp:2989`, `:3129`. Coco gọi vẽ khi `m_PifengType > 0` (`C/gamescene/KgameWorld.cpp:9896`). Đây là quan hệ trang bị → ngoại hình, chưa phải tài phú → trang bị.

| Điểm đối chiếu | Bản Coco `O/Classes/` | Bản `C/` / nguồn server | Kết luận tĩnh |
|---|---|---|---|
| Bảng tiền/getter/enum | `gamecore/KLadder.cpp`, `.h` | Cùng file phía `C/` giống byte | Giữ cùng cấu trúc và cả nhánh Xu chưa tách |
| Cấu trúc packet | `gamecore/KProtocol.h` | Cùng file phía `C/` giống byte | Đồng nhất file client, chưa kết luận mọi header server tương thích |
| Hàm gửi query | `gamecore/KProtocol.cpp`, `SendClientCmdQueryLadder` | Vùng hàm giống byte dù cả file khác | Không suy diễn thay đổi giao thức từ khác biệt toàn file |
| Hàm nhận kết quả | `gamecore/KProtocolProcess.cpp:5328` | `C/gamecore/KProtocolProcess.cpp:5352`, vùng hàm giống byte | Đều đưa 10 dòng về UI |
| Chuyển kết quả qua scene | `gamescene/KgameWorld.cpp:11112` | `C/gamescene/KgameWorld.cpp:11193`, vùng hàm giống byte | Cùng chuyển tới cửa sổ `OBJ_NODE_MOVEMAP` |
| UI danh sách hạng | `gameui/KuiCometoMap.cpp`, `GameSpaceChangedNotify.cpp` | Hai file phía `C/` giống byte | Có đường UI, chưa chạy thực tế |
| Vẽ phi phong | `gamescene/KgameWorld.cpp:11137` trả sprite sẵn có ngay | `C/gamescene/KgameWorld.cpp:11224` so sánh loại đã lưu, thay sprite khi đổi loại; lưu loại tại `:11253` | Coco tại máy có thể giữ sprite cũ khi đổi loại trong nhánh này; bản D-source có xử lý khác, chưa test |
| Khóa INI phi phong | `O/Classes/gamescene/KgameWorld.cpp:11156` dùng số `%d` | `C/gamescene/KgameWorld.cpp:11245` cũng dùng `%d`; lõi cũ `S/gameserver/Sources/Core/Src/KNpc.cpp:16694` dùng `Spr_%d` | Cần đúng INI cho đường renderer; chưa có giá trị thật để xác nhận |

Bản đối chiếu là **Coco hiện có trên đĩa**, không phải khẳng định bản phát hành gốc chưa sửa. Kiểm tra byte/SHA-256 chỉ trên file liên quan, không chạy binary:

| File giống byte giữa `O/Classes/` và `C/` | SHA-256 chung |
|---|---|
| `gamecore/KLadder.cpp` | `4085cbe711657e719b961f47f71a7efec48c4c4f39d6645dd1952d60833e63b4` |
| `gamecore/KLadder.h` | `e381f2078aa717ccf32b707f40d0fc4e9b4414dc02f20857d8739d303cd01b21` |
| `gamecore/KProtocol.h` | `1152e31d022ec8d78931fa3285f717bc553fe7727c6c0961ddc3214bb77ca084` |
| `gamecore/KItemList.cpp` | `82fd49a0f14b426e78bf1bff5b157a05ff56c9c0bf97b7c6da76a7f16fb5d3ba` |
| `gameui/KuiCometoMap.cpp` | `66d5751748c6f624314c44f1d9fdf9658222ee5a331160a6092a5745e2541722` |
| `gameui/GameSpaceChangedNotify.cpp` | `ea40b802fb200b1abb9d8089872f483fd5a9e9362e15db45e86f4e0355bb5323` |

### 6. Bất nhất có bằng chứng, chưa sửa mã

| Điểm | Bằng chứng | Ảnh hưởng cần kiểm tra |
|---|---|---|
| Chỉ số môn phái trong DB backup | `S/gateway/Sources/MultiServer/Goddess/DBBackup.cpp:530` chấp nhận `nSect=1…10`, `:532` ghi `[nSect+1]`; mảng chỉ 11 nhóm (`DBBackup.h:19`). Nhóm 0 bị đưa vào nhánh mặc định `:536`. Role lưu trực tiếp `m_nCurFaction` (`S/gameserver/Sources/Core/Src/KPlayerDBFuns.cpp:1439`). | Với `nSect=10`, truy cập nhóm 11 vượt biên 0…10; cùng mẫu còn ở Xu (`DBBackup.cpp:545`) và tỷ lệ (`:650`). Với `nSect=0`, đi nhóm không môn phái. Chưa tái hiện crash hoặc dữ liệu sai trên binary. |
| Xu môn phái chưa tách nhánh | Enum có dải Xu nhưng `KLadder::GetTopTen` chỉ có nhánh cuối gọi `TopTenFacRich` (`S/gameserver/Sources/Core/Src/KLadder.cpp:121`); client giống logic. | ID 27…37 không có kết quả do guard của getter; không được coi đây là 11 bảng Xu hoạt động. |
| Tổng tiền dùng `int` | Trường role `S/gameserver/Lib/S3DBInterface.h:107`; phép cộng trước khi gán `Money` ở `DBBackup.cpp:135`, phép chọn top `:510`. | Nếu tổng vượt giới hạn `int` 32-bit, có nguy cơ tràn số có dấu; chưa xác minh giới hạn tiền của room hoặc compiler/binary. Không coi ví dụ vượt giới hạn là giá trị hợp lệ để ghi DB. |
| Comment/cấu trúc lịch sử không thống nhất | `DBBackup.h:16` là 10; comment còn nói 100 (`DBBackup.cpp:647`, `KProtocol.h:2503`); `GameStatistic.cpp:103` thật sự dùng 100 và tên trường khác. | Phải chốt đường build trước khi dùng số 100 hoặc `imoney` vào đặc tả. |

## CHƯA XÁC MINH

- Chưa chạy build/test/runtime, chưa mở VM/kết nối mạng; không đọc DB, dump hoặc log người chơi. Không có kết quả PASS runtime.
- Chưa xác định điểm tài phú trang bị, hệ số cường hóa, mốc đổi phi phong, điều kiện mặc hay phần thưởng hạng. Không suy ra từ nhãn ngôn ngữ hoặc tên `FortuneRank`.
- Đã tìm các tên/symbol `wealth`, `fortune`, `caifu`, `rich/richer`, `财富/財富` trong source C/C++/header và các text/script cần thiết; tìm nhánh tiền bằng `MoneyStat`, nhánh trang bị bằng `Pifeng`. Không có nơi gọi `G_ITEM_FORTUNE_VALUE` trong source đã tìm. Tìm text không loại trừ tên khác hoặc logic nằm trong PAK/binary.
- Quét text rời dưới `P/gs/script` không thấy từ tài phú theo mẫu trên; `P/gs/Settings` chỉ thấy nhãn/ngôn ngữ liên quan. Không mở dữ liệu tài khoản, dump/log, không giải nén PAK hoặc chạy công cụ kèm gói.
- Không tìm được `npcbobo.ini` và `排名ID.ini` dạng rời dưới `O/Resources`, `O/data`; chưa đọc tài nguyên đóng gói để chốt sprite, tên bảng, đơn vị, ngưỡng thật.
- Chưa khẳng định chu kỳ cập nhật thật, thứ hạng đang chạy, UI giàu có hiển thị được, compiler/include được dùng hoặc binary khớp source. Chưa xác minh các lỗi source nêu trên có hiện diện trong server đang dùng.

## Ca test cho TESTER — CHƯA CHẠY

Chỉ thực hiện sau khi PM cho phép môi trường thử và dữ liệu giả. Ghi build/hash, tiền trước/sau, mốc lưu role, mốc thống kê, ID bảng và ảnh UI; không dùng nhân vật thật. Với ca biên nguy hiểm, ưu tiên unit harness trên dữ liệu giả thay vì ghi DB hoặc chạy server thật.

| ID | Thiết lập/thao tác | Kết quả cần kiểm tra |
|---|---|---|
| H08-T01 | A có túi 1.000/rương 2.000; B có 2.500/0. Lưu role, tính lại thống kê, tải cache, query ID 2. | A có `nValue=3000`, trên B `2500`; phân biệt tiền ngay lúc chơi với snapshot hạng. |
| H08-T02 | A gửi 500 vào rương rồi rút lại; tính hạng theo cùng chuỗi cập nhật. | Tiền hai nơi đổi, tổng hạng vẫn 3.000 nếu không có phí/thay đổi khác. |
| H08-T03 | A nhận thêm 200 bằng đường thưởng đã có; sau đó chi 100. | Tổng lần lượt 3.200 và 3.100 sau khi save/stat/cache cập nhật; UI tiền riêng đổi đúng. |
| H08-T04 | Hai người cùng tổng tiền, Xu khác nhau; query ID 2 và 4. | Bảng tiền không lấy Xu; bảng Xu dùng `iclientx`. Ghi cách hệ thực xử lý đồng hạng, không mặc định ổn định. |
| H08-T05 | Có 12 role giả với tổng tăng dần; thêm role tổng 0 và đồng hạng vị trí 10. | Top tiền chỉ 10 dòng theo nhánh CDBBackup; xác định xử lý ô trống/0/đồng hạng, cờ lên/xuống/giữ khi chạy thống kê lần hai. |
| H08-T06 | Harness tạo role có `nSect` lần lượt -1/255, 0, 1, 9, 10; bật kiểm tra biên bộ nhớ. | Đối chiếu nhóm 0…10; ca 10 phải phát hiện truy cập nhóm 11 ở nguồn hiện có. Không chạy ca gây hỏng bộ nhớ trên dịch vụ. |
| H08-T07 | Query ID 16…26 và 27…37 trong harness/VM thử được duyệt. | Tiền trả đúng nhóm; dải Xu cho thấy thiếu nhánh/không phản hồi ở nguồn hiện tại; chưa coi là test PASS chức năng. |
| H08-T08 | So sánh ngay sau Earn, sau lưu role, sau backup, sau refresh cache; khởi động lại môi trường thử khi được duyệt. | Xác định độ trễ thật, vai trò `StatData.dat`, giữ/đổi thứ hạng; không dùng timer 30 phút làm SLA. |
| H08-T09 | Mặc/tháo hoặc cường hóa đồ, giữ tiền không đổi bằng fixture; đối chiếu có/không phi phong. | Theo đường đã thấy, bảng tiền không cộng giá trị đồ; nếu runtime có tài phú trang bị khác, ghi rõ UI/field/nguồn cấu hình để mở rộng khảo sát. |
| H08-T10 | Mở trang hạng, chọn ID 2, đóng/mở lại để kiểm tra cache UI và đơn vị từ INI. | 10 dòng về `KuiCometoMap`, đúng tên/giá trị; xác định menu thật, lỗi INI thiếu, dữ liệu tạm cũ và giới hạn query. |
| H08-T11 | Đổi phi phong A→B ngay trong scene trên cả Coco và D-source; thử không có sprite; so khóa số với `Spr_%d` đúng renderer. | Xác minh sprite có đổi ngay không, tên có bị giữ cũ không; không gán mặc định `count=11` thành ngưỡng điểm. |
| H08-T12 | Harness kiểm tra phép tổng tiền gần `INT_MAX`, role không hợp lệ và packet đúng/sai kích thước. | Phát hiện tràn/giới hạn thực, từ chối hoặc xử lý dữ liệu lỗi; chốt packing/kích thước bằng build mục tiêu, không suy đoán từ header. |

## Công cụ và lỗi trong lượt

- `rg` không có trên PATH: lỗi `The term 'rg' is not recognized`; chuyển sang đọc/tìm bằng PowerShell và Python `-I`, không cài thêm công cụ.
- Một lệnh đọc gặp `UnicodeEncodeError` do stdout mặc định cp1252; đã dùng `sys.stdout.reconfigure(encoding='utf-8')`, đọc UTF-8 hoặc fallback GB18030, không sửa source.
- Có kết quả tìm kiếm bị giới hạn output; đã thu hẹp theo symbol và đọc vùng dòng cần thiết, không lấy output bị cắt làm bằng chứng đầy đủ.
- Git local: đã thử stage đúng hai file H-08 một lần; thất bại với `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/H-08/index.lock': Permission denied`. Git metadata nằm ngoài vùng ghi được phép; không thử lại, không sửa quyền/config hoặc xin vượt sandbox. Hai file kết quả được giữ trong worktree.

## Bàn giao

- Kết quả: DONE cho khảo sát tĩnh; không sửa mã hoặc khẳng định test game đạt. Có định nghĩa/công thức đã lần, bảng số liệu/ID, DB, gói tin, UI, trang bị/phi phong, đối chiếu Coco và 12 ca TESTER.
- Đã lưu nháp trong chính báo cáo này trước khi hoàn thiện; không tạo script/parser phụ hoặc báo cáo rời từng bước.
- Kiểm tra tài liệu đã chạy: 62 tham chiếu tường minh được kiểm tra có file và số dòng không vượt độ dài file; đủ 12 mã ca TESTER; quét mẫu gán secret/token/password/API key và IPv4 không có kết quả. Đây là kiểm tra báo cáo, không phải test chức năng hoặc bảo đảm rà soát hết mọi loại bí mật.
- Commit SHA: chưa có commit mới, vì `git add` bị từ chối quyền tạo `index.lock` như lỗi ở trên. Chưa stage được bằng lệnh này; không thay đổi Git metadata để vượt chặn.
- **BỊ CHẶN – CHƯA PUSH**: bàn giao Git bị chặn quyền ghi metadata; đồng thời task cấm mạng nên không thử push, không có link/bằng chứng GitHub mới. Trạng thái khảo sát là DONE; phần commit/push chưa hoàn tất.
