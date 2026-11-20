# KT-03C — Bản đồ chuỗi quái/NPC xuất hiện trên màn

Cập nhật 20/11/2026. Bản đồ đọc tĩnh; không thay kết luận cũ và tách nguồn gốc khỏi overlay B-02.

liên quan: JX1_OPS/REPORTS/A-05-diem-tuong-tac-gs001.md; JX1_OPS/REPORTS/B-02-loc-hien-thi.md; JX1_OPS/REPORTS/B-02-tom-tat-diff.md; JX1_OPS/HOP-THU/A-B.md; JX1_OPS/DESIGN/B-01-LOC-HIEN-THI.md

## Tóm tắt bằng lời thường

Người chơi chọn đi, client gửi tọa độ cho server. Server phát các gói đồng bộ ngắn theo chu kỳ vùng. Nếu client nhận gói ngắn có ID NPC chưa tồn tại cục bộ, client yêu cầu dữ liệu đầy đủ; server gửi NPC_SYNC; client tạo NPC rồi renderer vẽ. Việc quái hiện muộn có thể xảy ra ở nhiều chặng, chưa xác định nguyên nhân runtime của một map/quái cụ thể.

## Sơ đồ chính

~~~mermaid
flowchart LR
 A[Người chơi đi] --> B[Client SendClientCmdWalk]
 B -->|c2s_npcwalk| C[Server NpcWalkCommand]
 D[Lua AddNpc nếu script tạo] --> E[g_NpcSetting / AddServerNpcA]
 E --> F[Thực thể NPC]
 C --> F
 F --> G[NormalSync / BroadCast]
 G -->|s2c_syncnpcmin| H[Client SyncNpcMin]
 H --> I{Đã có ID?}
 I -->|Chưa| J[c2s_requestnpc]
 J --> K[NpcRequestCommand / KNpcSet SyncNpc]
 K -->|NPC_SYNC| L[Client SyncNpc / AddServerNpcA]
 I -->|Có| M[KNpc Paint / DataRes Draw]
 L --> M
~~~

## Chuỗi theo thứ tự game

1. **Dữ liệu NPC — ĐÃ ĐỌC MÃ.** Server nạp mẫu g_NpcSetting và gọi InitNpcSetting: src18/KCore.cpp:626,630. LuaAddNpc ánh xạ ID/tên mẫu và gọi NpcSet.AddServerNpcA: src18/ScriptFuns.cpp:12615-12655; KNpc.cpp:7198-7217 đọc trường mẫu NpcResType/AIMode/ActiveRadius. Đây là đường API tổng quát; chưa xác định script hoặc hàng dữ liệu của quái cụ thể.
2. **Người chơi đi — ĐÃ ĐỌC MÃ.** Client gọi SendClientCmdWalk: qh9A/CoreShell.cpp:5091-5100; dựng NPC_WALK_COMMAND/c2s_npcwalk và gửi: KProtocol.cpp:295-309. Server dispatch tới NpcWalkCommand: src18/KProtocolProcess.cpp:213,5436-5450.
3. **Server phát sync ngắn — ĐÃ ĐỌC MÃ.** KRegion::NewRegActivate phát NormalSync theo m_nNpcSyncCounter & 1 khi IsActiveAll: src18/KRegion.cpp:1127-1148. JxHalfActivate gọi NormalSync khi NPC vừa di chuyển: cùng file:1101-1115. KNpc::NormalSync dựng s2c_syncnpcmin và phát vùng hiện tại + 8 vùng nối: src18/KNpc.cpp:8177-8195,8321-8343.
4. **Vùng nhận — ĐÃ ĐỌC MÃ.** SendDataToNearRegion phát qua 9 vùng với offset POff: src18/KNpc.cpp:14394-14427. BroadCast kiểm player hợp lệ, kết nối, trạng thái sleep: KRegion.cpp:2244-2300. MAX_SYNC_RANGE=32 có guard khoảng cách đang comment: cùng file:2250,2287-2289.
5. **Client nhận sync ngắn — ĐÃ ĐỌC MÃ.** Dispatch s2c_syncnpcmin tới SyncNpcMin: qh9A/KProtocolProcess.cpp:57-59. SyncNpcMin bỏ gói nếu region không hợp lệ hoặc chênh quá CORRECT_SYNC_RANGE theo từng trục: cùng file:2414-2447; hằng số 30 tại qh9A/KRegion.h:24. Nếu ID chưa có và chưa bị khóa request, gửi request NPC: cùng file:2448-2453.
6. **Yêu cầu dữ liệu đầy đủ — ĐÃ ĐỌC MÃ.** SendClientCmdRequestNpc gửi NPC_REQUEST_COMMAND/c2s_requestnpc: qh9A/KProtocol.cpp:346-354. Server dispatch và gọi NpcRequestCommand: src18/KProtocolProcess.cpp:211,5421-5425; KNpcSet::SyncNpc gửi s2c_requestnpcfail nếu không tìm thấy ID, nếu có thì gọi KNpc::SendSyncData: src18/KNpcSet.cpp:1272-1289; KNpc.cpp:7954-8019.
7. **Tạo và vẽ — ĐÃ ĐỌC MÃ.** Client SyncNpc thêm ID mới qua AddServerNpcA: qh9A/KProtocolProcess.cpp:2159-2180. KgameWorld tạo ParentNode_npc và gọi ScenePlace.Paint: qh9A/gamescene/KgameWorld.cpp:618-624,5861; KScenePlaceC vẽ object tree: KScenePlaceC.cpp:1667-1681; KNpc::Paint gọi m_DataRes.Draw: qh9A/gamecore/KNpc.cpp:6028-6098. Nếu gói đã về mà hình chưa thấy, kiểm thêm hide flags trong KNpc::Paint: cùng file:6064-6088.

## Tham số tầm nhìn, khoảng cách và chu kỳ

| Tham số | Giá trị | Ý nghĩa / nơi đổi | Nguồn |
|---|---:|---|---|
| CORRECT_SYNC_RANGE (client) | 30 | Check từng trục trong SyncNpcMin; không phải bán kính tròn áp dụng cho mọi gói. | qh9A/KRegion.h:24; KProtocolProcess.cpp:2436-2447 |
| MAX_SYNC_RANGE (server) | 32 | Guard khoảng cách đang comment; đổi macro riêng không đổi hành vi hiện tại. | src18/KRegion.cpp:2250,2287-2289 |
| Vùng broadcast | vùng hiện tại + 8 vùng nối; POff dùng 16/32 | Chọn region, không phải một khoảng cách world-unit cố định. | src18/KNpc.cpp:8321-8343,14394-14427 |
| MAX_BROADCAST_COUNT | 100 | Chỉ caller truyền macro bị giới hạn; SendDataToNearRegion dùng 100, còn NormalSync dùng MAX_PLAYER. | src18/KRegion.h:15; KNpc.cpp:8334,14414 |
| Chu kỳ NormalSync | m_nNpcSyncCounter & 1, vùng IsActiveAll | Phụ thuộc lượt kích hoạt và số NPC; không suy ra mili giây cố định. | src18/KRegion.cpp:1101-1115,1127-1148 |
| Khóa request NPC | >100 m_dwCurrentTime | Xóa request cũ để lần sync sau có thể yêu cầu lại; không phải chờ trước request đầu. | qh9A/KNpcSet.cpp:1018-1032,1400-1415 |
| Clock client | tăng ở mỗi KSubWorld::Activate | Comment ghi 18 frame/giây; 100 bước ≈5,6 giây nếu nhịp thật là 18/s. Phép quy đổi giả định, chưa đo runtime; HOP-THU/A-B.md:255 ghi ước tính lịch sử 3–6 giây. | qh9A/KSubWorld.cpp:146-163; HOP-THU/A-B.md:252-261 |
| B-02 MaxVisible / Enabled | 60 / 0 theo tài liệu | Trần người chơi trong group visibility/công tắc; không phải khoảng cách hiện quái. | REPORTS/B-02-loc-hien-thi.md:34; B-02-tom-tat-diff.md:7,25 |

Không chỉnh các giá trị từ đọc tĩnh. Muốn tối ưu, đo P3 → c2s_requestnpc → NPC_SYNC/P1 và nhịp client/server trước.

## Overlay dự án và so sánh với gốc

- B-02 ghi overlay visibility ở KRegion::BroadCast, KNpc::SendSyncData, KNpcSet::SyncNpc, KSubWorld::SendSyncData và KVisibility.cpp/.h: REPORTS/B-02-loc-hien-thi.md:13-27; B-02-tom-tat-diff.md:12-16. Config mẫu Sources/Settings/visibility.ini có Enabled=0; báo cáo nói thiếu config thì đi đường gốc và chưa deploy trong task đó: B-02-loc-hien-thi.md:29-38,78-80.
- Root src18 đọc trực tiếp không có KVisibility.cpp/.h hoặc Sources/Settings/visibility.ini; không gán overlay B-02 cho root này hay cho runtime.
- qh9A có log P1/P3 quanh gói sync tại KProtocolProcess.cpp:2163,2417. Không có baseline canonical cùng revision để kết luận các khác biệt khác.
- qhcuonghoa.lua thuộc luồng cường hóa vật phẩm trong HOP-THU/A-B.md:457-479, không thuộc chuỗi NPC.

## Điểm dễ làm sai

- MAX_SYNC_RANGE=32 đang comment; CORRECT_SYNC_RANGE=30 là check client thấy trong SyncNpcMin.
- Giá trị 100 dọn khóa request; request đầu được gửi ngay khi client gặp sync ngắn của ID lạ.
- MAX_BROADCAST_COUNT=100 không áp mọi gói; NormalSync dùng MAX_PLAYER.
- Không suy mọi quái được tạo bởi Lua AddNpc; chưa xác định script/hàng dữ liệu của NPC cụ thể.
- Không kết luận B-02 gây hiện tượng khi chưa biết nhánh và config; tài liệu ghi Enabled mặc định 0.
- Một lần đọc mã không chứng minh binary/config đang chạy. Nếu NPC_SYNC đã về mà không thấy hình, tách lỗi tạo vùng và hide flags khỏi lỗi packet.

## KỊCH BẢN KIỂM ĐỘNG — để A/bot chạy sau

**Đồ/người cần:** hai nhân vật test A/B, một quái đứng yên, một quái đang di chuyển, map có tọa độ/region đã ghi; ghi build ID và config. Không dùng tài khoản/log thật.

**Thao tác:** A đứng cùng region, chờ NormalSync rồi đi qua biên sang region nối. Lặp riêng với quái đứng và di chuyển. Nếu có build B-02 được duyệt, tách hai lượt Enabled=0/1 và giữ tọa độ/nhân vật như nhau.

**Số đọc ở đâu:** timestamp, ID, tọa độ P3/P1; gói c2s_npcwalk, s2c_syncnpcmin, c2s_requestnpc, NPC_SYNC, s2c_requestnpcfail; thời điểm SearchID thấy ID; hide flags khi vẽ. Ghi riêng build/config/region và khoảng cách từng trục.

**Kỳ vọng:** sync ngắn của ID lạ trong ngưỡng 30 mỗi trục tạo request; server còn ID thì trả NPC_SYNC; client thêm ID trước khi vẽ. Timestamp tách được chờ NormalSync, gate client, request/response và render. Kịch bản chưa chạy trong KT-03C.

## Giải mã tên

| Tên gốc | Mã hóa | Chữ đúng | Nguồn |
|---|---|---|---|
| Không có tên riêng trong phạm vi; NPC/quái là danh từ chung. | — | — | Nội dung tài liệu này |

## Sắp theo cấu trúc game

Theo luồng: dữ liệu/mẫu NPC → Lua AddNpc (nếu script tạo) → thực thể trong vùng server → NormalSync/BroadCast → SyncNpcMin phía client → request dữ liệu đầy đủ theo ID → AddServerNpcA/region client → KNpc::Paint/DataRes.Draw. Task không chỉ định map, ID, phái, nhánh hoạt động hay hàng dữ liệu cụ thể.

## Đã xác minh

- Đã đọc trực tiếp file/hàm nêu trên trên root qh9A client và src18 server; số dòng thuộc các root đó.
- Client check 30 theo từng trục; server guard 32 hiện comment.
- Đã lập kịch bản đợt 2, chưa chạy.

## Chưa xác minh

- Map/NPC cụ thể, Lua spawn script và hàng mẫu thực tế; task không chỉ định ID/map.
- Config visibility.ini trên máy chạy, nhánh đang cài, packet trace và thời gian hiện thực.
- Diff byte-for-byte qh9A với canonical client cùng revision; không có baseline trong nguồn task.
- Không build, không chạy game/exe, không VM và không mạng.

## Đề xuất tối ưu

Giữ nguyên các hằng số tới khi đo P3/request/NPC_SYNC/P1. Nếu request không phát, kiểm 30/region/khóa request; nếu response thiếu, tách server lookup và B-02; nếu NPC_SYNC đã về, kiểm tạo region và hide flags. So sánh Enabled=0/1 chỉ trong môi trường test được duyệt.

Kỹ năng đã dùng: jx1-knowledge, jx1-read-server, jx1-read-client, jx1-parameters.
