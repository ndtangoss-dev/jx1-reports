# AMOLX-06 — Chẩn đoán updater dừng ở 6%

- Task: `AMOLX-06-UPDATER-6PCT-DIAG-20261116`; ngày 16/11/2026, Asia/Bangkok (UTC+7).
- Prompt GitHub đã đọc: `PROMPTS/AMOLX-06-UPDATER-6PCT-DIAG-20261116.md`, blob `9bd2e837c6625a1bf8cb3d8d47b36d13de3e8110`.
- Trạng thái: **DONE — hoàn tất lượt chẩn đoán tĩnh trong timebox 5 phút; chưa sửa hoặc kiểm thử runtime mới.**
- Root cause: **PROBABLE — lỗi bootstrap manifest/updater do cấu hình AMOLX chưa khớp bộ CDN Cocos V3; chưa có URL và mã lỗi runtime để chốt nguyên nhân mạng cụ thể.**
- Cần tôi quyết định: không trong phạm vi lượt chẩn đoán này.

## Kết luận có thể hành động

**VERIFIED:** APK chọn nhánh Việt (`_clientlanguage=2`), chứa `package_vn.ini` dài đúng **545 byte**, trùng byte với cấu hình bản copy AMOLX-04. Updater ghép URL HTTP từ host LAN trong cấu hình, không ghi cổng, rồi yêu cầu **`data/paklist_vn.ini`**. CDN local được chỉ định chỉ có **`data/paklist.ini`**, không có `data/paklist_vn.ini`. Đây là lệch tên manifest có thật; không đồng nghĩa đã nhận HTTP 404 từ một endpoint đang chạy.

**VERIFIED:** số 6% là tiến độ đếm tài nguyên khởi tạo: ba lần tăng trên tổng 50, tức `3/50 × 100 = 6`. `package_vn.ini:545` được tạo từ tên file local và số byte đã copy; **545 không phải mã HTTP, số dòng source hoặc tên file mạng lỗi**. APK không chứa file `.pak`. AMOLX-05 đã dựng được nền/renderer nhưng chưa qua bootstrap tài nguyên để tới login.

**PROBABLE:** lỗi đang nằm ở bước lấy danh sách PAK trước khi xử lý từng PAK: host trong AMOLX là cấu hình LAN cũ, URL không có cổng và nhánh VN dùng manifest không tồn tại trong bộ CDN local. Báo cáo Cocos hiện có ghi CDN cổng 8080; đó là bằng chứng lịch sử, không phải xác minh trạng thái mạng hiện tại. Không đổi host/cổng hay tự coi endpoint nào là môi trường thử nghiệm.

**UNKNOWN:** lần AMOLX-05 thất bại vì DNS, connect/timeout, HTTP, Content-Length/HEAD, ghi file hay nhánh lỗi khác. Không có HTTP status/CURLcode/errno runtime. Không gán chắc chắn lỗi 404, thiếu bản đồ hoặc EGL làm root cause.

## Luồng updater và bằng chứng source

Đường dẫn trong bảng tính từ `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client`.

| Chặng | File, symbol và dòng | Hành vi đã xác minh / ý nghĩa |
|---|---|---|
| Chọn scene/ngôn ngữ | `Source/AppDelegate.cpp:85`; `Source/gamecore/KCore.cpp:95–96` | Scene đầu `KUpdateLayer`; `_clientlanguage=2`, `_clientNoNetWork=false`. Vị trí scene kế thừa checkpoint AMOLX-05; hai biến đã đọc lại trực tiếp. |
| Copy cấu hình | `Source/gamescene/KUpdateLayer.cpp`, `init:91–108`, `copyData:382–436` | Tổng ban đầu 50; copy `package_vn.ini` vào writable `files/data/`; ghi `writelen`, tăng bộ đếm trong copyData và init. |
| Mốc 6% | `KUpdateLayer.cpp:175`, `update:590–593` | Tăng thứ ba sau init ImageStore. UI dùng `m_nLoadedResources / m_nAllLoadResources`, `nCurpFileName`, `writelen`; phù hợp 6%, package_vn.ini, 545 byte. |
| URL/downloader | `KUpdateLayer.cpp:111–146` | Android đọc `data\\package_vn.ini`; lấy `[Package] down`, ghép `http://%s/`; tạo `downloadFile::GetInst`, gọi `startload`. Không suy ra backslash là lỗi: engine có lớp xử lý đường dẫn, chưa audit lớp đó. |
| Tạo worker | `KUpdateLayer.cpp`, `startload:813–818`, `Run:674–710` | `isHaveClient=true`, `Start()`; worker yêu cầu `data/paklist_vn.ini` với reload ban đầu 1; ret true mới chuyển `STATE_LOAD_LISTDATA` và tăng bộ đếm. |
| File đích | `Source/engine/KDownLoadFile.cpp`, `DownLoadFile:50–56`, `createFile:152–164` | Đích là `nfullPath + filename`; mở wb+ hoặc ab+. Mở thất bại đặt `STATE_NO_FILE=2`, ret false. |
| HEAD/độ dài | `KDownLoadFile.cpp:64–71`, `getDownloadFileLenth:205–249` | Ghép URL + tên file, HEAD với timeout 5 giây, đọc Content-Length. CURL thất bại trả -1; độ dài không dương bị gom thành `STATE_NO_URLFILE=3`. |
| GET | `KDownLoadFile.cpp:80–108` | GET timeout 20 giây, resume offset; curl thất bại thành `STATE_NO_NET=1`. Không lưu CURLcode/HTTP status trong log hiện tại; chưa thấy kiểm checksum trong hàm này. |
| Ánh xạ lỗi/hộp thoại | `KDownLoadFile.h:20–25`; `KUpdateLayer.cpp:446–502`, `Run:690–703` | 1 → `STATE_ON_NET_UP`, 2 → `STATE_ON_FIEL_UP`, 3 → `STATE_ON_URLFIEL_UP`. `update()` đợi `errorLoop>=300` rồi hiện messageBox, trả sớm. Hộp thoại thiếu client là nhánh `!isHaveClient`; không chọn được nhánh runtime chỉ từ ảnh chữ hỏng. |
| Parse manifest | `KUpdateLayer.cpp:505–551` | Đọc `[list] count`, `isopen`, `pak_N`, `pak_N_r`; tạo danh sách và chuyển `STATE_DWON_LISTDATA`. Chưa có bằng chứng runtime đã tới đây. |
| Tải từng PAK | `KUpdateLayer.cpp:739–799` | Lấy `pakName` rồi DownLoadFile; chỉ tiến file khi ret true **và state=5**. Có lỗi hợp đồng state riêng bên dưới, không gộp vào nguyên nhân 6%. |

Worker gọi `sleep(0.5)` ở Android (`KUpdateLayer.cpp:713`); hàm sleep nhận số giây nguyên nên đây không phải bảo đảm nghỉ nửa giây. Chỉ ghi nhận khả năng retry quá nhanh, không sửa hoặc khẳng định đã gây treo.

## Đối chiếu cấu hình và asset Cocos/CDN

Cocos canonical chỉ đọc: `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`.
CDN local chỉ đọc: `C:\Jx1CocoV3\data_cdn\data`.

| Mục | AMOLX thực tế | Cocos/CDN thực tế | Kết luận |
|---|---|---|---|
| Cấu hình nhánh đang chọn | `Content/package_vn.ini:1–2`, down là host LAN literal; không công bố host | `Resources/package*.ini:2` có chuỗi down khác; chưa giải mã hoặc dùng để kết nối | VERIFIED: cấu hình khác; chưa xác minh endpoint live. Không chép chuỗi down của Cocos sang AMOLX. |
| URL mặc định | `http://<host-đã-che>/data/paklist_vn.ini`; không cổng tường minh | `Classes/gamescene/KUpdateLayer.cpp:345–355` cũng dựng HTTP từ down; báo cáo `docs-analysis/reports/36-chuan-bi-reboot-sau-cai-cpp.md:6,19` ghi CDN 8080 và cổng 80 thuộc ReportServer | VERIFIED tĩnh; PROBABLE cấu hình AMOLX không khớp CDN vận hành đã ghi nhận. Không kiểm tra lại tiến trình/cổng. |
| Manifest VN | APK và Content không có paklist_vn.ini; source yêu cầu tải file đó | `data_cdn/data/paklist_vn.ini` không tồn tại | VERIFIED lệch tên trong bộ local; trạng thái HTTP UNKNOWN. |
| Manifest chuẩn | Nhánh language=1 mới dùng `data/paklist.ini` | `data_cdn/data/paklist.ini:1–3` có `[list]`, `count=35;32`, `isopen=1`; có 35 mục pak_0..pak_34 | VERIFIED cấu trúc chính tương ứng parser. Chưa chạy parser để kết luận cách xử lý hậu tố `;32`. |
| PAK trong APK | Kiểm directory của ZIP: không có entry `.pak` | CDN có các PAK hiện hữu; chỉ đọc tên/kích thước, không quét nội dung hàng GB | VERIFIED app cần nguồn dữ liệu ngoài APK; không chứng minh từng asset đã tương thích. |
| Danh sách mount | `Content/package_vn.ini:4–35`: 32 mục, có một tên lặp | So sánh tên không phân biệt hoa thường với file trực tiếp trong CDN | VERIFIED thiếu 7 tên duy nhất ở CDN: `settings_ver.pak`, `Updata04.pak`, `Updata_vn.pak`, `common.pak`, `resupd1.pak`, `resupd.pak`, `Updata02-20.pak`. Đây là rủi ro sau bootstrap, chưa phải bằng chứng gây 6%. |
| Asset Cocos V3 | Danh sách AMOLX chưa tương ứng bộ mount Cocos | `Resources/package.ini:4–6` có script_skill/update10/update_music; CDN manifest `pak_32=data/update10.pak`, `pak_34=data/script_skill.pak`; hai file có thực trong CDN | VERIFIED file/manifest có; không suy ra toàn bộ PAK/SPR tương thích AMOLX hoặc đã thay thế/kiểm thử. |

Kiểm ZIP chỉ đọc ba nhóm tên cấu hình và sự tồn tại đuôi `.pak`; **`assets/package_vn.ini` trùng byte bản copy Content và dài 545 byte**. Không build/hash lại APK, không extract/copy asset sang emulator/CDN.

Checkpoint prompt nhắc kết quả V002 về update10.pak đã đóng gói/nạp được. Không tìm thấy báo cáo V002 được đặt tên rõ trong truy vấn hẹp của thư mục báo cáo; không mở rộng inventory. Chỉ dùng checkpoint đó làm ngữ cảnh, không coi là test AMOLX hiện tại.

## Hộp thoại sai mã hóa

**VERIFIED:** nhánh lỗi quyết định bằng `nDownState` và `isHaveClient` trước khi gọi `UTEXT(...,1)`/`messageBox` (`KUpdateLayer.cpp:446–502`). Vì vậy chữ sai mã hóa che thông tin chẩn đoán, không tự làm downloader thất bại theo luồng đã đọc. Căn nguyên chuyển mã cụ thể **UNKNOWN**, chưa truy sâu UTEXT ngoài timebox. Không giải đoán chắc chắn nội dung hộp thoại từ ảnh AMOLX-05.

## Lỗi phụ chắc chắn trong hợp đồng trạng thái

`KDownLoadFile.h:20–25` định nghĩa `STATE_NEXT_FILE=4`, `STATE_WANCHENG_FILE=5`. Sau GET mới thành công, `DownLoadFile` đặt state=4 (`KDownLoadFile.cpp:107`), trong khi vòng từng PAK chỉ tiến khi state=5 (`KUpdateLayer.cpp:785–799`). Nhánh file local đã đủ mới trả state=5 (`KDownLoadFile.cpp:74–77`).

**VERIFIED tĩnh:** hai bên không thống nhất cách công nhận file mới tải xong; kết hợp kiểm độ dài local bằng filename tương đối (`:61`) làm khả năng tự thoát phụ thuộc đường dẫn làm việc/file đã có. **Không gán lỗi này là nguyên nhân màn hình 6%**, vì vòng manifest thoát theo ret, chưa kiểm state=5. Không sửa trong lượt này để tránh trộn hai lỗi và cần build/runtime riêng.

Ngoài ra downloader chưa kiểm HTTP status/`CURLOPT_FAILONERROR`; phản hồi lỗi có body/Content-Length có thể không được phân biệt với file đúng. Đây là rủi ro tĩnh, không phải xác nhận endpoint trả HTML hoặc 404.

## Đúng một bước kế tiếp

**AMOLX-07: bổ sung chẩn đoán có cấu trúc trong bản copy AMOLX, build rồi smoke-test chỉ khi có môi trường mạng được duyệt.** Ghi từng chặng: tên file/đích, host đã che và cổng, thao tác HEAD/GET, CURLcode + curl error text, HTTP status, Content-Length, số byte thực ghi, errno khi mở/ghi, trạng thái downloader/updater và kết quả parse manifest; ghi rõ checksum chưa được hỗ trợ thay vì báo đạt. Đồng thời ghi error-code đọc được trước messageBox. Dữ liệu đó phân biệt được DNS/HTTP/404/timeout/HEAD không có độ dài/manifest/ghi file, trước khi quyết định patch nhỏ nhất.

Chưa đề xuất chép nguyên bộ Cocos hoặc đổi endpoint để thử. Lệch tên manifest cần được thống nhất bằng cấu hình/nhánh ngôn ngữ trong task được duyệt; lỗi state=4/5 cần sửa riêng sau khi khoanh đúng chặng. Không có thay đổi source trong AMOLX-06.

## Phạm vi đã làm và không làm

- Đã đọc source/config hẹp nêu trong bảng, đọc manifest CDN và tên/kích thước file trực tiếp, đối chiếu config đã đóng gói trong ZIP. Bằng chứng AMOLX-05 kế thừa từ báo cáo đã bàn giao, không chạy lại smoke-test.
- Git status/branch kiểm đúng một lần trước ghi: `master`, `docs-analysis/BAI_HOC.md` đã modified cùng nhiều file untracked cũ. Giữ nguyên; chỉ tạo báo cáo này.
- Không chạy APK/ADB/build/test mới, không truy cập VM/server/CDN endpoint, không gửi packet hoặc login, không đổi credential/model/Dispatcher.
- Không sửa AMOLX/Cocos/source server, asset/CDN gốc hoặc dữ liệu LDPlayer. Không tạo báo cáo phụ, không upload source/binary/ảnh/log thô.
- Có một lệnh trích dòng PowerShell gặp `Argument types do not match`; đã thay bằng đọc đoạn cụ thể, không tác động file hoặc lặp quá ba lần.

## Bàn giao GitHub

Chỉ báo cáo `TEST_RESULTS/AMOLX-UPDATER-6PCT-DIAG-20261116.md` được công bố lên `ndtangoss-dev/jx1-reports/main` bằng kết nối GitHub hiện có; không stage các thay đổi của workspace source. Link: https://github.com/ndtangoss-dev/jx1-reports/blob/main/TEST_RESULTS/AMOLX-UPDATER-6PCT-DIAG-20261116.md

Commit SHA được GitHub cấp sau khi ghi file; phản hồi cuối bàn giao SHA đã xác minh và kết quả đọc lại blob. Không ghi SHA giả định hoặc tự tham chiếu vào chính nội dung commit.
