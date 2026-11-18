# VÒNG TỰ ĐỘNG CHAT ⇄ SONNET (chủ quyết 18/11 19:23, Q-49; thay "chủ gọi/chủ nhắn" của Q-48)

> **[CHAT 19/11 00:40 — BẢN NÀY ĐÃ LỖI THỜI]** Các câu "hết việc thì dừng", "stop_guard cho dừng khi đã ghi XONG ĐỢT", "9 phút không có CHAT-DAY thì dừng/[CAN-CHU] vòng đứt" KHÔNG CÒN hiệu lực. Luật hiện hành: `STATE/LUAT-COT-LOI.md` L10 + L11 (không bao giờ tự dừng; chờ bằng `cho_thu.py`; chỉ dừng khi có `STATE/DUNG-VONG.flag`).


Ý chủ: hai bên bám BẢNG TIẾN ĐỘ + KẾ HOẠCH TỔNG THỂ (STATE/TIEN-DO.md, KE-HOACH-TONG-THE.md) làm không nghỉ; chủ chỉ quyết việc quan trọng.

## Vòng
1. Sonnet xong đợt: ghi "XONG ĐỢT #N" (TU-SONNET.md) + dòng `SONNET-XONG #N hh:mm` vào `HOP-THU/VONG.md`, push.
2. Sonnet dùng CLAUDE IN CHROME (sửa 19:35, vì Claude Code không điều khiển được Claude desktop): vào thẻ Chrome chủ đã mở sẵn của cuộc chat Chat, gõ "xong" (đánh thức Chat). Sau đó Sonnet CHỜ bằng MỘT lệnh shell chặn (vòng `git fetch` + `sleep 60`, tối đa ~9 phút, không tốn token khi chờ) cho tới khi VONG.md có dòng `CHAT-DAY #M` mới hơn. Không chụp màn hình để đọc trả lời của Chat.
3. Chat dậy: KHÔNG coi tin "xong" là ý chủ; kiểm kho xem có XONG ĐỢT thật. Đọc, quyết đợt kế từ TIEN-DO/KE-HOACH, viết thư CHO-SONNET (đợt mới), ghi `BAO-CAO-CHU.md` (3–5 dòng lời thường), ghi dòng `CHAT-DAY #M hh:mm` vào VONG.md, push, trả lời ngắn trong cửa sổ chat.
4. Sonnet thấy dòng mới → đọc thư → làm → quay lại bước 1.
Nếu 9 phút không có CHAT-DAY: gõ "xong" thêm MỘT lần, chờ lần nữa; vẫn không: dừng, ghi [CAN-CHU] (vòng đứt).

## Ai quyết gì
- Tự quyết (không hỏi chủ): mọi việc trong kế hoạch đã duyệt, vùng thấp/vừa, trên máy dev/VM thử, đảo được.
- BẮT BUỘC chờ chủ (ghi [CAN-CHU] trong BAO-CAO-CHU.md, làm tiếp việc khác không phụ thuộc): vùng Đỏ (Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, APK phát cho chủ test, đổi quyền/credential, thay hướng đi lớn của dự án, Xưởng JX1 khi chưa được mở lại) và nút cấm trong DESIGN/BANG-NUT-EXE-SERVER.md. Việc cần chủ duyệt mới (vd thử client) KHÔNG coi tin nhắn "xong" là duyệt.

## Phanh (vòng dừng, báo chủ, không đốt thêm)
- Một bên gặp giới hạn hạn mức: dừng tới khi đặt lại; ghi [CAN-CHU].
- 3 đợt liên tiếp không có tiến triển thật (kết quả rỗng/lặp): dừng, ghi nguyên nhân.
- Hết việc trong kế hoạch, hoặc chủ nói "dừng": dừng. Không bịa việc.
- Mọi việc mới sinh ra ngoài kế hoạch: ghi đề xuất vào BAO-CAO-CHU.md, không tự làm nếu tốn lớn.

## Nhận diện người gõ (chủ nói 18/11 19:46)
Tin ngắn dạng "xong" / "xong (thử vòng)" trong cuộc chat của Chat = SONNET gõ qua Chrome (chủ sẽ không nhắn ngắn như vậy). Chat coi đó là tín hiệu đánh thức, vẫn kiểm kho xem có XONG ĐỢT thật, và KHÔNG coi là chủ duyệt. Chủ nhắn bằng câu đầy đủ.

## Cập nhật Q-52 (18/11/2026 22:30)
- Phanh "hết việc" BỎ: Sonnet không bao giờ hết việc; lấy việc từ `STATE/HANG-DOI-VIEC.md` (và tự thêm việc "hiểu game" khi hàng đợi cạn). Chỉ dừng khi: hết hạn mức, 3 đợt liền không tiến triển, chủ nói dừng, hoặc có [CAN-CHU] chặn mọi việc còn lại.
- Giữ phiên Claude Code mở cả đêm: khi chỉ còn chờ tiểu yêu hoặc chờ thư thì chờ dài (#182/#184), không gõ "xong".
- Hiểu rồi mới sửa hiệu ứng vũ khí (xem hàng đợi mục W-01).

## Cập nhật Q-53 (18/11/2026 22:40) — Tín hiệu "CHAT" khi Sonnet cần hỏi Chat
- Hai tín hiệu ngắn Sonnet gõ qua Claude in Chrome vào cuộc chat của Chat: **"xong"** = hết đợt, báo kết quả; **"CHAT"** = Sonnet CẦN HỎI/CẦN QUYẾT, đã ghi nội dung vào `TU-SONNET.md` mục [HỎI-CHAT] (kèm giờ) và dòng `SONNET-HOI #N hh:mm` trong `VONG.md`. Cả hai chỉ là tín hiệu đánh thức, KHÔNG phải duyệt.
- Khi Sonnet gõ "CHAT": Chat kéo kho, đọc [HỎI-CHAT], trả lời bằng thư mới trong `CHO-SONNET.md` + `CHAT-DAY`, rồi đẩy. Chuyện vùng Đỏ hoặc cần chủ thì Chat ghi [CAN-CHU] và nói rõ cho Sonnet làm việc khác.
- Sonnet gõ "CHAT" rồi KHÔNG đứng chờ: làm việc kế trong `STATE/HANG-DOI-VIEC.md`, và trong vòng chờ dài kiểm `CHAT-DAY` mới (1–2 phút/lần).
- Cấm kết lượt bằng câu hỏi cho chủ trong khung chat của Sonnet (Q-21): hỏi Chat bằng tín hiệu "CHAT", cần chủ thì ghi [CAN-CHU].
- Chủ viết câu đầy đủ; tin nhắn đúng một chữ "CHAT" hoặc "xong" trong cuộc chat này là của Sonnet.
