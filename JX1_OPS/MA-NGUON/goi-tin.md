# Danh sách gói tin client↔server (tự sinh, chỉ đọc)

Lấy từ các `enum *_PROTOCOL` trong `KProtocolDef.h` (gameserver và gateway). Mã gói = thứ tự trong enum (bắt đầu từ 0 nếu không gán). "Tệp dùng" là các tệp nguồn nhắc tới tên gói.

## s2c_PROTOCOL (gameserver)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 10 | `s2c_rolehjdkalritopq_getroleinfo_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 11 | `s2c_syncogjfkdnvhf_roleinfo_cipher` |  | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 12 | `s2c_gamestatistic_bigpackage` |  | `KProtocolDef.h`, `ClientNode.cpp` |
| 13 | `s2c_micfghjkdtropackbegin` | 小包开始  31 排名 | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 32 | `s2c_accountbegin` |  | `KProtocolDef.h`, `Cipher.h`, `Cipher.h`, `Cipher.h` |
| 33 | `s2c_accountfdfsglogin` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `Intercessor.cpp`, `S3PDBSocketPool.cpp` |
| 34 | `s2c_gamelogin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 35 | `s2c_accountlogout` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 36 | `s2c_gatewayverify` | 用于连接后第一个包 | `KProtocolDef.h`, `SmartClient.cpp`, `Intercessor.cpp`, `RootClient.cpp` |
| 37 | `s2c_gatewayverifyagain` | 用于重连后第一个包 | `KProtocolDef.h` |
| 38 | `s2c_gatewayinfo` |  | `KProtocolDef.h`, `GatewayClient.cpp`, `HostConnect.cpp`, `RootClient.cpp` |
| 48 | `s2c_multiserverbegin` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 49 | `s2c_querymapinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GamePlayer.cpp` |
| 50 | `s2c_querygameserverinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 51 | `s2c_identitymapping` |  | `KProtocol.h`, `KProtocolDef.h` |
| 52 | `s2c_notifypl_ayerlogin_hfkqotivbhd` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 53 | `s2c_notifyplayerexchange` |  | `KProtocol.h`, `KProtocolDef.h`, `KgameWorld.cpp`, `KSelPlayer.cpp` |
| 54 | `s2c_notifysvrip` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp`, `GatewayClient.cpp` |
| 55 | `s2c_roleserver_getrolelist_result` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 56 | `s2c_roleserver_saverole_result` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 57 | `s2c_roleserver_createrole_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 58 | `s2c_roleserver_deleterole_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 59 | `s2c_logiclogout` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp` |
| 60 | `s2c_gateway_broadcast` | 同步播报 | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 61 | `s2c_gamestatistic` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 62 | `s2c_rolecheckname_result` | 检测角色名的 返回结果 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `KSOServer.cpp` |
| 63 | `s2c_gwsyn_broadcast` | 同步播报 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 64 | `s2c_clientbegin` |  | `CoreShell.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 65 | `s2c_login` | ref: ../../S3Client/Login/LoginDef.h | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `LoginDef.h` |
| 66 | `s2c_logout` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 67 | `s2c_syncclientend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 68 | `s2c_synonlineplayer` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 69 | `s2c_synccurplayerskill` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 70 | `s2c_synccurplayernormal` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 71 | `s2c_newplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 72 | `s2c_removeplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 73 | `s2c_syncworld` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 74 | `s2c_syncplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 75 | `s2c_syncplayermin` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 76 | `s2c_syncnpc` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 77 | `s2c_syncnpcmin` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 78 | `s2c_syncnpcminplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 79 | `s2c_objadd` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 80 | `s2c_syncobjstate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 81 | `s2c_syncobjdir` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 82 | `s2c_objremove` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 83 | `s2c_objTrapAct` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 84 | `s2c_npcremove` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 85 | `s2c_npcwalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 86 | `s2c_npcrun` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 87 | `s2c_npcattack` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 88 | `s2c_npcmagic` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 89 | `s2c_npcjump` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 90 | `s2c_npctalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 91 | `s2c_npchurt` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 92 | `s2c_npcdeath` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 93 | `s2c_npcchgcurcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 94 | `s2c_npcchgcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 95 | `s2c_npcsettmpcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 96 | `s2c_skillcast` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 97 | `s2c_playertalk` |  | `KNpc.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 98 | `s2c_playerexp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 99 | `s2c_teaminfo` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 100 | `s2c_teamselfinfo` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 101 | `s2c_teamapplyinfofalse` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 102 | `s2c_teamcreatesuccess` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 103 | `s2c_teamcreatefalse` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 104 | `s2c_teamopenclose` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 105 | `s2c_teamgetapply` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 106 | `s2c_teamaddmember` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 107 | `s2c_teamleave` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 108 | `s2c_teamchangecaptain` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 109 | `s2c_playerfactiondata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 110 | `s2c_playerleavefaction` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 111 | `s2c_playerfactionskilllevel` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 112 | `s2c_playersendchat` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 113 | `s2c_playersyncleadexp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 114 | `s2c_playerlevelup` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 115 | `s2c_teammatelevel` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 116 | `s2c_playersyncattribute` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 117 | `s2c_playerskilllevel` |  | `KNpcAttribModify.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 118 | `s2c_syncitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 119 | `s2c_removeitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 120 | `s2c_syncmonfs` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 121 | `s2c_syncqianfs` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 122 | `s2c_playermoveitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 123 | `s2c_scriptaction` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp`, `KPlayer - Copy - Copy.cpp` |
| 124 | `s2c_chatapplyaddfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 125 | `s2c_chataddfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 126 | `s2c_chatrefusefriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 127 | `s2c_chataddfriendfail` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 128 | `s2c_chatloginfriendnoname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 129 | `s2c_chatloginfriendname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 130 | `s2c_chatonefrienddata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 131 | `s2c_chatfriendonline` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 132 | `s2c_chatdeletefriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 133 | `s2c_chatfriendoffline` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 134 | `s2c_syncrolelist` | 没有给调用 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 135 | `s2c_tradechangestate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerMenuState.cpp` |
| 136 | `s2c_npcsetmenustate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerMenuState.cpp` |
| 137 | `s2c_trademoneysync` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 138 | `s2c_tradedecision` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 139 | `s2c_chatscreensingleerror` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 140 | `s2c_syncnpcstate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 141 | `s2c_teaminviteadd` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 142 | `s2c_tradepressoksync` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 143 | `s2c_ping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 144 | `s2c_npcsit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 145 | `s2c_npcstand` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 146 | `s2c_opensalebox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 147 | `s2c_castskilldirectly` | 有BUG | `KNpc.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 148 | `s2c_msgshow` |  | `KNpc.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 149 | `s2c_syncstateeffect` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 150 | `s2c_openstorebox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 151 | `s2c_openresetpass` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 152 | `s2c_openstringbox` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 153 | `s2c_opendataubox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 154 | `s2c_playerrevive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 155 | `s2c_requestnpcfail` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpcSet.cpp` |
| 156 | `s2c_tradeapplystart` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 157 | `s2c_rolenewdelresponse` | 新建与删除角色的结果返回,所带数据为结构tagNewDelRoleResponse | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `Klogin.cpp` |
| 158 | `s2c_ItemAutoMove` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 159 | `s2c_itemexchangefinish` |  | `KItemList.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 160 | `s2c_changeweather` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 161 | `s2c_pksyncnormalflag` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 162 | `s2c_pksyncenmitystate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 163 | `s2c_pksyncexercisestate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 164 | `s2c_pksyncpkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 165 | `s2c_reputesyncreputevalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerRepute.cpp` |
| 166 | `s2c_fuyuansyncfuyuanvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerFuYuan.cpp` |
| 167 | `s2c_rebornsyncrebornvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerReBorn.cpp` |
| 168 | `s2c_openmarketbox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 169 | `s2c_npcsleepmode` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 170 | `s2c_viewequip` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 171 | `s2c_ladderresult` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 172 | `s2c_ladderlist` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 173 | `s2c_tongcreate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTong.cpp` |
| 174 | `s2c_replyclientping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 175 | `s2c_npcgoldchange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpcGold.cpp` |
| 176 | `s2c_itemdurabilitychange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 177 | `s2c_opentremble` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 178 | `s2c_rankname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 179 | `s2c_viewsellitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 180 | `s2c_viewupdateitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 181 | `s2c_playergetcount` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 182 | `s2c_shopname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 183 | `s2c_syncmasklock` | mat na | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 184 | `s2c_opengive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 185 | `s2c_npcsecmove` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 186 | `s2c_pkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 187 | `s2c_viewlianitem` | 链接 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp` |
| 188 | `s2c_openwengang` | 纹钢 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 189 | `s2c_openstone` | 宝石镶嵌 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 190 | `s2c_updateviewequip` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 191 | `s2c_gettongback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 192 | `s2c_syncequipitem` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 193 | `s2c_taskcallback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTask.cpp` |
| 194 | `s2c_openjindutiao` | 打开进度条 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 195 | `s2c_syncitemposition` | 同步位置(没用) | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 196 | `s2c_openduanzhao` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 197 | `s2c_syncurupdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 198 | `s2c_JinMaicallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 199 | `s2c_openvipdazao` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 200 | `s2c_synnpcinfocallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 201 | `s2c_pautoMovecallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 202 | `s2c_plyerguzicallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 203 | `s2c_syncplayermap` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 204 | `s2c_synconestate` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 205 | `s2c_syncnodataeffect` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 206 | `s2c_npcsetpos` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 207 | `s2c_playermissiondata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 208 | `s2c_syncrankdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 209 | `s2c_syncsupershop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp`, `KProtocolProcess.cpp` |
| 210 | `s2c_syncitem_shop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp`, `KProtocolProcess.cpp` |
| 211 | `s2c_itemdata_shop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp`, `KProtocolProcess.cpp` |
| 212 | `s2c_kickoutgame` | 通知客户端退出游戏 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 213 | `s2c_objadd_vn` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp`, `KProtocol.cpp` |
| 214 | `s2c_rolesyncvipvalue` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerVip.cpp`, `KProtocolProcess.cpp` |
| 215 | `s2c_gm_synroleaction` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `ClientNode.cpp` |
| 216 | `s2c_queryiteminfo` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KSOServer.cpp`, `GameServer.cpp` |
| 217 | `s2c_returnitemlock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 218 | `s2c_findpath_state` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 219 | `s2c_refitemsync` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 220 | `s2c_chestpwsync` | 220 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 250 | `s2c_extend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KRelayProtocol.h` |
| 251 | `s2c_extendchat` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp` |
| 252 | `s2c_extendfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 253 | `s2c_extendchat_new` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp` |
| 254 | `s2c_extendtong` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTong.cpp` |
| 255 | `s2c_end` |  | `CoreShell.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.h` |

## c2s_PROTOCOL (gameserver)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 10 | `c2s_rolekfjhu_saveroleinfo` |  | `KProtocolDef.h`, `KPlayerDBFuns.cpp`, `KSOServer.cpp`, `ClientNode.cpp` |
| 11 | `c2s_roleserver_createroleinfo` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 12 | `c2s_gmsvr2gateway_saverole` |  | `KProtocol.h`, `KProtocolDef.h` |
| 13 | `c2s_micropackbegin` |  | `KProtocolDef.h` |
| 32 | `c2s_accountbegin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 33 | `c2s_accountlogin` | 账号登陆 | `KProtocolDef.h`, `GamePlayer.cpp`, `GamePlayer.cpp`, `S3PDBSocketPool.cpp` |
| 34 | `c2s_gamelogin_dkiqopjgurnmvbgc` | 开始登陆游戏 是否能成功！或提示服务器人满 | `KProtocolDef.h`, `GameServer.cpp`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 35 | `c2s_accountlogout` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `GameServer.cpp`, `S3PDBSocketPool.cpp` |
| 36 | `c2s_gatewayverify` |  | `KProtocolDef.h`, `SmartClient.cpp`, `Intercessor.cpp`, `RootClient.cpp` |
| 37 | `c2s_gatewayverifyagain` |  | `KProtocolDef.h`, `SmartClient.cpp`, `S3PDBSocketPool.cpp` |
| 38 | `c2s_gatewayinfo` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 48 | `c2s_multiserverbegin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 49 | `c2s_permit_logftihmcginqknd` |  | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 50 | `c2s_updatemapinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 51 | `c2s_updategameserverinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 52 | `c2s__entergamegkjyiruqine` | GS 通知开始进入游戏 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp`, `ChatConnect.cpp` |
| 53 | `c2s_leavegame` |  | `KProtocol.h`, `KProtocolDef.h`, `CoreServerShell.cpp`, `KPlayerSet.cpp` |
| 54 | `c2s_registeraccount` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 55 | `c2s_requestsvrip` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp`, `GatewayClient.cpp` |
| 56 | `c2s_roleserver_getrolelist` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp`, `GamePlayer.cpp` |
| 57 | `c2s_roleserver_getroleinfo` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp`, `GamePlayer.cpp` |
| 58 | `c2s_roleserver_deleteplayer` |  | `KProtocolDef.h`, `KuiSelPlayer_new.cpp`, `GamePlayer.cpp`, `Intercessor.cpp` |
| 59 | `c2s_gamestatistic` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 60 | `c2s_roleserver_lock` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KPlayerSet.cpp`, `ScriptFuns.cpp` |
| 64 | `c2s_gameserverbegin` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 65 | `c2s_login_fhgyrinhkmvnsheypo` |  | `KProtocolDef.h`, `Klogin.cpp`, `KuiWarnInfo.cpp`, `KloginVN.cpp` |
| 66 | `c2s__loginfs_kfjghtueodnchsf` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 67 | `c2s_syncclientend` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `KSOServer.cpp` |
| 68 | `c2s_loadplayer` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 69 | `c2s_newplayer` |  | `KProtocol.h`, `KProtocolDef.h`, `KuiNewPlayer.cpp`, `KProtocol.cpp` |
| 70 | `c2s_removeplayer` |  | `KProtocolDef.h`, `KuiAutoPlay.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 71 | `c2s_requestworld` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 72 | `c2s_requestplayer` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 73 | `c2s_requestnpc` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 74 | `c2s_requestobj` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 75 | `c2s_npcwalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 76 | `c2s_npcrun` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 77 | `c2s_npcskill` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 78 | `c2s_npcjump` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 79 | `c2s_npctalk` |  | `KProtocolDef.h`, `KuiItemdescVN.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 80 | `c2s_npchurt` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 81 | `c2s_npcdeath` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 82 | `c2s_playertalk` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 83 | `c2s_teamapplyinfo` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 84 | `c2s_teamapplycreate` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 85 | `c2s_teamapplyopenclose` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 86 | `c2s_teamapplyadd` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 87 | `c2s_teamacceptmember` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 88 | `c2s_teamapplyleave` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 89 | `c2s_teamapplykickmember` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 90 | `c2s_teamapplychangecaptain` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 91 | `c2s_teamapplydismiss` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 92 | `c2s_playerapplysetpk` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 93 | `c2s_playerapplyfactiondata` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 94 | `c2s_playersendchat` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 95 | `c2s_playeraddbaseattribute` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 96 | `c2s_playerapplyaddskillpoint` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 97 | `c2s_playereatitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 98 | `c2s_playerpickupitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 99 | `c2s_playermoveitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 100 | `c2s_playersellitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 101 | `c2s_playerbuyitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 102 | `c2s_playerthrowawayitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 103 | `c2s_playerselui` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 104 | `c2s_chatsetchannel` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 105 | `c2s_chatapplyaddfriend` |  | `KProtocolDef.h`, `KuiPlayerSelFunVN.cpp`, `KPlayerChat.cpp`, `KProtocol.cpp` |
| 106 | `c2s_chataddfriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 107 | `c2s_chatrefusefriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 108 | `c2s_dbplayerselect` |  | `KProtocolDef.h`, `KSelPlayer.cpp`, `KuiSelPlayer_new.cpp`, `KuiWarnInfo.cpp` |
| 109 | `c2s_chatapplyresendallfriendname` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 110 | `c2s_chatapplysendonefriendname` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 111 | `c2s_chatdeletefriend` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 112 | `c2s_chatredeletefriend` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 113 | `c2s_tradeapplystateopen` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 114 | `c2s_tradeapplystateclose` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 115 | `c2s_tradeapplystart` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 116 | `c2s_trademovemoney` |  | `KPlayer.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp` |
| 117 | `c2s_tradedecision` |  | `KPlayer.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp` |
| 118 | `c2s_dialognpc` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 119 | `c2s_teaminviteadd` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 120 | `c2s_changeauraskill` |  | `KNpc.cpp`, `KProtocolDef.h`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 121 | `c2s_teamreplyinvite` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 122 | `c2s_ping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 123 | `c2s_cpunlock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 124 | `c2s_cplock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 125 | `c2s_cpchange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 126 | `c2s_cpreset` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 127 | `c2s_market` | KTC | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 128 | `c2s_string` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 129 | `c2s_datau` |  | `KProtocol.cpp`, `KProtocolDef.h`, `Kuilaotou.cpp`, `KProtocol.cpp` |
| 130 | `c2s_npcsit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 131 | `c2s_objmouseclick` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 132 | `c2s_storemoney` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 133 | `c2s_playerrevive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 134 | `c2s_tradereplystart` |  | `KPlayerTrade.cpp`, `KProtocolDef.h`, `KPlayerTrade.cpp`, `KProtocol.cpp` |
| 135 | `c2s_pkapplychangenormalflag` |  | `KPlayerPK.cpp`, `KProtocolDef.h`, `KPlayerPK.cpp`, `KProtocol.cpp` |
| 136 | `c2s_pkapplyenmity` |  | `KPlayerPK.cpp`, `KProtocolDef.h`, `KPlayerPK.cpp`, `KProtocol.cpp` |
| 137 | `c2s_viewequip` |  | `KProtocol.h`, `KProtocolDef.h`, `KViewItem.cpp`, `KProtocol.cpp` |
| 138 | `c2s_ladderquery` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 139 | `c2s_repairitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 140 | `c2s_npcride` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 141 | `c2s_breakitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 142 | `c2s_playercomp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 143 | `c2s_playersetprice` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 144 | `c2s_playerstarttrade` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 145 | `c2s_viewitem` |  | `KProtocolDef.h`, `KSellItem.cpp`, `KViewItem.cpp`, `KProtocol.cpp` |
| 146 | `c2s_playertradebuyitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 147 | `c2s_updateviewitem` |  | `KProtocolDef.h`, `KSellItem.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 148 | `c2s_playerneedcount` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 149 | `c2s_playershopname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 150 | `c2s_playersysshop` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 151 | `c2s_playerlixian` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 152 | `c2s_playergiveback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 153 | `c2s_pkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 154 | `c2s_autoplay` | 挂机 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 155 | `c2s_npcsunyi` | 瞬移 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 156 | `c2s_guzi` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 157 | `c2s_gufarm` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 158 | `c2s_addjinbi` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 159 | `c2s_lianjie` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 160 | `c2s_fsjingmai` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 161 | `c2s_guaforbit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 162 | `c2s_skillsync` |  | `KPlayer.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp`, `KNpc.cpp` |
| 163 | `c2s_playerrong` | 熔炼 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 164 | `c2s_playeradditem` | 增加物品 没有用到 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 165 | `c2s_playerAutoMoveitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 166 | `c2s_playerdelitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 167 | `c2s_playersetLianFlg` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 168 | `c2s_updateviewequip` | 客户端 | `KProtocolDef.h`, `KViewItem.cpp`, `KProtocolProcess.cpp`, `KViewItem.cpp` |
| 169 | `c2s_playertongset` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 170 | `c2s_playerdoScript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 171 | `c2s_gettaskval` | 获取任务号的值 | `CoreShell.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp` |
| 172 | `c2s_jinducallback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 173 | `c2s_syncurdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 174 | `c2s_vipdoScript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 175 | `c2s_roomisfull` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 176 | `c2s_synnpcinfo` | 同步NPC信息 | `KNpc.cpp`, `KProtocolDef.h`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 177 | `c2s_playerautoequip` |  | `KItemList.cpp`, `KProtocolDef.h`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 178 | `c2s_playerguzgame` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 179 | `c2s_playersetpos` |  | `KProtocol.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp`, `KProtocol.cpp` |
| 180 | `c2s_synshopidx` | KTC | `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 181 | `c2s_settaskval` |  | `KProtocolDef.h`, `ScriptFuns.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 182 | `c2s_runscript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 183 | `c2s_player_req` | 请求再次同步个人信息基本数据 | `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 184 | `c2s_lockitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 185 | `c2s_gmcommand` | 请求再次同步个人信息基本数据 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 186 | `c2s_findpath_state` | 同步寻路状态 | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 187 | `c2s_create_ref_item` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 188 | `c2s_remove_ref_item` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 189 | `c2s_apply_mask_lock` |  | `KItemList.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 190 | `c2s_player_combine_item` |  | `KProtocolDef.h`, `KuiItemdescVN.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 191 | `c2s_playercommand` |  | `KProtocolDef.h`, `KuiItemdescVN.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 192 | `c2s_rolecheckname_result` | goddess查询角色是否存在 | `KProtocolDef.h`, `KProtocol.cpp`, `ScriptFuns.cpp`, `ClientNode.cpp` |
| 193 | `c2s_msginfo` | bishop全区信息 | `KProtocolDef.h`, `ScriptFuns.cpp`, `GameServer.cpp` |
| 194 | `c2s_msginfo_all` | bishop全区信息 | `KProtocolDef.h`, `ScriptFuns.cpp`, `GameServer.cpp` |
| 195 | `c2s_gm_synroleaction` | bishop全区信息 对角色的操作 | `KProtocolDef.h`, `ScriptFuns.cpp`, `KSOServer.cpp`, `GameServer.cpp` |
| 196 | `c2s_gm_synroleaction_result` | bishop全区信息 对角色的操作 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 197 | `c2s_item_synaction` | bishop全区信息 对物品的操作 | `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp`, `KProtocolProcess.cpp` |
| 198 | `c2s_item_synaction_result` |  | `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp`, `KSOServer.cpp` |
| 250 | `_c2s_begin_relay` |  | `KProtocolDef.h`, `KSOServer.cpp` |
| 251 | `c2s_extend` |  | `KPlayer.cpp`, `KPlayerTong.cpp`, `KProtocolDef.h`, `KRelayProtocol.h` |
| 252 | `c2s_extendchat` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KProtocol.cpp`, `KSOServer.cpp` |
| 253 | `c2s_extendfriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KuiFriendListVN.cpp`, `CoreShell.cpp` |
| 254 | `c2s_extendchat_new` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KSOServer.cpp` |
| 255 | `_c2s_end_relay` | c2s_extendfriend, | `KProtocolDef.h`, `KSOServer.cpp` |
| 256 | `c2s_extendtong` |  | `KPlayerTong.cpp`, `KProtocolDef.h`, `KPlayerTong.cpp`, `KProtocol.cpp` |
| 257 | `c2s_end` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KProtocolProcess.cpp`, `KProtocolProcess.h` |

## chat_PROTOCOL (gameserver)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 0 | `chat_micropackbegin` |  | `KProtocolDef.h` |
| 1 | `chat_someonechat` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KgameWorld.cpp`, `KNewProtocolProcess.cpp` |
| 2 | `chat_channelchat` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KgameWorld.cpp`, `KNewProtocolProcess.cpp` |
| 3 | `chat_feedback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ChannelMgr.cpp` |
| 4 | `chat_everyone` |  | `KProtocolDef.h`, `KSOServer.cpp`, `RootClient.cpp` |
| 5 | `chat_groupman` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `CoreServerShell.cpp`, `KSOServer.cpp` |
| 6 | `chat_specman` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ChannelMgr.cpp` |
| 7 | `chat_relegate` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KSOServer.cpp`, `ChannelMgr.cpp` |
| 8 | `chat_filterplayer` |  | `KProtocolDef.h` |
| 9 | `chat_coretask` |  | `KSOServer.cpp`, `Global.cpp` |
| 10 | `chat_caoritemtime` |  | `KSOServer.cpp`, `Global.cpp` |
| 11 | `chat_coreitemdata` |  | `KSOServer.cpp`, `Global.cpp` |
| 12 | `chat_goldthread` |  | `KSOServer.cpp`, `Global.cpp` |

## s2c_PROTOCOL (gateway)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 10 | `s2c_rolehjdkalritopq_getroleinfo_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 11 | `s2c_syncogjfkdnvhf_roleinfo_cipher` |  | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 12 | `s2c_gamestatistic_bigpackage` |  | `KProtocolDef.h`, `ClientNode.cpp` |
| 13 | `s2c_micfghjkdtropackbegin` | 小包开始  31 排名 | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 32 | `s2c_accountbegin` |  | `KProtocolDef.h`, `Cipher.h`, `Cipher.h`, `Cipher.h` |
| 33 | `s2c_accountfdfsglogin` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `Intercessor.cpp`, `S3PDBSocketPool.cpp` |
| 34 | `s2c_gamelogin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 35 | `s2c_accountlogout` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 36 | `s2c_gatewayverify` | 用于连接后第一个包 | `KProtocolDef.h`, `SmartClient.cpp`, `Intercessor.cpp`, `RootClient.cpp` |
| 37 | `s2c_gatewayverifyagain` | 用于重连后第一个包 | `KProtocolDef.h` |
| 38 | `s2c_gatewayinfo` |  | `KProtocolDef.h`, `GatewayClient.cpp`, `HostConnect.cpp`, `RootClient.cpp` |
| 48 | `s2c_multiserverbegin` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 49 | `s2c_querymapinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GamePlayer.cpp` |
| 50 | `s2c_querygameserverinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 51 | `s2c_identitymapping` |  | `KProtocol.h`, `KProtocolDef.h` |
| 52 | `s2c_notifypl_ayerlogin_hfkqotivbhd` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 53 | `s2c_notifyplayerexchange` |  | `KProtocol.h`, `KProtocolDef.h`, `KgameWorld.cpp`, `KSelPlayer.cpp` |
| 54 | `s2c_notifysvrip` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp`, `GatewayClient.cpp` |
| 55 | `s2c_roleserver_getrolelist_result` |  | `KProtocolDef.h`, `Klogin.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 56 | `s2c_roleserver_saverole_result` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 57 | `s2c_roleserver_createrole_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 58 | `s2c_roleserver_deleterole_result` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 59 | `s2c_logiclogout` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp` |
| 60 | `s2c_gateway_broadcast` | 同步播报 | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 61 | `s2c_gamestatistic` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 62 | `s2c_rolecheckname_result` | 检测角色名的 返回结果 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `KSOServer.cpp` |
| 63 | `s2c_gwsyn_broadcast` | 同步播报 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 64 | `s2c_clientbegin` |  | `CoreShell.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 65 | `s2c_login` | ref: ../../S3Client/Login/LoginDef.h | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `LoginDef.h` |
| 66 | `s2c_logout` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 67 | `s2c_syncclientend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 68 | `s2c_synonlineplayer` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 69 | `s2c_synccurplayerskill` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 70 | `s2c_synccurplayernormal` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 71 | `s2c_newplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 72 | `s2c_removeplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 73 | `s2c_syncworld` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 74 | `s2c_syncplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 75 | `s2c_syncplayermin` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 76 | `s2c_syncnpc` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 77 | `s2c_syncnpcmin` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 78 | `s2c_syncnpcminplayer` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 79 | `s2c_objadd` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 80 | `s2c_syncobjstate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 81 | `s2c_syncobjdir` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 82 | `s2c_objremove` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 83 | `s2c_objTrapAct` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp` |
| 84 | `s2c_npcremove` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 85 | `s2c_npcwalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 86 | `s2c_npcrun` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 87 | `s2c_npcattack` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 88 | `s2c_npcmagic` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 89 | `s2c_npcjump` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 90 | `s2c_npctalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 91 | `s2c_npchurt` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 92 | `s2c_npcdeath` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 93 | `s2c_npcchgcurcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 94 | `s2c_npcchgcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 95 | `s2c_npcsettmpcamp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 96 | `s2c_skillcast` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 97 | `s2c_playertalk` |  | `KNpc.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 98 | `s2c_playerexp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 99 | `s2c_teaminfo` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 100 | `s2c_teamselfinfo` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 101 | `s2c_teamapplyinfofalse` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 102 | `s2c_teamcreatesuccess` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 103 | `s2c_teamcreatefalse` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 104 | `s2c_teamopenclose` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 105 | `s2c_teamgetapply` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 106 | `s2c_teamaddmember` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 107 | `s2c_teamleave` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 108 | `s2c_teamchangecaptain` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 109 | `s2c_playerfactiondata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 110 | `s2c_playerleavefaction` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 111 | `s2c_playerfactionskilllevel` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 112 | `s2c_playersendchat` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 113 | `s2c_playersyncleadexp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 114 | `s2c_playerlevelup` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 115 | `s2c_teammatelevel` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 116 | `s2c_playersyncattribute` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 117 | `s2c_playerskilllevel` |  | `KNpcAttribModify.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 118 | `s2c_syncitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 119 | `s2c_removeitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 120 | `s2c_syncmonfs` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 121 | `s2c_syncqianfs` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 122 | `s2c_playermoveitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 123 | `s2c_scriptaction` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp`, `KPlayer - Copy - Copy.cpp` |
| 124 | `s2c_chatapplyaddfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 125 | `s2c_chataddfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 126 | `s2c_chatrefusefriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 127 | `s2c_chataddfriendfail` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 128 | `s2c_chatloginfriendnoname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 129 | `s2c_chatloginfriendname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 130 | `s2c_chatonefrienddata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 131 | `s2c_chatfriendonline` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 132 | `s2c_chatdeletefriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 133 | `s2c_chatfriendoffline` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 134 | `s2c_syncrolelist` | 没有给调用 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 135 | `s2c_tradechangestate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerMenuState.cpp` |
| 136 | `s2c_npcsetmenustate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerMenuState.cpp` |
| 137 | `s2c_trademoneysync` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 138 | `s2c_tradedecision` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 139 | `s2c_chatscreensingleerror` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerChat.cpp` |
| 140 | `s2c_syncnpcstate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 141 | `s2c_teaminviteadd` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTeam.cpp` |
| 142 | `s2c_tradepressoksync` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 143 | `s2c_ping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 144 | `s2c_npcsit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 145 | `s2c_npcstand` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 146 | `s2c_opensalebox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 147 | `s2c_castskilldirectly` | 有BUG | `KNpc.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 148 | `s2c_msgshow` |  | `KNpc.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 149 | `s2c_syncstateeffect` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 150 | `s2c_openstorebox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 151 | `s2c_openresetpass` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 152 | `s2c_openstringbox` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 153 | `s2c_opendataubox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 154 | `s2c_playerrevive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 155 | `s2c_requestnpcfail` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpcSet.cpp` |
| 156 | `s2c_tradeapplystart` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 157 | `s2c_rolenewdelresponse` | 新建与删除角色的结果返回,所带数据为结构tagNewDelRoleResponse | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `Klogin.cpp` |
| 158 | `s2c_ItemAutoMove` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 159 | `s2c_itemexchangefinish` |  | `KItemList.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 160 | `s2c_changeweather` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 161 | `s2c_pksyncnormalflag` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 162 | `s2c_pksyncenmitystate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 163 | `s2c_pksyncexercisestate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 164 | `s2c_pksyncpkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerPK.cpp` |
| 165 | `s2c_reputesyncreputevalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerRepute.cpp` |
| 166 | `s2c_fuyuansyncfuyuanvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerFuYuan.cpp` |
| 167 | `s2c_rebornsyncrebornvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerReBorn.cpp` |
| 168 | `s2c_openmarketbox` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp` |
| 169 | `s2c_npcsleepmode` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 170 | `s2c_viewequip` |  | `KProtocol.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 171 | `s2c_ladderresult` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 172 | `s2c_ladderlist` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 173 | `s2c_tongcreate` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTong.cpp` |
| 174 | `s2c_replyclientping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 175 | `s2c_npcgoldchange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpcGold.cpp` |
| 176 | `s2c_itemdurabilitychange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 177 | `s2c_opentremble` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 178 | `s2c_rankname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp` |
| 179 | `s2c_viewsellitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 180 | `s2c_viewupdateitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 181 | `s2c_playergetcount` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 182 | `s2c_shopname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 183 | `s2c_syncmasklock` | mat na | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 184 | `s2c_opengive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 185 | `s2c_npcsecmove` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 186 | `s2c_pkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 187 | `s2c_viewlianitem` | 链接 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp` |
| 188 | `s2c_openwengang` | 纹钢 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 189 | `s2c_openstone` | 宝石镶嵌 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 190 | `s2c_updateviewequip` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 191 | `s2c_gettongback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 192 | `s2c_syncequipitem` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 193 | `s2c_taskcallback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTask.cpp` |
| 194 | `s2c_openjindutiao` | 打开进度条 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 195 | `s2c_syncitemposition` | 同步位置(没用) | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp` |
| 196 | `s2c_openduanzhao` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 197 | `s2c_syncurupdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 198 | `s2c_JinMaicallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 199 | `s2c_openvipdazao` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 200 | `s2c_synnpcinfocallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 201 | `s2c_pautoMovecallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 202 | `s2c_plyerguzicallback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 203 | `s2c_syncplayermap` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 204 | `s2c_synconestate` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 205 | `s2c_syncnodataeffect` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 206 | `s2c_npcsetpos` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 207 | `s2c_playermissiondata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 208 | `s2c_syncrankdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp` |
| 209 | `s2c_syncsupershop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp`, `KProtocolProcess.cpp` |
| 210 | `s2c_syncitem_shop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KBuySell.cpp`, `KProtocolProcess.cpp` |
| 211 | `s2c_itemdata_shop` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp`, `KProtocolProcess.cpp` |
| 212 | `s2c_kickoutgame` | 通知客户端退出游戏 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 213 | `s2c_objadd_vn` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KObj.cpp`, `KProtocol.cpp` |
| 214 | `s2c_rolesyncvipvalue` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerVip.cpp`, `KProtocolProcess.cpp` |
| 215 | `s2c_gm_synroleaction` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `ClientNode.cpp` |
| 216 | `s2c_queryiteminfo` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KSOServer.cpp`, `GameServer.cpp` |
| 217 | `s2c_returnitemlock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 218 | `s2c_findpath_state` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 219 | `s2c_refitemsync` | 219 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KItemList.cpp` |
| 220 | `s2c_chestpwsync` | 220 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 250 | `s2c_extend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KRelayProtocol.h` |
| 251 | `s2c_extendchat` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `CoreServerShell.cpp` |
| 252 | `s2c_extendfriend` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 253 | `s2c_extendchat_new` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp` |
| 254 | `s2c_extendtong` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KPlayerTong.cpp` |
| 255 | `s2c_end` |  | `CoreShell.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.h` |

## c2s_PROTOCOL (gateway)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 10 | `c2s_rolekfjhu_saveroleinfo` |  | `KProtocolDef.h`, `KPlayerDBFuns.cpp`, `KSOServer.cpp`, `ClientNode.cpp` |
| 11 | `c2s_roleserver_createroleinfo` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp` |
| 12 | `c2s_gmsvr2gateway_saverole` |  | `KProtocol.h`, `KProtocolDef.h` |
| 13 | `c2s_micropackbegin` |  | `KProtocolDef.h` |
| 32 | `c2s_accountbegin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 33 | `c2s_accountlogin` | 账号登陆 | `KProtocolDef.h`, `GamePlayer.cpp`, `GamePlayer.cpp`, `S3PDBSocketPool.cpp` |
| 34 | `c2s_gamelogin_dkiqopjgurnmvbgc` | 开始登陆游戏 是否能成功！或提示服务器人满 | `KProtocolDef.h`, `GameServer.cpp`, `S3PDBSocketPool.cpp`, `S3PDBSocketPool.cpp` |
| 35 | `c2s_accountlogout` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `GameServer.cpp`, `S3PDBSocketPool.cpp` |
| 36 | `c2s_gatewayverify` |  | `KProtocolDef.h`, `SmartClient.cpp`, `Intercessor.cpp`, `RootClient.cpp` |
| 37 | `c2s_gatewayverifyagain` |  | `KProtocolDef.h`, `SmartClient.cpp`, `S3PDBSocketPool.cpp` |
| 38 | `c2s_gatewayinfo` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 48 | `c2s_multiserverbegin` |  | `KProtocolDef.h`, `S3PDBSocketPool.cpp` |
| 49 | `c2s_permit_logftihmcginqknd` |  | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 50 | `c2s_updatemapinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 51 | `c2s_updategameserverinfo` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 52 | `c2s__entergamegkjyiruqine` | GS 通知开始进入游戏 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp`, `ChatConnect.cpp` |
| 53 | `c2s_leavegame` |  | `KProtocol.h`, `KProtocolDef.h`, `CoreServerShell.cpp`, `KPlayerSet.cpp` |
| 54 | `c2s_registeraccount` |  | `KProtocol.h`, `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 55 | `c2s_requestsvrip` |  | `KProtocol.h`, `KProtocolDef.h`, `GameServer.cpp`, `GatewayClient.cpp` |
| 56 | `c2s_roleserver_getrolelist` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp`, `GamePlayer.cpp` |
| 57 | `c2s_roleserver_getroleinfo` |  | `KProtocolDef.h`, `GamePlayer.cpp`, `ClientNode.cpp`, `GamePlayer.cpp` |
| 58 | `c2s_roleserver_deleteplayer` |  | `KProtocolDef.h`, `KuiSelPlayer_new.cpp`, `GamePlayer.cpp`, `Intercessor.cpp` |
| 59 | `c2s_gamestatistic` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ClientNode.cpp` |
| 60 | `c2s_roleserver_lock` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KPlayerSet.cpp`, `ScriptFuns.cpp` |
| 64 | `c2s_gameserverbegin` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 65 | `c2s_login_fhgyrinhkmvnsheypo` |  | `KProtocolDef.h`, `Klogin.cpp`, `KuiWarnInfo.cpp`, `KloginVN.cpp` |
| 66 | `c2s__loginfs_kfjghtueodnchsf` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KSelPlayer.cpp`, `KuiNewPlayer.cpp` |
| 67 | `c2s_syncclientend` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `KSOServer.cpp` |
| 68 | `c2s_loadplayer` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 69 | `c2s_newplayer` |  | `KProtocol.h`, `KProtocolDef.h`, `KuiNewPlayer.cpp`, `KProtocol.cpp` |
| 70 | `c2s_removeplayer` |  | `KProtocolDef.h`, `KuiAutoPlay.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 71 | `c2s_requestworld` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 72 | `c2s_requestplayer` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 73 | `c2s_requestnpc` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 74 | `c2s_requestobj` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 75 | `c2s_npcwalk` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 76 | `c2s_npcrun` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 77 | `c2s_npcskill` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 78 | `c2s_npcjump` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 79 | `c2s_npctalk` |  | `KProtocolDef.h`, `KuiItemdescVN.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 80 | `c2s_npchurt` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 81 | `c2s_npcdeath` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 82 | `c2s_playertalk` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 83 | `c2s_teamapplyinfo` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 84 | `c2s_teamapplycreate` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 85 | `c2s_teamapplyopenclose` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 86 | `c2s_teamapplyadd` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 87 | `c2s_teamacceptmember` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 88 | `c2s_teamapplyleave` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 89 | `c2s_teamapplykickmember` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 90 | `c2s_teamapplychangecaptain` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 91 | `c2s_teamapplydismiss` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 92 | `c2s_playerapplysetpk` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 93 | `c2s_playerapplyfactiondata` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 94 | `c2s_playersendchat` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 95 | `c2s_playeraddbaseattribute` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 96 | `c2s_playerapplyaddskillpoint` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 97 | `c2s_playereatitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 98 | `c2s_playerpickupitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 99 | `c2s_playermoveitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 100 | `c2s_playersellitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 101 | `c2s_playerbuyitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 102 | `c2s_playerthrowawayitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 103 | `c2s_playerselui` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 104 | `c2s_chatsetchannel` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 105 | `c2s_chatapplyaddfriend` |  | `KProtocolDef.h`, `KuiPlayerSelFunVN.cpp`, `KPlayerChat.cpp`, `KProtocol.cpp` |
| 106 | `c2s_chataddfriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 107 | `c2s_chatrefusefriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 108 | `c2s_dbplayerselect` |  | `KProtocolDef.h`, `KSelPlayer.cpp`, `KuiSelPlayer_new.cpp`, `KuiWarnInfo.cpp` |
| 109 | `c2s_chatapplyresendallfriendname` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 110 | `c2s_chatapplysendonefriendname` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 111 | `c2s_chatdeletefriend` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 112 | `c2s_chatredeletefriend` |  | `KProtocolDef.h`, `KPlayerChat.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 113 | `c2s_tradeapplystateopen` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 114 | `c2s_tradeapplystateclose` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 115 | `c2s_tradeapplystart` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 116 | `c2s_trademovemoney` |  | `KPlayer.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp` |
| 117 | `c2s_tradedecision` |  | `KPlayer.cpp`, `KProtocol.h`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp` |
| 118 | `c2s_dialognpc` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 119 | `c2s_teaminviteadd` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 120 | `c2s_changeauraskill` |  | `KNpc.cpp`, `KProtocolDef.h`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 121 | `c2s_teamreplyinvite` |  | `KPlayerTeam.cpp`, `KProtocolDef.h`, `KPlayerTeam.cpp`, `KProtocol.cpp` |
| 122 | `c2s_ping` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 123 | `c2s_cpunlock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 124 | `c2s_cplock` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocol.cpp` |
| 125 | `c2s_cpchange` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 126 | `c2s_cpreset` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 127 | `c2s_market` | KTC | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 128 | `c2s_string` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 129 | `c2s_datau` |  | `KProtocol.cpp`, `KProtocolDef.h`, `Kuilaotou.cpp`, `KProtocol.cpp` |
| 130 | `c2s_npcsit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 131 | `c2s_objmouseclick` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 132 | `c2s_storemoney` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 133 | `c2s_playerrevive` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 134 | `c2s_tradereplystart` |  | `KPlayerTrade.cpp`, `KProtocolDef.h`, `KPlayerTrade.cpp`, `KProtocol.cpp` |
| 135 | `c2s_pkapplychangenormalflag` |  | `KPlayerPK.cpp`, `KProtocolDef.h`, `KPlayerPK.cpp`, `KProtocol.cpp` |
| 136 | `c2s_pkapplyenmity` |  | `KPlayerPK.cpp`, `KProtocolDef.h`, `KPlayerPK.cpp`, `KProtocol.cpp` |
| 137 | `c2s_viewequip` |  | `KProtocol.h`, `KProtocolDef.h`, `KViewItem.cpp`, `KProtocol.cpp` |
| 138 | `c2s_ladderquery` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 139 | `c2s_repairitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 140 | `c2s_npcride` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 141 | `c2s_breakitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 142 | `c2s_playercomp` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 143 | `c2s_playersetprice` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 144 | `c2s_playerstarttrade` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 145 | `c2s_viewitem` |  | `KProtocolDef.h`, `KSellItem.cpp`, `KViewItem.cpp`, `KProtocol.cpp` |
| 146 | `c2s_playertradebuyitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 147 | `c2s_updateviewitem` |  | `KProtocolDef.h`, `KSellItem.cpp`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 148 | `c2s_playerneedcount` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 149 | `c2s_playershopname` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 150 | `c2s_playersysshop` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 151 | `c2s_playerlixian` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 152 | `c2s_playergiveback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 153 | `c2s_pkvalue` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 154 | `c2s_autoplay` | 挂机 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 155 | `c2s_npcsunyi` | 瞬移 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 156 | `c2s_guzi` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 157 | `c2s_gufarm` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 158 | `c2s_addjinbi` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 159 | `c2s_lianjie` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 160 | `c2s_fsjingmai` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 161 | `c2s_guaforbit` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 162 | `c2s_skillsync` |  | `KPlayer.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp`, `KNpc.cpp` |
| 163 | `c2s_playerrong` | 熔炼 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 164 | `c2s_playeradditem` | 增加物品 没有用到 | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 165 | `c2s_playerAutoMoveitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 166 | `c2s_playerdelitem` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 167 | `c2s_playersetLianFlg` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 168 | `c2s_updateviewequip` | 客户端 | `KProtocolDef.h`, `KViewItem.cpp`, `KProtocolProcess.cpp`, `KViewItem.cpp` |
| 169 | `c2s_playertongset` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 170 | `c2s_playerdoScript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 171 | `c2s_gettaskval` | 获取任务号的值 | `CoreShell.cpp`, `KProtocol.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp` |
| 172 | `c2s_jinducallback` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 173 | `c2s_syncurdata` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 174 | `c2s_vipdoScript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 175 | `c2s_roomisfull` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp` |
| 176 | `c2s_synnpcinfo` | 同步NPC信息 | `KNpc.cpp`, `KProtocolDef.h`, `KNpc.cpp`, `KNpc_backup.cpp` |
| 177 | `c2s_playerautoequip` |  | `KItemList.cpp`, `KProtocolDef.h`, `KItemList.cpp`, `KProtocolProcess.cpp` |
| 178 | `c2s_playerguzgame` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 179 | `c2s_playersetpos` |  | `KProtocol.cpp`, `KProtocolDef.h`, `ScriptFuns.cpp`, `KProtocol.cpp` |
| 180 | `c2s_synshopidx` | KTC | `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 181 | `c2s_settaskval` |  | `KProtocolDef.h`, `ScriptFuns.cpp`, `KProtocolProcess.cpp`, `ScriptFuns.cpp` |
| 182 | `c2s_runscript` |  | `KProtocol.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 183 | `c2s_player_req` | 请求再次同步个人信息基本数据 | `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 184 | `c2s_lockitem` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 185 | `c2s_findpath_state` | 同步寻路状态 | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocolProcess.cpp` |
| 186 | `c2s_create_ref_item` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 187 | `c2s_remove_ref_item` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KProtocol.cpp`, `KProtocolProcess.cpp` |
| 188 | `c2s_rolecheckname_result` | goddess查询角色是否存在 | `KProtocolDef.h`, `KProtocol.cpp`, `ScriptFuns.cpp`, `ClientNode.cpp` |
| 189 | `c2s_msginfo` | bishop全区信息 | `KProtocolDef.h`, `ScriptFuns.cpp`, `GameServer.cpp` |
| 190 | `c2s_msginfo_all` | bishop全区信息 | `KProtocolDef.h`, `ScriptFuns.cpp`, `GameServer.cpp` |
| 191 | `c2s_gm_synroleaction` | bishop全区信息 对角色的操作 | `KProtocolDef.h`, `ScriptFuns.cpp`, `KSOServer.cpp`, `GameServer.cpp` |
| 192 | `c2s_gm_synroleaction_result` | bishop全区信息 对角色的操作 | `KProtocolDef.h`, `KSOServer.cpp`, `GameServer.cpp` |
| 193 | `c2s_item_synaction` | bishop全区信息 对物品的操作 | `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp`, `KProtocolProcess.cpp` |
| 194 | `c2s_item_synaction_result` |  | `KProtocolDef.h`, `KPlayer - Copy - Copy.cpp`, `KPlayer.cpp`, `KSOServer.cpp` |
| 250 | `_c2s_begin_relay` |  | `KProtocolDef.h`, `KSOServer.cpp` |
| 251 | `c2s_extend` |  | `KPlayer.cpp`, `KPlayerTong.cpp`, `KProtocolDef.h`, `KRelayProtocol.h` |
| 252 | `c2s_extendchat` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KProtocol.cpp`, `KSOServer.cpp` |
| 253 | `c2s_extendfriend` |  | `KPlayer.cpp`, `KProtocolDef.h`, `KuiFriendListVN.cpp`, `CoreShell.cpp` |
| 254 | `c2s_extendchat_new` |  | `KProtocolDef.h`, `KProtocol.cpp`, `KSOServer.cpp` |
| 255 | `_c2s_end_relay` | c2s_extendfriend, | `KProtocolDef.h`, `KSOServer.cpp` |
| 256 | `c2s_extendtong` |  | `KPlayerTong.cpp`, `KProtocolDef.h`, `KPlayerTong.cpp`, `KProtocol.cpp` |
| 257 | `c2s_end` |  | `KProtocolDef.h`, `CoreServerShell.cpp`, `KProtocolProcess.cpp`, `KProtocolProcess.h` |

## chat_PROTOCOL (gateway)

| Mã | Tên | Chú thích | Tệp dùng |
|---|---|---|---|
| 0 | `chat_micropackbegin` |  | `KProtocolDef.h` |
| 1 | `chat_someonechat` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KgameWorld.cpp`, `KNewProtocolProcess.cpp` |
| 2 | `chat_channelchat` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KgameWorld.cpp`, `KNewProtocolProcess.cpp` |
| 3 | `chat_feedback` |  | `KProtocolDef.h`, `KProtocolProcess.cpp`, `KProtocolProcess.cpp`, `ChannelMgr.cpp` |
| 4 | `chat_everyone` |  | `KProtocolDef.h`, `KSOServer.cpp`, `RootClient.cpp` |
| 5 | `chat_groupman` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `CoreServerShell.cpp`, `KSOServer.cpp` |
| 6 | `chat_specman` |  | `KProtocolDef.h`, `KSOServer.cpp`, `ChannelMgr.cpp` |
| 7 | `chat_relegate` |  | `KProtocolDef.h`, `KgameWorld.cpp`, `KSOServer.cpp`, `ChannelMgr.cpp` |
| 8 | `chat_filterplayer` |  | `KProtocolDef.h` |
| 9 | `chat_coretask` |  | `KSOServer.cpp`, `Global.cpp` |
| 10 | `chat_caoritemtime` |  | `KSOServer.cpp`, `Global.cpp` |
| 11 | `chat_coreitemdata` |  | `KSOServer.cpp`, `Global.cpp` |
| 12 | `chat_goldthread` |  | `KSOServer.cpp`, `Global.cpp` |

