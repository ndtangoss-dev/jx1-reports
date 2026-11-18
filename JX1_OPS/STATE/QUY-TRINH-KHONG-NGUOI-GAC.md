# QUY TRÌNH MỚI: KHÔNG NGƯỜI GÁC (chủ quyết 18/11 16:36, Q-48)

> **[CHAT 19/11 00:40 — BẢN NÀY ĐÃ LỖI THỜI]** Các câu "hết việc thì dừng", "stop_guard cho dừng khi đã ghi XONG ĐỢT", "9 phút không có CHAT-DAY thì dừng/[CAN-CHU] vòng đứt" KHÔNG CÒN hiệu lực. Luật hiện hành: `STATE/LUAT-COT-LOI.md` L10 + L11 (không bao giờ tự dừng; chờ bằng `cho_thu.py`; chỉ dừng khi có `STATE/DUNG-VONG.flag`).


Lý do: người gác gọi `claude -c -p` ~12 lần/giờ, ngốn hạn mức Claude của chủ. Chủ chỉ làm việc với Chat; không giao việc trực tiếp cho Sonnet.

## Vai trò
- Chủ ⇄ Chat (cửa sổ chat). Chat ⇄ Sonnet bằng hòm thư (CHO-SONNET.md / TU-SONNET.md). Sonnet ⇄ tiểu yêu (Codex) như cũ.
- Chat gom việc thành ĐỢT (1 thư lớn, nhiều việc, thứ tự rõ, tiêu chí xong rõ). Ít thư, ít vòng hỏi đáp.

## Sonnet làm việc theo đợt
1. Khi được đánh thức: đọc hòm thư một lần, làm hết các việc theo thứ tự, ghi MỘT báo cáo "XONG ĐỢT #N" vào TU-SONNET.md (đã xong / còn / cần chủ), push, rồi DỪNG. Không thăm dò, không "nhịp gác", không viết dòng chờ.
2. Hết việc thì dừng; không tự bịa việc. Hết hạn mức thì dừng và ghi 1 dòng.
3. Câu hỏi cho Chat: ghi [HỎI-CHAT] trong báo cáo, KHÔNG chặn cả đợt: làm tiếp phần không phụ thuộc, nêu giả định đã dùng.
4. Việc chạm vùng Đỏ: chuẩn bị, ghi [CAN-CHU], không làm.

## Đánh thức Sonnet (không có người gác)
- Chat báo chủ khi thư mới sẵn sàng. Chủ chỉ cần nhắn Sonnet MỘT câu cố định: **"Đọc hòm thư CHO-SONNET rồi làm."** (không giao việc gì khác).
- Chat không tự đánh thức được Sonnet (không có kênh).

## Tổng quản / công cụ
- Tổng quản chỉ giám sát tiểu yêu và ghi tệp; KHÔNG được gọi `claude`/`claude -c -p`. Sự kiện của Tổng quản ghi vào STATE/TONG-QUAN-GHI.md; Sonnet đọc khi bắt đầu đợt.
- Gỡ JX-Guard (người gác) và mọi lịch gọi claude; gỡ ghi chú "GÕ CỬA" khỏi quy trình. stop_guard: cho Sonnet dừng khi đã ghi "XONG ĐỢT".

## Chat (sửa 18/11 16:50: chủ gọi Chat, Chat không tự quét)
- Chat KHÔNG có lịch kiểm, KHÔNG tự quét kho. Chat chỉ dậy khi chủ gọi.
- Vòng làm việc: Sonnet xong đợt → chủ thấy → chủ gọi Chat "đọc" → Chat đọc TU-SONNET/kho, hai bên bàn cách làm → khi chốt, Chat đẩy thư lên CHO-SONNET.md và báo "đã đẩy" → chủ nhắn Sonnet "Đọc hòm thư CHO-SONNET rồi làm." → Sonnet làm đợt mới.
- Chat báo chủ ngay trong lượt trả lời; không có báo giờ định kỳ.
