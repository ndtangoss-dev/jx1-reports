# Asset Reference Coverage

- Status: **VERIFIED for the static literal scan described below; overall pack-internal coverage UNKNOWN.**
- Scope: C/C++/header text under the client Classes tree. Extracted quoted literals ending in common image, texture, atlas, font, audio, map, shader, or pack extensions. Sensitive-looking lines are skipped; source lines are never copied into this report.
- Code files scanned: 709
- Unique static resource-like references: 1069
- Exact/unique basename matches in loose Resources/data/Android assets: 254
- Not directly matched: 815; classified unresolved, not missing, because files may be packed, generated, built dynamically, or referenced by aliases.
- Source evidence: client CMakeLists.txt lines 47-54 declares Resources; custom loaders are in Classes/engine/KPakFile.cpp, KPakList.cpp, XPackFile.cpp, KDownLoadFile.cpp. Package indexes present at Resources/package.ini, Resources/paklist.ini, data/data/package.ini, data/data/paklist.ini and data_cdn/data/paklist.ini. Index contents were not emitted.
- Archive boundary: 40 data_cdn/data PAK files and other archives were not extracted or enumerated internally.

| Reference literal | Status | Loose match | Source file count |
|---|---|---|---:|
| , SPR_PATH_JINENG); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| , SPR_PATH_SYSTEM); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| , SPR_PATH_TASK); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| , SPR_PATH_TEAM); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| , SPR_PATH_TONG); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| , SPR_PATH_ZIMUDAI); \\\\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\maps\\��Ϸ��Դ\\background\\����ͼ.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\sound\\skill\\�������.wav | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\gm\\gm01.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\gm\\gmvn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\item\\cucsat.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\item\\cucsat36.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\item\\equip\\brokenequip.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\npcres\\passerby\\passerby239\\passerby239.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\npcres\\targetdo.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\npcres\\targetxanh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\obj\\box\\YellowPoint.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\others\\问号.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\others\\�ʺ�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 35 |
| \\spr\\Quest\\%d.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Quest\\ExpBtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Quest\\Main.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Quest\\Money.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Quest\\Random.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ÃÅÅÉ½ø½×\\»ð.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ÃÅÅÉ½ø½×\\½ð.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ÃÅÅÉ½ø½×\\Ä¾.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ÃÅÅÉ½ø½×\\Ë®.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ÃÅÅÉ½ø½×\\ÍÁ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\NPC\\mag_npc_��ˮ��ʧ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\others\\huangdi.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\skill\\others\\totempole_mask.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\others\\totempole_phoenix.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\skill\\others\\助攻王.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\skill\\others\\重击.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\special\\skill_heart.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\skill\\task\\randomtask.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\skill\\zhongqiu\\zq_sl_003.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\ͼ��\\ͨ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\补充\\mag_spe_眩晕.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\门派进阶\\土.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\门派进阶\\木.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\门派进阶\\水.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\门派进阶\\火.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\门派进阶\\金.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\���ɽ���\\ľ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\���ɽ���\\ˮ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\skill\\���ɽ���\\��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui\\¼¼ÄÜÍ¼±ê\\icon_sk_ty_ap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui\\技能图标\\icon_sk_ty_ap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui\\����ͼ��\\icon_sk_ty_ap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui\\����ͼ��\\ǹ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\–°µÿÕº\\–°µÿÕº£≠∂¥øﬂ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\???????\\????-?????-???????\\???????_6_???.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\״̬��װ��\\״̬�ӵ㰴ť��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\UI3\\״̬��װ��\\װ��ҳ��(��).spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\UI3\\״̬��װ��\\��ɫ��Ϣ��ͼ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\UI3\\״̬��װ��\\��ҳ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\UI3\\״̬��װ��\\����ҳ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\°ÚÌ¯\\°ÚÌ¯Í·¶¥Ìõ£­×ó.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\°ÚÌ¯\\°ÚÌ¯Í·¶¥Ìõ£­ÖÐ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\°ÚÌ¯\\°ÚÌ¯Í·¶¥Ìõ£­ÓÒ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\÷˜ΩÁ√Ê\\newui\\œµÕ≥∞¥≈•.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\½£ÏÀÖúÊÖ\\open.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\activityguide\\activityguideui.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 5 |
| \\spr\\Ui3\\activityguide\\activityguideui1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\activityguide\\activityguideui2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\activityguide\\calendarpage.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\activityguide\\closebutton.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\activityguide\\closebutton.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\activityguide\\gameicon.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\activityguide\\guidebutton.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\activityguide\\pagebutton.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\activityguide\\progressbar.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\activityguide\\progressbarback.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\arena\\ico.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\btn\\btn_check_vn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\btn\\close_btn.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\btn\\okay_btn.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\ǩ��\\��Ʒ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\loginui\\longi_6_b.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\loginui\\longin_9_big_b.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\Ui3\\loginui\\okbtn\\loginui_6_cancel.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\loginui\\okbtn\\loginui_6_ok.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\loginui\\saverole\\cancel_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 5 |
| \\spr\\Ui3\\loginui\\saverole\\delrole_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\loginui\\saverole\\newrole_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\loginui\\saverole\\ok_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\loginui\\startbtn\\log_2_rep.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\loginui\\uidonghua\\yezi.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\logo_vn.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\UI3\\Npc\\ActionIcon_RideHorse.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\UI3\\Npc\\ActionIcon_Sit.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\Npc\\series0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\Npc\\series1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\Npc\\series2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\Npc\\series3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\Npc\\series4.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\ui3\\npc�Ի���\\npc����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\NPC�Ի���\\�Ի���2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\spr\\UI3\\Ö÷½çÃæ\\¶ÓÎé°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\´ò×ø°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\°´Å¥Ìõ°´Å¥\\´ò×ø.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\°´Å¥Ìõ°´Å¥\\½»Ò×.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\°´Å¥Ìõ°´Å¥\\ÆïÂí.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\°´Å¥Ìõ°´Å¥\\ÅÜ²½.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\°´Å¥Ìõ°´Å¥\\pk.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\°ï»á°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\±³°ü°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\×ÓÄ¸´ü°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\½»Ò×°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\¼¼ÄÜ°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÁÄÌìÊÒ°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÆïÂí°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÅÜ²½°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÈËÎïÊôÐÔ°´Å¥_0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÈÎÎñ°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\ÏµÍ³°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\¶ÓÎé.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\°ïÅÉ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\°ü¹ü.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\×ÓÄ¸´ü.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\¼¼ÄÜ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\ÈËÎï.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\ÈÎÎñ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\ÝÄÌìÊÒ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\Ö÷½çÃæ\\newui\\ÝµÝ³°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\Ö÷½çÃæ\\PK°´Å¥.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\progressbar\\progressbar_back.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\progressbar\\progressbar_bit.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\ͬ�鱳��\\ͬ�鱳������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\uidynamicshop\\cell.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\uidynamicshop\\main1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\uidynamicshop\\menu.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\UiGetStrings\\huybo.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiGetStrings\\huybotype2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiGetStrings\\tienvan.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiGetStrings\\tienxu.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiGetStrings\\UiGetStrings.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\UiGetStrings\\UiGetStringsType2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiGetStrings\\xacnhan.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiMinMap\\UiMinMap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\UiPlayerFun\\playerfun.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\UiPlayerShop\\UiPlayerShop.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\uiselserver\\selserverbox.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\uitasktrace\\tasktrace.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\worldmap.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\worldmap.png | 1 |
| \\spr\\Ui3\\ϵͳ\\ϵͳ2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\ϵͳ\\ϵͳ��ѡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\ϵͳ\\ϵͳ���˳�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\ϵͳ\\ϵͳ������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\ϵͳ\\ϵͳ�������й�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\С???\\С??????л????0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\С��ͼ\\arrow.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\С��ͼ\\��ͼС����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\С��ͼ\\�����ɽ��ͼ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\主界面\\mainbackground.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\人物.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\任务.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\包裹.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\newui\\奇珍阁按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\子母袋.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\帮派.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\技能.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\拍卖行按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\系统按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\聊天室.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\newui\\队伍.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\PK按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-世界频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-城市频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-聊天发送.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-门派频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-队伍频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\主界面按钮-附近频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\交易按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\人物属性按钮_0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\任务按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\主界面\\图标\\zenglibtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\主界面\\图标\\快捷栏.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\子母袋按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\帮会按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\帮会聊天频道选择.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\打坐按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\技能按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\按钮条按钮\\pk.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\按钮条按钮\\交易.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\按钮条按钮\\打坐.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\按钮条按钮\\跑步.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\按钮条按钮\\骑马.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\生命条.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\系统按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\聊天室按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\UI3\\主界面\\聊天输入条.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\主界面\\聊天频道图示－gm频道.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\主界面\\聊天频道选择按键.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\背包按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\跑步按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\队伍按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\主界面\\骑马按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\买卖\\商店界面\\分页按钮.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\买卖\\新奇珍阁界面\\通用的二字标签.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\剑侠助手\\open.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\剑侠助手\\state_autofight.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\小地图\\地图小旗帜.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\小地图\\小地图－洞窟.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\摆摊\\摆摊头顶条－中.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\摆摊\\摆摊头顶条－右.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\摆摊\\摆摊头顶条－左.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\特殊对话条\\输入文字条－取消.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\特殊对话条\\输入文字条－确定.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\特殊对话条\\输入文字条2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\玩家交互\\玩家交互2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\登入界面\\新建角色按钮\\登陆界面_7_取消.spr\\spr\\Ui3\\loginui\\saverole\\cancel_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\登入界面\\新建角色按钮\\登陆界面_7_土.spr\\spr\\Ui3\\loginui\\saverole\\cancel_9_btn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\登入界面\\新建角色按钮\\登陆界面_7_选择人物.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\登入界面\\界面小动画\\叶子飘过.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\登入界面\\选存档角色按钮\\登陆界面_9_取消.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\登入界面\\选存档角色按钮\\登陆界面_9_确定.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\组队\\关闭.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\组队\\刷新列表.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\组队\\离开队伍.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\组队\\组队2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\组队\\组队开关.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\组队\\踢出队伍.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\组队\\邀请加入.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\组队\\队长移交.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\表情\\01.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\道具\\道具－关闭.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\道具\\道具－存钱.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\道具\\道具面板3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\��̯\\��̯ͷ��������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\���\\��ӿ���.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\���Ӵ�����\\һ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\���Ӵ�����\\�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\���Ӵ�����\\��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\���Ӵ�����\\����������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\����\\%s.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\����\\��̯\\�й�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����\\��̯\\��̯.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\��̯\\���.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\��̯\\���ù��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\��ҽ��ף�ȡ������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����\\��ҽ��ף�����ȷ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����\\��ҽ��ף���������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����\\��ҽ���.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����\\���ɴ���-ȡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\���ɴ���-ȷ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\���ɴ���-а��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\���ɴ���-����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\���Ӱ���2-�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����\\���Ӱ���2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\���ߣ��ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 5 |
| \\spr\\Ui3\\����\\���ߣ���Ǯ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\�̵����\\�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\�̵����\\��ҳ��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\�̵����\\����ʯ�̵�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\�̵����\\�̵����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����\\������壭��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\����\\�������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\�������3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\����\\���������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\����\\����������\\ͨ�õĶ��ֱ�ǩ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\����\\����������\\����󱳾�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\����������\\�����б���.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\����\\����������\\�����رհ���.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����Ի���\\ȡǮ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����Ի���\\����������2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\����Ի���\\������������ȡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\����Ի���\\������������ȷ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\spr\\Ui3\\����װ��\\ͼ�׷�ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����װ��\\�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����װ��\\��ȡ��ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����װ��\\��Ƕ��ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ͼ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ҳ�ϳ�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ҳ��ȡ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ҳ��Ƕ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\����װ��\\��ҳ����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����װ��\\�����ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\����װ��\\������ҳͼ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\������\\newui\\ݵݳ��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\������\\newui\\��ĸ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\NewUI\\��ͼ��С.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\ui3\\������\\newui\\����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\������\\newui\\������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\PK��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\ϵͳ��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\ȡ_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\������\\ͼ��\\ȡ��_��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\ȡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\ȷ��_��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\zenglibtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 5 |
| \\spr\\Ui3\\������\\ͼ��\\�ʺ�ע��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\��_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\������\\ͼ��\\��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\spr\\Ui3\\������\\ͼ��\\����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ͼ��\\�����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\ж��װ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\��Ա��ļ��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\����ʹ�ð�ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\�����Ϣ��ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\���ܷ��䰴ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\���������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��ļҳ\\���������ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\��ĸ����ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\������\\��ť����ť\\pk.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\������\\��ť����ť\\�ܲ�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\������\\��ť����ť\\����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\��Ѫ�����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\��չ������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\������\\��ᰴť-�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\��ᰴť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\���װ�ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\���鰴ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\����\\����ָ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\����ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\���ܰ�ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\�ܲ���ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\����װ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\�����Ϣҳ\\����ҳ-�����Ϣ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\������\\�����Ϣ�޸ĵ�ͼ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\�����Ұ�ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\�����䣭ȡǮ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\������\\�����䣭�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\������\\������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\UI3\\������\\������ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\UI3\\������\\�������԰�ť_0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui3\\������\\���������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\spr\\Ui3\\������ϵͳ\\������\\�������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\ѡ�浵��ɫ��ť\\��½����_8_ȡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\�������\\ѡ�浵��ɫ��ť\\��½����_9_ȡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\Spr\\Ui3\\�������\\ѡ�浵��ɫ��ť\\��½����_9_ȷ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\�������\\ѡ�浵��ɫ��ť\\��½����_9_ɾ����ɫ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\�������\\ѡ�浵��ɫ��ť\\��½����_9_�½���ɫ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\�������\\��½��ʾ\\ʹ����Լ����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\��½����_6_�߿�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\��½����_8_ѡ�����ִ�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\��½����_9_���߿�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\Spr\\Ui3\\�������\\���뿪ʼ��Ϸ��ť\\��½����_2_ϵͳѡ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\���뿪ʼ��Ϸ��ť\\��½����_2_�˳���Ϸ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\���뿪ʼ��Ϸ��ť\\��½����_2_�߿�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\ui3\\�������\\���뿪ʼ��Ϸ��ť\\��½����_2_��ʼ��Ϸ.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui3\\�������\\����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\Spr\\Ui3\\�������\\����С����\\Ҷ��Ʈ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 8 |
| \\spr\\Ui4\\common\\�ӵ㰴ť.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\common\\�ر�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\common\\��ť����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\Ö÷½çÃæ\\ÈÎÎñÖ¸ÄÏ×ÊÔ´\\opentracebtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\Ö÷½çÃæ\\levelupaward\\nextlevelawardbtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\主界面\\levelupaward\\nextlevelawardbtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\主界面\\任务指南资源\\opentracebtn.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\主界面\\任务指南资源\\任务追踪底板.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\��Ʒ����\\����ҳ��.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\���Ԥ��\\background.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\���Ԥ��\\blood.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\���Ԥ��\\mana.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\���Ԥ��\\��1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\����\\���ǵװ�.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\Spr\\Ui4\\������\\����ϵͳ\\������.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\spr\\Ui4\\������\\�������\\�޸�����.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\test\\btn_kytrancac.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\attack\\model\\kind_s.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\attack\\model\\kind_z.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\auto\\state_autofight.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\avatar\\1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\avatar\\2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\blood\\blood.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\blood\\mana.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\blood\\stamina.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\blood\\statebar.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\ad.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\add_in.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\buy.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\dinh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\dinhgia.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\dinhthao.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\fix.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\get.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\handbag.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\join.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\key_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\key_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\key_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\remove.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\sell.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\separate.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\store.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\store%d.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\throw.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_equip\\use.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_select\\textbg_1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_select\\textbg_2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_skill\\addpoint.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\chidinh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\dieuhuong.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\extra.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\main.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\remove_extra.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\remove_main.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_skill\\tutim.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn_start\\btn_setting.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_start\\btn_signout.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_start\\btn_signup.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn_start\\btn_start.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\blacklist.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\btn_pk_0.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\btn_pk_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\btn_pk_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\cuusat.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\dong.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\friend.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn\\giaodich.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\haohuu.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\selectnpc.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\btn\\tanngau.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\theosau.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\tintuc.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\todoi.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\vaobang.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn\\xintodoi.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\´ò×ø.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\±³°ü.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\×é¶Ó.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\×Ó±³°ü.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\¼¼ÄÜ.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\Æï³Ë.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\ÈËÎï.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\ÈÎÎñ.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\zidong1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\zidong2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\人物.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\人物.png | 1 |
| \\ui\\btn01\\任务.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\任务.png | 1 |
| \\ui\\btn01\\子背包.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\子背包.png | 1 |
| \\ui\\btn01\\打坐.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\打坐.png | 1 |
| \\ui\\btn01\\技能.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\技能.png | 1 |
| \\ui\\btn01\\组队.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\组队.png | 1 |
| \\ui\\btn01\\背包.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\背包.png | 1 |
| \\ui\\btn01\\骑乘.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\骑乘.png | 1 |
| \\ui\\btn01\\�ӱ���.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\���.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\btn01\\����.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\chat\\city.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\faction.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\nearby.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\private.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\team.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\tong.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chat\\world.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\ui\\chatlist\\btn_send.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\chatlist\\chatbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\chatlist\\chatlistbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\chatlist\\expbar_vn.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\chatlist\\expbar.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\chestlock\\changelockchest.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\chestlock\\createlock.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\chestlock\\dellockchest.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\chestlock\\unlockchest.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\bg_btn_1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\bg_btn_2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\btn_cancel_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\UI\\common\\btn_cancel_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 7 |
| \\ui\\common\\btn_close_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\btn_close_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\btn_close_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\UI\\common\\btn_close_4_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\common\\btn_close_4.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\common\\btn_confirm_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\UI\\common\\btn_confirm_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 7 |
| \\ui\\common\\btn_del_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\common\\switch.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\dynamicshop\\btn_buy.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\dynamicshop\\btn_card.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\dynamicshop\\btn_close.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\dynamicshop\\btn_next.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\dynamicshop\\btn_prev.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\dynamicshop\\dynamicshop_bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\friend\\btn_cuunhan.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\friend\\btn_haohuu.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\friend\\btn_soden.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\friend\\friendBg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\input\\btn_cancel.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\input\\btn_ok.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\item\\btn_close_big.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\ui\\item\\btn_sell.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\item\\btn_selling.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\item\\btn_title.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\item\\ui_item.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\ui_item.png | 1 |
| \\ui\\login\\btn_login.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\login\\btn_logout.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\login\\loginbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\bg2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\bg2.png | 1 |
| \\ui\\main\\cmd.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\cmd.png | 1 |
| \\ui\\main\\cmd2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\cmd2.png | 1 |
| \\ui\\main\\fan1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\fan2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\gauiwu.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\guaiwu-on.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\guaiwu1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\guaiwu2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\hp1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\hp1.png | 1 |
| \\ui\\main\\hp2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\hp2.png | 1 |
| \\ui\\main\\liao001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\liao001.png | 1 |
| \\ui\\main\\life\\hongbanqiu_%02d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\hongbanqiu_01_0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\hongyemian_%02d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\hongyemian_01.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\lanbanqiu_%02d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\lanbanqiu_01.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\lanyemian_%02d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\lanyemian_01.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\longyan_%02d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\life\\longyan_01.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\qiehuan001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\qiehuan001.png | 1 |
| \\ui\\main\\qiehuan002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\qiehuan002.png | 1 |
| \\ui\\main\\renwu1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\renwu2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\roleInfo.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\roleInfo.png | 1 |
| \\ui\\main\\scalable_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\scalable_1.png | 1 |
| \\ui\\main\\task01.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\task02.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\wanjia-on.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\wanjia.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\main\\任务追踪底板_1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\maxmap\\btn_close.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\maxmap\\btn_location.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\newplayer\\btn_cancel.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\newplayer\\btn_confirm.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\newplayer\\newplayerbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\btn_1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\btn_2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\btn_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\btn_4.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\picFaction\\btn_5.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\playerfun\\bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\playerfun\\btn_new.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\rolestate\\btn_dinh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\rolestate\\btn_khoa.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\rolestate\\btn_thao.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\rolestate\\rolestate.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\rolestate\\viewrolestate.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selname\\blacklist.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selname\\chat.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selname\\friend.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selname\\searchname.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selnative\\nativebox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selplayer\\btn_creplayer.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selplayer\\btn_delplayer.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selplayer\\selplayerbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selserver\\btn_bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selserver\\btn_cancel_giant.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\selserver\\btn_confirm_giant.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\shop\\shopbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\skill\\skillbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_%d.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_arrange.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_change_pass.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_create_pass.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_del_pass.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_get_money.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_lock_pass.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_save_money.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\btn_unlock_pass.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\store\\storebox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\task\\btn_cancel_small.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| \\ui\\task\\btn_confirm_small.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\ui\\task\\taskbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\task\\tasklistbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_appoint.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_close.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_invite.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_kick.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_leave.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_refesh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\btn_team.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\team\\teambox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\Bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\BtnEnterMap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\BtnRefresh.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\BtnTongList.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\appoint.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\betray.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\createmap.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\daithan.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\decwar.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\diary.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\dismiss.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\getmoney.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\giverole.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\kick.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\master.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\onoff.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\renboy.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\rengirl.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\renmy.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\savemoney.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\search.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\button\\switchside.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\common\\bt_cam1.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\common\\bt_cam2.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\common\\bt_cam3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\common\\btn_cancel.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\common\\btn_confirm.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongchangecam\\cam_balance.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongchangecam\\cam_evil.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongchangecam\\cam_justice.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongchangecam\\changecambox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongchangetitle\\changetitlebox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongchangetitle\\title_boy.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongchangetitle\\title_girl.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongcreate\\bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongdelegate\\daithanbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongdelegate\\nguyensoai.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongdelegate\\thuatuong.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongdelegate\\tienphong.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongdiary\\btn_close.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongdiary\\btn_save.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongdiary\\diarybox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tonglist\\Bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tonglist\\btn_sau.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tonglist\\btn_truoc.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongmemberchange\\memberchangebox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongmemberchange\\title_kick.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongposition\\captain.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongposition\\chucvu.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongposition\\elder.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongposition\\student.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongpower\\btn_close.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\tong\\tongpower\\powerbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongsearch\\level.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongsearch\\point.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongsearch\\position.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\UI\\tong\\tongsearch\\searchbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\trade\\btn_agree_big.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\trade\\btn_cancel_big.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\trade\\btn_confirm_big.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\ui\\trade\\shopbox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\ui\\trade\\tradebox.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\update10\\spr\\ui3\\chat\\system.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\update10\\spr\\Ui3\\UiDialog\\main_msgsel.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\update10\\spr\\Ui3\\UiTalkDialog\\main_talk.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| \\游戏资源\\logo.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\游戏资源\\地图动画\\熔岩\\10160.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| \\��Ϸ��Դ\\background\\����ͼ_��.jpg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \\��Ϸ��Դ\\logo.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| \\��Ϸ��Դ\\��ͼ����\\����\\10160.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \Music\Music001.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \Music\Music002.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| \music\music003.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| %s_%d.jpg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| %s_%d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| %s_%s_%s_%d.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| 10160.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| 24.jpg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| 64x64.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 9 |
| attack\attack_%d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| attack\model\kind_s.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\attack\model\kind_s.png | 1 |
| attack\model\kind_z.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\attack\model\kind_z.png | 1 |
| avatar\0.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\avatar\0.png | 2 |
| b.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| box001.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| box2exchange.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| boxgb.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\boxgb.png | 5 |
| btn_confirm_select.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 4 |
| btn_n.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\btn_n.png | 1 |
| btn_string_cn.xml | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| btn_string_vn.xml | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| cboDs1_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs1_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs2_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs2_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs3_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs3_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs4_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboDs4_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs1_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs1_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs2_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs2_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs3_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs3_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs4_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboFs4_target.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs1_start_m.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs1_start_w.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs2_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs3_start_m.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs3_start_w.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| cboZs4_start.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| close.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\close.png | 15 |
| CloseNormal.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\CloseNormal.png | 3 |
| CloseSelected.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\CloseSelected.png | 3 |
| color\green.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\color\green.png | 1 |
| color\magenta.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\color\magenta.png | 1 |
| color\white.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| color\yellow.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\color\yellow.png | 1 |
| cyclone.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| dare-win.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| drumloop.wav | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Field2.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Flashbox.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| fonts\arial.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\arial.ttf | 4 |
| fonts\font_11.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\font_11.fnt | 2 |
| fonts\font_12.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\font_12.fnt | 4 |
| fonts\font_14.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\font_14.fnt | 5 |
| fonts\font_16.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\font_16.fnt | 3 |
| fonts\font_18.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\font_18.fnt | 2 |
| fonts\gb_song.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\gb_song.ttf | 13 |
| fonts\Marker Felt.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\Marker Felt.ttf | 2 |
| fonts\msyh.ttf | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| fonts\number_16_r.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\number_16_r.fnt | 1 |
| fonts\number_16_w.fnt | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\number_16_w.fnt | 2 |
| fonts\roboto-light_new.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\roboto-light_new.ttf | 2 |
| fonts\Roboto-Regular.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\Roboto-Regular.ttf | 3 |
| fonts\RobotoCondensed-Regular.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\RobotoCondensed-Regular.ttf | 3 |
| fonts\syzt-e.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\syzt-e.ttf | 1 |
| fonts\vnavanb.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\vnavanb.ttf | 3 |
| fonts\VnAvant_Regular.TTF | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| fonts\vntimebold.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\vntimebold.ttf | 1 |
| fonts\yahei_gb2312.ttf | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fonts\yahei_gb2312.ttf | 3 |
| game over2.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| HelloWorld.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\HelloWorld.png | 1 |
| hero-shield.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| HeroLogin.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| HeroLogout.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| horsemix.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| huoliankuangwu.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Icon-Small-50.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Icon-Small.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| img_chat.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| jaguar.wav | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KgameWorld\attack_%d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\attackSpr_dir.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KgameWorld\attackSpr_dir.png | 2 |
| KgameWorld\battery_small.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\immediacybox.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KgameWorld\life_bg_null.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\mainskillmix.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\mr-1_new.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\mr-2_new.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KgameWorld\mr-2_new.png | 2 |
| KgameWorld\tili.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\useskill_b.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KgameWorld\yaoganx.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KuiChatList\banghoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KuiChatList\banghoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KuiChatList\ChatListIcon-001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\ChatListIcon-001.png | 2 |
| KuiChatList\ChatListIcon-002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\ChatListIcon-002.png | 2 |
| KuiChatList\ChatListIcon-003.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\ChatListIcon-003.png | 2 |
| KuiChatList\chonmotnguoi.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\chonmotnguoi.png | 1 |
| KuiChatList\chonmotnguoi2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\chonmotnguoi2.png | 1 |
| KuiChatList\hethong.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\hethong.png | 2 |
| KuiChatList\hethong2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\hethong2.png | 2 |
| KuiChatList\mat.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\mat.png | 2 |
| KuiChatList\mat2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\mat2.png | 2 |
| KuiChatList\tatca.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\tatca.png | 2 |
| KuiChatList\tatca2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\tatca2.png | 2 |
| KuiChatList\thegioi.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\thegioi.png | 2 |
| KuiChatList\thegioi2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\KuiChatList\thegioi2.png | 2 |
| KuiChatList\todoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KuiChatList\todoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| KuiPlayerSelFun\%d-%d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiPlayerSelFun\0-0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiPlayerSelFun\selplayer_life.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiPlayerSelFun\selplayeritem.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiPlayerSelFun\series-%d.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiTopControl\AvatarNam.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| KuiTopControl\AvatarNu.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Label_outline1.frag | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| loading_di.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\loading_di.png | 2 |
| loading_dijindutiao.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\loading_dijindutiao.png | 2 |
| loadingEnd.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\loadingEnd.png | 5 |
| loadingStart.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\loadingStart.png | 14 |
| Log-in-long2.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| login_bg.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\login_bg.png | 5 |
| login_bg1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\login_bg1.png | 2 |
| loginbg_2-9.jpg | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\loginbg_2-9.jpg | 7 |
| longin_bg.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\longin_bg.png | 4 |
| longsword-hit.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| M56-0.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| M56-3.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| main_theme.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| mainskillmix.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| map\default_vn.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\map\default_vn.png | 1 |
| map\greenPoint.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\map\greenPoint.png | 3 |
| map\redPoint.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\map\redPoint.png | 3 |
| map\white.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| map\YellowPoint.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\map\YellowPoint.png | 3 |
| map\zisePoint.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\map\zisePoint.png | 3 |
| maps\CityMaps\City%d.map | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| mask.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| music\Music001.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| music\music002.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| music\music003.mp3 | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| newysound-mix.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| newysound1.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| newysound2.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| Openbox.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| p_tips.plist | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 14 |
| powerup.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| qianxing_run.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| qianxing_shifang.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| rushhit.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| rushmove.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| S1-1.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| S1-2.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| S1-3.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| sel_mask.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\sel_mask.png | 5 |
| SelectBoxFlash.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| selpic\pkno1tong-012.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\selpic\pkno1tong-012.png | 1 |
| Shaders\blur.fsh | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\Shaders\blur.fsh | 1 |
| Shaders\blur.vsh | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\Shaders\blur.vsh | 1 |
| shengguanqindun.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| show.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\show.png | 1 |
| shuangyue.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| slider\slider_ball.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\slider\slider_ball.png | 1 |
| slider\slider_bar.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\slider\slider_bar.png | 1 |
| slider\slider_bg.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\slider\slider_bg.png | 1 |
| Sound\sound_i001.wav | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| spring.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| string_cn.xml | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\string_cn.xml | 2 |
| string_vn.xml | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\string_vn.xml | 2 |
| string.xml | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\string.xml | 1 |
| swish.wav | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| temp\c.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\temp\c.png | 1 |
| temp\inputip.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\temp\inputip.png | 2 |
| temp\ok.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| test.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\test.png | 2 |
| TextureAtlas\default.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\auto.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\auto.png | 1 |
| toolbar\auto2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\auto2.png | 1 |
| toolbar\banghoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\banghoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\banghuu.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\banghuu.png | 1 |
| toolbar\banghuu2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\banghuu2.png | 1 |
| toolbar\baodanh.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\baodanh.png | 1 |
| toolbar\baodanh2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\baodanh2.png | 1 |
| toolbar\caidat.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\caidat.png | 1 |
| toolbar\caidat2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\caidat2.png | 1 |
| toolbar\dichay.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay.png | 1 |
| toolbar\dichay2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay2.png | 1 |
| toolbar\dichay3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay3.png | 1 |
| toolbar\giaodich.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaodich.png | 1 |
| toolbar\giaodich2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaodich2.png | 1 |
| toolbar\giaotiep.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaotiep.png | 1 |
| toolbar\giaotiep2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaotiep2.png | 1 |
| toolbar\hangdong.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hangdong.png | 1 |
| toolbar\hangdong2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hangdong2.png | 1 |
| toolbar\hanhtrang.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hanhtrang.png | 1 |
| toolbar\hanhtrang2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hanhtrang2.png | 1 |
| toolbar\hide.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hide.png | 1 |
| toolbar\hide2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hide2.png | 1 |
| toolbar\horse.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\horse2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\horse2.png | 1 |
| toolbar\kytrancac1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac1.png | 1 |
| toolbar\kytrancac2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac2.png | 1 |
| toolbar\kytrancac3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac3.png | 1 |
| toolbar\mess.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\mess.png | 1 |
| toolbar\mess2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\mess2.png | 1 |
| toolbar\ngoi.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\ngoi.png | 1 |
| toolbar\ngoi2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\ngoi2.png | 1 |
| toolbar\nhanvat.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhanvat.png | 1 |
| toolbar\nhanvat2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhanvat2.png | 1 |
| toolbar\nhatnhanh.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhatnhanh.png | 1 |
| toolbar\nhatnhanh2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhatnhanh2.png | 1 |
| toolbar\todoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\todoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| toolbar\trangthai.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai.png | 1 |
| toolbar\trangthai2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai2.png | 1 |
| toolbar\trangthai3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai3.png | 1 |
| toolbar\vocong.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\vocong.png | 1 |
| toolbar\vocong2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\vocong2.png | 1 |
| toolbar\xephang.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\xephang.png | 1 |
| toolbar\xephang2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\xephang2.png | 1 |
| transence.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\transence.png | 5 |
| ui_vn\KuiChatList\khungchat.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\KuiTopControl\blood.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\KuiTopControl\mana.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\KuiTopControl\rolestate.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\KuiTopControl\stamina.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\auto.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\auto.png | 1 |
| ui_vn\toolbar\auto2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\auto2.png | 1 |
| ui_vn\toolbar\autoplay.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\autoplay3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\autoplay3.png | 1 |
| ui_vn\toolbar\autoplay4.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\autoplay4.png | 1 |
| ui_vn\toolbar\banghoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\banghoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\banghuu.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\banghuu.png | 1 |
| ui_vn\toolbar\banghuu2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\banghuu2.png | 1 |
| ui_vn\toolbar\baodanh.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\baodanh.png | 1 |
| ui_vn\toolbar\baodanh2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\baodanh2.png | 1 |
| ui_vn\toolbar\caidat.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\caidat.png | 1 |
| ui_vn\toolbar\caidat2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\caidat2.png | 1 |
| ui_vn\toolbar\dichay.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay.png | 1 |
| ui_vn\toolbar\dichay2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay2.png | 1 |
| ui_vn\toolbar\dichay3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\dichay3.png | 1 |
| ui_vn\toolbar\giaodich.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaodich.png | 1 |
| ui_vn\toolbar\giaodich2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaodich2.png | 1 |
| ui_vn\toolbar\giaotiep.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaotiep.png | 1 |
| ui_vn\toolbar\giaotiep2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\giaotiep2.png | 1 |
| ui_vn\toolbar\hangdong.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hangdong.png | 1 |
| ui_vn\toolbar\hangdong2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hangdong2.png | 1 |
| ui_vn\toolbar\hanhtrang.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hanhtrang.png | 1 |
| ui_vn\toolbar\hanhtrang2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hanhtrang2.png | 1 |
| ui_vn\toolbar\hide.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hide.png | 1 |
| ui_vn\toolbar\hide2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\hide2.png | 1 |
| ui_vn\toolbar\horse.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\horse2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\horse2.png | 1 |
| ui_vn\toolbar\kytrancac1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac1.png | 1 |
| ui_vn\toolbar\kytrancac2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac2.png | 1 |
| ui_vn\toolbar\kytrancac3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\kytrancac3.png | 1 |
| ui_vn\toolbar\mess.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\mess.png | 1 |
| ui_vn\toolbar\mess2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\mess2.png | 1 |
| ui_vn\toolbar\ngoi.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\ngoi.png | 1 |
| ui_vn\toolbar\ngoi2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\ngoi2.png | 1 |
| ui_vn\toolbar\nhanvat.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhanvat.png | 1 |
| ui_vn\toolbar\nhanvat2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhanvat2.png | 1 |
| ui_vn\toolbar\nhatnhanh.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhatnhanh.png | 1 |
| ui_vn\toolbar\nhatnhanh2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\nhatnhanh2.png | 1 |
| ui_vn\toolbar\todoi.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\todoi2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui_vn\toolbar\trangthai.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai.png | 1 |
| ui_vn\toolbar\trangthai2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai2.png | 1 |
| ui_vn\toolbar\trangthai3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\trangthai3.png | 1 |
| ui_vn\toolbar\vocong.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\vocong.png | 1 |
| ui_vn\toolbar\vocong2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\vocong2.png | 1 |
| ui_vn\toolbar\xephang.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\xephang.png | 1 |
| ui_vn\toolbar\xephang2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\toolbar\xephang2.png | 1 |
| ui_vn\UiKgameWorld.plist | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\UiKgameWorld.plist | 2 |
| ui_vn\UiKgameWorld.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui_vn\UiKgameWorld.png | 2 |
| ui\\auto\\page_%d.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\\btn\\horse.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\\common\\btn_close_4.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\\common\\check_box_3.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\\playerfun\\btn_bg.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\\shop\\btn_next_page.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\\shop\\btn_prev_page.spr | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\at\icon_sk_ty_ap.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\at\icon_sk_ty_ap.png | 1 |
| ui\at\mr-1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\at\mr-1.png | 1 |
| ui\at\mr-2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\at\mr-2.png | 1 |
| ui\battery_small.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\btn_3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn_3.png | 7 |
| ui\btn_sel.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 12 |
| ui\btn\btn_bg_auto.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\btn_bg_auto.png | 1 |
| ui\btn\fz01.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\fz01.png | 3 |
| ui\btn\fz02.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\fz02.png | 3 |
| ui\btn\pick_01.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\pick_01.png | 1 |
| ui\btn\pick_02.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\pick_02.png | 1 |
| ui\btn\qx01.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\qx01.png | 3 |
| ui\btn\qx02.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\btn\qx02.png | 3 |
| ui\buttons\battle.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\collapse_new.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\collapse_new.png | 2 |
| ui\buttons\expand_new.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\buttons\expand_new.png | 2 |
| ui\buttons\friend.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\items.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\role.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\settings.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\shop.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\skills.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\task.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\buttons\team.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\calendarpage.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\calendarpage.png | 2 |
| ui\chat\bang.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\bang.png | 2 |
| ui\chat\faction.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\chat\global.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\global.png | 2 |
| ui\chat\nearby.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\nearby.png | 2 |
| ui\chat\private.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\private.png | 2 |
| ui\chat\private1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\private1.png | 2 |
| ui\chat\system.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\chat\system.png | 2 |
| ui\chat\team.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\checkbox\001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\checkbox\001.png | 3 |
| ui\checkbox\002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\checkbox\002.png | 3 |
| ui\dir_role_new_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\dir_role_new_1.png | 2 |
| ui\editbg.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\editbg.png | 12 |
| ui\gameworld\AvatarNam.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\gameworld\AvatarNu.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\gameworld\btn_sel_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\btn_sel_1.png | 1 |
| ui\gameworld\btn_sel_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\btn_sel_2.png | 1 |
| ui\gameworld\UiItem\btn_bayban1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_bayban1.png | 1 |
| ui\gameworld\UiItem\btn_bayban2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_bayban2.png | 1 |
| ui\gameworld\UiItem\btn_huyban1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_huyban1.png | 1 |
| ui\gameworld\UiItem\btn_huyban2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_huyban2.png | 1 |
| ui\gameworld\UiItem\btn_sapxep1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_sapxep1.png | 1 |
| ui\gameworld\UiItem\btn_sapxep2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\btn_sapxep2.png | 1 |
| ui\gameworld\UiItem\ui_item.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\gameworld\UiItem\ui_item.png | 1 |
| ui\logo.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\logo.png | 1 |
| ui\main\cmd.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\cmd.png | 1 |
| ui\main\cmd2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\cmd2.png | 1 |
| ui\main\fan1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\main\fan2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\main\fire.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\fire.png | 1 |
| ui\main\liao001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\liao001.png | 1 |
| ui\main\mountain.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\mountain.png | 2 |
| ui\main\qiehuan001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\qiehuan001.png | 1 |
| ui\main\qiehuan002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\qiehuan002.png | 1 |
| ui\main\roleInfo.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\roleInfo.png | 1 |
| ui\main\search.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\main\search.png | 2 |
| ui\radius_skill.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\radius_skill.png | 1 |
| ui\rolestate.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selcolor.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selcolor.png | 4 |
| ui\selects\btn_sel.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selects\item_sel.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selects\item_sel.png | 1 |
| ui\selects\list_item.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selects\list_item.png | 1 |
| ui\selectsv.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selectsv.png | 1 |
| ui\selectsv1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selectsv1.png | 1 |
| ui\selnpc\0-0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\selnpc\1-0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\1-1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\2-1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\3-0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\3-1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\4-0.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selnpc\4-1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\selserver.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\selserver.png | 1 |
| ui\skill_selected.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\skill_selected.png | 2 |
| ui\sortskill_r_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\sortskill_r_1.png | 1 |
| ui\sortskill_r_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\sortskill_r_2.png | 1 |
| ui\state\immediacybox.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\state\kbgitem.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\state\kbgitem.png | 1 |
| ui\state\life_bg_null.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\state\life_bg.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| ui\state\life_deathmatch.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\state\life_killer.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\state\life_normal.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 6 |
| ui\state\life_pk.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 17 |
| ui\state\life_tusha.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| ui\state\normal.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 3 |
| ui\state\roleheadpic.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\state\roleheadpic.png | 1 |
| ui\state\skill.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\state\view_other.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\state\view_other.png | 1 |
| ui\statelan.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\statelan.png | 3 |
| ui\statelife.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\statelife.png | 3 |
| ui\textbg_1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 12 |
| ui\textbg_2.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\textbg_4.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\textbg_4.png | 1 |
| ui\textbg.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 14 |
| ui\textbg3_1.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\textbg3_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\textbg3_2.png | 1 |
| ui\tili.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| ui\tools\dibo-001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\dibo-001.png | 2 |
| ui\tools\dibo-002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\dibo-002.png | 2 |
| ui\tools\fight.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\fight.png | 2 |
| ui\tools\giaodich-001.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\giaodich-001.png | 2 |
| ui\tools\giaodich-002.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\giaodich-002.png | 2 |
| ui\tools\muder.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\muder.png | 2 |
| ui\tools\pAuto_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pAuto_1.png | 2 |
| ui\tools\pAuto_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pAuto_2.png | 2 |
| ui\tools\pAuto_3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pAuto_3.png | 2 |
| ui\tools\pCave_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pCave_1.png | 2 |
| ui\tools\pCave_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pCave_2.png | 2 |
| ui\tools\pCave_3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pCave_3.png | 2 |
| ui\tools\pHuo_1.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pHuo_1.png | 2 |
| ui\tools\pHuo_2.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pHuo_2.png | 2 |
| ui\tools\pHuo_3.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\pHuo_3.png | 2 |
| ui\tools\practise.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\tools\practise.png | 2 |
| ui\user_skill_.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\user_skill_.png | 2 |
| ui\white.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| ui\worldmap.png | FOUND_LOOSE | Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Resources\ui\worldmap.png | 1 |
| update.pak | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| useskill_b.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| useskill_z.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| vn\updateEnd.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| vn\updateStart.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| yanlongbo.ogg | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 1 |
| yaoganx.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
| yaoganz.png | UNRESOLVED_PACKED_DYNAMIC_OR_ABSENT |  | 2 |
