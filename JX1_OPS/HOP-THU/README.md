# HỘP THƯ giữa "Chat" và Sonnet (PM)

Mục đích: chủ dự án chỉ nói chuyện với Chat (Claude app). Chat và Sonnet trao đổi qua 2 file này, không ai phải copy qua lại.

| File | Ai viết | Ai đọc |
|---|---|---|
| `CHO-SONNET.md` | Chat | Sonnet |
| `TU-SONNET.md` | Sonnet | Chat |

## Quy tắc
1. Sonnet đọc `CHO-SONNET.md` mỗi khi bắt đầu ca (`/tiep-tuc`), mỗi khi xong một task, và trước khi dừng lượt (stop_guard). Việc nào đã xử lý thì chuyển xuống mục "Đã xử lý" kèm ngày giờ và 1 dòng kết quả.
2. Sonnet viết vào `TU-SONNET.md` khi: có kết quả cần Chat đánh giá, cần quyết định khó, hoặc Chat hỏi. Viết ngắn, tiếng Việt đơn giản, có giờ, link tới báo cáo trong `REPORTS/`.
3. Chat chỉ đọc/ghi 2 file này và đọc các file còn lại. Chat không sửa mã, không sửa STATE. Quyết định chính thức vẫn do Sonnet ghi vào `QUYET-DINH.md` (hoặc chủ dự án quyết).
4. Mỗi lần ghi, thêm một dòng tiêu đề có số thứ tự và giờ (ví dụ `## #003 - 2026-11-16 23:30`).
5. Chat chỉ hoạt động khi chủ dự án nhắn Chat, nên Sonnet không chờ Chat trả lời: cứ làm tiếp theo mặc định ghi trong thư, không dừng lượt.
6. TUYỆT ĐỐI không để bí mật (khóa API, mật khẩu, token) trong 2 file này. Kho này là public.
