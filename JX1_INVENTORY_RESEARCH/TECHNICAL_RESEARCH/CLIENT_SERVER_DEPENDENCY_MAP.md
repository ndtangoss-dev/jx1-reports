# CLIENT_SERVER_DEPENDENCY_MAP — Quan hệ client / gameserver / gateway / dữ liệu

Nhãn: **VERIFIED · PROBABLE · UNKNOWN · BLOCKED**. `CLIENT` = `Folder/Client2912-20260116T044348Z-3-001/Client2912/Client`; `SRV` = `SwordOnline/SwordOnline/jxOnline`; `RUNTIME` = `Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_`.
Phase này không chạy server, không mở cổng, không đọc cấu hình chứa giá trị nhạy cảm. Bảng cổng cụ thể nằm ở `docs-analysis/BAI_HOC.md` (không nhắc lại ở đây).

## TÓM TẮT
1. Theo mã nguồn, hệ thống gồm các tiến trình: `Sword3PaySys` (tài khoản/thanh toán), `Goddess` (lưu nhân vật), `S3Relay` (bang hội, bạn bè), `Bishop` (cửa đăng nhập/điều phối), `Intercessor`, `Heaven`/`Rainbow` (vai trò chưa rõ) và `gs001` (GameServer).
2. Client nói chuyện với server bằng gói tin nhị phân có kiểu 1 byte, mã hóa bằng XOR cuốn (chỉ làm rối, không phải mật mã). Bảng ID giao thức của client và server **trùng nhau** ở các họ quan trọng (xem mục 3).
3. Điểm giao thoa dễ lệch nhất là **struct payload** dùng `#pragma pack(1)` ở hai bên; phase này mới so sánh enum, chưa so sánh từng struct.
4. Mã nguồn server có thể không khớp exe đang chạy (CLAUDE.md); riêng `gs001` đã từng được dựng từ nguồn (`docs-analysis/reports/35-bien-dich-server-tu-nguon.md`, PROBABLE vì tôi không dựng lại).

---

## 1. Sơ đồ thành phần (theo mã + CLAUDE.md)
```
 Client (Cocos2d-x 3.17.2, Android/Win)                 Gateway tree (SRV/gateway/Sources)
 ┌────────────────────────────────┐                      ┌───────────────────────────────────┐
 │ AppDelegate → KUpdateLayerVN   │   TCP (CSocketClient │ MultiServer/Bishop  (login, chọn  │
 │   → login/chọn server (Ksel*)  │   + KSG_DecodeEncode)│   game server, SmartClient)       │
 │   → KgameWorld(VN) + gamecore  │◄────────────────────►│ MultiServer/Goddess (DB nhân vật  │
 │ engine: KPakList/XPackFile     │                      │   DBTable, IDBRoleServer)         │
 │ CDN: data_cdn/*.pak, apk       │                      │ MultiServer/S3Relay (bang, bạn)   │
 └──────────────┬─────────────────┘                      │ Sword3PaySys/S3AccServer (tài     │
                │ HTTP tải PAK (KDownLoadFile)           │   khoản; MSSQL), S3RELAYSERVER    │
                ▼                                         └───────────────┬───────────────────┘
        htdocs_send / data_cdn (máy chủ web tĩnh)                         │ nội bộ (relay_PROTOCOL)
                                                         ┌────────────────▼──────────────────┐
                                                         │ SRV/gameserver MultiServer/        │
                                                         │   GameServer (KSOServer) = gs001   │
                                                         │   Core/Src (KNpc, KPlayer, ...)    │
                                                         │   Lua script (RUNTIME/gs/script)   │
                                                         └────────────────────────────────────┘
```
Bằng chứng từng khối:
- Client khởi động: `CLIENT/Classes/AppDelegate.cpp` `applicationDidFinishLaunching` → `KUpdateLayerVN::scene()` (VERIFIED, đã trích ở `CLIENT_SOURCE_INVENTORY.md`, tôi đọc lại đoạn 70–140).
- Mạng client: `CLIENT/Classes/network/` — `SocketClient.{h,cpp}` (`CSocketClient : CThread, CIOBuffer::Allocator`), `IOBuffer`, `Event`, `Thread`, `KSG_EncodeDecode`, `Cipher.h` (VERIFIED tên/lớp).
- Server lõi: `SRV/gameserver/Sources/MultiServer/GameServer/KSOServer.cpp` — vòng lặp trò chơi `GAME_FPS 18` (dòng 90), điều kiện chạy khung `nMes * m_nGameLoop <= m_Timer.GetElapse()*GAME_FPS` (dòng 1442), bản tin `SvrFPS` mỗi 1080 khung (dòng 1453–1460), điều kiện `m_nGameLoop & 0x01` trước đoạn gửi gói cho mọi client (dòng 4378, chưa đọc kỹ) — VERIFIED trong nguồn gốc. Các bản 36 Hz do `docs-analysis/patches` / báo cáo 43–46 là sửa đổi riêng, không có trong cây nguồn gốc (PROBABLE; tôi không diff).
- Gateway: các hàm `main`/`WinMain` ở `Bishop.cpp:96`, `Goddess.cpp:385`, `Intercessor.cpp:67`, `S3Relay.cpp:191`, `S3AccServer/main.cpp:85`, `S3RELAYSERVER/main.cpp:78`; game: `GameServer.cpp:141`, `Heaven.cpp:14`, `Rainbow.cpp:10` (trích từ kiểm kê; không kiểm lại).
- Lưu trữ: `Goddess/mysql_db.cpp:51` có `mysql_real_connect` và thư mục `Goddess/dbsql/kgc_mysql_database.cpp`; `Sword3PaySys/S3AccServer/S3PDB_MSSQLServer_Connection.cpp` dùng MSSQL (VERIFIED có file). **CLAUDE.md nói SQL Server chạy đầu tiên; mã Goddess lại có đường MySQL.** Động cơ CSDL mà Goddess dùng trong triển khai thật là UNKNOWN từ nguồn (phase 2: đọc **tên khóa** cấu hình, không đọc giá trị).
- Thứ tự khởi động đã chạy được (CLAUDE.md): SQL → `Sword3PaySys` → `Goddess` → `S3Relay` → `Bishop` → `gs001`. `S3RelayServer.exe` (khác `S3Relay`) cấm chạy.

## 2. Giao thức: lớp truyền tải
| Mục | Bằng chứng | Mức |
|---|---|---|
| Tin có kiểu `BYTE` (`PROTOCOL_MSG_TYPE`), giới hạn `MAX_PROTOCOL_NUM 249` | `CLIENT/Classes/gamecore/KProtocol.h` | VERIFIED |
| Struct payload dùng `#pragma pack(1)` | `KProtocol.h` đầu file | VERIFIED |
| Mã hóa: XOR từng khối 4 byte với khóa 32-bit; phần dư XOR từng byte; khóa sau mỗi gói = `key*31 + 134775813` | `CLIENT/Classes/network/KSG_EncodeDecode.cpp` `KSG_DecodeEncode` | VERIFIED. Đây là **làm rối**, không phải mật mã; biết khóa khởi tạo là giải được toàn bộ |
| Cách trao khóa ban đầu | chưa đọc `ClientStage.cpp`, `Bishop/SmartClient.cpp` | UNKNOWN |
| Truy cập con trỏ `unsigned int*` trên bộ đệm byte (`*puBuf++ ^= uKey`) | `KSG_DecodeEncode` | VERIFIED; với `-fstrict-aliasing` ở CMake release (`CLIENT/CMakeLists.txt:814-815`) và ARM32 là rủi ro UB/căn lề (PROBABLE) |

## 3. Giao thức: bảng ID (so khớp mã nguồn)
Script: `scripts/protocol_enum_compare.py`. Giá trị enumerator = vị trí trong enum (đã tính `= N`), bỏ comment.
Các file: client `CLIENT/Classes/gamecore/KProtocolDef.h`; server `SRV/gameserver/Headers/KProtocolDef.h`, `SRV/gateway/Headers/KProtocolDef.h`.

| Họ | client vs gameserver | client vs gateway |
|---|---|---|
| `s2c_PROTOCOL` | **ID giống hệt** | giống hệt |
| `c2s_PROTOCOL` | **ID giống hệt**; chỉ khác **tên** `c2s_login` (client) ↔ `c2s_login_fhgyrinhkmvnsheypo` (server) | 155 mục đầu giống hệt; từ vị trí 155 hai bên khác nhau (client `c2s_gm_synroleaction`, gateway `_c2s_begin_relay`), gateway ngắn hơn 4 mục (163 so với 167). Gateway không xử lý các gói game của client nên có thể vô hại — PROBABLE, chưa kiểm |
| `c2c_PROTOCOL`, `gm_PROTOCOL`, `playercomm_PROTOCOL` | giống hệt | giống hệt |
| `relay_PROTOCOL` | server có thêm `relay_c2c_remote`, `relay_s2c_udateserver`, `relay_s2c_udatemaps` (làm dịch giá trị `relay_s2c_loseway`: 35 → 36). Đây là họ **chỉ giữa server và relay** (comment trong file) nên client không bị ảnh hưởng | cùng |
| `chat_PROTOCOL` | server có thêm 4 mục **ở cuối** (`chat_coretask`, `chat_caoritemtime`, `chat_coreitemdata`, `chat_goldthread`) nên mục cũ không dịch | cùng |

- Kết luận: tên giao thức đăng nhập bị đổi tên ở server nhưng ID không đổi (VERIFIED) — nếu nâng cấp lại client/server từ mã nguồn thì sửa `c2s_login` ở một bên sẽ không phá giao thức.
- **Phạm vi chưa kiểm:** (a) `KProtocol.h` (struct payload): 538 dòng khác sau chuẩn hóa so với gameserver, phần lớn là include/comment; chưa so sánh `sizeof`/layout từng struct (UNKNOWN). (b) `KRelayProtocol.h`, `KTongProtocol.h`. (c) hai họ `s2c_PROTOCOL`/`c2s_PROTOCOL` có phần khai báo gán tường minh (`= 32`, `= 48`, `= g_nGlobalProtocolType`) — đã tính trong script, nhưng ký hiệu `g_nGlobalProtocolType` được coi như cùng giá trị ở hai phía; chưa kiểm hằng số.

## 4. Quản lý đối tượng trò chơi (bản đồ chức năng)
| Miền | Client | Server | Mức |
|---|---|---|---|
| Người chơi | `gamecore/KPlayer.cpp` (5.804 dòng), `KPlayerTask`, `KPlayerTrade`, `KPlayerPK`, `KPlayerFaction` | `Core/Src/KPlayer.cpp`, `KPlayerSet` | VERIFIED tồn tại; hành vi đồng bộ UNKNOWN |
| NPC/quái | `KNpc.cpp` (11.385 dòng), `KNpcAI.cpp`, `KNpcRes.cpp` (2.992), `KNpcTemplate.cpp` | `Core/Src/KNpc.cpp`, `KNpcAI.cpp`, `KNpcFindPath.cpp`, `KNpcDeathCalcExp.cpp` | VERIFIED. Phân biệt NPC và quái (loại) = UNKNOWN |
| Bản đồ/vùng | `KSubWorld.cpp` (1.648), `KRegion.cpp`, `gamescene/KScenePlaceC.cpp`, `KScenePlaceRegionC.cpp` | `Core/Src/KSubWorld.cpp`, `KRegion.cpp` | VERIFIED; cấu trúc `.wor` UNKNOWN |
| Vật phẩm | `KItem.cpp`, `KInventory.cpp`, `KItemList.cpp` | `KItem.cpp`, `KItemGenerator.CPP`, `KItemSet.cpp`, `KDropScript.cpp`, `KBuySell.cpp` | VERIFIED |
| Kỹ năng/đạn | `KSkills.cpp`, `KSkillManager.cpp`, `KMissle.cpp`, `KMissleRes.cpp` | `KFightSkill.cpp`, `KMissleSkill.cpp`, `KMissle.cpp` | VERIFIED |
| Trò chơi GM | — | `KGMCommand.cpp`, `KGMProcess.cpp` | VERIFIED tồn tại; **không dùng** theo CLAUDE.md |
| Script | — | Lua (`RUNTIME/gs/script`, 4.030 file `.lua` toàn kho), `KScript*`, `KLuaScript.cpp` | VERIFIED số lượng; nội dung UNKNOWN |

Các mô-đun trùng tên (`KNpc`, `KSubWorld`, `KMissle`, …) tồn tại **hai bản** (client và server) và đã phân kỳ (client có `Res`, `Draw`; server có AI và tính toán). Dùng chung mã giữa hai bên: PROBABLE qua `Core/Src` nhưng chưa kiểm cây tập tin chung.

## 5. Dữ liệu dùng chung client ↔ server (cần đồng bộ)
| Dữ liệu | Client | Server | Rủi ro |
|---|---|---|---|
| Bảng thiết lập (`.ini`, `.txt`, TAB) | `setting*.pak`, `data/*` | `RUNTIME/gs/Settings` | Lệch phiên bản gây lỗi hiển thị/tính toán — UNKNOWN mức đồng bộ |
| Danh mục bản đồ | `map.pak`, `mapfix.pak` | `RUNTIME/gs/maps`, `Settings/MapList.ini`, `maps*.pak` (`.wor`) | CLAUDE.md: 28 bản đồ `gs001` thiếu `.wor` — chưa kiểm lại |
| Script Lua phía client | `script*.pak` | `gs/script` | UNKNOWN |
| Địa chỉ server gửi cho client | — | `gs00N_cfg.ini [GameServer] Ip`, đọc ở `KSOServer.cpp` (CLAUDE.md) | Cấu hình, không ghi giá trị |
| Danh sách PAK | `data/data/paklist.ini`, `Resources/paklist.ini` | CDN `data_cdn/data/paklist.ini` | Ba bản; chưa so khớp (chứa khóa nhạy cảm) |

## 6. Cái gì có thể tái sử dụng (đánh giá)
- **Cao:** định dạng PAK/hash đường dẫn (độc lập, khoảng 1.700 dòng: `KPakFile` 675 + `KPakList` 315 + `XPackFile` 741), ID giao thức (đã đồng nhất), `Core/Src` (logic chơi).
- **Trung bình:** `engine/` (I/O, bảng, Lua, bộ nhớ) vì kiểu C cổ và chặn Win32/pthread xen kẽ.
- **Thấp:** `vn/` (bản sao UI tiếng Việt, 131 file song song với `gameui/` 174 file) — trùng lặp lớn.
- **Cần nghiên cứu thêm:** `Heaven`/`Rainbow` (vai trò thực chưa rõ), `Intercessor`, `S3RELAYSERVER` (cấm chạy).
