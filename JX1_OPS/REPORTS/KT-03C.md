TÓM TẮT 5 DÒNG
1. [NGUỒN] DONE cho bản đồ chuỗi tĩnh KT-03C; giữ nguyên kết luận các báo cáo cũ.
2. [NGUỒN] Đã nối client → c2s_npcwalk → server NormalSync/BroadCast → c2s_requestnpc → NPC_SYNC → tạo/vẽ NPC.
3. [NGUỒN] Bản đồ bàn giao: JX1_OPS/HIEU-GAME/04-quai-npc-ban-do/BAN-DO-QUAI-HIEN-THI.md.
4. [CHƯA KIỂM] Chưa chạy game/build/VM; chưa đo nguyên nhân runtime; Graphify không trả kết quả symbol ổn định.
5. [CHƯA KIỂM] Không build/chạy exe/game/VM hay commit; .nhip bị Access denied; A/bot chạy kịch bản sau.

# KT-03C — Chuỗi quái/NPC xuất hiện trên màn

Loại: tổng hợp
Chủ đề: Bản đồ tĩnh từ thao tác di chuyển đến gói NPC đầy đủ và render client
Từ khóa: quái, NPC, NormalSync, SyncNpcMin, c2s_requestnpc, tầm nhìn, KRegion, visibility
Trạng thái: DONE — hoàn tất bản đồ tĩnh; runtime chưa kiểm
Độ phủ: đã phủ 5 trên tổng 5 đầu ra của task
Liên quan: A-05-diem-tuong-tac-gs001.md; B-01-LOC-HIEN-THI.md; B-02-loc-hien-thi.md; B-02-tom-tat-diff.md; B-03-test-visibility.md; HOP-THU/A-B.md
Cần tôi quyết định: không

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

## Phạm vi và độ phủ

| Hạng mục mục tiêu | Kết quả | Bằng chứng / giới hạn |
|---|---|---|
| Tóm tắt dễ hiểu | Đã phủ | Bản đồ: mục Tóm tắt bằng lời thường |
| Chuỗi player → client → packet → server → Lua/data → hiển thị | Đã phủ ở mức luồng chung | KCore.cpp:626,630; ScriptFuns.cpp:12615-12655; CoreShell.cpp:5091-5100; KProtocolProcess.cpp:213,5436-5450,2414-2453,2159-2180; KNpc.cpp:8177-8343,6028-6098 |
| Overlay dự án và so với đường gốc | Đã phủ theo B-02; diff trực tiếp có giới hạn | B-02 reports ghi file/điểm móc; src18 không có KVisibility.cpp/.h hoặc Sources/Settings/visibility.ini; không có canonical baseline cùng revision để diff qh9A |
| Tham số và điểm dễ sai | Đã phủ | CORRECT_SYNC_RANGE=30 đang dùng; MAX_SYNC_RANGE=32 bị comment; timeout 100; vùng 9 ô và nhịp đồng bộ |
| Kịch bản kiểm động đợt 2 | Đã chuẩn bị, chưa chạy | Bản đồ có người/vật cần, thao tác, số đọc và kỳ vọng; A/bot chạy sau |

## Đã tra đồ thị

- Client: graphify.exe explain "KProtocolProcess::SyncNpc" tại root D:\JX-build\qh9A\Classes trả “No node matching”. Đồ thị chỉ định vị, không dùng làm bằng chứng.
- Lệnh graphify.exe query "KNpcSet NormalSync SyncNpc" --root "D:\JX-build\src18" chạy từ worktree trả lỗi không tìm thấy D:\JX-wt\KT-03C\graphify-out\graph.json.
- Server: graphify.exe query "KNpcSet NormalSync SyncNpc" tại root D:\JX-build\src18 không có output sau khoảng chờ và đã dừng; graphify.exe explain ".KRegion::BroadCast()" cũng không trả output và đã dừng.
- Đã kiểm trực tiếp file/hàm tại qh9A/Classes và src18/jxOnline/gameserver/Sources.
- JX1_OPS/STATE/DO-THI.md ghi đồ thị src18 cũ/lệch với worktree QH-B035; số dòng dưới đây đã đối chiếu lại trên root task chỉ định.

## Đã đọc kiến thức

Đã đọc MUC-LUC-TRI-THUC.md; DESIGN/B-01-LOC-HIEN-THI.md; MA-NGUON/ban-do-server.md, ban-do-client.md, goi-tin.md; CONTEXT-PACK/GS001-MAP.md; TOOLS/CONG-CU.md; REPORTS/A-05-diem-tuong-tac-gs001.md, B-02-loc-hien-thi.md, B-02-tom-tat-diff.md, B-03-test-visibility.md, B-04a-bo-do-tick-bang-thong.md; phần liên quan cuối HOP-THU/A-B.md. Mục lục và Graphify chỉ để định vị.

## Tóm tắt kỹ thuật

- Client gửi NPC_WALK_COMMAND/c2s_npcwalk qua SendClientCmdWalk: qh9A/CoreShell.cpp:5091-5100; KProtocol.cpp:295-309. Server dispatch tới NpcWalkCommand: src18/KProtocolProcess.cpp:213,5436-5450.
- Vùng đang hoạt động phân bổ NormalSync theo m_nNpcSyncCounter & 1; nhánh NPC vừa đi gọi NormalSync ở JxHalfActivate: src18/KRegion.cpp:1101-1115,1127-1148. KNpc::NormalSync dựng s2c_syncnpcmin và phát region hiện tại + 8 region nối: src18/KNpc.cpp:8177-8195,8321-8343.
- BroadCast kiểm tra player, kết nối và trạng thái sleep; khoảng cách MAX_SYNC_RANGE=32 đang comment: src18/KRegion.cpp:2244-2300. SendDataToNearRegion phát qua 9 region: KNpc.cpp:14394-14427.
- Client lọc theo CORRECT_SYNC_RANGE=30 từng trục, rồi nếu ID chưa có gửi c2s_requestnpc: qh9A/KRegion.h:24; KProtocolProcess.cpp:2414-2453.
- Server nhận request, gọi KNpcSet::SyncNpc; ID có thì gửi KNpc::SendSyncData, ID thiếu thì s2c_requestnpcfail: src18/KProtocolProcess.cpp:211,5421-5425; KNpcSet.cpp:1272-1289; KNpc.cpp:7954-8019.
- Client SyncNpc tạo ID mới bằng AddServerNpcA: qh9A/KProtocolProcess.cpp:2159-2180. Đường vẽ dùng KNpc::Paint → m_DataRes.Draw; scene vẽ object tree: qh9A/gamecore/KNpc.cpp:6028-6098; qh9A/gamescene/KScenePlaceC.cpp:1667-1681.
- KCore nạp g_NpcSetting; LuaAddNpc ánh xạ mẫu và gọi AddServerNpcA: src18/KCore.cpp:626,630; ScriptFuns.cpp:12615-12655. Chưa biết Lua/data row của quái cụ thể do task không nêu map/ID.

## Thay đổi dự án và đối chiếu nguồn

B-02-loc-hien-thi.md ghi các điểm overlay ở KRegion::BroadCast, KSubWorld::SendSyncData, KNpc::SendSyncData, KNpcSet::SyncNpc, KObj, ScriptFuns và KVisibility.cpp/.h: dòng 13-27; B-02-tom-tat-diff.md mô tả cổng Enabled và các điểm móc: dòng 4-25. Tài liệu nói Enabled=0 hoặc thiếu file thì đi đường gốc, file config dành cho lần triển khai sau, và chưa chạy/test binary: B-02-loc-hien-thi.md:29-38,78-80.

Root src18 được đọc trực tiếp không có KVisibility.cpp/.h hoặc Sources/Settings/visibility.ini nên không gán overlay B-02 cho root này/runtime. qh9A có trace P1/P3 tại KProtocolProcess.cpp:2163,2417; chưa có baseline canonical cùng revision để kết luận các khác biệt khác. qhcuonghoa.lua nằm trong luồng cường hóa vật phẩm ở HOP-THU/A-B.md:457-479, không thuộc chuỗi NPC.

## Mục sổ thông số

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---:|---|---|---|---|
| Client sync | CORRECT_SYNC_RANGE | qh9A/KRegion.h:24; KProtocolProcess.cpp:2436-2447 | 30 | ô theo trục | Bỏ sync ngắn của NPC lạ ngoài ngưỡng | CẨN THẬN — xác nhận hệ tọa độ/caller | Đọc tĩnh |
| Server broadcast | MAX_SYNC_RANGE | src18/KRegion.cpp:2250,2287-2289 | 32 | ô theo điều kiện comment | Guard đang không hoạt động | Không chỉnh riêng macro | Đọc tĩnh |
| Region neighbor | POff | src18/KNpc.cpp:8321-8343,14403-14427 | 16/32 | ô tọa độ | Chọn 8 region nối | CẨN THẬN — gắn với kích thước region | Đọc tĩnh |
| Broadcast caller | MAX_BROADCAST_COUNT | src18/KRegion.h:15; KNpc.cpp:14414 | 100 | node trong danh sách region | Áp dụng cho caller dùng macro; NormalSync dùng MAX_PLAYER | CẨN THẬN — kiểm từng caller | Đọc tĩnh |
| Chu kỳ sync | m_nNpcSyncCounter & 1 / IsActiveAll | src18/KRegion.cpp:1101-1115,1127-1148 | theo bộ đếm | lượt kích hoạt | Rải sync theo vùng; NPC vừa đi có nhánh nửa bước | CẨN THẬN — đo đứng/yên và đang đi | Đọc tĩnh |
| Request client | timeout 100 | qh9A/KNpcSet.cpp:1022,1400-1415; KSubWorld.cpp:146-163 | 100 | bước Activate, lịch sử gọi là frame | Xóa khóa request cũ để lần sync sau yêu cầu lại | CẨN THẬN — không đổi trước khi đo | Đọc tĩnh; giả định 18 frame/giây |
| B-02 policy | MaxVisible / Enabled | B-02-loc-hien-thi.md:31-38; B-02-tom-tat-diff.md:7,25 | 60 / 0 | người trong group / công tắc | Visibility policy người chơi, không phải bán kính quái | CẨN THẬN — nhánh riêng, chưa runtime | Báo cáo cũ |

## Điểm dễ làm sai

- MAX_SYNC_RANGE=32 ở src18 đang comment; CORRECT_SYNC_RANGE=30 ở client mới là check thấy trong SyncNpcMin.
- Timeout 100 nằm trên m_dwCurrentTime; client gửi request ngay khi gặp sync ngắn ID lạ. HOP-THU/A-B.md:255 gọi 100 frame, ước tính 3–6 giây; KSubWorld.cpp:151 chú thích Activate 18 frame/giây. Không coi ước tính là số đo.
- MAX_BROADCAST_COUNT=100 không áp mọi gói; NormalSync dùng MAX_PLAYER.
- Không suy mọi quái được tạo bằng Lua AddNpc; chưa xác định script/hàng mẫu cụ thể.
- Không kết luận B-02 gây hiện tượng khi chưa xác định nhánh/config. Nếu NPC_SYNC đã về mà không thấy hình, kiểm tra tạo vùng và hide flags.

## Kịch bản kiểm động cho đợt 2

**Đồ/người cần:** hai nhân vật test A/B, một quái đứng yên, một quái di chuyển, map có tọa độ/region; ghi build ID và config. Không dùng tài khoản/log thật.

**Thao tác:** A đứng cùng region chờ NormalSync, sau đó đi qua biên sang region nối. Lặp với quái đứng và di chuyển. Nếu có build B-02 được duyệt, tách hai lượt Enabled=0/1 và giữ nguyên tọa độ.

**Số đọc ở đâu:** timestamp, ID, tọa độ P3/P1; gói c2s_npcwalk, s2c_syncnpcmin, c2s_requestnpc, NPC_SYNC, s2c_requestnpcfail; thời điểm SearchID thấy ID; hide flags khi vẽ. Ghi build/config/region và khoảng cách từng trục.

**Kỳ vọng:** sync ngắn của ID lạ trong ngưỡng 30 từng trục tạo request; server còn ID thì trả NPC_SYNC; client thêm ID trước khi vẽ. Timestamp giúp tách chờ NormalSync, gate client, request/response và render. Chưa chạy trong KT-03C.

## Giải mã tên

| Tên gốc | Mã hóa | Chữ đúng | Nguồn file:dòng |
|---|---|---|---|
| Không có tên riêng trong phạm vi; NPC/quái là danh từ chung. | — | — | — |

## Sắp theo cấu trúc game

Theo luồng: dữ liệu/mẫu NPC → Lua AddNpc (nếu script tạo) → thực thể vùng server → NormalSync/BroadCast → SyncNpcMin → request dữ liệu theo ID → AddServerNpcA/region client → KNpc::Paint/DataRes.Draw. Task không nêu map, ID, phái, hoạt động hay hàng dữ liệu cụ thể.

## Đã xác minh

- Đọc trực tiếp file/hàm nêu trên ở root qh9A client và src18 server; số dòng thuộc các root đó.
- Client check 30 theo từng trục; server guard 32 đang comment.
- Đã lập kịch bản đợt 2, chưa chạy.

## Chưa xác minh

- Map/NPC cụ thể, Lua spawn script, hàng mẫu thực tế; task không chỉ định ID/map.
- Config visibility.ini trên máy chạy, nhánh đang cài, packet trace và thời gian hiện thực.
- Diff byte-for-byte qh9A với canonical client cùng revision; không có baseline trong nguồn task.
- Không build, không chạy game/exe, không VM và không mạng.

## Đề xuất tối ưu

Giữ nguyên hằng số tới khi đo P3/request/NPC_SYNC/P1. Nếu request không phát, kiểm 30/region/khóa request; nếu response thiếu, tách server lookup và B-02; nếu NPC_SYNC đã về, kiểm tạo region và hide flags. So sánh Enabled=0/1 chỉ trong môi trường test được duyệt.

## Bàn giao

- Trạng thái: DONE cho bản đồ tĩnh; runtime chưa kiểm.
- Nhịp: ghi D:\JX-wt\KT-03C.nhip tại mốc bắt đầu bị Access denied.
- Commit: không thực hiện; chưa có SHA.
- Kỹ năng đã dùng: jx1-knowledge, jx1-read-server, jx1-read-client, jx1-parameters, jx1-report. jx1-retrofit được đọc nhưng không chuẩn hóa báo cáo cũ.
- Dòng đề nghị PM gộp mục lục: KT-03C | tổng hợp | Chuỗi quái/NPC từ vùng server tới render client | quái,NPC,NormalSync,SyncNpcMin,c2s_requestnpc,tầm nhìn,KRegion,visibility | DONE tĩnh | 5/5 đầu ra | A-05; B-01; B-02; HOP-THU/A-B.
