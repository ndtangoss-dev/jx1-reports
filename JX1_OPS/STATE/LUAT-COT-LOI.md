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

- (Q-99, 20/11) THỨ TỰ ĐỌC SAU NÉN MỚI (thay dòng trên): file này → `STATE/DANG-LAM.md` (mục của mình) → hồ sơ tính năng trong `DESIGN/TINH-NANG/` (đúng bước đang làm) → `HOP-THU/THU-HIEN-HANH.md` + CHỈ thư mới hơn số thư đã ghi trong DANG-LAM → tra Graphify phần đang làm rồi mới đọc mã. KHÔNG đọc lại toàn bộ CHO-SONNET.md. Ghi DANG-LAM trước khi nén và sau mỗi bước.

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
**Mở rộng (#244):** đồng bộ bằng MỘT lệnh `python -I JX1_OPS/TOOLS/dong_bo.py [--push]` (không autostash). Xung đột: file Tổng quản sinh (SONNET-SONG, TIEU-YEU, KHOA-XINGCHI, TIEN-DO, TONG-QUAN-GHI, BAN-GIAO) lấy bản origin; file chỉ-nối-thêm gộp union; file khác thì DỪNG và in tên. Cấm `checkout --ours` tay và cấm `stash drop` khi chưa `git stash show -p`.

## L13. HIỂU Ý CHỦ TRƯỚC, CHỦ CHỐT RỒI MỚI GIAO SONNET (chủ chốt 19/11 10:42)
Khi chủ bàn BẤT KỲ việc gì, Chat phải trình bày trước "thuộc hạ hiểu ý đại vương thế này" (kèm chỗ chưa chắc) và chờ chủ chốt; chỉ sau đó mới ghi quyết định và gửi thư Sonnet. Không giao nhanh khi chưa hiểu ý: thư sai gây xung đột (ví dụ #229 vs #230, Q-67 vs Q-68) và nếu chủ không nhắc thì không ai gỡ. Ngoại lệ: lệnh chủ đã ra rõ ràng, nguyên văn và không mơ hồ thì vẫn chuyển đúng nguyên văn kèm một câu xác nhận. Nếu đã lỡ gửi thư mâu thuẫn, Chat chủ động gửi thư gỡ ngay, không đợi chủ nhắc. Không bao giờ dùng luật này để ra lệnh Sonnet dừng (Q-56).

## L14. VIỆC CHỦ ĐÃ DUYỆT THÌ CHAT TỰ GÕ LỆNH LÊN CỬA SỔ CHAT CỦA SONNET (chủ chốt 19/11 13:43)
Khi chủ đã bảo/duyệt cài hay làm một việc (ví dụ Q-73 cài Node/command-code) mà Sonnet bị bộ kiểm soát quyền chặn hoặc cần một lệnh: Chat TỰ gõ lệnh vào khung chat Claude Code của Sonnet (qua Chrome), ghi rõ "chủ đã duyệt, Q-xx, giờ", KHÔNG hỏi lại chủ. Chỉ áp dụng cho việc chủ ĐÃ duyệt; việc chưa duyệt, vùng Đỏ (Main VM, tiền quá hạn mức, khóa ngoài phạm vi, xóa dữ liệu, APK cho chủ, đổi thông tin đăng nhập) vẫn phải hỏi chủ. Không bao giờ dùng để ra lệnh dừng (Q-56).

## L15. KHÔNG NGỒI CHỜ THƯ CHAT; GỌI CHAT BẰNG "A Xong" / "A Chat" / "B Xong" / "B Chat"; "SỐNG" PHẢI LÀ HOẠT ĐỘNG THẬT (chủ chốt 19/11 16:23)
Chủ bực vì A đứng chờ thư Chat ~30 phút mà Chat vẫn báo "đang chạy bình thường": gốc là nhịp tim của `cho_thu.py` bị tính là "sống". Vá ngay:
1. **Sonnet không bao giờ ngồi chờ thư Chat** (Q-56, L10). `cho_thu.py` chỉ dùng ngắn khi có việc chạy nền (dựng, tiểu yêu) cần đợi; không có thì làm việc kế trong `HANG-DOI-VIEC.md`. Hết việc đang giao = tự lấy việc, không chờ.
2. **Tín hiệu gọi Chat** (qua Chrome, gõ vào khung chat Chat, đúng nguyên văn): Sonnet A gõ `A Xong` (xong một việc, cần việc tiếp) hoặc `A Chat` (cần quyết định/hỏi); Sonnet B gõ `B Xong` / `B Chat`. Chat coi các chuỗi này là tín hiệu của Sonnet, không phải lời chủ. Dùng khi xong việc lớn hoặc cần Chat; không gõ liên tục.
3. **Chat kiểm theo hoạt động thật, không theo nhịp `cho_thu`:** mỗi vòng kiểm, nếu A hoặc B không có commit/ghi tệp việc >12 phút (chỉ có nhịp cho_thu) thì coi là CHỜ, Chat gửi ngay việc cụ thể trong hàng đợi và báo chủ đúng sự thật.
4. **Tổng quản** ghi trạng thái `CHO` (đứng chờ) khi chỉ có nhịp `cho_thu` mà không có commit/phiên làm việc >10 phút, tách riêng A và B (xem #248).

## L16 (chủ 19/11 16:39) — VIỆC CHỦ ĐÃ YÊU CẦU LÀ MẶC ĐỊNH ĐƯỢC PHÉP
Việc nằm trong lệnh chủ đã giao (kể cả các bước cần để thực hiện, như B gõ B Xong/B Chat qua Chrome) thì Chat và Sonnet làm luôn, không hỏi lại chủ. Chỉ hỏi chủ ở vùng Đỏ hoặc việc chủ chưa hề giao.

## L17 (chủ 20/11 00:00) — A TỰ CHỦ DỌN ĐƯỜNG VÀ KIỂM TRƯỚC KHI CHỦ TEST
Chủ test từ xa (không ở nhà), không được mất thời gian làm tay. Từ nay: (1) A có QUYỀN CHỦ ĐỘNG dừng/khởi động lại forwarder, tiến trình Test-36, gs001 (không trong 15 phút trước giờ test), LDPlayer T36test, dùng Stop-Process (không dùng taskkill, WMI hỏng); tiến trình Admin không dừng được vì UAC thì KHÔNG vượt UAC: A soạn một .ps1 tạo tác vụ Windows chạy quyền cao có hoàn tác, chủ chạy MỘT lần, từ đó A chạy bằng schtasks không cần UAC. (2) TRƯỚC mỗi lần chủ test, A chạy quy trình SẴN SÀNG TEST (thư #279): chọn đúng server (Test-36) + tài khoản, tự vào bằng LDPlayer tới màn hình game chính, chụp xác nhận, thu nhỏ LD ngay (L11), rồi MỚI báo chủ "SẴN SÀNG". Chủ không được phát hiện lỗi "treo ở chọn server/chờ máy chủ" lúc vào. Vùng Đỏ giữ nguyên (Server D, tiền, khóa/mật khẩu không vào chat, xóa dữ liệu).

## L18 (chủ 20/11 00:48) — TÀI KHOẢN TEST RIÊNG, CHỦ ĐỘNG, KHÔNG CHỜ CHỦ
Sonnet A (và B khi cần) TỰ TẠO tài khoản test riêng cho mình (vm_chay.py tao-tk-test, ví dụ tkatest01; không dùng chung `tkchuvuong` của chủ), tự vào test, không chờ chủ cấp. Khi chủ giao một mục thì HOÀN THÀNH bằng mọi giá; xong thì lấy tiếp việc trong hàng đợi; việc cần tiểu yêu thì gọi Tổng quản giao (TASKS/<mã>.md). Mật khẩu tài khoản test của A tự sinh, không vào kho/chat. Cách đăng nhập thực hiện theo luật an toàn của chính A (không nhập mật khẩu vào ô đăng nhập qua giao diện nếu luật chặn): dùng client bot không giao diện (E-01) hoặc APK thử có tệp tự đăng nhập do A tạo cho riêng tài khoản test (không bao giờ cho tk của chủ). Vùng Đỏ giữ nguyên.

## L19. HÀNG ĐỢI VIỆC + THƯ MỚI KHÔNG XÓA THƯ CŨ (Chat 20/11 16:30, chủ hỏi khi Chat ra lệnh liên tục)
1. Mỗi bên giữ mục "HÀNG ĐỢI" trong `STATE/DANG-LAM.md` (đánh số ưu tiên P0 làm ngay, P1, P2): mỗi dòng = mã thư (#306, #B-051...), việc, trạng thái (ĐANG/CHỜ/XONG/BỎ), lý do nếu BỎ.
2. Thư mới KHÔNG tự hủy việc đang làm dở. Chỉ hủy khi thư ghi rõ "THAY THẾ #x" hoặc "BỎ #x". Thư ghi "ƯU TIÊN CAO/KHẨN": dừng ở điểm an toàn, làm thư đó, rồi QUAY LẠI việc cũ theo hàng đợi.
3. Gặp 2 việc xung đột (cùng một lần restart gs001, cùng file): gộp thành MỘT lượt, ghi vào hàng đợi.
4. Việc nào bỏ qua phải ghi BỎ + lý do vào DANG-LAM; cấm im lặng bỏ. Chat đối chiếu hàng đợi với các thư đã gửi mỗi vòng kiểm.
5. Trước khi nén chat: hàng đợi phải cập nhật (đã có luật Q-99).

## L20 (chủ chốt 21/11 11:46) — ĐỌC SỔ TAY `HIEU-GAME/` TRƯỚC KHI SỬA BẤT CỨ PHẦN NÀO
Kho `HIEU-GAME/` (9 nhóm, mục lục ở `HIEU-GAME/README.md`) là công sức đã tích lũy của chủ và các phiên trước. Cấm đọc ngược mã gốc rồi đoán khi sổ tay đã có.
1. Trước khi sửa, thử hoặc báo một phần nào (trang bị, cường hóa, phi phong, ngựa, quái, rơi đồ, gói tin, giao diện...): mở sổ tay nhóm tương ứng trong `HIEU-GAME/` và đọc.
2. Mọi thư giao việc, mục DANG-LAM và báo cáo có dòng **"ĐÃ ĐỌC SỔ TAY: <đường dẫn file>"** (hoặc "KHÔNG CÓ SỔ TAY cho phần này" + tạo mục thiếu trong hàng đợi).
3. Báo cáo thiếu dòng này thì KHÔNG được ghi "XONG"; Chat trả lại, tính một lần trả lại.
4. Sổ tay sai hoặc thiếu thì sửa ngay tại chỗ (cùng commit với phần sửa) để công sức cộng dồn.
5. Điều chủ vừa chốt trong chat phải ghi vào kho (QUYET-DINH hoặc thư) NGAY trong lượt đó và liệt kê trong DANG-LAM trước khi nén.
6. Hàm engine Cocos2d-x lạ (client) thì tra mã Cocos2d-x ĐÚNG PHIÊN BẢN của client (A xác nhận phiên bản từ mã client; nguồn: https://github.com/cocos2d/cocos2d-x, MIT), không dùng tài liệu v4 nếu client cũ hơn. Cocos2d-x không có thông tin giao thức/dữ liệu JX1.

6. CƠ CHẾ TỰ ĐỘNG (chủ duyệt 21/11 16:33): Tổng quản chạy `TOOLS/kiem_so_tay.py` mỗi lần đẩy trạng thái; báo cáo A/B có chữ XONG/DONE về phần game mà thiếu dòng "ĐÃ ĐỌC SỔ TAY" thì được ghi vào `STATE/TRA-LAI-SO-TAY.md`. A và B ĐỌC TỆP NÀY ĐẦU MỖI LƯỢT và bổ sung dòng thiếu; chưa bổ sung = PARTIAL. Mọi thư Chat giao việc có dòng "SỔ TAY LIÊN QUAN: <tệp HIEU-GAME/>". Việc rà lại sửa đổi sai (cường hóa, phi phong, giật ngựa) và lấp chỗ thiếu của sổ tay giao cho tiểu yêu; Chat duyệt kết quả trước khi A/B sửa tiếp.

## L21 (chủ chốt 21/11 22:02) — LUẬT RIÊNG CỦA B: xem `STATE/LUAT-RIENG-B.md` (việc đầu tiên mọi việc là đọc hiểu game, khối "HIỂU GAME", Chat kiểm trước).

## L22 (chủ chốt 21/11 22:23) — LẬP KẾ HOẠCH BA BÊN TRƯỚC KHI GIAO: xem `STATE/QUY-TRINH-LAP-KE-HOACH.md` và lịch `STATE/LICH-CONG-VIEC.md`.

## L23 (chủ chốt 22/11 00:17) — A VÀ B CHỦ ĐỘNG GÕ VÀO KHUNG CHAT ĐỂ ĐÁNH THỨC CHAT (vá L15; Chat không phải kiểm dày)
Nguyên nhân sự cố 22/11 00:14: A xong vc37 lúc 22:58, B xong đề xuất 22:35, chỉ ghi vào kho rồi chờ; Chat cũng chờ → cả hai bên chờ ~75 phút. Chủ nói: không cần Chat kiểm dày, chỉ cần A/B chủ động gọi.
1. BẮT BUỘC: mỗi khi A/B (a) xong một việc hoặc một buổi chụp/đo/build, (b) cần Chat duyệt/quyết định/chủ, (c) bị chặn quyền hoặc gặp lỗi, (d) hết việc trong lịch — việc CUỐI CÙNG của lượt là gõ vào khung chat Chat (Claude in Chrome / trình duyệt, URL phiên Chat: https://claude.ai/code/session_01MrvZcvMaZXNKa8dLsj2hfU) đúng mẫu: `A Xong hh:mm: <1 câu việc đã xong + tệp báo cáo>; cần: <việc tiếp/quyết định>` hoặc `A Chat hh:mm: ...`; B dùng `B Xong`/`B Chat`. Gõ xong nhấn gửi (Ctrl+Enter nếu Chat đang bận) và xác nhận tin hiện trong khung.
2. KHÔNG kết thúc lượt, không ghi "chờ Chat" khi chưa gõ tin này. Báo kho (TU-SONNET/A-B.md) vẫn làm, nhưng tin gõ là tín hiệu đánh thức.
3. Đang làm việc dài: gõ `A Chat hh:mm: tiến độ ...` tối đa mỗi 30 phút nếu có thay đổi đáng kể; không gõ liên tục.
4. Hết việc trong lịch: gõ `A Chat hh:mm: RẢNH` (không tự bịa việc to; có thể làm việc nền trong LICH-CONG-VIEC.md rồi gõ).
5. Nếu hộp thoại "Đăng nhập lại" chặn khung nhập thì bấm "Để sau" rồi gõ lại; nếu khung Chat bận, dùng Ctrl+Enter (hàng đợi).
6. Chat: mỗi thư giao việc kết thúc bằng dòng "XONG thì gõ `A Xong`/`B Xong` vào khung Chat (L23)". Chat chỉ đặt vòng kiểm thưa 30 phút làm lưới an toàn, và đọc tin A/B gõ ngay khi tới. Tổng quản kiểm: A/B im >40 phút mà không có gõ gọi Chat → ghi CHO vào TONG-QUAN-GHI để Chat biết.

## L24 (chủ chốt 22/11 00:32) — KHÔNG KẾT LUẬN "HỎNG / MẤT / KHÔNG CÓ" KHI CHƯA KIỂM ĐẦU VÀO; HÀNG ĐỢI ≥10 VIỆC
Sự cố 22/11 00:25: Chat chạy `bang_tien_do.py` với `--root` sai thư mục (cha thay vì `JX1_OPS`), ra 0/0, rồi báo chủ "công cụ hỏng, bảng không dựng được" — SAI; chạy đúng ra 93/124 việc. Chủ phải hỏi lại, mất thời gian và niềm tin.
1. Công cụ ra rỗng/0/lỗi/không thấy: TRƯỚC khi báo chủ "hỏng/mất/không có", Chat (và A, B) phải kiểm lại THAM SỐ và ĐƯỜNG DẪN vào (đường dẫn gốc, thư mục làm việc, tên file, nhánh), chạy lại ít nhất một lần với giá trị đúng, và đọc phần `--help`/đầu tệp công cụ. Chỉ báo "hỏng/mất" khi đã thử đúng mà vẫn rỗng, và nêu đã thử gì.
2. Khi báo chủ điều có thể sai vì mình chưa kiểm hết, ghi rõ "CHƯA KIỂM: ..." và không dùng giọng chắc chắn ("hỏng", "mất", "không còn").
3. `TOOLS/bang_tien_do.py` đã tự dò `JX1_OPS` nếu `--root` là thư mục cha, và báo LỖI rõ khi bảng rỗng — chạy chuẩn: `python3 -I JX1_OPS/TOOLS/bang_tien_do.py --root JX1_OPS --out /home/claude/board` rồi đăng artifact (publish_files, `index.html`).
4. BẢNG TIẾN ĐỘ là nguồn của HÀNG ĐỢI: A và B luôn có ≥10 việc trong `STATE/HANG-DOI-VIEC.md` / `HANG-DOI-VIEC-B.md`; dưới 10 thì nạp lại từ bảng (việc "chờ"/"đang chạy"/"bị chặn") + `LICH-CONG-VIEC.md`. Tổng quản kiểm mỗi vòng; Chat dựng lại bảng và đăng artifact mỗi lần đổi tài khoản và mỗi khi số việc đổi đáng kể, và ghi URL artifact vào `HOP-THU/KHOI-DONG-CHAT.md`.
