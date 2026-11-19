# LUẬT CỐT LÕI (chủ chốt 18/11/2026, sáng) — ĐỌC ĐẦU TIÊN, KHÔNG ĐƯỢC QUÊN

File này ngắn có chủ ý. Đọc nó: đầu mỗi phiên, sau mỗi lần bị nén, trước khi dừng lượt. Không ai được sửa nghĩa các luật dưới đây trừ chủ (qua thư Chat).

## L1. Kênh làm việc
- Chủ CHỈ giao lệnh cho Chat. Chat viết thư vào `HOP-THU/CHO-SONNET.md`. Sonnet làm theo thư. Hòm thư (nhánh `jx1-ops`) là nguồn sự thật duy nhất; điều không có trong kho coi như chưa có.
- Nếu chủ vẫn nhắn thẳng trong Claude Code: ghi ngay vào `STATE/QUYET-DINH.md` (hoặc mục "CHỦ NÓI TRỰC TIẾP" trong `TU-SONNET.md`) rồi mới làm.
- Thư hiệu lực xem `HOP-THU/THU-HIEN-HANH.md`. Thư không sửa; thư mới ghi "thay thế/bổ sung #N".

## L2. Không treo
- Không bao giờ kết thúc lượt bằng câu hỏi, không dùng hộp chọn (Q-21). Việc làm lại được: tự quyết sau 10 phút, ghi `[TỰ QUYẾT]`. Chỉ chờ chủ với: Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, phát APK mới cho chủ test. Đang chờ thì vẫn làm việc khác.
- Thẻ `[DUNG-CAN-CHU]` hiệu lực tối đa 60 phút; việc xong thì xóa ngay.
- Làm theo ĐỢT (Q-48): mỗi đợt ghi MỘT báo cáo "XONG ĐỢT #N" vào TU-SONNET.md và push. **SAU ĐỢT KHÔNG DỪNG PHIÊN** (chủ chốt Q-52/Q-54, 18/11 đêm, thay luật "push, dừng" cũ): lấy việc kế trong `STATE/HANG-DOI-VIEC.md`; hết việc làm được thì chạy `python JX1_OPS\TOOLS\cho_thu.py` (chờ có nhịp tim) rồi làm tiếp khi nó thoát. Xem mục L10. Chỉ dừng khi hết hạn mức, 3 đợt không tiến triển hoặc chủ nói dừng.
- KẸT CẦN QUYẾT: không hỏi chủ, không đứng chờ. Ghi mục `[HỎI-CHAT]` trong `HOP-THU/TU-SONNET.md` (vấn đề, các phương án, phương án khuyến nghị), push, rồi làm việc khác. Chat trả lời trong `CHO-SONNET.md` (thường ≤10 phút khi có việc mở, tối đa 30 phút) và ghi "Chat quyết thay chủ" vào QUYET-DINH. Quá 30 phút chưa có trả lời: làm theo phương án khuyến nghị nếu làm lại được. Chỉ vùng Đỏ mới lên chủ (qua Chat).
- KHÔNG gõ cửa, không người gác (Q-48). [HỎI-CHAT] ghi trong báo cáo đợt, không chặn đợt: nêu giả định, làm tiếp phần độc lập.
- KÉO HÒM THƯ SAU MỖI MỤC (không chờ xong cả thư): `git pull` jx1-ops; có thư mới thì đọc; thư mới quan trọng hơn thì làm trước. Thư tiêu đề có `[KHẨN]`: dừng mục đang làm ở điểm an toàn gần nhất và làm ngay; người gác thấy `[KHẨN]` thì đánh thức Sonnet.
- Không có người gác (JX-Guard đã tắt; khôi phục: `schtasks /Change /TN JX-Guard /ENABLE`). Tổng quản chạy lịch Windows, chỉ ghi tệp, không gọi claude; tiểu yêu chết thì Tổng quản tự chạy lại.

## L3. Chống quên khi bị nén
- TRƯỚC khi nén: ghi "ĐANG LÀM DỞ" (việc, bước, lệnh chạy lại) vào `STATE/TRANG-THAI.md`, push.
- SAU khi nén, đọc theo thứ tự: file này → `STATE/TIEN-DO.md` → `HOP-THU/THU-HIEN-HANH.md` + thư mới trong `CHO-SONNET.md` → `STATE/QUYET-DINH.md` → lịch sử chat Claude Code (`C:\Users\PC\.claude\projects\...\*.jsonl`) từ lần push cuối lùi 15 phút, tối thiểu 60 phút, tối đa 3 giờ; chỉ đọc tin của chủ và trả lời cuối của Sonnet, bỏ log/kết quả lệnh. Điều chủ nói mà chưa có trong kho thì ghi vào kho ngay.

## L4. Tiến độ
- `STATE/TIEN-DO.md` sinh TỰ ĐỘNG bằng script từ front-matter `TASKS/*.md` (không viết tay). Đầu file 3 dòng: ĐANG LÀM / KẾ TIẾP / BỊ CHẶN (vì sao). Dưới là một sơ đồ Mermaid ≤30 ô theo 3 chặng (#091), màu theo trạng thái, mũi tên = chặn; việc xong lâu gom thành một ô.

## L5. Chuẩn hóa = hiểu game
- "Chuẩn hóa" của chủ là MỘT việc: chuẩn hóa báo cáo của tiểu yêu để hiểu game, gồm (a) khuôn `DESIGN/CHUAN-BAO-CAO.md`, (b) GIẢI MÃ tên ra chữ đúng (Hán: GBK; Việt cũ: TCVN3) và ghi cả tên gốc, (c) SẮP dữ liệu theo cấu trúc game (ví dụ kỹ năng phái: chia nhánh, xếp theo cấp học; bộ trang bị: liệt kê món). Thư #099 nói Sonnet "hiểu lầm" là SAI, đã thay bằng #107.
- Mỗi đợt chuẩn hóa xong, Chat hỏi thử bằng câu của người chơi (`DESIGN/KIEM-TRA-KIEN-THUC.md`). Đạt = trả lời được từ kho, dẫn đúng file mang tên đó.

## L8. Khóa xingchi và tiểu yêu (Q-41, Q-44; chủ chốt lại 18/11 09:29)
- Trần: 20 khóa × 3 tiểu yêu = tối đa 60 tiểu yêu, miễn phân công hợp lý. Dùng nhiều khóa KHÔNG gây quá tải; 429/lỗi Responses là do xingchi quá tải phía họ.
- Chỉ tạo khóa mới khi: còn việc chờ giao VÀ mọi khóa hiện có đã đủ 3 tiểu yêu. Không tạo sẵn, không tạo hàng loạt.
- Giãn cách tạo khóa: tối thiểu 1 phút giữa hai khóa. Tạo xong ping /v1/models rồi mới giao.
- Cách tạo ghi ở `DESIGN/QUY-TRINH-TAO-KHOA.md`. Giá trị khóa chỉ nằm trong `C:\Users\PC\.jx1keys\`, không ghi vào kho/log, không in ra màn hình. Không cần hỏi chủ trong trần 20.
- Sống/chết tiểu yêu xét bằng tiến trình + log/nhịp (`D:\\JX-wt\\<ID>.nhip`), KHÔNG bằng commit. Im 20–60 phút mà tiến trình còn: chỉ báo, không giết. Im > 60 phút: giết, chạy lại. Tiểu yêu không commit được thì người gác/chay_codex commit hộ.
- Rải đều do CODE làm (chay_codex.ps1/guard/Tổng quản tự chọn khóa ít việc nhất, ≤3/khóa), không dựa vào trí nhớ. Không chạy tiểu yêu bằng khóa mặc định.

## L9. Tổng quản là người duy nhất quản tiểu yêu (chủ chốt 18/11 09:47)
- Sonnet KHÔNG giao tay tiểu yêu nữa (không gọi chay_codex.ps1 trực tiếp). Sonnet chỉ viết TASKS/<ID>.md (status ready) để Tổng quản giao.
- Tổng quản làm hết: giao việc, rải khóa (≤3/khóa, hết chỗ báo CẦN KHÓA MỚI), xét sống/im/treo/chết, chạy lại khi chết/429 (chờ tăng dần), commit hộ khi xong, cập nhật status.
- Tổng quản ghi sự kiện vào `STATE/TONG-QUAN-GHI.md`; Sonnet đọc khi bắt đầu đợt.
- Khi chủ (qua Chat) hỏi tình hình tiểu yêu: Sonnet lấy báo cáo của Tổng quản (`STATE/TIEN-DO.md` + bảng tiểu yêu do Tổng quản sinh) rồi báo lại, không tự đoán.

## L7. Kế thừa khi đổi tài khoản
- Gõ cửa đã bỏ (Q-48); không cần ghi GO-CUA.log.
- Chat mới: đọc `HOP-THU/KHOI-DONG-CHAT.md`. Sonnet mới: đăng nhập lại Claude Code rồi `/tiep-tuc`; file này tự hiện qua hook.

## L6. Ưu tiên (#091)
Hiểu game (chuẩn hóa) → đường truyền client-server + hiểu exe → tick/độ phản hồi/đồ họa. Chỉ làm bản A (qh9A).


## L10. VÒNG LIÊN TỤC — KHÔNG BAO GIỜ TỰ DỪNG (chủ chốt 18/11 22:16–23:40: Q-52, Q-53, Q-54; ưu tiên hơn mọi chỗ khác nói "dừng")
- Sonnet giữ phiên mở và làm việc liên tục cả đêm. Mỗi đợt xong: ghi XONG ĐỢT, dòng `SONNET-XONG #N` vào VONG.md, đẩy, rồi LÀM TIẾP ngay (không chờ ai gõ, không dừng lượt). "Hết việc" không tồn tại: lấy từ `STATE/HANG-DOI-VIEC.md`, cạn thì tự thêm việc "hiểu game".
- Việc chờ tiểu yêu hoặc chờ thư: chạy `python JX1_OPS\TOOLS\cho_thu.py` (≤55 phút, ghi nhịp tim `HOP-THU/NHIP-TIM.md` mỗi 5 phút). Thoát mã 10 = có thư mới (pull, đọc, làm); 11 = có việc chờ gộp; 12 = hết hạn → chạy lại. Cấm tự viết vòng chờ khác. Kết thúc lượt mà không đang chạy cho_thu.py hoặc làm việc = LỖI.
- Tín hiệu qua Chrome: "xong" chỉ khi có đợt đáng báo (xong một mục lớn); "CHAT" khi cần hỏi (đã ghi [HỎI-CHAT] vào TU-SONNET.md + `SONNET-HOI` vào VONG.md). Gõ xong KHÔNG dừng: làm việc kế/`cho_thu.py`.
- Cần chủ thật: ghi [CAN-CHU] vào BAO-CAO-CHU.md rồi làm việc khác. Không bao giờ kết lượt bằng câu hỏi trong khung chat Sonnet (Q-21).
- Hiệu ứng vũ khí: KHÔNG sửa mã tới khi `DESIGN/HIEU-HIEU-UNG-VU-KHI.md` được Chat duyệt (Q-52).
- Sau khi bị nén: đọc file này trước, rồi làm tiếp đúng vòng này, không đợi chủ gõ.
**KHI NÀO DỄ DỪNG VÀ CÁCH CHẶN** (Sonnet tự nêu, #199/#200):
- (i) Viết trả lời cuối ngay sau một thư dài mà quên chạy `cho_thu.py` → chặn: sau mỗi đợt làm việc kế trong hàng đợi; `cho_thu.py` CHỈ khi không còn việc làm-được-ngay; hook Stop chỉ chặn tối đa 150 lần.
- (ii) Bị nén ngữ cảnh giữa chừng và mất mạch → chặn: đọc lại LUAT-COT-LOI, TIEN-DO, thư mới nhất; hook SessionStart nạp luật.
- (iii) Coi việc chờ chủ (APK mới, bật D, vùng Đỏ) là "hết việc" → chặn: việc chờ chủ là việc phụ; lấy ngay việc kế khác.
- (iv) Cạn hạn mức → chặn: ghi trạng thái vào VONG.md/BAO-CAO-CHU.md trước khi cạn; `SONNET-SONG.md` cho Chat thấy.

## L11. THÓI QUEN CHỦ DẶN — BẤT BIẾN (MỘT chỗ duy nhất; Chat ghi vào đây NGAY khi chủ dặn thường trực; không rải ở thư/nhật ký)
- **LDPlayer: mở xong phải ẨN/thu nhỏ cửa sổ NGAY** (máy chủ có người khác dùng, không được để cửa sổ game/giả lập nổi lên). Áp dụng mọi lần khởi động/khởi động lại LDPlayer, kể cả bản sao `T36test`: mở bằng cách không hiện cửa sổ nếu được, nếu không thì thu nhỏ/ẩn ngay sau khi lên, và kiểm lại bằng ảnh chụp. Chủ dặn từ #078 (17:09 ngày 17/11), nhắc lại 18/11 23:51.
- **Không cửa sổ nháy:** mọi tiến trình nền (Tổng quản, cho_thu.py, forwarder) chạy không console (pythonw/CREATE_NO_WINDOW).
- **Không bridged:** VM không bao giờ ở chế độ bridged (Q-17). Main VM `JX-Server-D`: chỉ theo Q-18.
- **Khóa/mật khẩu:** không bao giờ vào kho, nhật ký, báo cáo, chat; chỉ ở `C:\Users\PC\.jx1keys\` hoặc `D:\JX-keys\`.
- **Hiểu rồi mới sửa** (hiệu ứng vũ khí): không sửa mã tới khi tài liệu W-01 được Chat duyệt + có bằng chứng tái hiện (Q-52).
- **Cách thêm luật mới:** chủ nói thường trực → Chat thêm MỘT dòng vào mục này (kèm ngày) và đẩy; các tài liệu khác chỉ dẫn link tới đây, không chép lại.
- **Server D và LDPlayer nối D chỉ chạy khi chủ ra test trên điện thoại** (chủ dặn 18/11 23:58, Q-55): không test thì TẮT để đỡ tốn RAM cho tiểu yêu. **Chủ ĐÃ CHO PHÉP THƯỜNG TRỰC (19/11 00:10): D có 0 người chơi thì cứ tắt D + LDPlayer-D, KHÔNG hỏi lại.** Chủ nói "bật D để test" thì bật lại (Q-18, `KHOI_DONG_CHUOI_SERVER_D.md`). Tắt kiểu sạch (dừng chuỗi server/đóng ứng dụng tử tế, tắt ACPI), không kill cứng. LDPlayer của `T36test` (việc Test-36) giữ theo nhu cầu và luôn ẩn.
- **Luôn có ít nhất 8 tiểu yêu đang làm việc, mỗi khóa tối đa 2 con** (K2..K6 = tối đa 10 chỗ; dùng ≥4 khóa, ưu tiên khóa ít lỗi; K5 giữ 2 con). Sonnet giữ hàng đợi ≥12 việc `ready` đọc-tóm không-Đỏ để Tổng quản luôn đủ 8. Việc thiếu thì tự thêm từ `HANG-DOI-VIEC.md` (mục "hiểu game").
- **RAM máy thật:** Sonnet kiểm RAM mỗi đợt (tổng/đã dùng/còn trống; top 8 tiến trình theo bộ nhớ: VBoxHeadless, LDPlayer, python/codex, Chrome...). Phần nào cao bất thường (vd 1 tiến trình >4 GB không giải thích được, hoặc RAM trống <15%) → ghi [CAN-CHU] NGAY và gõ "CHAT": Chat báo chủ xin tắt. Không tự giết tiến trình lạ của chủ.
- **Chốt kỹ thuật (Q-54, 19/11):** hook Stop `TOOLS/stop_guard.py` KHÔNG còn cho dừng vì "đã ghi XONG ĐỢT" hay "hết việc": nó chặn dừng và bảo chạy `cho_thu.py`. Chỉ cho dừng khi có `STATE/DUNG-VONG.flag` (chủ bảo dừng → Chat tạo tệp này), `/ket-thuc-ca`, Codex chạm trần, hoặc đã chặn 40 lần/phiên. Muốn chạy lại thì xóa tệp cờ.
- **Chờ thư (19/11 00:50):** `cho_thu.py` mặc định giờ là **9 phút** (lệnh Bash của Claude Code tối đa 10 phút; 55 phút sẽ bị cắt giữa chừng). Gọi bằng Bash với `timeout` 600000; thoát mã 12 thì chạy lại NGAY. Hook chặn dừng tối đa 150 lần/phiên (~22 giờ).
- **LUẬT TỐI THƯỢNG (chủ chốt 19/11 00:56): CHAT KHÔNG BAO GIỜ RA LỆNH CHO SONNET DỪNG. Sonnet làm việc LIÊN TỤC, không ngắt quãng.** Sonnet có toàn quyền chủ động (sửa công cụ, hook, script, Tổng quản, lịch, cấu hình, thêm việc, mở thêm tiểu yêu trong giới hạn RAM/khóa) để việc không thể dừng. Mọi thư Chat không được chứa lệnh "dừng/tạm dừng/chờ chủ/nghỉ"; muốn dừng thì CHỈ khi chủ nói rõ "dừng vòng" (khi đó Chat tạo `STATE/DUNG-VONG.flag`). Chỉ vùng Đỏ (Main VM, tiền vượt trần, khóa ngoài 20, xóa dữ liệu, APK phát chủ, đổi credential) vẫn cần chủ: việc đó chỉ được bỏ qua và làm việc khác, không dừng cả vòng.
- **Ngân sách và tiểu yêu (chủ chốt 19/11 01:08, Q-57):** xingchi đã mở GPT 1x rate, đã cộng thêm 1000 USD, tổng chủ có hơn 3000 USD, mạng xingchi đêm nay tốt. Chủ CHO PHÉP mở tiểu yêu KHÔNG GIỚI HẠN SỐ LƯỢNG khi cần (thay trần 10/`MAXKEY=2` và trần 20 khóa × 3 ở L8), miễn: tăng DẦN (mỗi bước quan sát 5–10 phút), RAM trống ≥20% (<15% thì hạ ngay), 429 không tăng; mỗi con có việc thật thuộc mẫu số. Trần ngày/tuần trong `stop_guard.py` đã nâng lên 1000/3000 USD; Sonnet nâng tương ứng ở `TRANG-THAI.md` (mục Ngân sách) và mọi script có trần ngân sách khác. Khóa mới: được tạo thêm theo `DESIGN/QUY-TRINH-TAO-KHOA.md` (không vào kho, tối đa 1 khóa/phút).

## L12. Pull trong worktree có file ghi liên tục [TỰ QUYẾT, #221]
Luôn `git pull --rebase --autostash`; `STATE/TONG-QUAN-GHI.md` đặt `merge=union` trong `JX1_OPS/.gitattributes`. Cấm commit file còn dấu `<<<<<<<`.
