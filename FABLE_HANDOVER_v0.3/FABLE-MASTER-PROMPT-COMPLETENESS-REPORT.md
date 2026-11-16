# BÁO CÁO ĐỘ ĐẦY ĐỦ CỦA MASTER PROMPT – FABLE

Ngày 2026-11-16 · Viết cho bộ tài liệu v0.2, đã chỉnh ở v0.3 (bỏ Secret Vault, chốt thế giới Bot; xem `CHANGELOG-v0.3.md`) · Viết cho chủ dự án

---

## 1. Đã đọc được toàn bộ Master Prompt chưa?

**Rồi.** Bản anh gửi lần thứ ba là bản đầy đủ: 1.241 dòng, 16 phần, **30 mục**, kết thúc bằng "Chỉ thị bắt đầu cho Fable". Tôi đã đọc hết.

Diễn biến, để anh đối chiếu:

| Lần | Nhận được | Tình trạng |
|---|---|---|
| 1 | Master Prompt | Bị cắt ở dòng 838, giữa mục 21. Bộ v0.1 làm từ bản này. |
| 2 | Yêu cầu khắc phục (13 mục) | Đầy đủ. |
| 3 | Master Prompt gửi lại | Đầy đủ 30 mục. |

Lịch sử cuộc trò chuyện này không chứa phần sau mục 21 cho tới khi anh gửi lại, và tôi không đọc được các cuộc trò chuyện khác của anh. Vì vậy **nếu anh từng nêu yêu cầu bổ sung ở một cuộc trò chuyện khác mà không nằm trong ba văn bản trên thì tôi chưa có**. Ngoài điểm đó, không còn phần nào không khôi phục được.

## 2. Phần sau mục 21 gồm những gì

| Mục | Nội dung | Đã đưa vào |
|---|---|---|
| 21 (cuối) | Opus phải thiết lập quy trình reviewer độc lập | Operating Rules mục 7 |
| 22 | Báo cáo cuối ngày: nghĩa vụ của Opus, giờ báo cáo, mẫu 8 mục, tiêu chuẩn | Operating Rules mục 11, mẫu trong Memory Structure |
| 23 | Nơi lưu báo cáo và trạng thái | Memory Structure |
| 24 | Kế hoạch thử nghiệm 7 ngày và 10 chỉ số đánh giá | Roadmap phần A |
| 25 | 17 báo cáo A–Q Opus phải bàn giao | Handover mục 7 |
| 26–28 | Ba giai đoạn; chủ dự án phê duyệt kế hoạch tổng thể trước khi triển khai | Master mục 5, Operating Rules mục 1a |
| 29 | Cơ cấu quyền hạn cuối cùng | Master mục 4 |
| 30 | 10 tiêu chuẩn thành công | Master mục 6 |
| Chỉ thị cho Fable | 5 điều phải nêu khi bàn giao | Handover mục 1, 2, 4, 5, 9 |

## 3. Đối chiếu v0.1

**Đã phản ánh đúng:** định hướng game; vai trò Fable và Opus; phân cấp L0–L5; nhãn tin cậy; danh sách hoạt động; quy tắc Git; nhóm thao tác phải xin phép; nguyên tắc không phụ thuộc một model. Câu bị cắt ở cuối mục 21 tôi đã đoán đúng ("…không kiểm tra ảnh hưởng").

**Thiếu vì bản bị cắt:** toàn bộ bảng ở mục 2 trên. Nặng nhất là kế hoạch 7 ngày, cổng phê duyệt kế hoạch và 17 báo cáo A–Q: v0.1 không có.

**Thiếu vì chưa có văn bản thứ hai:** triết lý "chủ dự án chỉ xem kết quả"; thang tự sửa lỗi; worker phối hợp trực tiếp; Secret Vault; vai trò Codex trong bảng phân cấp; tự chuyển model khi hết quota; 7 câu hỏi của báo cáo ngày.

**Do tôi tự đề xuất trong v0.1** (nay đã ghi rõ là đề xuất, hoặc đã thay): mẫu báo cáo ngày; lộ trình game M0–M9; cách đặt Task ID; gộp các file trạng thái.

**Mâu thuẫn với yêu cầu của anh, đã sửa:**

| v0.1 viết | Vì sao sai | v0.2 |
|---|---|---|
| Worker bị chặn thì dừng và báo Opus | Dồn mọi lỗi lên Opus | Thang tự sửa 9 bước; Opus chỉ nhận lỗi khó |
| Muốn sửa file ngoài phạm vi phải chờ Opus | Opus thành nút thắt | Worker thỏa thuận trực tiếp; chỉ hợp đồng dùng chung mới cần Opus |
| Mỗi task một file báo cáo riêng và bảng nhật ký | Thủ tục thừa | Bằng chứng là commit + kết quả test + vài dòng trong task |
| Gắn nhãn tin cậy cho mọi phát biểu | Quá nặng | Chỉ trong tài liệu kiến trúc, ADR, báo cáo nghiên cứu |
| Mẫu báo cáo ngày của tôi | Khác mẫu của anh | Theo mẫu của anh, chia hai lớp |
| Gộp 7 file trạng thái còn 3 | Anh nêu rõ 7 file ở hai chỗ | Giữ 7 file, ba file danh sách tự sinh |
| Câu hỏi mở viết bằng thuật ngữ | Anh không lập trình | Viết lại bằng lời thường |

## 4. Tài liệu đã cập nhật

Cả 8 tài liệu lên v0.2, thêm báo cáo này. (Tài liệu Secret Vault của v0.2 đã bỏ ở v0.3.) Bản v0.1 giữ nguyên trong `archive/fable-v0.1/`.

## 5. Quy định đã đơn giản hóa

- Không báo cáo Markdown riêng cho mỗi thao tác hay mỗi task.
- Mẫu task bỏ bảng nhật ký; file đã sửa xem trong Git, không chép lại.
- Bảng trạng thái task do script sinh, không ai sửa tay.
- Đổi worker không cần văn bản bàn giao; file task và commit là đủ.
- Việc mức L0–L2 được cho qua bằng reviewer độc lập và kiểm tra tự động, không qua Opus.
- AI chỉ đọc trạng thái hiện tại và task của mình khi bắt đầu, không đọc lại toàn bộ nhật ký.

Không đơn giản hóa: kiểm thử, review độc lập, khả năng truy vết và khôi phục.

## 6. Cơ chế tự sửa lỗi

Chín bước đúng như anh nêu: phát hiện → phân tích → sửa → chạy lại test → kiểm tra hồi quy → thử phương án khác → chuyển worker chuyên môn hoặc model mạnh hơn → Opus chỉ nhận xung đột, kiến trúc, lỗi khó → chỉ báo anh khi rủi ro lớn hoặc cần anh quyết.

Kèm theo: lỗi do review tìm ra quay thẳng về worker đã viết; anh không bao giờ phải chuyển log; chỉ được nói "đã sửa" sau khi test lại qua; không sửa bằng cách tắt test; mặc định sau 3 phương án thất bại thì tự chuyển bậc, giữ nguyên mã task.

## 7. Secret Vault

Đã bỏ ở v0.3 theo quyết định của chủ dự án. Bản thiết kế cũ còn trong `archive/fable-v0.2/` để đối chiếu, không dùng.

## 8. Quyền hạn của Opus

| Vùng | Phạm vi | Cách làm |
|---|---|---|
| Xanh | Mọi thứ trong máy phát triển và thư mục dự án | Tự làm, không hỏi |
| Vàng | Xóa hoặc ghi đè thứ không tái tạo được trong thư mục dự án | Tự sao lưu rồi tự làm, không hỏi |
| Đỏ | Server đang vận hành; dữ liệu thật; xóa không khôi phục được; ghi đè source gốc; mật khẩu và quyền bảo mật; ghi đè lịch sử Git; công khai mã nguồn hoặc bí mật; chi phí ngoài ngân sách | Chuẩn bị sẵn, hỏi anh bằng lời thường kèm đề xuất, làm việc khác trong lúc chờ |

Ngoài ra anh phê duyệt kế hoạch tổng thể một lần trước khi đội AI bắt đầu triển khai, đúng theo mục 28 của Master Prompt.

## 9. Báo cáo cuối ngày

- Chỉ Opus gửi, 22:00 giờ Việt Nam. Máy tắt thì gửi ngay khi chạy lại. Sự cố nghiêm trọng báo ngay.
- Phần chính trả lời 7 câu của anh bằng lời thường, mục "Cần anh quyết định" đặt trên cùng.
- Phụ lục kỹ thuật ở cuối giữ các mục trong mẫu gốc của anh (số task, bảng agent, bằng chứng, chi phí, đánh giá của Opus). Anh không cần đọc; nó phục vụ việc kiểm tra và AI kế nhiệm.
- Số liệu phải là số đo thật; không có thì ghi "không có dữ liệu".
- Opus phải dựng lịch chạy thật; chưa có thì không được hứa báo cáo tự gửi.

## 10. Còn thiếu gì

Về tài liệu: không còn gì thiếu so với ba văn bản đã nhận.

Về thông tin, cần anh cung cấp hoặc trả lời (Opus sẽ hỏi lại trong báo cáo đầu tiên):
- Địa chỉ repo GitHub của dự án.
- Bảy câu hỏi về game trong `docs/01-PRODUCT-REQUIREMENTS.md` mục H.

## 11. Gói bàn giao đã sẵn sàng chưa?

Về nội dung: **sẵn sàng**. Theo yêu cầu của anh, tôi **chưa gửi cho Opus**; không sửa source, không sửa server, không cài plugin, không tạo worker. Gói sẽ được chuyển khi anh xem xong và đồng ý.
