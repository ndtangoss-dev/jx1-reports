# AMOLX-07 — Dùng asset Cocos hiện có, đưa AMOLX vào game để kiểm thử

Ngày: 16/11/2026
Repository báo cáo: `ndtangoss-dev/jx1-reports`

## Mục tiêu
Người dùng không tìm thấy CDN AMOLX riêng và muốn tiếp tục bằng tài nguyên sẵn có để **đưa AMOLX qua updater, tới login, kết nối server JX1 đang dùng được bởi APK Cocos cũ, và cố gắng vào bản đồ để kiểm thử**.

Đây là task tích hợp client + kiểm thử có kiểm soát. Không chỉ dừng ở chẩn đoán tĩnh. Làm tối đa trong một lượt, ưu tiên có APK kiểm thử và bằng chứng runtime. Không tuyên bố vào game thành công nếu chưa thấy bằng chứng.

## Checkpoint bắt buộc — không làm lại
- AMOLX source copy: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client`.
- APK AMOLX-04: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk`; SHA-256 `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1`.
- LDPlayer 9 đã nhận package `com.kull.jx1client`; AMOLX-05 INSTALL-OK/LAUNCH-OK, dựng Axmol 2.1.5/OpenGL ES 3.1, đứng khoảng 6%.
- AMOLX-06 report: `TEST_RESULTS/AMOLX-UPDATER-6PCT-DIAG-20261116.md`. Đọc báo cáo này và các đường dẫn/source được trích trong đó; không chạy lại audit.
- Kết luận AMOLX-06:
  - App chọn language=2, `Content/package_vn.ini` dài 545 byte.
  - Updater yêu cầu `data/paklist_vn.ini`; CDN local Cocos chỉ có `data/paklist.ini`.
  - AMOLX package_vn.ini khai 32 mục (một tên trùng); so với CDN có 7 tên PAK không tồn tại: `settings_ver.pak`, `Updata04.pak`, `Updata_vn.pak`, `common.pak`, `resupd1.pak`, `resupd.pak`, `Updata02-20.pak`.
  - CDN Cocos hiện có `data/paklist.ini`, 35 mục; một số PAK như `update10.pak` và `script_skill.pak` tồn tại.
  - AMOLX dùng host LAN cũ và HTTP URL không ghi port; chưa có HTTP runtime status. Không lấy host/cổng từ cấu hình cũ nếu chưa chứng minh là endpoint thử nghiệm hiện dùng.
  - Downloader có state contract mismatch: GET thành công đặt state 4, vòng PAK chờ state 5. Đây là lỗi tĩnh độc lập; chưa chứng minh gây lỗi 6%.
  - Không có CDN AMOLX riêng được tìm thấy bởi người dùng.
- Cocos V3 CDN root: `C:\Jx1CocoV3\data_cdn`; dữ liệu nằm `C:\Jx1CocoV3\data_cdn\data`.
- Cocos APK cũ của người dùng hiện vẫn vào game qua Tailscale. Đây là bằng chứng thực tế về đường kết nối hiện tại, nhưng không tự chứng minh AMOLX protocol tương thích.
- Báo cáo V002: `JX1_VISUAL/REPORTS/V002_full-technical-feasibility-audit.md`; BAI_HOC.md có lịch sử CDN và các bài học; chỉ đọc phần liên quan nếu cần.
- Cocos canonical không được sửa.

## Quyền được duyệt trong task này
Người dùng yêu cầu đưa AMOLX vào game để test. Cho phép:
- Sửa source/config trong bản copy AMOLX ở workspace riêng.
- Dùng dữ liệu PAK/config từ CDN Cocos hiện có làm nguồn thử nghiệm, nhưng chỉ sau khi kiểm tra tương thích và chọn tập nhỏ nhất đủ để qua bootstrap/login/map.
- Build APK debug mới, cài/cập nhật package AMOLX trên đúng LDPlayer 9 đã nhận diện ở AMOLX-05, launch, đọc log và chụp bằng chứng.
- Dùng đúng endpoint/IP/port/protocol mà APK Cocos cũ đang dùng thành công, nếu có thể xác định từ báo cáo/config đã có mà không thay đổi server. Chỉ kết nối client tới server hiện hữu để thử login/gameplay. Không dò quét mạng.
- Nếu AMOLX tới login, có thể dùng quy trình đăng nhập thử hiện có của người dùng nếu credential đã được cung cấp rõ ràng trong môi trường được phép; tuyệt đối không đọc/in/log/commit mật khẩu. Nếu không có credential được cung cấp an toàn, dừng ở login và báo cần người dùng nhập trực tiếp.
- Kiểm tra đến màn hình chọn server, chọn nhân vật, vào bản đồ nếu các bước trước thành công. Không dùng tài khoản của người khác.

## Không được phép / rào chắn
- **Không sửa, restart, stop, cấu hình hoặc chạy thêm bất kỳ EXE/server process nào trên VM/Main VM.** Không đụng SQL, database, CDN server process, firewall, router, Tailscale config, port-forward hay Task Scheduler.
- Không quét port/IP, không dò endpoint. Chỉ dùng đúng endpoint đã được xác nhận từ cấu hình Cocos/APK và báo cáo lịch sử; nếu không tìm được bằng chứng endpoint chính xác, dừng trước kết nối và ghi rõ blocker.
- Không thay đổi cấu hình mạng trên máy/VM. Không thử các host/cổng phỏng đoán.
- Không xóa dữ liệu LDPlayer, không factory reset, không clear app data. Có thể cài đè APK cùng package chỉ khi package đang cài là AMOLX-04 đã cài trong AMOLX-05; trước khi ghi đè, xác minh package/version và giữ dữ liệu hiện có. Không uninstall.
- Không sửa Cocos canonical, source server, CDN gốc, asset gốc. Mọi manifest/asset thử nghiệm phải ở thư mục riêng trong workspace AMOLX, không ghi vào `data_cdn`.
- Không sao chép nguyên 3.2 GB một cách máy móc. Chỉ dùng PAK thực sự có và kiểm tra tham chiếu/manifest; không giả tạo PAK rỗng, không đổi tên file thiếu để đánh lừa updater.
- Không tự tạo `paklist_vn.ini` giả nếu chưa chứng minh parser và format. Có thể tạo manifest thử nghiệm trong thư mục riêng dựa trên PAK tồn tại, ghi rõ nguồn và phạm vi.
- Không vô hiệu hóa updater, không bỏ qua kiểm tra integrity, không hardcode bypass login/protocol, không bỏ qua lỗi asset.
- Không ghi mật khẩu/token vào source, file cấu hình, log, GitHub hoặc báo cáo.
- Giữ mọi thay đổi local/untracked có sẵn; không reset/clean/checkout phá hủy. Kiểm tra git status một lần trước khi ghi; chỉ stage/commit đúng file AMOLX task và báo cáo. Không sửa local AGENTS.md hoặc CLI/model config.
- Không chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`, `S3RelayServer.exe` hoặc EXE server.

## Kế hoạch thực hiện — theo thứ tự
1. **Resume đúng checkpoint**: đọc AMOLX-06 report và kiểm tra Git status một lần. Xác định LDPlayer 9 từ ADB theo bằng chứng AMOLX-05; không kiểm tra lại toàn bộ môi trường.
2. **Tạo asset test tối thiểu** trong workspace AMOLX riêng:
   - So sánh package_vn.ini với package.ini Cocos và file thật trong CDN.
   - Phân tích cách parser `paklist` và package mount xử lý `pak_N`, `pak_N_r`, hậu tố số lượng, thứ tự ưu tiên, tên file.
   - Chọn các PAK có thật và cần thiết cho bootstrap, login và map. Không giả định PAK Cocos tương thích chỉ vì cùng định dạng; kiểm tra version/header/hash/manifest và cấu trúc dữ liệu liên quan.
   - Quyết định rõ: giữ nhánh VN với manifest thử nghiệm đúng format, hoặc dùng cấu hình package phù hợp đã có. Không đổi ngôn ngữ/asset một cách ngầm định.
   - Chỉ copy vào thư mục thử nghiệm riêng; không thay CDN gốc. Tạo manifest/URL local test chỉ nếu có endpoint local đã được phê duyệt và đang tồn tại; không tự chạy server/CDN process hoặc mở port.
3. **Sửa downloader trong bản copy AMOLX**:
   - Xác minh và sửa state contract 4/5 nhỏ nhất, có unit/static test phù hợp.
   - Thêm log có cấu trúc đã lọc secret: stage, tên file, destination tương đối, CURLcode/error text, HTTP status, Content-Length, bytes written, file-open/write errno, updater state, manifest parse result. Không ghi URL có host/token nhạy cảm; có thể ghi scheme/port và host hash/đã che.
   - Phân biệt HEAD fail, GET fail, HTTP 4xx/5xx, file local missing, manifest parse fail, file open/write fail. Không tuyên bố checksum nếu code không kiểm.
   - Giữ thông báo UI có thể đọc được; không sửa mã hóa tùy tiện nếu chưa xác định encoding. Ghi error code trước messageBox.
4. **Build APK mới** bằng toolchain AMOLX-04 đã có. Build chỉ từ bản copy. Nếu lỗi, tự xử lý an toàn trong phạm vi, không lặp một lỗi quá 3 lần.
5. **Smoke-test LDPlayer 9**:
   - Xác minh đúng emulator serial trước thao tác.
   - Giữ app data; cài đè chỉ khi đúng package AMOLX-04 đã cài. Launch và thu log.
   - Xác nhận vượt updater và đến login. Nếu không, ghi stage/error cụ thể và dừng không retry vô hạn.
6. **Kết nối server/gameplay**:
   - Chỉ khi endpoint chính xác được chứng minh từ cấu hình/report Cocos cũ, và không cần thay đổi server/network.
   - Kết nối AMOLX tới endpoint đó; quan sát handshake/login/server list/role/map. Không gửi credential vào log.
   - Vì AMOLX-03 đã phát hiện protocol enum/struct lệch, nếu fail login/role/map thì thu đúng packet-stage/error/log để xác định, không sửa server và không tự đổi hàng loạt enum.
   - Nếu endpoint không xác định hoặc cần thay đổi port-forward/firewall/server, dừng trước bước đó và báo cần người dùng phê duyệt cụ thể.
7. Kết thúc với APK và báo cáo rõ ràng. Không tự chuyển sang task tiếp theo.

## Kết quả mong muốn
Ưu tiên đạt:
- APK AMOLX mới build thành công.
- Vượt updater.
- Tới màn hình login.
- Kết nối đúng server JX1 hiện có.
- Nếu protocol tương thích đủ, vào được bản đồ và thao tác cơ bản.
Nếu không đạt, xác định đúng chặng bị chặn bằng log mới và báo cáo không phỏng đoán.

## Báo cáo cuối duy nhất
Tạo `TEST_RESULTS/AMOLX-07-ASSET-UPDATER-GAMEPLAY-20261116.md`:
- DONE/PARTIAL/BLOCKED/FAILED.
- Tóm tắt kết quả từng mốc: asset, updater, build, install, launch, login, server select, role select, map/gameplay.
- Cấu hình/manifest thử nghiệm và danh sách PAK đã dùng; nguồn từng PAK; không công khai host/IP/port nhạy cảm.
- Các file source AMOLX đã sửa và lý do; diff summary.
- Log lỗi đã lọc; HTTP/CURL status và byte count nếu thu được.
- APK path local, size, SHA-256, package/version/ABI.
- Bằng chứng ADB/emulator và ảnh màn hình local; không upload ảnh/log thô nếu có dữ liệu nhạy cảm.
- Server endpoint có dùng hay không, nguồn bằng chứng; không nêu credential.
- Những gì chưa kiểm thử và blocker chính xác.
- Chỉ stage/commit đúng các file source AMOLX thuộc task và báo cáo cuối; không commit asset/binary lớn hoặc secret. Push nếu quyền hiện có cho phép; nếu bị chặn giữ local và ghi đúng lỗi.
- Ghi commit SHA và link GitHub đã xác minh; không bịa SHA.
