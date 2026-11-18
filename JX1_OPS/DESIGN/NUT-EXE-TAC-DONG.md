# Nút của các exe server tác động tới server và client thế nào

Tổng hợp từ 6 báo cáo đọc tĩnh N-01..N-06 (#164, gộp ở #165). **Không có phép thử nào ở đợt này**: không chạy exe, không VM, không client. Nhãn: [NGUỒN file:dòng] = đọc từ mã nguồn; [TÀI LIỆU] = kết quả đã ghi ở tài liệu trước (#161/#162); [GIẢ THUYẾT] = suy ra, chưa kiểm; "chưa kiểm" = không có bằng chứng. Mã nguồn có thể không khớp exe đang chạy (chưa đối chiếu binary lần nào).

Bốn câu hỏi cho mỗi nút: (1) ghi vào đâu; (2) exe nào nhận và làm gì; (3) tác động lên server; (4) tác động lên client. Bảng đầy đủ từng nút nằm ở báo cáo gốc (đường dẫn ở đầu mỗi nhóm). Các tên tắt trong ngoặc: B = Bishop, G = Goddess, GS = gs001, O = client.

## 0. Bức tranh chung

```mermaid
flowchart LR
    C[Client] -->|56722 đăng nhập| B[Bishop]
    B -->|5002 xác thực| P[PaySys]
    B -->|5001 danh sách và dữ liệu nhân vật| G[Goddess]
    C -->|IP và cổng trong permit| GS[gs001]
    GS -->|56732 đăng ký, permit, Announcer| B
    GS -->|5001 nạp và lưu nhân vật| G
    GS -->|5003 5004 5005| R[S3Relay]
    R -->|5001| G
    R -->|56732| B
    G --> DB[(Kho nhân vật)]
```

Điểm dễ hiểu sai [NGUỒN N-06 §3]: đây **không** phải chuỗi nối tiếp. Client chỉ nói chuyện với Bishop lúc đăng nhập và chọn nhân vật, rồi nhận permit (IP và cổng của GS) để nối thẳng vào gs001. GS có năm đầu ra riêng: tới Bishop (56732), Goddess (5001) và ba dịch vụ của S3Relay (5003 transfer, 5004 chat, 5005 bang hội). S3Relay cũng nối Bishop và Goddess. Cổng 56732 là cổng Bishop nghe GS/Relay, không phải cổng chơi của client; 51189 chỉ là giá trị lịch sử trong tài liệu.

## 1. Bishop Announcer (báo cáo `REPORTS/N-01.md`)

Ba lựa chọn, nút Send mặc định là kiểu 3.

```mermaid
flowchart LR
    A[Bishop Announcer Send] --> B{kiểu lệnh}
    B -->|3 Notify all player| C[gói s2c_gateway_broadcast ID 60]
    B -->|2 hoặc 1 có dấu *| C
    C --> D[gs001 GatewayBoardCastProcess]
    D -->|3| E[phát tin cho mọi người chơi qua chat mở rộng]
    D -->|2 hoặc 1| F[phát cảnh báo, rồi ExitAllPlayer và ReleaseDbData]
    E --> G[client: khung chat, danh sách thông báo]
```

| Lựa chọn | Ghi/gửi đi đâu | Server (gs001) | Client |
|---|---|---|---|
| Notify all player (kiểu 3) | Không ghi cfg/DB. Nội dung ô nhập đóng vào gói ID 60 gửi một GS hoặc mọi GS [NGUỒN GameServer.cpp:1581-1628] | Phát tin cho mọi người chơi online; mã còn đặt lại `m_nGameLoop` và `m_Timer` trước khi phát (tác động chưa đo) [NGUỒN KSOServer.cpp:4276-4345] | Nhận qua gói chat mở rộng (ID 251, tiểu gói 33) vào khung chat; có nhánh đưa vào danh sách thông báo tùy kênh và nhãn bản địa. Mã không cho thấy banner giữa màn hình [NGUỒN KProtocolProcess.cpp:4303-4312; Kuiplayerfun.cpp:3338-3363] |
| Notify game server to close safely * (kiểu 2) | Cùng đường, có cờ lưu Pai Shop | Phát cảnh báo, **đưa toàn bộ người chơi thoát** và giải phóng dữ liệu DB. Mã không thấy lệnh dừng tiến trình, nên chữ "close safely" không chứng minh GS tự tắt [NGUỒN KSOServer.cpp:4312-4332] | Nhận tin rồi bị ngắt; có kịp thấy tin trước khi ngắt hay không: chưa kiểm |
| Notify and warning all player to quit * (kiểu 1) | Như trên | Gần như y hệt kiểu 2 [NGUỒN KSOServer.cpp:4290-4310] | Như trên |

[TÀI LIỆU] #161: bấm Notify all player một câu thử không lỗi và gs001 vẫn chạy; chưa ai xác nhận người chơi thật nhận được tin. Hai kiểu có dấu * chưa bấm bao giờ và không nên bấm khi chưa có người duyệt vì chúng đuổi người chơi.

## 2. Bishop: lọc tài khoản, VIP, cấm IP, giới hạn mở nhiều client (báo cáo `REPORTS/N-02.md`)

Các danh sách này chặn **sau** khi PaySys xác thực xong và **trước** khi lấy danh sách nhân vật. Chúng không ngăn kết nối TCP và không tránh lượt hỏi PaySys [NGUỒN GamePlayer.cpp:734-738, 1016-1043].

```mermaid
flowchart TD
    C[Client gửi c2s_login 65] --> V{kiểm phiên bản}
    V --> P[Bishop hỏi PaySys]
    P --> R[PaySys trả kết quả]
    R --> VIP[VIP: bật mà không khớp thì ra mã 7]
    VIP --> ACC[cấm tài khoản: khớp thì ra mã 11]
    ACC --> IP[cấm IP: khớp thì ra mã 9]
    IP -->|mã khác 0| X[Bishop trả lỗi, dừng đăng nhập, báo PaySys đăng xuất]
    IP -->|mã 0| L[lấy danh sách nhân vật từ Goddess]
```

| Nút/ô | Ghi vào đâu | Hiệu quả server | Client thấy gì |
|---|---|---|---|
| Filter account list | `accforbitlist.cfg` khi bấm nút nhỏ "live" (= Save), ngoài ra chỉ nằm trên màn hình [TÀI LIỆU #162] | Khớp **chuỗi con** (strstr, phân biệt hoa thường), không phải so chính xác hay dải IP [NGUỒN GamePlayer.cpp:1194-1207] | Mã 11 (đóng băng tài khoản), về màn nhập tài khoản [NGUỒN Klogin.cpp:973-977] |
| VIP | `acclist_vip.cfg` | Bật mà tài khoản không có trong danh sách thì bị loại | Mã 7 "không trong danh sách", về màn nhập [NGUỒN Klogin.cpp:995-999] |
| Filter IP list | `ipforbitlist.cfg` (trên VM thử chưa có tệp này) | Khớp chuỗi con trên IP | Mã 9 không có nhánh riêng, rơi vào lỗi đăng nhập chung (G_LOGIN_FAIL); chưa rõ người chơi phải thao tác lại hay chờ [NGUỒN Klogin.cpp:1001-1009] |
| Giới hạn mở nhiều client | Chỉ gửi số `nForbitopennum`; đoạn đếm phía Bishop bị comment, đoạn nhận phía client rỗng | Hiện gần như không có tác dụng chặn [NGUỒN GamePlayer.cpp:1324-1377; Klogin.cpp:923-925] | Không thấy gì |
| Unrestricted | Cửa riêng sau khi chọn nhân vật | Từ chối thì gói 52 báo bận | Hiện G_NEW_PLAYER_INVALID_BUSY, không dùng mã 7/9/11 [NGUỒN GameServer.cpp:1045-1063; KuiSelPlayer_new.cpp:993-1004] |

Mã lỗi thật là phép OR giữa kết quả PaySys và mã lọc, không phải hằng số riêng (ví dụ thành công 1 OR 8 = 9). Chưa thử cái nào trên client thật; câu chữ tiếng Việt cuối cùng nằm trong bảng ngôn ngữ nạp động, chưa kiểm.

## 3. Bishop: Birth role setting, Reset character rebirth m, Send to client to detect ve

Mỗi ô trả lời 4 câu (ghi vào đâu / exe nào nhận / tác động server / tác động client). Chi tiết và số dòng nguồn ở `REPORTS/N-03.md`.

| Ô | Ghi vào đâu | Server | Client |
|---|---|---|---|
| **turn on** (checkbox Birth) | Chỉ bộ nhớ Bishop; Save settings không ghi nó vào `Bishop.cfg` (khớp #162). Khi có yêu cầu tạo nhân vật, Bishop đọc checkbox rồi mới xét ba ô số. | Chỉ áp cho nhân vật **mới tạo**, không sửa nhân vật cũ. Tắt chỉ bỏ nhánh gán. | Không có thông báo riêng; client chỉ thấy tạo thành công/thất bại (gói 157). |
| **Cap** | Ô số → hồ sơ mẫu trong RAM Bishop: nếu > 0 thì cấp = L, điểm tiềm năng chưa cộng = (L−1)×5, điểm kỹ năng chưa cộng = L−1. | Là gán cấp/điểm **khởi đầu**, không tính lại kinh nghiệm hay máu/nội lực theo cấp. 0/rỗng không có nghĩa về cấp 1. | GS đồng bộ gói 68 (cấp, điểm), client nạp thẳng; không có thông báo "tăng cấp". |
| **Silver** | Gán thẳng bạc cầm theo của hồ sơ (nếu > 0). | Hồ sơ được Goddess lưu nên bạc có đường vào kho dữ liệu; "không ghi cfg" không có nghĩa là bạc chỉ tạm thời. Không nhân hệ số (không phải "vạn"). | Gói 68 mang bạc cầm theo; túi hiện số nguyên. |
| **gold** | Gán thẳng trường vàng/xu của hồ sơ (nếu > 0). | Giá trị khởi đầu trong hồ sơ, khác với Add Money của Goddess. | Gói 68 mang số xu; túi hiện số nguyên. |

**Giá trị mẫu dùng chung (giả thuyết từ mã, chưa thử):** Bishop giữ 10 mẫu nhân vật đọc từ `settings/player/newplayerini%02d.ini` và nhánh Birth sửa **chính mẫu đó**. Vì vậy sau một lần gán Cap/Silver/gold dương, nhân vật tạo tiếp cùng loại có thể thừa kế dù đã bỏ tích hoặc xóa ô, kể cả khi lần tạo trước bị Goddess từ chối. Hoàn tác ở #162 chỉ là hoàn tác giao diện. Chưa thử nạp lại mẫu hay khởi động lại Bishop.

**Reset character rebirth m (`TwoRevivePos`):** ghi vào `Bishop.cfg [Network] TwoRevivePos` khi Save settings; lúc xác thực tài khoản Bishop chụp giá trị vào phiên. Chỉ dùng để chọn gs001 dự phòng khi không tìm được gs cho bản đồ ưu tiên. Mã không gán nó vào điểm hồi sinh trong hồ sơ, nên không đủ căn cứ hứa nó đưa người chơi tới đúng bản đồ. Không có gói riêng cho client; nếu không định tuyến được thì permit báo không cho phép (mã 2 là dấu lỗi, không phải cổng).

**Send to client to detect ve (`BishopVer`):** ghi vào `Bishop.cfg [Network] BishopVer`; Bishop gửi nó cho client trong `s2c_login` (gói 65). Client đọc `Settings/Ver/Xfsverjx.ini` (`[CilentVer] ver`) rồi so. Thiếu file hoặc lệch phiên bản thì client báo lỗi phiên bản và thoát/không nối gs001. Không đổi cấp, tiền hay hồ sơ. Giả thuyết: khi tạo nhân vật mới có thể đã lưu rồi mới bị chặn ở bước permit.

```mermaid
sequenceDiagram
  participant C as Client
  participant B as Bishop
  participant G as Goddess
  participant S as gs001
  C->>B: tạo nhân vật (tên, giới, ngũ hành, nơi sinh)
  B->>B: chọn mẫu, gán Birth nếu bật
  B->>G: lưu hồ sơ (gói 11)
  G-->>B: kết quả lưu
  B-->>C: tạo thành công/thất bại (gói 157)
  B->>S: gửi hồ sơ, xin nhận nhân vật
  S-->>B: permit
  B-->>C: permit (gói 52), client kiểm phiên bản rồi nối gs001
  S-->>C: đồng bộ cấp/điểm/tiền (gói 68)
```

Giới hạn: chưa thử tạo nhân vật có Birth bật, chưa đo số dư thật sau script đăng nhập (`script/system/online.lua` chưa đọc), nguồn có thể không khớp exe đang chạy. [NGUỒN N-03]

## 4. Goddess: Max char create, MAX Player, danh sách nhân vật (báo cáo `REPORTS/N-04.md`)

```mermaid
flowchart LR
    CL[Client Klogin hoặc màn chọn nhân vật] -->|yêu cầu role list| B[Bishop]
    B -->|c2s_roleserver_getrolelist| G[Goddess ClientNode]
    G --> D[DB hoặc SQL]
    D --> G
    G -->|s2c_roleserver_getrolelist_result| B
    B --> CL
    CFG[Goddess.cfg] -->|MaxRoleCount| G
    CFG -->|MaxPlayerCount| H[heaven.dll SetEnvironment]
```

- **Max char create (MaxRoleCount).** Ghi vào `Goddess.cfg`, nạp vào biến `g_nMaxRoleCount` rồi truyền vào lớp DB; khi tạo nhân vật mới mà số vai đã đạt ngưỡng thì Goddess từ chối và trả kết quả tạo vai về Bishop [NGUỒN Goddess.cpp:71, 1422-1426, 1521-1561; IDBRoleServer.cpp:187-189, 688-696, 812-826; ClientNode.cpp:407-461]. [TÀI LIỆU #161] đặt 3→4→3 ghi cfg đúng; **chưa tạo được nhân vật thứ 4** (cần client). Đáng chú ý: **Bishop cố định tối đa 3 vai** (`s_nRoleListCount=3`, GamePlayer.cpp:61) và client cũng kẹp về 3, nên nâng lên 4 ở Goddess chưa chắc hiện ra cho người chơi.
- **MAX Player.** Ô bị khóa (WS_DISABLED) trong giao diện; giá trị đọc từ cfg và truyền vào `heaven.dll` qua `SetEnvironment` [NGUỒN Goddess.rc:79-81; Goddess.cpp:1443-1451]. Có là giới hạn cứng hay không: chưa kiểm (chưa đọc heaven.dll).
- **Danh sách nhân vật ở màn chọn.** Goddess lọc theo tài khoản và khu (`isWaiGua == nThisServer`) và chỉ trả tên, giới tính, hệ phái, cấp; Bishop chuyển gói nguyên vẹn; client dựng màn chọn bằng `KuiSelPlayer_new` (bản cũ `KSelPlayer`) [NGUỒN IDBRoleServer.cpp:923-975; GamePlayer.cpp:1404-1505; Klogin.cpp:1033-1075].

## 5. Goddess: Add Money, EnterMap, Remove Role, Backup, Pause, Restart (báo cáo `REPORTS/N-05.md`)

Nhân vật lưu ở backend của Goddess (nhánh DB `roledb` hoặc nhánh SQL bảng role_Blob; chưa biết exe đang dùng nhánh nào). Bishop lấy danh sách và hồ sơ từ Goddess; GS gửi gói lưu về Goddess khi cần. Chi tiết ở `REPORTS/N-05.md`.

| Nút | Làm gì thật | Server | Client | Thử thật |
|---|---|---|---|---|
| **Add Money** | Chỉ nhân vật **offline**: tìm theo tên, cộng vàng (kind 0) hoặc bạc (kind 1) rồi ghi lại bản ghi DB. Nhánh online để trống nên thất bại; SQL mode không có nhánh tương đương. | Sửa DB, không đụng GS đang chạy. | Không có gói; số mới có thể thấy ở lần đăng nhập sau (chưa xác minh). | #161: +1000 bạc đọc được ở `.txt` backup. |
| **EnterMap / IDMap** | Nhân vật offline: đặt cUseRevive=1 và ghi điểm hồi sinh **cố định 53/19**; số map nhập chỉ bị kiểm > 0, không được ghi. SQL mode trả 1 mà không cập nhật. | Chỉ đổi dữ liệu hồi sinh trong DB, không đổi map nhân vật đang online. | Không có gói; vị trí khi vào lại chưa xác minh. | #162: không thử. |
| **Remove Role** | Xóa **hàng loạt** mọi nhân vật có cấp thấp hơn ngưỡng nhập; không có xác nhận. | Mất dữ liệu ngay trong backend đang mở. | Nhân vật biến khỏi danh sách; người đang online chưa biết. | KHÔNG bấm. |
| **Manual backup** | Tạo thư mục `database\<giờ>` với `.bak` và `.txt` (DB mode); SQL mode copy sang bảng backup. | Chỉ đọc/copy. | Không có. | #161 đã tạo tệp. |
| **Backup phần đồ** | Cần chọn một mục cụ thể; mã chỉ làm việc nếu có bảng SQL rồi vẫn trả true. | Chỉ đọc. | Không có. | #162: "All" báo lỗi chọn mục; chọn Body không thấy tệp mới. |
| **Pause** | Tạm dừng/tiếp tục **chỉ timer backup tự động**, không phải pause gs001. | Không ghi nhân vật. | Không có. | #162: đổi nhãn Pause↔Resume, không lỗi. |
| **Restart / tắt Goddess** | Restart đóng rồi mở lại giao diện DB bên trong Goddess (không phải thoát hẳn). Tắt process thì phiên Bishop→Goddess đóng và Bishop không tự nối lại; cần **Reconnect DB**. | GS có nhánh thử nối lại DB; khi mất DB thì lưu nhân vật thất bại. | Không gói từ Goddess; người đăng nhập lúc role list chưa sẵn sàng sẽ timeout rồi về màn đăng nhập (giả thuyết từ mã). | #161: tắt/mở lại làm Bishop mất DB, Reconnect DB xong gs001 báo "reconnect OK". #162: Restart không hồi phục sau 90 giây (hai kết quả khác nhau, không gộp). |

```mermaid
flowchart LR
  GS[gs001] -- gói lưu nhân vật --> GD[Goddess]
  B[Bishop] -- lấy danh sách / hồ sơ --> GD
  GD --> DB[(roledb hoặc role_Blob)]
  AM[Add Money / EnterMap / Remove Role] -- sửa trực tiếp --> DB
  BK[Manual backup] -- đọc --> DB
```

Chưa kiểm: tác động lên người đang chơi, GS ghi đè lại nhân vật sau khi bị Remove/Add offline, SQL mode, và việc source có khớp binary. [NGUỒN N-05; TÀI LIỆU #161/#162]

## 6. Liên kết tổng và thứ tự bật/tắt (báo cáo `REPORTS/N-06.md`)

Sơ đồ ở mục 0; bảng 14 luồng (L01–L14) cùng cổng nằm ở N-06 §3.

- **Bật** [GIẢ THUYẾT]: thứ tự đã dùng SQL → PaySys → Goddess → S3Relay → Bishop → GS vẫn là đường đã chạy được. Nên chờ từng thành phần thật sự sẵn sàng (có listener đúng cổng, nối được phụ thuộc) chứ không chỉ nhìn cửa sổ; SvrFPS 18/18 hay Online=0 không thay cho các điều kiện này.
- **Tắt** [GIẢ THUYẾT]: giữ Goddess, Bishop, PaySys và Relay sống cho tới khi GS lưu xong và đọc lại được nhân vật; đóng GS trước, rồi Relay, Bishop, Goddess (sau khi không còn writer và đã kiểm backup), PaySys, SQL. Chưa có nút nào được chứng minh là "dừng GS an toàn": hai kiểu Announcer dấu * gọi `ExitAllPlayer`/`ReleaseDbData` nhưng `SetRunningStatus(FALSE)` bị comment [NGUỒN KSOServer.cpp:4290-4332].
- **Goddess bị khởi lại ngoài kế hoạch:** ghi sự cố, bấm Reconnect DB ở Bishop (đừng bấm Reconnect Pay), rồi kiểm riêng GS, Relay và client. Close Goddess chờ luồng 50 giây rồi có nhánh `TerminateThread` [NGUỒN Goddess.cpp:1493-1501].
- **S3Relay root cổng 7777:** có dự án `S3RelayServer` trong mã nguồn (đọc `relay_setup.ini [Local] port`, mặc định 7777) nhưng chưa biết exe triển khai có dùng không; vẫn **không chạy** `S3RelayServer.exe` [NGUỒN S3RELAYSERVER/main.cpp:100-109,186-197].

## Điều chưa kiểm tra (tất cả cần client thật hoặc đối chiếu binary)

1. Mã nguồn khớp exe/APK đang chạy hay không (chưa đối chiếu lần nào).
2. Tin Notify all player có hiện ra ở client và hiện ở đâu.
3. Mã lỗi/thông báo thật người chơi thấy khi bị lọc tài khoản/VIP/IP, nhất là mã 9.
4. Tạo nhân vật thứ 4 khi MaxRoleCount=4 (Bishop và client cùng kẹp ở 3).
5. Birth role setting áp lên nhân vật mới tạo thế nào ở runtime, và việc mẫu RAM bị thừa kế cho lần tạo sau (mới là giả thuyết từ mã).
6. Tác động của Add Money/EnterMap lên người đang chơi; dữ liệu được nạp thế nào lúc đăng nhập lại (chỉ có kết quả từ mã và #161/#162).
7. Chuỗi tắt an toàn GS và cổng root 7777.

## Muốn xác nhận trên client thật thì cần gì

**Cần**: LDPlayer với APK đã có (ghi phiên bản và SHA-256 của APK, của Bishop/Goddess/gs001), VM thử JX-Test-36 đã dựng, hai tài khoản chuyên dùng để thử (bí danh TEST-A và TEST-B; mật khẩu do chủ cấp lúc chạy, không ghi vào tệp nào), sao lưu cfg và DB trước từng ca, và duyệt riêng của chủ cho mỗi ca đổi trạng thái. Không dùng tài khoản thật. Ca nào cũng chỉ trên VM thử, không đụng Main VM.

| Ca | Thao tác | Quan sát | Rủi ro |
|---|---|---|---|
| C01 | TEST-A đăng nhập, chọn khu, chọn nhân vật, vào thế giới (chưa đổi gì) | 5 mốc giao diện, nối 56722 rồi permit tới GS | thấp |
| C02 | Đăng nhập sai mật khẩu, thiếu quyền chơi, khác phiên bản | mã lỗi PaySys/Bishop và câu báo ở client | thấp |
| C04 | Notify all player một câu ASCII, hai client online | có hiện, hiện ở đâu, có ngắt không | thấp; nhánh này reset GameLoop |
| C05 | Notify all player câu tiếng Việt có dấu | chữ có vỡ không | thấp |
| L1 | Đưa `zz_test_acc` vào Filter account rồi đăng nhập bằng đúng tên đó | mã 11 và câu báo thật; bỏ ra thì vào lại được | thấp, hoàn tác bằng nút "live" |
| L2 | Tương tự cho VIP (bật rồi dùng tài khoản ngoài danh sách) và IP | mã 7 và mã 9 | trung bình: bật nhầm VIP sẽ khóa mọi tài khoản ngoài danh sách |
| M1 | MaxRoleCount=4, tạo nhân vật thứ 4 từ client | Bishop/client có cho tạo không | trung bình: tạo thêm dữ liệu nhân vật; đặt lại 3 và xóa nhân vật thử |
| B1 | Birth role setting bật, rồi tạo nhân vật mới | cấp/bạc/vàng của nhân vật mới (chờ N-03) | trung bình |
| A1 | Add Money cho nhân vật offline rồi đăng nhập bằng client | số bạc thấy ở client | trung bình, ghi trước/sau |
| S1 | Thoát, lưu, vào lại; sau đó mới thử Goddess mất kết nối rồi Reconnect DB | dữ liệu đọc lại đúng | cao hơn; phải làm sau S1 đạt và có sao lưu |
| X1 | Hai kiểu Announcer dấu * | thứ tự báo, đuổi người chơi, lưu | **rất cao**: đuổi người chơi, giải phóng DB; chỉ làm khi có sao lưu và duyệt riêng |

Danh sách đầy đủ 13 ca (C01–C13) kèm tiêu chí đạt nằm ở N-06 §7. **Không ca nào đã chạy; chờ đại vương duyệt.**
