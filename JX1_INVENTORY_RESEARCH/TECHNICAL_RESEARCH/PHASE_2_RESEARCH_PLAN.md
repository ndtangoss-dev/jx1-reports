# PHASE_2_RESEARCH_PLAN — Kế hoạch nghiên cứu tiếp theo (chờ duyệt, chưa triển khai)

Ngày 2026-11-12. Nhãn: **VERIFIED · PROBABLE · UNKNOWN · BLOCKED**.

## TÓM TẮT 5 DÒNG
1. Phase 1.5 đã giải mã định dạng PAK (VERIFIED) và đối chiếu 1.113 literal: 649 có trong chỉ mục, 101 chưa giải thích, **không có literal nào được chứng minh là thiếu**.
2. Việc có giá trị cao nhất tiếp theo: **đọc đường nạp/vẽ SPR** (`KImageStore2::LoadImage`, `KSprControl`, `KScenePlaceC`) vì đó là nơi độ mượt và chất lượng hình ảnh được quyết định.
3. Việc rẻ và an toàn nhất: dựng **từ điển tên → hash** để biết PAK nào chứa gì, và so sánh struct giao thức client↔server (cả hai đều chỉ đọc).
4. Giải nén nội dung PAK (đọc ảnh, bản đồ) cần chủ máy nới quy tắc "không giải nén": đề xuất làm trên bản copy và ghi ra thư mục riêng.
5. Mọi bước đều chỉ-đọc cho tới khi chủ máy duyệt từng nhóm.

**Cần tôi quyết định: có** (chọn nhóm việc ở mục 5; nhóm 2B/3 cần nới quy tắc không giải nén).

---

## 1. Thứ tự đề xuất
| Ưu tiên | Nhóm việc | Vì sao trước | Rủi ro với dữ liệu gốc |
|---:|---|---|---|
| 1 | **A. Đọc mã** SPR→texture, vẽ thế giới | quyết định độ mượt/chất lượng, hiện là điểm mù lớn nhất | Không (chỉ đọc) |
| 2 | **B. Từ điển tên→hash** để lập danh mục nội dung PAK | biến "UNRESOLVED" thành bản đồ tài nguyên thật; cần cho mọi bước sau | Không (chỉ đọc chỉ mục) |
| 3 | **C. So khớp struct giao thức** client↔server | ngăn lỗi tinh vi khi sửa một phía | Không |
| 4 | **D. Kiểm tra tính toàn vẹn PAK** (sắp xếp, trùng, CRC) | R2, R3 trong `INVENTORY_GAPS_AND_RISKS.md` | Không |
| 5 | **E. Đọc mã bản đồ** (`.wor`, `.map`) và đối chiếu 28 bản đồ thiếu | giải một tồn đọng CLAUDE.md | Không |
| 6 | **F. Giải nén thử trên bản copy** (nrv2b) → xuất SPR/ảnh ra thư mục riêng | cần cho phân tích nội dung/chất lượng ảnh | Trung bình-thấp (xem rủi ro) |
| 7 | **G. Đối chiếu mã nguồn server ↔ exe** (hash biểu tượng, so chuỗi) | trả lời "nguồn có khớp binary?" | Không chạy exe |

## 2. Chi tiết từng nhóm

### A. Đọc mã đường nạp và vẽ ảnh (ưu tiên 1)
- **Việc:** đọc `ImageStore/KImageStore2.cpp` (`LoadImage`, `GetSprFrame`, `FreeImageObject`, `CheckBalance`), `gamecore/KSprControl.cpp`, `CoreDrawGameObj.cpp`, `gamescene/KScenePlaceC.cpp` (`Preprocess`, `SetFocusPosition`), `XPackFile::GetSprHeader/GetSprFrame`.
- **Bằng chứng cần thu thập:** (1) định dạng pixel và đường giải RLE→RGBA; (2) vòng đời texture (tạo/giữ/giải phóng); (3) cách `TYPE_FRAME` khác `TYPE_UCL`; (4) cache của kho ảnh; (5) bản vẽ tối đa số lệnh vẽ mỗi khung.
- **Công cụ:** `rg`/Grep, script đếm gọi hàm; không cần công cụ mới.
- **Sản phẩm:** `RENDER_PATH_NOTES.md` với sơ đồ luồng hàm và các điểm nóng (có số dòng).
- **Rủi ro/giới hạn:** chỉ đọc mã; không xác nhận được hiệu năng thật nếu không đo trên thiết bị (đo thuộc nhóm riêng, cần duyệt).

### B. Từ điển tên→hash (ưu tiên 2)
- **Việc:** thu thập tên ứng viên từ (1) literal trong mã, (2) các INI/TAB/Lua/TXT *đã có sẵn dạng rời* trong `RUNTIME/gs/Settings` và `Resources`, (3) tên trong script, (4) mẫu đường dẫn (`\spr\…`, `\sound\…`); chuẩn hóa như `g_GetPackPath`; tính hash; ghi lại `tên → PAK → chỉ số → kích thước/nén`.
- **Giả định cần kiểm:** cùng tên có thể được viết nhiều dạng (GBK/UTF-8); script đã thử bốn biến thể.
- **Sản phẩm:** `PAK_CONTENT_CATALOG.csv` (tên, PAK, nén, kích thước). Đo độ bao phủ = số `uId` có tên / 154.098 (kỳ vọng thấp: PAK không lưu tên).
- **Rủi ro/giới hạn:** không bao giờ phủ 100%; id không có tên vẫn là "UNKNOWN", không phải "thừa". Có thể bắt gặp tên chứa dữ liệu nhạy cảm (tên tài khoản) → lọc.

### C. So khớp struct giao thức
- **Việc:** trích mọi `struct` trong `KProtocol.h` (client, gameserver, gateway) có `#pragma pack(1)`; tính `sizeof` và offset từng trường bằng script (biên dịch thử một tệp `static_assert` cục bộ trên máy, **không** build dự án, không chạy server). Báo các cặp có layout khác.
- **Bằng chứng:** bảng `struct, trường, offset, kích thước` ở cả ba bản.
- **Công cụ:** Python + `clang -fsyntax-only` hoặc `pycparser`; nếu không có trình biên dịch, phân tích văn bản (đủ cho struct đơn giản).
- **Rủi ro/giới hạn:** `#pragma pack` lồng nhau, `BYTE/WORD/DWORD` kiểu typedef, GUID khác định nghĩa trên Android (có `typedef struct _GUID` trong client). Cần kiểm tay vài struct.

### D. Kiểm tra tính toàn vẹn PAK
- **Việc:** (1) với từng PAK, tính CRC32 theo định nghĩa của `uCrc32` (cần suy ra phạm vi: toàn file/chỉ mục/dữ liệu — thử các phương án trên PAK nhỏ như `volam01.pak`, `dyshop.pak`, `test.pak`); (2) liệt kê mọi `uId` nằm ở đoạn sau chỗ sai thứ tự của `updata01.pak`, xem có `uId` nào được hash từ tên ứng viên (nhóm B) không; (3) xác nhận từng cặp trùng `uId` giữa PAK có cùng nội dung hay khác (so băm nội dung đã nén, không giải nén).
- **Sản phẩm:** `PAK_INTEGRITY_REPORT.md`.
- **Rủi ro:** ý nghĩa của `uCrc32` có thể không còn được dùng (có thể bằng 0); khi đó ghi nhận UNKNOWN.

### E. Mã bản đồ và 28 bản đồ thiếu
- **Việc:** đọc `Core/Src/KSubWorld.cpp LoadMapS`, `KSubWorldSet.cpp`, và phía client `KSubWorld.cpp`, `KRegion.cpp`, `KMapMusic.cpp`; mô tả định dạng `.wor`/`.map`; so với `gs\Settings\MapList.ini`, `gs\maps\WorldSet_gs001.ini` (chỉ đọc tên khóa/ID bản đồ).
- **Sản phẩm:** `MAP_FORMAT_NOTES.md`, bảng bản đồ ↔ nguồn dữ liệu client/server.
- **Giới hạn:** file `.wor` nằm trong `gs\pak\maps*.pak` — liệt kê tên cần nhóm B.

### F. Giải nén thử trên bản copy (cần duyệt)
- **Việc:** viết trình giải `nrv2b` độc lập (Python/C, không dùng mã dự án), chạy **chỉ trên bản copy** của vài PAK nhỏ (`ui.pak` 292 KB, `font.pak`, `volam01.pak`), ghi ra `C:\Jx1CocoV3_RESEARCH\extracted\<pak>\`; kiểm tra: tổng kích thước = `lSize`, chữ ký `SPR\0`/PNG/INI.
- **Ranh giới an toàn:** không giải đè, không tạo file trong cây nguồn; không giải nén `spr.pak` và `map.pak` lớn khi chưa có kết quả với PAK nhỏ; xử lý dữ liệu như không tin cậy (CLAUDE.md): trình giải chạy trong tiến trình giới hạn, đặt giới hạn đầu ra = `lSize` (tránh lỗi tràn ở R2).
- **Rủi ro/giới hạn:** tên file sau giải phụ thuộc nhóm B; có thể thấy tên/tài khoản thật trong dữ liệu `serlst/slist*`; thư mục ra phải ngoài git và ngoài repo công khai.

### G. Nguồn server ↔ exe đang chạy
- **Việc:** (1) dựng danh sách chuỗi/hằng số đặc trưng từ nguồn (`GAME_FPS`, thông điệp log) rồi tìm trong exe bằng chuỗi (không chạy); (2) so thời gian build trong PE header với ngày sửa nguồn; (3) đối chiếu danh sách tệp `.cpp` biên dịch với `.pdb`/`.map` nếu có.
- **Rủi ro:** không chứng minh tuyệt đối; chỉ cho bằng chứng thống kê.

## 3. Tổng hợp công cụ cần thiết
| Công cụ | Việc | Có sẵn? |
|---|---|---|
| `scripts/pak_index_probe.py`, `classify_unresolved.py`, `residual.py`, `protocol_enum_compare.py` | đã dùng ở Phase 1.5 | Có (`C:\Jx1CocoV3_RESEARCH\scripts`) |
| `docs-analysis/tools` (công cụ PAK của dự án) | tham khảo, chưa dùng ở phase này | Có (dự án trước) |
| Trình giải nrv2b độc lập | nhóm F | Cần viết (dựa đặc tả nrv2b công khai); không dùng mã trong `ucl/` để tránh đồng nhất lỗi |
| `clang`/`pycparser` | nhóm C | UNKNOWN có trên máy |
| Python 3.12 (`-I`) | mọi script | Có |

## 4. Rủi ro tổng và giới hạn từng phương pháp
| Phương pháp | Giới hạn thật | Điều không được kết luận |
|---|---|---|
| Tra hash theo tên | chỉ xác nhận *có mục tên này*, không xác nhận nội dung đúng | "không có hash" không có nghĩa là thiếu (mã hóa/đường dẫn khác) |
| Đọc mã | không cho biết hành vi lúc chạy | hiệu năng thực |
| So khớp struct | chỉ bắt lệch bố cục, không bắt lệch ngữ nghĩa | tương thích hành vi |
| Giải nén thử | phụ thuộc đúng đặc tả nrv2b | PAK nào "hỏng" nếu giải sai |
| So exe với nguồn | thống kê | "khớp hoàn toàn" |

## 5. Quyết định cần chủ máy
1. Duyệt thứ tự **A → B → C → D → E → G** (đều chỉ đọc, không đổi gì)?
2. Có cho phép nhóm **F** (giải nén thử trên bản copy PAK nhỏ, ghi vào `C:\Jx1CocoV3_RESEARCH\extracted`) hay giữ nguyên quy tắc "không giải nén"?
3. Giá trị `accinfo`/`accpint` trong `paklist.ini` là gì (và có nên coi như bí mật)? Tôi sẽ không ghi lại cho tới khi chủ máy xác nhận.

Khuyến nghị: duyệt A–E và G ngay; F để sau khi A và B xong.
