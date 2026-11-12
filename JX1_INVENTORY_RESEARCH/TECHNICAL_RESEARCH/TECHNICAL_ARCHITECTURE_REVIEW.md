# TECHNICAL_ARCHITECTURE_REVIEW — Đánh giá kiến trúc client và server

Phase 1.5 (nghiên cứu, chỉ đọc). Ngày 2026-11-12.
Nhãn: **VERIFIED · PROBABLE · UNKNOWN · BLOCKED**. `CLIENT` = `Folder/Client2912-20260116T044348Z-3-001/Client2912/Client`; `SRV` = `SwordOnline/SwordOnline/jxOnline`.
Không build, không chạy, không đo trên thiết bị. Số dòng do `wc -l` / `cat | wc -l` trên cây nguồn (không tính LuaLib, MySql, ipch, x64, Release).

## TÓM TẮT 5 DÒNG
1. Client là ứng dụng **Cocos2d-x 3.17.2 dùng như lớp cửa sổ/GL**; toàn bộ game (thế giới, NPC, kỹ năng, UI, mạng, tài nguyên) là mã C++ cổ kiểu Kingsoft/Windows (2003) được chuyển sang Android.
2. Tài nguyên không đi qua hệ thống asset của Cocos mà qua **PAK tự chế + SPR (bảng màu + RLE)**, tra bằng hash tên đường dẫn; phần còn lại (PNG/OGG/TTF) nạp rời qua `FileUtils`.
3. Server là **hai cây mã Visual Studio** (gameserver ≈425 nghìn dòng, gateway ≈279 nghìn dòng) có chung họ giao thức với client; ID giao thức hai phía đã khớp (`CLIENT_SERVER_DEPENDENCY_MAP.md`).
4. Điểm yếu lớn nhất: tệp khổng lồ (`KgameWorld.cpp` 15.397 dòng, `KNpc.cpp` 11.385 dòng), mã vẽ gắn chặt logic, giải nén PAK không giới hạn đầu ra, tải PAK qua CDN mà không kiểm tra CRC.
5. Chưa biết: đường render thật trên thiết bị, cách trao khóa mạng, cấu trúc `.wor`, mã giải RLE SPR, và mã nguồn server có khớp exe đang chạy hay không.

---

## A. KIẾN TRÚC CLIENT

### A1. Cấu trúc và mô-đun — VERIFIED
`CLIENT/Classes` (thống kê từ `CLIENT_SOURCE_INVENTORY.md`, kiểm lại bằng `wc -l`):

| Mô-đun | Vai trò (bằng chứng) |
|---|---|
| `engine` (213 file) | I/O, PAK (`XPackFile`, `KPakList`, `KPakFile`), codec (`KCodec`, `KCodecLzo`, `ucl/`), Lua (`KLuaScript`, `lualib/`), INI/TAB (`KIniFile`, `KTabFile`), bộ nhớ (`KMem*`), tải file (`KDownLoadFile`) |
| `gamecore` (157) | `KPlayer` (5.804 dòng), `KNpc` (11.385), `KNpcRes` (2.992), `KSubWorld`, `KRegion`, `KItem`, `KSkills`, `KMissle`, `KProtocolProcess` (5.355), `KProtocol(Def).h` |
| `gamescene` (29) | `KgameWorld` (15.397), `KUpdateLayer` (1.379), `KScenePlaceC`, `KScenePlaceRegionC` |
| `gameui` (174) / `vn` (131) | UI game; `vn/` là bản UI/scene tiếng Việt song song (`KgameWorldVN` 7.134 dòng, `KUpdateLayerVN` 428) |
| `ImageStore` | `KImageStore2` (754 dòng): kho ảnh, giải khung SPR, cân bằng bộ nhớ |
| `network` | `SocketClient`, `IOBuffer`, `KSG_EncodeDecode`, `ClientStage` |
| `manager`, `tools` | tiện ích nhỏ |

Cocos2d-x: `CLIENT/cocos2d/CHANGELOG` cho 3.17.2; `CMakeLists.txt` thêm engine kèm theo (VERIFIED). Chỉ dùng lớp `Director`/`GLView`/`Scene`/`Layer`/`Sprite` (chi tiết sử dụng từng lớp: PROBABLE).

### A2. Luồng khởi chạy — VERIFIED (đoạn đã đọc) / PROBABLE (đoạn sau)
1. `AppDelegate::initGLContextAttrs`: RGBA8888, depth 24, stencil 8, **multisample = 3** (`AppDelegate.cpp`, đã đọc). Giá trị 3 không phải lũy thừa của 2; GPU/driver có thể bỏ qua hoặc làm chọn config khác — UNKNOWN trên thiết bị.
2. `applicationDidFinishLaunching`: tạo `GLView` (tên "jx1client_new" trên Android), `setProjection(_2D)`, `setDepthTest(false)`, `g_SetRootPath(NULL)` (non-Windows), `setAnimationInterval(1.0f/60)`, `setDesignResolutionSize(mediumResolutionSize, EXACT_FIT)`, khởi động `KUpdateLayerVN::scene()`.
3. `KUpdateLayerVN` / `KUpdateLayer` + `KDownLoadFile` tải danh sách PAK (`data/paklist.ini`), đọc `Resources/package.ini` (địa chỉ — nội dung BLOCKED) → `KPakList::Open` nạp tối đa 50 PAK.
4. Đăng nhập/chọn server/chọn nhân vật: `gameui/Klogin*.cpp`, `KuiSelserver.cpp`, `KuiSelPlayer_new.cpp`, `KSelPlayer.cpp` (CLAUDE.md và nguồn).
5. Vào game: `gamescene/KgameWorld.cpp` (+ `vn/gamescence/KgameWorldVN.cpp`); `mianSkillCallback` → `gamecore/KNpcAI.cpp mainSkillattack` (CLAUDE.md).
Đoạn 3–5: tôi xác nhận **tên hàm và tệp**, chưa đọc từng nhánh; PROBABLE.

### A3. Render, camera, animation, UI
- **Render 2D thuần**: `setProjection(_2D)`, tắt depth test (VERIFIED). Thế giới được dựng bằng **cây đối tượng riêng** của game (`KScenePlaceC`, `KScenePlaceRegionC`, `CoreDrawGameObj.cpp`, `KRUImage.h`) rồi vẽ qua Cocos; không dùng `TMXTiledMap`/`Camera` của Cocos — PROBABLE (chưa grep toàn diện; tìm thấy `SpriteFrameCache`, `SpriteBatchNode`, `TextureCache` trong kiểm kê).
- **Camera = tiêu điểm vùng**: `KScenePlaceC::SetFocusPosition` đổi vùng xử lý và gọi `ChangeProcessArea`/`Preprocess` (đã khảo sát ở phase 47: hiện tượng biến mất đối tượng 53–59 ms khi đổi vùng; xem `docs-analysis/reports/47-*.md`, kiểm chứng trước đây, ngoài phạm vi phiên này).
- **Animation = khung SPR**: `SPRHEAD.Frames/Directions/nInterval` (đơn vị nhịp game, `KbugInfo.h`); khung RLE giải nén theo nhu cầu qua `KImageStore2::GetSprFrame` → bộ nhớ ảnh → texture. Đường chuyển RLE→texture: UNKNOWN (chưa đọc).
- **UI**: Hai lớp UI cạnh nhau (`gameui` 174 file, `vn` 131 file), phần lớn tài nguyên UI là SPR/PNG trong `ui/`, `Spr\Ui3\…`; bố trí đọc từ INI trong PAK (`\ui\ui3_800\uinewlogin\*.ini` — VERIFIED từ literal `Klogin.cpp:158`).
- **Độ phân giải**: `EXACT_FIT` — kéo giãn không giữ tỉ lệ nếu khung thiết bị khác tỉ lệ thiết kế. Đã có đo `curSalx = height/width` nhưng nhánh thay thế `ResolutionPolicy::FIXED…` đã bị comment (VERIFIED). Ảnh hưởng chất lượng ảnh trên màn hình tỉ lệ khác: PROBABLE, chưa chụp.

### A4. Hệ thống tài nguyên — VERIFIED
Chi tiết ở `ASSET_FORMAT_RESEARCH.md`. Tóm tắt: `KPakFile::Open/Read` → `g_pPakList->pGetFilePath` → `XPackFile::XFindElemFile` (nhị phân) → `ReadElemFile`/`ExtractRead` (nrv2b/nrv2d/nrv2e) → `KImageStore2`.

### A5. Thành phần gameplay đã xác định — VERIFIED (có mặt) / UNKNOWN (hành vi)
Map/world, NPC + AI, người chơi, vật phẩm/hành trang, nhiệm vụ, môn phái, giao dịch, nhóm, PK, kỹ năng/đạn, âm nhạc bản đồ (`KMapMusic.cpp`), tự đánh (`KuiAutoPlay`, CLAUDE.md), GM (phía server `KGMCommand.cpp`). Tôi không đọc hành vi từng hệ thống trong phase này.

### A6. Thành phần quan trọng chưa làm rõ — UNKNOWN
1. Đường chuyển SPR RLE → texture (bộ nhớ CPU, định dạng pixel, tạo texture mỗi khung hay gộp atlas).
2. Cách nạp bản đồ client (`.map`/`.wor`/cấu trúc ô) và quy tắc tải theo vùng.
3. Trao khóa/thủ tục bắt tay mạng (`ClientStage.cpp`, `Bishop/SmartClient.cpp`).
4. `dataChecksum.cpp`, `KSG_MD5_String.cpp`: dùng để làm gì (có thể là kiểm tra toàn vẹn nhưng không được gọi trong `XPackFile::Open`).
5. Vòng đời cache/giải phóng bộ nhớ: `XPackFile::FreeElemCache` có lệnh `free` bị comment, `KImageStore2::CheckBalance`.
6. Lý do multisample = 3 và hiệu quả `-ffast-math -flto` ở cấu hình CMake Release (`CLIENT/CMakeLists.txt:814-815`).

---

## B. KIẾN TRÚC SERVER

### B1. Hai cây dự án — VERIFIED
- `SRV/gameserver/Sources`: `Core` (247 file nguồn trong `Core/Src`), `Engine`, `MultiServer/{GameServer,Heaven,Rainbow,Common,Protocol}`, `Library/LuaLib`, `MySql`, `FilterText`, `AutoUpdateRes`. 11 `.vcxproj`. ≈ **425.463 dòng** C/C++/H (không tính LuaLib, MySql, build output).
- `SRV/gateway/Sources`: `MultiServer/{Bishop,Goddess,Heaven,Intercessor,Rainbow,S3Relay,Common,Protocol}`, `Sword3PaySys/{S3AccServer,S3RELAYSERVER,S3DBClient,S3AccClientSample,Toolkits}`, `Common`, `Engine`, `Library/LuaLib`, `MySql`. 17 `.vcxproj`. ≈ **279.231 dòng**.
- Hai cây có sẵn bản sao riêng của `Engine`, `FilterText`, `Library/LuaLib`, `MySql`, `Protocol` (trùng lặp, đồng bộ bằng tay). Mức chênh giữa các bản sao: UNKNOWN (chưa diff; riêng `KProtocolDef.h` đã khác nhau nhẹ — xem dependency map).
- Cây nguồn lẫn sản phẩm build (`.obj`, `.pdb`, `.ipch`, `.sbr`…): VERIFIED theo kiểm kê (hàng trăm MB).

### B2. gameserver ↔ gateway — VERIFIED (cấu trúc) / PROBABLE (luồng)
Thứ tự khởi động và vai trò: xem `CLIENT_SERVER_DEPENDENCY_MAP.md` mục 1. Gameserver không tự đăng nhập: nó nhận người chơi do Bishop/Goddess/Paysys xác thực (CLAUDE.md "Đăng nhập, vào game"). `S3Relay` quản lý bang hội/bạn bè.

### B3. Vòng lặp trò chơi — VERIFIED (gốc)
`KSOServer.cpp`: `GAME_FPS 18` (dòng 90); bước khung khi `nMes * m_nGameLoop <= m_Timer.GetElapse()*GAME_FPS` (1442); `m_nGameLoop` reset ở 1.512.000 khung (1433–1435, ≈ 23 giờ ở 18 Hz); in `SvrFPS` mỗi 1080 khung = 60 giây (1453–1460); có điều kiện `m_nGameLoop & 0x01` trước đoạn gửi gói cho mọi client (4378; ý nghĩa chính xác chưa đọc kỹ — UNKNOWN). Bản 36 Hz đã dùng ở VM thử (báo cáo 43–46) là chỉnh sửa không nằm trong cây này (PROBABLE).

### B4. Cơ sở dữ liệu — PROBABLE / UNKNOWN
Có đường MySQL (`Goddess/mysql_db.cpp`, `dbsql/kgc_mysql_database.cpp`) và MSSQL (`S3PDB_MSSQLServer_Connection.cpp`). Động cơ Goddess dùng ở triển khai thật: UNKNOWN từ nguồn (CLAUDE.md nói SQL Server chạy đầu tiên).

### B5. Quản lý nội dung: người chơi, bản đồ, NPC, quái, vật phẩm, kỹ năng — VERIFIED (có mặt)
Theo bảng ở `CLIENT_SERVER_DEPENDENCY_MAP.md` mục 4. Dữ liệu game nằm ngoài mã (INI/TAB/Lua trong `RUNTIME/gs`), nên "có bao nhiêu quái/vật phẩm" cần kiểm dữ liệu chứ không phải mã (UNKNOWN).

### B6. Tái sử dụng / cần nghiên cứu
Tái sử dụng tốt: `Core/Src` (logic), bảng giao thức, `LuaLib` (nhưng phiên bản Lua UNKNOWN). Cần nghiên cứu: `Heaven`, `Rainbow`, `Intercessor`, `AutoUpdateRes`, `FilterText`.

---

## C. ĐÁNH GIÁ CHẤT LƯỢNG NGUỒN

### C1. Hoàn chỉnh — VERIFIED
Client và `gs001` có đường biên dịch thật (Gradle+CMake 3.30.5, NDK 25.2.9519653; `gs001` dựng từ nguồn theo báo cáo 35 — PROBABLE vì tôi không dựng lại). Các giao thức, PAK, SPR có đầy đủ tại mã.

### C2. Thiếu/chưa xác định
- Không tìm thấy mã sinh/ghi PAK ở client (chỉ đọc). Công cụ ghi nằm trong `docs-analysis/tools` (dự án sau này), không phải nguồn gốc.
- 28 bản đồ `gs001` thiếu `.wor` (CLAUDE.md, chưa kiểm).
- `ASSET_REFERENCE_COVERAGE` còn 101 literal không giải thích (xem `ASSET_FORMAT_RESEARCH.md`).

### C3. Mã cũ, thư viện bên thứ ba, rủi ro bảo trì
1. **Tệp khổng lồ:** `KgameWorld.cpp` 15.397 dòng, `KNpc.cpp` 11.385, `KgameWorldVN.cpp` 7.134, `KPlayer.cpp` 5.804 (VERIFIED). Bảo trì khó, khó kiểm thử.
2. **Trùng lặp lớn** `gameui` ↔ `vn` (174 ↔ 131 file) và hai cây server.
3. **Kiểu viết 2003:** macro Win32 (`CRITICAL_SECTION`, `ZeroMemory`, `DWORD`) giả lập trên Android; `fopen/fseek` với `long`/`unsigned int` (giới hạn 2–4 GB, đủ cho các PAK hiện có — PAK lớn nhất ≈1,04 GB); khối mã comment chiếm tỉ lệ cao (`XPackFile.cpp`, `KPakList.cpp`).
4. **Mã hóa nguồn lẫn lộn:** nhiều file GBK, một số UTF-8, một số UTF-8 hỏng (literal tiếng Trung thành `??`) — 20 literal đường dẫn không thể hash.
5. **Bên thứ ba bundle:** Cocos2d-x 3.17.2 (cũ; hỗ trợ Android 34 phải kiểm), OpenSSL/curl/zlib/libpng/libjpeg/FreeType/websockets/FMOD… trong `cocos2d/external` — phiên bản từng thư viện UNKNOWN; rủi ro CVE là có thể xảy ra, chưa đánh giá.
6. **Cờ trình biên dịch mạo hiểm:** Release CMake `-O3 -flto -ffast-math -fstrict-aliasing` (`CMakeLists.txt:814-815`) trên mã có ép kiểu con trỏ (mã hóa mạng, header SPR) — PROBABLE rủi ro hành vi không xác định.
7. **Bộ build cũ:** ba hệ (ndk-build `Android.mk`/`Application*.mk`, CMake, Xcode) cùng tồn tại; cái đang dùng: CMake (`PROP_BUILD_TYPE=cmake`), VERIFIED.
8. **Bảo mật dữ liệu/kho mã:** tệp SQL dữ liệu tài khoản [tên đã ẩn] và dump trong lịch sử git (CLAUDE.md); `paklist.ini` chứa khóa mờ (`accinfo`, `accpint`) — giá trị không ghi lại ở đây.
9. **Lỗi cụ thể đã xác nhận trong mã (PAK):** `FileNameToId` (`&&` thay vì `||`), giải nén không chặn tràn, không kiểm CRC, chỉ mục không sắp xếp trong `updata01.pak`.

### C4. Ảnh hưởng hiệu năng, chất lượng hình ảnh, mở rộng
| Chủ đề | Quan sát | Mức |
|---|---|---|
| Nhịp client | 1/60 s yêu cầu (`AppDelegate`), thực đo ≈60 trên LDPlayer (ngoài phạm vi, từ phase trước) | PROBABLE |
| Nhịp server | 18 Hz gốc; 36 Hz là bản sửa | VERIFIED gốc |
| Giải RLE trên CPU, tạo texture theo khung | Chưa đọc `KImageStore2::LoadImage`; có `CheckBalance` nên có cơ chế giải phóng | UNKNOWN |
| Giải nén `nrv2b` đồng bộ trong luồng nạp | `XPackFile::ReadElemFile` cấp phát và giải nén ngay trên luồng gọi, khóa `m_ReadCritical` | VERIFIED |
| Cache PAK chỉ 10 phần tử (`MAX_XPACKFILE_CACHE`) | nhỏ so với 154.098 mục | VERIFIED số, tác động UNKNOWN |
| Hình ảnh | `EXACT_FIT`, MSAA yêu cầu 3, ảnh SPR ≤256 màu | PROBABLE giới hạn chất lượng |
| Mở rộng server | Mô hình mỗi gs001 một tiến trình, bộ nhớ ≈6,8 GB (phase 48, ngoài phạm vi) | PROBABLE |

---

## D. KẾT LUẬN CHUNG
Mã nguồn đủ để dựng và vận hành, nhưng là **bản chuyển cổ từ Windows**. Hai bài toán chính của dự án hiện tại — độ mượt và chất lượng ảnh — đều đi qua phần mã **chưa được đọc** (`KImageStore2::LoadImage`, đường vẽ `KScenePlaceC`/`CoreDrawGameObj`). Đọc hai phần đó và so khớp struct giao thức là việc có giá trị cao nhất cho Phase 2 (`PHASE_2_RESEARCH_PLAN.md`).
