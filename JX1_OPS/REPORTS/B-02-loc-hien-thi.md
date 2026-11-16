# B-02 - Loc hien thi P1 (build only)

## TOM TAT
1. Tiep tuc dung hai file KVisibility.h/.cpp con dang do; ban dau Git chi co hai file nay untracked, HEAD 18c6f18, nhanh feature/visibility.
2. Da noi policy Solo/Group/Open, VisGroup, IsBot, OwnerPlayer va gioi han nhom vao cac duong dong bo P1; khong sua GetRelation hay logic P2/P3.
3. Theo doi NPC ID da gui tren tung viewer; REMOVE bo qua policy hien tai/count/sleep, refresh hai chieu khi doi nhom/doi va reset ledger sau WORLD_SYNC thanh cong.
4. Co visibility.ini mac dinh Enabled=0, doc mot lan khi khoi dong; da dang ky API Lua va setter bot/owner de script gan co.
5. Build VS2022 v143 x64: CoreServer.dll, Common.lib, gs001.exe thanh cong; chua chay binary, chua ket noi VM/SQL/server, chua test B-03/B-04.

## File:dong da sua
Cac dong duoi day la vi tri bat dau tung hunk trong ban cuoi; duong dan tu goc worktree.

- `server/jxOnline/gameserver/Sources/Core/Core.vcxproj:704,1151`
- `server/jxOnline/gameserver/Sources/Core/Src/KCore.cpp:10,257`
- `server/jxOnline/gameserver/Sources/Core/Src/KNpc.cpp:5,158,7961,8018,8124,10234`
- `server/jxOnline/gameserver/Sources/Core/Src/KNpc.h:340`
- `server/jxOnline/gameserver/Sources/Core/Src/KNpcSet.cpp:2,1289`
- `server/jxOnline/gameserver/Sources/Core/Src/KObj.cpp:10,1454,1471`
- `server/jxOnline/gameserver/Sources/Core/Src/KPlayer.cpp:103`
- `server/jxOnline/gameserver/Sources/Core/Src/KPlayer.h:24,256`
- `server/jxOnline/gameserver/Sources/Core/Src/KPlayerTeam.cpp:25,500,850,885`
- `server/jxOnline/gameserver/Sources/Core/Src/KRegion.cpp:2,2247,2296`
- `server/jxOnline/gameserver/Sources/Core/Src/KSubWorld.cpp:2,1784,1787,2386,2392`
- `server/jxOnline/gameserver/Sources/Core/Src/ScriptFuns.cpp:20,25671,25715`
- `server/jxOnline/gameserver/Sources/Core/Src/KVisibility.cpp:1`
- `server/jxOnline/gameserver/Sources/Core/Src/KVisibility.h:1`
- `server/jxOnline/gameserver/Sources/Settings/visibility.ini:1`

## Hanh vi va cach bat/tat
- Mau cau hinh: `server/jxOnline/gameserver/Sources/Settings/visibility.ini`. Do task chi cho ghi Sources, dat mau tai day; khi trien khai sau phe duyet, chep thanh `Settings/visibility.ini` cua gameserver runtime. Khong deploy trong task nay.
- `Enabled=0` (hoac thieu file) di thang duong gui goc, khong doi buffer/do dai goi, khong them ADD/REMOVE. Doi file can khoi dong lai; khong co hot reload.
- Bat bang `[General] Enabled=1`. Map khong khai bao mac dinh Solo. `[Map_<mapId>] Mode=Solo|Group|Open`; Map_0 trong mau chi la placeholder, can doi sang map hoat dong thuc. Solo an nguoi that; Group cho thay nguoi cung VisGroup khac 0; Open giu hien thi goc. Self luon thay self; NPC/quai/object dung chung; co OwnerPlayer uu tien truoc mien tru NPC/bot.
- `BotsVisibleToAll=1`, `PartyMutualVisible=0` mac dinh. Hao huu duoc gan owner chi hien voi owner va dong doi cua owner, ke ca PartyMutualVisible=0. Owner duoc kiem tra ca player ID de tranh slot tai su dung.
- `[Group_<id>] MaxVisible=60`: tran thanh vien nguoi that (tinh ca ban than), clamp 1..MAX_PLAYER-1. `SetVisGroup(group)` tra 1/0 va tu choi nhom day; group=0 roi nhom. `GetVisGroup()` tra ID. Chi map Group su dung VisGroup de hien thi.
- `JoinActivityGroup(activityId)` dung `[Group_<activityId>] MaxVisible`, tu tao/chon nhom con con cho, tra group ID hoac 0. `LeaveActivityGroup()` ve 0. ID nhom con lay tu INT_MAX giam dan, tranh ID da dung/cau hinh.
- `IsBotPlayer(playerIdx)` tra 1/0 (bo tham so thi lay player Lua hien tai). `SetBotPlayer(playerIdx,flag)` gan co IsBot; `SetNpcVisibilityOwner(npcIdx,ownerPlayerIdx)` gan owner, 0 = NPC chung. Bot/owner mac dinh false/0, script tao bot/hao huu phai gan co ro rang; khong suy doan bot tu sleep/offline/ten nhan vat.
- `RefreshVisibility(playerIdx)` co ban C++ va Lua (Lua bo tham so dung player hien tai). Duyet region hien tai + 8 region noi; REMOVE quan he mat thay va SendSyncData cho quan he moi thay; refresh ca hai chieu. Doi nhom va doi co tu refresh; join/leave/dismiss party refresh tat ca viewer sau khi doi state.
- Gui thang KNpc::SendSyncData/KNpcSet::SyncNpc bat buoc viewer hop le, cung world va trong 9 region khi bat loc. KSubWorld::BroadCasts phan loai goi; chi screen chat di theo visibility, chat he thong/kenh khac giu routing cu.
- KObj direct add dung mien tru visObject; state/dir/remove/trap qua KRegion voi mien tru object. Khong gan owner cho object trong P1.
- Full/min NPC sync duoc ghi nhan theo ID (bao thu voi min sync co the gay client request full ADD); chi xoa ledger sau PackDataToClient thanh cong. REMOVE goc giu nguyen byte/Rv; REMOVE do refresh tao su dung Rv=TRUE de unlink region node client.

## Build va kiem tra
Ban sao rieng con luu tai `server/jxOnline/gameserver/Sources/.b02-build/`; du lieu build bi ignore noi bo va khong commit. Dau vao C++/header la ban sao worktree, da doi chieu byte voi tat ca file thay doi; khong dung ma Core cu thay cho ma da sua.

Doc `D:\jx1-ops-wt\JX1_OPS\TOOLS\a07\build-debug-a07.ps1` de lay cach goi toolchain. Khong chay script do vi hardcode ghi D:\JX-build\a07. Chi doc D:\JX-build\src18 va shim de sao chep import/static libs, msado15.tlh/.tli va resource GameServer.ico vao ban build. Cac lan dau ban sao thieu msado15.tlh, S3DBInterface.h, LuaLibDll.lib, USBKey libs, serverstage.h, GameServer.ico; da bo sung dependency trong ban sao, khong sua noi canonical.

Trong vcxproj cua ban sao: tat PostBuildEvent, ep /MT /Od /GL-, PCH/obj/PDB/out vao .b02-build, /source-charset:.936 /execution-charset:.936 /Zc:sizedDealloc- /Zc:strictStrings-, linker /DEBUG:FULL /INCREMENTAL:NO. Common va GameServer dung Release, Core dung Server Release; cau hinh build kiem tra co optimization disabled. GameServer link Common.lib va CoreServer.lib vua build, engine.lib/ms64.lib co san va iob_shim.obj. Khong ghi de project/build D:\JX-build.

Lenh PowerShell (chay o goc worktree, voi ban sao da chuan bi nhu tren):

```powershell
$msbuild = 'C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe'
$b02 = Join-Path (Get-Location) 'server\jxOnline\gameserver\Sources\.b02-build'
$jobs = @(
    @('Core', 'Core\Core.vcxproj', 'Server Release'),
    @('Common', 'MultiServer\Common\Common.vcxproj', 'Release'),
    @('GameServer', 'MultiServer\GameServer\GameServer.vcxproj', 'Release')
)
foreach ($job in $jobs) {
    & $msbuild "$b02\gameserver\Sources\$($job[1])" /t:Build /m:1 /nologo /v:minimal `
        "/p:Configuration=$($job[2])" /p:Platform=x64 /p:PlatformToolset=v143 `
        /p:WindowsTargetPlatformVersion=10.0.19041.0 /p:BuildProjectReferences=false `
        "/p:OutDir=$b02\out\" "/p:IntDir=$b02\obj\$($job[0])\" `
        "/flp:logfile=$b02\logs\$($job[0]).log;verbosity=normal"
    if ($LASTEXITCODE -ne 0) { throw "Build $($job[0]) failed" }
}
```

Log `Core.log`, `Common.log`, `GameServer.log` trong `.b02-build/logs/` deu ket thuc 0 Error(s). Con canh bao ma cu: macro rpcsal, conversion/printf size_t, encoding GBK, target Core/CoreServer mismatch va thieu PDB cua ms64.lib. Khong khang dinh warning-free. `git diff --check` dat.

SHA256 artifact (chi build, khong chay):

- `CoreServer.dll`: `8539f80f0a8d8b472237c8a270e768947beb3ebe390d58bbdb40915aa423baf7`
- `Common.lib`: `a50c2f3d39daa40482e51a3c1e684a3faaaaa8fb1db7aefb8e7da67c79e70dae`
- `gs001.exe`: `774adbdfc2a47facbf72e4e0f8c813fd090c618117bd39e2de524b43b31fecb8`

## Chua kiem
- Chua chay 2 client + 1 bot, chua so goi Enabled=0 voi baseline; chi doi chieu nhanh disabled bang doc ma.
- Chua test runtime REMOVE/ADD khi doi nhom/party, teleport/random world, reconnect/slot reuse, min-sync/request full, queue send failure, bot chuyen thanh nguoi, owner ra/vao doi.
- Chua gan script hoat dong/bot/hao huu production vao cac API moi, chua test tran MaxVisible+1 tren client.
- Chua do tick/bang thong/bo nho ledger (B-04). Lookup policy khong doc file/DB; refresh toan viewer chi o su kien doi party.
- P2 (dame/AoE/team/trade/PK tu client) va P3 (don slot offline) nam ngoai task; P1 chua phai co che chan tuong tac hoan chinh.

## Ket qua Git
Chua commit: lenh `git add -- B-02-loc-hien-thi.md ...` bi chan truoc khi stage:

```text
fatal: Unable to create 'D:/JX-source/.git/worktrees/B-02/index.lock': Permission denied
```

Worktree dung nhanh feature/visibility; metadata Git nam ngoai vung duoc ghi cua session. Khong doi quyen, khong ghi de Git metadata. PM can stage/commit tu moi truong co quyen, tieu de de nghi `B-02: integrate P1 visibility filtering and Lua group APIs`. File mau visibility.ini bi rule *.ini ignore nen can `git add -f -- server/jxOnline/gameserver/Sources/Settings/visibility.ini`. Artifact/log build chi luu trong .b02-build, khong commit.
