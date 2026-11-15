# AMOLX-06 — Chẩn đoán updater dừng ở 6% (timebox 5 phút)

## Mục tiêu duy nhất
Trong tối đa **5 phút**, xác định bằng chứng gần nhất về nguyên nhân AMOLX-04/05 dừng ở khoảng 6% trước màn hình đăng nhập. Ưu tiên truy vết updater và dữ liệu PAK/CDN; không làm audit rộng, không sửa mò. Đầu ra là một kết luận kỹ thuật có thể hành động, có đường dẫn/file/symbol/dòng và phân biệt rõ VERIFIED / PROBABLE / UNKNOWN.

## Checkpoint đã biết — không làm lại
- APK AMOLX-04 đã build thành công; file:
  `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\handover\AMOLX-04-debug-arm64-v8a.apk`
- SHA-256: `D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1`.
- LDPlayer 9 smoke-test AMOLX-05: package `com.kull.jx1client`, INSTALL-OK, LAUNCH-OK, Axmol 2.1.5/OpenGL ES 3.1 và ARM64 native libraries nạp thành công; không crash/ANR trong khoảng quan sát.
- Runtime đứng ở khoảng 6%, UI hiện `package_vn.ini:545` và hộp thoại lỗi chữ bị sai mã hóa; chưa tới login. Chưa có bằng chứng runtime nào xác định URL/file tải thất bại.
- AMOLX source copy: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client`.
- AMOLX source cần xem trước: `Source/gamescene/KUpdateLayer.cpp`, `Source/engine/KDownLoadFile.cpp`, `Source/AppDelegate.cpp`, cấu hình updater/package trong `Content`.
- Cocos canonical (chỉ đọc): `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`.
- Cocos asset/CDN gốc (chỉ đọc): `C:\Jx1CocoV3\data_cdn\data`.
- Báo cáo Cocos V3 V002 xác nhận có `docs-analysis\tools\pak_extract.py`, `pak_replace.py`, `pak_verify.py`; file cấu hình `update10.pak` từng được đóng gói lại và game nạp được. Không suy ra rằng toàn bộ SPR/PAK đã được thay thế và kiểm thử.
- Báo cáo handover AMOLX cho biết gói AMOLX chưa có đủ dữ liệu bản đồ; updater lấy `paklist_vn.ini` và tài nguyên qua URL HTTP trong cấu hình package. Cần xác minh trên source/config thực tế, không mặc định kết luận này là nguyên nhân 6%.

## Phạm vi được phép
1. Đọc một lần Git status/branch trước khi ghi; giữ nguyên mọi thay đổi local hiện có. Không reset/clean/checkout và không stage file ngoài task.
2. Đọc đúng các source/config nêu trên và báo cáo AMOLX-05 / V002 / handover liên quan. Chỉ mở thêm file nếu được gọi trực tiếp bởi luồng updater.
3. Truy vết tuyến thực thi từ scene đầu `KUpdateLayer` → `startload()` → downloader → tải danh sách PAK → tải/kiểm tra/ghi file → trạng thái lỗi/hộp thoại. Ghi rõ điều kiện tạo thông báo và biến/mã lỗi gốc nếu xác định được.
4. Đối chiếu cấu hình URL, tên file, thư mục đích và manifest PAK của AMOLX với cấu trúc CDN/asset Cocos hiện có ở chế độ chỉ đọc. Không quét toàn bộ 3.2 GB; dùng tên file, cấu hình, manifest và truy vấn hẹp.
5. Nếu có thể xác định bằng chứng sẵn có (log/source/config) trong 5 phút, kết luận nguyên nhân và đề xuất patch nhỏ nhất. Nếu thiếu runtime evidence, nói rõ chính xác cần log gì để phân biệt DNS/HTTP/404/timeout/manifest/thiếu PAK/ghi file/checksum.
6. Chỉ khi phát hiện lỗi thuần túy, chắc chắn trong bản copy AMOLX (ví dụ đường dẫn local sai rõ ràng), được phép sửa tối đa một thay đổi nhỏ có thể hoàn tác, không thay URL/host/port/credential hay chính sách mạng. Nếu không rõ, không sửa; ghi patch đề xuất.
7. Kết thúc đúng timebox. Không tự mở rộng thành build/test; báo cáo có thể kết luận rằng cần task AMOLX-07 riêng để instrument log và chạy lại smoke-test.

## Cấm / rào chắn
- Không sửa Cocos canonical, asset gốc, CDN gốc, source server, EXE server, VM, firewall, Tailscale, router, port-forward hoặc bất kỳ cấu hình mạng nào.
- Không kết nối Main VM/server đang chạy; không thử endpoint updater/game server, không gửi packet, không login, không dùng tài khoản/mật khẩu. Không khởi chạy APK trong task này vì updater tự chạy mạng; AMOLX-05 đã cung cấp bằng chứng màn hình.
- Không tải lại asset, không copy/ghi đè PAK vào CDN, không xóa cache/dữ liệu LDPlayer, không uninstall/reinstall app.
- Không chạy server EXE, `Autoupdate.exe`, `JxStudio.exe`, `str_tool.exe` hoặc `S3RelayServer.exe`.
- Không build APK trong timebox này; không đổi model/provider/reasoning/CODEX_HOME/CLI config; không Dispatcher.
- Không upload source, binary, asset, dump, ảnh hoặc log thô ra ngoài. Báo cáo GitHub chỉ chứa kết luận đã lọc thông tin nhạy cảm.
- Không làm lại protocol audit, kiểm kê port/EXE, inventory toàn repo, hay bất kỳ công việc AMOLX-01..05 đã có checkpoint.

## Báo cáo cuối duy nhất
Tạo `TEST_RESULTS/AMOLX-UPDATER-6PCT-DIAG-20261116.md` với:
- Trạng thái DONE/PARTIAL/BLOCKED.
- Kết luận ngắn: root cause VERIFIED / PROBABLE / UNKNOWN.
- Bảng từng chặng updater: source file + symbol/dòng + hành vi + bằng chứng.
- Bảng so sánh cấu hình AMOLX với Cocos/CDN: URL (che host/secret nếu nhạy cảm), manifest, file, đường dẫn, trạng thái có/không/chưa xác minh.
- Giải thích hộp thoại sai mã hóa có phải nguyên nhân hay chỉ là lỗi hiển thị.
- Nếu chưa kết luận được: nêu đúng một bước kế tiếp có giá trị nhất (ví dụ instrument downloader để log URL đã che, HTTP status, bytes, destination, checksum/error code rồi build và smoke-test).
- Những gì không chạy/không xác minh; không khẳng định runtime success từ static source.
- Chỉ stage/commit đúng file báo cáo; push lên `ndtangoss-dev/jx1-reports` nếu quyền hiện có cho phép. Nếu push bị chặn, giữ file local và ghi đúng lỗi; không thay credential/config.
- Ghi SHA commit và link GitHub khi có bằng chứng. Không tạo báo cáo phụ.

## Tiêu chí hoàn tất
Trong 5 phút phải có báo cáo có căn cứ hoặc ghi rõ blocker và bằng chứng còn thiếu. Không được chỉ lập kế hoạch, không vượt phạm vi để cố đạt kết luận.
