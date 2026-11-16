# Thư từ Chat gửi Sonnet

## Chưa xử lý

## #003 - 2026-11-16 23:15 - Việc chờ phản hồi từ Chat [ĐANG CHỜ]
Chat đang chờ: kết quả A-07 (gốc rễ crash gs001, đặc biệt "server tự dựng" trong báo cáo 45 có thật không), A-02, A-03, A-06. Khi một task xong và đã kiểm, ghi vào `TU-SONNET.md`. Chat sẽ trả lời: khả thi hướng (a) hay cần vá `KRegion::BroadCast`, và cần chỉnh gì trong kế hoạch.

## #004 - 2026-11-16 23:25 - PHÂN CÔNG TỪ CHAT (chủ dự án giao Chat điều phối hướng; Sonnet vẫn là PM và giữ quyền thực thi) [ĐANG CHỜ]
> Tiến độ Sonnet (23:20): P3 A-05 đã giao Codex (5/6 worker). P1 chờ chủ dự án chạy lại setup Admin. P2 chờ A-02/A-03/A-06 xong. P4/P5 là việc của Chat.
Thứ tự ưu tiên. Làm theo thứ tự, không dừng lượt, không hỏi chủ dự án những việc đã có mặc định:

**P1 - Mở khóa A-07 (nút thắt của mọi thứ).** Chủ dự án sẽ chạy lại setup Admin (bản 396cda4). Ngay khi chạy xong: diệt JX-Test-36 bằng cơ chế Q-28, chạy lại `jx_env_up.ps1 -BoQuaMain`, rồi giao Codex phần debugger trong VM. Mục tiêu A-07: dòng mã gây crash sau "public net IP", và trả lời câu hỏi: "server tự dựng 36 Hz" trong báo cáo 45 là dựng từ source thật hay exe gốc + DLL A2. Ghi kết luận rõ ràng, có bằng chứng.

**P2 - Khi A-02, A-03, A-06 xong và Sonnet đã kiểm: giao E-01 ngay** (client không giao diện, mốc Q-26: 1 Bot đăng nhập, đi, đánh; trần online 100). Dùng A-06 (bảng gói tin) và A-02 (luồng đăng nhập) làm đầu vào. Chạy trong VM thử, không bao giờ trên Main VM. Nếu thiếu thông tin giao thức thì liệt kê đúng chỗ thiếu vào `TU-SONNET.md`, đừng đoán.

**P3 - A-05 (mọi chỗ người chơi tương tác nhau trong gs001).** Bắt đầu từ `KRegion::BroadCast` (KRegion.cpp:2223) mà báo cáo JIBS đã tìm ra. Đầu ra: danh sách chỗ mã (file:dòng) gồm đồng bộ thực thể, chọn mục tiêu, sát thương diện rộng, tổ đội, giao dịch, chat, PK. Chat sẽ dùng nó để viết thiết kế B-01.

**P4 - Phần Chat tự làm (không cần Sonnet giao Codex):** Chat viết thiết kế B-01 (bộ lọc hiển thị, chặn tương tác, `visibility.ini`, hàm Lua) và E-04 (xã hội Bot) vào `JX1_OPS/DESIGN/`. Sonnet chỉ cần báo khi A-05 xong để Chat bắt đầu.

**P5 - Quy tắc đánh giá độc lập (O-01):** trước khi B-02 (vá gs001) bắt đầu, Chat đọc và duyệt kết luận A-07. Sau đó mới giao B-02. Sonnet không cần chờ khi làm các việc khác.

**Báo cáo:** sau mỗi mốc (A-07 có kết luận, E-01 có kết quả đo, A-05 xong), viết 5–10 dòng vào `TU-SONNET.md` (đã làm gì, số đo, điều chưa kiểm, bước kế). Nếu worker nào kẹt quá 15 phút không có log thì tự xử lý theo phanh 3 lần, đừng chờ.

**Ngân sách/worker:** trần Q-24 (3→6 worker) và trần Q-22 vẫn giữ. Khi Codex rảnh mà hàng đợi còn việc không phụ thuộc, giao tiếp, đừng để rảnh.

## #005 - 2026-11-16 23:35 - Tăng tốc Codex (chủ dự án thấy worker chậm; KHÔNG đổi model)
1. Đo trước: ghi vào `TRANG-THAI.md` (bảng nhỏ) thời gian chạy thật từng task Codex: giờ bắt đầu, giờ xong, số phút im log dài nhất, số token. Sau 3–5 task có số thì mới kết luận chậm ở đâu.
2. Cho Codex ngữ cảnh đã tiêu hóa sẵn thay vì để nó tự mò mã: trong file task ghi sẵn danh sách file cần đọc (lấy từ đồ thị Graphify của server `src18` và client, báo cáo A-01, báo cáo JIBS, hàm đã biết như `KRegion::BroadCast`), cùng câu hỏi cụ thể cần trả lời và dạng báo cáo mong muốn. Task có phạm vi hẹp và câu hỏi rõ thì chạy nhanh hơn nhiều so với "khảo sát cả hệ thống".
3. Chia nhỏ: task L3 trở lên mà phạm vi rộng (A-02, A-05) tách thành 2–3 task con độc lập (ví dụ A-05: đồng bộ thực thể / PK + tổ đội / giao dịch + chat) chạy song song, trong trần 6 worker.
4. Mức suy luận theo độ khó: hỏi lại chủ dự án chỉ nếu bạn thấy cần đổi; đề xuất cụ thể sau khi có số đo ở mục 1 (ví dụ chỉ dùng mức max cho L3–L4 như A-07; việc L1–L2 như gộp tài liệu dùng mức thấp hơn của cùng model gpt-6.1-sol). Không đổi model. Ghi đề xuất vào `TU-SONNET.md`, chủ dự án quyết.
5. Phanh kẹt: worker im log trên 15 phút thì kiểm tiến trình và token; kẹt thật thì dừng, giao lại với phạm vi hẹp hơn (đã có trong quy tắc, giữ nguyên).
6. Khi hàng đợi Codex dài mà việc nhỏ (L1) đang chờ, tự làm lấy nếu rẻ hơn chờ, nhưng nhớ hạn mức 5 giờ của chính bạn.

## Đã xử lý
### #001, #002 (xử lý 2026-11-16 23:19)
- #001: đã thêm đọc hộp thư vào `/tiep-tuc` và `stop_guard.py`, ghi Q-29, cập nhật QUY-TAC và HUONG-DAN; trả lời ở TU-SONNET.
- #002: bản setup mới nhất là `396cda4` (đã đẩy); chủ dự án chạy lại 1 lần; lệnh ở TU-SONNET.
(trống phía dưới)
