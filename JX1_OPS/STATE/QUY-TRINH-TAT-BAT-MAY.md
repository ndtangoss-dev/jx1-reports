# QUY TRÌNH TẮT MÁY / BẬT MÁY ĐẦY ĐỦ (chủ chốt 21/11 10:25: "tắt máy" = DỪNG HẾT, kể cả Tổng quản và worker; bật lại phải có quy trình bật từ Tổng quản đến worker)
BẢN THIẾT KẾ của Chat (21/11 10:30). Phần ghi (CẦN B XÁC MINH) = Chat đọc từ kho, chưa chạy thật: B/A kiểm bằng `schtasks /Query`, sửa đúng tên thật, rồi cập nhật `TOOLS/commands/ket-thuc-ca.md` và `tiep-tuc.md`.
Cơ sở: Tổng quản = Task Scheduler `JX-TongQuan` chạy `TOOLS/tong_quan.py` mỗi 3 phút (STATE/DUONG-DAN.md:19); mỗi tiểu yêu Codex = tác vụ `JX-codex-<ID>` do `chay_codex.ps1` (DUONG-DAN.md:20); log/dấu xong ở `D:\JX-wt\<ID>.codex.log/.done/.nhip`. Tổng quản TỰ CHẠY LẠI việc chết (chờ 2/5/15 phút, tối đa 3 lần) và giao việc `status=ready` ⇒ nếu dừng worker mà để Tổng quản chạy thì nó bật lại worker.

## I. TẮT (chủ gõ `/ket-thuc-ca`; ĐÚNG THỨ TỰ)
1. Không giao việc mới (không đặt task `ready` mới).
2. Chủ thoát nhân vật; A dừng gs001 rồi VM Test-36 đúng thứ tự (Online=0 trước), không cắt ngang. Main VM `JX-Server-D`: không đụng.
3. **TẮT TỔNG QUẢN TRƯỚC** (để không bật lại worker): `schtasks /End /TN JX-TongQuan` rồi `schtasks /Change /TN JX-TongQuan /DISABLE` (CẦN B XÁC MINH quyền/tên). Ghi vào `STATE/TRANG-THAI.md`: "Tổng quản đã DISABLE lúc hh:mm".
4. **Danh sách worker đang chạy:** `schtasks /Query` lọc `JX-codex-*` + đối chiếu `STATE/TIEU-YEU.md`, `STATE/KHOA.md`. Ghi vào `STATE/DANG-CHAY-TRUOC-TAT.md`: ID, khóa, vùng file, trạng thái, commit gần nhất.
5. **Dừng từng worker:** chờ tới điểm dừng an toàn (có `.done` hoặc `.nhip` dừng) tối đa 10 phút; quá hạn: `schtasks /End /TN JX-codex-<ID>`, commit phần dở thành `WIP` trên nhánh `task/<ID>`, ghi "Bước tiếp theo" vào file task, đặt status task về `ready` (để lần bật sau Tổng quản giao lại). Gỡ khóa trong `KHOA.md` cho worker đã dừng.
6. **Dừng các tiến trình nền khác theo chủ (CẦN B XÁC MINH danh sách thật):** bộ canh LD `JX-LDCanh`, cầu LD, người gác (`guard`/`stop_guard`), Command Code, Bot, Monitor `.done`. Mỗi cái: ghi tên + trạng thái trước khi dừng vào `DANG-CHAY-TRUOC-TAT.md` để bật lại đúng.
7. A và B: cập nhật `STATE/BAN-GIAO.md` / `BAN-GIAO-B.md`, `TRANG-THAI.md`, báo cáo ngày; commit, push, KIỂM GitHub khớp.
8. Chỉ khi cả bốn đúng mới nói "Đã lưu. Có thể tắt máy.": (a) VM/gs001 đã tắt, (b) `JX-TongQuan` DISABLED, (c) không còn `JX-codex-*` chạy, (d) GitHub có commit cuối. Thiếu một điều thì nói rõ thiếu gì và KHÔNG nói tắt máy được.

## II. BẬT (chủ gõ `/tiep-tuc` sau khi mở máy; ĐÚNG THỨ TỰ, Tổng quản đứng TRƯỚC worker)
1. Máy lên: KHÔNG tự bật gì; kiểm `JX-TongQuan` vẫn DISABLED (nếu tự chạy thì dừng, tránh giao việc khi chưa sẵn sàng).
2. Hạ tầng (A): VM Test-36 + chuỗi máy chủ `vm_chay.py chain-up` rồi `ports`; Main VM `JX-Server-D` chỉ theo Q-18 (không đụng ngoài quy trình). gs001 nạp 7–10 phút.
3. Phiên Claude: A (`C:\Jx1CocoV3`, `/tiep-tuc`), B (`D:\JX-wt\SONNET-B`, đoạn khởi động B), Chat mới (`KHOI-DONG-CHAT.md`). Đọc bàn giao, `git pull`, so thực tế với TRANG-THAI.
4. Đọc `STATE/DANG-CHAY-TRUOC-TAT.md` + `STATE/KHOA.md`: gỡ khóa của worker không còn chạy; kiểm nhánh `task/<ID>` có WIP; kiểm khóa/ngân sách Codex còn (`STATE/KHOA-XINGCHI.md`, cầu dao xingchi ĐÓNG/MỞ).
5. Bộ canh LD, cầu LD, người gác: bật lại đúng danh sách đã ghi (cần cho worker/LD).
6. **BẬT TỔNG QUẢN:** `python -I TOOLS/tong_quan.py --dry` (chạy thử, xem nó sẽ giao gì) → nếu hợp lý: `schtasks /Change /TN JX-TongQuan /ENABLE` rồi `schtasks /Run /TN JX-TongQuan`. Nó sẽ giao lại việc `ready` (WIP tiếp tục), rải khóa (≤3 tiểu yêu/khóa, trần 10 đồng thời).
7. Kiểm: `STATE/TONG-QUAN-GHI.md` có dòng mới (3 phút), `STATE/TIEU-YEU.md` liệt kê đúng worker, `.nhip` của từng worker cập nhật, nhịp tim A/B/Chat, số liệu `TRANG-THAI.md` không lùi; ghi dòng tiếp quản vào `BAN-GIAO.md`.
8. Báo chủ 2–3 dòng: đã bật những gì, worker nào chạy lại, còn gì cần chủ quyết.

## III. VIỆC CẦN LÀM NGAY (giao B làm chính, A kiểm)
B: (1) `schtasks /Query` thật → ghi bảng tác vụ thật (tên, trạng thái) vào mục "Danh sách thật" dưới đây; (2) thực hiện bước I.3–I.6 NGAY cho lần tắt này, ghi `DANG-CHAY-TRUOC-TAT.md`; (3) sửa `TOOLS/commands/ket-thuc-ca.md` + `tiep-tuc.md` (và QUY-TAC-VAN-HANH.md mục 7) theo quy trình này; (4) trả lời chủ: "Tổng quản đã dừng, worker đã dừng, danh sách nằm ở ..., cách bật lại ...". A: kiểm lại bước I.8 và cập nhật `HUONG-DAN-CHU-BAT-LAI-21-11.md` mục B.

## Danh sách thật (B điền)
(B kiểm bằng schtasks /Query 21/11): JX-TongQuan (nay DISABLED), ~190 tác vụ JX-codex-<ID> (đều Ready), JX-Guard (Disabled), JX-LDCanh (Ready), JX-Forwarder-T36 (Running, thuộc VM), JX-Forwarder-Tailscale, JX-CDN-8080, JX1-Task-Dispatcher (Running, của A/chủ), JX1-ADMIN-* (tay chủ). Tên đúng như bản thiết kế; `/Change /DISABLE` chạy được không cần nâng quyền. Chi tiết: STATE/DANG-CHAY-TRUOC-TAT.md.

- [A 21/11 #349] Sau khi bật LD: chạy `pythonw -I TOOLS/ld_canh_cua_so.py` (nền) để thu nhỏ cửa sổ LD; `--once` kiểm 1 lần (đã thử với LD T36-tester01: thu nhỏ 1 cửa sổ). Đưa vào bước /tiep-tuc.
