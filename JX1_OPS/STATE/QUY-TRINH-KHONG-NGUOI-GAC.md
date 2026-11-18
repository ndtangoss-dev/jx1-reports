# QUY TRÌNH MỚI: KHÔNG NGƯỜI GÁC (chủ quyết 18/11 16:36, Q-48)

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

## Chat
- Chat kiểm kho 30 phút/lần CHỈ khi có đợt đang chạy; hết đợt thì tạm ngừng lịch kiểm, chủ nhắn Chat thì mới dậy. Chat báo chủ khi: đợt xong, Sonnet cần chủ, sự cố, hạn mức.
