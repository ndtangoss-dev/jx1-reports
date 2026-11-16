1. Luồng đọc từ nguồn: client → Bishop:56722 → Sword3PaySys:5002 (tài khoản) / Goddess:5001 (nhân vật) → client nối gs001:51189 bằng GUID; `BH:9-17`, `Bishop/GamePlayer.cpp:734-738`, `CLIENT/gameui/KSelPlayer.cpp:1117-1134`.
2. Đăng nhập cần `Account_Info` và `Account_Habitus`; mật khẩu được client băm MD5, PaySys so chuỗi có phân biệt hoa/thường và kiểm hạn/điểm; `CLIENT/gameui/Klogin.cpp:471-495`, `PAY/S3PAccount.cpp:50-99,582-647`, `R/02-b2-account-db.md:19`.
3. `roledb` là Berkeley DB B-tree, khóa chính là tên nhân vật, giá trị là blob `TRoleData`; `roledb.0` lập chỉ mục tài khoản; `Goddess/DBTable.cpp:107-128`, `Goddess/IDBRoleServer.cpp:65-74,334-343,876`.
4. Sao lưu tích hợp ghi dump `.bak` theo từng cặp khóa/dữ liệu trong thư mục thời gian, không phải chép nguyên file B-tree; phục hồi/chất lượng bản sao hiện tại **chưa kiểm**; `Goddess/DBBackup.cpp:353-424`, `Goddess/DBDumpLoad.cpp:48-70,140-174`.
5. Đề xuất lưu `is_bot` ở bảng metadata SQL mới theo `cAccName`; tránh tái dùng cờ tính phí, trạng thái phiên hoặc sửa blob nhân vật; đây là thiết kế chưa triển khai; `PAY/S3PAccount.cpp:50-99,593-638`, `Goddess/IDBRoleServer.cpp:947-962`.

# A-02 — Luồng đăng nhập và tài khoản

Trạng thái: **PARTIAL — báo cáo hoàn tất, commit bị chặn**, ngày 16/11/2026. Kết luận nguồn không thay cho kiểm chứng runtime. Phạm vi theo `JX1_OPS/TASKS/A-02.md:16-28`.

## Worker kiểm tra trước khi làm

- Workspace xác nhận bằng `Get-Location`: `D:\JX-wt\A-02`; Git xác nhận nhánh `task/A-02-luong-dang-nhap`, khớp task. Trạng thái ban đầu chỉ có `?? JX1_OPS/TASKS/A-02.md`; giữ nội dung task có sẵn. Bằng chứng: kết quả lệnh trong phiên; yêu cầu tại `JX1_OPS/TASKS/A-02.md:7-8,16-19`.
- Chỉ ghi báo cáo này và mục **Kết quả** trong task; không chạy exe game, không kết nối VM/SQL/server, không đọc bản ghi tài khoản, file `roledb` hay dump dữ liệu. Ràng buộc: `JX1_OPS/TASKS/A-02.md:17-19,24-28`.

## Quy ước đường dẫn và mức bằng chứng

Các đường dẫn rút gọn dưới đây luôn tính từ đúng gốc trong bảng; số sau dấu `:` là số dòng thực trong file, tính cả dòng trống.

| Ký hiệu | Gốc tuyệt đối |
|---|---|
| `Bishop/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\MultiServer\Bishop\` |
| `Goddess/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\MultiServer\Goddess\` |
| `PAY/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\Sword3PaySys\S3AccServer\` |
| `GW/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\` |
| `CLIENT/` | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\` |
| `R/` | `C:\Jx1CocoV3\docs-analysis\reports\` |
| `BH` | File `C:\Jx1CocoV3\docs-analysis\BAI_HOC.md` |

**Nguồn trực tiếp** mô tả hành vi của mã đang đọc. **Báo cáo cũ** chỉ là bằng chứng lịch sử, không xác nhận trạng thái server ngày 16/11. **Đề xuất** chưa thay đổi schema/code. Cần phân biệt như vậy vì báo cáo 16 đã ghi nguồn và exe có thể lệch; báo cáo 44 còn có kết quả riêng cho từng bộ exe/DLL (`R/16-khao-sat-bot-ai.md:46`; `R/44-dieu-tra-a2-thoat-som.md:13-18,42-47`).

## Luồng đăng nhập dạng văn bản

```text
Client
  │ (1) c2s_login: tài khoản + MD5 + khu vực/phiên bản
  ▼
Bishop :56722
  ├─ (2) c2s_accountlogin ─► Sword3PaySys :5002 ─► SQL account :1433
  │                                              ├─ Account_Info
  │                 ◄─ kết quả xác thực/hạn/điểm ─└─ Account_Habitus
  │
  ├─ (3) c2s_roleserver_getrolelist ─► Goddess :5001
  │                                    └─ database/roledb + roledb.0
  │                 ◄─ danh sách nhân vật
  │                 ─► client chọn c2s_dbplayerselect
  ├─ (4) c2s_roleserver_getroleinfo ─► Goddess ─► blob nhân vật
  │                 ◄─ blob
  └─ (5) đồng bộ blob + GUID ─────────► gs001
         (qua kết nối gs001 → Bishop :56732)
                     ◄─ cho phép vào game + GUID
      ─► client: địa chỉ/cổng gs001 + GUID + bPermit

Client ── (6) kết nối mới + tagLogicLogin{GUID} ──► gs001 :51189
```

Bằng chứng cho từng bước:

1. `Klogin` đặt `c2s_login`, `LOGIN_A_LOGIN | LOGIN_R_REQUEST`, trường tài khoản, MD5, khu vực, bản đồ và phiên bản trước khi gửi. Cổng 56722 được ghi trong bản đồ cổng cũ và Bishop mở cổng client qua `GetClientOpenPort()`. Mật khẩu MD5 **viết hoa** là ghi nhận cũ; PaySys dùng `COLLATE Chinese_PRC_CS_AS`, nên phân biệt hoa/thường là có ý nghĩa (`CLIENT/gameui/Klogin.cpp:471-495`; `Bishop/Intercessor.cpp:329-337`; `BH:15`; `R/02-b2-account-db.md:19`; `PAY/S3PAccount.cpp:50`). Tên protocol đầu vào giữa cây client và Bishop có biến thể (`c2s_login_fhgyrinhkmvnsheypo` tại `Bishop/GamePlayer.cpp:818`); giá trị byte tương ứng **chưa kiểm**.
2. Bishop xếp chuỗi `WaitForAccPwd → QueryAccPwd → VerifyAccount → QueryRoleList → ProcessRoleList`; yêu cầu tài khoản mang `c2s_accountlogin` gửi qua `g_theSmartClient`. PaySys đọc `Account_Info`, rồi `GetLeftSecondsOfDeposit` ở `Account_Habitus`; thiếu bản ghi hạn trả `E_ACCOUNT_NODEPOSIT`. Với `iFlag=0` phải còn thời gian; với `iFlag=1` phải còn điểm, còn có xử lý trừ điểm (`Bishop/GamePlayer.cpp:734-738,908-940`; `PAY/S3PAccount.cpp:50-125,593-640`; cổng theo `BH:9-11`).
3. Bishop hỏi Goddess bằng tài khoản và khu vực, rồi chuyển kết quả về client. Ở nhánh DB, Goddess chuyển tài khoản về chữ thường, tìm chỉ mục tài khoản và lọc `BaseInfo.isWaiGua == nThisServer` để lấy tên/giới tính/ngũ hành/cấp (`Bishop/GamePlayer.cpp:1412-1428,1451-1452,1495-1503`; `Goddess/IDBRoleServer.cpp:923-962`).
4. `KSelPlayer::EnterGame` gửi `c2s_dbplayerselect` kèm tên nhân vật đã chọn; Bishop hỏi `c2s_roleserver_getroleinfo` kèm tên nhân vật, tài khoản, khu vực. Kết quả thành công được `_SyncRoleInfo_ToGameServerFs` chuyển tới game server (`CLIENT/gameui/KSelPlayer.cpp:1176-1190`; `Bishop/GamePlayer.cpp:1523-1554,1903-1911,2139-2158`).
5. Bishop tạo GUID và đóng gói cùng dữ liệu nhân vật gửi sang gs. `_NotifyPlayerLogin` nhận GUID, `bPermit`, thêm địa chỉ/cổng game server; `WaitForGameSvrPermit` gửi về client (`Bishop/GameServer.cpp:1415-1446,991-1021,1073-1081`; `Bishop/GamePlayer.cpp:2411-2433`). Kết nối nội bộ 56732 tách khỏi cổng client 56722 (`Bishop/Intercessor.cpp:306-337`; `BH:15-17`).
6. Client kiểm `bPermit` và tên tài khoản/nhân vật, nối `nIPAddr:nPort`, chép GUID vào `tagLogicLogin`, gửi `c2s__loginfs_kfjghtueodnchsf` và dọn kết nối gateway. Đích gs001 51189 là cổng được ghi nhận trong tài liệu trước, không phải giá trị cố định trong hàm này (`CLIENT/gameui/KSelPlayer.cpp:1073-1089,1105-1149`; `BH:17`; `R/12-doi-ip-tailscale-va-roledb.md:26`).

**Tài khoản dịch vụ:** Bishop/S3Relay đăng nhập PaySys qua `ServerList`; `S3PAccount::ServerLogin` truy vấn bảng này riêng với `Login` của người chơi. Vì vậy không dùng `ServerList` để đánh dấu bot người chơi (`PAY/S3PAccount.cpp:35-50,409-451`; `R/09-xoa-tai-khoan-that.md:6`; `BH:87`).

## Các bảng SQL và cột liên quan

Báo cáo 02 ghi DB `account` có 32 bảng; bảng dưới chỉ liệt kê phần cần cho task. Cột và vai trò được đọc từ câu SQL trong nguồn; kiểu SQL, chiều dài, khóa, default, trigger và schema đang chạy **chưa kiểm**. Không trích bất kỳ dòng dữ liệu nào (`R/02-b2-account-db.md:4-5,24`; `PAY/S3PAccount.cpp:50,593`).

| Bảng | Cột quan sát được | Vai trò và giới hạn kết luận | Bằng chứng |
|---|---|---|---|
| `Account_Info` | `cAccName`, `cPassword`, `iClientID`, `dLoginDate`, `dLogoutDate` | Danh tính/mật khẩu và trạng thái phiên. Login đọc `iClientID`; đoạn thành công đang ghi `iClientID=0`, không thể chỉ từ tên cột suy ra khóa phiên luôn hoạt động. Có cập nhật ngày đăng nhập/đăng xuất. | `PAY/S3PAccount.cpp:50-99,150,532,561` |
| `Account_Habitus` | `cAccName`, `iFlag`, `dEndDate`, `iLeftSecond`, `nExtPoint`, `iClientID`, `dBeginDate` | `iFlag` được dùng làm loại tính phí/VIP: 0 theo hạn, 1 theo điểm. `dEndDate` tạo số giây còn lại; `iLeftSecond` còn được dùng như thời gian game; `nExtPoint` bị trừ/cập nhật. Các cột này đã có nghĩa nghiệp vụ. | `PAY/S3PAccount.cpp:64-124,351,546,593-640` |
| `ServerList` | `cServerName`, `cPassword`, `cIP`, `iPort`, `iid`, `cMemo` | Xác thực dịch vụ; `iid` được trả làm game/server ID, `cMemo` được đối chiếu MAC trong nhánh kiểm địa chỉ. `iPort` có trong SELECT; đoạn đã đọc không chứng minh so khớp cổng. | `PAY/S3PAccount.cpp:409-451` |
| `Account_History` | `name_user`, `email_user` | Chỉ biết từ báo cáo cũ là bảng có dữ liệu cá nhân còn lại; chưa chứng minh tham gia đường đăng nhập. | `R/09-xoa-tai-khoan-that.md:23-24` |
| `AccCard_History` | **chưa kiểm** | Báo cáo cũ ghi đã dọn cùng dữ liệu tài khoản; không có bằng chứng trong phần nguồn đọc lần này rằng đây là điều kiện đăng nhập. | `R/09-xoa-tai-khoan-that.md:4,20` |

Liên kết logic hai bảng người chơi là `cAccName` (các câu truy vấn đều lọc theo trường này); quan hệ khóa ngoại vật lý **chưa kiểm**. Tài khoản đăng nhập được cần đồng thời thỏa điều kiện mật khẩu và quyền chơi, nên chỉ thêm dòng `Account_Info` là chưa đủ (`PAY/S3PAccount.cpp:50-99,593-611`; `BH:102-104`).

## Goddess `roledb`: định dạng và cách lưu

| Thành phần | Kết luận nguồn | Bằng chứng |
|---|---|---|
| Đường dẫn DB | `new ZDBTable("database","roledb")`, tương đối với thư mục làm việc Goddess; vị trí lịch sử `gw\database\roledb`. Không đọc file DB thực tế. | `Goddess/IDBRoleServer.cpp:334-343`; `R/09-xoa-tai-khoan-that.md:25` |
| Định dạng vật lý | Berkeley DB API `db_env_create`, `DB_ENV`, `DBT`, B-tree `DB_BTREE`. Môi trường bật log/transaction/recovery, `DB_PRIVATE`; DB chính có `DB_CREATE`. Phiên bản thư viện/endianness file thực tế **chưa kiểm**. | `Goddess/DBTable.cpp:30-42,107-110` |
| Khóa chính | Tên nhân vật dạng chuỗi, độ dài `strlen(name)+1` gồm NUL. | `Goddess/IDBRoleServer.cpp:798,876` |
| Giá trị | Blob `TRoleData` dài `dwDataLen`, được đưa trực tiếp vào `DBT.data`; hàm lưu từ chối độ dài từ 128 KiB trở lên. | `Goddess/IDBRoleServer.cpp:591-607,876`; `Goddess/DBTable.cpp:199-218` |
| Bố cục blob | Header tham khảo ở `Lib/S3DBInterface.h`: `BaseInfo`, version, số kỹ năng/task/item/bạn bè, các offset, `dwDataLen`, vùng dữ liệu biến độ dài. Header dùng pack 1; chưa xác nhận header nào được từng binary thực tế biên dịch. | `GW/Lib/S3DBInterface.h:15,183-201`; giới hạn nguồn/exe: `R/16-khao-sat-bot-ai.md:46` |
| Chỉ mục `roledb.0` | `get_account` lấy `BaseInfo.caccname`; `addIndex` gắn chỉ mục phụ, DB phụ cho phép khóa trùng. Vì vậy một tài khoản có nhiều nhân vật; giới hạn được nhận từ `nMaxRoleCount`. | `Goddess/IDBRoleServer.cpp:65-74,187-189,339,812-825`; `Goddess/DBTable.cpp:113-128` |
| Ghi và độ bền | `put(..., DB_AUTO_COMMIT)` cập nhật dữ liệu; môi trường bật `DB_TXN_NOSYNC`, lệnh `sync` sau put đang comment, `ZDBTable::commit()` chỉ trả true. Chưa đo mất dữ liệu khi crash; không xem chữ “commit” ở wrapper là bằng chứng đã flush ổ đĩa. | `Goddess/DBTable.cpp:40-42,194-196,218-234` |
| Dọn log | `removeLog` checkpoint rồi hỏi `log_archive(DB_ARCH_ABS)` và xóa các file được trả về; log thuộc cơ chế recovery. | `Goddess/DBTable.cpp:513-543` |
| Backend khác | Nguồn còn nhánh `DATA_KIND_SQL` lấy blob/danh sách từ `sqlitel_table`; không mặc định mọi cấu hình Goddess dùng `roledb`. Nhánh đang chạy **chưa kiểm**; các báo cáo cũ xác nhận đã dùng DB file. | `Goddess/IDBRoleServer.cpp:187-200,486-501,941-947`; `R/12-doi-ip-tailscale-va-roledb.md:6,22` |

## Sao lưu và phục hồi: cơ chế có trong nguồn

- **Lịch:** Goddess gọi `StartBackupTimer(g_BackupSleepTime)`; hàm này tạo `CDBBackup("database","roledb",db_table)`. `Open` lấy giờ modulo 24; luồng timer so giờ địa phương, kiểm mỗi 30 phút. Đây là lịch theo giờ trong ngày; giờ cấu hình và lần chạy thành công gần nhất **chưa kiểm** (`Goddess/Goddess.cpp:1435-1438`; `Goddess/IDBRoleServer.cpp:1648-1663`; `Goddess/DBBackup.cpp:198-212,307-324`).
- **Đầu ra:** hàm Backup tạo `database/<chuỗi thời gian>/<chuỗi thời gian>.bak`, kèm `.txt` thống kê và `Backup.log`. Chuỗi tên dùng `GetSystemTime`, ghép các thành phần số không zero-pad. Vì vậy tên thư mục không có bảo đảm dạng ISO cố định; thống kê có thông tin tài khoản/nhân vật (`Goddess/DBBackup.cpp:345-408,420-430`). Nhận định cũ “database/<ngày>” là cách gọi rút gọn (`BH:89`).
- **Định dạng `.bak`:** lặp cursor qua DB, ghi `[keysize: sizeof(UINT)] [key bytes] [datasize: sizeof(UINT)] [blob bytes]`. Không coi `.bak` này là file `roledb` B-tree để đổi tên rồi dùng trực tiếp (`Goddess/DBBackup.cpp:420-424`; `Goddess/DBDumpLoad.cpp:48-70`).
- **Đường phục hồi:** `CDBLoad` có `ReadData` theo cấu trúc trên; `copyData` đưa dữ liệu qua `UpdateDBPlayerDB` rồi `dbTable->add`. Do có bước chuyển cấu trúc, cần kiểm bản nguồn/binary và khôi phục thử trên bản copy trước khi tin cậy; task này chưa chạy phục hồi (`Goddess/DBDumpLoad.cpp:113-127,140-174`).
- **Đề xuất bản sao vật lý:** ở task vận hành được duyệt riêng, ngừng phát sinh ghi, thoát game và đóng Goddess hợp lệ, sau đó giữ bản copy nguyên môi trường `database` gồm DB chính, chỉ mục và các log còn cần cho recovery; kiểm hash và thử phục hồi trên môi trường tách biệt. Đây là đề xuất thận trọng từ việc có `DB_RECOVER`, ghi bất đồng bộ và log, chưa phải quy trình đã thử. Không tự xóa log để “làm sạch bản sao” (`Goddess/DBTable.cpp:40-42,107-128,218-234,521-535`; `Goddess/IDBRoleServer.cpp:386-403`).
- **Độ nhất quán chưa được chứng minh:** code backup đi qua cursor, nhưng chưa xác minh dump đang chạy có ảnh chụp transaction nhất quán khi server đồng thời ghi. Dữ liệu thật còn có thể nằm trong dump SQL, DB nhân vật, bản sao theo thời gian, log và snapshot cũ; báo cáo này chỉ ghi đường dẫn nguồn, không sao chép dữ liệu (`Goddess/DBBackup.cpp:420-430`; `R/09-xoa-tai-khoan-that.md:7,23-30`; `BH:89`).

## Đề xuất lưu cờ `is_bot` — chưa triển khai

| Vị trí | Đánh giá và lý do | Căn cứ |
|---|---|---|
| **Bảng mới `Account_BotMetadata`** | Ưu tiên cho cờ cấp tài khoản: `cAccName` là khóa logic và `is_bot bit NOT NULL DEFAULT 0` là cột mới đề xuất; không có dòng metadata thì ứng dụng coi là false. Kiểu/độ dài/collation của `cAccName`, khóa unique và FK phải lấy từ schema thực tế trước khi viết migration. Không lưu mật khẩu trong bảng này. | Truy vấn tài khoản dùng `cAccName`: `PAY/S3PAccount.cpp:50,593`; tên tài khoản ở chỉ mục nhân vật: `Goddess/IDBRoleServer.cpp:65-74,928-947` |
| Thêm `Account_Info.is_bot` | Có thể cân nhắc nếu muốn quản lý trong bảng danh tính. Các câu SQL đã đọc gọi tên cột cụ thể, nhưng chưa rà mọi tool/import/`SELECT *`; chưa đủ cơ sở khẳng định thêm cột tương thích hoàn toàn. | `PAY/S3PAccount.cpp:50,74-82,532,561` |
| Metadata theo nhân vật | Nếu một tài khoản trộn người chơi và bot, đề xuất bảng mới theo khóa tài khoản + định danh nhân vật; phải giải quyết đổi tên/xóa nhân vật trước. Không mặc định cờ cấp tài khoản giải quyết được tình huống này. | Khóa chính theo tên và chỉ mục theo tài khoản: `Goddess/IDBRoleServer.cpp:65-74,798,876` |
| Trường sẵn có trong SQL/blob | Không tái dùng `iFlag` (loại tính phí), `iClientID` (trạng thái phiên), `isWaiGua` (lọc khu vực), `iRoleParm6` (đã tham gia điều kiện đọc nhân vật). Không thêm byte vào blob trước khi xác minh version/offset và tất cả bên đọc. | `PAY/S3PAccount.cpp:50-99,593-638`; `Goddess/IDBRoleServer.cpp:537-549,947-962`; `GW/Lib/S3DBInterface.h:183-201` |

**Điểm đọc cờ đề xuất:** bộ quản lý bot có thể tra metadata bằng tài khoản, rồi vẫn đi qua xác thực PaySys và chọn nhân vật như client. Nếu gs cần cờ để áp chính sách riêng, phải thiết kế đường truyền từ nguồn metadata đáng tin, điểm gắn vào phiên và cơ chế làm mới ở một task triển khai riêng. Chỉ thêm cột không tự khiến Bishop/Goddess/gs biết `is_bot`; chuỗi nguồn đang đọc chỉ chuyển các thông tin tài khoản, hạn/điểm, nhân vật và GUID (`Bishop/GamePlayer.cpp:908-940`; `Bishop/GameServer.cpp:1421-1437`; `CLIENT/gameui/KSelPlayer.cpp:1128-1134`).

## Tái sử dụng tài liệu và giới hạn runtime

| Tài liệu đã dùng | Nội dung giữ lại cho A-02 |
|---|---|
| `R/02-b2-account-db.md:4-5,19,24` | DB SQL `account`, số bảng lịch sử, MD5 viết hoa; không dùng các giá trị tài khoản. |
| `R/09-xoa-tai-khoan-that.md:6-7,20,23-30` | Phân biệt `ServerList` với tài khoản người chơi; lịch sử dọn DB không có nghĩa roledb/log/snapshot cũng sạch. |
| `R/12-doi-ip-tailscale-va-roledb.md:6,22-26` | Đã từng ghi nhận DB rỗng 8192 byte và các cổng; không suy ra kích thước/nội dung hiện tại. |
| `R/16-khao-sat-bot-ai.md:20,46,53` | Luồng MD5 → Bishop → GUID → gs, nhu cầu hai bảng tài khoản và giới hạn khớp nguồn/exe. |
| `R/29-dieu-tra-gs001-crash.md:54-58,79-81` | Đã từng có lỗi khi thăm dò 51189 lúc gs còn nạp; A-02 không thử kết nối cổng. |
| `R/44-dieu-tra-a2-thoat-som.md:13-18,42-47` | Kết quả tùy bộ exe/DLL, có cập nhật sau kết luận đầu; không lấy việc nghe cổng/sống một thời gian làm bằng chứng đăng nhập hoàn chỉnh. |
| `BH:9-17,87-89,102-104,200` | Bản đồ cổng, vai trò ServerList, roledb/backup, hai bảng tài khoản và hạn chế thăm dò gs. |

## Chưa kiểm

- **Runtime:** chưa kết nối client, Bishop, PaySys, Goddess hoặc gs; chưa xác nhận binary/config đang chạy, giá trị protocol, đóng gói/ABI hay phiên đăng nhập thực. Cơ sở cần xác minh: `R/16-khao-sat-bot-ai.md:46`; `R/44-dieu-tra-a2-thoat-som.md:13-18,42-47`.
- **SQL:** chưa đọc schema sống, constraint, trigger, dữ liệu/giá trị credential; chưa kiểm mọi bảng trong 32 bảng hoặc nhánh super-password. Bảng SQL trên chỉ dựa vào truy vấn nguồn (`R/02-b2-account-db.md:24`; `PAY/S3PAccount.cpp:50,593`; `Bishop/GamePlayer.cpp:919-931`).
- **DB nhân vật:** chưa mở `roledb`, xác nhận phiên bản Berkeley DB, backend DB/SQL thực dùng, header biên dịch, độ bền khi mất điện hay phần dữ liệu chưa flush (`Goddess/DBTable.cpp:40-42,218-234`; `Goddess/IDBRoleServer.cpp:941-947`; `GW/Lib/S3DBInterface.h:183-201`).
- **Backup:** chưa xem thư mục backup thật, cấu hình lịch, log thành công, tính nhất quán hoặc khôi phục thử; chưa có bằng chứng quy trình sao lưu vật lý đề xuất hoạt động (`Goddess/Goddess.cpp:1435-1438`; `Goddess/DBBackup.cpp:307-324,420-430`; `Goddess/DBDumpLoad.cpp:140-174`).
- **`is_bot`:** chưa migration, tạo tài khoản, sửa code/packet, build hay thử quyền đọc metadata. Thiết kế bảng và vị trí tiêu thụ cờ là đề xuất từ các khóa và luồng hiện có (`PAY/S3PAccount.cpp:50,593`; `Bishop/GameServer.cpp:1421-1437`).

## Kiểm tra hoàn tất, lỗi và xử lý trong cùng task

- Kiểm tra tài liệu: có đúng 5 dòng tóm tắt đầu file, sơ đồ văn bản, bảng SQL/cột, roledb và backup, phương án `is_bot`, nguồn có số dòng và mục Chưa kiểm. Không có lệnh build/test trong task (`JX1_OPS/TASKS/A-02.md:25-28`); không chạy build/test, exe hay kiểm tra mạng.
- Lệnh đọc đầu tiên qua shell mặc định không hoàn tất trong thời gian chờ; dừng cell chờ. Một lần tạo process sau đó trả `orchestrator_helper_incomplete: setup helper exited successfully before setup completed`. Dùng `powershell` với `login:false` và `git -c core.fsmonitor=false status --short --branch` đọc trạng thái thành công. Chưa xác định nguyên nhân gốc của helper; không sửa cấu hình người dùng.
- `rg` không có trong PATH (`The term 'rg' is not recognized`); dùng `Get-ChildItem`, `Select-String` và đọc các đoạn nguồn cụ thể. Không cài công cụ hoặc tạo parser/script phụ.
- Giải mã Default/GBK làm một số phần báo cáo/BAI_HOC sai chữ; đọc lại các đoạn cần dùng bằng UTF-8. BAI_HOC và phần cập nhật của báo cáo 44 có các đoạn không giải mã đồng nhất; chỉ dùng symbol/số dòng đọc được và đối chiếu nguồn, không chuyển mã hay ghi lại file gốc.
- Một lệnh đọc nhiều khoảng dòng gặp `Argument types do not match` ở khoảng DBBackup đơn; tách truy vấn theo symbol/khoảng dòng rồi đọc thành công. `KSelPlayer.cpp` không ở `jxOnline/gameui`; đã tìm đúng bản client 2912 bằng tên file, không dùng bản làm việc AMOLX để thay nguồn.
- Kiểm tra nội dung bằng PowerShell đạt: đúng 5 dòng tóm tắt, đủ các mục bắt buộc và không có ký tự Unicode thay thế trong báo cáo. Đây là kiểm tra tài liệu, không phải test/build/runtime.
- **Commit bị chặn:** `git -c core.fsmonitor=false add -- JX1_OPS/REPORTS/A-02-luong-dang-nhap.md JX1_OPS/TASKS/A-02.md` thoát 1 với lỗi nguyên văn `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-02/index.lock': Permission denied`. Git metadata của worktree nằm ngoài writable root `D:\JX-wt\A-02`; không thử lại cùng lỗi, không sửa quyền/config hoặc chuyển Git directory để vượt sandbox. Chưa stage, chưa commit, không có SHA mới. Hai file được giữ local; diff của file mới được xem bằng chế độ `git diff --no-index` chỉ đọc.
- **BỊ CHẶN – CHƯA PUSH.** Người dùng chỉ yêu cầu commit local; không thực hiện push. Bước tiếp tục khi có phiên được phép ghi Git metadata: stage đúng hai file trên và commit với tiêu đề `A-02 Mô tả luồng đăng nhập và tài khoản`; các lệnh đầy đủ nằm trong mục Kết quả của task.
