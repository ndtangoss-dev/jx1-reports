# BÀN GIAO

File ngắn. Chỉ ghi điều không có ở chỗ khác. Ai tiếp quản đọc file này sau `README.md`.

## Bản bàn giao hiện tại
- Thời điểm: 2026-11-21 16:31 (hook PreCompact tự ghi đè)
- Việc đang chạy (TASKS status running): SC-006
- Thư cuối đã nhận: #157
- Sắp nén ngữ cảnh: PM mới đọc LUAT-COT-LOI.md, TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md rồi lịch sử chat; chi tiết việc dở ở dòng trạng thái cuối TRANG-THAI.md.

## Nhật ký tiếp quản
| Thời điểm | Ai (model, tài khoản) | Kết quả tự kiểm tra | Sai lệch đã sửa |
|---|---|---|---|
| 2026-11-16 | Sonnet PM, phiên Claude Code `C:\Jx1CocoV3` | Đã đọc README, quy tắc, backlog; nhánh khớp | Chưa có |
| 2026-11-16 22:40 | Sonnet PM, cập nhật bản bàn giao (thử vòng 0-08) | Đã ghi lại việc dở và điều chưa kiểm | Bản cũ ghi "không có việc dở", đã sửa |

## Đổi tài khoản / phiên mới (#108.4)
- Khi chuyển tài khoản Claude: đăng nhập lại Claude Code, rồi gõ `/tiep-tuc`. Bước đầu của `/tiep-tuc` là đọc `STATE/LUAT-COT-LOI.md`. Hook SessionStart (startup, resume, compact) cũng tự in file này vào ngữ cảnh (`TOOLS/hook_luat.py`).

## Bàn giao đổi tài khoản 19/11 21:50 — Sonnet A (theo #272)
**Việc dở**
- **#268 vc23 (ưu tiên cao nhất):** cây build `D:\JX-build\qh9A` (đã vá trực tiếp; bản gốc `Classes\network\SocketClient.cpp.bak-vc23`). Thêm bộ đo mạng vào `SocketClient.cpp`: mỗi giây ghi `/data/data/com.jxclient.hoiuctruyenky/files/jx_net.log` (gói/byte gửi-nhận, trễ gửi→nhận kế tiếp TB/max ms); tắt bằng file `jx_netlog.txt` nội dung `0`. `versionCode 23`. Lần build đầu lỗi do `<chrono>` → đổi `clock_gettime`; build lại bằng `D:\JX-build\build-vc23.ps1` (xong khi có `D:\JX-build\build-vc23.done`, log `build-vc23.log`). Kế tiếp: kiểm aapt2/apksigner (cert `a48601f7…`)/SHA256, chép `D:\JX1_U003_build\serve\jx-goc-v23-….apk` (không vào git), Artifact có nút Sao chép như `scratchpad\link-apk-v22.html` (http://100.95.186.86:8091/…), đo trước/sau (LD emulator-5556, `TOOLS/bench/do_muot_khung.py` + jx_net.log), ghi hướng dẫn vào BAO-CAO-CHU, `A Chat`. Chưa làm: dự đoán chạy/đánh, gộp gói, giảm trễ nội suy (công tắc `jx_interp.txt` "0" đã có).
- **ĐÍNH CHÍNH:** KHÔNG phải client thiếu TCP_NODELAY — cây build qh9A đã có (fix33) và sleep nhận 2 ms (fix34); chỉ bản trong repo chính C:\Jx1CocoV3 thiếu. Trễ ~150 ms là RTT Tailscale/5G, ngoài tầm client. Nguyên nhân còn lại có thể: nhịp logic 18 Hz, nội suy tới ~55 ms, sửa vị trí từ server (B lo #B-026).
- **#269/#270 chùy cấp 1:** Test-36 `gs\script\System\online.lua` có `JXGive269()` (bản gốc `online.lua.bak-269`), cờ `gs\Logs\jx269_given.txt`; phát 1 chùy cấp 1 +15 (`AddItem(0,0,4,1,…,1,15,0)`) cho `chuvuongtestaa`. CHƯA xác nhận chủ đã nhận (cần chủ đăng nhập; kiểm cờ qua WinRM, báo A Chat "chùy cấp 1 trong túi"). Sau đó viết `REPORTS/` so chùy cấp 1 (obj-adha01.spr) với cấp 10 (obj-adha04.spr) cho lỗi hiệu ứng 2 tay (không sửa mã hiệu ứng vũ khí, Q-52; xem VK-04-set-hai-tay.md).
- **#271 gs001:** khởi động lại 21:29:27 (pid 1820 qua JX-ChainUp); nạp bản đồ ~10-12 phút, trong lúc đó Bishop báo "máy chủ chưa hoạt động" — bình thường. Chờ log `chain_up.log` "CHUOI LEN DU" (~21:40); xác nhận bằng `TOOLS/vm_chay.py ports` và log bishop có "GS Send,LogIn Succes". Lỡ gọi `vm_chay.py chain-up` thêm 1 lần lúc 21:34, không thấy gs001 thứ hai.
- **Forwarder Tailscale:** đã chuyển sang Test-36 bằng `docs-analysis\scripts\chuyen_forwarder_sang_t36.ps1` (chủ chạy qua CHAY-CHUYEN-T36.bat Admin); 100.95.186.86:56722/51189 → 192.168.56.150, chỉ cho 100.123.183.6. Máy host lỗi WMI: dùng netstat/Stop-Process, không taskkill.
**Lệnh/tiến trình đang chạy nền:** build gradle vc23 (ẩn, BelowNormal); Test-36 chuỗi server + gs001; không dừng khi chủ đổi tài khoản (Q-56).
**Chưa kiểm:** vũ khí #257 (9 món cấp 10) chủ đã nhận đủ chưa; LimitFPS 30/60; đo nội suy ON/OFF; APK vc22 gọi địa chỉ nào ở bước chọn máy chủ so với P46/P47; dọn file mật khẩu trên Desktop; CDN/forwarder tạm.
**Đường dẫn:** APK vc22 `D:\JX1_U003_build\serve\jx-goc-v22-noisuy.apk`, SHA256 `b235e8642137b0635161d22dd6d297b9bc4881332d6f2bf7b4d8aa1eceb76873`; link http://100.95.186.86:8091/jx-goc-v22-noisuy.apk. Tài khoản test: `tkchuvuong` (nhân vật `chuvuongtestaa`); mật khẩu ở Credential Manager/`%LOCALAPPDATA%\jx1-secrets`, không ghi vào kho. Hộp thư: `HOP-THU/CHO-SONNET.md` (đến #272), trả lời `TU-SONNET.md`, báo chủ `BAO-CAO-CHU.md`. Báo Chat: gõ `A Chat …` vào tab Chat (Chrome tab claude.ai/chat/75ee9a0d…). Khi mở phiên mới: `/tiep-tuc`.

## Cập nhật 19/11 22:15 — Sonnet A: vc23, #274/#275, chuyển tài khoản (theo #276)
**vc23 (gộp vk04, Q-84)** — cây dựng `D:\JX-build\qh9A`, `versionCode 23`, script `D:\JX-build\build-vc23.ps1` (kết quả `build-vc23.log/.done`). Có 2 thay đổi, đều có công tắc (tệp trong `/data/data/com.jxclient.hoiuctruyenky/files/`, nội dung `0` = tắt):
1. Đo mạng phía máy khách `SocketClient.cpp` (bản gốc `.bak-vc23`): ghi `jx_net.log` mỗi giây `tx/rx byte, tre_n/tre_tb/tre_max` (ms từ gói gửi cuối tới gói nhận đầu). Tắt: `jx_netlog.txt`=0.
2. vk04 sét chùy hai tay `vn/gamecore/KNpcResVN.cpp` (bản trước `.bak-vc23`; nguồn `D:\JX-build\qh9A-vk04`): vẽ thêm tia cho lớp thứ hai khi ≥20 điểm và ≥40% lớp chính. Tắt: `jx_vk04.txt`=0. Đã kiểm LD trước khi gộp (REPORTS/VK-04-set-hai-tay.md). Bản vc23 gộp: CHƯA kiểm trên LD/điện thoại tới khi chủ cài.
Nội suy 18→60 Hz giữ như vc22 (`jx_interp.txt`=0 tắt). Ra tệp `D:\JX1_U003_build\serve\jx-goc-v23-….apk` (không vào git). Chưa có số đo trước/sau từ điện thoại: cần chủ chơi vc23 rồi đọc `jx_net.log`.

**#275 nghẽn gs001 (đo console, 19/11)**: rỗi `SvrFPS 18/18`, tick avg ≈0,7 ms. Có người đăng nhập: 21:44 avg 40 ms/max 973 ms (over 189); 21:49 avg 116 ms/max 864 ms (over 572), SvrFPS 16; lúc thoát avg 75 ms/max 678 ms, SvrFPS 15; ngay sau khi thoát lại 0,3 ms. Tức tick nặng GẮN VỚI người chơi đang online (cả lúc vào, cả lúc chơi), không phải mạng. Chưa xác định phần tốn (online.lua / AI quái / ghi log): cần thử hoàn tác tạm `online.lua` (bản `.bak-269`, `.bak-257`) và đo lại cùng cách (đăng nhập 1 phút, đọc dòng `tick avg`). Hoàn tác phải khởi động lại gs001, mất ~11 phút nạp bản đồ.
**Làn lệnh gs001 lúc chủ đánh (21:49–21:51)**: kỹ năng nhận 525, chạy 80; `skill_over`(bị ghi đè) 291, `busy discard` 154 → ~85% lệnh kỹ năng không chạy (làn lệnh giữ 1 ô kỹ năng). Nhất quán với "quái đánh mãi không chết".
**Kỹ năng đánh thường của vai `chuvuongtestaa`**: chưa kiểm xong (chưa đọc danh sách kỹ năng đã học; log tải `LoadPlayerFightSkillList` báo thành công). Chủ nói chỉ đánh được sau khi nhận kỹ năng → nghi vai tạo bằng `bot_tao_role.py` chưa có kỹ năng cơ bản gán phím.
**Chùy cấp 1 vs cấp 10**: đã phát chùy cấp 1 (`JXGive269`, cờ `gs\Logs\jx269_given.txt`), chờ chủ so hiệu ứng, chưa viết REPORTS so sánh.
**Chuyển tài khoản**: `/tiep-tuc`; mọi việc nền ở trên; không có việc đỏ treo.

| 2026-11-19 23:10 | Sonnet PM (tai khoan moi), /tiep-tuc | dong_bo OK (het UU); vc23 SHA256 cdef8446 + cert a48601f7 khop BAO-CAO-CHU; D tat, chi JX-Test-36 chay; thu den #276 da xu ly | Chua kiem: RAM (WMI loi), tieu yeu, bench vc23 tren LD |

| 2026-11-21 10:21 | Sonnet A, /ket-thuc-ca (#343,#344) | Test-36 tắt sạch 10:20 sau Online=0; TU-SONNET + TRANG-THAI đã lưu; push | Bật lại: chờ gs001 7–10 phút; làm các mục "Chưa kiểm" ở TRANG-THAI |

| 2026-11-21 16:25 | Sonnet A (phiên mới), /tiep-tuc sau tắt máy | Git khớp origin (06b6843c); thư cuối A #345 đã xử lý, không có thư mới. VM: máy mới mở, cả 3 VM tắt. Bốn `find.exe` Git kẹt (20/11→, ~36 triệu handle) làm VBox không bật được VM (VBoxDrvStub 0xc0000004): đã Stop-Process, VM bật được. Bật headless JX-Test-36 và JX-Server-D 16:20. | Test-36 không ping được: card Host-only máy thật rơi về 169.254.83.226 (cần 192.168.56.101); netsh cần Admin, bị chặn; chủ chạy `docs-analysis/scripts/dat_ip_hostonly_56.ps1` (Admin, có -Undo). Chuỗi server chưa lên (D: chỉ SQL 1433 mở). TongQuan còn DISABLED, chưa bật. |
