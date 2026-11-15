# Bàn giao phiên khảo sát AMOLX JX1 và công việc Dispatcher

Ngày: 15/11/2026  
Repository bàn giao: `ndtangoss-dev/jx1-reports`, nhánh `main`.

## TÓM TẮT 5 DÒNG
1. Đã đọc trực tiếp, chỉ đọc source AMOLX tại `C:\JX1\jx1client-axmol-main\jx1client-axmol-main`; không sửa source, build APK hay kết nối server.
2. Luồng login/chọn server/chọn nhân vật/vào game đã được lần theo trong mã; có thể tiếp tục phát triển làm client JX1 nhưng chưa sẵn sàng cho gameplay.
3. Header protocol AMOLX lệch với client Cocos và server JX1; cần đồng bộ enum trước khi thử gameplay. Mã login còn lưu mật khẩu dạng rõ trong `accinfo.ini`.
4. Báo cáo Dispatcher trước đó ghi 10/10 unit test và fixture hoàn tất; trạng thái Task Scheduler hiện tại không xác minh được do lần truy vấn gần nhất bị từ chối quyền.
5. Báo cáo này không đánh dấu các phần build, chạy LDPlayer 14, kết nối VM thử nghiệm hoặc audit đầy đủ là đã hoàn thành.

Cần tôi quyết định: không

## Kết luận AMOLX

AMOLX có tiềm năng trở thành client mới cho JX1 Server hiện tại, nhưng bằng chứng hiện có chỉ hỗ trợ kết luận **có thể phát triển tiếp**, chưa đủ để kết luận tương thích gameplay. Phần định dạng đăng nhập và luồng chuyển từ Bishop sang game server có cấu trúc tương ứng; protocol gameplay có lệch chỉ số lệnh và chưa được kiểm nghiệm bằng build hay kết nối.

Các việc ưu tiên trước khi chạy thử:

1. Đồng bộ `KProtocolDef.h` theo một nguồn chuẩn đã xác định là đúng với server đang chạy; kiểm tra lại toàn bộ giá trị enum và packet handler, đặc biệt vùng từ `s2c_skillcast` trở đi.
2. Rà soát lưu thông tin đăng nhập. `MainLogin.cpp` dòng 127–136 ghi tài khoản/mật khẩu nhập vào `accinfo.ini` dạng rõ; cần thay bằng cơ chế không lưu mật khẩu dạng rõ trước khi phát hành hoặc dùng tài khoản thật.
3. Chuẩn bị Axmol 2.1.5 cùng `AX_ROOT`, xác nhận bộ Android SDK/NDK/Java tương thích, rồi build từ bản sao cô lập vì Gradle có thể xóa và tạo lại `proj.android/app/build/assets`.
4. Chỉ chạy APK trên LDPlayer 14 sau khi build thành công và xác nhận đích kết nối là VM thử nghiệm riêng. Chưa xác định được VM thử nghiệm đủ chắc chắn trong phần khảo sát này; không kết nối tới Main VM/server production.
5. Chuẩn bị bộ `.pak`/`.wor` và CDN thử nghiệm tương ứng. Gói AMOLX đã kiểm kê không có đủ dữ liệu bản đồ; updater lấy danh sách `paklist_vn.ini` và tài nguyên qua URL HTTP trong cấu hình package.

## AMOLX: phạm vi đã thực hiện

Source đã mở và đọc được ở chế độ chỉ đọc tại:

`C:\JX1\jx1client-axmol-main\jx1client-axmol-main`

Việc đọc các file thành công xác nhận tiến trình hiện tại có quyền đọc những đường dẫn đó. Không thực hiện phép thử ghi hoặc thay đổi ACL; source AMOLX không bị sửa, xóa, đổi tên hay ghi dữ liệu trong phiên.

Các file và vùng mã đã đọc:

- `README.md`, `CMakeLists.txt`, `proj.android/settings.gradle`, `proj.android/app/build.gradle`, `proj.android/gradle.properties`.
- `Source/AppDelegate.cpp`, `Source/gamescene/KUpdateLayer.cpp`, `MainMenu.cpp`, `SelServer.cpp`, `MainLogin.cpp` và các header liên quan.
- `Source/gameui/KSelPlayer.cpp`, `Source/gameui/KSelPlayer.h`, `Source/gamescene/KgameWorld.cpp`.
- `Source/gamecore/KProtocolDef.h`, `Source/gamecore/KProtocol.h`, `Source/gamecore/KProtocolProcess.cpp`.
- `Source/network/ClientStage.cpp`, `Source/network/SocketClient.cpp`, `Source/network/Cipher.h`, `Source/network/KSG_EncodeDecode.cpp` và `.h`.
- `Source/engine/KDownLoadFile.cpp` và cấu hình đóng gói trong `Content`. Tên từng file cấu hình Content không được ghi nhận trong bằng chứng của phiên, vì vậy không liệt kê tên cụ thể.
- Đã đối chiếu định nghĩa protocol với header client Cocos canonical trong cây `Folder/Client2912-.../Client2912/Client/Classes` và mã nguồn server JX1 trong cây `SwordOnline/SwordOnline/jxOnline/...`. Source server không mặc nhiên được xem là khớp với executable server đang chạy.

Nội dung đã xác minh từ mã:

- Luồng giao diện đi từ `KUpdateLayer` sang `MainMenu`, `SelServer`, `MainLogin`, `KSelPlayer`, rồi `KgameWorld`.
- Client gửi login với `KPROTOCOL_VERSION = 1`; mật khẩu được băm MD5 cho gói login. Sau phản hồi chọn nhân vật có địa chỉ/cổng/GUID, client nối game server và gửi `tagLogicLogin`.
- Luồng socket, mã hóa/giải mã packet và xử lý packet nằm trong các module network/protocol được liệt kê phía trên.
- `KProtocolDef.h` của AMOLX thiếu chín mục `s2c` có ở header tham chiếu: `s2c_npcsettmpcamp`, `s2c_npcstand`, `s2c_gm_synroleaction`, `s2c_queryiteminfo`, `s2c_returnitemlock`, `s2c_findpath_state`, `s2c_refitemsync`, `s2c_chestpwsync`, `s2c_extendchat_new`. Thứ tự enum đã khác tại vùng `s2c_skillcast`; `KProtocolProcess.cpp` xử lý tên lệnh này ở dòng 71. Chỉ số lệnh lệch có thể làm client và server diễn giải packet khác nhau.
- `MainLogin.cpp:127–136` ghi tài khoản/mật khẩu vào `accinfo.ini` dạng rõ; đây là rủi ro cần xử lý trước khi dùng tài khoản thật.
- CMake/Android build yêu cầu Axmol 2.1.5 và `AX_ROOT`. Axmol engine chưa có trong môi trường được kiểm tra trước đó nên build chưa chạy. Android SDK được ghi nhận là có sẵn, nhưng điều đó không thay thế các phụ thuộc còn thiếu.
- Không thấy dữ liệu `.pak`/`.wor` đầy đủ trong gói đã kiểm kê. Tải tài nguyên phụ thuộc cấu hình package và endpoint HTTP; chưa thử tải hoặc kết nối endpoint.

## AMOLX: chưa thực hiện

- Chưa build Android, chưa tạo APK và chưa chạy Gradle.
- Chưa cài/chạy APK trên LDPlayer 14; chưa kiểm thử nhập liệu, hiển thị, login hay gameplay.
- Chưa kết nối client tới VM/server nào; chưa xác minh VM thử nghiệm.
- Chưa xác minh bằng packet capture hoặc runtime rằng handshake, mã hóa, endian, packet size, login Bishop, chuyển game server và chọn nhân vật tương thích với executable JX1 Server hiện tại.
- Chưa xác minh nội dung thực tế của asset bên trong PAK/WOR hoặc tính khả dụng của CDN.
- Chưa hoàn thành audit toàn bộ mã nguồn AMOLX. Đây là khảo sát thực chất các luồng chính, nhưng chưa phải rà soát mọi module hoặc kiểm thử tích hợp.

## Dispatcher: công việc và bằng chứng đã có

Phần Dispatcher dưới đây là lịch sử công việc đã có bằng chứng trong workspace, không phải hoạt động được chạy lại khi chốt bàn giao này.

Các file Dispatcher cục bộ đang có thay đổi chưa commit:

- `docs-analysis/scripts/jx1_task_dispatcher.py`: polling GitHub theo chu kỳ, chỉ nhận task được duyệt, tải prompt/tài liệu tại commit ghim và kiểm tra hash/path, lưu state, chống chạy trùng, khóa tiến trình, phục hồi/resume và tạo báo cáo.
- `docs-analysis/scripts/install_jx1_task_dispatcher.ps1`, `uninstall_jx1_task_dispatcher.ps1`, `enable_jx1_task_dispatcher.ps1`, `disable_jx1_task_dispatcher.ps1`, `status_jx1_task_dispatcher.ps1`: đăng ký, gỡ, bật/tắt và xem trạng thái Task Scheduler.
- `docs-analysis/scripts/configure_jx1_codex_console.ps1`, `docs-analysis/scripts/test_jx1_font_coverage.ps1`: thiết lập UTF-8/font trong console hiện tại và kiểm tra glyph.
- `tmp_start_xingchi_codex.ps1` ở thư mục gốc repository: launcher Codex gọi helper UTF-8/font trước khi mở CLI.
- `docs-analysis/scripts/test_jx1_task_dispatcher.py`, `test_jx1_task_dispatcher_live.py`: unit test và fixture tích hợp có chọn bật.
- `docs-analysis/BAI_HOC.md`: bài học về mạng trong sandbox, logger khóa file, encoding PowerShell và stdout.
- Báo cáo/fixture local: `docs-analysis/reports/72-jx1-task-dispatcher-va-font.md`, các báo cáo `docs-analysis/reports/dispatcher-livefix-*.md`, `docs-analysis/out/jx1-dispatcher-fixture-20261115/` và `TEST_RESULTS/dispatcher-livefix-recovery-20261115-01.md`.

Các cập nhật workflow/queue đã được ghi nhận trên GitHub trong những commit trước: `WORKFLOW_JX1.md` (`65878e5b7ff06bc8fb9cf87684c32d173b621ca2`), `PROMPTS/00_CODEX_START_HERE.md` (`b35c3904bbedb23dd9406498e1ae431c40fcb151`), `PROMPTS/DISPATCH_QUEUE.json` (`24531873431794ca124a50e85d33eb9316858655`), prompt fixture (`806ff7e88b5ec165a4f1a2faf3be08a223818dc1`) và cập nhật queue hoàn tất (`1af2d05aaf3c37000a229353c417fa10d6f4279c`). Chúng không phải thay đổi AMOLX.

Kết quả theo `docs-analysis/reports/72-jx1-task-dispatcher-va-font.md`:

- Unit test: 10/10 đạt, bao gồm hồi quy xuất JSON tiếng Việt khi stdout ban đầu là `cp1252`.
- Preflight Codex read-only với model/provider/reasoning truyền tường minh: báo cáo ghi `JX1_DISPATCHER_PREFLIGHT_OK`.
- Fixture tích hợp GitHub → Dispatcher → Codex → báo cáo: Task ID `LIVEFIX-F9764FEC0E` được ghi `COMPLETED`; nội dung UTF-8 khớp và báo cáo fixture được upload.
- Kiểm tra glyph qua GDI ghi nhận Cascadia Mono và Consolas phủ các ký tự tiếng Việt đã kiểm tra. TUI Codex hiển thị trực quan và nhập liệu thực tế **chưa kiểm thử**.
- Báo cáo trước ghi Task Scheduler `JX1-Task-Dispatcher` ở `Running`, trigger `AtLogOn`, quyền `Interactive/Limited`, `IgnoreNew`; thao tác disable/enable đã kiểm tra. Windows reboot thật chưa kiểm thử.
- Lần truy vấn Scheduler gần nhất được ghi nhận bị `Access denied`; vì vậy trạng thái Task Scheduler và Dispatcher **hiện chưa xác minh được**. Không chạy lại preflight, Scheduler, credential, polling, fixture hay test Dispatcher trong bước bàn giao này.

Báo cáo `TEST_RESULTS/dispatcher-livefix-recovery-20261115-01.md` ghi fixture recovery local 31 byte UTF-8 tạo mới và so khớp SHA-256. Báo cáo đó nói rõ không đọc source, không chạy script, không dùng mạng/VM, và không kiểm chứng GitHub queue hoặc Dispatcher. Không xem fixture này là lần chạy end-to-end của Dispatcher.

## Lỗi còn tồn tại và hướng xử lý

- **Protocol enum AMOLX lệch:** đối chiếu toàn bộ ID `c2s`/`s2c` với header đúng của server đang chạy; giữ một nguồn chuẩn, cập nhật handler tương ứng và kiểm tra giá trị số của từng packet trước khi build.
- **Mật khẩu lưu dạng rõ:** bỏ việc ghi mật khẩu vào `accinfo.ini`; kiểm tra thêm log/cache để không lưu mật khẩu hoặc token ngoài ý muốn.
- **Thiếu Axmol 2.1.5/`AX_ROOT`:** chuẩn bị toolchain được ghim phiên bản trong thư mục build riêng; xác nhận build output không ghi vào source gốc.
- **Thiếu asset/CDN thử nghiệm:** chuẩn bị dữ liệu và endpoint thử nghiệm; xác nhận không trỏ nhầm tới production.
- **Chưa có VM thử nghiệm được xác minh:** xác nhận danh tính VM, IP và trạng thái cô lập trước mọi kết nối; hiện chưa có kiểm thử mạng.
- **Scheduler chưa xác minh:** trạng thái cuối cùng có bằng chứng thành công là `Running` theo report 72; reboot/resume thật chưa được thử.

## Git và bàn giao

Trạng thái local được kiểm tra trước khi tạo báo cáo:

- Branch: `master`.
- HEAD: `2a1c0d91023df05e65a78e9fc2d953eb79b0e16d`.
- Một thay đổi tracked chưa commit tại `docs-analysis/BAI_HOC.md` (14 dòng thêm); không có staged diff.
- Báo cáo này được tạo tại workspace trong bước bàn giao và đang là file untracked local; commit GitHub chỉ chứa báo cáo này.
- `git status` liệt kê nhiều file untracked tích lũy từ các công việc khác nhau, gồm báo cáo/fixture Dispatcher, báo cáo 67–71, output/log và backup. Không thể xác định thời điểm tạo chỉ từ trạng thái Git hiện tại.
- Repository local không có remote Git được cấu hình. Vì vậy, gửi lên `ndtangoss-dev/jx1-reports` được thực hiện như commit chỉ chứa báo cáo này qua GitHub, không đẩy các thay đổi local khác.
- Trước khi gửi, GitHub xác nhận repository tồn tại, nhánh mặc định `main`, quyền push có sẵn; đường dẫn `TEST_RESULTS/AMOLX-SESSION-HANDOVER-20261115.md` chưa tồn tại.
- SHA HEAD local được ghi ở trên. SHA commit GitHub tạo báo cáo sẽ có trong thông báo bàn giao cuối cùng và liên kết file. Không nhúng SHA commit chứa chính file vào nội dung, vì cập nhật file để ghi SHA sẽ tạo commit mới và làm SHA cuối thay đổi.

## Trạng thái cuối

- **Đã hoàn thành:** đọc/phân tích các luồng AMOLX được nêu; ghi nhận lệch protocol, cách login, rủi ro lưu mật khẩu và điều kiện build; lập báo cáo bàn giao local.
- **Đang làm:** không có tiến trình AMOLX đang chạy dở. Bước tiếp theo là xử lý vấn đề protocol/credential và chuẩn bị toolchain/build trên bản sao sau khi xác minh VM thử nghiệm.
- **Bị chặn:** build Android vì Axmol 2.1.5/`AX_ROOT` chưa sẵn sàng; kiểm thử kết nối vì chưa xác minh VM thử nghiệm; xác minh trạng thái Scheduler vì `Access denied`.
- **Chưa thực hiện:** LDPlayer 14, kết nối server, build, kiểm tra runtime, kiểm thử reboot Scheduler và audit toàn bộ AMOLX.