# AMOLX-10 — Báo cáo tổng hợp updater, server list, đăng nhập và gameplay

- Ngày: 16/11/2026, múi giờ UTC+7.
- Trạng thái tổng thể: **PARTIAL**; đăng nhập hiện **BLOCKED** bởi lỗi layout giao thức.
- Kết luận: đã vượt updater, hiển thị đúng một server test và đạt TCP/handshake; **chưa đăng nhập thành công, chưa vào bản đồ và chưa test di chuyển/đánh quái**.
- Báo cáo credential chi tiết: [AMOLX-CREDENTIAL-TRACE-20261116.md](AMOLX-CREDENTIAL-TRACE-20261116.md).
- Cần người dùng quyết định: không đối với bàn giao này. Bước tiếp theo cần cho phép sửa AMOLX và tạo APK mới; chỉ thị không build lại vẫn được giữ trong lượt tiếp tục/bàn giao.

## Tóm tắt 5 dòng

1. Ba dòng Server Test 1 cũ là placeholder FairyGUI còn sót khi nạp sai đường dẫn cấu hình, không phải ba endpoint game độc lập.
2. Bản APK đã build/cài trước chỉ thị không build lại đã dùng đúng cấu hình, hiển thị một server JX1 Mobile TEST và vượt updater.
3. Đã khôi phục credential testlocal từ lịch sử Claude, lưu an toàn và thử trên APK hiện có; không reset account hoặc sửa DB.
4. Phản hồi runtime xác nhận mã 10 LOGIN_R_INVALID_PROTOCOLVERSION: KLoginAccountInfo AMOLX thiếu nEnterMapIdx, ngắn hơn 4 byte.
5. Chưa kiểm thử gameplay; không sửa server/VM/mạng và không tiếp tục Dispatcher. Lượt cuối chỉ tổng hợp và xuất bản báo cáo.

## Phạm vi thực tế và trình tự

Báo cáo gộp các kết quả AMOLX-10 và credential trace đã thực hiện trước đó. Phân biệt giai đoạn sửa/build APK đã hoàn tất trước chỉ thị không build lại với giai đoạn tiếp tục chỉ truy tìm, thử APK hiện có và chẩn đoán chỉ đọc. Lượt gửi Git không chạy lại audit, build, ADB, đăng nhập hoặc kiểm tra Dispatcher.

Không tuyên bố mục tiêu gameplay end-to-end hoàn tất. Thời gian log Android dùng đồng hồ emulator; thời gian JSON metadata có UTC và đã quy đổi sang UTC+7 khi nêu rõ.

## Updater và dữ liệu server list

### Nguồn ba dòng trùng

AMOLX trước đó đọc đường dẫn runtime sai: \Settings\Ver_vn\FsjxClient.ini. Ba dòng Server Test 1 là mục mẫu trong FairyGUI. Logic cũ chỉ xóa mẫu sau bước Load, nên Load thất bại để nguyên cả ba mục. Những mục mẫu không có ID/data server hợp lệ; khi chọn, index = -1 và endpoint rỗng.

Không còn log chính xác tại thời điểm người dùng nhấn từng placeholder cũ, vì vậy không gán errno TCP lịch sử cho ba lần đó. Source/UI và trạng thái dữ liệu giải thích được ba dòng; không coi chúng là ba máy chủ đã được xác minh khác nhau.

Cấu hình runtime đúng: \update10\FsjxClient.ini, mục Region_0, Count = 1, tên JX1 Mobile TEST. Chỉ có **một endpoint được cấu hình: 100.95.186.86:56722, TCP**. Tuyến canonical/forwarder đến Bishop 192.168.1.50 đã có bằng chứng trước đó; nhiệm vụ không đổi route, forwarder hoặc port.

Bản sửa dùng danh sách dữ liệu data/paklist.ini thay guard paklist_vn.ini rỗng; nạp cấu hình đúng và loại bỏ placeholder trong logic UI. Không xóa hoặc chỉnh cấu hình server/VM để làm biến mất ba dòng.

### Kết quả updater

Bằng chứng đã có ghi HTTP 200, count 35 và loadSuccess; update10 và script_skill tải thành công. File PAK đọc chỉ đọc từ app:

- Local: amolx-work/AMOLX-04-20261115/build/amolx10-device-update10-readonly.pak.
- Kích thước: 10.882.596 byte.
- SHA256: f2ab0d337971119b4504073f7b0a7a7e3b96dda9aee86f8e279f7c473ec480be.
- Hash trùng docs-analysis/out/tailscale/update10.pak hiện có.

Không build lại hoặc thay CDN trong lượt truy tìm credential/bàn giao.

## Những thay đổi và APK đã có

Các thay đổi dưới đây được thực hiện trên bản copy C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client, trước yêu cầu không build lại; không sửa Cocos canonical.

| File trong bản copy | Mục đích đã thực hiện |
|---|---|
| Source/gamescene/SelServer.cpp | Sửa đường dẫn cấu hình/runtime guard, bỏ mục UI mẫu khi nạp danh sách và dùng endpoint có dữ liệu hợp lệ; thêm bằng chứng trạng thái kết nối. |
| Source/gamescene/SelServer.h | Khai báo/trạng thái hỗ trợ logic chọn server đã sửa. |
| Source/network/SocketClient.cpp | Ghi metadata TCP và handshake để xác định tầng lỗi, không ghi payload đăng nhập. |

Backup local: build/amolx10-server-fix-before/. Các sửa manifest/updater thuộc những giai đoạn AMOLX trước đã có checkpoint; lượt xuất bản này không kiểm kê lại hoặc gộp chúng vào commit báo cáo.

APK đã kiểm thử: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx10-v3-serverfix-signed-amolx04-20261116.apk.

- SHA256: C9A13AE3313AD16B683BB6266B868C509DF07B0F418E93246E6FB2BCF4B8FD83.
- Build đã chạy trước đó: BUILD SUCCESSFUL, 51 giây, 65 tasks, 7 executed.
- Dùng debug keystore có sẵn; certificate SHA256: 84341660dceade5c34308f2780a840fe87dfebf6be9d3edafec64e784fe85b7d.
- Xác minh chữ ký v1/v2/v3 đạt; adb install -r trả Success, giữ dữ liệu ứng dụng.
- Thiết bị đã xác định: LDPlayer 9, serial emulator-5554; package com.kull.jx1client; activity org.axmol.app.AppActivity.

Không chạy lại build/install trong lượt tiếp tục đăng nhập hoặc gửi báo cáo. Source copy, backup, APK và log local không nằm trong commit này.

## Đăng nhập testlocal: kết quả và nguyên nhân

### Credential lịch sử

Đã hoàn thành truy tìm trong dữ liệu Claude cục bộ và Credential Manager theo phạm vi của báo cáo kèm theo. Tìm được credential lịch sử gắn với testlocal và log Login Success! ngày 11/11/2026 lúc 10:18:53. Đã lưu vào Windows Credential Manager, không xuất mật khẩu hoặc hash. **Log lịch sử không chứng minh AMOLX hiện tại đã đăng nhập thành công.**

Đã nhập credential khôi phục trên APK hiện có, làm sạch ô nhập sau lỗi ký tự do thao tác Enter và nhập lại không Enter. Đã mở lại riêng app để thử kết nối mới, không xóa dữ liệu/emulator. Lần thử mới tiếp tục bị chặn ở protocol.

### TCP và handshake đã đạt

Metadata log đã lọc theo đồng hồ emulator:

| Thời điểm 16/11/2026 | Bằng chứng |
|---|---|
| 13:09:51.810 | AMOLX_NET stage=tcp_start endpoint=100.95.186.86 port=56722 immediate=0 errno=115 |
| 13:09:51.825 | AMOLX_NET stage=tcp_ready socket_error=0 |
| 13:09:51.825 | AMOLX_NET stage=handshake bytes=34 protocol=32 mode=0 |
| 13:09:51.825 | AMOLX_NET stage=handshake result=ok; AMOLX_SERVER result=ready_for_login |

errno 115 ở connect không chặn thành công tiếp theo: socket_error = 0 và handshake = ok đã được ghi nhận. Không còn căn cứ quy lỗi hiện tại cho tuyến TCP.

Trước khi mở lại app từng có 149 byte nằm trong receive queue. Sau mở lại riêng app, luồng nhận đã tiêu thụ dữ liệu (rx_queue = 0), sau đó TCP chuyển CLOSE_WAIT, nhưng phản hồi login vẫn mang mã lỗi 10. Không kết luận receive queue là nguyên nhân cuối.

### Bằng chứng runtime xác nhận sai layout

Đã dùng run-as và quyền đọc bộ nhớ của chính app test để đọc vùng đệm được xác định từ symbol/DWARF của thư viện native đã build. Không ghi bộ nhớ app, không lưu dump/payload; chỉ lưu các trường metadata cần thiết. PID tại checkpoint là 12585, không khẳng định PID đó còn tồn tại khi đọc báo cáo.

| Trường phản hồi runtime | Giá trị đã xác minh |
|---|---|
| Message | 65 / s2c_login |
| Declared struct size | 146 byte |
| Param | 0x0005000a |
| Action | LOGIN_A_LOGIN |
| Result | 10 / LOGIN_R_INVALID_PROTOCOLVERSION |
| ProtocolVersion theo offset AMOLX | 0 |
| ProtocolVersion theo offset canonical | 1 |

| Thuộc tính KLoginAccountInfo | AMOLX đang cài | Cocos/Bishop tham chiếu; phản hồi runtime |
|---|---|---|
| Kích thước struct | 142 byte (0x8e), DWARF xác minh | 146 byte theo header runtime |
| nEnterMapIdx | Thiếu | Có, trước ProtocolVersion |
| Offset ProtocolVersion tính từ đầu struct | 138 (0x8a) | 142 |

Kết luận có bằng chứng: thiếu trường 4 byte làm gói gửi ngắn hơn và Bishop đọc ProtocolVersion sai vị trí, trả mã 10 trước kiểm tra mật khẩu. Không cần reset account hoặc thay đổi server để xử lý lỗi layout này.

### Vì sao giao diện không hiện thông báo lỗi rõ ràng

MainLogin::ProcessAccountLoginResponse kiểm tra account/password echo trước khi xử lý mã lỗi. Response từ chối sớm không khớp echo, nên bị bỏ qua trước nhánh thông báo version. Các so sánh accountMatches = false và passwordMd5Matches = false trong phản hồi lỗi **không chứng minh mật khẩu sai**.

MainLogin có scheduleUpdate; không chẩn đoán lỗi này là thiếu scheduleUpdate. Mật khẩu hiện tại còn CHƯA XÁC MINH vì chưa vượt bước kiểm tra version.

### Source đã đối chiếu chỉ đọc

Root AMOLX copy: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\Source.

| File/symbol | Số dòng tham chiếu | Nội dung xác minh |
|---|---|---|
| gamescene/LoginDef.h | 80, 84–102 | Mã lỗi 10; header/struct thiếu nEnterMapIdx, ProtocolVersion ở dòng 102. |
| gamescene/MainLogin.cpp | 42; 139–151; 238–289 | Có scheduleUpdate; tạo/gửi gói; kiểm echo trước xử lý lỗi; nhánh version. |
| network/ClientStage.cpp | 174, 280, 345 | Buffer giải mã, framing và luồng nhận. |
| network/SocketClient.cpp, Thread.cpp, IOBuffer.*, ClientStage.h | Đọc theo nhánh chẩn đoán | Kiểm tra kết nối và luồng buffer; không sửa trong lượt truy tìm. |

Canonical: C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamescene\LoginDef.h, dòng 100 có unsigned int nEnterMapIdx; ProtocolVersion dòng 103.

Bishop tham chiếu: C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway\Sources\MultiServer\Bishop\GamePlayer.cpp: WaitForAccPwd dòng 811, kiểm version dòng 842, đọc nEnterMapIdx dòng 856, tạo lỗi version dòng 862, gán version/size/id/gửi ở 1384/1388/1394/1399.

Giới hạn: mã nguồn Bishop có thể không trùng executable chạy thực tế. Kết luận không chỉ dựa trên source: response runtime 146 byte, mã 10 và version đúng tại offset canonical là bằng chứng trực tiếp bổ sung.

## Ma trận nghiệm thu trung thực

| Hạng mục | Trạng thái | Bằng chứng/giới hạn |
|---|---|---|
| Vượt updater | PASS trong lần chạy đã ghi | HTTP 200, count 35, loadSuccess. |
| Một server hợp lệ | PASS | amolx10-v3-server-list.png; cấu hình Count = 1. |
| Build APK đã sửa server list | PASS ở giai đoạn trước | BUILD SUCCESSFUL 51s; không build lại. |
| Chữ ký và cập nhật giữ dữ liệu | PASS ở giai đoạn trước | v1/v2/v3 và install -r Success. |
| Mở form login | PASS | Ảnh/log của APK hiện có. |
| TCP và handshake | PASS | tcp_ready socket_error=0, handshake ok. |
| Truy tìm credential lịch sử | DONE trong phạm vi đã nêu | Claude JSONL + báo cáo 19 + file-history + vault thật. |
| Xác thực testlocal hiện tại | BLOCKED | LOGIN_R_INVALID_PROTOCOLVERSION; chưa đánh giá được password. |
| Chọn nhân vật | CHƯA THỰC HIỆN | Chưa vượt login. |
| Vào bản đồ | CHƯA THỰC HIỆN | Chưa vượt login. |
| Di chuyển, đánh quái | CHƯA THỰC HIỆN | Chưa vào bản đồ. |
| Sửa layout login/build APK mới | CHƯA THỰC HIỆN | Giữ chỉ thị không build lại. |
| Unit test/ABI test cho bản sửa protocol | CHƯA CHẠY | Chưa có bản sửa protocol. |
| Preflight/Dispatcher/Scheduler | KHÔNG CHẠY LẠI | Ngoài nhiệm vụ hiện tại; không kết luận trạng thái hiện thời. |

## Bằng chứng local đã có, không đẩy log thô

Root: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build.

- amolx10-login-protocol-metadata.json: metadata blocker; recordedAt 2026-11-16T07:21:35.641Z = 14:21:35 UTC+7.
- amolx10-login-connect-safe.log: metadata TCP/handshake đã lọc.
- amolx10-restart-login-result.png và amolx10-fresh-clean-login-result.png: trạng thái form login, không coi là thành công.
- amolx10-restart-login.log và amolx10-login-app-excerpt.log: bằng chứng chẩn đoán local; không đẩy nguyên log.
- amolx10-v3-server-list.png, amolx10-v3-login-screen.png, amolx10-v3-startup-excerpt.log, amolx10-v3-login-connect-excerpt.log: kết quả APK trước đó.

Không công bố ảnh/log/raw payload trong commit; báo cáo chỉ trích metadata tối thiểu. Lượt xuất bản kiểm tra lại file metadata đã lưu, không chạy lại phiên game.

## Bước tiếp theo đề xuất

Khi có phạm vi sửa/build APK mới: thêm nEnterMapIdx vào đúng vị trí KLoginAccountInfo phía AMOLX, khởi tạo giá trị phù hợp, bổ sung kiểm tra size/offset của request/response, xử lý mã lỗi từ chối trước khi đòi echo thành công và kiểm tra bounds trước đọc struct. Không đổi server hoặc canonical để né lỗi version.

Sau build/ký cùng khóa và cài cập nhật giữ dữ liệu, thử lại login bằng credential lưu trong vault. Chỉ khi qua login mới xác minh chọn nhân vật, handoff, bản đồ, di chuyển và đánh. AMOLX-03 còn các lệch handoff dự kiến 120/184 byte, S2C skillcast 95/96 byte và enum gameplay; đây là checkpoint tồn đọng, chưa được sửa hoặc xác minh runtime lại trong lượt này.

## Git và ranh giới thay đổi

- Đã kiểm git status/diff của C:\Jx1CocoV3 trước ghi: nhánh master, HEAD 2f7aa0c39be94b86cbd077bf85e24b4855873e27.
- Có sẵn docs-analysis/BAI_HOC.md sửa thêm 14 dòng cùng nhiều untracked source copy/backup/báo cáo/script khác. Giữ nguyên; không stage/reset/clean hoặc đưa vào commit bàn giao.
- Source AMOLX copy và APK vẫn local, không được push trong lần này. Không có thay đổi Dispatcher mới, không xác minh lại Scheduler/credential polling.
- Chỉ xuất bản hai Markdown: TEST_RESULTS/AMOLX-10-GAMEPLAY-TEST-20261116.md và TEST_RESULTS/AMOLX-CREDENTIAL-TRACE-20261116.md.
- Repository đích ndtangoss-dev/jx1-reports, nhánh main, commit cha 39b97e0b0fa061bae2e847c462b8f0e0158dfa9e. Tạo commit chỉ với hai file trên từ tree của main và cập nhật nhánh có kiểm tra HEAD, không đẩy lịch sử repository source.
- SHA của commit xuất bản được xác minh sau khi tạo và cung cấp trong lời bàn giao. Không tự nhận toàn bộ workspace sạch.

Không reset mật khẩu/tạo account/sửa DB, không sửa Cocos canonical, VM, server, firewall, Tailscale, forwarder hoặc CDN trong lượt truy tìm tiếp tục và bàn giao. Không gỡ app, clear data hoặc reset emulator.
