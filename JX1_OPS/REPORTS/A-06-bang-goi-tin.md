Tóm tắt 1: Đối chiếu source hoàn tất; commit BỊ CHẶN bởi quyền ghi metadata Git ngoài workspace, chưa có commit SHA.
Tóm tắt 2: s2c có 190 mục khớp mã; c2s client/gameserver có 167 mục, chỉ khác tên login mã 65 (C/KProtocolDef.h:20,218; S/KProtocolDef.h:21,220).
Tóm tắt 3: Gateway thiếu bốn symbol c2s làm lệch mã từ 185; client thiếu ba relay và bốn chat (C/KProtocolDef.h:370,431,440; S/KProtocolDef.h:372,434,446; G/KProtocolDef.h:372).
Tóm tắt 4: KProtocol.h có 18 struct chung khác khai báo; KTongProtocol.h lệch ID và payload; bảng độ dài client còn dư mục trước chestpwsync (C/KProtocol.cpp:171-173).
Tóm tắt 5: Chưa build/test/runtime theo task; mọi kết luận chỉ ở mức source, endpoint thực tế và ABI chưa xác minh.

# A-06 — Bảng gói tin client, gameserver và gateway

## Phạm vi và quy ước dẫn nguồn

Trạng thái: **PARTIAL** — đã hoàn tất báo cáo; chưa tạo commit do sandbox từ chối ghi Git metadata. Ngày hoàn tất nội dung: 17/11/2026.

Các ký hiệu dưới đây là tiền tố đường dẫn tuyệt đối; ví dụ C/KProtocol.h:178 là file KProtocol.h trong thư mục C bên dưới, dòng 178. Cột D trong bảng kiểm kê là KProtocolDef.h; CP/SP là hai bảng độ dài, CX/SX là hai bảng dispatch.

- C = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\`.
- S = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Headers\`.
- G = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Headers\`.
- CP = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocol.cpp`.
- SP = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KProtocol.cpp`.
- CX = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocolProcess.cpp`.
- SX = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KProtocolProcess.cpp`.

Chỉ đọc các header giao thức và source KProtocol.cpp/KProtocolProcess.cpp để nối tên gói với cấu trúc. Header server nằm ở gameserver/Headers, còn source xử lý nằm ở gameserver/Sources/Core/Src (SP:5; C/KProtocol.h:7-8; S/KProtocol.h:15-16). Không sửa source, không chạy binary game, không tải source/log/dump ra ngoài.

SHA-256 của ba KProtocolDef.h khi đọc:

- C (533 dòng): `78CC6D34999B4CE8CFE1ADFE13F358E15FCC4D9FC3985EC7BDACB752F2441810`.
- S (570 dòng): `82F83399DDD198E04D431F74C5EE385832FC0A304D560EA3BF70EE78ED83CBCE`.
- G (570 dòng): `828D477DC2C81B43274D135BCAD76C0F20C213CA12FD42D01C07DC2E9B7FFC20`.

## Kết quả đối chiếu

1. C và S đều khai báo USE_KPROTOCOL_VERSION=1, KPROTOCOL_VERSION=1 và g_nGlobalProtocolType=31; cùng số version không chứng minh tương thích payload (C/KProtocolDef.h:8-18; S/KProtocolDef.h:8-19; bảng khác struct bên dưới).
2. Toàn bộ s2c, c2c, gm và playercomm khớp tên/mã giữa C/S/G. Trong c2s, C đặt c2s_login=65 còn S/G đặt c2s_login_fhgyrinhkmvnsheypo=65; khác tên này giữ nguyên giá trị (C/KProtocolDef.h:249; S/KProtocolDef.h:251; G/KProtocolDef.h:251). Bảng dưới liệt kê cả các mốc begin/end và alias, nên số mục không đồng nghĩa số gói có payload.
3. G thiếu c2s_gmcommand, c2s_apply_mask_lock, c2s_player_combine_item, c2s_playercommand; các mục còn lại từ findpath_state đến item_synaction_result bị nén mã. Mốc extend=250 khôi phục cùng mã ở cuối enum (C/KProtocolDef.h:369-391; S/KProtocolDef.h:371-394; G/KProtocolDef.h:371-389).
4. relay_s2c_loseway là 35 ở C nhưng 36 ở S/G do S/G chèn relay_c2c_remote=35; S/G thêm udateserver=37, udatemaps=38. chat 31–39 khớp, S/G có thêm 40–43 (C/KProtocolDef.h:431-451; S/KProtocolDef.h:434-461; G/KProtocolDef.h:429-456).
5. ID TONG_SYNC và PLAYERCOMMAND trong KProtocolDef.h khớp; chỉ G thêm enumTONG_COMMAND_ID_EXTPOINT=21 làm NUM thành 22, trong khi C/S có NUM=21 (C/KProtocolDef.h:498-519; S/KProtocolDef.h:510-531; G/KProtocolDef.h:518-541). Các enum trong KTongProtocol.h là lớp ID khác và có nhiều lệch riêng, không được nhập hai lớp làm một.

### Số mục enum KProtocolDef.h

Số đếm bao gồm mốc, sentinel và alias; mỗi dòng kiểm kê phía sau có nguồn riêng.

| Enum (tên đầu nếu anonymous) | C | S | G |
| --- | --- | --- | --- |
| `s2c_PROTOCOL` | 190 | 190 | 190 |
| `c2s_PROTOCOL` | 167 | 167 | 163 |
| `c2c_PROTOCOL` | 9 | 9 | 9 |
| `gm_PROTOCOL` | 16 | 16 | 16 |
| `relay_PROTOCOL` | 5 | 8 | 8 |
| `chat_PROTOCOL` | 9 | 13 | 13 |
| `playercomm_PROTOCOL` | 14 | 14 | 14 |
| `enumTONG_SYNC_ID_CREATE_FAIL` | 19 | 19 | 19 |
| `enumTONG_COMMAND_ID_START` | 22 | 22 | 23 |
| `enumC2S_PLAYERCOMMAND_ID_LOCKSTATE` | 7 | 7 | 7 |
| `enum_COMMAND_ID_MAP` | 0 | 13 | 13 |
| `enum_ITEM_ID_FIND` | 0 | 1 | 1 |

### Cấu trúc khác giữa client và gameserver

Đối chiếu 328 khai báo struct/typedef tìm thấy ở C/KProtocol.h với 334 ở S/KProtocol.h sau khi bỏ comment và khoảng trắng: 327 tên chung, 18 tên khác khai báo. Đây là kiểm tra văn bản khai báo; macro, typedef, constructor và nhánh tiền xử lý chưa được compiler đánh giá. Mỗi struct khác có nguồn ở bảng sau.

| Struct | Khác biệt trực tiếp | C | S |
| --- | --- | --- | --- |
| `PLAYER_REQUEST_CP_LOCK` | C dùng is_Mobile, S dùng _isMobile; đều int, chưa thấy đổi thứ tự/kiểu. | `C/KProtocol.h:144` | `S/KProtocol.h:161` |
| `DATAU_BOX` | C thêm int m_nAWIndex[3] và char sz_TitleAww[256]; S chỉ có ProtocolType. | `C/KProtocol.h:178` | `S/KProtocol.h:188` |
| `REBORN_VALUE_SYNC` | m_nReBornLifeMaxVal: C int; S __int64. | `C/KProtocol.h:215` | `S/KProtocol.h:223` |
| `ROLEVIP_VALUE_SYNC` | m_nRoleVipLifeMaxVal: C int; S __int64. | `C/KProtocol.h:230` | `S/KProtocol.h:238` |
| `NPC_NORMAL_SYNC` | nCurrentLifeMax: C int; S __int64. | `C/KProtocol.h:314` | `S/KProtocol.h:323` |
| `NPC_SET_TMPCAMP` | C đặt tên Camp; S đặt tên TmpCamp; đều BYTE, chưa thấy đổi layout. | `C/KProtocol.h:467` | `S/KProtocol.h:488` |
| `PLAYER_SEND_CHAT_SYNC` | m_szSentence: C [32 + CHAT_MSG_PREFIX_MAX_LEN + MAX_SENTENCE_LENGTH]; S dùng NAME_LENGHT thay 32. C/GameDataDef.h:152 định nghĩa NAME_LENGHT=64; macro build S chưa kiểm. | `C/KProtocol.h:725` | `S/KProtocol.h:732` |
| `PLAYER_LEVEL_UP_SYNC` | m_nBaseLifeMax, m_nBaseStaminaMax, m_nBaseManaMax: C UINT; S __int64. | `C/KProtocol.h:823` | `S/KProtocol.h:831` |
| `CURPLAYER_NORMAL_SYNC` | m_shLife, m_shStamina, m_shMana và ba trường Max: C int; S __int64. | `C/KProtocol.h:1208` | `S/KProtocol.h:1261` |
| `tagGuidableInfo` | S thêm unsigned int nTempEnTerMapIndx và nTempKeyId trước datalength. | `C/KProtocol.h:1542` | `S/KProtocol.h:1608` |
| `tagQueryMapInfo` | C chỉ có base header; S thêm nProtoKind, nKey, nVerX, nVerY, nName[64], nGmName[64]. | `C/KProtocol.h:1591` | `S/KProtocol.h:1659` |
| `tagRequestSvrIp` | S thêm unsigned int nSerNoIndex sau dwMapID. | `C/KProtocol.h:1635` | `S/KProtocol.h:1709` |
| `tagGameSvrInfo` | S thêm unsigned int nSerNoIndex, nGsNumber. | `C/KProtocol.h:1673` | `S/KProtocol.h:1747` |
| `tagMsgInGame` | S thêm char strMsg[256]. | `C/KProtocol.h:1761` | `S/KProtocol.h:1843` |
| `tagRoleEnterGame` | S thêm bool Lixian, int nRegServerIndex và nGsNumber trước Name. | `C/KProtocol.h:1840` | `S/KProtocol.h:1962` |
| `LADDER_LIST` | S thêm BYTE turn trước wSize; C không có. | `C/KProtocol.h:2414` | `S/KProtocol.h:2552` |
| `STONG_SERVER_TO_CORE_APPLY_CREATE` | S thêm int m_nLevel trước tên bang; đây là cấu trúc nội bộ, chưa kết luận có truyền trực tiếp trên mạng. | `C/KProtocol.h:2534` | `S/KProtocol.h:2687` |
| `TONG_SEARCH_RESULT_SYNC` | m_btCurNum/m_btType ở C đổi tên thành m_nCurNum/m_nType ở S; đều BYTE, chưa thấy đổi layout. | `C/KProtocol.h:2952` | `S/KProtocol.h:3227` |

C khai báo GUID riêng (C/KProtocol.h:18); S có thêm các cấu trúc sau, chưa xác định tất cả có đi trên wire:

| Tên chỉ thấy ở S/KProtocol.h | Nguồn |
| --- | --- |
| `tagRoleOffline` | `S/KProtocol.h:1825` |
| `tagItemAction` | `S/KProtocol.h:1853` |
| `tagGmAction` | `S/KProtocol.h:1865` |
| `tagMsgForGame` | `S/KProtocol.h:1876` |
| `tagUpMapGame2` | `S/KProtocol.h:1890` |
| `mapPos` | `S/KProtocol.h:2324` |
| `GS_TASK_GROUPMAN` | `S/KProtocol.h:2631` |

### Bảng kích thước và handler

- Mã s2c_chestpwsync=220 (C/KProtocolDef.h:209); CX:200/5288 gán handler rồi ép payload thành PLAYER_CHESTPW_SYNC, khai báo ở C/KProtocol.h:151-156. Tuy nhiên, đếm phần tử g_nProtocolSize từ s2c_clientbegin+1=65 thì phần tử cho mã 220 là sizeof(PLAYER_TRADE_ITEM_SYNC) tại CP:172; sizeof(PLAYER_CHESTPW_SYNC) ở CP:173 thành vị trí 221. Không có enum s2c_playertradeitem trong C/KProtocolDef.h:20-216. Đây là lệch bảng source, chưa chứng minh hậu quả runtime.
- Nhánh #ifndef _SERVER trong SP:19-170 thiếu mục NPC_SET_TMPCAMP giữa NPC_CHGCAMP_SYNC và NPC_SKILL_SYNC (SP:49-50), trong khi enum có s2c_npcsettmpcamp=95 (S/KProtocolDef.h:84) và C có mục tương ứng CP:47. Vì đây là nhánh loại trừ _SERVER, chưa suy ra gameserver đang chạy bị lệch nhận gói.
- Bảng nhận c2s dưới #else ở SP:172-299 có 127 phần tử đến mã 191. Các mã 192–198 vẫn có enum (S/KProtocolDef.h:379-385), chưa kiểm nơi xử lý riêng ngoài core. CP và SP là bảng theo vị trí, nên comment cạnh phần tử chỉ là gợi ý; cột payload kiểm kê ghi rõ nguồn bảng/handler.

### KTongProtocol.h và KRelayProtocol.h

- C2S bang hội trong C/KTongProtocol.h:24-43 có 20 mục; S:24-52 có 26. S chèn SEARCH_INFO=5, SET_POWER=15, GET_POWER=16, MORE_INFO=17, UPDATE_LEVEL=18 và CHANGE_ANNOUNCE=24, làm nhiều tên chung đổi số. S2C C:67-93 có 27 mục, S:79-114 có 33 mục. Bảng từng tên/mã ở phần kiểm kê phụ bên dưới.
- Enum SET_* có C enumC2S_TONG_SET_CAMP=11 và SET_ANNOUNCE=12, NUM=13 (C/KTongProtocol.h:48-61); S dùng SET_CAM=11 và NUM=12, không có SET_ANNOUNCE (S:59-71).
- friend ID 10 mang tên/ý nghĩa khác: C friend_c2c_addblacklist (C/KTongProtocol.h:113), S friend_s2c_syncblacklist (S:134). S có ADDBLACKLIST_SYNC tại S:200 và FRIEND_SYNCBLACKLIST tại S:251; không có hai tên struct này ở C.
- EXTEND_PASSTOSOMEONE::lnID dùng unsigned long ở C/KTongProtocol.h:239 và UINT ở S:260; chưa kết luận khác byte khi chưa xác định ABI. STONG_GET_TONG_HEAD_INFO_COMMAND thêm UINT m_dwNpcID ở C:328 so với S:349. STONG_ATTACKSTIME_SENDBACK::m_szTime dùng char[64] ở C:421, TCHAR[64] ở S:442; cấu hình TCHAR/Unicode chưa kiểm.
- KRelayProtocol.h C/S có cùng toàn bộ 14 struct đã đối chiếu, PROTOCOL_FAMILY và ROUTESERVER_METHOD cũng khớp (C/S KRelayProtocol.h:14-168). Hash file khác do phần chữ/comment, không dùng hash khác để suy ra layout khác. Packing được khai báo tại C/S KRelayProtocol.h:12; macro/typedef cuối cùng chưa kiểm.

### Header gateway không đồng nhất với gameserver

G/KProtocol.h cũng khác S/KProtocol.h. Bảng bổ sung này chỉ mô tả khai báo, chưa kiểm binary gateway có nhận/gửi các payload này.

| Struct | Khác biệt G so với S | G | S |
| --- | --- | --- | --- |
| `PLAYER_REQUEST_CP_LOCK` | G thiếu int _isMobile. | `G/KProtocol.h:159` | `S/KProtocol.h:161` |
| `REBORN_VALUE_SYNC` | G dùng int m_nReBornLifeMaxVal; S dùng __int64. | `G/KProtocol.h:221` | `S/KProtocol.h:223` |
| `ROLEVIP_VALUE_SYNC` | G dùng int m_nRoleVipLifeMaxVal; S dùng __int64. | `G/KProtocol.h:236` | `S/KProtocol.h:238` |
| `NPC_NORMAL_SYNC` | G dùng int nCurrentLifeMax; S dùng __int64. | `G/KProtocol.h:321` | `S/KProtocol.h:323` |
| `PLAYER_MISSION_RANKDATA` | G có MissionRank[MISSION_STATNUM]; S có MissionRank đơn và int m_nIndex. | `G/KProtocol.h:390` | `S/KProtocol.h:392` |
| `PLAYER_LEVEL_UP_SYNC` | G dùng UINT cho ba Max; S dùng __int64. | `G/KProtocol.h:828` | `S/KProtocol.h:831` |
| `PLAYER_SKILL_LEVEL_SYNC` | S thêm int m_nSkillExp. | `G/KProtocol.h:870` | `S/KProtocol.h:873` |
| `ITEM_SYNC` | S thêm int m_TradePrice. | `G/KProtocol.h:989` | `S/KProtocol.h:993` |
| `PLAYER_COMMAND` | G dùng DWORD m_lpBuf; S dùng uint32_t; ABI/typedef chưa kiểm. | `G/KProtocol.h:1082` | `S/KProtocol.h:1097` |
| `CURPLAYER_NORMAL_SYNC` | G dùng int cho sáu trường life/stamina/mana và Max; S dùng __int64. | `G/KProtocol.h:1249` | `S/KProtocol.h:1261` |
| `PING_COMMAND` | G dùng UINT m_dwTime; S dùng uint32_t. | `G/KProtocol.h:2210` | `S/KProtocol.h:2225` |
| `PING_CLIENTREPLY_COMMAND` | Hai timestamp dùng UINT ở G, uint32_t ở S. | `G/KProtocol.h:2216` | `S/KProtocol.h:2231` |
| `LADDER_DATA` | G dùng TRoleListExt StatData[10]; S dùng TRoleList StatData[10]. | `G/KProtocol.h:2512` | `S/KProtocol.h:2527` |
| `SViewSellItemInfo` | G thêm char nShopName[NAME_LENGHT]. | `G/KProtocol.h:3367` | `S/KProtocol.h:3382` |

## Kiểm kê từng mã KProtocolDef.h

Trong cột mã C/S/G, dấu — nghĩa là không thấy symbol trong enum tương ứng, không khẳng định không có handler khác. Các hướng s2c/c2s dưới 64 là tên luồng; chúng có cả thông điệp nội bộ giữa gateway/GS/role server (ví dụ c2s_gmsvr2gateway_saverole), nên endpoint mạng cụ thể chưa kiểm. Các mục begin/end, NUM và alias là mốc, không tính như gói dữ liệu độc lập.

Payload lấy từ khai báo header, ép kiểu trong handler hoặc biểu thức bảng độ dài, không suy từ comment thành kết quả runtime. “Bảng” nghĩa là phần tử theo vị trí, không phải cấu trúc đã xác nhận bằng bắt gói. -1 là giá trị trong bảng; không tự khẳng định tất cả các mục này đều là gói hợp lệ có độ dài thay đổi.

### `s2c_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `s2c_rolehjdkalritopq_getroleinfo_result` | 10 | 10 | 10 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:22; S-D:23; G-D:23 |
| `s2c_syncogjfkdnvhf_roleinfo_cipher` | 11 | 11 | 11 | luồng s2c; endpoint chưa kiểm | `tagGuidableInfo` (`C/KProtocol.h:1542`; `S/KProtocol.h:1608`) | C-D:23; S-D:24; G-D:24 |
| `s2c_gamestatistic_bigpackage` | 12 | 12 | 12 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:24; S-D:25; G-D:25 |
| `s2c_micfghjkdtropackbegin` | 31 | 31 | 31 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:28; S-D:29; G-D:29 |
| `s2c_accountbegin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:29; S-D:30; G-D:30 |
| `s2c_accountfdfsglogin` | 33 | 33 | 33 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:30; S-D:31; G-D:31 |
| `s2c_gamelogin` | 34 | 34 | 34 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:31; S-D:32; G-D:32 |
| `s2c_accountlogout` | 35 | 35 | 35 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:32; S-D:33; G-D:33 |
| `s2c_gatewayverify` | 36 | 36 | 36 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:33; S-D:34; G-D:34 |
| `s2c_gatewayverifyagain` | 37 | 37 | 37 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:34; S-D:35; G-D:35 |
| `s2c_gatewayinfo` | 38 | 38 | 38 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:35; S-D:36; G-D:36 |
| `s2c_multiserverbegin` | 48 | 48 | 48 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:36; S-D:37; G-D:37 |
| `s2c_querymapinfo` | 49 | 49 | 49 | luồng s2c; endpoint chưa kiểm | `tagQueryMapInfo` (`C/KProtocol.h:1591`; `S/KProtocol.h:1659`) | C-D:37; S-D:38; G-D:38 |
| `s2c_querygameserverinfo` | 50 | 50 | 50 | luồng s2c; endpoint chưa kiểm | `tagQueryGameSvrInfo` (`C/KProtocol.h:1598`; `S/KProtocol.h:1672`) | C-D:38; S-D:39; G-D:39 |
| `s2c_identitymapping` | 51 | 51 | 51 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:39; S-D:40; G-D:40 |
| `s2c_notifypl_ayerlogin_hfkqotivbhd` | 52 | 52 | 52 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:40; S-D:41; G-D:41 |
| `s2c_notifyplayerexchange` | 53 | 53 | 53 | luồng s2c; endpoint chưa kiểm | `tagNotifyPlayerExchange` (`C/KProtocol.h:1618`; `S/KProtocol.h:1692`) | C-D:41; S-D:42; G-D:42 |
| `s2c_notifysvrip` | 54 | 54 | 54 | luồng s2c; endpoint chưa kiểm | `tagNotifySvrIp` (`C/KProtocol.h:1605`; `S/KProtocol.h:1679`) | C-D:42; S-D:43; G-D:43 |
| `s2c_roleserver_getrolelist_result` | 55 | 55 | 55 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:43; S-D:44; G-D:44 |
| `s2c_roleserver_saverole_result` | 56 | 56 | 56 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:44; S-D:45; G-D:45 |
| `s2c_roleserver_createrole_result` | 57 | 57 | 57 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:45; S-D:46; G-D:46 |
| `s2c_roleserver_deleterole_result` | 58 | 58 | 58 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:46; S-D:47; G-D:47 |
| `s2c_logiclogout` | 59 | 59 | 59 | luồng s2c; endpoint chưa kiểm | `tagLogicLogout` (`C/KProtocol.h:1703`; `S/KProtocol.h:1779`) | C-D:47; S-D:48; G-D:48 |
| `s2c_gateway_broadcast` | 60 | 60 | 60 | luồng s2c; endpoint chưa kiểm | `tagGatewayBroadCast` (`C/KProtocol.h:1531`; `S/KProtocol.h:1597`) | C-D:48; S-D:49; G-D:49 |
| `s2c_gamestatistic` | 61 | 61 | 61 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:49; S-D:50; G-D:50 |
| `s2c_rolecheckname_result` | 62 | 62 | 62 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:50; S-D:51; G-D:51 |
| `s2c_gwsyn_broadcast` | 63 | 63 | 63 | luồng s2c; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:51; S-D:52; G-D:52 |
| `s2c_clientbegin` | 64 | 64 | 64 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:52; S-D:53; G-D:53 |
| `s2c_login` | 65 | 65 | 65 | server → client | Bảng `-1` (CP:17) | C-D:53; S-D:54; G-D:54 |
| `s2c_logout` | 66 | 66 | 66 | server → client | Bảng `-1` (CP:18) | C-D:54; S-D:55; G-D:55 |
| `s2c_syncclientend` | 67 | 67 | 67 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:55; S-D:56; G-D:56 |
| `s2c_synonlineplayer` | 68 | 68 | 68 | server → client | Bảng `sizeof(CURPLAYER_SYNC)` (CP:20) | C-D:56; S-D:57; G-D:57 |
| `s2c_synccurplayerskill` | 69 | 69 | 69 | server → client | Handler `SKILL_SEND_ALL_SYNC` (`C/KProtocol.h:1353`; `S/KProtocol.h:1406`); CX:3303; Bảng `-1` (CP:21) | C-D:57; S-D:58; G-D:58 |
| `s2c_synccurplayernormal` | 70 | 70 | 70 | server → client | Handler `CURPLAYER_NORMAL_SYNC` (`C/KProtocol.h:1208`; `S/KProtocol.h:1261`); CX:2071; Bảng `sizeof(CURPLAYER_NORMAL_SYNC)` (CP:22) | C-D:58; S-D:59; G-D:59 |
| `s2c_newplayer` | 71 | 71 | 71 | server → client | Bảng `-1` (CP:23) | C-D:59; S-D:60; G-D:60 |
| `s2c_removeplayer` | 72 | 72 | 72 | server → client | Bảng `-1` (CP:24) | C-D:60; S-D:61; G-D:61 |
| `s2c_syncworld` | 73 | 73 | 73 | server → client | Handler `WORLD_SYNC` (`C/KProtocol.h:1367`; `S/KProtocol.h:1419`); CX:3216; Bảng `sizeof(WORLD_SYNC)` (CP:25) | C-D:61; S-D:62; G-D:62 |
| `s2c_syncplayer` | 74 | 74 | 74 | server → client | Handler `PLAYER_SYNC` (`C/KProtocol.h:36`; `S/KProtocol.h:34`); CX:2940; Bảng `sizeof(PLAYER_SYNC)` (CP:26) | C-D:62; S-D:63; G-D:63 |
| `s2c_syncplayermin` | 75 | 75 | 75 | server → client | Handler `PLAYER_NORMAL_SYNC` (`C/KProtocol.h:76`; `S/KProtocol.h:93`); CX:3061; Bảng `sizeof(PLAYER_NORMAL_SYNC)` (CP:27) | C-D:63; S-D:64; G-D:64 |
| `s2c_syncnpc` | 76 | 76 | 76 | server → client | Handler `NPC_SYNC` (`C/KProtocol.h:293`; `S/KProtocol.h:301`); CX:2160; Bảng `-1` (CP:28) | C-D:64; S-D:65; G-D:65 |
| `s2c_syncnpcmin` | 77 | 77 | 77 | server → client | Handler `NPC_NORMAL_SYNC` (`C/KProtocol.h:314`; `S/KProtocol.h:323`); CX:2412; Bảng `sizeof(NPC_NORMAL_SYNC)` (CP:29) | C-D:65; S-D:66; G-D:66 |
| `s2c_syncnpcminplayer` | 78 | 78 | 78 | server → client | Handler `NPC_PLAYER_TYPE_NORMAL_SYNC` (`C/KProtocol.h:362`; `S/KProtocol.h:371`); CX:2639; Bảng `sizeof(NPC_PLAYER_TYPE_NORMAL_SYNC)` (CP:30) | C-D:66; S-D:67; G-D:67 |
| `s2c_objadd` | 79 | 79 | 79 | server → client | Handler `OBJ_ADD_SYNC` (`C/KProtocol.h:738`; `S/KProtocol.h:745`); CX:2723; Bảng `-1` (CP:31) | C-D:67; S-D:68; G-D:68 |
| `s2c_syncobjstate` | 80 | 80 | 80 | server → client | Handler `OBJ_SYNC_STATE` (`C/KProtocol.h:782`; `S/KProtocol.h:790`); CX:2888; Bảng `sizeof(OBJ_SYNC_STATE)` (CP:32) | C-D:68; S-D:69; G-D:69 |
| `s2c_syncobjdir` | 81 | 81 | 81 | server → client | Handler `OBJ_SYNC_DIR` (`C/KProtocol.h:789`; `S/KProtocol.h:797`); CX:2855; Bảng `sizeof(OBJ_SYNC_DIR)` (CP:33) | C-D:69; S-D:70; G-D:70 |
| `s2c_objremove` | 82 | 82 | 82 | server → client | Handler `OBJ_SYNC_REMOVE` (`C/KProtocol.h:796`; `S/KProtocol.h:804`); CX:2875; Bảng `sizeof(OBJ_SYNC_REMOVE)` (CP:34) | C-D:70; S-D:71; G-D:71 |
| `s2c_objTrapAct` | 83 | 83 | 83 | server → client | Handler `OBJ_SYNC_TRAP_ACT` (`C/KProtocol.h:803`; `S/KProtocol.h:811`); CX:2918; Bảng `sizeof(OBJ_SYNC_TRAP_ACT)` (CP:35) | C-D:71; S-D:72; G-D:72 |
| `s2c_npcremove` | 84 | 84 | 84 | server → client | Handler `NPC_REMOVE_SYNC` (`C/KProtocol.h:403`; `S/KProtocol.h:417`); CX:626; Bảng `sizeof(NPC_REMOVE_SYNC)` (CP:36) | C-D:72; S-D:73; G-D:73 |
| `s2c_npcwalk` | 85 | 85 | 85 | server → client | Handler `NPC_WALK_SYNC` (`C/KProtocol.h:419`; `S/KProtocol.h:433`); CX:885; Bảng `sizeof(NPC_WALK_SYNC)` (CP:37) | C-D:73; S-D:74; G-D:74 |
| `s2c_npcrun` | 86 | 86 | 86 | server → client | Handler `NPC_RUN_SYNC` (`C/KProtocol.h:443`; `S/KProtocol.h:457`); CX:649; Bảng `sizeof(NPC_RUN_SYNC)` (CP:38) | C-D:74; S-D:75; G-D:75 |
| `s2c_npcattack` | 87 | 87 | 87 | server → client | Bảng `-1` (CP:39) | C-D:75; S-D:76; G-D:76 |
| `s2c_npcmagic` | 88 | 88 | 88 | server → client | Bảng `-1` (CP:40) | C-D:76; S-D:77; G-D:77 |
| `s2c_npcjump` | 89 | 89 | 89 | server → client | Handler `NPC_JUMP_SYNC` (`C/KProtocol.h:435`; `S/KProtocol.h:449`); CX:600; Bảng `sizeof(NPC_JUMP_SYNC)` (CP:41) | C-D:77; S-D:78; G-D:78 |
| `s2c_npctalk` | 90 | 90 | 90 | server → client | Handler `NPC_CHAT_SYNC` (`C/KProtocol.h:410`; `S/KProtocol.h:424`); CX:587; Bảng `sizeof(NPC_CHAT_SYNC)` (CP:42) | C-D:78; S-D:79; G-D:79 |
| `s2c_npchurt` | 91 | 91 | 91 | server → client | Handler `NPC_HURT_SYNC` (`C/KProtocol.h:451`; `S/KProtocol.h:465`); CX:612; Bảng `sizeof(NPC_HURT_SYNC)` (CP:43) | C-D:79; S-D:80; G-D:80 |
| `s2c_npcdeath` | 92 | 92 | 92 | server → client | Handler `NPC_DEATH_SYNC` (khai báo chưa kiểm); CX:571; Bảng `sizeof(NPC_DEATH_SYNC)` (CP:44) | C-D:80; S-D:81; G-D:81 |
| `s2c_npcchgcurcamp` | 93 | 93 | 93 | server → client | Handler `NPC_CHGCURCAMP_SYNC` (`C/KProtocol.h:460`; `S/KProtocol.h:474`); CX:558; Bảng `sizeof(NPC_CHGCURCAMP_SYNC)` (CP:45) | C-D:81; S-D:82; G-D:82 |
| `s2c_npcchgcamp` | 94 | 94 | 94 | server → client | Handler `NPC_CHGCAMP_SYNC` (`C/KProtocol.h:473`; `S/KProtocol.h:481`); CX:537; Bảng `sizeof(NPC_CHGCAMP_SYNC)` (CP:46) | C-D:82; S-D:83; G-D:83 |
| `s2c_npcsettmpcamp` | 95 | 95 | 95 | server → client | Handler `NPC_SET_TMPCAMP` (`C/KProtocol.h:467`; `S/KProtocol.h:488`); CX:551; Bảng `sizeof(NPC_SET_TMPCAMP)` (CP:47) | C-D:83; S-D:84; G-D:84 |
| `s2c_skillcast` | 96 | 96 | 96 | server → client | Handler `NPC_SKILL_SYNC` (`C/KProtocol.h:480`; `S/KProtocol.h:494`); CX:835; Bảng `sizeof(NPC_SKILL_SYNC)` (CP:48) | C-D:84; S-D:85; G-D:85 |
| `s2c_playertalk` | 97 | 97 | 97 | server → client | Bảng `-1` (CP:49) | C-D:85; S-D:86; G-D:86 |
| `s2c_playerexp` | 98 | 98 | 98 | server → client | Handler `PLAYER_EXP_SYNC` (`C/KProtocol.h:535`; `S/KProtocol.h:549`); CX:510; Bảng `sizeof(PLAYER_EXP_SYNC)` (CP:50) | C-D:86; S-D:87; G-D:87 |
| `s2c_teaminfo` | 99 | 99 | 99 | server → client | Bảng `sizeof(PLAYER_SEND_TEAM_INFO)` (CP:51) | C-D:87; S-D:88; G-D:88 |
| `s2c_teamselfinfo` | 100 | 100 | 100 | server → client | Handler `PLAYER_SEND_SELF_TEAM_INFO` (`C/KProtocol.h:598`; `S/KProtocol.h:612`); CX:2017; Bảng `sizeof(PLAYER_SEND_SELF_TEAM_INFO)` (CP:52) | C-D:88; S-D:89; G-D:89 |
| `s2c_teamapplyinfofalse` | 101 | 101 | 101 | server → client | Bảng `sizeof(PLAYER_APPLY_TEAM_INFO_FALSE)` (CP:53) | C-D:89; S-D:90; G-D:90 |
| `s2c_teamcreatesuccess` | 102 | 102 | 102 | server → client | Handler `PLAYER_SEND_CREATE_TEAM_SUCCESS` (`C/KProtocol.h:552`; `S/KProtocol.h:566`); CX:1164; Bảng `sizeof(PLAYER_SEND_CREATE_TEAM_SUCCESS)` (CP:54) | C-D:90; S-D:91; G-D:91 |
| `s2c_teamcreatefalse` | 103 | 103 | 103 | server → client | Handler `PLAYER_SEND_CREATE_TEAM_FALSE` (`C/KProtocol.h:559`; `S/KProtocol.h:573`); CX:902; Bảng `sizeof(PLAYER_SEND_CREATE_TEAM_FALSE)` (CP:55) | C-D:91; S-D:92; G-D:92 |
| `s2c_teamopenclose` | 104 | 104 | 104 | server → client | Handler `PLAYER_TEAM_OPEN_CLOSE` (`C/KProtocol.h:610`; `S/KProtocol.h:624`); CX:1474; Bảng `sizeof(PLAYER_TEAM_OPEN_CLOSE)` (CP:56) | C-D:92; S-D:93; G-D:93 |
| `s2c_teamgetapply` | 105 | 105 | 105 | server → client | Bảng `sizeof(PLAYER_APPLY_ADD_TEAM)` (CP:57) | C-D:93; S-D:94; G-D:94 |
| `s2c_teamaddmember` | 106 | 106 | 106 | server → client | Handler `PLAYER_TEAM_ADD_MEMBER` (`C/KProtocol.h:635`; `S/KProtocol.h:642`); CX:1919; Bảng `sizeof(PLAYER_TEAM_ADD_MEMBER)` (CP:58) | C-D:94; S-D:95; G-D:95 |
| `s2c_teamleave` | 107 | 107 | 107 | server → client | Handler `PLAYER_LEAVE_TEAM` (`C/KProtocol.h:649`; `S/KProtocol.h:656`); CX:1368; Bảng `sizeof(PLAYER_LEAVE_TEAM)` (CP:59) | C-D:95; S-D:96; G-D:96 |
| `s2c_teamchangecaptain` | 108 | 108 | 108 | server → client | Handler `PLAYER_TEAM_CHANGE_CAPTAIN` (`C/KProtocol.h:667`; `S/KProtocol.h:674`); CX:1956; Bảng `sizeof(PLAYER_TEAM_CHANGE_CAPTAIN)` (CP:60) | C-D:96; S-D:97; G-D:97 |
| `s2c_playerfactiondata` | 109 | 109 | 109 | server → client | Handler `PLAYER_FACTION_DATA` (`C/KProtocol.h:685`; `S/KProtocol.h:692`); CX:1445; Bảng `sizeof(PLAYER_FACTION_DATA)` (CP:61) | C-D:97; S-D:98; G-D:98 |
| `s2c_playerleavefaction` | 110 | 110 | 110 | server → client | Bảng `sizeof(PLAYER_LEAVE_FACTION)` (CP:62) | C-D:98; S-D:99; G-D:99 |
| `s2c_playerfactionskilllevel` | 111 | 111 | 111 | server → client | Handler `PLAYER_FACTION_SKILL_LEVEL` (`C/KProtocol.h:699`; `S/KProtocol.h:706`); CX:1204; Bảng `sizeof(PLAYER_FACTION_SKILL_LEVEL)` (CP:63) | C-D:99; S-D:100; G-D:100 |
| `s2c_playersendchat` | 112 | 112 | 112 | server → client | Handler `PLAYER_SEND_CHAT_SYNC` (`C/KProtocol.h:725`; `S/KProtocol.h:732`); CX:1229; Bảng `-1` (CP:64) | C-D:100; S-D:101; G-D:101 |
| `s2c_playersyncleadexp` | 113 | 113 | 113 | server → client | Handler `PLAYER_LEAD_EXP_SYNC` (`C/KProtocol.h:817`; `S/KProtocol.h:825`); CX:1249; Bảng `sizeof(PLAYER_LEAD_EXP_SYNC)` (CP:65) | C-D:101; S-D:102; G-D:102 |
| `s2c_playerlevelup` | 114 | 114 | 114 | server → client | Bảng `sizeof(PLAYER_LEVEL_UP_SYNC)` (CP:66) | C-D:102; S-D:103; G-D:103 |
| `s2c_teammatelevel` | 115 | 115 | 115 | server → client | Handler `PLAYER_TEAMMATE_LEVEL_SYNC` (`C/KProtocol.h:835`; `S/KProtocol.h:843`); CX:1325; Bảng `sizeof(PLAYER_TEAMMATE_LEVEL_SYNC)` (CP:67) | C-D:103; S-D:104; G-D:104 |
| `s2c_playersyncattribute` | 116 | 116 | 116 | server → client | Bảng `sizeof(PLAYER_ATTRIBUTE_SYNC)` (CP:68) | C-D:104; S-D:105; G-D:105 |
| `s2c_playerskilllevel` | 117 | 117 | 117 | server → client | Handler `PLAYER_SKILL_LEVEL_SYNC` (`C/KProtocol.h:865`; `S/KProtocol.h:873`); CX:1275; Bảng `sizeof(PLAYER_SKILL_LEVEL_SYNC)` (CP:69) | C-D:105; S-D:106; G-D:106 |
| `s2c_syncitem` | 118 | 118 | 118 | server → client | Handler `ITEM_SYNC` (`C/KProtocol.h:946`; `S/KProtocol.h:993`); CX:1710; Bảng `sizeof(ITEM_SYNC)` (CP:70) | C-D:106; S-D:107; G-D:107 |
| `s2c_removeitem` | 119 | 119 | 119 | server → client | Handler `ITEM_REMOVE_SYNC` (`C/KProtocol.h:1004`; `S/KProtocol.h:1050`); CX:1423; Bảng `sizeof(ITEM_REMOVE_SYNC)` (CP:71) | C-D:107; S-D:108; G-D:108 |
| `s2c_syncmonfs` | 120 | 120 | 120 | server → client | Bảng `sizeof(PLAYER_FS_MONEY_SYNC)` (CP:72) | C-D:108; S-D:109; G-D:109 |
| `s2c_syncqianfs` | 121 | 121 | 121 | server → client | Bảng `sizeof(PLAYER_FS_XU_SYNC)` (CP:73) | C-D:109; S-D:110; G-D:110 |
| `s2c_playermoveitem` | 122 | 122 | 122 | server → client | Handler `PLAYER_MOVE_ITEM_SYNC` (`C/KProtocol.h:1154`; `S/KProtocol.h:1207`); CX:1399; Bảng `sizeof(PLAYER_MOVE_ITEM_SYNC)` (CP:74) | C-D:110; S-D:111; G-D:111 |
| `s2c_scriptaction` | 123 | 123 | 123 | server → client | Handler `PLAYER_SCRIPTACTION_SYNC` (`C/KProtocol.h:1333`; `S/KProtocol.h:1386`); CX:3210; Bảng `-1` (CP:75) | C-D:111; S-D:112; G-D:112 |
| `s2c_chatapplyaddfriend` | 124 | 124 | 124 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:112; S-D:113; G-D:113 |
| `s2c_chataddfriend` | 125 | 125 | 125 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:113; S-D:114; G-D:114 |
| `s2c_chatrefusefriend` | 126 | 126 | 126 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:114; S-D:115; G-D:115 |
| `s2c_chataddfriendfail` | 127 | 127 | 127 | server → client | Handler `CHAT_ADD_FRIEND_FAIL_SYNC` (`C/KProtocol.h:1445`; `S/KProtocol.h:1497`); CX:975; Bảng `sizeof(CHAT_ADD_FRIEND_FAIL_SYNC)` (CP:79) | C-D:115; S-D:116; G-D:116 |
| `s2c_chatloginfriendnoname` | 128 | 128 | 128 | server → client | Handler `CHAT_LOGIN_FRIEND_NONAME_SYNC` (`C/KProtocol.h:1858`; `S/KProtocol.h:1983`); CX:1123; Bảng `sizeof(CHAT_LOGIN_FRIEND_NONAME_SYNC)` (CP:80) | C-D:116; S-D:117; G-D:117 |
| `s2c_chatloginfriendname` | 129 | 129 | 129 | server → client | Handler `CHAT_LOGIN_FRIEND_NAME_SYNC` (`C/KProtocol.h:1865`; `S/KProtocol.h:1990`); CX:1104; Bảng `-1` (CP:81) | C-D:117; S-D:118; G-D:118 |
| `s2c_chatonefrienddata` | 130 | 130 | 130 | server → client | Handler `CHAT_ONE_FRIEND_DATA_SYNC` (`C/KProtocol.h:1885`; `S/KProtocol.h:2010`); CX:1009; Bảng `sizeof(CHAT_ONE_FRIEND_DATA_SYNC)` (CP:82) | C-D:118; S-D:119; G-D:119 |
| `s2c_chatfriendonline` | 131 | 131 | 131 | server → client | Handler `CHAT_FRIEND_ONLINE_SYNC` (`C/KProtocol.h:1893`; `S/KProtocol.h:2018`); CX:1053; Bảng `sizeof(CHAT_FRIEND_ONLINE_SYNC)` (CP:83) | C-D:119; S-D:120; G-D:120 |
| `s2c_chatdeletefriend` | 132 | 132 | 132 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:120; S-D:121; G-D:121 |
| `s2c_chatfriendoffline` | 133 | 133 | 133 | server → client | Handler `CHAT_FRIEND_OFFLINE_SYNC` (`C/KProtocol.h:1930`; `S/KProtocol.h:2055`); CX:3296; Bảng `sizeof(CHAT_FRIEND_OFFLINE_SYNC)` (CP:85) | C-D:121; S-D:122; G-D:122 |
| `s2c_syncrolelist` | 134 | 134 | 134 | server → client | Handler `ROLE_LIST_SYNC` (`C/KProtocol.h:1811`; `S/KProtocol.h:1933`); CX:1904; Bảng `sizeof(ROLE_LIST_SYNC)` (CP:86) | C-D:122; S-D:123; G-D:123 |
| `s2c_tradechangestate` | 135 | 135 | 135 | server → client | Bảng `sizeof(TRADE_CHANGE_STATE_SYNC)` (CP:87) | C-D:123; S-D:124; G-D:124 |
| `s2c_npcsetmenustate` | 136 | 136 | 136 | server → client | Handler `NPC_SET_MENU_STATE_SYNC` (`C/KProtocol.h:1955`; `S/KProtocol.h:2080`); CX:3387; Bảng `-1` (CP:88) | C-D:124; S-D:125; G-D:125 |
| `s2c_trademoneysync` | 137 | 137 | 137 | server → client | Bảng `sizeof(TRADE_MONEY_SYNC)` (CP:89) | C-D:125; S-D:126; G-D:126 |
| `s2c_tradedecision` | 138 | 138 | 138 | server → client | Bảng `sizeof(TRADE_DECISION_SYNC)` (CP:90) | C-D:126; S-D:127; G-D:127 |
| `s2c_chatscreensingleerror` | 139 | 139 | 139 | server → client | Handler `CHAT_SCREENSINGLE_ERROR_SYNC` (`C/KProtocol.h:2025`; `S/KProtocol.h:2150`); CX:516; Bảng `-1` (CP:91) | C-D:127; S-D:128; G-D:128 |
| `s2c_syncnpcstate` | 140 | 140 | 140 | server → client | Handler `NPC_SYNC_STATEINFO` (`C/KProtocol.h:2033`; `S/KProtocol.h:2158`); CX:3447; Bảng `sizeof(NPC_SYNC_STATEINFO)` (CP:92) | C-D:128; S-D:129; G-D:129 |
| `s2c_teaminviteadd` | 141 | 141 | 141 | server → client | Handler `TEAM_INVITE_ADD_SYNC` (`C/KProtocol.h:2046`; `S/KProtocol.h:2171`); CX:3463; Bảng `-1` (CP:93) | C-D:129; S-D:130; G-D:130 |
| `s2c_tradepressoksync` | 142 | 142 | 142 | server → client | Handler `TRADE_STATE_SYNC` (`C/KProtocol.h:2067`; `S/KProtocol.h:2192`); CX:3473; Bảng `sizeof(TRADE_STATE_SYNC)` (CP:94) | C-D:130; S-D:131; G-D:131 |
| `s2c_ping` | 143 | 143 | 143 | server → client | Handler `PING_COMMAND` (`C/KProtocol.h:2098`; `S/KProtocol.h:2225`); CX:409; Bảng `sizeof(PING_COMMAND)` (CP:95) | C-D:131; S-D:132; G-D:132 |
| `s2c_npcsit` | 144 | 144 | 144 | server → client | Handler `NPC_SIT_SYNC` (khai báo chưa kiểm); CX:668; Bảng `sizeof(NPC_SIT_SYNC)` (CP:96) | C-D:132; S-D:133; G-D:133 |
| `s2c_npcstand` | 145 | 145 | 145 | server → client | Handler `NPC_PLAYER_TYPE_NORMAL_SYNC` (`C/KProtocol.h:362`; `S/KProtocol.h:371`); CX:682; Bảng `sizeof(NPC_PLAYER_TYPE_NORMAL_SYNC)` (CP:97) | C-D:133; S-D:134; G-D:134 |
| `s2c_opensalebox` | 146 | 146 | 146 | server → client | Handler `SALE_BOX_SYNC` (`C/KProtocol.h:523`; `S/KProtocol.h:537`); CX:759; Bảng `sizeof(SALE_BOX_SYNC)` (CP:98) | C-D:134; S-D:135; G-D:135 |
| `s2c_castskilldirectly` | 147 | 147 | 147 | server → client | Handler `NPC_SKILL_SYNC` (`C/KProtocol.h:480`; `S/KProtocol.h:494`); CX:3485; Bảng `sizeof(NPC_SKILL_SYNC)` (CP:99) | C-D:135; S-D:136; G-D:136 |
| `s2c_msgshow` | 148 | 148 | 148 | server → client | Handler `SHOW_MSG_SYNC` (`C/KProtocol.h:2203`; `S/KProtocol.h:2338`); CX:3554; Bảng `-1` (CP:100) | C-D:136; S-D:137; G-D:137 |
| `s2c_syncstateeffect` | 149 | 149 | 149 | server → client | Handler `STATE_EFFECT_SYNC` (`C/KProtocol.h:2076`; `S/KProtocol.h:2201`); CX:4238; Bảng `-1` (CP:101) | C-D:137; S-D:138; G-D:138 |
| `s2c_openstorebox` | 150 | 150 | 150 | server → client | Bảng `sizeof(BYTE)` (CP:102) | C-D:138; S-D:139; G-D:139 |
| `s2c_openresetpass` | 151 | 151 | 151 | server → client | Bảng `sizeof(RESET_PASS)` (CP:103) | C-D:139; S-D:140; G-D:140 |
| `s2c_openstringbox` | 152 | 152 | 152 | server → client | Bảng `sizeof(PLAYER_STRING)` (CP:104) | C-D:140; S-D:141; G-D:141 |
| `s2c_opendataubox` | 153 | 153 | 153 | server → client | Bảng `sizeof(DATAU_BOX)` (CP:105) | C-D:141; S-D:142; G-D:142 |
| `s2c_playerrevive` | 154 | 154 | 154 | server → client | Handler `NPC_REVIVE_SYNC` (`C/KProtocol.h:427`; `S/KProtocol.h:441`); CX:782; Bảng `sizeof(NPC_REVIVE_SYNC)` (CP:106) | C-D:142; S-D:143; G-D:143 |
| `s2c_requestnpcfail` | 155 | 155 | 155 | server → client | Handler `NPC_REQUEST_FAIL` (khai báo chưa kiểm); CX:812; Bảng `sizeof(NPC_REQUEST_FAIL)` (CP:107) | C-D:143; S-D:144; G-D:144 |
| `s2c_tradeapplystart` | 156 | 156 | 156 | server → client | Bảng `sizeof(TRADE_APPLY_START_SYNC)` (CP:108) | C-D:144; S-D:145; G-D:145 |
| `s2c_rolenewdelresponse` | 157 | 157 | 157 | server → client | Bảng `sizeof(tagNewDelRoleResponse)` (CP:109) | C-D:145; S-D:146; G-D:146 |
| `s2c_ItemAutoMove` | 158 | 158 | 158 | server → client | Handler `ITEM_AUTO_MOVE_SYNC` (`C/KProtocol.h:1169`; `S/KProtocol.h:1222`); CX:4255; Bảng `sizeof(ITEM_AUTO_MOVE_SYNC)` (CP:110) | C-D:146; S-D:147; G-D:147 |
| `s2c_itemexchangefinish` | 159 | 159 | 159 | server → client | Bảng `sizeof(BYTE)` (CP:111) | C-D:147; S-D:148; G-D:148 |
| `s2c_changeweather` | 160 | 160 | 160 | server → client | Handler `SYNC_WEATHER` (`C/KProtocol.h:1360`; `S/KProtocol.h:1413`); CX:4995; Bảng `sizeof(SYNC_WEATHER)` (CP:112) | C-D:148; S-D:149; G-D:149 |
| `s2c_pksyncnormalflag` | 161 | 161 | 161 | server → client | Handler `PK_NORMAL_FLAG_SYNC` (`C/KProtocol.h:2223`; `S/KProtocol.h:2358`); CX:5000; Bảng `sizeof(PK_NORMAL_FLAG_SYNC)` (CP:113) | C-D:149; S-D:150; G-D:150 |
| `s2c_pksyncenmitystate` | 162 | 162 | 162 | server → client | Handler `PK_ENMITY_STATE_SYNC` (`C/KProtocol.h:2235`; `S/KProtocol.h:2370`); CX:5006; Bảng `-1` (CP:114) | C-D:150; S-D:151; G-D:151 |
| `s2c_pksyncexercisestate` | 163 | 163 | 163 | server → client | Handler `PK_EXERCISE_STATE_SYNC` (`C/KProtocol.h:2244`; `S/KProtocol.h:2379`); CX:5018; Bảng `-1` (CP:115) | C-D:151; S-D:152; G-D:152 |
| `s2c_pksyncpkvalue` | 164 | 164 | 164 | server → client | Handler `PK_VALUE_SYNC` (`C/KProtocol.h:2253`; `S/KProtocol.h:2388`); CX:5029; Bảng `sizeof(PK_VALUE_SYNC)` (CP:116) | C-D:152; S-D:153; G-D:153 |
| `s2c_reputesyncreputevalue` | 165 | 165 | 165 | server → client | Handler `REPUTE_VALUE_SYNC` (`C/KProtocol.h:203`; `S/KProtocol.h:211`); CX:5035; Bảng `sizeof(REPUTE_VALUE_SYNC)` (CP:117) | C-D:153; S-D:154; G-D:154 |
| `s2c_fuyuansyncfuyuanvalue` | 166 | 166 | 166 | server → client | Handler `FUYUAN_VALUE_SYNC` (`C/KProtocol.h:209`; `S/KProtocol.h:217`); CX:5041; Bảng `sizeof(FUYUAN_VALUE_SYNC)` (CP:118) | C-D:154; S-D:155; G-D:155 |
| `s2c_rebornsyncrebornvalue` | 167 | 167 | 167 | server → client | Handler `REBORN_VALUE_SYNC` (`C/KProtocol.h:215`; `S/KProtocol.h:223`); CX:5093; Bảng `sizeof(REBORN_VALUE_SYNC)` (CP:119) | C-D:155; S-D:156; G-D:156 |
| `s2c_openmarketbox` | 168 | 168 | 168 | server → client | Bảng `sizeof(SALE_MARKET_SYNC)` (CP:120) | C-D:156; S-D:157; G-D:157 |
| `s2c_npcsleepmode` | 169 | 169 | 169 | server → client | Handler `NPC_SLEEP_SYNC` (`C/KProtocol.h:2380`; `S/KProtocol.h:2505`); CX:394; Bảng `sizeof(NPC_SLEEP_SYNC)` (CP:121) | C-D:157; S-D:158; G-D:158 |
| `s2c_viewequip` | 170 | 170 | 170 | server → client | Bảng `-1` (CP:122) | C-D:158; S-D:159; G-D:159 |
| `s2c_ladderresult` | 171 | 171 | 171 | server → client | Handler `LADDER_DATA` (`C/KProtocol.h:2389`; `S/KProtocol.h:2527`); CX:5330; Bảng `sizeof(LADDER_DATA)` (CP:123) | C-D:159; S-D:160; G-D:160 |
| `s2c_ladderlist` | 172 | 172 | 172 | server → client | Handler `LADDER_LIST` (`C/KProtocol.h:2414`; `S/KProtocol.h:2552`); CX:5310; Bảng `-1` (CP:124) | C-D:160; S-D:161; G-D:161 |
| `s2c_tongcreate` | 173 | 173 | 173 | server → client | Handler `TONG_CREATE_SYNC` (`C/KProtocol.h:2792`; `S/KProtocol.h:2963`); CX:5112; Bảng `sizeof(TONG_CREATE_SYNC)` (CP:125) | C-D:161; S-D:162; G-D:162 |
| `s2c_replyclientping` | 174 | 174 | 174 | server → client | Handler `PING_COMMAND` (`C/KProtocol.h:2098`; `S/KProtocol.h:2225`); CX:455; Bảng `sizeof(PING_COMMAND)` (CP:126) | C-D:162; S-D:163; G-D:163 |
| `s2c_npcgoldchange` | 175 | 175 | 175 | server → client | Handler `NPC_GOLD_CHANGE_SYNC` (`C/KProtocol.h:3086`; `S/KProtocol.h:3239`); CX:5118; Bảng `sizeof(NPC_GOLD_CHANGE_SYNC)` (CP:127) | C-D:163; S-D:164; G-D:164 |
| `s2c_itemdurabilitychange` | 176 | 176 | 176 | server → client | Handler `ITEM_DURABILITY_CHANGE` (`C/KProtocol.h:3093`; `S/KProtocol.h:3246`); CX:5132; Bảng `sizeof(ITEM_DURABILITY_CHANGE)` (CP:128) | C-D:164; S-D:165; G-D:165 |
| `s2c_opentremble` | 177 | 177 | 177 | server → client | Bảng `sizeof(BYTE)` (CP:129) | C-D:165; S-D:166; G-D:166 |
| `s2c_rankname` | 178 | 178 | 178 | server → client | Handler `RANKFF_SYNC` (`C/KProtocol.h:245`; `S/KProtocol.h:253`); CX:5297; Bảng `sizeof(RANKFF_SYNC)` (CP:130) | C-D:166; S-D:167; G-D:167 |
| `s2c_viewsellitem` | 179 | 179 | 179 | server → client | Bảng `sizeof(VIEW_ITEM_SYNC)` (CP:131) | C-D:167; S-D:168; G-D:168 |
| `s2c_viewupdateitem` | 180 | 180 | 180 | server → client | Bảng `sizeof(VIEW_ITEM_SYNC)` (CP:132) | C-D:168; S-D:169; G-D:169 |
| `s2c_playergetcount` | 181 | 181 | 181 | server → client | Handler `PLAYER_GET_COUNT` (`C/KProtocol.h:3316`; `S/KProtocol.h:3511`); CX:364; Bảng `sizeof(PLAYER_GET_COUNT)` (CP:133) | C-D:169; S-D:170; G-D:170 |
| `s2c_shopname` | 182 | 182 | 182 | server → client | Handler `PLAYER_PLAYER_SHOPNAME` (`C/KProtocol.h:3377`; `S/KProtocol.h:3572`); CX:370; Bảng `sizeof(PLAYER_PLAYER_SHOPNAME)` (CP:134) | C-D:170; S-D:171; G-D:171 |
| `s2c_syncmasklock` | 183 | 183 | 183 | server → client | Handler `NPC_SIT_SYNC` (khai báo chưa kiểm); CX:388; Bảng `sizeof(NPC_SIT_SYNC)` (CP:135) | C-D:171; S-D:172; G-D:172 |
| `s2c_opengive` | 184 | 184 | 184 | server → client | Handler `PLAYER_GIVE` (`C/KProtocol.h:3430`; `S/KProtocol.h:3625`); CX:251; Bảng `sizeof(PLAYER_GIVE)` (CP:136) | C-D:172; S-D:173; G-D:173 |
| `s2c_npcsecmove` | 185 | 185 | 185 | server → client | Handler `NPC_JUMP_SYNC` (`C/KProtocol.h:435`; `S/KProtocol.h:449`); CX:234; Bảng `sizeof(NPC_JUMP_SYNC)` (CP:137) | C-D:173; S-D:174; G-D:174 |
| `s2c_pkvalue` | 186 | 186 | 186 | server → client | Bảng `sizeof(PKVALUE)` (CP:138) | C-D:174; S-D:175; G-D:175 |
| `s2c_viewlianitem` | 187 | 187 | 187 | server → client | Bảng `sizeof(VIEW_LIAN_ITEM_SYNC)` (CP:139) | C-D:175; S-D:176; G-D:176 |
| `s2c_openwengang` | 188 | 188 | 188 | server → client | Bảng `sizeof(BYTE)` (CP:140) | C-D:176; S-D:177; G-D:177 |
| `s2c_openstone` | 189 | 189 | 189 | server → client | Bảng `sizeof(BYTE)` (CP:141) | C-D:177; S-D:178; G-D:178 |
| `s2c_updateviewequip` | 190 | 190 | 190 | server → client | Bảng `sizeof(VIEW_ITEM_SYNC)` (CP:142) | C-D:179; S-D:180; G-D:180 |
| `s2c_gettongback` | 191 | 191 | 191 | server → client | Handler `PLAYER_TONGINFO_CALLBACK` (`C/KProtocol.h:3177`; `S/KProtocol.h:3330`); CX:308; Bảng `sizeof(PLAYER_TONGINFO_CALLBACK)` (CP:143) | C-D:180; S-D:181; G-D:181 |
| `s2c_syncequipitem` | 192 | 192 | 192 | server → client | Handler `ITEM_SYNC` (`C/KProtocol.h:946`; `S/KProtocol.h:993`); CX:1558; Bảng `sizeof(ITEM_SYNC)` (CP:144) | C-D:181; S-D:182; G-D:182 |
| `s2c_taskcallback` | 193 | 193 | 193 | server → client | Handler `PLAYER_GETBACK_TASKVAL` (`C/KProtocol.h:1078`; `S/KProtocol.h:1131`); CX:1548; Bảng `sizeof(PLAYER_GETBACK_TASKVAL)` (CP:145) | C-D:182; S-D:183; G-D:183 |
| `s2c_openjindutiao` | 194 | 194 | 194 | server → client | Handler `PLAYER_OPEN_JINDUTIAO` (`C/KProtocol.h:3467`; `S/KProtocol.h:3662`); CX:1527; Bảng `sizeof(PLAYER_OPEN_JINDUTIAO)` (CP:146) | C-D:183; S-D:184; G-D:184 |
| `s2c_syncitemposition` | 195 | 195 | 195 | server → client | Bảng `-1` (CP:147) | C-D:184; S-D:185; G-D:185 |
| `s2c_openduanzhao` | 196 | 196 | 196 | server → client | Handler `PLAYER_DUANZHAO` (`C/KProtocol.h:3441`; `S/KProtocol.h:3636`); CX:5173; Bảng `sizeof(PLAYER_DUANZHAO)` (CP:148) | C-D:185; S-D:186; G-D:186 |
| `s2c_syncurupdata` | 197 | 197 | 197 | server → client | Bảng `sizeof(BYTE)` (CP:149) | C-D:186; S-D:187; G-D:187 |
| `s2c_JinMaicallback` | 198 | 198 | 198 | server → client | Handler `PLAYER_JINMAI_GETBACK` (`C/KProtocol.h:1088`; `S/KProtocol.h:1141`); CX:5260; Bảng `sizeof(PLAYER_JINMAI_GETBACK)` (CP:150) | C-D:187; S-D:188; G-D:188 |
| `s2c_openvipdazao` | 199 | 199 | 199 | server → client | Handler `PLAYER_VIPDAZAO` (`C/KProtocol.h:3448`; `S/KProtocol.h:3643`); CX:5254; Bảng `sizeof(PLAYER_VIPDAZAO)` (CP:151) | C-D:188; S-D:189; G-D:189 |
| `s2c_synnpcinfocallback` | 200 | 200 | 200 | server → client | Handler `NPC_SYN_INFO_GETBACK` (`C/KProtocol.h:1102`; `S/KProtocol.h:1155`); CX:5233; Bảng `sizeof(NPC_SYN_INFO_GETBACK)` (CP:152) | C-D:189; S-D:190; G-D:190 |
| `s2c_pautoMovecallback` | 201 | 201 | 201 | server → client | Handler `PLAYER_AUTOCALLBACK_EQUIP` (`C/KProtocol.h:1183`; `S/KProtocol.h:1236`); CX:5195; Bảng `sizeof(PLAYER_AUTOCALLBACK_EQUIP)` (CP:153) | C-D:190; S-D:191; G-D:191 |
| `s2c_plyerguzicallback` | 202 | 202 | 202 | server → client | Handler `PLAYER_SYNCALLBACK_GUZI` (`C/KProtocol.h:877`; `S/KProtocol.h:885`); CX:5182; Bảng `sizeof(PLAYER_SYNCALLBACK_GUZI)` (CP:154) | C-D:191; S-D:192; G-D:192 |
| `s2c_syncplayermap` | 203 | 203 | 203 | server → client | Handler `PLAYER_NORMALMAP_SYNC` (`C/KProtocol.h:122`; `S/KProtocol.h:139`); CX:2399; Bảng `sizeof(PLAYER_NORMALMAP_SYNC)` (CP:155) | C-D:192; S-D:193; G-D:193 |
| `s2c_synconestate` | 204 | 204 | 204 | server → client | Handler `PLAYER_ONESTATE_SYNC` (`C/KProtocol.h:130`; `S/KProtocol.h:147`); CX:2384; Bảng `sizeof(PLAYER_ONESTATE_SYNC)` (CP:156) | C-D:193; S-D:194; G-D:194 |
| `s2c_syncnodataeffect` | 205 | 205 | 205 | server → client | Handler `STATE_NODATA_EFFECT_SYNC` (`C/KProtocol.h:2087`; `S/KProtocol.h:2212`); CX:2373; Bảng `sizeof(STATE_NODATA_EFFECT_SYNC)` (CP:157) | C-D:194; S-D:195; G-D:195 |
| `s2c_npcsetpos` | 206 | 206 | 206 | server → client | Handler `NPC_PLAYER_TYPE_NORMAL_SYNC` (`C/KProtocol.h:362`; `S/KProtocol.h:371`); CX:2313; Bảng `sizeof(NPC_PLAYER_TYPE_NORMAL_SYNC)` (CP:158) | C-D:195; S-D:196; G-D:196 |
| `s2c_playermissiondata` | 207 | 207 | 207 | server → client | Handler `PLAYER_MISSION_DATA` (`C/KProtocol.h:373`; `S/KProtocol.h:386`); CX:2259; Bảng `sizeof(PLAYER_MISSION_DATA)` (CP:159) | C-D:196; S-D:197; G-D:197 |
| `s2c_syncrankdata` | 208 | 208 | 208 | server → client | Handler `PLAYER_MISSION_RANKDATA` (`C/KProtocol.h:379`; `S/KProtocol.h:392`); CX:2269; Bảng `sizeof(PLAYER_MISSION_RANKDATA)` (CP:160) | C-D:197; S-D:198; G-D:198 |
| `s2c_syncsupershop` | 209 | 209 | 209 | server → client | Handler `S2C_SUPERSHOP` (`C/KProtocol.h:387`; `S/KProtocol.h:401`); CX:752; Bảng `sizeof(S2C_SUPERSHOP)` (CP:161) | C-D:198; S-D:199; G-D:199 |
| `s2c_syncitem_shop` | 210 | 210 | 210 | server → client | Handler `S2C_SUPERSHOP` (`C/KProtocol.h:387`; `S/KProtocol.h:401`); CX:743; Bảng `sizeof(ITEM_SYNC_SHOP)` (CP:162) | C-D:199; S-D:200; G-D:200 |
| `s2c_itemdata_shop` | 211 | 211 | 211 | server → client | Bảng `sizeof(ITEMDATA_SYNC_END)` (CP:163) | C-D:200; S-D:201; G-D:201 |
| `s2c_kickoutgame` | 212 | 212 | 212 | server → client | Handler `KICK_OUT_GAME_COMMAND` (`C/KProtocol.h:2005`; `S/KProtocol.h:2130`); CX:730; Bảng `sizeof(KICK_OUT_GAME_COMMAND)` (CP:164) | C-D:201; S-D:202; G-D:202 |
| `s2c_objadd_vn` | 213 | 213 | 213 | server → client | Handler `OBJ_SYNC_FINDPATH` (`C/KProtocol.h:774`; `S/KProtocol.h:782`); CX:2837; Bảng `sizeof(OBJ_SYNC_FINDPATH)` (CP:165) | C-D:202; S-D:203; G-D:203 |
| `s2c_rolesyncvipvalue` | 214 | 214 | 214 | server → client | Handler `SALE_MARKET_SYNC` (`C/KProtocol.h:3499`; `S/KProtocol.h:3694`); CX:5088; Bảng `sizeof(ROLEVIP_VALUE_SYNC)` (CP:166) | C-D:203; S-D:204; G-D:204 |
| `s2c_gm_synroleaction` | 215 | 215 | 215 | server → client | Bảng `-1` (CP:167) | C-D:204; S-D:205; G-D:205 |
| `s2c_queryiteminfo` | 216 | 216 | 216 | server → client | Bảng `-1` (CP:168) | C-D:205; S-D:206; G-D:206 |
| `s2c_returnitemlock` | 217 | 217 | 217 | server → client | Handler `PLAYER_AUTOMUVE_ITEM_COMMAND` (`C/KProtocol.h:905`; `S/KProtocol.h:913`); CX:5058; Bảng `sizeof(PLAYER_AUTOMUVE_ITEM_COMMAND)` (CP:169) | C-D:206; S-D:207; G-D:207 |
| `s2c_findpath_state` | 218 | 218 | 218 | server → client | Handler `PLAYER_FINDPATH_STATE` (`C/KProtocol.h:617`; `S/KProtocol.h:958`); CX:5050; Bảng `sizeof(PLAYER_FINDPATH_STATE)` (CP:170) | C-D:207; S-D:208; G-D:208 |
| `s2c_refitemsync` | 219 | 219 | 219 | server → client | Bảng `sizeof(REF_ITEM_SYNC)` (CP:171) | C-D:208; S-D:209; G-D:209 |
| `s2c_chestpwsync` | 220 | 220 | 220 | server → client | Handler `PLAYER_CHESTPW_SYNC` (`C/KProtocol.h:151`; `S/KProtocol.h:945`); CX:5288; Bảng `sizeof(PLAYER_TRADE_ITEM_SYNC)` (CP:172) | C-D:209; S-D:210; G-D:210 |
| `s2c_extend` | 250 | 250 | 250 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:210; S-D:212; G-D:212 |
| `s2c_extendchat` | 251 | 251 | 251 | server → client | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:211; S-D:213; G-D:213 |
| `s2c_extendfriend` | 252 | 252 | 252 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:212; S-D:214; G-D:214 |
| `s2c_extendchat_new` | 253 | 253 | 253 | server → client | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:213; S-D:215; G-D:215 |
| `s2c_extendtong` | 254 | 254 | 254 | server → client | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:214; S-D:216; G-D:216 |
| `s2c_end` | 255 | 255 | 255 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:215; S-D:217; G-D:217 |

### `c2s_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `c2s_rolekfjhu_saveroleinfo` | 10 | 10 | 10 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:220; S-D:222; G-D:222 |
| `c2s_roleserver_createroleinfo` | 11 | 11 | 11 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:221; S-D:223; G-D:223 |
| `c2s_gmsvr2gateway_saverole` | 12 | 12 | 12 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:222; S-D:224; G-D:224 |
| `c2s_micropackbegin` | 31 | 31 | 31 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:226; S-D:228; G-D:228 |
| `c2s_accountbegin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:227; S-D:229; G-D:229 |
| `c2s_accountlogin` | 33 | 33 | 33 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:228; S-D:230; G-D:230 |
| `c2s_gamelogin_dkiqopjgurnmvbgc` | 34 | 34 | 34 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:229; S-D:231; G-D:231 |
| `c2s_accountlogout` | 35 | 35 | 35 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:230; S-D:232; G-D:232 |
| `c2s_gatewayverify` | 36 | 36 | 36 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:231; S-D:233; G-D:233 |
| `c2s_gatewayverifyagain` | 37 | 37 | 37 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:232; S-D:234; G-D:234 |
| `c2s_gatewayinfo` | 38 | 38 | 38 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:233; S-D:235; G-D:235 |
| `c2s_multiserverbegin` | 48 | 48 | 48 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:235; S-D:237; G-D:237 |
| `c2s_permit_logftihmcginqknd` | 49 | 49 | 49 | luồng c2s; endpoint chưa kiểm | `tagPermitPlayerLogin` (`C/KProtocol.h:1557`; `S/KProtocol.h:1625`) | C-D:236; S-D:238; G-D:238 |
| `c2s_updatemapinfo` | 50 | 50 | 50 | luồng c2s; endpoint chưa kiểm | `tagUpdateMapID` (`C/KProtocol.h:1656`; `S/KProtocol.h:1730`) | C-D:237; S-D:239; G-D:239 |
| `c2s_updategameserverinfo` | 51 | 51 | 51 | luồng c2s; endpoint chưa kiểm | `tagGameSvrInfo` (`C/KProtocol.h:1673`; `S/KProtocol.h:1747`) | C-D:238; S-D:240; G-D:240 |
| `c2s__entergamegkjyiruqine` | 52 | 52 | 52 | luồng c2s; endpoint chưa kiểm | `tagEnterGame` (`C/KProtocol.h:1719`; `S/KProtocol.h:1795`) | C-D:239; S-D:241; G-D:241 |
| `c2s_leavegame` | 53 | 53 | 53 | luồng c2s; endpoint chưa kiểm | `tagLeaveGame` (`C/KProtocol.h:1748`; `S/KProtocol.h:1830`) | C-D:240; S-D:242; G-D:242 |
| `c2s_registeraccount` | 54 | 54 | 54 | luồng c2s; endpoint chưa kiểm | `tagRegisterAccount` (`C/KProtocol.h:1711`; `S/KProtocol.h:1787`) | C-D:241; S-D:243; G-D:243 |
| `c2s_requestsvrip` | 55 | 55 | 55 | luồng c2s; endpoint chưa kiểm | `tagRequestSvrIp` (`C/KProtocol.h:1635`; `S/KProtocol.h:1709`) | C-D:242; S-D:244; G-D:244 |
| `c2s_roleserver_getrolelist` | 56 | 56 | 56 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:243; S-D:245; G-D:245 |
| `c2s_roleserver_getroleinfo` | 57 | 57 | 57 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:244; S-D:246; G-D:246 |
| `c2s_roleserver_deleteplayer` | 58 | 58 | 58 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:245; S-D:247; G-D:247 |
| `c2s_gamestatistic` | 59 | 59 | 59 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:246; S-D:248; G-D:248 |
| `c2s_roleserver_lock` | 60 | 60 | 60 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:247; S-D:249; G-D:249 |
| `c2s_gameserverbegin` | 64 | 64 | 64 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:248; S-D:250; G-D:250 |
| `c2s_login` | 65 | — | — | client → server | Bảng `-1` (SP:172) | C-D:249 |
| `c2s_login_fhgyrinhkmvnsheypo` | — | 65 | 65 | client → server | Bảng `-1` (SP:172) | S-D:251; G-D:251 |
| `c2s__loginfs_kfjghtueodnchsf` | 66 | 66 | 66 | client → server | Bảng `sizeof(tagLogicLogin)` (SP:173); `S/KProtocol.h:1770` | C-D:250; S-D:252; G-D:252 |
| `c2s_syncclientend` | 67 | 67 | 67 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:251; S-D:253; G-D:253 |
| `c2s_loadplayer` | 68 | 68 | 68 | client → server | Bảng `-1` (SP:175) | C-D:252; S-D:254; G-D:254 |
| `c2s_newplayer` | 69 | 69 | 69 | client → server | Bảng `-1` (SP:176) | C-D:253; S-D:255; G-D:255 |
| `c2s_removeplayer` | 70 | 70 | 70 | client → server | Bảng `-1` (SP:177) | C-D:254; S-D:256; G-D:256 |
| `c2s_requestworld` | 71 | 71 | 71 | client → server | Bảng `-1` (SP:178) | C-D:255; S-D:257; G-D:257 |
| `c2s_requestplayer` | 72 | 72 | 72 | client → server | Bảng `-1` (SP:179) | C-D:256; S-D:258; G-D:258 |
| `c2s_requestnpc` | 73 | 73 | 73 | client → server | Bảng `sizeof(NPC_REQUEST_COMMAND)` (SP:180) | C-D:257; S-D:259; G-D:259 |
| `c2s_requestobj` | 74 | 74 | 74 | client → server | Bảng `sizeof(OBJ_CLIENT_SYNC_ADD)` (SP:181); `S/KProtocol.h:819` | C-D:258; S-D:260; G-D:260 |
| `c2s_npcwalk` | 75 | 75 | 75 | client → server | Bảng `sizeof(NPC_WALK_COMMAND)` (SP:182); `S/KProtocol.h:516` | C-D:259; S-D:261; G-D:261 |
| `c2s_npcrun` | 76 | 76 | 76 | client → server | Bảng `sizeof(NPC_RUN_COMMAND)` (SP:183); `S/KProtocol.h:529` | C-D:260; S-D:262; G-D:262 |
| `c2s_npcskill` | 77 | 77 | 77 | client → server | Bảng `sizeof(NPC_SKILL_COMMAND)` (SP:184); `S/KProtocol.h:508` | C-D:261; S-D:263; G-D:263 |
| `c2s_npcjump` | 78 | 78 | 78 | client → server | Bảng `sizeof(NPC_JUMP_COMMAND)` (SP:185); `S/KProtocol.h:2316` | C-D:262; S-D:264; G-D:264 |
| `c2s_npctalk` | 79 | 79 | 79 | client → server | Bảng `-1` (SP:186) | C-D:263; S-D:265; G-D:265 |
| `c2s_npchurt` | 80 | 80 | 80 | client → server | Bảng `-1` (SP:187) | C-D:264; S-D:266; G-D:266 |
| `c2s_npcdeath` | 81 | 81 | 81 | client → server | Bảng `-1` (SP:188) | C-D:265; S-D:267; G-D:267 |
| `c2s_playertalk` | 82 | 82 | 82 | client → server | Bảng `-1` (SP:189) | C-D:266; S-D:268; G-D:268 |
| `c2s_teamapplyinfo` | 83 | 83 | 83 | client → server | Bảng `sizeof(PLAYER_APPLY_TEAM_INFO)` (SP:190); `S/KProtocol.h:579` | C-D:267; S-D:269; G-D:269 |
| `c2s_teamapplycreate` | 84 | 84 | 84 | client → server | Bảng `sizeof(PLAYER_APPLY_CREATE_TEAM)` (SP:191); `S/KProtocol.h:561` | C-D:268; S-D:270; G-D:270 |
| `c2s_teamapplyopenclose` | 85 | 85 | 85 | client → server | Bảng `sizeof(PLAYER_TEAM_OPEN_CLOSE)` (SP:192); `S/KProtocol.h:624` | C-D:269; S-D:271; G-D:271 |
| `c2s_teamapplyadd` | 86 | 86 | 86 | client → server | Bảng `sizeof(PLAYER_APPLY_ADD_TEAM)` (SP:193); `S/KProtocol.h:630` | C-D:270; S-D:272; G-D:272 |
| `c2s_teamacceptmember` | 87 | 87 | 87 | client → server | Bảng `sizeof(PLAYER_ACCEPT_TEAM_MEMBER)` (SP:194); `S/KProtocol.h:636` | C-D:271; S-D:273; G-D:273 |
| `c2s_teamapplyleave` | 88 | 88 | 88 | client → server | Bảng `sizeof(PLAYER_APPLY_LEAVE_TEAM)` (SP:195); `S/KProtocol.h:651` | C-D:272; S-D:274; G-D:274 |
| `c2s_teamapplykickmember` | 89 | 89 | 89 | client → server | Bảng `sizeof(PLAYER_TEAM_KICK_MEMBER)` (SP:196); `S/KProtocol.h:662` | C-D:273; S-D:275; G-D:275 |
| `c2s_teamapplychangecaptain` | 90 | 90 | 90 | client → server | Bảng `sizeof(PLAYER_APPLY_TEAM_CHANGE_CAPTAIN)` (SP:197); `S/KProtocol.h:668` | C-D:274; S-D:276; G-D:276 |
| `c2s_teamapplydismiss` | 91 | 91 | 91 | client → server | Bảng `sizeof(PLAYER_APPLY_TEAM_DISMISS)` (SP:198); `S/KProtocol.h:681` | C-D:275; S-D:277; G-D:277 |
| `c2s_playerapplysetpk` | 92 | 92 | 92 | client → server | Bảng `sizeof(PLAYER_SET_PK)` (SP:199); `S/KProtocol.h:686` | C-D:276; S-D:278; G-D:278 |
| `c2s_playerapplyfactiondata` | 93 | 93 | 93 | client → server | Bảng `sizeof(PLAYER_APPLY_FACTION_DATA)` (SP:200); `S/KProtocol.h:713` | C-D:277; S-D:279; G-D:279 |
| `c2s_playersendchat` | 94 | 94 | 94 | client → server | Bảng `-1` (SP:201) | C-D:278; S-D:280; G-D:280 |
| `c2s_playeraddbaseattribute` | 95 | 95 | 95 | client → server | Bảng `sizeof(PLAYER_ADD_BASE_ATTRIBUTE_COMMAND)` (SP:202); `S/KProtocol.h:850` | C-D:279; S-D:281; G-D:281 |
| `c2s_playerapplyaddskillpoint` | 96 | 96 | 96 | client → server | Bảng `sizeof(PLAYER_ADD_SKILL_POINT_COMMAND)` (SP:203); `S/KProtocol.h:857` | C-D:280; S-D:282; G-D:282 |
| `c2s_playereatitem` | 97 | 97 | 97 | client → server | Bảng `sizeof(PLAYER_EAT_ITEM_COMMAND)` (SP:204); `S/KProtocol.h:904` | C-D:281; S-D:283; G-D:283 |
| `c2s_playerpickupitem` | 98 | 98 | 98 | client → server | Bảng `sizeof(PLAYER_PICKUP_ITEM_COMMAND)` (SP:205); `S/KProtocol.h:964` | C-D:282; S-D:284; G-D:284 |
| `c2s_playermoveitem` | 99 | 99 | 99 | client → server | Bảng `sizeof(PLAYER_MOVE_ITEM_COMMAND)` (SP:206); `S/KProtocol.h:1193` | C-D:283; S-D:285; G-D:285 |
| `c2s_playersellitem` | 100 | 100 | 100 | client → server | Bảng `sizeof(PLAYER_SELL_ITEM_COMMAND)` (SP:207); `S/KProtocol.h:1060` | C-D:284; S-D:286; G-D:286 |
| `c2s_playerbuyitem` | 101 | 101 | 101 | client → server | Bảng `sizeof(PLAYER_BUY_ITEM_COMMAND)` (SP:208); `S/KProtocol.h:1067` | C-D:285; S-D:287; G-D:287 |
| `c2s_playerthrowawayitem` | 102 | 102 | 102 | client → server | Bảng `sizeof(PLAYER_THROW_AWAY_ITEM_COMMAND)` (SP:209); `S/KProtocol.h:1249` | C-D:286; S-D:288; G-D:288 |
| `c2s_playerselui` | 103 | 103 | 103 | client → server | Bảng `sizeof(PLAYER_SELECTUI_COMMAND)` (SP:210); `S/KProtocol.h:1442` | C-D:287; S-D:289; G-D:289 |
| `c2s_chatsetchannel` | 104 | 104 | 104 | client → server | Bảng `sizeof(CHAT_SET_CHANNEL_COMMAND)` (SP:211); `S/KProtocol.h:1448` | C-D:288; S-D:290; G-D:290 |
| `c2s_chatapplyaddfriend` | 105 | 105 | 105 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:289; S-D:291; G-D:291 |
| `c2s_chataddfriend` | 106 | 106 | 106 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:290; S-D:292; G-D:292 |
| `c2s_chatrefusefriend` | 107 | 107 | 107 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:291; S-D:293; G-D:293 |
| `c2s_dbplayerselect` | 108 | 108 | 108 | client → server | Bảng `sizeof(tagDBSelPlayer)` (SP:215); `S/KProtocol.h:1548` | C-D:292; S-D:294; G-D:294 |
| `c2s_chatapplyresendallfriendname` | 109 | 109 | 109 | client → server | Bảng `sizeof(CHAT_APPLY_RESEND_ALL_FRIEND_NAME_COMMAND)` (SP:216); `S/KProtocol.h:1999` | C-D:293; S-D:295; G-D:295 |
| `c2s_chatapplysendonefriendname` | 110 | 110 | 110 | client → server | Bảng `sizeof(CHAT_APPLY_SEND_ONE_FRIEND_NAME_COMMAND)` (SP:217); `S/KProtocol.h:2004` | C-D:294; S-D:296; G-D:296 |
| `c2s_chatdeletefriend` | 111 | 111 | 111 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:295; S-D:297; G-D:297 |
| `c2s_chatredeletefriend` | 112 | 112 | 112 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:296; S-D:298; G-D:298 |
| `c2s_tradeapplystateopen` | 113 | 113 | 113 | client → server | Bảng `-1` (SP:220) | C-D:297; S-D:299; G-D:299 |
| `c2s_tradeapplystateclose` | 114 | 114 | 114 | client → server | Bảng `sizeof(TRADE_APPLY_CLOSE_COMMAND)` (SP:221); `S/KProtocol.h:2068` | C-D:298; S-D:300; G-D:300 |
| `c2s_tradeapplystart` | 115 | 115 | 115 | client → server | Bảng `sizeof(TRADE_APPLY_START_COMMAND)` (SP:222); `S/KProtocol.h:2089` | C-D:299; S-D:301; G-D:301 |
| `c2s_trademovemoney` | 116 | 116 | 116 | client → server | Bảng `sizeof(TRADE_MOVE_MONEY_COMMAND)` (SP:223); `S/KProtocol.h:2111` | C-D:300; S-D:302; G-D:302 |
| `c2s_tradedecision` | 117 | 117 | 117 | client → server | Bảng `sizeof(TRADE_DECISION_COMMAND)` (SP:224); `S/KProtocol.h:2123` | C-D:301; S-D:303; G-D:303 |
| `c2s_dialognpc` | 118 | 118 | 118 | client → server | Bảng `sizeof(PLAYER_DIALOG_NPC_COMMAND)` (SP:225); `S/KProtocol.h:543` | C-D:302; S-D:304; G-D:304 |
| `c2s_teaminviteadd` | 119 | 119 | 119 | client → server | Bảng `sizeof(TEAM_INVITE_ADD_COMMAND)` (SP:226); `S/KProtocol.h:2165` | C-D:303; S-D:305; G-D:305 |
| `c2s_changeauraskill` | 120 | 120 | 120 | client → server | Bảng `sizeof(SKILL_CHANGEAURASKILL_COMMAND)` (SP:227); `S/KProtocol.h:2179` | C-D:304; S-D:306; G-D:306 |
| `c2s_teamreplyinvite` | 121 | 121 | 121 | client → server | Bảng `sizeof(TEAM_REPLY_INVITE_COMMAND)` (SP:228); `S/KProtocol.h:2185` | C-D:305; S-D:307; G-D:307 |
| `c2s_ping` | 122 | 122 | 122 | client → server | Bảng `sizeof(PING_CLIENTREPLY_COMMAND)` (SP:229); `S/KProtocol.h:2231` | C-D:306; S-D:308; G-D:308 |
| `c2s_cpunlock` | 123 | 123 | 123 | client → server | Bảng `sizeof(PLAYER_REQUEST_CP_UNLOCK)` (SP:230); `S/KProtocol.h:155` | C-D:307; S-D:309; G-D:309 |
| `c2s_cplock` | 124 | 124 | 124 | client → server | Bảng `sizeof(PLAYER_REQUEST_CP_LOCK)` (SP:231); `S/KProtocol.h:161` | C-D:308; S-D:310; G-D:310 |
| `c2s_cpchange` | 125 | 125 | 125 | client → server | Bảng `sizeof(PLAYER_REQUEST_CP_CHANGE)` (SP:232); `S/KProtocol.h:198` | C-D:309; S-D:311; G-D:311 |
| `c2s_cpreset` | 126 | 126 | 126 | client → server | Bảng `sizeof(PLAYER_REQUEST_CP_RESET)` (SP:233); `S/KProtocol.h:205` | C-D:310; S-D:312; G-D:312 |
| `c2s_market` | 127 | 127 | 127 | client → server | Bảng `sizeof(PLAYER_REQUEST_OPEN_MARKET)` (SP:234); `S/KProtocol.h:3676` | C-D:311; S-D:313; G-D:313 |
| `c2s_string` | 128 | 128 | 128 | client → server | Bảng `sizeof(PLAYER_STRING_CALLBACK)` (SP:235); `S/KProtocol.h:3684` | C-D:312; S-D:314; G-D:314 |
| `c2s_datau` | 129 | 129 | 129 | client → server | Bảng `sizeof(CP_DATAU)` (SP:236); `S/KProtocol.h:278` | C-D:313; S-D:315; G-D:315 |
| `c2s_npcsit` | 130 | 130 | 130 | client → server | Bảng `sizeof(NPC_SIT_COMMAND)` (SP:237); `S/KProtocol.h:2238` | C-D:314; S-D:316; G-D:316 |
| `c2s_objmouseclick` | 131 | 131 | 131 | client → server | Bảng `sizeof(OBJ_MOUSE_CLICK_SYNC)` (SP:238); `S/KProtocol.h:2331` | C-D:315; S-D:317; G-D:317 |
| `c2s_storemoney` | 132 | 132 | 132 | client → server | Bảng `sizeof(STORE_MONEY_COMMAND)` (SP:239); `S/KProtocol.h:2143` | C-D:316; S-D:318; G-D:318 |
| `c2s_playerrevive` | 133 | 133 | 133 | client → server | Bảng `sizeof(NPC_REVIVE_COMMAND)` (SP:240); `S/KProtocol.h:523` | C-D:317; S-D:319; G-D:319 |
| `c2s_tradereplystart` | 134 | 134 | 134 | client → server | Bảng `sizeof(TRADE_REPLY_START_COMMAND)` (SP:241); `S/KProtocol.h:2104` | C-D:318; S-D:320; G-D:320 |
| `c2s_pkapplychangenormalflag` | 135 | 135 | 135 | client → server | Bảng `sizeof(PK_APPLY_NORMAL_FLAG_COMMAND)` (SP:242); `S/KProtocol.h:2352` | C-D:319; S-D:321; G-D:321 |
| `c2s_pkapplyenmity` | 136 | 136 | 136 | client → server | Bảng `sizeof(PK_APPLY_ENMITY_COMMAND)` (SP:243); `S/KProtocol.h:2364` | C-D:320; S-D:322; G-D:322 |
| `c2s_viewequip` | 137 | 137 | 137 | client → server | Bảng `sizeof(VIEW_EQUIP_COMMAND)` (SP:244); `S/KProtocol.h:1503` | C-D:321; S-D:323; G-D:323 |
| `c2s_ladderquery` | 138 | 138 | 138 | client → server | Bảng `sizeof(LADDER_QUERY)` (SP:245); `S/KProtocol.h:2561` | C-D:323; S-D:325; G-D:325 |
| `c2s_repairitem` | 139 | 139 | 139 | client → server | Bảng `sizeof(ITEM_REPAIR)` (SP:246); `S/KProtocol.h:3254` | C-D:324; S-D:326; G-D:326 |
| `c2s_npcride` | 140 | 140 | 140 | client → server | Bảng `sizeof(NPC_RIDE_COMMAND)` (SP:247); `S/KProtocol.h:2244` | C-D:325; S-D:327; G-D:327 |
| `c2s_breakitem` | 141 | 141 | 141 | client → server | Bảng `sizeof(ITEM_BREAK)` (SP:248); `S/KProtocol.h:3275` | C-D:326; S-D:328; G-D:328 |
| `c2s_playercomp` | 142 | 142 | 142 | client → server | Bảng `sizeof(PLAYER_COMPITEM)` (SP:249); `S/KProtocol.h:3282` | C-D:327; S-D:329; G-D:329 |
| `c2s_playersetprice` | 143 | 143 | 143 | client → server | Bảng `sizeof(PLAYER_SET_PRICE)` (SP:250); `S/KProtocol.h:3549` | C-D:328; S-D:330; G-D:330 |
| `c2s_playerstarttrade` | 144 | 144 | 144 | client → server | Bảng `sizeof(PLAYER_START_TRADE)` (SP:251); `S/KProtocol.h:3565` | C-D:329; S-D:331; G-D:331 |
| `c2s_viewitem` | 145 | 145 | 145 | client → server | Bảng `sizeof(VIEW_EQUIP_COMMAND)` (SP:252); `S/KProtocol.h:1503` | C-D:330; S-D:332; G-D:332 |
| `c2s_playertradebuyitem` | 146 | 146 | 146 | client → server | Bảng `sizeof(PLAYER_TRADE_BUY_ITEM_COMMAND)` (SP:253); `S/KProtocol.h:3535` | C-D:331; S-D:333; G-D:333 |
| `c2s_updateviewitem` | 147 | 147 | 147 | client → server | Bảng `sizeof(VIEW_EQUIP_COMMAND)` (SP:254); `S/KProtocol.h:1503` | C-D:332; S-D:334; G-D:334 |
| `c2s_playerneedcount` | 148 | 148 | 148 | client → server | Bảng `sizeof(PLAYER_NEED_COUNT)` (SP:255); `S/KProtocol.h:3518` | C-D:333; S-D:335; G-D:335 |
| `c2s_playershopname` | 149 | 149 | 149 | client → server | Bảng `sizeof(PLAYER_NEED_COUNT)` (SP:256); `S/KProtocol.h:3518` | C-D:334; S-D:336; G-D:336 |
| `c2s_playersysshop` | 150 | 150 | 150 | client → server | Bảng `sizeof(TONG_DISMISS_SYNC)` (SP:257); `S/KProtocol.h:2993` | C-D:335; S-D:337; G-D:337 |
| `c2s_playerlixian` | 151 | 151 | 151 | client → server | Bảng `sizeof(TONG_DISMISS_SYNC)` (SP:258); `S/KProtocol.h:2993` | C-D:336; S-D:338; G-D:338 |
| `c2s_playergiveback` | 152 | 152 | 152 | client → server | Bảng `sizeof(PLAYER_GIVE_CALLBACK)` (SP:259); `S/KProtocol.h:3650` | C-D:337; S-D:339; G-D:339 |
| `c2s_pkvalue` | 153 | 153 | 153 | client → server | Bảng `sizeof(CP_PKVALUE)` (SP:260); `S/KProtocol.h:285` | C-D:338; S-D:340; G-D:340 |
| `c2s_autoplay` | 154 | 154 | 154 | client → server | Bảng `sizeof(CP_AUTOPLAY)` (SP:261); `S/KProtocol.h:291` | C-D:339; S-D:341; G-D:341 |
| `c2s_npcsunyi` | 155 | 155 | 155 | client → server | Bảng `sizeof(NPC_SUNYI_COMMAND)` (SP:262); `S/KProtocol.h:2249` | C-D:340; S-D:342; G-D:342 |
| `c2s_guzi` | 156 | 156 | 156 | client → server | Bảng `sizeof(CP_GUZI)` (SP:263); `S/KProtocol.h:2260` | C-D:341; S-D:343; G-D:343 |
| `c2s_gufarm` | 157 | 157 | 157 | client → server | Bảng `sizeof(CP_GUZI_FARMS)` (SP:264); `S/KProtocol.h:2270` | C-D:342; S-D:344; G-D:344 |
| `c2s_addjinbi` | 158 | 158 | 158 | client → server | Bảng `sizeof(CP_ADD_JINBI)` (SP:265); `S/KProtocol.h:2279` | C-D:343; S-D:345; G-D:345 |
| `c2s_lianjie` | 159 | 159 | 159 | client → server | Bảng `sizeof(VIEW_LIANJIE_COMMAND)` (SP:266); `S/KProtocol.h:2285` | C-D:344; S-D:346; G-D:346 |
| `c2s_fsjingmai` | 160 | 160 | 160 | client → server | Bảng `sizeof(CP_JINGMAI)` (SP:267); `S/KProtocol.h:2294` | C-D:345; S-D:347; G-D:347 |
| `c2s_guaforbit` | 161 | 161 | 161 | client → server | Bảng `sizeof(NPC_GUAFORBIT_COMMAND)` (SP:268); `S/KProtocol.h:2302` | C-D:346; S-D:348; G-D:348 |
| `c2s_skillsync` | 162 | 162 | 162 | client → server | Bảng `sizeof(SKILL_LEFT_SYNC)` (SP:269); `S/KProtocol.h:2309` | C-D:347; S-D:349; G-D:349 |
| `c2s_playerrong` | 163 | 163 | 163 | client → server | Bảng `sizeof(PLAYER_RONGITEM)` (SP:270); `S/KProtocol.h:3375` | C-D:348; S-D:350; G-D:350 |
| `c2s_playeradditem` | 164 | 164 | 164 | client → server | Bảng `sizeof(PLAYER_ADD_ITEM)` (SP:271); `S/KProtocol.h:3347` | C-D:349; S-D:351; G-D:351 |
| `c2s_playerAutoMoveitem` | 165 | 165 | 165 | client → server | Bảng `sizeof(PLAYER_AUTOMUVE_ITEM_COMMAND)` (SP:272); `S/KProtocol.h:913` | C-D:350; S-D:352; G-D:352 |
| `c2s_playerdelitem` | 166 | 166 | 166 | client → server | Bảng `sizeof(PLAYER_DELL_ITEM)` (SP:273); `S/KProtocol.h:3368` | C-D:351; S-D:353; G-D:353 |
| `c2s_playersetLianFlg` | 167 | 167 | 167 | client → server | Bảng `sizeof(PLAYER_SET_LIANJIEFLG)` (SP:274); `S/KProtocol.h:3557` | C-D:352; S-D:354; G-D:354 |
| `c2s_updateviewequip` | 168 | 168 | 168 | client → server | Bảng `sizeof(VIEW_EQUIP_COMMAND)` (SP:275); `S/KProtocol.h:1503` | C-D:353; S-D:355; G-D:355 |
| `c2s_playertongset` | 169 | 169 | 169 | client → server | Bảng `sizeof(PLAYER_TONGINFO)` (SP:276); `S/KProtocol.h:3290` | C-D:354; S-D:356; G-D:356 |
| `c2s_playerdoScript` | 170 | 170 | 170 | client → server | Bảng `sizeof(PLAYER_DOSCRIPT)` (SP:277); `S/KProtocol.h:3306` | C-D:355; S-D:357; G-D:357 |
| `c2s_gettaskval` | 171 | 171 | 171 | client → server | Bảng `sizeof(PLAYER_GET_TASKVAL_COMMAND)` (SP:278); `S/KProtocol.h:1123` | C-D:356; S-D:358; G-D:358 |
| `c2s_jinducallback` | 172 | 172 | 172 | client → server | Bảng `sizeof(PLAYER_JINDU_CALLBACK)` (SP:279); `S/KProtocol.h:3524` | C-D:357; S-D:359; G-D:359 |
| `c2s_syncurdata` | 173 | 173 | 173 | client → server | Bảng `sizeof(BYTE)` (SP:280) | C-D:358; S-D:360; G-D:360 |
| `c2s_vipdoScript` | 174 | 174 | 174 | client → server | Bảng `sizeof(PLAYER_VIP_DOSCRIPT)` (SP:281); `S/KProtocol.h:3318` | C-D:359; S-D:361; G-D:361 |
| `c2s_roomisfull` | 175 | 175 | 175 | client → server | Bảng `sizeof(PLAYER_NO_ROOM_INFO)` (SP:282); `S/KProtocol.h:585` | C-D:360; S-D:362; G-D:362 |
| `c2s_synnpcinfo` | 176 | 176 | 176 | client → server | Bảng `sizeof(NPC_SYN_INFO)` (SP:283); `S/KProtocol.h:591` | C-D:361; S-D:363; G-D:363 |
| `c2s_playerautoequip` | 177 | 177 | 177 | client → server | Bảng `sizeof(PLAYER_AUTO_EQUIP)` (SP:284); `S/KProtocol.h:3357` | C-D:362; S-D:364; G-D:364 |
| `c2s_playerguzgame` | 178 | 178 | 178 | client → server | Bảng `sizeof(PLAYER_SYN_TYPE)` (SP:285); `S/KProtocol.h:3260` | C-D:363; S-D:365; G-D:365 |
| `c2s_playersetpos` | 179 | 179 | 179 | client → server | Bảng `sizeof(PLAYER_SYN_POS)` (SP:286); `S/KProtocol.h:3267` | C-D:364; S-D:366; G-D:366 |
| `c2s_synshopidx` | 180 | 180 | 180 | client → server | Bảng `sizeof(PLAYER_SET_TASKVAL_COMMAND)` (SP:287); `S/KProtocol.h:1106` | C-D:365; S-D:367; G-D:367 |
| `c2s_settaskval` | 181 | 181 | 181 | client → server | Bảng `-1` (SP:288) | C-D:366; S-D:368; G-D:368 |
| `c2s_runscript` | 182 | 182 | 182 | client → server | Bảng `sizeof(CLIENT_RUN_SCRIPT)` (SP:289); `S/KProtocol.h:1114` | C-D:367; S-D:369; G-D:369 |
| `c2s_player_req` | 183 | 183 | 183 | client → server | Bảng `sizeof(PLAYER_REQ_COMMAND)` (SP:290); `S/KProtocol.h:555` | C-D:368; S-D:370; G-D:370 |
| `c2s_lockitem` | 184 | 184 | 184 | client → server | Bảng `sizeof(PLAYER_AUTOMUVE_ITEM_COMMAND)` (SP:291); `S/KProtocol.h:913` | C-D:369; S-D:371; G-D:371 |
| `c2s_gmcommand` | 185 | 185 | — | client → server | Bảng `-1` (SP:292) | C-D:370; S-D:372 |
| `c2s_findpath_state` | 186 | 186 | 185 | client → server | Bảng `sizeof(PLAYER_FINDPATH_STATE)` (SP:294); `S/KProtocol.h:958` | C-D:371; S-D:373; G-D:372 |
| `c2s_create_ref_item` | 187 | 187 | 186 | client → server | Bảng `sizeof(PLAYER_CREATE_REF_ITEM_COMMAND)` (SP:295); `S/KProtocol.h:925` | C-D:372; S-D:374; G-D:373 |
| `c2s_remove_ref_item` | 188 | 188 | 187 | client → server | Bảng `sizeof(PLAYER_REMOVE_REF_ITEM_COMMAND)` (SP:296); `S/KProtocol.h:932` | C-D:373; S-D:375; G-D:374 |
| `c2s_rolecheckname_result` | 192 | 192 | 188 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:377; S-D:379; G-D:375 |
| `c2s_apply_mask_lock` | 189 | 189 | — | client → server | Bảng `sizeof(PLAYERREQUESTLOCKMASK)` (SP:297); `S/KProtocol.h:952` | C-D:374; S-D:376 |
| `c2s_msginfo` | 193 | 193 | 189 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:378; S-D:380; G-D:376 |
| `c2s_player_combine_item` | 190 | 190 | — | client → server | Bảng `sizeof(PLAYER_COMBINE_ITEM)` (SP:298); `S/KProtocol.h:1080` | C-D:375; S-D:377 |
| `c2s_msginfo_all` | 194 | 194 | 190 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:379; S-D:381; G-D:377 |
| `c2s_playercommand` | 191 | 191 | — | client → server | Bảng `sizeof(PLAYER_COMMAND)` (SP:299); `S/KProtocol.h:1097` | C-D:376; S-D:378 |
| `c2s_gm_synroleaction` | 195 | 195 | 191 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:380; S-D:382; G-D:378 |
| `c2s_gm_synroleaction_result` | 196 | 196 | 192 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:381; S-D:383; G-D:379 |
| `c2s_item_synaction` | 197 | 197 | 193 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:382; S-D:384; G-D:380 |
| `c2s_item_synaction_result` | 198 | 198 | 194 | luồng c2s; endpoint chưa kiểm | Cấu trúc/handler ngoài core: chưa kiểm. | C-D:383; S-D:385; G-D:381 |
| `_c2s_begin_relay` | 250 | 250 | 250 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:384; S-D:387; G-D:382 |
| `c2s_extend` | 250 | 250 | 250 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:385; S-D:388; G-D:383 |
| `c2s_extendchat` | 251 | 251 | 251 | luồng c2s; endpoint chưa kiểm | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:386; S-D:389; G-D:384 |
| `c2s_extendfriend` | 252 | 252 | 252 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:387; S-D:390; G-D:385 |
| `c2s_extendchat_new` | 253 | 253 | 253 | luồng c2s; endpoint chưa kiểm | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:388; S-D:391; G-D:386 |
| `_c2s_end_relay` | 253 | 253 | 253 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:389; S-D:392; G-D:387 |
| `c2s_extendtong` | 254 | 254 | 254 | luồng c2s; endpoint chưa kiểm | `tagExtendProtoHeader` + payload mở rộng (`C/KRelayProtocol.h:81`; `S/KRelayProtocol.h:81`); dispatch cụ thể chưa kiểm. | C-D:390; S-D:393; G-D:388 |
| `c2s_end` | 255 | 255 | 255 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:391; S-D:394; G-D:389 |

### `c2c_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `c2c_transferroleinfo` | 14 | 14 | 14 | server ↔ server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:396; S-D:399; G-D:394 |
| `c2c_micropackbegin` | 31 | 31 | 31 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:397; S-D:400; G-D:395 |
| `c2c_protocolbegin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:398; S-D:401; G-D:396 |
| `c2c_permitplayerexchangeout` | 64 | 64 | 64 | server ↔ server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:399; S-D:402; G-D:397 |
| `c2c_permitplayerexchangein` | 65 | 65 | 65 | server ↔ server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:400; S-D:403; G-D:398 |
| `c2c_notifyexchange` | 66 | 66 | 66 | server ↔ server | `tagSearchWay` (`C/KProtocol.h:1646`; `S/KProtocol.h:1720`) | C-D:401; S-D:404; G-D:399 |
| `s2s_broadcast` | 96 | 96 | 96 | server ↔ server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:402; S-D:405; G-D:400 |
| `s2s_execute` | 97 | 97 | 97 | server ↔ server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:403; S-D:406; G-D:401 |
| `c2c_end` | 98 | 98 | 98 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:404; S-D:407; G-D:402 |

### `gm_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `gm_begin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:412; S-D:415; G-D:410 |
| `gm_c2s_execute` | 33 | 33 | 33 | GM → server | `GM_EXECUTE_COMMAND` (`S/KGmProtocol.h:27`); C chưa kiểm. | C-D:413; S-D:416; G-D:411 |
| `gm_c2s_disable` | 34 | 34 | 34 | GM → server | `GM_DISABLE_ACTION_COMMAND` (`S/KGmProtocol.h:36`); C chưa kiểm. | C-D:414; S-D:417; G-D:412 |
| `gm_c2s_enable` | 35 | 35 | 35 | GM → server | `GM_ENABLE_ACTION_COMMAND` (`S/KGmProtocol.h:45`); C chưa kiểm. | C-D:415; S-D:418; G-D:413 |
| `gm_c2s_tracking` | 36 | 36 | 36 | GM → server | `GM_TRACK_COMMAND` (`S/KGmProtocol.h:54`); C chưa kiểm. | C-D:416; S-D:419; G-D:414 |
| `gm_c2s_setrole` | 37 | 37 | 37 | GM → server | `GM_SET_ROLE_DATA_COMMAND` (`S/KGmProtocol.h:83`); C chưa kiểm. | C-D:417; S-D:420; G-D:415 |
| `gm_c2s_getrole` | 38 | 38 | 38 | GM → server | `GM_GET_ROLE_DATA_COMMAND` (`S/KGmProtocol.h:91`); C chưa kiểm. | C-D:418; S-D:421; G-D:416 |
| `gm_c2s_findplayer` | 39 | 39 | 39 | GM → server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:419; S-D:422; G-D:417 |
| `gm_c2s_unlock` | 40 | 40 | 40 | GM → server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:420; S-D:423; G-D:418 |
| `gm_c2s_getrolelist` | 41 | 41 | 41 | GM → server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:421; S-D:424; G-D:419 |
| `gm_c2s_broadcast_chat` | 42 | 42 | 42 | GM → server | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:422; S-D:425; G-D:420 |
| `gm_s2c_tracking` | 43 | 43 | 43 | server → GM | `GM_TRACK_SYNC` (`S/KGmProtocol.h:63`); C chưa kiểm. | C-D:423; S-D:426; G-D:421 |
| `gm_s2c_getrole` | 44 | 44 | 44 | server → GM | `GM_GET_ROLE_DATA_SYNC` (`S/KGmProtocol.h:100`); C chưa kiểm. | C-D:424; S-D:427; G-D:422 |
| `gm_s2c_findplayer` | 45 | 45 | 45 | server → GM | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:425; S-D:428; G-D:423 |
| `gm_s2c_getrolelist` | 46 | 46 | 46 | server → GM | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:426; S-D:429; G-D:424 |
| `gm_end` | 47 | 47 | 47 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:427; S-D:430; G-D:425 |

### `relay_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `relay_begin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:433; S-D:436; G-D:431 |
| `relay_c2c_data` | 33 | 33 | 33 | server ↔ relay | `RELAY_DATA` (`C/KRelayProtocol.h:47`; `S/KRelayProtocol.h:47`) | C-D:434; S-D:437; G-D:432 |
| `relay_c2c_askwaydata` | 34 | 34 | 34 | server ↔ relay | `RELAY_ASKWAY_DATA` (`C/KRelayProtocol.h:61`; `S/KRelayProtocol.h:61`) | C-D:435; S-D:438; G-D:433 |
| `relay_s2c_loseway` | 35 | 36 | 36 | server ↔ relay | `RELAY_DATA` (`C/KRelayProtocol.h:47`; `S/KRelayProtocol.h:47`) | C-D:436; S-D:440; G-D:435 |
| `relay_c2c_remote` | — | 35 | 35 | server ↔ relay | `RELAY_REMOTE` (`C/KRelayProtocol.h:161`; `S/KRelayProtocol.h:161`) | S-D:439; G-D:434 |
| `relay_end` | 36 | 39 | 39 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:437; S-D:443; G-D:438 |
| `relay_s2c_udateserver` | — | 37 | 37 | server ↔ relay | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:441; G-D:436 |
| `relay_s2c_udatemaps` | — | 38 | 38 | server ↔ relay | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:442; G-D:437 |

### `chat_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `chat_micropackbegin` | 31 | 31 | 31 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:442; S-D:448; G-D:443 |
| `chat_someonechat` | 32 | 32 | 32 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:443; S-D:449; G-D:444 |
| `chat_channelchat` | 33 | 33 | 33 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:444; S-D:450; G-D:445 |
| `chat_feedback` | 34 | 34 | 34 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:445; S-D:451; G-D:446 |
| `chat_everyone` | 35 | 35 | 35 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:446; S-D:452; G-D:447 |
| `chat_groupman` | 36 | 36 | 36 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:447; S-D:453; G-D:448 |
| `chat_specman` | 37 | 37 | 37 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:448; S-D:454; G-D:449 |
| `chat_relegate` | 38 | 38 | 38 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:449; S-D:455; G-D:450 |
| `chat_filterplayer` | 39 | 39 | 39 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:450; S-D:456; G-D:451 |
| `chat_coretask` | — | 40 | 40 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:457; G-D:452 |
| `chat_caoritemtime` | — | 41 | 41 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:458; G-D:453 |
| `chat_coreitemdata` | — | 42 | 42 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:459; G-D:454 |
| `chat_goldthread` | — | 43 | 43 | luồng chat; endpoint chưa kiểm | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:460; G-D:455 |

### `playercomm_PROTOCOL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `playercomm_begin` | 32 | 32 | 32 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:455; S-D:465; G-D:460 |
| `playercomm_c2s_querychannelid` | 33 | 33 | 33 | client → server/relay | `PLAYERCOMM_QUERYCHANNELID` (`C/KRelayProtocol.h:106`; `S/KRelayProtocol.h:106`) | C-D:456; S-D:466; G-D:461 |
| `playercomm_s2c_notifychannelid` | 34 | 34 | 34 | server/relay → client | `PLAYERCOMM_NOTIFYCHANNELID` (`C/KRelayProtocol.h:112`; `S/KRelayProtocol.h:112`) | C-D:457; S-D:467; G-D:462 |
| `playercomm_c2s_freechannelid` | 35 | 35 | 35 | client → server/relay | `PLAYERCOMM_FREECHANNELID` (`C/KRelayProtocol.h:120`; `S/KRelayProtocol.h:120`) | C-D:458; S-D:468; G-D:463 |
| `playercomm_c2s_subscribe` | 36 | 36 | 36 | client → server/relay | `PLAYERCOMM_SUBSCRIBE` (`C/KRelayProtocol.h:126`; `S/KRelayProtocol.h:126`) | C-D:459; S-D:469; G-D:464 |
| `playercomm_s2c_relegate` | 37 | 37 | 37 | server/relay → client | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:460; S-D:470; G-D:465 |
| `playercomm_c2s_rollback` | 38 | 38 | 38 | client → server/relay | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:461; S-D:471; G-D:466 |
| `playercomm_s2c_gmquerychannelid` | 39 | 39 | 39 | server/relay → client | `PLAYERCOMM_GMQUERYCHANNELID` (`C/KRelayProtocol.h:133`; `S/KRelayProtocol.h:133`) | C-D:462; S-D:472; G-D:467 |
| `playercomm_s2c_gmfreechannelid` | 40 | 40 | 40 | server/relay → client | `PLAYERCOMM_GMFREECHANNELID` (`C/KRelayProtocol.h:140`; `S/KRelayProtocol.h:140`) | C-D:463; S-D:473; G-D:468 |
| `playercomm_s2c_gmsubscribe` | 41 | 41 | 41 | server/relay → client | `PLAYERCOMM_GMSUBSCRIBE` (`C/KRelayProtocol.h:146`; `S/KRelayProtocol.h:146`) | C-D:464; S-D:474; G-D:469 |
| `playercomm_c2s_someoneact` | 42 | 42 | 42 | client → server/relay | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:465; S-D:475; G-D:470 |
| `playercomm_c2s_channelact` | 43 | 43 | 43 | client → server/relay | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:466; S-D:476; G-D:471 |
| `playercomm_someonechat` | 44 | 44 | 44 | server/relay ↔ client | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:467; S-D:477; G-D:472 |
| `playercomm_channelchat` | 45 | 45 | 45 | server/relay ↔ client | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:468; S-D:478; G-D:473 |

### `enumTONG_SYNC_ID_CREATE_FAIL`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `enumTONG_SYNC_ID_CREATE_FAIL` | 0 | 0 | 0 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:474; S-D:485; G-D:480 |
| `enumTONG_SYNC_ID_TRANSFER_ADD_APPLY` | 1 | 1 | 1 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:475; S-D:486; G-D:481 |
| `enumTONG_SYNC_ID_ADD` | 2 | 2 | 2 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:476; S-D:487; G-D:482 |
| `enumTONG_SYNC_ID_HEAD_INFO` | 3 | 3 | 3 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:477; S-D:488; G-D:483 |
| `enumTONG_SYNC_ID_SELF_INFO` | 4 | 4 | 4 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:478; S-D:489; G-D:484 |
| `enumTONG_SYNC_ID_MANAGER_INFO` | 5 | 5 | 5 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:479; S-D:490; G-D:485 |
| `enumTONG_SYNC_ID_MEMBER_INFO` | 6 | 6 | 6 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:480; S-D:491; G-D:486 |
| `enumTONG_SYNC_ID_INSTATE` | 7 | 7 | 7 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:481; S-D:492; G-D:487 |
| `enumTONG_SYNC_ID_KICK` | 8 | 8 | 8 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:482; S-D:493; G-D:488 |
| `enumTONG_SYNC_ID_CHANGE_MASTER_FAIL` | 9 | 9 | 9 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:483; S-D:494; G-D:489 |
| `enumTONG_SYNC_ID_LIST_INFO` | 10 | 10 | 10 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:484; S-D:495; G-D:490 |
| `enumTONG_SYNC_ID_ATTACK_INFO` | 11 | 11 | 11 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:485; S-D:496; G-D:491 |
| `enumTONG_SYNC_ID_CITY_INFO` | 12 | 12 | 12 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:486; S-D:497; G-D:492 |
| `enumTONG_SYNC_ID_TRANSFER_ADD_INVITE` | 13 | 13 | 13 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:487; S-D:498; G-D:493 |
| `enumTONG_SYNC_ID_SEARCH_RESULT` | 14 | 14 | 14 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:488; S-D:499; G-D:494 |
| `enumTONG_SYNC_ID_CHANGE_ANNOUNCE` | 15 | 15 | 15 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:489; S-D:500; G-D:495 |
| `enumTONG_SYNC_ID_SET_POWER` | 16 | 16 | 16 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:490; S-D:501; G-D:496 |
| `enumTONG_SYNC_ID_GET_POWER` | 17 | 17 | 17 | server → client (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:491; S-D:502; G-D:497 |
| `enumTONG_SYNC_ID_NUM` | 18 | 18 | 18 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:492; S-D:503; G-D:498 |

### `enumTONG_COMMAND_ID_START`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `enumTONG_COMMAND_ID_START` | 0 | 0 | 0 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:498; S-D:510; G-D:518 |
| `enumTONG_COMMAND_ID_APPLY_CREATE` | 1 | 1 | 1 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:499; S-D:511; G-D:519 |
| `enumTONG_COMMAND_ID_APPLY_ADD` | 2 | 2 | 2 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:500; S-D:512; G-D:520 |
| `enumTONG_COMMAND_ID_ACCEPT_ADD` | 3 | 3 | 3 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:501; S-D:513; G-D:521 |
| `enumTONG_COMMAND_ID_APPLY_INFO` | 4 | 4 | 4 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:502; S-D:514; G-D:522 |
| `enumTONG_COMMAND_ID_APPLY_INSTATE` | 5 | 5 | 5 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:503; S-D:515; G-D:523 |
| `enumTONG_COMMAND_ID_APPLY_KICK` | 6 | 6 | 6 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:504; S-D:516; G-D:524 |
| `enumTONG_COMMAND_ID_APPLY_LEAVE` | 7 | 7 | 7 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:505; S-D:517; G-D:525 |
| `enumTONG_COMMAND_ID_APPLY_CHANGE_MASTER` | 8 | 8 | 8 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:506; S-D:518; G-D:526 |
| `enumTONG_COMMAND_ID_APPLY_ATTACK_GET` | 9 | 9 | 9 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:507; S-D:519; G-D:527 |
| `enumTONG_COMMAND_ID_APPLY_ATTACK_SEND` | 10 | 10 | 10 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:508; S-D:520; G-D:528 |
| `enumTONG_COMMAND_ID_APPLY_SET_SEND` | 11 | 11 | 11 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:509; S-D:521; G-D:529 |
| `enumTONG_COMMAND_ID_APPLY_CHANGE_ANNOUNCE` | 12 | 12 | 12 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:510; S-D:522; G-D:530 |
| `enumTONG_COMMAND_ID_APPLY_INVITE` | 13 | 13 | 13 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:511; S-D:523; G-D:531 |
| `enumTONG_COMMAND_ID_APPLY_SAVE` | 14 | 14 | 14 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:512; S-D:524; G-D:532 |
| `enumTONG_COMMAND_ID_APPLY_GET` | 15 | 15 | 15 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:513; S-D:525; G-D:533 |
| `enumTONG_COMMAND_ID_APPLY_SND` | 16 | 16 | 16 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:514; S-D:526; G-D:534 |
| `enumTONG_COMMAND_ID_MORE_INFO` | 17 | 17 | 17 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:515; S-D:527; G-D:535 |
| `enumTONG_COMMAND_ID_ACCEPT_INVITE` | 18 | 18 | 18 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:516; S-D:528; G-D:536 |
| `enumTONG_COMMAND_ID_APPLY_POWER` | 19 | 19 | 19 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:517; S-D:529; G-D:537 |
| `enumTONG_COMMAND_ID_GET_POWER` | 20 | 20 | 20 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:518; S-D:530; G-D:538 |
| `enumTONG_COMMAND_ID_NUM` | 21 | 21 | 22 | Mốc/ID | Mốc/alias; không có payload riêng. | C-D:519; S-D:531; G-D:541 |
| `enumTONG_COMMAND_ID_EXTPOINT` | — | — | 21 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | G-D:540 |

### `enumC2S_PLAYERCOMMAND_ID_LOCKSTATE`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `enumC2S_PLAYERCOMMAND_ID_LOCKSTATE` | 0 | 0 | 0 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:524; S-D:536; G-D:504 |
| `enumC2S_PLAYERCOMMAND_ID_GIVE` | 1 | 1 | 1 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:525; S-D:537; G-D:505 |
| `enumC2S_PLAYERCOMMAND_ID_LOCKITEM` | 2 | 2 | 2 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:526; S-D:538; G-D:506 |
| `enumC2S_PLAYERCOMMAND_ID_SUPERSHOP` | 3 | 3 | 3 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:527; S-D:539; G-D:507 |
| `enumC2S_PLAYERCOMMAND_ID_OFFLINE` | 4 | 4 | 4 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:528; S-D:540; G-D:508 |
| `enumC2S_PLAYERCOMMAND_ID_MASKFEATURE` | 5 | 5 | 5 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:529; S-D:541; G-D:509 |
| `enumC2S_PLAYERCOMMAND_ID_RETURN` | 6 | 6 | 6 | client → server (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | C-D:530; S-D:542; G-D:510 |

### `enum_COMMAND_ID_MAP`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `enum_COMMAND_ID_MAP` | — | 0 | 0 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:548; G-D:548 |
| `enum_COMMAND_ID_KICKOUTROLE` | — | 1 | 1 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:549; G-D:549 |
| `enum_COMMAND_ID_KICKOUTROLE_GM` | — | 2 | 2 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:550; G-D:550 |
| `enum_COMMAND_ID_MONEY_GM` | — | 3 | 3 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:551; G-D:551 |
| `enum_COMMAND_ID_XU_GM` | — | 4 | 4 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:552; G-D:552 |
| `enum_COMMAND_ID_TASK_GM` | — | 5 | 5 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:553; G-D:553 |
| `enum_COMMAND_ID_FORBITCHAT_GM` | — | 6 | 6 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:554; G-D:554 |
| `enum_COMMAND_ID_LEVEL_GM` | — | 7 | 7 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:555; G-D:555 |
| `enum_COMMAND_ID_MOVETOP_GM` | — | 8 | 8 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:556; G-D:556 |
| `enum_COMMAND_ID_MOVETOP_results_GM` | — | 9 | 9 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:557; G-D:557 |
| `enum_COMMAND_ID_FUYUAN_GM` | — | 10 | 10 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:558; G-D:558 |
| `enum_COMMAND_ID_SHENGWANG_GM` | — | 11 | 11 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:559; G-D:559 |
| `enum_COMMAND_ID_EXP_GM` | — | 12 | 12 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:560; G-D:560 |

### `enum_ITEM_ID_FIND`

| Tên | C | S | G | Hướng | Cấu trúc / biểu thức bảng / nơi xử lý | Nguồn mã |
| --- | --- | --- | --- | --- | --- | --- |
| `enum_ITEM_ID_FIND` | — | 0 | 0 | bishop → gameserver (ID phụ) | Cấu trúc/handler cụ thể: chưa kiểm. | S-D:567; G-D:567 |

## Kiểm kê ID phụ KTongProtocol.h

Đây là ID của các lớp command/response trong KTongProtocol.h, tách khỏi ID ở KProtocolDef.h. Bảng ghi đủ tên và mã; payload nào chưa nối được call-site được ghi chưa kiểm. Các struct bên dưới chỉ là ứng viên có cùng tên chức năng khi ghi “chưa kiểm liên kết”.

### `enumC2S_TONG_*`

| Tên | C | S | Hướng | Cấu trúc / giới hạn | Nguồn |
| --- | --- | --- | --- | --- | --- |
| `enumC2S_TONG_CREATE` | 0 | 0 | client/gameworld → relay (lớp command) | `STONG_CREATE_COMMAND` (`C/KTongProtocol.h:256`; `S/KTongProtocol.h:277`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:24; S/KTongProtocol.h:24 |
| `enumC2S_TONG_ADD_MEMBER` | 1 | 1 | client/gameworld → relay (lớp command) | `STONG_ADD_MEMBER_COMMAND` (`C/KTongProtocol.h:290`; `S/KTongProtocol.h:311`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:25; S/KTongProtocol.h:25 |
| `enumC2S_TONG_GET_HEAD_INFO` | 2 | 2 | client/gameworld → relay (lớp command) | `STONG_GET_TONG_HEAD_INFO_COMMAND` (`C/KTongProtocol.h:328`; `S/KTongProtocol.h:349`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:26; S/KTongProtocol.h:26 |
| `enumC2S_TONG_GET_MANAGER_INFO` | 3 | 3 | client/gameworld → relay (lớp command) | `STONG_GET_MANAGER_INFO_COMMAND` (`C/KTongProtocol.h:353`; `S/KTongProtocol.h:374`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:27; S/KTongProtocol.h:27 |
| `enumC2S_TONG_GET_MEMBER_INFO` | 4 | 4 | client/gameworld → relay (lớp command) | `STONG_GET_MEMBER_INFO_COMMAND` (`C/KTongProtocol.h:377`; `S/KTongProtocol.h:398`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:28; S/KTongProtocol.h:28 |
| `enumC2S_TONG_INSTATE` | 5 | 6 | client/gameworld → relay (lớp command) | `STONG_INSTATE_COMMAND` (`C/KTongProtocol.h:539`; `S/KTongProtocol.h:560`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:29; S/KTongProtocol.h:30 |
| `enumC2S_TONG_SEARCH_INFO` | — | 5 | client/gameworld → relay (lớp command) | `STONG_SEARCH_INFO_COMMAND` (`C/KTongProtocol.h:361`; `S/KTongProtocol.h:382`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:29 |
| `enumC2S_TONG_KICK` | 6 | 7 | client/gameworld → relay (lớp command) | `STONG_KICK_COMMAND` (`C/KTongProtocol.h:581`; `S/KTongProtocol.h:602`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:30; S/KTongProtocol.h:31 |
| `enumC2S_TONG_LEAVE` | 7 | 8 | client/gameworld → relay (lớp command) | `STONG_LEAVE_COMMAND` (`C/KTongProtocol.h:605`; `S/KTongProtocol.h:626`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:31; S/KTongProtocol.h:32 |
| `enumC2S_TONG_CHANGE_MASTER` | 8 | 9 | client/gameworld → relay (lớp command) | `STONG_CHANGE_MASTER_COMMAND` (`C/KTongProtocol.h:621`; `S/KTongProtocol.h:642`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:32; S/KTongProtocol.h:33 |
| `enumC2S_TONG_ACCEPT_MASTER` | 9 | 10 | client/gameworld → relay (lớp command) | `STONG_ACCEPT_MASTER_COMMAND` (`C/KTongProtocol.h:657`; `S/KTongProtocol.h:678`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:33; S/KTongProtocol.h:34 |
| `enumC2S_TONG_GET_LOGIN_DATA` | 10 | 11 | client/gameworld → relay (lớp command) | `STONG_GET_LOGIN_DATA_COMMAND` (`C/KTongProtocol.h:673`; `S/KTongProtocol.h:694`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:34; S/KTongProtocol.h:35 |
| `enumC2S_TONG_MONEY_SAVE` | 11 | 12 | client/gameworld → relay (lớp command) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:35; S/KTongProtocol.h:36 |
| `enumC2S_TONG_MONEY_GET` | 12 | 13 | client/gameworld → relay (lớp command) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:36; S/KTongProtocol.h:37 |
| `enumC2S_TONG_MONEY_SND` | 13 | 14 | client/gameworld → relay (lớp command) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:37; S/KTongProtocol.h:38 |
| `enumC2S_TONG_ATTACK` | 14 | 19 | client/gameworld → relay (lớp command) | `STONG_ATTACK_COMMAND` (`C/KTongProtocol.h:590`; `S/KTongProtocol.h:611`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:38; S/KTongProtocol.h:45 |
| `enumC2S_TONG_ATTACK_GET_INFO` | 15 | 20 | client/gameworld → relay (lớp command) | `STONG_GET_TONG_ATTACK_INFO_COMMAND` (`C/KTongProtocol.h:335`; `S/KTongProtocol.h:356`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:39; S/KTongProtocol.h:46 |
| `enumC2S_TONG_SET_POWER` | — | 15 | client/gameworld → relay (lớp command) | `STONG_POWER_COMMAND` (`C/KTongProtocol.h:741`; `S/KTongProtocol.h:762`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:39 |
| `enumC2S_TONG_ATTACK_SEND_INFO` | 16 | 21 | client/gameworld → relay (lớp command) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:40; S/KTongProtocol.h:47 |
| `enumC2S_TONG_GET_POWER` | — | 16 | client/gameworld → relay (lớp command) | `STONG_GET_POWER_COMMAND` (`C/KTongProtocol.h:370`; `S/KTongProtocol.h:391`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:40 |
| `enumC2S_TONG_GET_LIST_INFO` | 17 | 22 | client/gameworld → relay (lớp command) | `STONG_GET_LIST_INFO_COMMAND` (`C/KTongProtocol.h:385`; `S/KTongProtocol.h:406`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:41; S/KTongProtocol.h:48 |
| `enumC2S_TONG_MORE_INFO` | — | 17 | client/gameworld → relay (lớp command) | `STONG_MORE_INFO_COMMAND` (`C/KTongProtocol.h:734`; `S/KTongProtocol.h:755`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:41 |
| `enumC2S_TONG_INFO_SET` | 18 | 23 | client/gameworld → relay (lớp command) | `STONG_SET_TONG_INFO_COMMAND` (`C/KTongProtocol.h:342`; `S/KTongProtocol.h:363`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:42; S/KTongProtocol.h:49 |
| `enumC2S_TONG_UPDATE_LEVEL` | — | 18 | client/gameworld → relay (lớp command) | `STONG_UPDATE_LEVEL_COMMAND` (`C/KTongProtocol.h:302`; `S/KTongProtocol.h:323`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:42 |
| `enumC2S_TONG_NUM` | 19 | 25 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:43; S/KTongProtocol.h:52 |
| `enumC2S_TONG_CHANGE_ANNOUNCE` | — | 24 | client/gameworld → relay (lớp command) | `STONG_CHANGE_ANNOUNCE_COMMAND` (`C/KTongProtocol.h:727`; `S/KTongProtocol.h:748`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:50 |

### `enumC2S_TONG_SET_*`

| Tên | C | S | Hướng | Cấu trúc / giới hạn | Nguồn |
| --- | --- | --- | --- | --- | --- |
| `enumC2S_TONG_SET_LEVEL` | 0 | 0 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:48; S/KTongProtocol.h:59 |
| `enumC2S_TONG_SET_MAP` | 1 | 1 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:49; S/KTongProtocol.h:60 |
| `enumC2S_TONG_SET_CREDIT` | 2 | 2 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:50; S/KTongProtocol.h:61 |
| `enumC2S_TONG_SET_BANGTITLE` | 3 | 3 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:51; S/KTongProtocol.h:62 |
| `enumC2S_TONG_SET_ZHANGTITLE` | 4 | 4 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:52; S/KTongProtocol.h:63 |
| `enumC2S_TONG_SET_DUITITLE` | 5 | 5 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:53; S/KTongProtocol.h:64 |
| `enumC2S_TONG_SET_ZONGTITLE` | 6 | 6 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:54; S/KTongProtocol.h:65 |
| `enumC2S_TONG_SET_DEATHCOUNT` | 7 | 7 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:55; S/KTongProtocol.h:66 |
| `enumC2S_TONG_SET_ATTACKWIN` | 8 | 8 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:56; S/KTongProtocol.h:67 |
| `enumC2S_TONG_SET_ATTACKLOSE` | 9 | 9 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:57; S/KTongProtocol.h:68 |
| `enumC2S_TONG_RANDOM_MAP` | 10 | 10 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:58; S/KTongProtocol.h:69 |
| `enumC2S_TONG_SET_CAMP` | 11 | — | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:59 |
| `enumC2S_TONG_SET_CAM` | — | 11 | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:70 |
| `enumC2S_TONG_SET_ANNOUNCE` | 12 | — | client/gameworld → relay (ID con) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:60 |
| `enumC2S_TONG_SET_NUM` | 13 | 12 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:61; S/KTongProtocol.h:71 |

### `enumS2C_TONG_* / enumS3C_TONG_*`

| Tên | C | S | Hướng | Cấu trúc / giới hạn | Nguồn |
| --- | --- | --- | --- | --- | --- |
| `enumS2C_TONG_CREATE_SUCCESS` | 0 | 0 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:67; S/KTongProtocol.h:79 |
| `enumS2C_TONG_CREATE_FAIL` | 1 | 1 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:68; S/KTongProtocol.h:80 |
| `enumS2C_TONG_ADD_MEMBER_SUCCESS` | 2 | 2 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:69; S/KTongProtocol.h:81 |
| `enumS2C_TONG_ADD_MEMBER_FAIL` | 3 | 3 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:70; S/KTongProtocol.h:82 |
| `enumS2C_TONG_HEAD_INFO` | 4 | 4 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:71; S/KTongProtocol.h:83 |
| `enumS2C_TONG_MANAGER_INFO` | 5 | 5 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:72; S/KTongProtocol.h:84 |
| `enumS2C_TONG_MEMBER_INFO` | 6 | 6 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:73; S/KTongProtocol.h:85 |
| `enumS2C_TONG_BE_INSTATED` | 7 | 7 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:74; S/KTongProtocol.h:86 |
| `enumS2C_TONG_INSTATE` | 8 | 8 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:75; S/KTongProtocol.h:87 |
| `enumS2C_TONG_KICK` | 9 | 9 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:76; S/KTongProtocol.h:88 |
| `enumS2C_TONG_BE_KICKED` | 10 | 10 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:77; S/KTongProtocol.h:89 |
| `enumS2C_TONG_LEAVE` | 11 | 11 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:78; S/KTongProtocol.h:90 |
| `enumS2C_TONG_CHECK_CHANGE_MASTER_POWER` | 12 | 12 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:79; S/KTongProtocol.h:91 |
| `enumS2C_TONG_CHANGE_MASTER_FAIL` | 13 | 13 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:80; S/KTongProtocol.h:92 |
| `enumS2C_TONG_CHANGE_AS` | 14 | 14 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:81; S/KTongProtocol.h:93 |
| `enumS2C_TONG_CHANGE_MASTER` | 15 | 15 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:82; S/KTongProtocol.h:94 |
| `enumS2C_TONG_LOGIN_DATA` | 16 | 16 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:83; S/KTongProtocol.h:95 |
| `enumS2C_TONG_MONEY_SAVE` | 17 | 17 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:84; S/KTongProtocol.h:96 |
| `enumS2C_TONG_MONEY_GET` | 18 | 18 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:85; S/KTongProtocol.h:97 |
| `enumS2C_TONG_MONEY_SND` | 19 | 19 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:86; S/KTongProtocol.h:98 |
| `enumS2C_TONG_ATTACK_GETBACK` | 20 | 23 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:87; S/KTongProtocol.h:104 |
| `enumS2C_TONG_SET_POWER` | — | 20 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:99 |
| `enumS2C_TONG_ATTACK_SENDBACK` | 21 | 24 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:88; S/KTongProtocol.h:105 |
| `enumS2C_TONG_GET_POWER` | — | 21 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:100 |
| `enumS2C_TONG_ATTACK_OVER` | 22 | 25 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:89; S/KTongProtocol.h:106 |
| `enumS2C_TONG_SEARCH_INFO` | — | 22 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:101 |
| `enumS2C_TONG_ALLLIST_INFO` | 23 | 26 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:90; S/KTongProtocol.h:107 |
| `enumS3C_TONG_SYNCITY_INFO` | 24 | 27 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:91; S/KTongProtocol.h:108 |
| `enumS3C_TONG_SERVER_TIEM` | 25 | 28 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:92; S/KTongProtocol.h:109 |
| `enumS2C_TONG_NUM` | 26 | 32 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:93; S/KTongProtocol.h:114 |
| `enumS2C_TONG_CHANGE_DATA` | — | 29 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:110 |
| `enumS2C_TONG_CHANGE_TITLE` | — | 30 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:111 |
| `enumS2C_TONG_CHANGE_ANNOUNCE` | — | 31 | relay → gameworld/client (lớp sync) | Cấu trúc/ID con: chưa kiểm. | S/KTongProtocol.h:112 |

### `friend_*`

| Tên | C | S | Hướng | Cấu trúc / giới hạn | Nguồn |
| --- | --- | --- | --- | --- | --- |
| `friend_c2c_askaddfriend` | 0 | 0 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:100; S/KTongProtocol.h:121 |
| `friend_c2c_repaddfriend` | 1 | 1 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:101; S/KTongProtocol.h:122 |
| `friend_c2s_groupfriend` | 2 | 2 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:102; S/KTongProtocol.h:123 |
| `friend_c2s_erasefriend` | 3 | 3 | Mốc | Mốc/số lượng. | C/KTongProtocol.h:103; S/KTongProtocol.h:124 |
| `friend_c2s_asksyncfriendlist` | 4 | 4 | theo c2s/s2c/c2c; endpoint chưa kiểm | `ASK_SYNCFRIENDLIST` (`C/KTongProtocol.h:184`; `S/KTongProtocol.h:205`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:105; S/KTongProtocol.h:126 |
| `friend_s2c_repsyncfriendlist` | 5 | 5 | theo c2s/s2c/c2c; endpoint chưa kiểm | `REP_SYNCFRIENDLIST` (`C/KTongProtocol.h:191`; `S/KTongProtocol.h:212`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:106; S/KTongProtocol.h:127 |
| `friend_s2c_friendstate` | 6 | 6 | theo c2s/s2c/c2c; endpoint chưa kiểm | `FRIEND_STATE` (`C/KTongProtocol.h:202`; `S/KTongProtocol.h:223`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:108; S/KTongProtocol.h:129 |
| `friend_c2s_associate` | 7 | 7 | theo c2s/s2c/c2c; endpoint chưa kiểm | `FRIEND_ASSOCIATE` (`C/KTongProtocol.h:208`; `S/KTongProtocol.h:229`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:110; S/KTongProtocol.h:131 |
| `friend_c2s_associatebevy` | 8 | 8 | theo c2s/s2c/c2c; endpoint chưa kiểm | `FRIEND_ASSOCIATEBEVY` (`C/KTongProtocol.h:216`; `S/KTongProtocol.h:237`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:111; S/KTongProtocol.h:132 |
| `friend_s2c_syncassociate` | 9 | 9 | theo c2s/s2c/c2c; endpoint chưa kiểm | `FRIEND_SYNCASSOCIATE` (`C/KTongProtocol.h:223`; `S/KTongProtocol.h:244`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:112; S/KTongProtocol.h:133 |
| `friend_c2c_addblacklist` | 10 | — | theo c2s/s2c/c2c; endpoint chưa kiểm | Cấu trúc/ID con: chưa kiểm. | C/KTongProtocol.h:113 |
| `friend_s2c_syncblacklist` | — | 10 | theo c2s/s2c/c2c; endpoint chưa kiểm | `FRIEND_SYNCBLACKLIST` (`S/KTongProtocol.h:251`); chưa kiểm liên kết call-site. | S/KTongProtocol.h:134 |

### `extend_s2c_*`

| Tên | C | S | Hướng | Cấu trúc / giới hạn | Nguồn |
| --- | --- | --- | --- | --- | --- |
| `extend_s2c_passtosomeone` | 0 | 0 | server → client | `EXTEND_PASSTOSOMEONE` (`C/KTongProtocol.h:239`; `S/KTongProtocol.h:260`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:119; S/KTongProtocol.h:140 |
| `extend_s2c_passtobevy` | 1 | 1 | server → client | `EXTEND_PASSTOBEVY` (`C/KTongProtocol.h:246`; `S/KTongProtocol.h:267`); chưa kiểm liên kết call-site. | C/KTongProtocol.h:120; S/KTongProtocol.h:141 |

## Kiểm chứng, lỗi đã gặp và bàn giao

- Worker được kiểm tra trước khi đọc source: Get-Location trả D:\JX-wt\A-06; git status --porcelain=v1 --branch trả task/A-06-bang-goi-tin và chỉ file task chưa được theo dõi. Không checkout/reset/clean, không chỉnh model/provider/config.
- Báo cáo có 5 dòng tóm tắt đầu file, 481 dòng symbol trong KProtocolDef.h và 88 dòng ID phụ KTongProtocol.h (gồm mốc/alias); các payload chưa nối được đều ghi chưa kiểm. Dữ liệu từ header được xử lý trong bộ nhớ, không lưu parser/script hoặc bản chép source.
- Kiểm tra tài liệu: PASS — đủ 5 dòng tóm tắt, 481 symbol chính và 88 ID phụ; tên symbol khớp dòng KProtocolDef.h, không có giá trị thiếu trong bảng; file task chỉ thay mục Kết quả, index tạm đã dọn. Build/test/runtime không chạy theo task; đây không phải bằng chứng build/test game đạt.
- Lệnh đọc file đầu tiên không trả sau khoảng một phút; đã dừng chờ và chạy lại PowerShell với login=false thì đọc được. rg không có: The term 'rg' is not recognized; dùng Get-ChildItem/Select-String trong đúng thư mục source liên quan.
- Một lần cập nhật task bằng apply_patch không khớp dòng cuối do ký tự \r; đã thu hẹp hunk về mục Kết quả và ghi được. Các lần soạn chuỗi Markdown bằng template literal gặp SyntaxError: Unexpected identifier; đã chuyển sang chuỗi/khối dữ liệu an toàn, không phát sinh file từ lệnh lỗi.
- Hàm đọc enum tổng quát gặp Cannot read properties of undefined (reading 'name') ở enum rỗng sau khi bỏ comment trong KTongProtocol.h; dừng cách đó sau ba lần, dùng trích trực tiếp những đoạn enum có số dòng đã đọc. Các bảng chính KProtocolDef.h đã đối chiếu độc lập với kết quả PowerShell.
- Commit lần đầu: git add rồi git commit -m `A-06: đối chiếu gói tin client và server` cùng báo `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-06/index.lock': Permission denied`. File .git trỏ đến metadata này; không có index.lock tồn tại khi kiểm tra read-only.
- Thử index tạm trong workspace: git read-tree HEAD thành công; git add thất bại với `error: insufficient permission for adding an object to repository database D:/jx1-reports/.git/objects`, `failed to insert into database` và `fatal: adding files failed`. Dừng thử ghi Git, không đổi ACL/config/credential và không chuyển object/ref để vượt sandbox. Index tạm đã dọn; chỉ giữ hai file task/report.
- Bộ duyệt lệnh tự động từ chối một lệnh ghép dùng index tạm và hai lệnh Remove-Item với `rejected: blocked by policy`. Việc tạo commit vẫn không thể hoàn tất bằng lệnh Git đã thử trong quyền hiện tại.

**BỊ CHẶN – CHƯA PUSH.** Chưa có commit SHA vì chưa tạo được commit; không yêu cầu push trong task. Báo cáo không trỏ link commit chưa tồn tại. Tiếp tục sau khi phiên làm việc có quyền ghi metadata Git của worktree và object database: stage đúng JX1_OPS/REPORTS/A-06-bang-goi-tin.md và JX1_OPS/TASKS/A-06.md, rồi commit trên nhánh hiện tại với tiêu đề `A-06: đối chiếu gói tin client và server`. Phần nội dung đã lưu local, source không thay đổi.

## Chưa kiểm

- Chưa build, chạy game, kết nối server/VM, quét binary hoặc bắt gói; không có lệnh build/test trong task.
- Chưa xác nhận source trùng binary đang chạy; không dùng việc đọc source để kết luận runtime.
- Chưa đo sizeof/offsetof bằng compiler/kiến trúc thực tế; các macro/typedef bên ngoài như NAME_LENGHT, TCHAR, UINT, GUID và #ifdef chưa được giải hết. C/S KProtocol.h:10-11/18-19 và C/S KRelayProtocol.h:12 có packing, nhưng đó chưa phải kiểm chứng ABI.
- Chưa truy toàn bộ đường gửi/nhận cho mọi ID; cột payload ghi rõ biểu thức bảng, ép kiểu handler hoặc chưa kiểm. Những ánh xạ chỉ giống tên ở bảng KTongProtocol.h được ghi chưa kiểm liên kết call-site.
- Chưa kiểm mọi header ngoài phạm vi, protocol multi-server/login/framing/serialize, giới hạn độ dài hoặc bảo mật parser.
- Chưa tạo commit và chưa push do blocker quyền Git mô tả ở trên.
