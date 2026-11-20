# QUYẾT ĐỊNH ĐÃ CHỐT

Chỉ ghi quyết định đã chốt. Muốn đổi thì thêm dòng mới, không sửa dòng cũ.

| # | Ngày | Quyết định | Ai chốt | Nguồn |
|---|---|---|---|---|
| Q-01 | 2026-11-16 | Thế giới Bot dùng chung: mọi người chơi thấy cùng một Bot; A giết Bot thì Bot chết với tất cả; trạng thái Bot quản lý tập trung | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/03`, `owner-inputs/05` |
| Q-02 | 2026-11-16 | Bỏ Secret Vault và bảo mật phức tạp | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/03` |
| Q-03 | 2026-11-16 | Dùng lại client và server JX1 gốc; bỏ hướng client Axmol mới và server mới | Chủ dự án | `owner-inputs/05` |
| Q-04 | 2026-11-16 | Người chơi thật không thấy nhau ở bản đồ thường; chỉ thấy nhau trong hoạt động được chủ dự án bật, có giới hạn số người | Chủ dự án | `owner-inputs/05` |
| Q-05 | 2026-11-16 | Opus lập kế hoạch; Sonnet là PM có toàn quyền; Fable kết thúc | Chủ dự án | `owner-inputs/05`, `06` |
| Q-06 | 2026-11-16 | Bỏ ChatGPT, 8 phòng ban, Dispatcher | Chủ dự án | `owner-inputs/06` |
| Q-07 | 2026-11-16 | Toàn bộ quy trình và tiến độ lưu trên một nhánh riêng (`jx1-ops`) | Chủ dự án | `owner-inputs/06` |
| Q-08 | 2026-11-16 | Thay AI, tài khoản, model bất cứ lúc nào không mất tiến độ | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/04` |
| Q-09 | 2026-11-16 | Bot chỉ triển khai sau khi mô hình server mới được thử nghiệm và kiểm chứng | Chủ dự án | `owner-inputs/05` |
| Q-10 | 2026-11-16 | **Đồng ý** đưa source (đã lọc dữ liệu tài khoản, không PAK, APK, exe) lên repository GitHub riêng tư `jx1-source` (D1) | Chủ dự án | Tin nhắn 16:41 |
| Q-11 | 2026-11-16 | **Bỏ hẳn AMOLX**, chỉ dùng client Cocos V3 (D2) | Chủ dự án | Tin nhắn 16:41 |
| Q-12 | 2026-11-16 | Codex CLI dùng model Sol Max qua xingchi, **không đổi model**; ngân sách khoảng 2.000 USD; được dùng nhiều worker Codex để đẩy nhanh tiến độ | Chủ dự án | Tin nhắn 16:41 |
| Q-13 | 2026-11-16 | D3: nền thử chuyển đổi là VM thử `JX-Test-36` với server tự dựng 36 Hz; Main VM không đụng | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-14 | 2026-11-16 | D4: giao hàng với mọi hoạt động tắt cho người thật thấy nhau; chủ dự án bật sau | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-15 | 2026-11-16 | D5: giữ kênh chat thế giới như game gốc ở bản đồ thường | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-16 | 2026-11-16 | D6: Sonnet dùng danh sách cho phép + danh sách cấm (`TOOLS/settings.mau.json`), không bỏ qua mọi hỏi đáp. Chủ dự án duyệt `KE-HOACH-TONG-THE.md`; Codex giữ nguyên model và cấu hình; PM tự động, báo một lần mỗi ngày | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-17 | 2026-11-16 | **Không bật VM nào ở chế độ bridged (hoặc nối thẳng vào LAN nhà) khi chủ dự án chưa cho phép.** Thay Q-13 ở điểm "dùng bridged": `JX-Test-36` dùng Host-only. Lý do: mạng nhà (mesh) sập tối 16/11 sau khi bật VM thử, chưa xác định nguyên nhân | Chủ dự án | Tin nhắn tối 16/11 |
| Q-18 | 2026-11-16 | Quyền tự chủ với Main VM `JX-Server-D`. **Được tự làm, không hỏi:** bật headless khi đang tắt; xem trạng thái; kiểm tra Windows và chuỗi server game đã lên chưa (chỉ đọc); khởi động chuỗi server đúng thứ tự trong `KHOI_DONG_CHUOI_SERVER_D.md` nếu chưa lên. **Vẫn cấm nếu chưa nói rõ:** tắt, reset, sửa cấu hình VM, đổi mạng, chụp snapshot, xóa hay sửa dữ liệu, cài đặt, sửa file trong Main VM | Chủ dự án | Tin nhắn tối 16/11 |
| Q-19 | 2026-11-16 | (1) Chuỗi server game (PaySys, Goddess, S3Relay, Bishop, gs001 và exe server đi kèm đã biết): PM tự khởi động, dừng, khởi động lại trong `JX-Test-36` bất cứ lúc nào; trong Main VM chỉ khởi động theo Q-18; không cần hỏi. (2) Exe lạ, chưa từng chạy: chỉ chạy trong VM thử, sau khi lưu SHA-256 và quét Defender; không cần hỏi. (3) Vẫn cấm: chạy exe của gói game trên máy thật; chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe` ở bất kỳ đâu. (4) Quy định "mỗi exe server cần phê duyệt riêng" trong AGENTS.md cũ trên main hết hiệu lực (ghi rõ khi làm 0-06). (5) Ưu tiên script 0-07 khởi động chuỗi bằng một lệnh, không bấm nút Startup của Bishop bằng tay qua ảnh chụp | Chủ dự án | Tin nhắn tối 16/11 |
| Q-20 | 2026-11-16 | (1) Main VM: kiểm hồ sơ mạng trước; nếu bị đổi sang Public thì đổi lại Private; cổng đã mở thì không thêm luật. (2) Nếu cổng vẫn đóng: thêm luật tường lửa Inbound mở 5985, 1433, 5002 **chỉ cho IP máy thật 192.168.1.12**; ghi luật cũ và lệnh hoàn tác vào `ENVIRONMENT.md`; không mở cho cả mạng, không tắt tường lửa. (3) Từ giờ, câu hỏi nào đang chờ chủ dự án trả lời thì PM vẫn làm các việc khác trong backlog, không dừng lượt để chờ | Chủ dự án | Tin nhắn tối 16/11 |
| Q-21 | 2026-11-16 | Không bao giờ kết thúc lượt bằng câu hỏi. Việc nhỏ hoặc có mặc định hợp lý: PM tự quyết và ghi vào bảng này. Chỉ hỏi khi quyết định không đảo ngược được hoặc cần quyền của chủ dự án (Admin, tiền, xóa dữ liệu, mở cổng ra ngoài...); hỏi xong vẫn làm việc khác (Q-20). Hook Stop `TOOLS/stop_guard.py` (khai báo ở `.claude/settings.json`) chặn dừng lượt khi BACKLOG còn task chưa xong và không bị chặn; được dừng khi Codex chạm trần ngày (dòng `Hôm nay: N USD` ≥ 200, hoặc ≥ 1.000 USD / 7 ngày, hoặc thẻ `[CODEX-CHAM-TRAN]`), một task lỗi 3 lần liên tiếp (`lỗi liên tiếp: 3` trong `TASKS/<ID>.md`), việc bắt buộc cần chủ (ghi thẻ `[DUNG-CAN-CHU yyyy-mm-dd HH:MM]` + lý do vào TRANG-THAI trước, hiệu lực 12 giờ), hoặc chủ gõ `/ket-thuc-ca`. Hết an toàn: chặn tối đa 60 lần một phiên | Chủ dự án | Tin nhắn tối 16/11 |
| Q-22 | 2026-11-16 | Trần tạm Codex do PM đặt vì chưa có đơn giá USD (0-10): tối đa 3 worker song song; dừng giao Codex khi 7 ngày ≥ 700 USD hoặc trong ngày tăng ≥ 150 USD; chủ dự án cập nhật số thật thì sửa lại. Việc nhỏ có mặc định, tự quyết theo Q-21 | PM (Q-21) | 0-10 |
| Q-23 | 2026-11-16 | Worker Codex phải tách khỏi phiên Claude Code: giao bằng `TOOLS/chay_codex.ps1` (Task Scheduler, giới hạn thời gian 0, log `D:\JX-wt\<ID>.codex.log`, cờ xong `<ID>.done`), không dùng `Start-Process` trực tiếp vì tiến trình con nằm cùng Job Object với shell của phiên (đã đo; có bị giết khi đóng phiên hay không CHƯA kiểm). Khi hạn mức phiên PM >80%: giao sẵn hàng đợi tối đa 3 worker theo Q-22, mỗi worker một task có prompt trong file, rồi PM nghỉ; kết quả đọc lại khi phiên mở | PM (yêu cầu chủ 16/11) | 0-07 |
| Q-24 | 2026-11-16 | Chủ dự án cho phép tăng số worker Codex khi Codex chậm: nâng trần Q-22 từ 3 lên tối đa 6 worker song song, vẫn giữ trần USD của Q-22 và khóa vùng file (mục 12). Chỉ tăng khi đã thấy chậm bằng số đo, không tăng khi Codex lỗi | Chủ dự án (tin nhắn 16/11 tối) | A-03, A-06 |

| Q-25 | 2026-11-16 | Chủ dự án cho phép khôi phục model Codex = Sol Max. Tên chính xác: `gpt-6.1-sol` + `model_reasoning_effort=max` (nguồn: config.toml `review_model`, lệnh 0-03 chạy được ghi ở ENVIRONMENT.md, `/v1/models` xingchi chỉ trả `gpt-6.1-sol` và `gpt-6-astra`). Cố định bằng tham số `--model` trong `TOOLS/chay_codex.ps1`; không sửa config.toml | Chủ dự án | Tin nhắn 16/11 |
| Q-26 | 2026-11-16 | Bot: chọn hướng (a) bot thô qua giao thức, chưa vá server. Mốc đầu = 1 Bot đăng nhập, đi, đánh. Trần Bot online ban đầu 100; đo tải rồi mới tăng. Dormant/Background = Bot ngoại tuyến, tiến bộ (EXP, vật phẩm) qua Lua server. Song song: Codex tìm gốc crash gs001 tự dựng (A-07) | Chủ dự án | Tin nhắn 16/11 |
| Q-27 | 2026-11-16 | Nhịp server (đối chiếu 18/36/54 Hz): **bản chạy thật và mặc định là 18 Hz** (`GAME_FPS 18`, `KSOServer.cpp:90`; báo cáo 41, 45 mục 5). 36 Hz là nhánh thử `C:\JX\Bisect\T4` (`LogicFps=36`, đã chạy thử, chưa giao người dùng, đường dẫn chưa kiểm lại: báo cáo 45, 59). 54 Hz là kế hoạch, chưa làm (báo cáo 59). Mọi con số sức chứa/đo tải của Bot tính ở 18 Hz | PM | Báo cáo 41, 43, 45, 59 |
| Q-28 | 2026-11-16 | Cơ chế Admin tự chủ an toàn (chủ dự án yêu cầu): chủ máy chạy `TOOLS/setup_quyen_admin.ps1` Admin đúng 1 lần; nó đăng ký 4 scheduled task `JX1-ADMIN-{kill-test-vm,firewall,trustedhosts,service}` chạy SYSTEM/Highest, cho tài khoản chủ máy quyền `schtasks /run` (không UAC). Danh sách việc cố định, tham số kiểm chặt theo `C:\ProgramData\JX1_ADMIN\config\allowed.json` (chỉ Admin sửa): chỉ diệt VBoxHeadless của `JX-Test-36` (tuyệt đối từ chối `JX-Server-D`, kiểm cả PID); luật tường lửa chỉ tên `JX1-AUTO-*`, cổng và IP thuộc danh sách; TrustedHosts chỉ IP trong danh sách, không `*`; dịch vụ chỉ start/enable trong danh sách, không stop/disable. Mọi việc ghi `log\admin.log`. PM kích hoạt bằng `TOOLS/admin_chay.ps1`. Mở cổng vẫn phải đúng danh sách cổng đã duyệt | Chủ dự án | Tin nhắn 16/11 |
| Q-29 | 2026-11-16 | Hộp thư `HOP-THU/` là kênh chính thức Chat ↔ Sonnet (chủ dự án chỉ nói chuyện với Chat): Chat viết `CHO-SONNET.md`, Sonnet viết `TU-SONNET.md`. Sonnet đọc hộp thư đầu ca (`/tiep-tuc`), sau mỗi task và trước khi dừng (`stop_guard.py` chặn dừng khi còn thư chưa xử lý, trừ thư đánh dấu [ĐANG CHỜ]); sau mỗi mốc lớn viết 5–10 dòng vào `TU-SONNET.md`. Quyết định chính thức vẫn do Sonnet ghi vào file này; không để bí mật trong hộp thư (kho public). | Chủ dự án (qua Chat) |
| Q-43 | 2026-11-17 | Mục tiêu hiệu năng client (thư #069/#070, chủ duyệt): giai đoạn 1 = tối ưu ở 90 FPS (mức tối đa thanh trượt, KuiOptions.cpp:182-192) để chủ chơi thử; giai đoạn 2 = 120 FPS ổn định, chưa làm. H-15: đo 30/60/90 trước khi sửa; đề xuất sửa gửi Chat duyệt thiết kế; sau duyệt sửa trên BẢN SAO client, dựng APK thử tên riêng; không đụng D:\Android\Client gốc, không đụng backup qh7; kiểm lại hiệu ứng vũ khí +6/+12/+15 và H-14. Việc gom: DESIGN/TOI-UU-120FPS.md. |
| Q-44 | 2026-11-17 | Mở rộng worker (thư #071, chủ duyệt thường trực): tới 20 khóa (Q-41), ≤3 worker/khóa, trần worker có thể nâng 16→20 khi đủ khóa, không cần hỏi chủ. Chia task thành mảnh ≤30 phút, độc lập, có checkpoint commit. Giữ watchdog E-13b (im 10 phút chạy lại khóa khác; ≥3 im cùng lúc = sự cố nhà cung cấp, dừng giao mới, thăm dò 2 phút/lần). Giữ trần mềm 400 USD/ngày và dừng báo ở 1.500 USD tích lũy; báo cáo 30 phút/lần; chỉ đọc/đo trừ khi duyệt thiết kế sửa. Bảng hiệu quả thêm: tỉ lệ cache/đầu vào (hôm nay ~81%), độ trễ trung bình (39,5 s). |
| Q-45 | 2026-11-18 | Chủ duyệt (chat 00:4x, "Ok"): lập đội test tính năng game (DESIGN/DOI-TEST-TINH-NANG.md). Được tạo tài khoản/nhân vật test trong DB của VM thử `JX-Test-36` cho các vòng T-02..T-04, có ghi chú hoàn tác, cô lập khỏi dữ liệu thật; không dùng Main VM ngoài Q-18; không đưa tài khoản vào báo cáo. Giao qua Tổng quản. |

## Chờ chủ dự án
Không còn mục chờ về mạng: máy thật đã có Host-only `192.168.56.101`, không cần đổi. Chủ dự án chỉ cần xác nhận đã đọc báo cáo mạng trong `ENVIRONMENT.md` trước khi tôi tiếp tục dùng VM thử.

| Q-46 | 2026-11-18 | Chủ xác nhận: "chuẩn hóa" = CHUẨN HÓA DỮ LIỆU GAME (giải mã TCVN3 ↔ UTF-8 ↔ tên Hán; bảng ánh xạ tên trang bị/quái/NPC/bản đồ/kỹ năng), không phải chuẩn hóa báo cáo. K-03 làm trước; R-* chỉ chạy tiếp con nào đang chạy, không mở lại con chết. Model Codex chưa đổi (thử gpt-6/gpt-5.6 đều lỗi/timeout). | Chủ (chat) |

| Q-47 | 2026-11-18 | **Lời chủ ở phiên Claude Code, khung 22:00 17/11 → 01:00 18/11 (đọc lại từ lịch sử chat theo #107.6; giờ trong jsonl là UTC, +7 = địa phương).** (a) Sau chuẩn hóa thì kiểm kê asset; việc chỉ đọc/báo cáo được gọi thêm tiểu yêu, chia nhỏ để tránh 429; dùng tổng quản để PM không thành nút thắt, không giảm tiểu yêu vì PM quá tải. → `TASKS/K-02` (kiểm kê asset) chia theo loại asset, làm SAU chuẩn hóa. (b) Chủ hỏi môn phái Võ Đang: nhánh, số skill mỗi nhánh, cấp học → ghi câu #0 ở KIEM-TRA/NHAT-KY-HOI-DAP.md, chấm "Một phần". (c) Chủ hỏi "làm chủ asset gốc bao nhiêu %": trả lời solid/yếu, 28 bản đồ `gs001` thiếu `.wor` (A-01 dòng 71) → `REPORTS/ASSET-LAM-CHU.md`. (d) Chủ muốn áp khuôn mới cho TOÀN BỘ báo cáo cũ và đang chạy để đồng bộ, dễ tìm ("thà mất công lúc đầu") = chuẩn hóa báo cáo (khớp L5). (e) 17:07 chủ: xingchi quá tải chung, "cứ mở lên thoải mái"; 17:14 khóa xingchi tạo từng cái khi cần, trần 20; 17:31 mở lại sau 120 giây, lập đội test tính năng game (Q-45); 17:36 test trên VM hiệu quả hơn, bỏ T-01; 17:40 xem việc chuẩn hóa có nặng quá thì chia nhỏ. Q-46 bị thay bằng L5/#107: chuẩn hóa = khuôn báo cáo + giải mã tên + sắp theo cấu trúc game; K-03 là phần giải mã tên. |

- Q-#137 (Chat quyết thay chủ, 18/11 11:27): trần đồng thời tạm 10 tiểu yêu, không tạo khóa mới, giao tăng dần 2/4/6/8/10 mỗi bước chờ 3 phút. Đảo được.

- Q-48 (chủ, 18/11 16:36): BỎ người gác (tốn hạn mức Claude). Chủ chỉ làm việc với Chat, không giao việc trực tiếp cho Sonnet. Chat và Sonnet làm việc qua hòm thư theo đợt; chủ chỉ nhắn Sonnet một câu cố định "Đọc hòm thư CHO-SONNET rồi làm." khi Chat báo có thư. Chi tiết: STATE/QUY-TRINH-KHONG-NGUOI-GAC.md.

- Q-49 (chủ, 18/11 19:23): XOAY VÒNG TỰ ĐỘNG: Chat và Sonnet bám bảng tiến độ + kế hoạch tổng thể làm không nghỉ; chủ chỉ quyết việc quan trọng (vùng Đỏ). Sonnet đánh thức Chat bằng cách gõ "xong" vào cuộc chat qua Claude desktop; Chat đẩy thư rồi ghi dấu mốc để Sonnet nhận. Chi tiết và phanh: STATE/QUY-TRINH-VONG-TU-DONG.md. Thay phần "chủ gọi/chủ nhắn" của Q-48.

## Q-50 — 18/11/2026 21:04 — Chủ duyệt 5 mục (câu "Duyệt 1-5")
(1) thử Gemini miễn phí, chỉ việc đọc không nhạy cảm; (2) thử client C01+C03 (C02/C04/C05 chưa); (3) A-07 bước 2–6 trong VM kể cả snapshot, dựng lại từ snapshot đã vá; (4) cửa sổ Tổng quản đã hết nháy; (5) tạo kho riêng PRIVATE `jx1-source` (0-05). Vòng tự động (Q-49) chạy lại.
- 0-05 giữ cục bộ theo chủ (#178, 18/11): D:\jx1-source + tag baseline-20261116, không đẩy GitHub.

## Q-51 — 18/11/2026 22:10 — Bỏ nhánh Gemini miễn phí; áp dụng đề xuất giảm token ít rủi ro (Chat, theo #181)
Gemini miễn phí chỉ 20 lượt/ngày/mô hình: không dùng được (REPORTS/SO-SANH-NHA-CUNG-CAP.md). xingchi vẫn là đường chính; thay nhà cung cấp trả phí chờ chủ quyết sau, chưa gấp. Áp dụng từ REPORTS/TIEU-YEU-429-VA-TOKEN.md: #3 (xoay khỏi K5, tránh phát việc dồn 17h–19h nếu việc không gấp), #5 (K5 tối đa 2 việc), thử #1 (high thay max cho việc đọc-tóm, kiểm 2–3 việc so mẫu), #2 (mẫu prompt nêu sẵn danh sách tệp). Để lại #4, #6, #7.

## Q-52 — 18/11/2026 22:16 — Chủ chốt 4 điều
(1) Sonnet không bao giờ hết việc: dùng `STATE/HANG-DOI-VIEC.md`. (2) Hiệu ứng vũ khí sửa mãi không được → hiểu game trước, KHÔNG sửa mã hiệu ứng tới khi có tài liệu hiểu được Chat duyệt (W-01). (3) Giữ phiên Sonnet mở cả đêm. (4) Chat cập nhật tiến độ/kế hoạch để giao việc (hàng đợi + bảng tiến độ).

## Q-53 — 18/11/2026 22:25 — Sonnet gõ "CHAT" để đánh thức Chat khi cần hỏi (chủ chốt). "xong" = hết đợt; "CHAT" = có câu hỏi. Chi tiết: QUY-TRINH-VONG-TU-DONG.md.

## Q-54 — 18/11/2026 22:50 — Chờ dài bằng LỆNH CỐ ĐỊNH `TOOLS/cho_thu.py` + nhịp tim (chủ: không thể phải thức gõ tay cả đêm)
Vòng ngủ do Sonnet tự viết không đáng tin (đêm 18/11 đứng im sau #186/#189 mà không ai biết nó sống hay chết). Từ giờ: chờ = chạy `python TOOLS/cho_thu.py` (tối đa 55 phút/lượt; thoát mã 10 = thư mới, 11 = có việc chờ gộp, 12 = hết hạn). Lệnh tự ghi `HOP-THU/NHIP-TIM.md` và đẩy lên kho mỗi 5 phút: Chat/chủ nhìn tệp này (hoặc `git log`) để biết Sonnet còn sống. Chat sẽ đọc nhịp tim mỗi lần thức; nhịp tim cũ hơn 15 phút = Sonnet treo → ghi BAO-CAO-CHU.

## Q-55 — 18/11/2026 23:58 — Chủ dặn: tắt Server D + LDPlayer-D khi không test điện thoại; luôn ≥8 tiểu yêu (2/khóa); kiểm RAM và báo bất thường
Chủ nói rõ (tháo hạn chế "không tắt" của Q-18 CHỈ cho việc tắt sạch khi không test): tắt `JX-Server-D` và LDPlayer nối D; bật lại khi chủ báo ra test. Tiểu yêu ≥8 việc đồng thời, mỗi khóa tối đa 2. Kiểm RAM máy thật mỗi đợt, báo ngay phần bất thường để chủ quyết tắt. Chi tiết: LUAT-COT-LOI.md L11.
| Q-56 | 2026-11-19 | CHỦ CHỐT: Chat không bao giờ ra lệnh cho Sonnet dừng; Sonnet làm liên tục, toàn quyền chủ động để không dừng (trừ vùng Đỏ). Chỉ "dừng vòng" của chủ mới tạo DUNG-VONG.flag. Ghi ở LUAT-COT-LOI.md (luật tối thượng), SO-TAY-CHAT, KHOI-DONG-CHAT. | Chủ |
| Q-57 | 2026-11-19 | CHỦ: xingchi GPT 1x rate, +1000 USD, tổng >3000 USD; cho mở tiểu yêu không giới hạn khi cần (tăng dần, theo dõi RAM); trần ngày/tuần nâng 1000/3000 USD. | Chủ |

## Q-58 (chủ 19/11 07:02)
Chủ DUYỆT: (1) cấp khóa client đúng bản APK + tài khoản/vai thử cho Bot trên Test-36 (khóa KHÔNG vào repo) để chạy E-01/E-05/E-09/B-04/C-01/P-02; (2) duyệt thử client C02, C04, C05. SAU KHI 1 VÀ 2 XONG: (3) bật Server D + LDPlayer-D cho chủ test trên điện thoại. TRƯỚC KHI bật D: kiểm lỗi vẽ sai thứ tự giữa vũ khí (đặc biệt thương/giáo) và nhân vật khi CHẠY BỘ, đủ 8 hướng, rồi báo chủ. Chỉ kiểm/quan sát, chưa sửa mã hiệu ứng vũ khí khi chưa có bằng chứng + Chat duyệt.

## Q-59 (chủ 19/11 07:16) — TIỂU YÊU TESTER (nhiệm vụ quan trọng phần test game)
1. Trên server test (Test-36): bật 1 LDPlayer test đặt tên theo tiểu yêu tester (vd T36-tester01), tạo 1 tài khoản test và cấp riêng cho 1 tiểu yêu. Giao nhiệm vụ: tìm hiểu game như tester thật; hiểu đến đâu lưu vào 1 bộ nhớ knowledge (file riêng); Sonnet/Chat kiểm soát xem nó làm có hiệu quả không. Mục tiêu dài hạn: nhiều tester chạy cùng lúc, báo lỗi phát hiện, tìm hiểu game như người thật.
2. Chỉ khi tester đầu chạy ổn (có knowledge hữu ích, lỗi báo đúng, không treo) mới sinh tester kế tiếp.
3. Báo cáo tiến độ tester thường xuyên cho chủ.

## Q-60 (chủ 19/11 07:23) — CẤU TRÚC KHO TÀI LIỆU TESTER (bổ sung Q-59)
Kho kiến thức và bảng lỗi PHẢI chia nhánh theo từng mục (thư mục STATE/TESTER/KIEN-THUC/<mục>/ và STATE/TESTER/LOI/<mục>/), ví dụ: dang-nhap (cần làm gì, lỗi phát hiện, báo cáo ra sao), tao-nhan-vat (tạo thế nào, chọn ngũ hành thế nào), mon-phai (môn phái nào cần ngũ hành nào: vd Võ Đang, Côn Lôn cần ngũ hành Thổ → Sonnet hiểu và ra lệnh tiểu yêu lập đúng môn phái/ngũ hành cho từng ca test), di-chuyen, chien-dau, tui-do, shop, nhiem-vu... Có mục lục INDEX. Kho phải đủ để tiểu yêu chết thì con sau vào thay đọc là hiểu ngay, KHÔNG dò lại từ đầu, và làm tiếp việc dang dở (cần file TRANG-THAI/NHAT-KY-VIEC-DANG-DO cập nhật liên tục: đang ở bước nào, tài khoản/nhân vật nào, việc kế).

## Q-61 (chủ 19/11 08:38) — Test hiệu ứng vũ khí cận chiến
Trên Test-36, tạo MỘT LẦN đủ các loại vũ khí cận chiến: kiếm, đao, thương, chùy, song đao, bổng; mỗi loại chỉ cần test CẤP 15. Sau đó test 8 hướng (thứ tự vẽ vũ khí/nhân vật khi chạy bộ). Chỉ kiểm/quan sát, chưa sửa mã hiệu ứng. Bước bật Server D vẫn sau khi kiểm xong.

## Q-62 (chủ 19/11 08:41) — DUYỆT thiết kế BOT v1
Chủ DUYỆT DESIGN/BOT/THIET-KE-BOT-v1-DUYET.md (3 loại BOT, 5 giai đoạn, file giá gia-vat-pham, cổng duyệt). Thực hiện theo thứ tự: xong #216 (khóa Bot, thử client, vũ khí +15 8 hướng #219, bật D) và tester01 (#217/#218), rồi GĐ0 khảo sát A/B → GĐ1 … → GĐ4. Sonnet khảo sát và chọn hướng nhẹ nhất cho game.

## Q-63 (chủ 19/11 09:00) — MỞ MẪU SỐ BẢNG TIẾN ĐỘ
Chủ lệnh cập nhật phần mới vào bảng tiến độ để mẫu số tăng. Thay #212 (đóng băng 107): từ 09:00 mẫu số = 107 + 16 hạng mục mới (VK-01..03, TS-01..04, BT-01..06, HT-01..03) = 123. Đếm vẫn NGHIÊM (xong đúng chữ tên việc). Chủ biết % sẽ giảm lúc đầu.

## Q-64 (chủ 19/11 10:07) — Sét vũ khí hai tay
Chủ quan sát ảnh #219: vũ khí hiện ở hai tay (chùy → song chùy, thích → song thích) mà hiệu ứng sét +15 chỉ chạy ở MỘT bên. Yêu cầu: cả hai bên vũ khí đều có sét chạy. Bước 1 kiểm/chứng minh + tìm gốc; sửa mã hiệu ứng chỉ khi có bằng chứng + Chat duyệt (luật cũ). Thêm hạng mục VK-04 vào bảng.

## Q-65 (Chat 19/11 10:25) — DUYỆT hướng Bot A và quy trình sửa sét hai tay
(1) BOT GĐ0 (chủ ủy quyền "Sonnet khảo sát rồi quyết hướng nhẹ nhất", 19/11 08:17): Chat duyệt hướng A (Bot ngoài server qua giao thức) cho GĐ1 và GĐ3; hướng B (NPC hình người trong server) giữ làm nghiên cứu cho Bot dân số, quyết sau khi có thang đo tải. Thang thử tải 1→5→20→50→100 chỉ trên Test-36, canh RAM. (2) VK-04 sét hai tay: Chat duyệt theo 2 bước: đo n section bằng g_jxTrace trước; nếu n≥2 mới sửa KNpcResVN.cpp theo đề xuất, chỉ trên bản thử Test-36 (APK T36test), JX1_EFFECT_OK=1 chỉ cho commit đó; APK giao chủ là vùng Đỏ, chờ chủ.

## Q-66 (chủ 19/11 10:22) — Chủ xác nhận: SỬA sét hai tay và LÀM THEO #226
Chủ đồng ý cho sửa VK-04 và làm hướng Bot theo #226/Q-65 (hướng A, thang đo tải trên Test-36). Quy trình 2 bước và an toàn của #226 giữ nguyên.

## Q-67 (chủ 19/11 10:37) — THỐNG NHẤT MỘT BẢN APK GỐC [PHẦN "QH9A LÀ GỐC" ĐÃ BỊ Q-68 THAY THẾ; phần "một bản gốc, bỏ bản khác, cài lại được" vẫn hiệu lực]
Chủ: cứ dựa theo bản test hiện tại (dòng qh9A) và bám theo nó để làm tiếp; mọi bản khác cho phép BỎ để khỏi rối. Chủ chấp nhận cài lại điện thoại (gỡ rồi cài mới nếu cần). Hiệu lực từ lần này trở đi.

## Q-68 (chủ 19/11 10:39) — SỬA Q-67: BẢN GỐC = BẢN T36test ĐANG CHẠY
Chủ: khỏi quan sát lại. Lấy đúng APK đang chạy trong T36test (SHA-256 7894c22d…2d8 (A3a, vc20; số 8da22c0c là số cũ, sai), package com.jxclient.hoiuctruyenky) làm BẢN GỐC; điện thoại chủ cài theo bản đó. Thay cho "qh9A" trong Q-67.

## Q-69 (chủ 19/11 10:50) — MỖI TIỂU YÊU TESTER DÙNG RIÊNG MỘT KHÓA
Việc test game nặng: một tester = một khóa xingchi (JX-K*), không chia khóa đó cho tiểu yêu khác; tiểu yêu làm việc khác không dùng khóa của tester. Thêm tester thì lấy khóa còn trống; hết khóa trống thì không sinh thêm, không dồn hai tester vào một khóa. Khóa cho tester01: giữ khóa TS-02 đang dùng (JX-K4) để khỏi đổi giữa chừng (chủ xác nhận "Đúng vậy" sau khi Chat trình bày cách hiểu, L13).

## Q-70 (chủ 19/11 11:23) — NỐI MÁY GIẢ LẬP CHO TIỂU YÊU TESTER + KHO TÀI LIỆU + CHIA VIỆC THEO MỤC
Chủ chốt: (1) làm cầu nối để tiểu yêu tester điều khiển được máy giả lập (hiện tiểu yêu bị chặn adb, 0/7); (2) phải có bộ tài liệu để tiểu yêu hiểu ngay, tiểu yêu chết thì con khác vào biết ngay; (3) chia việc theo từng MỤC cho từng tiểu yêu test, kết quả nhập vào kho knowledge chung, chia nhánh theo mục. Giữ: Q-59 (tester đầu ổn rồi mới sinh thêm), Q-60 (kho chia nhánh), Q-69 (một tester một khóa).

## Q-71 (chủ 19/11 11:27) — DUYỆT Q-70; XINGCHI HẠ KHÓA 1x → 0.5x: KHÔNG CHỜ, ĐỔI KHÓA
Chủ duyệt Q-70 ("cứ theo dõi"). Tin mới: nhà xingchi vừa hạ các api key từ mốc 1x xuống 0.5x; có thể vì thế tiểu yêu chưa lên lại. Lệnh chủ: nếu tiểu yêu chưa lên thì TẮT con đó và dùng KHÓA KHÁC, xem lỗi thế nào; KHÔNG CHỜ ĐỢI. Vẫn giữ Q-69 (một tester một khóa riêng; đổi khóa thì cập nhật bảng khóa↔tester).

## Q-72 (chủ 19/11 13:19) — THỬ COMMAND CODE (commandcode.ai) LÀM THỢ SỬA VIỆC NHỎ
Chủ chốt "Thử" sau khi Chat trình bày cách hiểu: Command Code là thợ sửa việc nhỏ; Sonnet chỉ đúng tệp/dòng/sửa gì, Command Code sửa trong worktree riêng, Sonnet xem diff rồi gộp. Thử 3 việc nhỏ bằng 10 USD tín dụng miễn phí, đo tốc độ và đúng/sai, so với một tiểu yêu Codex làm cùng việc. Chủ tự đăng nhập/nhập khóa (Chat/Sonnet không nhập hộ, khóa không vào kho). Giới hạn: không đụng mã game riêng tư, tệp hiệu ứng vũ khí, tệp có hook chặn; mỗi việc một worktree + một nhánh.

## Q-73 (chủ 19/11 13:29) — DUYỆT CÀI NODE.JS (cho thử Command Code, Q-72)
Chủ duyệt cài Node.js (bản LTS chính thức) trên máy chạy Tổng quản để thử Command Code. Đăng nhập Command Code vẫn do chủ tự làm. Ý "cho Command Code làm tester" chủ ĐANG BÀN, chưa chốt, chưa giao Sonnet.

## Q-74 (chủ 19/11 13:31) — CHỐT: THỬ COMMAND CODE LÀM TESTER (đọc mã nút trước, rồi chơi qua cầu)
Chủ chốt sau khi Chat trình bày cách hiểu: sau khi Node + đăng nhập xong (Q-72/Q-73), thử Command Code làm tester trên đúng mục đăng nhập → tạo nhân vật (mục tester01), đọc tệp giao diện/nút trước rồi chơi qua cầu adb; so với Sonnet tự chơi. Điều kiện: (1) kiểm nó nhìn được ảnh chụp màn hình không; (2) theo dõi tín dụng; (3) chỉ cho đọc tệp bố cục giao diện/tên nút, không toàn bộ mã game riêng tư; (4) Tổng quản chấm: không có lệnh cầu hoặc không có ảnh = KHÔNG ĐẠT.

## Q-75 (chủ 19/11 14:34) — CHỐT: THÊM SONNET B CHẠY SONG SONG PHIÊN KHÁC
Chủ thấy Sonnet (A) quá tải, chốt thêm một Sonnet thứ hai (B), ngang quyền, chạy ở phiên Claude Code riêng, cùng kho jx1-ops. Chia việc theo chủ đề, mỗi bên một hộp thư và một thư mục làm việc riêng (git worktree). Phạm vi và ranh giới: `STATE/SONNET-B.md`. A giữ: sửa lỗi game/APK/VK-04, Server D, ca thử C02/C04/C05, bảng tiến độ, hàng đợi W/SO/HG/KC/V/M, tổng hợp. B nhận: chương trình tiểu yêu tester (kể cả Command Code Q-72/Q-74, cầu LD, bộ canh cửa sổ LD) và hệ thống Bot. Luật tối thượng (Q-56), vùng đỏ, L1–L14 áp dụng cho cả hai. Chủ chỉ cần mở phiên mới theo hướng dẫn Chat đưa.

## Q-76 (chủ 19/11 14:49) — CHỦ ĐÃ ĐĂNG KÝ GÓI COMMAND CODE GO (1 đô/tháng) VÀ TẠO KHÓA
Chủ tự đăng ký gói Go (≈1 đô/tháng + phí xử lý, kèm ≈10 đô tín dụng) và tạo được nhiều khóa API; đã tự nhập thử MỘT khóa vào máy. Khóa không nằm trong chat/kho. Chi tiêu thêm (gói cao hơn, nạp tín dụng) vẫn là vùng đỏ, phải hỏi chủ. Gợi ý Chat (chưa chủ chốt): dùng một khóa trước; tín dụng có thể dùng chung cả tài khoản nên nhiều khóa chưa chắc nhân thêm tiền; mô hình rẻ cho việc sửa nhỏ, mô hình đọc được ảnh cho tester; ghi tín dụng trước/sau mỗi lượt.

## Q-77 (chủ 19/11 15:16) — CHỦ CHO PHÉP COMMAND CODE CHẠY `--yolo` TRONG WORKTREE RIÊNG; SONNET B CHẠY CHẾ ĐỘ TỰ ĐỘNG NHƯ A
Chủ chấp nhận cho `command-code --yolo` chạy (tự chạy lệnh không hỏi từng lần) với điều kiện Chat nêu: chỉ trong worktree riêng của việc đó (đầu tiên `D:\JX-wt\CC-01`), không để khóa/mật khẩu/ khóa API trong thư mục đó, Sonnet B xem kết quả sau mỗi lượt, không mua/nạp thêm. Chủ cũng đã chuyển phiên Sonnet B sang chế độ tự động giống A (bớt hỏi quyền). Bộ phân loại an toàn của Claude Code vẫn có thể chặn; nếu bị chặn thì ghi BAO-CAO-CHU, không lách.

## Q-78 (chủ 19/11 15:59) — CHỦ DUYỆT: B XEM LOG/DỮ LIỆU MÁY THỬ TEST-36 (CHỈ ĐỌC); DEEPSEEK ĐỂ SAU
Chủ: "Xem log máy thì cho luôn" (B xin đọc log Bishop/Goddess và tra tên trùng trong dữ liệu `JX-Test-36` cho lỗi Bot + lỗi tên nhân vật). Phạm vi: máy thử Test-36, chỉ đọc (Q-19 đã cho PM toàn quyền trên Test-36). KHÔNG gồm Main VM `JX-Server-D` (vẫn theo Q-18/Q-55: chỉ khi chủ test điện thoại). Không in mật khẩu/khóa ra kho. Việc thử DeepSeek cho Command Code: chủ bảo để sau (Chat không làm tới khi chủ nhắc lại).

## Q-79 (chủ 19/11 16:25) — SONNET B NGANG QUYỀN SONNET A, KHÔNG ĐI VÒNG QUA CHAT
Chủ chốt: B phải có đầy đủ quyền ngang A; B không được phải đợi báo Chat rồi Chat báo A. Thực hiện: (1) A và B có HỘP THƯ TRỰC TIẾP `HOP-THU/A-B.md` để nhờ nhau, không qua Chat; (2) B được sửa mọi tệp/mã giống A (phân vai chỉ là ưu tiên để khỏi dẫm chân, KHÔNG phải cấm): làm trong worktree riêng, commit nhỏ, rebase, ghi một dòng vào A-B.md khi đụng vùng của bên kia; (3) B dùng chung đường vào VM Test-36 như A qua một công cụ trung gian giữ thông tin đăng nhập trên máy chủ (B không nhìn thấy mật khẩu, không dò mật khẩu); (4) vùng đỏ giữ nguyên cho cả hai (Server D, tiền, khóa, xóa dữ liệu, giao APK, đổi thông tin đăng nhập); (5) việc gấp thì B làm ngay rồi báo Chat sau.

## Q-80 (chủ 19/11 18:09) — ƯU TIÊN LÊN ĐẦU: TỐI ƯU ĐƯỜNG TRUYỀN THÔNG TIN, TỐI NAY CHỦ TEST ĐỘ MƯỢT
Chủ: "tối ưu các đường truyền tải thông tin giữa các file, để tối nay test độ mượt, ưu tiên việc này lên đầu" (chốt sau khi Chat nói cách hiểu). Phạm vi: Test-36 + LD, không đụng Server D, bản thử chỉ LD, APK giao chủ theo #228. A sửa/tối ưu (#252), B đo/kịch bản (#B-015). Việc cũ làm sau.
- Bổ sung Q-80 (chủ 18:11): mục tiêu là CẢM GIÁC MƯỢT, không giật lag: tối ưu nhất có thể cả đường truyền dữ liệu (nạp tệp/map/spr, bộ nhớ đệm) và đường truyền máy chủ↔máy khách (tick, gói, trễ, FPS). Thư #253/#B-016.
- Bổ sung Q-80 (chủ 18:14): test trên Test-36, HẠN CỨNG 19:30 tối 19/11. Thư #254/#B-017.

## Q-81 (chủ 19/11 18:24) — CHO PHÉP GIAO APK THỬ ĐỘ MƯỢT CHO ĐIỆN THOẠI CHỦ TỐI NAY
Chủ đồng ý để A đưa APK thử (nội suy client, Q-80) đến điện thoại chủ để test trên Test-36 tối nay. Chỉ APK thử này; không APK khác; APK không vào git (repo công khai); giao theo đường đã dùng cho P46/P47 hoặc thư mục trên máy chủ + hướng dẫn bằng lời đơn giản. Không đụng Server D.

## Q-82 (19/11 21:24) Tối ưu độ phản hồi khi chạy nhanh/đánh quái (chủ)
Chủ đã vào game trên điện thoại (Test-36, APK vc22): hoạt ảnh/hoạt cảnh đạt, truyền gói tài nguyên ổn; còn LAG khi chạy nhanh và đánh quái, phản hồi chưa tốt. Giao: A client (dự đoán di chuyển, phản hồi đánh tức thì, gộp gói, APK thử vc23 có công tắc, đo ms); B mạng/forwarder/máy chủ (Tailscale direct hay DERP, RTT, NODELAY, SvrFPS lúc chạy/đánh). Phạm vi: Test-36 + APK thử, không Server D, không sửa mã server chính.
- Q-83 (19/11 21:36) Chủ: gom việc, ghi đầy đủ, hướng dẫn bàn giao sang tài khoản cũ của chủ → BAN-GIAO-CHAT-19-11-2140.md

## Q-84 (chủ 19/11 21:59) DUYỆT GỘP vk04 vào vc23, test một thể, rồi chuyển tài khoản
Chủ: "Gộp luôn, test luôn 1 thể; sau khi gộp xong ta sẽ chuyển tài khoản và báo lỗi ở tài khoản mới. Bảo A B làm gọn đi, không để trống thông tin. Trước khi chuyển ta sẽ báo Chat." → A gộp vk04 (chỉ vẽ thêm tia khi section phụ ≥20 điểm và ≥40%, công tắc tắt được) vào vc23, dựng MỘT lần (vc23 = giảm lag + vk04), giao APK theo Q-81 (Artifact + cài đè); B/A làm gọn sổ bàn giao, không bỏ trống thông tin; việc nghẽn gs001 (#275) ghi đủ trong bàn giao để tiếp ở tài khoản mới. Q-52 vẫn: chỉ gộp bản vk04 đã kiểm trên LD.

## Q-85 (chủ 20/11 00:00) A tự chủ dọn đường + kiểm vào game trước khi chủ test
Chủ: tối 19/11 A không tự tắt được PID, chủ phải làm rất nhiều việc bằng tay khi không ở nhà. Giao A quyền chủ động (L17); trước test A phải kiểm server nào, tài khoản nào, rồi dùng LDPlayer tự vào tới màn hình game chính, báo chủ OK. Không để chủ vào mới thấy đủ lỗi, treo ở chọn server mãi.

## Q-86 (chủ 20/11 00:48) CHỐT cường hóa + phi phong + tài phú; A, B làm ngay
Chủ chốt: cường hóa cho TẤT CẢ vũ khí/trang bị trên người, tối đa +15, 5% cộng thẳng; +14 thêm "+1 tất cả điểm kỹ năng vốn có", +15 thêm "+2"; điểm tài phú = X × tổng cấp cường hóa đang mặc, ngưỡng phi phong chia đều (+6 → cấp thấp nhất, +15 → cấp cao nhất); bỏ vũ khí +15 phát thử; đơn vị tiền bạc/vạn/ức, sửa server nếu cần; A có tài khoản test riêng tự tạo (L18). Thiết kế: DESIGN/THIET-KE-CUONG-HOA-PHI-PHONG.md. Chủ: làm bằng mọi giá, không chờ.

## Q-87 (chủ 20/11 00:59) Chat được giảm giá cường hóa nếu tiền không cho phép; không máy móc
Chủ: cần kết quả cuối là chức năng cường hóa xây thành công; tiền tệ không cho phép thì Chat quyết giảm giá cho hợp game, không dừng tiến độ. Phương án sẵn: DESIGN/THIET-KE-CUONG-HOA-PHI-PHONG.md mục 4 (64 bit nếu gọn, không thì kẹp 20 ức/cấp, nguyên liệu vẫn gấp đôi).

## Q-88 (20/11 07:00, đại vương chốt) — Hiển thị điểm tài phú
Điểm tài phú nhân vật = tổng điểm tài phú từng trang bị đang mặc (10 ô, mỗi món 100 × +N). Hiển thị: 1 dòng trong GIAO DIỆN NHÂN VẬT (asset gốc) + 1 dòng "Điểm tài phú" trong tooltip từng trang bị. Giao A (#286), B hỗ trợ đối chiếu (#B-037).

## Q-89 (20/11 07:12, đại vương chỉ thị) — Restart gs001 tốn 10–15 phút; thứ tự nghiệm thu
Mỗi lần khởi động + nạp gs001 mất 10–15 phút: A/B phải suy xét kỹ rồi gộp mọi thay đổi vào 1 lần restart. Sau khi xong hiển thị tài phú (khung nhân vật + tooltip) và tổng cộng gộp, A chạy quy trình SẴN SÀNG TEST rồi báo; Chat báo chủ vào test; sau đó chủ nghiệm thu, Chat chỉ thị hướng tiếp theo.

## Q-90 (20/11 07:35, đại vương chốt, ƯU TIÊN CAO NHẤT để chủ vào test) — Tài phú = thuộc tính nhân vật
1) Điểm tài phú là 1 dòng thuộc tính (magic attrib) như sức mạnh/thân pháp: trang bị có dòng "Điểm tài phú +M" (M = 100 × +N của món, tăng theo cường hóa); nhân vật mặc lên thì điểm tài phú nhân vật TĂNG đúng M, tháo xuống thì GIẢM đúng M, theo đúng cơ chế cộng/trừ thuộc tính chuẩn của engine; hiện ở khung thông tin nhân vật như các thuộc tính khác và ở tooltip món.
2) Điều kiện mặc phi phong = yêu cầu như điểm sức mạnh/thân pháp: tooltip "Yêu cầu tài phú: X" (đỏ nếu thiếu), chặn mặc theo cơ chế yêu cầu chuẩn. Mức X giữ nguyên bảng: cấp k = 6000 + 900(k−1), k=1..11 (6000…15000).
3) Game của ta TỰ THÁO phi phong khi điểm tài phú tụt dưới yêu cầu (khác game chuẩn); giữ QhCheckPifeng của B, dùng điểm tài phú thuộc tính nhân vật làm chuẩn.
4) Thay thế: tính tổng/gate tài phú tự viết cũ (QhWealth/QhPifengWealthOK, tính client) bằng cơ chế thuộc tính + yêu cầu chuẩn. Cường hóa +N/giá/tỉ lệ giữ nguyên. Không đụng vùng Đỏ. Nhớ Q-89: gộp 1 lần restart gs001.

## Q-91 (20/11 09:30, đại vương chốt ý Chat) — Giao diện cường hóa theo ảnh chuẩn
Làm cửa sổ "Cường hóa trang bị" giống ảnh trong DESIGN/UI-CUONG-HOA/ (dùng asset gốc, không chế lại), thay đường lệnh/dòng [QH]. Công thức Q-86 giữ nguyên. Đại vương giao Chat TỰ QUYẾT 3 điểm mở: (1) Bùa Bảo Hộ / Phù May Mắn: GIAI ĐOẠN 1 vẽ đủ 2 ô nhưng khóa (không tác dụng, tooltip "chưa mở"), không đổi luật thất bại; (2) số % trên icon trang bị trong túi = độ bền, hiển thị như game gốc (không làm gì thêm); (3) mở cửa sổ bằng nút "Cường hóa" trong giao diện túi/hành trang (có chữ "Cuong hoa" ở ảnh ba), nếu client chưa có thì A tạo nút nhỏ ở đó. THỨ TỰ: làm SAU Q-92.

## Q-92 (20/11 09:32, đại vương test phát hiện, ƯU TIÊN CAO NHẤT) — Cường hóa phải đổi thật dòng thuộc tính và chỉ số nhân vật
Đại vương test: bấm cường hóa áo báo lên cấp nhưng xem áo ở giao diện thông tin không đổi gì; áo test chưa có dòng thuộc tính nên chưa biết chỉ số nhân vật có đổi thật không. Cần kiểm và sửa: (1) lấy 1 vũ khí/trang bị ĐỦ dòng thuộc tính (ảnh 3: Thế lực tối đa, Sát thương vật lý nội/ngoại công, Độ chính xác, Kháng độc, Tốc độ đánh...); (2) cường hóa +0→+N: các dòng đó phải tăng +5%×N (làm tròn như Q-86) trong tooltip; (3) mặc vào: chỉ số THẬT của nhân vật (panel nhân vật, HP/MP/sát thương thực) đổi đúng bằng dòng tooltip; tháo ra thì trả lại; cường hóa khi đang mặc cập nhật ngay; (4) kiểm lại vì sao áo test không đổi (áo chưa có dòng nào hay do đã mặc/bị cache tooltip/client không nạp lại EnChance), báo kết luận số liệu trước-sau.

## Q-93 (20/11 09:37, đại vương giao thêm vai) — Chat nghiệm thu HÌNH ẢNH
Ngoài điều phối, Chat nghiệm thu về mặt hình ảnh thay đại vương: trước khi báo "SẴN SÀNG TEST/vào nghiệm thu", Chat tự xem ảnh chụp LDPlayer của A (đường dẫn trong TU-SONNET, thư mục docs-analysis/out/ld/) và đối chiếu ảnh chuẩn đại vương gửi (DESIGN/UI-CUONG-HOA/): bố cục, vị trí, font, màu, chữ tiếng Việt có dấu, không vỡ/lệch/thiếu. Lệch thì trả A sửa, không báo chủ. Quy cách: A chụp từng màn mới/đã sửa (cửa sổ cường hóa, tooltip, khung nhân vật), đặt tên có mô tả, ghi đường dẫn vào TU-SONNET; ảnh phải thấy rõ, không chụp lúc đang tải. Chat ghi kết quả "NGHIỆM THU HÌNH ẢNH: đạt/không đạt + điểm lệch" trong báo cáo cho chủ.

## Q-94 (20/11 10:42, đại vương CHỈ THỊ NGHIÊM) — Cường hóa phải bám sát logic gốc của game; "hoàn thành" chỉ khi đã thấy số thật trong game
1) Nguyên tắc: mọi thứ liên quan trang bị/cường hóa phải đi ĐÚNG đường chuẩn của game gốc: trang bị có dòng thuộc tính → khi MẶC, các dòng đó được áp lên nhân vật qua cơ chế gốc (ApplyMagicAttribToNPC/ cơ chế mặc đồ), nên dame, thủ, sinh lực, kháng, tốc độ... THẬT SỰ xuất hiện trên nhân vật (khung thông tin nhân vật đổi, đánh quái thấy dame đổi); THÁO thì mất đúng bấy nhiêu. Cường hóa là đổi giá trị các dòng của món; món đang mặc phải áp lại ngay. Không làm kiểu "báo lên cấp mà nhân vật không đổi".
2) Mọi việc cường hóa/tài phú/phi phong: A và B ĐỌC LẠI logic gốc (mặc/tháo/đổi thuộc tính trong KItemList/KPlayer/KNpc) trước khi viết, dùng lại hàm gốc, không tự chế đường song song; ghi trong thư trả lời "đã đối chiếu hàm gốc X".
3) Định nghĩa "XONG": chỉ ghi hoàn thành (kể cả các mục tiến độ) khi đã KIỂM TRONG GAME có số liệu trước/sau (ảnh LD của khung nhân vật + tooltip). Mục chưa kiểm bằng số liệu thật phải ghi "chưa kiểm", KHÔNG đánh hoàn thành. Chat sẽ rà TIEN-DO và hạ trạng thái các mục chỉ mới đọc mã/build sạch.
4) Tiêu chí nghiệm thu Q-92: cầm vũ khí/áo nhiều dòng; ghi chỉ số nhân vật (khung thông tin) → mặc: tăng đúng bằng các dòng tooltip → cường hóa +N khi đang mặc: chỉ số đổi ngay đúng +5%×N → tháo: về cũ. Ít nhất 3 chỉ số (sinh lực, sát thương vật lý, độ chính xác/kháng) kèm ảnh.
