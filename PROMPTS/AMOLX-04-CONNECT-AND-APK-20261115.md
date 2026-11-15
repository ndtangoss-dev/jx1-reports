# AMOLX-04 — Kiểm tra kết nối server và build APK để người dùng test

Task ID: AMOLX-04-CONNECT-AND-APK-20261115
Executor: Codex CLI trực tiếp trong phiên hiện tại. Giữ nguyên cấu hình Sol Max.
Mục tiêu thời gian: mốc 1 trong 10 phút; mốc 2 trong 30 phút tiếp theo. Đây là timebox mục tiêu, không được giả nhận kết quả nếu chưa có bằng chứng.

## Mục tiêu người dùng

1. Trong 10 phút đầu: xác định AMOLX có kết nối được với đúng server JX1 hiện tại hay không. Nếu thiếu dependency thì cài; nếu protocol/client sai lệch thì sửa phía AMOLX trong phạm vi an toàn; kiểm tra kết nối thực tế nếu endpoint là môi trường test được phép.
2. Trong 30 phút tiếp theo: build APK AMOLX, xử lý lỗi build và chuẩn bị APK chạy được để người dùng tự test trên LDPlayer 14. Nếu có thể cài/chạy trên LDPlayer đã có sẵn thì thực hiện; không cài đặt/phần mềm hệ thống vượt quyền.

## Baseline bắt buộc — không làm lại

Dùng đúng báo cáo gần nhất:
- `TEST_RESULTS/AMOLX-GO-NO-GO-20261115.md`
- Prompt/checkpoint trước: `PROMPTS/AMOLX-03-GO-NO-GO-20261115.md`

Các đường dẫn đã xác nhận:
- AMOLX: `C:\JX1\jx1client-axmol-main\jx1client-axmol-main\Source`
- Cocos canonical (chỉ đọc/đối chiếu): `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes`
- GameServer source: `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver`
- Gateway/Bishop source: `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway`

Các lỗi đã xác minh cần xử lý ở AMOLX:
- S2C enum va chạm đầu tiên ID 95: C/G/B `s2c_npcsettmpcamp=95`, AMOLX lại đặt `s2c_skillcast=95`; C/G/B skillcast=96.
- AMOLX thiếu 9 S2C symbol; có 120 symbol chung lệch giá trị, nhưng các explicit ID/alias làm vùng sau không dịch đều. Không chỉ chèn 9 enum một cách máy móc.
- C2S nền login=65, logic-login=66, select role=108, walk=75, skill=77 khớp; nhóm C2S mở rộng còn lệch và Gateway B khác GameServer G.
- `tagNotifyPlayerLogin` AMOLX dự kiến 120 bytes, Cocos layout 184 bytes theo pack(1); server macro value chưa xác minh. `tagLogicLogin` dự kiến 17 bytes và source definitions align.
- Checkpoint trước ghi thiếu Axmol 2.1.5/`AX_ROOT`; chưa build, chưa có login/runtime test.
- AMOLX lưu mật khẩu rõ vào `accinfo.ini` tại `Source/gamescene/MainLogin.cpp:127–136`; xử lý để không ghi password rõ trước khi dùng tài khoản thật.
- Mâu thuẫn Gateway↔GameServer source và quan hệ source với executable đang chạy chưa được giải quyết.

## Giai đoạn 1 — 10 phút: xác định và thử kết nối

1. Resume đúng workspace/checkpoint; xem Git status/branch đúng một lần trước khi sửa. Giữ nguyên mọi thay đổi local có sẵn.
2. Xác định endpoint/server build hiện tại từ cấu hình/báo cáo đã có. Không in IP nội bộ, token, password, account hoặc secret vào báo cáo/Git.
3. Phân biệt rõ endpoint là test VM đã được xác nhận hay Main VM/production. Chỉ kết nối nếu xác định chắc chắn là test endpoint được phép. Nếu endpoint là Main VM/production hoặc không phân biệt được, không gửi packet/kết nối; dừng phần runtime, nêu chính xác cần người dùng xác nhận môi trường nào. Không tự đổi endpoint.
4. Chốt protocol contract dựa trên bộ Gateway/Bishop/GameServer thực sự đi cùng server thử nghiệm; nếu có executable/build manifest/report đối chiếu sẵn, dùng nó. Không suy luận executable từ source. Xử lý mâu thuẫn Gateway↔GameServer trước khi sửa enum.
5. Cài dependency còn thiếu nếu là công cụ phát triển an toàn, cần thiết cho AMOLX (ưu tiên Axmol 2.1.5, Android SDK/NDK/CMake/JDK phù hợp). Ưu tiên cài portable/workspace-local hoặc user-scope, ghi rõ phiên bản và vị trí. Không thay cấu hình Sol Max/Codex, không thay biến môi trường toàn hệ thống, không tự nâng cấp hàng loạt. Nếu cần Admin/UAC, tạo hướng dẫn/script có hoàn tác để chủ máy tự chạy; không vượt UAC.
6. Sửa sai lệch protocol trong bản AMOLX riêng: enum/reserved ID/alias, packet layout/packing/field width, framing/packet size table, dispatch/handler, Bishop handoff và lưu credential. Sửa đồng bộ theo contract đã xác minh, không chỉ thêm enum. Không sửa Cocos/server.
7. Chạy kiểm tra tối thiểu có thể chứng minh: compile phần protocol nếu khả thi; test packet size/offset hoặc unit test; kết nối TCP tới test endpoint chỉ khi được phép. Phân biệt TCP connect, handshake, login, vào world; không gọi TCP connect là login thành công.
8. Tại phút thứ 10, gửi cho người dùng một kết luận ngắn có bằng chứng: CONNECTED / TCP-ONLY / REJECTED / NOT-TESTED; lý do; những gì đã sửa/cài. Sau kết luận, tiếp tục ngay giai đoạn 2 trong cùng task, không chờ người dùng trả lời trừ khi gặp rào chắn cần quyết định.

## Giai đoạn 2 — 30 phút tiếp theo: build APK và chuẩn bị test

1. Dùng toolchain vừa xác minh/cài đặt; kiểm tra các dependency trực tiếp cần cho Android build. Không chạy lại preflight chung hay dò toàn repo.
2. Build APK debug cho ABI/Android phù hợp với LDPlayer 14. Tự xử lý lỗi trong phạm vi AMOLX/toolchain, tối đa 3 lần cho cùng một lỗi; không dừng để viết báo cáo trung gian.
3. Nếu build thành công, xác nhận file tồn tại, dung lượng, SHA-256, package name, version, ABI và đường dẫn APK. Nếu LDPlayer 14 đang sẵn có và có thể cài an toàn, cài và mở app; nếu không, bàn giao APK và lệnh cài rõ ràng.
4. Nếu kết nối test được phép, thử theo từng tầng: socket → protocol/handshake → login → server/role select → enter world. Chỉ ghi nhận tầng thực sự đạt. Không dùng tài khoản thật nếu còn lưu password rõ hoặc có nguy cơ lộ credential; dùng tài khoản test được cấp.
5. Nếu không thể đạt APK trong 30 phút, vẫn phải giao trạng thái build cụ thể: lệnh cuối, lỗi compiler/Gradle nguyên văn đã lọc secret, dependency còn thiếu, file đã sửa, bước tiếp tục ngắn nhất. Không giả vờ có APK.

## Rào chắn an toàn và phạm vi

- Chỉ sửa source AMOLX trong workspace riêng hoặc bản copy an toàn. Không sửa Cocos canonical, GameServer, Gateway/Bishop server source, executable server, Main VM, production hoặc cấu hình server.
- Không khởi động, restart, stop hoặc cấu hình lại bất kỳ EXE server nào. Không thay firewall, port-forward, Tailscale, router, credentials hoặc quyền truy cập.
- Không chạy JxStudio.exe, str_tool.exe, Autoupdate.exe. Không tự chạy S3RelayServer.exe hoặc bất kỳ server EXE nào.
- Không tải source/binary/log/dump dự án lên dịch vụ ngoài. Báo cáo GitHub chỉ chứa kết quả đã lọc secret và thông tin nội bộ nhạy cảm.
- Không reset/clean/checkout phá hủy, không ghi đè thay đổi local; chỉ stage/commit đúng file AMOLX thuộc task và báo cáo cuối.
- Không kiểm tra/sửa model/provider/reasoning/CODEX_HOME/CLI config. Không Dispatcher, không polling.
- Khi gặp lỗi, tự xử lý trong cùng task; một lỗi không thử quá 3 lần. Không tạo báo cáo từng lỗi. Chỉ dừng sớm nếu cần người dùng xác nhận endpoint production/test, cần quyền Admin/UAC, có nguy cơ ảnh hưởng dữ liệu/dịch vụ, hoặc blocker không thể xử lý an toàn.

## Báo cáo và bàn giao

Tạo đúng một báo cáo cuối:
`TEST_RESULTS/AMOLX-CONNECT-APK-20261115.md`

Báo cáo phải có:
- Kết luận kết nối tại mốc 10 phút: CONNECTED / TCP-ONLY / REJECTED / NOT-TESTED; endpoint chỉ ghi nhãn môi trường, không lộ IP/secret.
- Protocol contract được chọn và bằng chứng; mâu thuẫn server source còn lại.
- Dependency đã cài (phiên bản, phạm vi cài), file AMOLX đã sửa.
- Build command, kết quả, APK path, SHA-256, package/version/ABI; cài/chạy LDPlayer nếu đã thực hiện.
- Tầng runtime thực sự đạt: socket, handshake, login, chọn server/role, vào world.
- Tất cả lỗi đã gặp, cách khắc phục, kết quả, nguyên nhân còn tồn tại và hướng xử lý.
- Trạng thái DONE/PARTIAL/BLOCKED/FAILED; commit SHA/link. Không đưa secret vào báo cáo.

Commit/push duy nhất các file AMOLX thuộc task được phép và báo cáo cuối lên `ndtangoss-dev/jx1-reports` nhánh `main` theo quyền hiện có. Không stage file ngoài phạm vi. Nếu không thể push source (hoặc chính sách repo chỉ dành cho báo cáo), giữ source local, push báo cáo đã lọc secret và ghi rõ file nào chưa push cùng lý do. Không tuyên bố hoàn tất nếu không có bằng chứng.

**Ưu tiên tuyệt đối:** giao APK chạy được để người dùng test; không biến task thành audit hoặc báo cáo thuần túy.