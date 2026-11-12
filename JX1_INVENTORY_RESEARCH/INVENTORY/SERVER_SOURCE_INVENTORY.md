# Server Source Inventory

Legend: VERIFIED = directly supported by a file or configuration; PROBABLE = inference from structure/symbols; UNKNOWN = not established from source inspection; BLOCKED = intentionally not inspected.

## Source roots and build system

- **VERIFIED** — Game server source tree: SwordOnline/SwordOnline/jxOnline/gameserver/Sources.
- **VERIFIED** — Gateway/service source tree: SwordOnline/SwordOnline/jxOnline/gateway/Sources.
- **VERIFIED** — Both trees are legacy Windows C/C++ projects. Gameserver has JXAll_GameServer.sln and JXAll.sln plus 11 .vcxproj files. Gateway has JXAll_GateWay.sln and JXAll.sln plus 17 .vcxproj files.
- **VERIFIED** — Source extensions under these roots include .cpp, .c and .h; the same trees also contain Visual Studio intermediates and outputs (.obj, .sbr, .cod, .lib, .dll, .pdb, .tlog, .log, x64/Release/ipch).
- **UNKNOWN** — Compiler/toolset and exact server version currently running. No build or server process was started; source/runtime binary parity is not established.
- **PROBABLE** — Multiple service executables/components are assembled through Visual Studio solutions, based on their project files and service directories. Exact deployment graph was not run or validated.

## Gameserver modules

Verified top-level modules in gameserver/Sources:

- AutoUpdateRes
- Core
- Engine
- FilterText and FilterTextTest
- Library (including LuaLib)
- MultiServer
- MySql
- x64 build output

The GameServer project is MultiServer/GameServer/GameServer.vcxproj; launch-signature candidate is GameServer.cpp:141. Heaven and Rainbow each have project/source directories under MultiServer. Core source names include game-world, NPC, map and skill components. Project paths and source names establish presence, not that each project is shipped or active.

## Gateway and service modules

Verified top-level modules in gateway/Sources:

- AutoUpdateRes, Common, Engine
- FilterText and FilterTextTest
- Library (including LuaLib)
- MultiServer
- MySql
- Sword3PaySys
- Release/ipch build output

Service/project directories include MultiServer/Bishop, Goddess, Heaven, Intercessor, Rainbow and S3Relay; account/payment projects include Sword3PaySys/S3AccServer, S3RELAYSERVER, S3DBClient and S3AccClientSample.

Launch-signature candidates found by source scan include:
- gameserver: MultiServer/GameServer/GameServer.cpp:141; MultiServer/Heaven/Heaven.cpp:14; MultiServer/Rainbow/Rainbow.cpp:10.
- gateway: MultiServer/Bishop/Bishop.cpp:96; Goddess/Goddess.cpp:385; Intercessor/Intercessor.cpp:67; S3Relay/S3Relay.cpp:191; Sword3PaySys/S3AccServer/main.cpp:85; Sword3PaySys/S3RELAYSERVER/main.cpp:78.

These are source-level main/WinMain/DllMain signature locations, not proof of the exact runtime launch order.

## Game-domain source areas

Verified source filenames under gameserver/Sources/Core/Src include KNpc.cpp, KNpcAI.cpp, KPlayer.cpp, KSubWorld.cpp, KRegion.cpp, KItem.cpp, KSkills.cpp, KSkillManager.cpp and KProtocol.cpp. These establish source modules for NPC/AI, player, world/map/region, item, skill and protocol handling. The distinction between NPCs and monster types, and exact activity/event coverage, is UNKNOWN without inspecting game data/scripts.
## Language, database, network and dependencies

- **VERIFIED** — C and C++ source is present. Lua interpreter/compiler sources are included under Library/LuaLib; server runtime bundle contains Lua scripts, but script contents were not inspected here.
- **VERIFIED** — Dependency/module directories include MySql, Library/LuaLib, FilterText, Engine, Common, include and Lib. Gateway Goddess includes mysql_db.cpp and IDBRoleServer/DBTable components.
- **VERIFIED** — Network source files include Engine/Src/KNetServer.cpp and MultiServer/Common/SocketServer.cpp; protocol-oriented client/server source names include KProtocol files.
- **PROBABLE** — The code uses a custom TCP/socket service layer and a legacy database integration. Exact wire protocol, transport settings and database engine in the active deployment are not established by filename evidence alone.
- **UNKNOWN** — Third-party dependency versions, library linkage per service, active database schema/configuration and complete protocol documentation.
- **BLOCKED** — Database files, account data, server configuration values, logs, dumps, private credentials and key material were not opened or copied into this report.

## Runtime package versus source

- **VERIFIED** — A separate runtime/deployment bundle is under Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_. It includes binaries, settings/scripts, archives, logs and dumps by metadata. This is not the same path as the SwordOnline source tree.
- **UNKNOWN** — Which exact runtime binaries were built from the visible source revision. No hashes were calculated for server binaries and no runtime was launched.
- **NOT TESTED** — No build, database connection, service startup, VM operation, network test or gameplay test was performed.
- Server source inventories cover file metadata and selected source/project names. Secrets/configuration content and archive internals remain intentionally unread.