# INVENTORY_GAPS_AND_RISKS — Lỗ hổng của kiểm kê và rủi ro đã nhận diện

Phase 1.5 (nghiên cứu, chỉ đọc). Ngày 2026-11-12.
Nhãn: **VERIFIED · PROBABLE · UNKNOWN · BLOCKED**.

## TÓM TẮT
1. Sáu báo cáo kiểm kê **đúng ở mức số liệu thô** (35.211 file ↔ 35.212 dòng `FILE_MANIFEST.csv` gồm header; mọi số lượng tôi kiểm lại đều khớp).
2. Con số "815 UNRESOLVED" **bị đọc quá nặng**: nó trộn tên chưa giải mã đúng, mảnh chuỗi, tên dựng lúc chạy và tài nguyên rời. Sau khi hash lại, 649/1113 literal có mặt trong chỉ mục PAK, còn **101** thật sự chưa lý giải được.
3. Kiểm kê có **ba điểm yếu phương pháp** (trích literal bị lẫn mã, mất mã hóa, đối chiếu chỉ theo tên file) nhưng không làm sai kết luận cấp cao.
4. Rủi ro ưu tiên cao: (a) dữ liệu nhạy cảm nằm trong kho (tệp SQL dữ liệu tài khoản [tên đã ẩn], dump, khóa trong `paklist.ini`); (b) giải nén PAK không giới hạn; (c) mã nguồn server chưa chứng minh khớp exe đang chạy.
5. Không có bằng chứng nào cho thấy **thiếu** tài nguyên; chỉ có các điểm chưa tìm thấy.

---

## 1. Đối chiếu các báo cáo kiểm kê với phiên đọc này
| Khẳng định trong kiểm kê | Kiểm tra | Kết quả |
|---|---|---|
| 35.211 file | `FILE_MANIFEST.csv` có 35.212 dòng (1 header) | VERIFIED khớp |
| 46 `.pak`, 40 ở `data_cdn/data` | liệt kê và phân tích header 40 file | VERIFIED; cả 40 hợp lệ |
| Header mẫu bắt đầu `PACK` | đọc 32 byte đầu từng file | VERIFIED, định dạng đã giải mã |
| "Định dạng/nén UNKNOWN" | đã giải mã từ nguồn client + kiểm dữ liệu | **Giải quyết** (xem `ASSET_FORMAT_RESEARCH.md`) |
| `sound.pak`, `sound-old.pak`, `sound-old1.pak` cùng SHA-256 | cả ba có 416 mục, cùng kích thước 18.868.355 | VERIFIED nhất quán |
| 815 literal chưa khớp, 254 khớp | trích lại bằng cách khác (1113 literal) | Khác phương pháp nên không so từng số; xem mục 2 |
| "Không có `.spr/.ani/.dds/.pvr` rời" | `spr.pak` có 14.616 mục | Nhất quán |

## 2. Lỗ hổng phương pháp của `ASSET_REFERENCE_COVERAGE.md`
Bằng chứng nằm ngay trong báo cáo:
1. **Trích chuỗi bị lẫn mã.** Các dòng 14–19 bắt đầu bằng `, SPR_PATH_JINENG); \\spr\\Ui3\\loginui\\startbtn\\log_2_start.spr` — regex dính cả phần mã trước dấu nháy. Các dòng này là *một* tài nguyên (`log_2_start.spr`) bị đếm nhiều lần. VERIFIED.
2. **Mất mã hóa.** Nhiều literal tiếng Trung hiện thành `�ʺ�.spr`, `ÃÅÅÉ½ø½×`, `–°µÿÕº` (dòng 20–21, 32, 38–42, 59–76, …). Nguồn là GBK; đọc sai mã thì không thể hash để đối chiếu. Sau khi đọc byte thô và thử U2G/G2U/cp1252 của tôi, 46 literal nữa tìm được trong PAK. VERIFIED.
3. **Đối chiếu chỉ theo tên file** ("exact/unique basename") nên `close.png` ở hai thư mục khác nhau có thể bị coi là khớp. Báo cáo ghi "không khớp ≠ thiếu" là đúng, nhưng "khớp" cũng chỉ là PROBABLE.
4. **Không thử nghiệm bất kỳ quy tắc chuẩn hóa nào** của client (`g_GetPackPath`: hạ chữ thường ASCII, bỏ `..`), nên mọi tên trong PAK đều rơi vào "UNRESOLVED".
5. **Đếm theo "unique reference"** thay vì theo tên chuẩn hóa nên số 1.069 bị thổi phồng bởi biến thể viết hoa/thường và dấu gạch chéo.

Kết quả sau hiệu chỉnh (script `pak_index_probe.py` + `residual.py`, 1.113 literal):

| Lớp | Số lượng |
|---|---:|
| A. hash có trong chỉ mục PAK | 649 |
| B. chuỗi định dạng (tên dựng lúc chạy) | 19 |
| C. tồn tại rời cùng tên file (PROBABLE) | 321 |
| D. mảnh đuôi | 3 |
| E. literal hỏng trong nguồn | 20 |
| F. chưa giải thích | 101 |

Chi tiết từng literal: `data/literal_classes.csv`.

## 3. Lỗ hổng phạm vi (những gì kiểm kê chưa chạm)
| Mục | Vì sao quan trọng | Trạng thái |
|---|---|---|
| Nội dung `Resources/package.ini`, `Resources/paklist.ini`, `data/data/*.ini` | quyết định nguồn tải PAK và PAK nào được nạp | BLOCKED (chứa điểm cuối, khóa). Chỉ `data_cdn/data/paklist.ini` được đọc phần tên PAK |
| Cấu trúc `.wor`/`.map` (bản đồ) | gốc của 28 bản đồ thiếu | UNKNOWN |
| Định dạng khung SPR (RLE, alpha, bảng màu) | chất lượng hình ảnh | UNKNOWN |
| So khớp struct giao thức client↔server | dễ lệch nhất khi sửa một phía | UNKNOWN (chỉ mới so khớp ID) |
| Mã nguồn server ↔ exe đang chạy | quyết định có sửa/dựng lại được không | UNKNOWN (đã có `reports/35` dựng `gs001`; chưa tái dựng độc lập) |
| 6 PAK không có trong `paklist` | có thể là bản vá/thay thế | UNKNOWN |
| Phiên bản thư viện bên thứ ba | rủi ro bảo mật | UNKNOWN |
| 9 APK: 1 APK nằm ngoài tập băm | chuỗi cung ứng | UNKNOWN |
| `Heaven`, `Rainbow`, `Intercessor` | vai trò | UNKNOWN |

## 4. Rủi ro đã nhận diện (xếp ưu tiên)

### R1. Dữ liệu nhạy cảm trong kho — CAO
- Một tệp SQL dữ liệu tài khoản trong `RUNTIME` [tên đã ẩn theo quy ước của kiểm kê] và tệp tương tự có trong cây làm việc; CLAUDE.md ghi chúng còn trong **lịch sử git**.
- `data_cdn/data/paklist.ini` chứa hai khóa có giá trị dạng chuỗi mờ (`accinfo`, `accpint`). Tôi **không ghi giá trị**. Cần chủ máy xác nhận bản chất (token tải xuống, khóa giải mã danh sách, hay giá trị mẫu).
- Hành động đề xuất: không đưa các tệp này vào báo cáo công khai; kiểm tra bộ lọc của `dong_bo_jx1_reports.py` (Phase 48) để đảm bảo chúng không bị đẩy lên repo công khai.

### R2. Giải nén PAK có thể tràn bộ đệm — TRUNG BÌNH
`XPackFile::ExtractRead` gọi `ucl_nrv2b_decompress_8(src, size, dst, &len, NULL)` mà không truyền dung lượng `dst`; chỉ so `len == lSize` **sau khi** đã ghi. `uCrc32` ở header không được kiểm tra trong `XPackFile::Open`. PAK tải từ CDN qua HTTP (`KDownLoadFile`). Mức khai thác thực tế: UNKNOWN; mức nguy hiểm khi CDN bị can thiệp: PROBABLE. Giảm thiểu: chỉ cấp PAK từ CDN do chủ máy kiểm soát qua Tailscale (đã có) và kiểm SHA-256 trước khi cấp.

### R3. Chỉ mục PAK sai thứ tự — TRUNG BÌNH
`updata01.pak` có 3 chỗ giảm trong cột `uId` (vị trí 1398, 1412, 1421) và 312 `uId` trùng; tìm nhị phân (`XFindElemFileA`) có thể bỏ sót. Cần kiểm: id nào ở các đoạn sau, và có được yêu cầu bởi mã không. `map.pak` (1 trùng), `uinew.pak` (10), `updata02/03` (4, 1) cũng có trùng.

### R4. Mã nguồn không chứng minh khớp binary — TRUNG BÌNH
Không có băm nhị phân server; CLAUDE.md đã nêu. Rủi ro khi sửa nguồn rồi triển khai: hành vi khác exe đang chạy.

### R5. Hiệu năng/độ mượt phụ thuộc phần chưa đọc — TRUNG BÌNH
Đường vẽ và đường nạp ảnh (`KImageStore2::LoadImage`, `KScenePlaceC`) chưa được lập hồ sơ. Các phase trước đã chạm đến (30–34, 45–47) nhưng kết luận nằm ngoài phạm vi phiên này.

### R6. Ba hệ build cùng tồn tại, cờ trình biên dịch mạo hiểm — THẤP-TRUNG BÌNH
`ndk-build` (`Application*.mk`), CMake và Xcode; `-ffast-math -fstrict-aliasing -flto` trong Release CMake. Rủi ro: hồi quy hành vi khi đổi trình biên dịch/NDK.

### R7. Mã hóa ký tự — THẤP-TRUNG BÌNH
GBK/UTF-8/hỏng lẫn lộn trong nguồn; 20 đường dẫn mất byte. Mọi công cụ phân tích phải đọc byte thô, không đọc "văn bản".

### R8. Thư viện bên thứ ba cũ — UNKNOWN
Cocos2d-x 3.17.2 và `external/*` đi kèm. Chưa tra phiên bản; nếu cần, tra **chỉ bằng hash/phiên bản**, không tải file lên dịch vụ ngoài (CLAUDE.md).

### R9. Cây nguồn lẫn sản phẩm build và dữ liệu vận hành — THẤP
Hàng trăm MB `.obj/.pdb/.ipch/.sbr`, 19 `.dmp` (≈180 MB), 1.635 `.log`. Chủ yếu làm chậm quét và tăng nguy cơ lộ dữ liệu; không ảnh hưởng chạy.

## 5. Những gì tôi không kết luận
- Không kết luận asset nào thiếu: lớp F (101) chỉ là "chưa tìm thấy" và đa phần là tên trần chưa biết thư mục gốc.
- Không kết luận ai đó tạo/chỉnh PAK sai: các bất thường (dup/unsorted) có thể do cách đóng gói của công cụ gốc.
- Không đánh giá độ an toàn của các binary (chưa quét ở phase này).
