# A-05 – Điểm tương tác người chơi trong gs001

## TÓM TẮT

1. Luồng nhìn thấy thực thể tập trung ở KRegion::BroadCast (Core/Src/KRegion.cpp:2223-2280) và KNpc::SendDataToNearRegion (Core/Src/KNpc.cpp:14103-14137); bộ lọc hiện tại là chỉ số player hợp lệ, m_nNetConnectIdx >= 0, không ngủ, còn lọc khoảng cách trong KRegion::BroadCast bị comment.
2. Đồng bộ NPC/người chơi có thêm các đường gửi thẳng tới một client (Core/Src/KNpc.cpp:7718, 7822), đồng bộ khi đổi bản đồ (Core/Src/KNpc.cpp:14993-15030), KSubWorld::BroadCasts (Core/Src/KSubWorld.cpp:2366-2377), đồng bộ object (Core/Src/KObj.cpp:1468-1621) và relay (Core/Src/KNewProtocolProcess.cpp:40-179); vá riêng BroadCast sẽ không bao phủ tất cả.
3. Chọn mục tiêu và AoE dùng ô bản đồ, quan hệ PK/đội/bang, bán kính hoặc FindNpc (Core/Src/KRegion.h:408-447; Core/Src/KMissle.cpp:1785-1867); các hàm này không kiểm tra kết nối nên slot đã tồn tại nhưng offline có thể vẫn bị xử lý.
4. Đội/bang/bạn bè, giao dịch/cửa hàng, chat/thông báo, PK/hồi sinh và xếp hạng đều có các gói gửi trực tiếp hoặc qua Chat/Tong/S3Relay (Core/Src/KPlayerTeam.cpp:397-560; MultiServer/GameServer/KSOServer.cpp:1721-1768); điều kiện lọc khác nhau, nhiều nơi chỉ kiểm tra index hoặc blacklist.
5. Bot Dormant hoàn toàn không có trong PlayerSet thì không lọt vào; một nhân vật đã tạo trong gs001 nhưng mất kết nối có thể còn lọt vào logic trạng thái/đếm/chọn mục tiêu (Core/Src/ScriptFuns.cpp:17574-18334; Core/Src/KNpcSet.cpp:1813-2042), nhưng không nhận được gói mạng hợp lệ.

Báo cáo là kết quả đọc mã tĩnh tại C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources, chủ yếu Core/Src và MultiServer/GameServer. Không chạy exe, không sửa mã nguồn canonical, không build/test.

## Phương pháp và quy ước

- BroadCast là đường phát dữ liệu tới danh sách người chơi trong region; các đường PackDataToClient/SendData trực tiếp được ghi riêng.
- “Bot Dormant” gồm (a) chưa có slot trong gs001 và (b) slot đã tồn tại nhưng m_nNetConnectIdx < 0, m_bSleepMode hoặc trạng thái offline. Trường hợp (b) không mặc định là vô hại vì nhiều đường logic không kiểm tra kết nối.
- “Chỗ vá tối thiểu” là điểm chèn kiểm tra viewer thấy thực thể này hoặc kiểm tra mục tiêu trước khi xử lý. Đây là đề xuất, chưa sửa và chưa build xác nhận.
- MAX_BROADCAST_COUNT là 100 tại Core/Src/KRegion.h:15. Vì nMaxCount truyền bằng tham chiếu và được dùng tiếp qua các region lân cận, không nên diễn giải là 100 người độc lập cho từng ô.

## 1. Đồng bộ thực thể

| File:dòng | Hàm / gói | Đường gửi/nhận và lọc hiện có | Chỗ chèn lọc viewer | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KRegion.cpp:2223-2280 | KRegion::BroadCast | Duyệt m_PlayerList; kiểm tra index player, NPC hợp lệ, m_nNetConnectIdx >= 0, m_bSleepMode == FALSE, rồi PackDataToClient ở 2266-2272. MAX_SYNC_RANGE ở 2229, điều kiện khoảng cách ở 2267-2268 bị comment. | Ngay trước 2266, sau khi có nNpcIndex và tọa độ viewer; dùng helper chung ViewerCanSee(viewer, source, packetType). | Cao: ảnh hưởng mọi gói dùng hàm này. |
| Core/Src/KNpc.cpp:7663-7725 | KNpc::SendSyncData | Dựng NPC_SYNC; bBroadCast=true gọi SendDataToNearRegion ở 7712-7715, false gửi thẳng nClient ở 7718. | Nhánh gửi thẳng 7718 phải kiểm tra viewer; nhánh broadcast đi qua KRegion::BroadCast. | Cao: request đồng bộ đơn lẻ đi vòng broadcast. |
| Core/Src/KNpc.cpp:7842-7881 | NormalMapSync | PLAYER_NORMALMAP_SYNC, phát region hiện tại và 8 region nối ở 7873-7880 bằng KRegion::BroadCast. | KRegion::BroadCast; nếu policy khác map thì chèn tại caller. | Trung bình-cao. |
| Core/Src/KNpc.cpp:7886-8055, 8235-8244 | NormalSync | NPC_NORMAL_SYNC và PLAYER_NORMAL_SYNC; phát 9 region. nMaxCount = MAX_PLAYER ở 8043/8235; gửi bản thân trực tiếp ở 8258. | Broadcast ở 8044/8236; gói bản thân chỉ cần kiểm tra connection. | Cao. |
| Core/Src/KNpc.cpp:14103-14137 | SendDataToNearRegion | Phát region hiện tại và 8 region nối, truyền chung nMaxCount bằng tham chiếu; mọi caller NPC dùng đường này. | Đây là điểm trung tâm tốt cho gói “viewer thấy thực thể”, cùng KRegion::BroadCast. | Cao nhưng phạm vi rộng. |
| Core/Src/KNpc.cpp:14485-14523 | BroadCastState | NPC_SYNC_STATEINFO, phát qua BroadCast ở 14512 và 8 region ở 14521. | KRegion::BroadCast; nếu aura có visibility riêng cần thêm loại packet. | Cao. |
| Core/Src/KNpcSet.cpp:992-1032 | KNpcSet::Remove | Khi isNeedSyn, tạo NPC_REMOVE_SYNC và phát BroadCast region hiện tại + 8 region. | Lọc viewer ở KRegion::BroadCast; không chặn xóa state server. | Cao: chặn nhầm để client giữ NPC ma. |
| Core/Src/KNpc.cpp:14848-14900 | đổi vị trí cùng map | Gửi NPC_REMOVE_SYNC ở 14853-14858, sau đó NPC_PLAYER_TYPE_NORMAL_SYNC ở 14889-14900, đều qua SendDataToNearRegion. | Cần xử lý viewer cũ và viewer mới khác nhau. | Rất cao. |
| Core/Src/KNpc.cpp:14993-15030 | ChangeWorld | Remove gửi qua near-region ở 15000-15004; client đích nhận SubWorld::SendSyncData trực tiếp ở 15030. | Near-region cho viewer cũ; kiểm tra client đích ở SendSyncData. | Rất cao. |
| Core/Src/KNpcSet.cpp:1272-1289 và Core/Src/KProtocolProcess.cpp:5418-5424 | request NPC / SyncNpc | Client yêu cầu NPC theo ID; server gọi Npc[nFindIndex].SendSyncData(nClientIdx) trực tiếp. | Trước SendSyncData kiểm tra cùng map/region/quyền nhìn. | Cao. |
| Core/Src/KSubWorld.cpp:2366-2377 | KSubWorld::BroadCasts | Duyệt toàn PlayerSet, chỉ kiểm tra connection, NPC hợp lệ và cùng subworld; gửi trực tiếp, không qua KRegion::BroadCast. | Trong vòng 2371-2373 thêm policy viewer/map nếu packet không phải broadcast toàn map. | Cao. |
| Core/Src/KObj.cpp:1468-1621 | KObj::SyncState, SyncDir, SyncRemove, TrapAct | Object state/dir/remove/trap action phát region + 8 region bằng BroadCast. | KRegion::BroadCast; nếu object visibility khác NPC phải truyền packet type. | Trung bình-cao. |
| Core/Src/KNpc.cpp:16000-16046 | SendSerCommand | Gói skill/autodo phát qua BroadCast ở 16036-16043, sau đó gửi lại chính client ở 16046. | Broadcast tại region; direct self chỉ kiểm tra connection. | Cao. |

Bot Dormant: bot chưa có slot không phát hiện/không nhận gói. Slot đã tồn tại nhưng m_nNetConnectIdx < 0 bị loại khỏi KRegion::BroadCast ở 2266, nhưng các đường direct (SendSyncData, KSubWorld::BroadCasts) phải kiểm tra riêng; chưa có bằng chứng runtime cho từng trạng thái.

Đường gửi không qua BroadCast đã đọc: KNpc::SendSyncData(..., false) (KNpc.cpp:7718, 7822), KNpcSet::SyncNpc (KNpcSet.cpp:1284-1288), KSubWorld::BroadCasts (KSubWorld.cpp:2366-2377), gói self/direct trong KNpc.cpp:8258, 15030, 15093, 16046, cùng các đường object/item/PK nêu ở mục sau.

## 2. Chọn mục tiêu

| File:dòng | Hàm / gói | Đường chọn và lọc hiện có | Chỗ chèn lọc viewer/mục tiêu | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KRegion.h:408-447 | KRegion::FindNpc | Kiểm tra ô có NPC, m_CurrentLife > 0; nType=0 dùng nRelation & NpcSet.GetRelation, nType=1 theo setting, nType=2 theo DWID. Không kiểm m_nNetConnectIdx. | Nếu là chọn mục tiêu từ player, thêm TargetCanBeInteracted(player, npc) sau kiểm quan hệ; không áp dụng bừa cho AI/NPC. | Cao. |
| Core/Src/KPlayer.cpp:2361-2480 | FindAroundPlayer, FindAroundNpc, FindAroundNpcID | Tìm region hiện tại + 8 region nối; FindAroundNpcID có kiểm khoảng cách qua NpcSet.GetDistance, không kiểm kết nối. | Chèn kiểm tra mục tiêu player ở caller hoặc tạo biến thể online interactable; tránh sửa hàm dùng cho AI. | Cao. |
| Core/Src/KNpcAI.cpp:2248-2295, 2621-2797 | GetNearestCharacter, GetNearestNpc | Dùng m_VisionRadius, cell map, vòng khoảng cách, FindNpc và relation. | Chỉ thêm policy ở nhánh player-origin; AI server vẫn cần thấy NPC không kết nối. | Cao. |
| Core/Src/KNpcAI.cpp:3009-3014 | InEyeshot | Khoảng cách GetDistance so với m_VisionRadius, không kiểm connection. | Chỉ dùng làm điều kiện hiển thị khi caller biết viewer. | Trung bình. |
| Core/Src/KSkills.cpp:221-265 | CanCastSkill | Quan hệ dialog/enemy/ally/self từ NpcSet.GetRelation; có kiểm loại mục tiêu và equipment. | Trước cast từ player, kiểm target cùng map/online/visible; không đổi quan hệ AI. | Cao. |
| Core/Src/KSkills.cpp:3348-3415 | CastInitiativeSkill | Server kiểm nParam2, relation và loại target; sau đó ReceiveDamage/SetStateSkillEffect. | lab_processdamage là điểm chặn target player trước gây tác động. | Rất cao. |
| Core/Src/KProtocolProcess.cpp:5581-5606 | NpcSkillCommand | ParamY == -1 dùng Player[nIndex].FindAroundNpc(dwID) rồi SendSerCommand; tọa độ thì gửi theo param. | Trước SendSerCommand kiểm target player thấy được và cùng subworld. | Cao. |
| Core/Src/ScriptFuns.cpp:6784-6865 | LuaGetAroundNpcList | Lua truyền range/relation/type; vòng cell kiểm khoảng cách và m_Hide, gọi FindNpc. | Nếu script theo player, lọc m_nNetConnectIdx/visibility trước đưa ID ra Lua. | Trung bình-cao. |
| Core/Src/ScriptFuns.cpp:19852-19900 | LuaFindAroundPlayer | Duyệt toàn PlayerSet, cùng map, khoảng cách bình phương <= radius; chỉ kiểm m_nIndex > 0. | Thêm m_nNetConnectIdx >= 0 nếu API nghĩa là người chơi đang tương tác; giữ API thống kê nếu cần offline. | Trung bình. |
| Core/Src/KNpcSet.cpp:1813-2042 | GetRelation | Quan hệ người/NPC dựa camp, PK, team, tong, fight mode; là lọc tác động, không phải lọc hiển thị. | Không dùng GetRelation thay ViewerCanSee; thêm policy riêng sau quan hệ. | Rất cao nếu sửa trực tiếp. |

Bot Dormant: chưa có slot thì không lọt. Slot player đã tồn tại nhưng mất kết nối có thể lọt vào FindNpc, FindAround*, LuaFindAroundPlayer vì các đường này không kiểm connection; chưa kiểm runtime xem slot offline còn trong mọi region hay không.

Chỗ vá tối thiểu: không sửa GetRelation toàn cục. Tạo helper cho player-origin ở NpcSkillCommand, CastInitiativeSkill, FindAround* và LuaFindAroundPlayer; giữ đường AI/NPC riêng.

## 3. Sát thương diện rộng và hiệu ứng vùng

| File:dòng | Hàm / gói | Đường tác động và lọc hiện có | Chỗ chèn lọc target/viewer | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KMissle.cpp:1785-1867 | KMissle::ProcessCollision | Quét hình vuông nRangeX/Y; điều kiện hình tròn ở 1835-1836 bị comment; FindNpc(..., eRelation) ở 1846, sau đó ProcessDamage ở 1851. | Trước ProcessDamage, kiểm target hợp lệ với launcher; không dùng visibility viewer để ngăn NPC server bị damage. | Rất cao. |
| Core/Src/KMissle.cpp:1499-1588 | ProcessDamage nhánh damage/state | Gọi ReceiveDamage, SetStateSkillEffect, SetImmediatelySkillEffect; lọc relation/return/ignore skill theo từng nhánh. | Điểm an toàn sau FindNpc và trước ReceiveDamage; điểm broadcast hiệu ứng ở KNpc::SetStateSkillEffect. | Rất cao. |
| Core/Src/KSkills.cpp:1668-1680, 1813-1815, 2169-2331, 2472-2623 | CastZone, CastLine, CastWall, CastCircle, CastSpread | Sinh nhiều missile theo vùng/toạ độ; collision mới chọn target. | Lọc target tại ProcessCollision; lọc gói hiệu ứng tại SendDataToNearRegion/state effect. | Cao. |
| Core/Src/KNpc.cpp:1677-1730 | aura chủ động | Aura cast child skill từ player/dialoger; không kiểm viewer ở bước tính/cast. | Lọc target trong child skill/collision; không chặn aura server state. | Cao. |
| Core/Src/KNpc.cpp:10365-10394, 10163-10164 | SetStateSkillEffect | Cập nhật state; với player gửi STATE_EFFECT_SYNC direct ở 10394; caller có thể BroadCastState. | Direct self kiểm connection; state broadcast dùng KRegion::BroadCast. | Trung bình-cao. |
| Core/Src/KRegion.cpp:1472-1501, KNpc.cpp:15298-15325 | bẫy map | Region lưu trap script; CheckTrap đọc trap tại tọa độ và chạy Lua script cho player. Không có viewer concept. | Chặn tại script/target nếu trap chỉ dành cho người đang kết nối; không dùng viewer lọc trigger server. | Cao. |
| Core/Src/KObj.cpp:1585-1621 | KObj::TrapAct | Gửi OBJ_SYNC_TRAP_ACT qua BroadCast region + 8 region. | KRegion::BroadCast với packet type object trap. | Trung bình. |
| Core/Src/KNpc.cpp:4466-4504 | ReceiveDamage | Kiểm launcher/target index, death/revive, hit rating; không kiểm connection. | Không chèn viewer filter ở đây; đây là lớp damage dùng cho AI. | Rất cao. |

Bot Dormant: bot không có slot thì không bị collision. Slot player còn trong Npc/PlayerSet nhưng không kết nối có thể bị FindNpc/ReceiveDamage/state effect tác động vì các hàm không kiểm m_nNetConnectIdx; hiệu ứng gửi ra client có thể bị bỏ hoặc gửi vào chỉ số không hợp lệ tùy caller.

Chỗ vá tối thiểu: tách CanReceivePlayerAction khỏi visibility. Nếu mục tiêu là bot dormant không bị ảnh hưởng, chặn tại ProcessCollision/CastInitiativeSkill cho launcher là player; nếu mục tiêu chỉ là không cho người khác nhìn, chặn ở đường phát gói hiệu ứng.

## 4. Tổ đội, bang hội, bạn bè và S3Relay

| File:dòng | Hàm / gói | Đường gửi/nhận và lọc hiện có | Chỗ chèn lọc | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KPlayerTeam.cpp:397-426 | KPlayerTeam::InviteAdd | Tìm target bằng FindAroundPlayer; kiểm team flag/can-team; gửi TEAM_INVITE_ADD_SYNC direct tới target. | Sau FindAroundPlayer và trước PackDataToClient kiểm target connection/visible. | Cao. |
| Core/Src/KPlayerTeam.cpp:433-560 | GetInviteReply | Kiểm invite list, player index, team capacity; gửi add member/self info direct tới captain/member/target. | Mỗi PackDataToClient cần helper IsConnectedPlayer. | Cao. |
| Core/Src/KPlayer.cpp:1700-2221 | team info/add/leave/kick | Nhiều gói PLAYER_SEND_TEAM_INFO, PLAYER_TEAM_ADD_MEMBER, PLAYER_SEND_SELF_TEAM_INFO tới player index. | Tập trung wrapper gửi team để bỏ recipient offline. | Cao. |
| Core/Src/KPlayerTong.cpp:413-476, 525-593 | TransferAddApply, TransferInviteApply | Tìm target quanh player; tạo gói tong và gửi direct; điều kiện camp/level/team/trading. | Sau tìm target, trước gói direct; relay state vẫn xử lý server. | Cao. |
| Core/Src/KNewProtocolProcess.cpp:40-179 | Transfer/Chat/Tong queues, BroadcastGlobal, BroadcastLocalServer | Queue gửi qua IClient::SendPackToServer; BroadcastLocalServer duyệt PlayerSet và gửi mọi player, không kiểm m_nNetConnectIdx ở 175. | Thêm connection check ở BroadcastLocalServer; giữ queue relay tách viewer policy. | Cao. |
| Core/Src/KPlayerChat.cpp:1272-1330, 1496-1528 | bạn bè add/resend/offline | Add friend gửi direct; offline notification đánh dấu friend index 0 và gửi CHAT_FRIEND_OFFLINE_SYNC. | Recipient direct và GetMsgOffLine cần kiểm connection trước gửi. | Trung bình. |
| MultiServer/GameServer/KSOServer.cpp:1721-1768 | TongMessageProcess | Nhận từ Tong/S3Relay; passtosomeone/passtobevy chuyển tới một/nhiều net ID sau CheckPlayerID. | CheckPlayerID nên là cổng xác thực connection + character ID. | Cao. |
| MultiServer/GameServer/KSOServer.cpp:3592-3690 | PlayerFschatProcess | Chọn m_pTransferClient, m_pChatClient, m_pTongClient; kiểm channel trả phí và private target online, gắn tagPlusSrcInfo, gửi S3Relay. | Trước SendPackToServer kiểm source/target; giữ CheckPlayerID phía nhận. | Cao. |
| MultiServer/GameServer/KSOServer.cpp:6787-6805 | CheckPlayerID | Xác nhận net index, game status, player index và character ID. Đây là bộ lọc relay rõ nhất. | Tái dùng làm gateway cho đường relay khác. | Trung bình. |

Bot Dormant: chưa có slot không thể được mời/đội/bạn. Slot tồn tại nhưng m_nNetConnectIdx < 0 có thể còn trong team/friend/tong state và bị mutate; gói direct không có người nhận. Relay có CheckPlayerID tốt hơn, nhưng chỉ áp dụng đường đi qua nó.

Chỗ vá tối thiểu: wrapper SendToConnectedPlayer cho team/friend/tong và bổ sung connection check trong BroadcastLocalServer; không sửa thuật toán quan hệ team/tong.

## 5. Giao dịch, cửa hàng cá nhân, trao đổi vật phẩm

| File:dòng | Hàm / gói | Đường gửi/nhận và lọc hiện có | Chỗ chèn lọc | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KProtocolProcess.cpp:8058-8101 | c2sViewEquip, c2sViewItem, c2supdateitem | Chặn tự xem; dùng FindAroundPlayer; gọi SendEquipItemInfo/SendSellItemInfo tới requester. | Sau FindAroundPlayer kiểm target online/cùng map; trước hàm gửi view. | Cao. |
| Core/Src/KPlayer.cpp:11808-11899 | SendSellItemInfo | Thu thập item đang bán, chia packet, gửi direct tới nTargetPlayer; dữ liệu item không qua broadcast. | Validate requester connection ở đầu hàm và trước mỗi send. | Cao. |
| Core/Src/KPlayer.cpp:11904-11977, 12100-12117 | SendEquipItemInfo, SendLianItemInfo | Đọc trang bị/lian item target, gửi direct tới viewer. | Cùng policy requester/target visibility. | Cao. |
| Core/Src/KProtocolProcess.cpp:8823-8905 | c2sNeedCount, c2sTradeBuy | Tìm shop quanh player; kiểm m_BaiTan, item tồn tại, giá, tiền; direct reply. | Kiểm online/visible trước FindAroundPlayer/mua; giữ kiểm item/tiền. | Rất cao. |
| Core/Src/KPlayer.cpp:6563-6633, 7054-7115 | trade open/start/reply | Trade target phải quanh qua FindAroundPlayer, menu state đúng; gửi TRADE_APPLY_START_SYNC direct. | Chặn target offline trước tạo m_cTrade; validate cả hai connection. | Rất cao. |
| Core/Src/KPlayer.cpp:6640-6654, 6724-6749, 7122-7137 | money/decision/state | Kiểm trading/lock/tiền; SyncTradeState gửi cho hai net index. | Wrapper direct gửi tới hai bên; không để state lock chạy một phía nếu bên kia offline. | Rất cao. |
| Core/Src/KItemList.cpp:4541, 6128-6216, 8841-8933 | item transfer | Item sync/remove gửi direct tới m_nTradeDest và player hiện tại; có kiểm trade/lock/item tradeable. | Mọi send tới Player[...m_nTradeDest].m_nNetConnectIdx cần kiểm connection và trade pair. | Rất cao. |
| Core/Src/KPlayerMenuState.cpp:65-130 | menu/trade state | Gửi TRADE_CHANGE_STATE_SYNC direct và NPC_SET_MENU_STATE_SYNC qua SendDataToNearRegion. | Direct recipient check; near-region dùng visibility chung. | Cao. |

Bot Dormant: chưa có slot không lọt. Slot còn state nhưng offline có thể bị tìm thấy bởi FindAroundPlayer và state trade có thể được tạo; gói direct không có người nhận. Không coi gửi vào net index âm là bộ lọc an toàn.

Chỗ vá tối thiểu: guard chung cho cặp trade (both connected, cùng map/visible, menu state hợp lệ) trước TradeApplyStart, TradeDecision, KItemList transfer; không vá từng packet riêng lẻ.

## 6. Chat và thông báo hệ thống

| File:dòng | Hàm / gói | Đường gửi/nhận và lọc hiện có | Chỗ chèn lọc | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KPlayerChat.cpp:423-497 | ServerSendChat | Kiểm channel, độ dài, tốc độ; channel all duyệt PlayerSet và gửi direct ở 464-470 không kiểm net; channel screen dùng SendDataToNearRegion ở 497. | Channel all thêm m_nNetConnectIdx >= 0; screen dùng visibility helper. | Cao. |
| Core/Src/KPlayerChat.cpp:501-560 | private chat | Tìm target trong region/8 region theo ID, kiểm target và gửi direct; phần thân sau dòng 524 chưa đọc hết. | Chưa kiểm toàn thân; điểm chắc chắn sau tìm target, trước direct send. | Cao. |
| Core/Src/KPlayerChat.cpp:709-805 | GetChat | Client nhận all/screen/single; screen yêu cầu talker tồn tại, single kiểm friend hoặc tìm name. | Phía client, không phải điểm chống gửi server. | Thấp cho server patch. |
| Core/Src/CoreServerShell.cpp:2777-2859 | GroupChat | Team gửi captain/member, có blacklist; faction/tong duyệt PlayerSet, có blacklist nhưng không luôn kiểm net. | Wrapper recipient connected + blacklist. | Cao. |
| Core/Src/CoreServerShell.cpp:2861-2995 | group/mission/screen chat | Tong/mission duyệt player; screen lọc khoảng cách MAX_SYNC_RANGE=23 và blacklist ở 2993-2995. | Giữ khoảng cách screen; thêm connection check tại send. | Cao. |
| Core/Src/KPlayerChat.cpp:1841-1909, 1912-1976, 2054-... | system map/specific/global | System map gửi toàn player cùng map hoặc target; system all duyệt PlayerSet; global system qua extended chat. | Tất cả vòng PlayerSet cần bỏ recipient không kết nối; target path kiểm index. | Cao. |
| Core/Src/KPlayerSet.cpp:587-601 | Broadcasting | Chuẩn bị packet, gọi SendSystemInfo(0,0,...), rồi SendPackToClient(-1). | SendSystemInfo/transport layer; không dùng -1 như broadcast nếu cần policy viewer. | Cao. |
| MultiServer/GameServer/KSOServer.cpp:1619-1714 | ChatMessageProcess | Nhận chat relay; team/faction/near/screen/private gọi GroupChat/ChatGroupMan/ChatSpecMan; GM announcement gọi OperationRequest. | Gateway xác thực source; core recipient policy tại GroupChat/SendSystem. | Cao. |
| MultiServer/GameServer/KSOServer.cpp:2790-2878 | ChatGroupMan, ChatSpecMan | CheckPlayerID và blacklist; group gửi nhiều net ID, private gửi một net ID. | Giữ CheckPlayerID, bổ sung recipient connection trong loop. | Cao. |
| MultiServer/GameServer/KSOServer.cpp:3592-3690 | relay chat vào S3 | Chọn chat/tong/transfer client, tính phí channel và kiểm private source online, gửi tagPlusSrcInfo tới S3Relay. | Kiểm source/target ở đây. | Trung bình-cao. |

Bot Dormant: chưa có slot không nhận chat. Slot tồn tại nhưng mất kết nối có thể vẫn được duyệt bởi vòng PlayerSet; một số đường không kiểm m_nNetConnectIdx, nên có thể tạo gửi lỗi/log/chi phí dù không có client nhận. Channel screen đi qua BroadCast nên lọc connection.

Chỗ vá tối thiểu: SendToConnectedPlayer ở mọi vòng PlayerSet, giữ blacklist và lọc screen hiện có; không đưa viewer lọc vào nội dung chat private/relay.

## 7. PK, thù, trạng thái chiến đấu, hồi sinh

| File:dòng | Hàm / gói | Đường gửi/nhận và lọc hiện có | Chỗ chèn lọc | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/KPlayerPK.cpp:55-86 | SetNormalPKState | Cập nhật PK/NPC flag, gửi PK_NORMAL_FLAG_SYNC direct cho chính player. | Kiểm connection ở direct send; state server vẫn cập nhật. | Trung bình. |
| Core/Src/KPlayerPK.cpp:128-228 | EnmityPKOpen | Kiểm aim index, fight mode, camp, exercise/enmity; cập nhật hai phía; gửi PK_ENMITY_STATE_SYNC direct cho hai net index. | Trước cập nhật hai phía kiểm cả hai player connected/targetable. | Cao. |
| Core/Src/KPlayerPK.cpp:276-312 | ExercisePKOpen | Kiểm camp/aim, cập nhật hai phía, gửi sync direct cho hai bên. | Guard targetable trước state mutation. | Cao. |
| Core/Src/KNpcSet.cpp:1951-2042 | player-player GetRelation | Quan hệ dựa fight mode, PK flag, team, tong, camp; quyết định enemy/ally/none. | Không sửa relation toàn cục; guard targetable tại caller. | Rất cao. |
| Core/Src/KProtocolProcess.cpp:6211-6238 | PK command | c2sPKApplyEnmity kiểm cấm/fight mode, FindAroundNpc, yêu cầu target player, gọi EnmityPKOpen. | Sau FindAroundNpc kiểm connection/visibility. | Cao. |
| Core/Src/KNpc.cpp:14144-14208 | DeathCalcPKValue | Tính punishment/PK value theo killer, enmity, normal PK, camp, level; không gửi viewer. | Không lọc viewer; chỉ kiểm killer/target hợp lệ nếu cần. | Cao nếu sửa. |
| Core/Src/KPlayer.cpp:7248-7308 | Revive | Gửi NPC_REVIVE_SYNC direct cho người hồi sinh, gọi BroadCastRevive xung quanh, đổi world/fight mode và hồi máu. | Direct self kiểm connection; broadcast dùng BroadCast; guard state trước đổi world. | Cao. |
| Core/Src/KNpc.cpp:8263-8300 | BroadCastRevive | Phát revive qua region + 8 region bằng BroadCast. | KRegion::BroadCast. | Cao. |
| Core/Src/KProtocolProcess.cpp:6178-6204 | revive command | Chọn hồi tại chỗ/về thành, gọi Player::Revive. | Không cần viewer lọc; cần kiểm command/player connected. | Trung bình. |
| Core/Src/KNpc.cpp:7802-7818, 8212-8224 | PK/fight/sleep flags trong sync | PLAYER_SYNC/PLAYER_NORMAL_SYNC chứa rank, PK, fight, sleep flag; phát near-region hoặc direct. | Viewer policy ở broadcast; direct self ở caller. | Cao. |
| Core/Src/KPlayerSet.cpp:788-833, 1027-1041 | logout/offline cleanup | CheckMaps gọi chat offline, leave team, trade cancel, PK close; login failure clear tong/PK. | Đây là cleanup; không chặn theo viewer. | Trung bình. |

Bot Dormant: không có slot thì không bị PK/revive. Slot tồn tại nhưng offline có thể bị EnmityPKOpen, GetRelation, punishment hoặc cleanup tác động vì state dựa player index; gói direct tới net index âm không tạo quan sát hợp lệ. BroadCastRevive vẫn loại người nhận không kết nối.

Chỗ vá tối thiểu: guard targetable ở c2sPKApplyEnmity, EnmityPKOpen, ExercisePKOpen; không sửa GetRelation hoặc DeathCalcPKValue để giải quyết visibility.

## 8. Xếp hạng, bảng điểm, đếm và danh sách player/Lua

| File:dòng | Hàm / gói | Dữ liệu/đường gửi và lọc hiện có | Chỗ chèn lọc | Rủi ro vá |
|---|---|---|---|---|
| Core/Src/ScriptFuns.cpp:17574-17578 | LuaGetPlayerCount | Trả PlayerSet.GetPlayerNumber(); đây là số slot đang dùng, không phải đếm connection. | Nếu API cần online thật, dùng GetOnlinePlayerCount/lọc m_nNetConnectIdx; cần xác định semantics trước sửa. | Trung bình. |
| Core/Src/ScriptFuns.cpp:18298-18313 | LuaGetPlayerCountInMap | Duyệt PlayerSet, so subworld, không kiểm connection. | Thêm tùy chọn online hoặc đổi semantics; không sửa âm thầm. | Trung bình. |
| Core/Src/ScriptFuns.cpp:18315-18334 | LuaGetPlayerCountOffLive | Duyệt m_nLiXian, trả tổng offline/online theo cờ; đây là API trạng thái offline. | Không lọc; tài liệu hóa đây là API offline. | Thấp. |
| Core/Src/ScriptFuns.cpp:19852-19900 | LuaFindAroundPlayer | Duyệt PlayerSet, cùng map + bán kính; chỉ m_nIndex > 0, không connection. | Thêm mode online; giữ mode thống kê nếu cần. | Trung bình-cao. |
| Core/Src/ScriptFuns.cpp:22969-23005, 23107-23122 | LuaGetNextPlayer, LuaMissionPlayerCount | Lấy player từ mission list/group; wrapper không lọc connection. | API online riêng hoặc lọc khi build mission list; chưa kiểm lifecycle đầy đủ. | Trung bình. |
| Core/Src/ScriptFuns.cpp:24764-24832 | LuaBT_BroadSelf, LuaBT_WorldLadder | Xây/cập nhật ladder từ mission player list; SendRank gửi direct tới m_nNetConnectIdx ở 24760; WorldLadder gọi SendRank cho từng member. | SendRank kiểm connection trước send; lọc participant ở mission nếu bảng chỉ online. | Cao. |
| Core/Src/KProtocolProcess.cpp:6241-6265 | LadderQuery | Chỉ cho requester lnID >= 0, lấy Ladder.GetTopTen, gửi LADDER_DATA direct. | Đã có guard requester; không cần viewer filter thêm. | Thấp. |
| Core/Src/KLadder.cpp:95-125 | KLadder::GetTopTen | Trả bảng top từ GameStatData, không duyệt player runtime. | Kiểm dữ liệu đầu vào/lifecycle; nguồn cập nhật bảng chưa kiểm. | Thấp-trung bình. |
| Core/Src/KPlayer.cpp:11269-11312 | SendMSRank | Gửi mission rank direct nếu m_nNetConnectIdx != -1. | Guard đã có; kiểm thêm mission member offline. | Thấp. |
| Core/Src/KMission.h:428-455 | GetPlayerCount, GetGroupPlayerCount | Đếm mission container/group, không kiểm network. | Chỉ sửa nếu yêu cầu online count; giữ count gameplay. | Trung bình. |
| Core/Src/KPlayerSet.h:145-147, KPlayerSet.cpp:447-459 | GetFirstPlayer, GetNextPlayer | Duyệt m_UseIdxPlayerSet; không đồng nghĩa connection online. | Không sửa iterator; tạo helper ForEachConnectedPlayer. | Thấp. |
| Core/Src/ScriptFuns.cpp:6784-6865, 19852-19900 | danh sách quanh NPC/player | Trả ID/index cho Lua; lọc life/hide hoặc map/range, không net. | Mode online/visible tại API caller. | Trung bình. |
| Core/Src + MultiServer/GameServer | GetAllPlayer... | Không tìm thấy symbol GetAllPlayer* trong vùng đã đọc; API tương đương là GetFirstPlayer/GetNextPlayer, LuaGetPlayerCount*, LuaGetNextPlayer. | Chưa cần vá symbol không tồn tại; rà script ngoài Sources nếu mở rộng. | Chưa kiểm ngoài phạm vi. |

Bot Dormant: không có slot thì không xuất hiện trong iterator. Slot đã tạo nhưng offline có thể bị tính trong GetPlayerCount, GetPlayerCountInMap, mission/ladder và LuaFindAroundPlayer; đường gửi bảng đã có nơi kiểm m_nNetConnectIdx, nhưng dữ liệu có thể vẫn được tính.

Chỗ vá tối thiểu: không đổi semantics hàm đếm gameplay. Thêm API/tuỳ chọn ConnectedPlayerCount và GetConnectedPlayers; tại SendRank/LadderQuery giữ guard connection. GetAllPlayer... chưa thấy trong source đã đọc.

## Đường gửi ngoài KRegion::BroadCast

- Direct core: KNpc::SendSyncData (KNpc.cpp:7718, 7822), KNpcSet::SyncNpc (KNpcSet.cpp:1284-1288), KSubWorld::BroadCasts (KSubWorld.cpp:2366-2377), KPlayer::Revive (KPlayer.cpp:7264), PK direct (KPlayerPK.cpp:85, 111-113, 221, 305-310), team/tong/friend/trade direct (KPlayer.cpp, KPlayerTeam.cpp, KPlayerTong.cpp, KPlayerChat.cpp), item transfer (KItemList.cpp:4541, 6128-6216, 8841-8933), ranking (KProtocolProcess.cpp:6241-6265, ScriptFuns.cpp:24760).
- Near-region wrapper: KNpc::SendDataToNearRegion (KNpc.cpp:14103-14137) và các caller remove/move/state/chat/object.
- Core relay queues: KNewProtocolProcess::SendNetMsgToTransfer/Chat/Tong, BroadcastGlobal, BroadcastLocalServer (KNewProtocolProcess.cpp:40-179).
- S3Relay/Chat/Tong: ChatMessageProcess (KSOServer.cpp:1619-1714), TongMessageProcess (1721-1768), ChatGroupMan/ChatSpecMan (2790-2878), PlayerFschatProcess (3592-3690), CheckPlayerID (6787-6805).

## Đề xuất điểm chèn bộ lọc (xếp theo rủi ro)

1. **Rất cao – tác động gameplay và dữ liệu:** chặn target/cặp player trước `ProcessCollision` (Core/Src/KMissle.cpp:1785-1867), `CastInitiativeSkill` (Core/Src/KSkills.cpp:3348-3415), `EnmityPKOpen`/`ExercisePKOpen` (Core/Src/KPlayerPK.cpp:128-228, 276-312), và trade/item transfer (Core/Src/KPlayer.cpp:6605-6724; Core/Src/KItemList.cpp:6128-6216).
2. **Rất cao – đồng bộ spawn/remove/move:** dùng policy viewer tại `KRegion::BroadCast` (Core/Src/KRegion.cpp:2223-2280) và `SendDataToNearRegion` (Core/Src/KNpc.cpp:14103-14137), đồng thời kiểm đường direct `SendSyncData`/`SyncNpc` (Core/Src/KNpc.cpp:7718, 7822; Core/Src/KNpcSet.cpp:1272-1289).
3. **Cao – relay và phát nhóm:** thêm wrapper recipient connected tại `BroadcastLocalServer`/các queue (Core/Src/KNewProtocolProcess.cpp:139-179), `GroupChat` (Core/Src/CoreServerShell.cpp:2777-2995) và `ChatGroupMan`/`ChatSpecMan` (MultiServer/GameServer/KSOServer.cpp:2790-2878), giữ `CheckPlayerID` (KSOServer.cpp:6787-6805).
4. **Cao – team/tong/friend/shop:** kiểm connection sau `FindAroundPlayer` và trước mọi `PackDataToClient` trong team/tong/view item (Core/Src/KPlayerTeam.cpp:397-560; Core/Src/KPlayerTong.cpp:413-476; Core/Src/KProtocolProcess.cpp:8058-8101).
5. **Trung bình-cao – AoE/state/object:** phân biệt target server với viewer khi phát state/effect/object (Core/Src/KNpc.cpp:10365-10394; Core/Src/KObj.cpp:1468-1621; Core/Src/KMissle.cpp:1499-1588).
6. **Trung bình – Lua/API đếm và tìm quanh:** thêm mode online/connected thay vì đổi âm thầm semantics của API hiện có (Core/Src/ScriptFuns.cpp:17574-18334, 19852-19900, 22969-23005).
7. **Thấp-trung bình – ranking:** giữ guard requester ở `LadderQuery`/`SendMSRank`, chỉ lọc member khi yêu cầu bảng online (Core/Src/KProtocolProcess.cpp:6241-6265; Core/Src/KPlayer.cpp:11269-11312).
8. **Chưa kiểm – ngoài vùng source đã đọc:** symbol `GetAllPlayer...` không xuất hiện trong Core/Src và MultiServer/GameServer; cần rà script ngoài Sources nếu task mở rộng.

## Kết luận và thứ tự vá đề xuất

1. Rủi ro cao nhất: giao dịch/item transfer, PK target, AoE damage và đồng bộ remove/move; cần guard mục tiêu/cặp player trước mutate state.
2. Rủi ro cao: KRegion::BroadCast/SendDataToNearRegion, direct SendSyncData, BroadcastLocalServer, chat/group relay; cần policy viewer chung nhưng phân loại packet.
3. Rủi ro trung bình: team/tong/friend, shop view, Lua list/count; dùng wrapper recipient connected và API online riêng.
4. Không sửa canonical source trong task này. Báo cáo chỉ ghi điểm chèn; chưa có build/runtime xác nhận.

## Kiểm chứng

- Đã đọc trực tiếp các file và dòng được trích dẫn từ nguồn chỉ đọc.
- Không có lệnh build/test theo task; không chạy exe.
- rg không có trong môi trường nên tìm kiếm dùng Select-String/đọc dòng PowerShell; các số dòng trong bảng là từ kết quả đọc file thực tế.
- JIBS-danh-gia-bot.md được dùng làm bối cảnh; kết luận mới được đối chiếu với source, không suy diễn runtime.

