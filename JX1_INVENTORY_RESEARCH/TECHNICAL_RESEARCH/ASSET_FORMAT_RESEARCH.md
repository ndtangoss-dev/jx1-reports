# ASSET_FORMAT_RESEARCH — Định dạng PAK/SPR và cơ chế truy cập tài nguyên

Phase 1.5 (nghiên cứu, chỉ đọc). Ngày: 2026-11-12.
Nhãn: **VERIFIED** (đã kiểm chứng trực tiếp) · **PROBABLE** · **UNKNOWN** · **BLOCKED**.
Viết tắt: `CLIENT` = `Folder/Client2912-20260116T044348Z-3-001/Client2912/Client`; `SRV` = `SwordOnline/SwordOnline/jxOnline`.
Mọi con số "đo" dưới đây do script chỉ-đọc trong `C:\Jx1CocoV3_RESEARCH\scripts` tạo ra; dữ liệu thô ở `C:\Jx1CocoV3_RESEARCH\data`.

## TÓM TẮT
1. Định dạng PAK đã được giải mã đầy đủ từ mã nguồn client và **đối chiếu với 40 file PAK thật**: cả 40 file có header hợp lệ, bảng chỉ mục nằm trong file, 0 mục vượt biên.
2. PAK **không lưu tên file**. Chỉ mục chứa `uId` 32-bit là hash của đường dẫn đã chuẩn hóa. Muốn biết "file X có trong PAK không" phải tính hash của X rồi tra bảng, không thể liệt kê tên.
3. Cài đặt lại hàm hash bằng Python khớp bảng chỉ mục thật: 649/1113 literal trong mã nguồn tìm thấy trong chỉ mục (xác suất trùng ngẫu nhiên kỳ vọng ≈ 0,04 mục), nên cách tính hash là đúng.
4. 815 literal "UNRESOLVED" của báo cáo kiểm kê **không có nghĩa là thiếu**. Đối chiếu lại với cơ chế nạp thực tế: phần lớn có lời giải (xem mục 5).
5. Chưa giải nén nội dung, chưa giải mã khung SPR. Nội dung bên trong từng mục là UNKNOWN.

---

## 1. Container PAK

**Nguồn:** `CLIENT/Classes/engine/KbugInfo.h` (struct `XPackFileHeader`, `XPackIndexInfo`, enum `XPACK_METHOD`), `XPackFile.cpp` (`Open`, `XFindElemFileA`, `XFindElemFile`, `ReadElemFile`, `ExtractRead`), `KPakList.cpp` (`Open`, `pFindElemFile`, `pGetFilePath`, `pFindElemFileA`), `KFilePath.cpp` (`g_FileName2Id`, `g_CheckFileExist`, `g_GetPackPath`).

### 1.1 Bố cục byte (little-endian) — VERIFIED
```
Header (32 byte)   XPackFileHeader
  +0  char[4]  "PACK"  (0x4B434150)
  +4  u32      uCount             số mục
  +8  u32      uIndexTableOffset  vị trí bảng chỉ mục
  +12 u32      uDataOffset
  +16 u32      uCrc32             (trường có, XPackFile::Open KHÔNG kiểm tra)
  +20 u32      uPakTime           time()
  +24 byte[8]  reserved
Index (uCount × 16 byte)  XPackIndexInfo
  u32 uId            hash đường dẫn (xem 1.2)
  u32 uOffset        vị trí dữ liệu trong file
  i32 lSize          kích thước gốc sau giải nén
  i32 lCompressSizeFlag   byte cao = kiểu nén, 24 bit thấp = kích thước nén
```
- Kiểm chứng trên dữ liệu: `pak_index_summary.csv` — 40/40 file `status=OK`, tổng 169.999 mục, tổng 3.406.000.554 byte, `entries_out_of_bounds=0` ở mọi file.
- Hệ quả: kích thước nén tối đa mỗi mục = 2^24−1 (16 MiB) vì `ReadElemFile` lấy `flag & ~0xFF000000`. Mục lớn hơn phải lưu dạng khác (VERIFIED từ mã; chưa kiểm tra mục nào chạm giới hạn).

### 1.2 Hash đường dẫn → `uId` — VERIFIED
`g_FileName2Id` (`KFilePath.cpp`) và `g_CheckFileExist` (cùng file; nhánh `GAME_RUN_MOBILE` dùng đúng công thức này):
```
id = 0
for i, ch in enumerate(path):          # ch là char CÓ DẤU
    id = ((id + (i+1)*ch) mod 2^32) % 0x8000000B
    id = (id * 0xFFFFFFEF) mod 2^32
return id ^ 0x12345678
```
- Chuẩn hóa trước khi hash (`g_GetPackPath`): bỏ **một** dấu `\` hoặc `/` đầu, `RemoveAllPointPath` (xử lý `.`/`..`), hạ chữ thường **chỉ ASCII** (`g_StrLower`, `KStrBase.cpp`), rồi `KPakList::pFindElemFile` thêm tiền tố `\`. Dấu `/` **không** được đổi sang `\`.
- `char` có dấu là điều kiện bắt buộc cho tên có byte ≥0x80 (tiếng Trung GBK). Bản build đang dùng là CMake (`proj.android/gradle.properties` có `PROP_BUILD_TYPE=cmake`) và `proj.android/app/build.gradle:47` truyền `cppFlags "-frtti -fexceptions -fsigned-char"` — VERIFIED cờ có mặt. Ảnh hưởng thực tế trên thiết bị: chưa đo (PROBABLE đúng vì game chạy được).
- Có ba lần thử mã hóa: `KPakList::pGetFilePath` với `TYPE_CONVER_ALL` thử byte gốc → `U2G` → `G2U` (VERIFIED). Báo cáo kiểm kê đọc literal với mã hóa khác nên sinh mojibake.

### 1.3 Tra cứu — VERIFIED
- `KPakList::Open` đọc `[Package] Path` rồi các khóa `0..49` (`MAX_PAK = 50`, `KPakList.h:44`); mỗi mục `N=ten.pak` được mở bằng `XPackFile::Open`; mục mở lỗi bị **bỏ qua im lặng**.
- `pFindElemFileA` duyệt PAK **theo thứ tự `paklist`**, PAK đầu tiên có `uId` thắng. Trước đó `XFindElemFile` còn tra bộ đệm tĩnh dùng chung (`MAX_XPACKFILE_CACHE = 10`).
- Trong từng PAK, `XFindElemFileA` là **tìm nhị phân** trên `uId` (không dấu). Cần bảng chỉ mục đã sắp xếp.
- Thứ tự `paklist` thật (`data_cdn/data/paklist.ini`, chỉ đọc phần `pak_N=`): 0 updata01, 1 updata02, 2 updata03, 3 updata06, 4 updata07, 5 updata09, 6 slistcl, 7 freeresource, 8 slistcache, 9 slist, 10 serlst, 11 serverlist, 12 skills, 13 image2, 14 image1, 15 setting, 16 resource, 17 ui, 18 script, 19 font, 20 sound, 21 spr, 22 map, 23 update, 24 vltk, 25 updata08, 26 mapfix, 27 volam01, 28 volam00, 29 test, 30 dyshop, 31 update_music, 32 update10, 33 musiclist.txt (không phải PAK), 34 script_skill. Tiêu đề `count=35;32`.
- **Ghi chú:** file này còn hai khóa `accinfo`/`accpint` có giá trị dạng chuỗi mờ. Giá trị **không** được ghi vào báo cáo (nhạy cảm tiềm năng). Xem `INVENTORY_GAPS_AND_RISKS.md`.

### 1.4 Nén — VERIFIED (mã) + đếm (dữ liệu)
`XPackFile::ExtractRead`:

| Cờ (byte cao) | Tên trong enum | Thực tế mã gọi |
|---|---|---|
| 0x00 | `TYPE_NONE` | đọc thẳng |
| 0x01 (`UCL_OLD`), 0x02 (`BZIP2_OLD`), 0x20 (`BZIP2`), 0x10 (`UCL`) | tên gây hiểu nhầm | **cùng một giải thuật `ucl_nrv2b_decompress_8`** (không có bzip2 nào) |
| 0x03/0x30 | `FRAGMENT(_OLD)` | `ucl_nrv2d_decompress_8` |
| 0x04/0x40 | `FRAGMENTA(_OLD)` | `ucl_nrv2e_decompress_8` |
| cờ khác (ví dụ 0x11) | — | rơi vào nhánh "new pack" cuối: lại `nrv2b` |

- Đếm trên dữ liệu thật: mọi PAK chỉ dùng `NONE`, `UCL_OLD`(0x01), `BZIP2`(0x20), `UCL/FRAME`(0x10, chỉ 1 mục trong `script-new` và 1 trong `update10`) và `0x11` (tổng 189 mục: image1 4, image2 41, resource 60, script_skill 7, skills 23, spr 43, updata06 11). Không thấy cờ FRAGMENT 0x03/0x04/0x30/0x40.
- Thư viện UCL nằm trong `CLIENT/Classes/engine/ucl/`. Cần một bộ giải nén `nrv2b` độc lập để đọc nội dung (BLOCKED trong phase này vì quy tắc "không giải nén").

### 1.5 Bất thường của chỉ mục — VERIFIED (dữ liệu)
- `map.pak`(1 id trùng), `uinew.pak`(10), `updata01.pak`(312), `updata02.pak`(4), `updata03.pak`(1) có `uId` trùng nhau trong cùng file.
- **`updata01.pak` không sắp xếp tăng dần**: 1424 mục, 3 chỗ giảm (tại vị trí 1398, 1412, 1421) tức là bảng gồm 4 đoạn đã sắp riêng. Hệ quả với `XFindElemFileA` (tìm nhị phân): các id ở đoạn sau có thể **không tìm thấy** — PROBABLE (phụ thuộc id nào thực sự được yêu cầu; chưa kiểm tra).
- Trùng giữa PAK: 10.682 `uId` xuất hiện ở hơn một PAK (kể cả 6 PAK không có trong `paklist`). Thứ tự `paklist` quyết định bản nào hiển thị (VERIFIED từ mã) — các PAK `updata01..09` đứng đầu danh sách nên ghi đè bản cơ sở.
- 6 PAK có trên CDN nhưng **không có trong `paklist`**: `script-new`, `setting-new`, `sound-old`, `sound-old1`, `uinew`, `update10-pc`. Mã client không tham chiếu tên nào trong số này (chỉ có `update.pak` 3 lần). Việc chúng có được dùng hay không là UNKNOWN (có thể `paklist` khác được tải lúc chạy; `Resources/paklist.ini` và `data/data/paklist.ini` chưa so sánh vì nội dung chứa khóa nhạy cảm).
- `sound.pak`, `sound-old.pak`, `sound-old1.pak` trùng SHA-256 (kiểm kê). Chỉ `sound.pak` nằm trong `paklist`.

## 2. Định dạng SPR (ảnh/hoạt ảnh) — PROBABLE (đọc cấu trúc, chưa giải mã khung)
Nguồn: `KbugInfo.h` (`SPRHEAD`, `SPROFFS`, `SPRFRAME`, `SPR_COMMENT_FLAG`), `KPakFile.cpp` (`SprGetHeader`), `XPackFile::GetSprHeader/GetSprFrame`, `ImageStore/KImageStore2.cpp`.
- Header 32 byte: `"SPR\0"`, `Width`, `Height`, `CenterX`, `CenterY`, `Frames`, `Colors`(≤256), `Directions`, `nInterval`, `Reserved[6]` (VERIFIED từ struct). `Reserved[0]` được client ghi đè bằng chỉ số PAK (`PAK_INDEX_STORE_IN_RESERVED`) — VERIFIED.
- Sau header: bảng màu `Colors×3` byte, rồi bảng `SPROFFS{Offset,Length}` cho từng khung, rồi các khung `SPRFRAME{Width,Height,OffsetX,OffsetY,RLE…}` (VERIFIED từ `SprGetHeader`: `pOffsetTable = pSpr + sizeof(SPRHEAD) + Colors*3`).
- Ảnh là bảng màu (≤256 màu) + RLE. Chi tiết mã RLE/alpha và cách chuyển sang texture GL: UNKNOWN (chưa đọc `KSprControl.cpp`, `CoreDrawGameObj.cpp`).
- Cờ `TYPE_FRAME = 0x10000000` trùng giá trị `TYPE_UCL` (cùng `0x10000000`): cách phân biệt "nén theo từng khung" với "nén cả file" cho SPR là UNKNOWN (cần đọc `XPackFile::GetSprFrame` và `XPackSprFrameInfo`).
- Quản lý bộ nhớ ảnh: `KImageStore2` (`GetImage`, `GetSprFrame`, `LoadImage`, `CheckBalance`, `FreeImageObject`) cân bằng bộ nhớ theo số ảnh/ngưỡng (`SetBalanceParam`) — VERIFIED tên hàm; hành vi giải phóng là PROBABLE.
- Không có file `.spr/.ani/.dds/.pvr` rời nào trong cây nguồn (kiểm kê). Mọi SPR nằm trong PAK; `spr.pak` có 14.616 mục (VERIFIED), cộng thêm `image1/2`, `resource`, `update`, `updata*`.

## 3. Các định dạng khác
| Nhóm | Bằng chứng | Trạng thái |
|---|---|---|
| Ảnh Cocos rời PNG/JPG | `CLIENT/Resources` 646 PNG; nạp qua Cocos `TextureCache` | VERIFIED tồn tại |
| Phông | 20 TTF + `.fnt` trong `Resources/fonts`, `font.pak` (3 mục) | VERIFIED |
| Âm thanh | `Resources` 103 OGG; FMOD DLL trong thư mục client; `sound.pak` 416 mục; `update_music.pak` 41 mục | VERIFIED số lượng; nội dung UNKNOWN |
| Bản đồ client | `map.pak` 67.487 mục; `mapfix.pak` 1.828 mục | VERIFIED số mục; cấu trúc ô bản đồ UNKNOWN |
| Bản đồ server `.wor` | `gs\pak\maps*.pak` trong `_bin_v2_` (CLAUDE.md nêu 28 bản đồ thiếu `.wor`) | PROBABLE; chưa kiểm tra lại trong phase này |
| Script Lua | `script.pak`(683), `script-new.pak`(2.593), `script_skill.pak`(849), `setting*.pak` (INI/TAB) | VERIFIED số mục; nội dung UNKNOWN |
| FSB/BANK (FMOD) | 9 `.bank`, 2 `.fsb` rời | UNKNOWN phiên bản |

## 4. Đối chiếu literal ↔ cơ chế nạp
Script: `scripts/pak_index_probe.py` → `data/literal_pak_resolution.csv`, `scripts/residual.py` → `data/literal_classes.csv`.
Cách làm: trích mọi literal chuỗi trong 709 file nguồn client (đọc **byte thô**, không giải mã sai), bỏ escape `\\`, chuẩn hóa như `g_GetPackPath`, thử các biến thể mã hóa (gốc / `U2G` / `G2U` / UTF-8 mã hóa sai qua cp1252/latin-1), tính hash, tra trong chỉ mục của 40 PAK.

| Lớp | Số literal | Ý nghĩa | Mức |
|---|---:|---|---|
| A. `uId` có trong chỉ mục ít nhất một PAK | **649** | tồn tại mục có cùng hash | VERIFIED (hash), nội dung chưa xem |
| B. Chuỗi định dạng (`%d`, `%s`…) | 19 | tên được dựng lúc chạy | VERIFIED |
| C. Không có trong PAK nhưng cùng tên file tồn tại rời trong `Resources`/`data` | 321 | gần như chắc chắn nạp qua Cocos `FileUtils` (đường dẫn `ui/…`, `KgameWorld/…`, `fonts/…`) | PROBABLE (chỉ so tên file, không so đường dẫn) |
| D. Mảnh ghép (chỉ còn đuôi như `.png`, `.spr`) | 3 | nối chuỗi lúc chạy | VERIFIED |
| E. Literal hỏng trong nguồn (`?`, ký tự thay thế) | 20 | file nguồn đã mất byte tên; không thể hash | VERIFIED hỏng; tên thật UNKNOWN |
| F. Còn lại chưa giải thích | **101** | xem dưới | UNKNOWN |
| **Tổng** | **1113** | | |

- Số 1113 khác 1069 của kiểm kê vì cách trích khác (thêm đuôi `.plist/.fsh/.vsh/.pak/.wor/.map`, đọc byte thô, không đọc dòng nhạy cảm). Không so trực tiếp từng con số được; kết luận định tính giống nhau.
- Lớp F (101): chủ yếu tên **trần không đường dẫn**, ví dụ `cboDs1_start.ogg`, `HeroLogin.ogg`, `newysound1.ogg` (≈60 mục âm thanh), `ui/main/fan1.png`, `p_tips.plist` (14 lần tham chiếu), `/Music/Music001.mp3`, `fonts/msyh.ttf`, vài `\spr\Ui3\…\*.png` chưa tìm thấy. Nhiều khả năng là tên cộng thêm tiền tố thư mục lúc chạy (ví dụ `\sound\`) hoặc file được đưa vào thư mục khác; **chưa có bằng chứng thiếu**.
- Kết luận mức 815 UNRESOLVED: **không có literal nào được chứng minh là thiếu tài nguyên**. 649+19+321+3 = 992/1113 (≈89%) có lời giải hoặc lý do rõ ràng; 20 hỏng nguồn; 101 mở.

## 5. Mức độ có thể khai thác (đánh giá, không phải kết luận thiếu)
| Nhóm | Khả năng đọc | Rào cản |
|---|---|---|
| Liệt kê thành phần PAK theo tên | Thấp: chỉ có hash; cần danh sách tên ứng viên (từ nguồn, INI, TAB, Lua) | Phải dựng từ điển tên |
| Đọc nội dung (giải nén `nrv2b`) | Cao về kỹ thuật (thư viện UCL có trong nguồn) | BLOCKED bởi quy tắc phase này |
| Giải mã SPR → ảnh | Trung bình-cao (cấu trúc đã rõ) | Cần đọc mã RLE ở `KSprControl`/render, kiểm bằng ảnh mẫu |
| Bản đồ/`.wor` | Trung bình | Định dạng chưa đọc |
| Âm thanh FMOD bank | Không rõ | Phiên bản FMOD |

## 6. Rủi ro định dạng (nhìn từ mã đọc)
1. Giải nén không giới hạn đầu ra: `ucl_nrv2b_decompress_8(src, size, dst, &len, NULL)` không nhận dung lượng đệm; chỉ kiểm tra `len == lSize` sau khi đã ghi (`XPackFile::ExtractRead`). PAK hỏng hoặc bị thay thế có thể ghi tràn bộ đệm `lSize` byte — VERIFIED mẫu mã; khả năng khai thác thực tế UNKNOWN. Liên quan: PAK tải từ CDN, `uCrc32` không được kiểm tra.
2. `KPakList::FileNameToId` có điều kiện `if (!pszFileName && !pszFileName[0])` (nên là `||`) — VERIFIED; trên con trỏ NULL sẽ truy cập NULL. Hàm này dường như không được gọi từ đường nóng (UNKNOWN).
3. Tìm nhị phân trên chỉ mục không bảo đảm sắp xếp (`updata01.pak`) — PROBABLE.
4. Hàm hash 32-bit, va chạm có thể xảy ra giữa hai tên khác nhau trong cùng bộ 154.098 id (xác suất mỗi truy vấn ≈ 3,6×10⁻⁵) — VERIFIED tính toán.
