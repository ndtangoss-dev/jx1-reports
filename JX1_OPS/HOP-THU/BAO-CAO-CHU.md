# BÁO CÁO CHO CHỦ (Chat cập nhật mỗi vòng, 3–5 dòng lời thường; chủ đọc khi muốn)
- 18/11 19:35: bắt đầu vòng tự động (Q-49). Chờ Sonnet xong #165 rồi tới #166.
- 18/11 19:56: Vòng tự động qua Chrome ĐÃ THÔNG: Sonnet gõ "xong (thử vòng)" vào thẻ chat này lúc 19:43, Chat nhận và đẩy thư. Đợt #168: kiểm kê asset (K-02), mở khóa R-04b/R-05a, đánh giá A-07, soạn đề xuất thử client 3–5 ca. Chưa có việc nào cần chủ quyết ngay; đề xuất thử client sẽ trình chủ khi Sonnet viết xong.
- 18/11 20:15 — CẦN CHỦ QUYẾT (nhắn Chat bằng câu đầy đủ): (1) Có cho thử client ca C01 + C03 trước không (đăng nhập, chọn nhân vật, vào game bằng LDPlayer + APK, ghi 5 mốc và cổng thật; chạm thấp, không đổi dữ liệu)? Sau đó C02, C04, C05. Chi tiết: DESIGN/DE-XUAT-THU-CLIENT.md. (2) Có cho Sonnet chạy A-07 bước 3–6 (dựng Debug rồi chạy công cụ bắt lỗi trong VM thử) không? Bước 1 trên máy dev Chat đã cho làm. Chi tiết: DESIGN/DE-XUAT-A-07.md. Trong lúc chờ: Sonnet dựng thử A-07, gộp kiểm kê asset (K-02) và hai việc báo cáo còn lại.
- 18/11 20:10: Bảng tiến độ JX1 (artifact) đang LỖI THỜI (đăng 17/11 05:36, 38%). Đã giao Sonnet (#170) đồng bộ trạng thái thật, thêm các nhóm việc mới; Chat sẽ đăng lại bảng mỗi vòng. Việc kế theo kế hoạch cho Chat: viết thiết kế B-01 (bộ lọc hiển thị + chặn tương tác), vì A-05 đã xong.
- 18/11 20:25 — CẦN CHỦ QUYẾT: thay nhà cung cấp cho tiểu yêu (xingchi nhóm 0.25x hay chết/chậm). Chọn nhà cung cấp thử (vd OpenAI trực tiếp hoặc Meta Muse Spark API, cả hai có Responses API) và trần ngân sách/ngày. Sonnet đang chuẩn bị bộ thử (#171), chưa gửi dữ liệu ra ngoài.
- 18/11 20:20 — CẦN CHỦ QUYẾT: duyệt thử Gemini miễn phí (gói miễn phí có thể dùng dữ liệu để huấn luyện; chỉ thử với việc đọc không nhạy cảm). Sonnet đang chuẩn bị (#172), chưa gửi gì ra ngoài.
- 18/11 21:12 — VÒNG TẠM DỪNG (hết việc không-Đỏ). Bảng tiến độ 28/51. Chờ đại vương quyết (trả lời bằng câu đầy đủ): (1) duyệt thử Gemini miễn phí; (2) thử client C01+C03; (3) A-07 bước 3–6 trong VM; (4) cửa sổ Tổng quản đã hết nháy chưa; (5) 0-05 tạo kho riêng jx1-source.
- 18/11 21:20 — Chủ đã duyệt 1–5; vòng chạy lại. Sonnet sẽ hỏi [CAN-CHU] khi cần chủ làm tay (lấy khóa Gemini, đăng nhập client, quyền gh).
- 18/11 21:35 — CHỦ LÀM TAY: (a) tạo repo RỖNG PRIVATE jx1-source trên GitHub, báo tên; (b) bấm đúp nhap_khoa.bat dán khóa Gemini; (c) tạo tài khoản TEST-A trên JX-Test-36 + mật khẩu; (d) xác nhận 2 VBoxSVC + 6 VBoxHeadless đang chạy là bình thường.
- 18/11 21:45 — Sonnet tự làm TEST-A + VirtualBox + C01/C03. Chủ chỉ cần làm khi ngồi máy: tạo repo private jx1-source (hoặc đăng nhập gh) và dán khóa Gemini.
- 18/11 21:30 — Khóa Gemini đã nhập; Sonnet chạy so sánh. jx1-source giữ cục bộ (theo chủ). Không còn việc tay cho chủ.
- 18/11 22:12 — Gemini miễn phí không dùng được (20 lượt/ngày), đã bỏ. Đang giảm token tiểu yêu, thử client trên máy thử. Không cần chủ làm gì.
- 18/11 22:35 — Đã lập hàng đợi việc không bao giờ cạn (STATE/HANG-DOI-VIEC.md); dừng sửa hiệu ứng vũ khí cho tới khi hiểu (W-01); Sonnet giữ phiên mở cả đêm.
- 19/11 01:00 — Chủ đi ngủ. LỆNH: 07:00 sáng tiến độ ≥70% (đang 56%). Chat+Sonnet làm (#202), kiểm 15 phút/lần, mở thêm tiểu yêu theo RAM.

## TỔNG KẾT ĐÊM — 19/11 06:30 (Chat)
- SỐ THẬT 88/107 = 82% (bảng cũng 82%; đêm qua 56%). Vượt mục tiêu 70% của chủ. Số đếm nghiêm: việc cha chỉ tính xong khi đúng từng chữ tên việc; mẫu số đóng băng 107.
- Đã làm: vá lỗ hổng móc chặn dừng (stop_guard) và cho_thu 9 phút; tổng quản mở tới 4 khóa/20 tiểu yêu, RAM luôn trống ≥54%, lỗi 429 = 0; kiểm toán nghiêm làm E-01, HG-14, HG-16 từng bị mở lại rồi đóng đúng mức. Hiệu ứng vũ khí: chưa sửa mã (đúng luật).
- Kẹt: B-04, E-01, E-05, E-09, C-01, P-02, W-02 chỉ còn thiếu chạy thật trên máy thử Test-36: thiếu khóa client đúng bản APK và tài khoản/vai thử cho Bot, B-04 cần 3 lượt x 3 pha x 660 s.
- CẦN CHỦ QUYẾT sáng nay: (1) cho cấp khóa client + tài khoản thử cho Bot để chạy E-01; (2) duyệt thử client C02/C04/C05; (3) có muốn "bật D để test" bằng điện thoại không.
- Sonnet tự dừng ~20 phút/lần: gốc là phiên Claude Code kết thúc lượt khi trả lời bằng chữ. Đề xuất chữa tận gốc: Tổng quản (tác vụ Windows, không tốn Claude) tự đánh thức phiên bằng cách chạy lệnh nhập chữ vào cửa sổ khi SONNET-SONG báo IM >10 phút, thay cho Chat gõ qua Chrome.
- 19/11 07:20 — CHỦ GIAO: tiểu yêu TESTER (Q-59/#217): 1 con trước, ổn mới sinh tiếp; Chat báo tiến độ thường xuyên.

## (B) 19/11 15:40 — Command Code CC-01 lượt đầu: ĐẠT (phần cầu LD)
- Chạy `command-code --yolo -m flint-v1.0:free` đúng trong `D:\JX-wt\CC-01` (Q-77). Nó tự gửi 3 lệnh cầu (chụp ảnh, chạm, chạm) và có ảnh mới: tính là ĐẠT theo thư #B-002 (≥1 lệnh + ảnh mới).
- Nó đọc được ảnh: tả đúng màn "Lựa chọn hệ phái", ô tên đang là "Tsbaone", nút Xác định/Hủy bỏ. Tự viết `KET-QUA.md`.
- Chưa xong cả việc đăng nhập → tạo nhân vật; lỗi tên (gõ qua adb không được ô nhập nhận) vẫn là điểm kẹt chung. Chưa đo tốc độ/đúng so với tiểu yêu Codex; chưa ghi số dư `/usage` (cần phiên tương tác). Không mua/nạp gì.
- Việc khác: bảng giá Bot `gia-vat-pham.csv` đã có cột tên Unicode (80a44d9). Bot vào thất bại: chạy riêng lẻ vẫn lỗi → lỗi theo vai/tài khoản, cần log Bishop/Goddess trên VM (chờ duyệt).

## (B) 19/11 15:55 — #B-004 Kiểm tên nhân vật: dấu cách cuối / trùng tên
- **Dấu cách cuối: KHÔNG thấy.** Mã client `KuiNewPlayer.cpp:554-604` không cắt (trim) chuỗi; nếu có dấu cách cuối thì chính mã này đã báo "ký tự đặc biệt" (cấm dấu cách, số, ký hiệu). Thử tên khác hẳn `Cctesterone` (11 chữ cái), xóa ô bằng 58 lần phím xóa trước: không còn báo lỗi tên. Tổng cộng khoảng 4 lần thử.
- **Lỗi cũ `Tsbaone`: chưa chứng minh nguyên nhân.** Khả năng cao là chữ cũ còn trong ô (ví dụ `T36nv2` có số) bị nối vào chuỗi thật. Ảnh chụp hiển thị chữ có thể khác giá trị thật.
- **Tên trùng: không thể gây thông báo "ký tự đặc biệt".** Trùng tên do server từ chối, thông báo riêng (`KuiNewPlayer.cpp:1054-1067`, CREATE_FAIL). CHƯA KIỂM dữ liệu Test-36 (cần quyền đọc VM, chưa có duyệt); nên chưa biết tên `Tsbaone`/`T36nv1/2` có sẵn không.
- **Phát hiện mới:** với tên sạch, bấm Xác định (kể cả đã chọn hệ) KHÔNG có hộp thông báo nào, không thành công cũng không thất bại. Theo `KuiNewPlayer.cpp:616-660`, `CreateRole()` im lặng thoát khi chưa kết nối, chưa chọn vùng, trạng thái không phải "danh sách vai sẵn sàng" hoặc đủ số vai. Thành công/thất bại đều hiện hộp (dòng 1049, 1065). Vậy lệnh tạo vai chưa tới server.
- **Liên hệ Bot:** chưa có bằng chứng Bot trùng tên. Nhưng nếu Bot cũng gặp `CreateRole()` im lặng thì giải thích "vào thất bại theo tài khoản/vai" một phần; cần nhật ký Bishop/Goddess mới kết luận.
- **Bước tiếp:** (1) kiểm trạng thái kết nối/vùng của LD T36-tester01 (DNAT 56722/51189/8080 sau lần khởi động lại); (2) xin duyệt đọc-chỉ Test-36 để tra tên trùng; (3) chuyển A xem đoạn `CreateRole` có cần thông báo khi thoát im lặng không.

## (B) 19/11 16:20 — #B-005 Test-36: mạng LD thông; chưa đọc được log (thiếu đường vào máy khách)
- **Mạng LD tester01 (emulator-5558): THÔNG.** DNAT `100.95.186.86:{56722,51189,8080}` → `192.168.56.101` còn nguyên; từ trong LD nối TCP cả 3 cổng thành công (busybox nc, rc=0). Cổng 56722/51189 của Test-36 (`192.168.56.150`) mở; 8080 trực tiếp tới .150 hết giờ (đi qua forwarder .101 thì mở). Vậy `CreateRole()` im lặng KHÔNG do mất mạng.
- **Giả thuyết mạnh nhất (từ báo cáo C01, 18/11):** sau khi Goddess khởi động lại mà Bishop không khởi động lại, phiên Bishop↔Goddess cũ làm yêu cầu treo, không có trả lời nên client không hiện hộp nào (đúng triệu chứng tên sạch + Xác định im lặng, và Bot `TimeoutError` sau đăng nhập). Hướng sửa đã biết: khởi động lại Bishop (JX-ChainUp), rồi kiểm gs001 nối lại Bishop 56732. **CHƯA KIỂM** trên máy hiện tại.
- **Log Bishop/Goddess và tên trùng (Tsbaone, T36nv1/2, Cctesterone, tên Bot): CHƯA ĐỌC.** Từ máy thật không vào được ổ máy khách (`\192.168.56.150\C$` không mở, không có thông tin đăng nhập; tôi không tự đoán/nhập mật khẩu). `admin_chay.ps1` không có việc đọc log.
- **Cần chủ/A (một trong hai):** (a) chủ chạy lệnh trong máy khách Test-36 xem 50 dòng cuối log Bishop và Goddess rồi dán vào hộp thư; hoặc (b) chủ duyệt khởi động lại Bishop trên Test-36 (không đụng Server-D) để thử hết kẹt; tôi thử lại tạo vai `Cctesterone` ngay sau đó.

## (B) 19/11 16:45 — #B-007 Khởi động lại Bishop Test-36: CHƯA LÀM ĐƯỢC (thiếu đường xác thực)
- WinRM tới `192.168.56.150` trả lời (TrustedHosts đã có IP) nhưng cần tài khoản/mật khẩu; theo ghi chú cũ tài khoản mu1 mật khẩu trống bị từ chối "Access denied". B không có thông tin đăng nhập và bộ phân loại quyền đã CHẶN khi B thử liệt kê biến môi trường tìm mật khẩu; B không lách. `admin_chay.ps1` chỉ có kill-test-vm/firewall/trustedhosts/service (dịch vụ máy thật), không chạm chương trình trong VM. Kiểm LD: DNAT + cổng vẫn thông (không đổi so với 16:20).
- **Cần đại vương/Sonnet A, một lệnh duy nhất, chạy TRONG VM Test-36** (PowerShell, tài khoản mu1): `schtasks /run /tn JX-ChainUp` rồi đợi ~4 phút để gs001 nối lại 56732; (nếu có `JX-gs001` thì chạy thêm). Xong báo B, B thử lại tạo vai `Cctesterone` và botld007 ngay, ghi trước/sau.
- Hoặc Sonnet A/Tổng quản đã có đường vào VM (đã làm C01/jx_env_up) thì làm giúp việc này; B làm phần thử lại.

## (B) 19/11 17:00 — Bot GĐ1: 8 dòng giá mẫu xin đại vương duyệt
Bảng đủ 1034 món: `STATE/BOT/gia-vat-pham.csv` (tên đã đổi sang chữ có dấu). Cách tính hiện tại (GIẢ ĐỊNH, chưa ai duyệt): **giá Bot bán = 50% giá gốc trong bảng game**, không thấp hơn giá sàn. Xin đại vương xem các dòng mẫu rồi nói "được" hoặc nêu hệ số khác:
| Món | Loại | Giá gốc | Bot bán (50%) |
|---|---|---|---|
| Bố Mão | mũ | 360 | 180 |
| Tu Chân đạo y | áo | 1.160 | 580 |
| Thanh La quần | áo | 1.160 | 580 |
| Hoàng Bố Phát Đái | mũ | 3.080 | 1.540 |
| Lưu Tinh | ngựa | 5.000 | 2.500 |
| Nguyện Bạch Cà Sa | áo | 5.960 | 2.980 |
| Thôn Nhật Trãm | vũ khí cận chiến | 8.840 | 4.420 |
| Xích Long Câu | ngựa | 250.000 | 125.000 |
Lưu ý: 17 tên là ký tự hỏng (GBK) nên để nguyên; độ hiếm và thành thị bán chưa điền. Chưa chạy Bot bán thật.

## (B) 19/11 17:50 — #B-011: thử lại tạo vai sau khi chuỗi Test-36 lên
- Tên `Cctesterone` bấm Xác định: VẪN im lặng, vì LD đã ngồi ở màn tạo vai suốt lúc Bishop khởi động lại nên kết nối cũ chết. B tắt/mở lại ứng dụng (stop/start): về màn đầu "Bắt đầu trò chơi". Đăng nhập lại cần tài khoản và mật khẩu thử; B không có (không lấy trong kho), nên chưa tạo vai/chạy botld007 được.
- **Cần đại vương:** cho B tài khoản thử + mật khẩu qua biến môi trường `JX_BOT_PASSWORD` (hoặc một lệnh PowerShell ngắn đặt biến này trong cửa sổ B), hoặc tự đăng nhập một lần trong LD tester01 rồi báo B.
- Đã tạo 2 việc cho tiểu yêu (owner B): `TASKS/BOT-01.md` (giá bán Bot), `TASKS/BOT-02.md` (kiểm tên vai).

## (B) 19/11 18:10 — Bẩm đại vương, thuộc hạ đã đọc nhật ký máy chủ Test-36
- Bishop đang chạy tốt: các tài khoản Bot (botld007/013/018 và botld069–100) đều vào được và nhận danh sách vai. Vậy lỗi "hết giờ" của Bot nằm ở phía client/bot, không phải máy chủ hỏng.
- Máy chủ có vai T36nv1 (tạo 11:56) và một vai tên tsvkbonenamea (13 chữ, tạo 16:51) → tạo vai bằng tên dài 13 chữ THÀNH CÔNG. Các tên Tsbaone, Tsalphaone, T36nv2, Cctesterone không hề có trong kho vai.
- Mã nguồn Bishop (GamePlayer.cpp:1942-1946) cho tên 6..16 byte, chỉ cấm ký hiệu; "Cctesterone" (11) hợp lệ về phía máy chủ → độ dài KHÔNG phải nguyên nhân. Nghi nhất vẫn là kết nối client chết sau khi Bishop khởi động lại. Cần đăng nhập lại để thử (cần tài khoản thử + mật khẩu từ đại vương).

## (B) 19/11 18:35 — Bẩm đại vương, ĐÃ TẠO ĐƯỢC VAI MỚI TRÊN TEST-36
- Tạo vai thành công, nhật ký Goddess/Bishop ghi vai "TsmocnamebravTsm" (hệ Mộc) rồi vào game. Đăng nhập dùng tài khoản đã lưu sẵn trong máy giả lập, thuộc hạ KHÔNG gõ mật khẩu.
- Nguyên nhân các lần im lặng trước: thiếu bước chọn "Tân thủ thôn" (Ba Lăng huyện → Xác nhận) sau khi bấm "Tạo nhân vật mới"; bỏ bước này client thoát lặng (không phải máy chủ hỏng, không phải tên). Bishop khởi động lại cũng đã giúp.
- Luật tên đúng: 6–16 chữ cái ASCII (client 6–24, máy chủ 6–16).
- Còn: lệnh gõ chữ của cầu LD giao lộn thứ tự, thuộc hạ sẽ sửa; sau đó chạy lại Bot botld007.

## (B) 19/11 19:45 — nhắc đại vương 1 dòng
Bảng giá mẫu Bot GĐ1 (8 dòng trong `STATE/BOT/gia-vat-pham.csv`) vẫn chờ đại vương duyệt; BOT-01 (mô-đun tính giá) đã xong và test pass nên duyệt xong là dùng được ngay.

## (B) 19/11 18:20 — Kịch bản test mượt cho đại vương (5–10 phút, DỰ THẢO)
1. Vào game bằng vai đã có, đứng yên 1 phút: nói "ổn" hay "giật" (nhìn số ping/FPS góc dưới trái, đọc to cho thuộc hạ ghi).
2. Chạy qua lại 1 phút; rồi đổi sang map khác: nói có khựng khi nạp map không, khựng mấy giây.
3. Đánh quái 1 phút: nói số sát thương nổi lên có trễ so với đòn không.
4. Khi thuộc hạ thả 5, 10, 20 Bot gần chỗ đại vương: lặp bước 1–3, nói "ổn/giật nhẹ/giật nặng" ở mỗi mức.
Thuộc hạ ghi mốc: ping, FPS, CPU máy chủ ở từng mức. (Mốc rỗi đã có; mức có Bot chờ tài khoản test.)

## (B) 19/11 19:00 — Tài khoản test cho đại vương (Test-36)
- Đã tạo tài khoản test **`tkchuvuong`** trên Test-36 (không phải máy chủ chính). Mật khẩu do máy tự sinh, nằm ở tệp trên máy thật: `C:\Users\PC\AppData\Local\jx1-secrets\tkchuvuong.txt` (ngoài kho, thuộc hạ KHÔNG đọc, không ghi vào đâu). Đại vương mở tệp đó lấy mật khẩu.
- Chưa có vai: tạo vai phải đăng nhập bằng mật khẩu đó, thuộc hạ không được tự nhập mật khẩu. Hai cách: (1) đại vương tự đăng nhập trên điện thoại/LD và bấm "Tạo nhân vật mới" (chọn Ba Lăng huyện → hệ → tên chữ thường ≥12 ký tự), hoặc (2) đại vương cho phép rõ ràng "B dùng tệp mật khẩu đó để chạy `bot_tao_role.py`" thì thuộc hạ chạy (vẫn không in mật khẩu).
- Hoàn tác: `python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py xoa-tk-test tkchuvuong`.


## 19/11 19:02 — Vai thử vũ khí cho đại vương (Test-36)
1. Vào game bằng tài khoản **tkchuvuong**, chọn vai **chuvuongtestaa** (mật khẩu ở tệp `%LOCALAPPDATA%\jx1-secrets\tkchuvuong.txt` trên máy thật, thuộc hạ không ghi ra đây).
2. Lần vào đầu tiên, túi tự có 9 món vũ khí cấp 10, cường hóa +15 (6 loại cận chiến, 3 loại tầm xa); nhân vật lên cấp 90 kèm 300 điểm tiềm năng.
3. Muốn cầm vũ khí: cộng điểm vào Sức (≥100) và Nhanh nhẹn (≥155 cho tầm xa) trong bảng nhân vật, rồi mặc.

## 19:20 — Bản thử mượt hình (APK bản 22) cho đại vương
**Cài đặt (3 dòng):** 1) Bật Tailscale. 2) Mở trang Artifact "Link tải APK" (https://claude.ai/artifact/DTwgvhWEnGXBp9dHE1uYDu), bấm "Sao chép link", dán vào Chrome, tải và cài đè. 3) Mở game, chọn máy chủ, đăng nhập như cũ.
**File:** jx-goc-v22-noisuy.apk, 78,9 MB, SHA256 b235e8642137b0635161d22dd6d297b9bc4881332d6f2bf7b4d8aa1eceb76873.

| | Trước (bản cũ) | Sau (bản 22) |
|---|---|---|
| Quay 3 giây khi chạy: % cặp khung đứng yên (thấp = mượt) | 10,3% (tắt nội suy, 1 lần quay) | 20,5% và 15,4% (bật nội suy, 2 lần quay) |
| Độ dịch trung bình giữa 2 khung (điểm ảnh) | 1,54 | 1,39 và 1,62 |
| Hình LD hiện FPS | 30-34 | 30-34 |

Thuộc hạ nói thẳng: số đo trên LD (1-2 lần quay, 3 giây) chưa cho thấy bản 22 mượt hơn; chưa đủ để kết luận, có thể không khác gì. Bản 22 vào game được, cảnh đứng yên hiển thị đúng; chưa thử khi chạy thật. Công tắc tắt: ghi chữ 0 vào tệp jx_interp.txt trong thư mục dữ liệu game (nội suy tắt). Nếu thấy giật hay lệch hình hơn bản cũ, báo để thuộc hạ gỡ. Cần đại vương báo cảm nhận.
Ghi chú: vai thử vũ khí (tkchuvuong) nằm ở Test-36, không ở máy chủ chính.

Kiểm chuỗi Test-36: `python -I JX1_OPS/TOOLS/vm_chay.py ports` thấy 56722, 51189, gs001; máy thật nghe 100.95.186.86:56722/51189/8080/8091. Link APK: máy thật không tự tải thử được (tường lửa/địa chỉ nguồn), phục vụ APK đang chạy từ 17/11; xem `access.log` thư mục serve sau khi chủ tải.

## 19/11 19:58 — Mật khẩu tkchuvuong (thư #261)
- Tệp gốc: `C:\Users\PC\AppData\Local\jx1-secrets\tkchuvuong.txt` (có tồn tại; thư mục ẩn, bật "Hiện mục ẩn" mới thấy).
- Bản chép cho đại vương: `C:\Users\PC\OneDrive\Desktop\tkchuvuong-matkhau.txt` (Desktop của máy này nằm trong OneDrive, không phải `C:\Users\PC\Desktop`). Trong tệp: tài khoản, vai chuvuongtestaa, mật khẩu. Chỉ dùng cho Test-36; dùng xong nên xóa tệp.

## 19/11 20:10 — Điện thoại đứng im ở màn chọn server (thư #262)
- NGUYÊN NHÂN (THẤY): điện thoại (100.123.183.6) tải APK được và nối tới forwarder Tailscale, nhưng forwarder đang chuyển tiếp sang Server D `192.168.1.50`, mà D đang tắt → `LOI noi toi VM 192.168.1.50:56722: TimeoutError` lúc 19:59:59 và 20:01:44 (`docs-analysis/out/forwarder.log.truoc-t36`). Tài khoản `tkchuvuong` chỉ có trên Test-36 nên phải trỏ sang Test-36 `192.168.56.150` (từ máy thật ping được).
- APK đúng; Tailscale, cổng nghe 100.95.186.86:56722/51189/8080/8091 đều bình thường.
- CHƯA SỬA ĐƯỢC: forwarder cũ (PID 21276, bật từ 14/11) chạy quyền Admin, thuộc hạ không tắt được (Access denied; không vượt UAC).
- ĐẠI VƯƠNG LÀM 1 LẦN: trên Desktop có tệp `chuyen_forwarder_sang_t36.ps1` → chuột phải → Run with PowerShell **as Administrator**. Xong thử lại trên điện thoại (thoát game, mở lại). Hoàn tác: chạy `chuyen_forwarder_sang_t36.ps1 -Ve D`. Bản gốc ở `docs-analysis\scripts\chuyen_forwarder_sang_t36.ps1`.
