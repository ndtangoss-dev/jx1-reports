# TÓM TẮT 5 DÒNG

1. PARTIAL: đã đối chiếu tĩnh request tạo role, response, role list và đường thoát/lưu; chưa có bằng chứng ACK logout ứng dụng dành cho BOT.
2. Tạo role: `c2s_newplayer=69`, header `TProcessData` 14 byte + gender/series/map/name; response `157`, 66 byte, chỉ có bool kết quả.
3. Role list `55`: 14 byte header + count + mỗi role 67 byte; luồng tạo thành công đi thẳng vào game, không tự gửi lại role list.
4. Client thoát bằng dọn/đóng socket; ACK lưu `56` là Goddess → GS, có sentinel `791030`, không phải client ACK và chưa bảo đảm DB thành công.
5. Không sửa source, không test/build/chạy exe/kết nối mạng; vector là dữ liệu tổng hợp từ source; ABI/binary/encoding thực tế [CHƯA KIỂM].

## Phạm vi, đường dẫn và quy ước

Ngày 17/11/2026, workspace `D:\JX-wt\E-07`, branch `task/E-07-gap`.
Đã đọc đúng task E-07 và hai báo cáo E-05b/E-01b. Git status trước khi ghi:
chỉ `?? JX1_OPS/TASKS/E-07.md`; giữ nguyên task ngoài mục Kết quả.
Không có báo cáo E-07 sẵn để tiếp tục. Chỉ ghi báo cáo này và mục Kết quả task.

Hai đường dẫn `D:\Jx1CocoV3\Folder` và `D:\JX-source\SwordOnline` trong task
không tồn tại (`PathNotFound`). Dùng cây tương ứng ở ổ C đã được E-01b dẫn
nguồn, chỉ đọc; không khẳng định đó là cùng revision với cây D bị thiếu.

Các dẫn nguồn dưới đây là `bí danh/file:dòng`, số dòng tính từ 1:

- C = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes`.
- S = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline`.
- B = S/`gateway/Sources/MultiServer/Bishop`.
- G = S/`gateway/Sources/MultiServer/Goddess`.
- GH = S/`gateway/Headers`; SH = S/`gameserver/Headers`.
- GS = S/`gameserver/Sources/MultiServer/GameServer`.
- CS = S/`gameserver/Sources/Core/Src`.

Profile tính byte: little-endian, BYTE/char/bool=1, unsigned short/WORD=2,
int/UINT/unsigned int=4, `pack(1)`. C/gamecore/KProtocol.h:10-11,
GH/KProtocol.h:18-19 khai báo pack1; S/header/GameDataDef.h:134-135 cho
NAME_LENGHT=64, ACC_LENGTH=32 (client NAME_LENGHT tại
C/gamecore/GameDataDef.h:152). Đây là tính từ khai báo, **không phải sizeof
đã chạy bằng compiler/binary đích** [CHƯA KIỂM].

## Header chung và lớp vận chuyển

`TProcessData`: tổng sizeof 15, prefix trước `pDataBuffer` là 14 byte.
Khai báo client C/gamecore/KProtocol.h:1819-1827; Bishop/Goddess
GH/KProtocol.h:1929-1937; GS SH/KProtocol.h:1941-1949 khớp thứ tự:

| Offset | Số byte | Field |
| --- | ---: | --- |
| 0 | 1 | nProtoId |
| 1 | 4 | nDataLen, UINT LE; ý nghĩa tùy message, không dùng một quy tắc chung |
| 5 | 4 | ulIdentity, unsigned int LE |
| 9 | 1 | bLeave, bool |
| 10 | 4 | uSelServer, UINT LE |
| 14 | biến | pDataBuffer |

Client `SendPackToServer` thêm WORD LE bằng **2 + số byte payload**, rồi XOR
payload, không XOR WORD (C/network/ClientStage.cpp:136-177, cụ thể 157-161).
KSG_EncodeBuf gọi KSG_DecodeEncode (C/network/KSG_EncodeDecode.h:33-42).
Thuật toán ở C/network/KSG_EncodeDecode.cpp:14-35: mỗi DWORD XOR cùng giá trị
trạng thái phiên hiện tại; đuôi 1–3 byte XOR lần lượt byte thấp của trạng thái;
cập nhật trạng thái một lần sau payload bằng phép nhân 31 rồi cộng hằng số
trong source, modulo 2^32. Không chép giá trị trạng thái/khóa phiên vào báo cáo.
Không có mật khẩu trong request tạo role.

Vector dưới đây là **payload rõ trước XOR / sau giải mã**, không phải capture
TCP. Prefix WORD được ghi riêng khi hữu ích, chưa ghép ciphertext. Không có
vector mã hóa gắn với phiên thật [CHƯA KIỂM]. Gói nội bộ save/create lớn còn
qua CPackager; không gửi các payload nội bộ đó như request của BOT.

## 1. Tạo nhân vật

### Request client → Bishop

C/gameui/KSelPlayer.cpp:1041-1044 chỉ có lời gọi xử lý list/create bị comment.
Đường tạo thực được khảo sát là C/gameui/KuiNewPlayer.cpp::CreateRole:616-650.
Enum C/gamecore/KProtocolDef.h:248-253 đếm từ gameserverbegin=64 nên
`c2s_newplayer=69=0x45`; GH/KProtocolDef.h:255 là symbol phía gateway.

| Offset payload | Byte | Giá trị / ý nghĩa |
| --- | ---: | --- |
| 0 | 1 | 45, c2s_newplayer |
| 1 | 4 | nDataLen = 4 + L + 1, L là strlen tên theo byte |
| 5 | 4 | ulIdentity=0 |
| 9 | 1 | bLeave **không được gán** bởi CreateRole |
| 10 | 4 | uSelServer=nServerRegionIndex, phải >0 ở guard client |
| 14 | 1 | m_btRoleNo = m_Info.Gender (giới tính, không phải slot role) |
| 15 | 1 | m_btSeries = m_Info.Attribute (hệ/ngũ hành) |
| 16 | 2 | m_NativePlaceId, unsigned short LE |
| 18 | L+1 | m_szName, byte tên rồi NUL |

`NEW_PLAYER_COMMAND` cố định trong bộ nhớ là 68 byte nhưng trên dây rút gọn
tên: tổng payload **19+L**. C/gamecore/KProtocol.h:1849-1855;
GH/KProtocol.h:1961-1967. Client gán giới tính/hệ/map tại
C/gameui/KuiNewPlayer.cpp:633-635, tên tại 637-638, nDataLen/identity/region
tại 640-646. Mảng Data không zero-init và không gán bLeave: không được mô tả
mọi byte header của client là xác định. BOT sau này có thể chọn 00 cho byte
này trong fixture, nhưng đó là chuẩn hóa của fixture, không phải byte đo được.

B/GamePlayer.cpp::SelAddDelRole:1562-1615 nhận đúng TProcessData và body,
chuyển tham số sang `_CreateNewPlayer_ToDBRole`. Có lỗi tính namelen tại
1574: lấy tổng buffer trừ sizeof(TProcessData), thay vì lấy độ dài tên.
Với request rút gọn, giá trị là L+4, có thể đọc thêm ba byte ngoài độ dài
đã gửi khi memcpy tên tại 1578; NUL ở tên vẫn có trong payload. Không sửa
source; ảnh hưởng binary thực và giới hạn tên [CHƯA KIỂM].

Tên: UI lấy `getText`, strlen 6..24, loại chữ số/khoảng trắng/ký tự khác,
copy trực tiếp sang m_Info.Name; không thấy chuyển codec trên đường này
(C/gameui/KuiNewPlayer.cpp:554-606). Bishop gọi CountTCVN3Characters thực chất
strlen và yêu cầu 6..16 byte, rồi IsTCVN3NameValid
(B/GamePlayer.cpp:1942-1947; B/PlayerCreator.cpp:460-476). Vì vậy **không được
kết luận wire bắt buộc UTF-8 hoặc TCVN3 chỉ từ comment/tên hàm**; tên có dấu
và round-trip DB [CHƯA KIỂM]. Dùng ASCII `BotAbc` để tránh mơ hồ trong vector.
Giá trị map 53/hệ 0/giới tính 0 là tổng hợp, không khẳng định map/tạo role
hợp lệ với cấu hình runtime.

### Response Bishop → client; kết quả Goddess

`tagProtoHeader` một byte, `tagDBSelPlayer` thêm tên 64 byte,
`tagNewDelRoleResponse` thêm bool (C/gamecore/KProtocol.h:1486-1512;
GH/KProtocol.h:1549). Enum từ 64, qua ping=143 tới newdel=157:
C/gamecore/KProtocolDef.h:52-145; GH/KProtocolDef.h:132-146.

| Offset | Byte | Nội dung |
| --- | ---: | --- |
| 0 | 1 | 9D, s2c_rolenewdelresponse=157 |
| 1 | 64 | szRoleName |
| 65 | 1 | bSucceeded: 01 thành công, 00 thất bại |

Payload 66 byte, không có nDataLen, không có mã lỗi chi tiết cho client.
B/GamePlayer.cpp::WaitForCreateResult:1730-1777 chỉ gán szRoleName[0]=NUL;
63 byte còn lại chưa khởi tạo. Success/failure đều giữ tên rỗng, không echo
tên role. Case lỗi sớm tại 1603-1607 cũng như vậy. Không dùng vùng tên rác
để so khớp request hoặc ghi log. Client kiểm bool và chuyển WAIT_TO_LOGIN_GAMESERVER
(C/gameui/KuiNewPlayer.cpp:1032-1071); so sánh tên tại 1041 bị comment.

Luồng nội bộ: B/GamePlayer.cpp:1980-1993 tạo `TProcessData` ID 11=0B,
identity là connection ID, region, body `01 || TRoleData`, nDataLen=D+1,
tổng 15+D rồi CPackager chia gói. G/ClientNode.cpp::_CreateRole:407-461
gọi SaveRoleInfo(body+1,NULL,TRUE); response nội bộ ID **57=39**, nDataLen=1,
identity echo, body **01 nếu nResult==1, FF nếu khác**; gửi sizeof(TProcessData)=15.
bLeave/uSelServer response create không được gán. Bishop chỉ chấp nhận kết quả
1, mọi giá trị khác trở thành bool false, không tách lỗi trùng tên/hết slot.

G/IDBRoleServer.cpp:602-607 từ chối blob >=128 KiB; 688-705 kiểm số role và
tên trùng ở nhánh SQL. Tại 760 gọi updateBlobData_n rồi trả 1 tại 787 mà
không kiểm kết quả lời gọi trong hàm này. Nhánh DB khác dùng
db_table->add tại 876 và trả 1 tại 910; G/DBTable.cpp:199-230 thực hiện put
DB_AUTO_COMMIT và kiểm ret; `ZDBTable::commit` tại 194-197 chỉ trả true.
Do đó ACK 01 chỉ là kết quả theo logic source, **chưa chứng minh dữ liệu đã
bền vững**, đặc biệt nhánh SQL [CHƯA KIỂM]. Không truy cập DB.

### Role list cập nhật

Đường thành công sau tạo là `WaitForCreateResult → ProcessRoleInfo →
WaitForGameSvrPermit` (B/GamePlayer.cpp:762-764); không phải quay lại
QueryRoleList. Role list chỉ nằm trong login task tại 734-738. Không thấy
push list mới trong đường tạo vừa đối chiếu. Muốn kiểm list sau tạo cần
login lại và đọc response list; chưa chứng minh có API refresh trực tiếp
client → Bishop trong trạng thái này [CHƯA KIỂM].

G/ClientNode.cpp::_QueryRoleList:337-397 gửi nguyên danh sách cho Bishop,
B/GamePlayer.cpp::ProcessRoleList:1472-1499 forward nguyên buffer tới client.
ID **55=37**, header chung 14 byte; nDataLen=1+67*N; tổng **15+67*N**.
Body offset 14: count 1 byte; mỗi record từ offset 15+67*i:

| Offset trong record | Byte | Field |
| --- | ---: | --- |
| 0 | 64 | szName, chuỗi NUL trong vùng cố định |
| 64 | 1 | Sex |
| 65 | 1 | Series |
| 66 | 1 | Level (BYTE, không phải int) |

Struct GH/KProtocol.h:1910-1919, C/gamecore/KProtocol.h:1800-1809;
client đọc C/gameui/Klogin.cpp:1033-1075. Count yêu cầu Bishop là 3 tại
B/GamePlayer.cpp:61,1425; Goddess có mảng DBI[4] tại G/ClientNode.cpp:372.
Không suy mảng 4 nghĩa là client luôn nhận bốn record. Goddess chỉ gán
ID/identity/nDataLen/count, không gán bLeave/uSelServer của response này.
`memcpy(...,nDataLen)` tại G/ClientNode.cpp:392 copy thừa 1 byte so với
67*N vào vùng sau count, nhưng nUsedLen=14+nDataLen nên byte thừa không
được gửi. N=4 còn có nguy cơ đọc ngoài DBI; không kiểm runtime.

`s2c_syncrolelist` là message khác: handler
C/gamecore/KProtocolProcess.cpp:1902-1906 chỉ cast và TODO. Không dùng nó
làm bằng chứng cập nhật role list sau create.

## 2. Logout ứng dụng và lưu

### Client → GS: đường thoát không có application payload riêng

C/gameui/KuiEscInfo.cpp:257-266 đặt `nisgetinfo=false`; update ở
C/gamescene/KgameWorld.cpp:5059-5064 gọi `_quitGame`. Hàm này tại 2378-2417
đặt key mode chặn gửi, dừng thread, xóa buffer, Cleanup, giải phóng core và
trở về login. C/network/ClientStage.cpp:73-88 gọi StopConnections;
C/network/SocketClient.cpp:148-180 đóng socket bằng closesocket trên Windows.
Đường được đọc không gửi gói logout ứng dụng và không đợi ACK lưu.

Vì vậy vector logout ứng dụng cho đường này là **chuỗi payload rỗng ε**,
không phải byte `00`, không phải frame `02 00`. Việc đóng socket có thể tạo
FIN/RST tùy hệ điều hành/trạng thái; không dựng TCP header/sequence giả để
nhận đó là vector ứng dụng. Không có mã kết quả hoặc thời điểm ACK client
xác định được từ đường này [CHƯA KIỂM].

`GOI_LIXIAN` ở KuiEscInfo.cpp:278-282 là chức năng offline khác;
CS/KProtocolProcess.cpp::c2sLiXian:9191-9194 gọi offline.lua, không coi là
logout lưu bình thường. `s2c_logout=66` có handler NULL tại
C/gamecore/KProtocolProcess.cpp:46, nên không tự gán ý nghĩa save ACK.
`KPlayer::QuitGame` tại CS/KPlayer.cpp:1176-1196 còn comment `Save()`.

### GS → Goddess: lưu sau đóng kết nối

GS/KSOServer.cpp::ServerEventNotify:175-176 nhận enumClientConnectClose rồi
SetNetStatus(...enumNetUnconnect,true). Nhánh đang chơi tại 4938-4955 kiểm
index kết nối, CheckSerMaps rồi gọi CoreServerShell::SavePlayerData(nIndex,isSave).
CS/CoreServerShell.cpp:579-601 gọi Player.Save để dựng blob rồi
Player.SavePlayerData(isLeave). Return TRUE của shell không chứng minh các
thao tác lồng nhau thành công vì kết quả SavePlayerData không được kiểm.

CS/KPlayerDBFuns.cpp:44-115 dựng save stream:

| Offset | Byte | Field |
| --- | ---: | --- |
| 0 | 1 | 0A = c2s_rolekfjhu_saveroleinfo |
| 1 | 4 | nDataLen = D+14 (tổng stream), khác quy ước create/list |
| 5 | 4 | ulIdentity = player index GS |
| 9 | 1 | bLeave = isLeave, 01 trên nhánh disconnect nói trên |
| 10 | 4 | uSelServer = vùng hiện tại |
| 14 | D | TRoleData blob, D lấy dwDataLen |

14 byte header + D byte blob qua CPackager::GetHeadPack/GetNextPack.
Không có CRC được thêm trong đoạn này: lời gọi CRC/comment tại 85-95.
Luồng fallback GS/KSOServer.cpp::SavePlayerData:4553-4616 có cùng công thức.
**[CHƯA KIỂM]** toàn bộ layout TRoleData, dữ liệu phụ thuộc inventory/skill/task,
CPackager wire fragmentation và codec đường server nội bộ; không cung cấp
blob tổng hợp rồi gọi đó là request save hợp lệ. BOT không có quyền gửi
message ID 10 vào kênh game để giả lập GS.

### Goddess → GS: ACK nội bộ, không chuyển tới client

G/ClientNode.cpp::_SaveRoleInfo:469-504 gọi SaveRoleInfo(body,NULL,FALSE).
Chỉ khi bLeave và identity thỏa điều kiện mới gửi sizeof(TProcessData)=15:

| Offset | Byte | Giá trị |
| --- | ---: | --- |
| 0 | 1 | 38 = s2c_roleserver_saverole_result=56 |
| 1 | 4 | F6 11 0C 00 = 791030, **sentinel**, không phải length 1 |
| 5 | 4 | ulIdentity echo player index |
| 9 | 1 | bLeave chưa được khởi tạo trong Info |
| 10 | 4 | uSelServer echo |
| 14 | 1 | 01 nếu SaveRoleInfo trả 1, FF nếu khác |

GS/KSOServer.cpp:2916-2950 kiểm sentinel/index, nhưng **không đọc byte
pDataBuffer[0]**. Khi SAVE_DONE, GS đặt SAVE_REQUEST rồi ClientDisconnect;
khi trạng thái khác còn có nhánh về SAVE_IDLE. Không thấy send ACK client
trong handler này. Ngay cả log `Archive successfully` tại 2927 cũng xuất
trước kiểm kết quả body, không dùng log đó làm bằng chứng save thành công.
Nhánh SQL return 1 không kiểm update như phần tạo role tiếp tục là giới hạn.

### Các message logout tên tương tự nhưng khác kênh

`c2s_leavegame=53=35` là **GS → Bishop**, không phải client → GS.
GH/KProtocol.h:1818-1829 và SH/KProtocol.h:1830-1841:
payload 106 byte = ID1 + cmd1 + int4 + int4 + char64 + char32.
Offsets: 0 ID, 1 cCmdType, 2 nExtPoint, 6 nGameExtTime,
10 nClientIp[64], 74 szAccountName[32]. NORMAL=00, HOLDACC=1A
(GH/KProtocol.h:1809-1810); trường tên `nClientIp` thực được GS gán role name
tại GS/KSOServer.cpp:4819-4824, không nên suy nó là địa chỉ IP.
B/GameServer.cpp:1139-1177 gọi PopAccount; đoạn định gửi client ở
1148-1176 **bị comment**. GS phát message trên nhánh timeout/quit trong
PlayerLogoutGateway (4791-4917), không có bool save-success trong message.

`s2c_logiclogout=59=3B` là **Bishop → GS**, 65 byte: ID1 + roleName[64]
(C/gamecore/KProtocol.h:1703-1706; SH/KProtocol.h:1779).
B/GameServer.cpp::_PlayerLogicLogout:1398-1410 gửi bằng m_pGameSvrServer,
không phải m_pPlayerServer. Không có result field; đuôi tên có thể chưa
khởi tạo do memcpy datalength. Không dùng làm ACK logout client. Account
logout ID35 thuộc kênh account/pay, cũng không thay thế xác nhận lưu.

## Vector tổng hợp có thể dùng để đối chiếu parser

Ký hiệu `00{n}` là lặp byte 00 đúng n lần; `||` là nối, không phải byte.
Các byte chưa khởi tạo được chuẩn hóa 00 **chỉ trong fixture**, nên vector
không khẳng định sender thật sẽ phát vùng đệm zero. Không chứa thông tin
tài khoản thật, mật khẩu, khóa hoặc trạng thái mã hóa phiên.

| Vector | Payload hex rõ | Tổng byte / điều kiện kiểm |
| --- | --- | --- |
| Create BotAbc | `45 0B 00 00 00 00 00 00 00 00 01 00 00 00 00 00 35 00 42 6F 74 41 62 63 00` | 25; L=6, prefix WORD `1B 00`; region=1; gender=0, series=0, map=53 |
| Create OK client | `9D || 00{64} || 01` | 66; prefix `44 00`; byte 65=1, tên rỗng |
| Create FAIL client | `9D || 00{64} || 00` | 66; bool=0; không đoán chi tiết lỗi |
| Goddess create OK nội bộ | `39 01 00 00 00 01 00 00 00 00 00 00 00 00 01` | 15; identity=1; hai field không gán đã chuẩn hóa; FAIL đổi cuối thành FF |
| List rỗng | `37 01 00 00 00 01 00 00 00 00 00 00 00 00 00` | 15; nDataLen=1, count=0 |
| List một role BotAbc | `37 44 00 00 00 01 00 00 00 00 00 00 00 00 01 || 42 6F 74 41 62 63 || 00{58} || 00 00 01` | 82; nDataLen=68, prefix `54 00`; name64, Sex0/Series0/Level1 |
| Logout client | `ε` | 0 application byte; không có frame; socket close là sự kiện riêng |
| Save stream prefix nội bộ | `0A || LE32(D+14) || 01 00 00 00 || 01 || 01 00 00 00 || blob[D]` | Công thức 14+D, chưa có full blob vector hợp lệ [CHƯA KIỂM] |
| Save ACK OK nội bộ | `38 F6 11 0C 00 01 00 00 00 00 01 00 00 00 01` | 15; identity1, region1; FAIL đổi cuối FF; parser không lấy sentinel làm length |
| Leave GS → Bishop | `35 00 || 00{8} || 42 6F 74 41 62 63 || 00{58} || 66 69 78 74 75 72 65 || 00{25}` | 106; role BotAbc, account giả fixture; không phải request BOT |
| Logic logout Bishop → GS | `3B || 42 6F 74 41 62 63 || 00{58}` | 65; không có bool; không phải save ACK |

Các kiểm tra âm có thể dựng từ chính bảng, **chưa chạy**: cắt create trước
NUL; khai nDataLen khác 4+L+1; role count 1 nhưng thiếu 67 byte; nhầm Level
thành DWORD; coi 791030 là body length; coi save FF như OK; chờ 9D trong
kênh game thay vì Bishop. E-07 chỉ giao tài liệu, không thêm parser/test BOT.

## Kết luận cho E-05b và phần chưa xác minh

Phần tạo role đã có đủ hợp đồng byte theo source profile để thiết kế fixture:
chờ role-list-ready, gửi 69 tới Bishop, nhận 157 bool, thành công tiếp tục
permit/game login; role list kiểm ở login sau. Không phụ thuộc echo tên từ
response vì sender đặt tên rỗng. Việc này chưa được triển khai vào BOT.

Phần logout/persistence vẫn cần giữ BỎ QUA xác nhận ứng dụng trong E-05b:
source đang xét đóng socket; ACK DB nằm ở kênh khác và GS bỏ qua cờ lỗi.
Role list sau re-login chỉ xác nhận role/name/sex/series/level; không xác
nhận vị trí, HP, item hoặc toàn bộ trạng thái đã lưu.

**[CHƯA KIỂM]** revision/binary khớp source; sizeof ABI đích; codec tên có dấu;
map/gender/series được runtime chấp nhận; role list thật sau create; full blob
TRoleData/CPackager và framing nội bộ; DB persistence; application logout ACK
ngoài đường client đã đọc. Không tạo ID/request/ACK fallback khi thiếu bằng chứng.

Trạng thái **PARTIAL** vì chưa thể cung cấp vector request/ACK logout ứng dụng
có xác nhận lưu: đường source khảo sát không có hợp đồng đó, full save blob
chưa khai triển và runtime bị loại khỏi phạm vi. Bước tiếp: PM dùng báo cáo
để thiết kế fixture tạo role; việc xác minh binary/DB hoặc chọn cơ chế xác
nhận lưu cần một task được duyệt riêng. Không cần chạy lại khảo sát đã có.

## Kiểm chứng, lỗi công cụ và bàn giao

Chỉ đọc source và tính độ dài/offset từ khai báo; không chạy test, build,
exe, game/server, DB, socket kể cả loopback, VM hoặc lệnh mạng. Không công bố
offline tests đạt và không suy runtime từ source. Không sửa source canonical,
BOT, cấu hình hay BAI_HOC; không ghi secret/credential.

Lỗi trong lượt: lượt đọc task đầu PowerShell mặc định hiển thị sai dấu, đọc
lại UTF-8 thành công. Đường source ổ D thiếu như trên; hai đường Bishop/Goddess
trực tiếp dưới Sources cũng thiếu, đã xác định đúng Sources/MultiServer và
đọc tiếp. `rg` không có trong PATH (Get-Command không trả kết quả); dùng
Select-String/Get-Content có phạm vi. Một lệnh Get-ChildItem -LiteralPath
kết hợp -Include trả quá rộng và đầu ra bị cắt; không dùng danh sách đó làm
bằng chứng, chuyển -Filter/đường thư mục cụ thể. Không sửa môi trường/quyền,
không lặp một lỗi quá ba lần. Không có lỗi test vì không chạy test.

Đã rà nội dung/diff một lượt và kiểm whitespace sau khi ghi. Hai file đều
là file mới/untracked từ góc nhìn Git nên diff --no-index trả 1 khi có nội dung,
không phải kiểm thử thất bại. Không stage/commit/push: người dùng chỉ cho ghi
báo cáo và mục Kết quả, đồng thời cấm mạng. Không có commit SHA/link GitHub mới;
kết quả local, **CHƯA PUSH** theo phạm vi, không phải đã thử rồi bị Git chặn.
