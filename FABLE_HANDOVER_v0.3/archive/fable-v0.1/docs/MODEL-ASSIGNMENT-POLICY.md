# MODEL ASSIGNMENT POLICY

Phiên bản v0.1 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

Mục tiêu: dùng model phù hợp nhất cho từng việc, tiết kiệm quota mà không giảm chất lượng. Đây là chính sách mặc định, Opus được điều chỉnh sau khi có kết quả thực tế và phải ghi lại thay đổi.

---

## 1. Việc phải làm trước khi áp dụng

Chưa mục nào dưới đây được xác minh.

| Việc | Cách xác minh |
|---|---|
| Tên model thực tế tài khoản dùng được | Lệnh chọn model trong Claude Code, ghi đúng tên hiển thị vào `agents/registry/`. Master Prompt chỉ ghi "Opus, Sonnet, Haiku" không kèm phiên bản. |
| Gói Claude Pro dùng thử 7 ngày có dùng được Opus trong Claude Code không, hạn mức bao nhiêu | Kiểm tra trực tiếp trong tài khoản. Nếu không có Opus, vai trò PM cần phương án khác và phải trình chủ dự án. |
| Hạn mức Codex CLI "1.000 USD" | Xác định loại hạn mức (credit, giới hạn chi tiêu, hay ước tính), điều kiện, thời hạn. Không coi là tiền chi được cho đến khi xác minh. |
| Khả năng chạy song song | Thử số phiên đồng thời thực tế của từng công cụ, ghi giới hạn tốc độ và quota. |
| Ngày hết hạn tài khoản dùng thử | Ghi vào `RISKS.md` kèm phương án thay PM. |

## 2. Phân loại trước khi giao

Opus chấm mỗi task theo: độ khó, mức rủi ro, phạm vi thay đổi, số module liên quan, yêu cầu tư duy, khả năng kiểm thử, hậu quả nếu lỗi. Lấy cấp cao nhất mà bất kỳ tiêu chí nào chạm tới.

| Cấp | Đặc điểm | Model ưu tiên | Nghiệm thu |
|---|---|---|---|
| L0 | Rất đơn giản: tóm tắt, checklist | Haiku | Kiểm tra tự động và checklist |
| L1 | Đơn giản: tài liệu, script nhỏ | Haiku / Sonnet | Kiểm tra tự động và checklist |
| L2 | Module độc lập, API, unit test | Sonnet | Model khác review hoặc test độc lập |
| L3 | Nhiều file, nhiều module, tích hợp | Sonnet, Opus review | Opus hoặc reviewer đủ năng lực kiểm tra phần quan trọng |
| L4 | Kiến trúc, concurrency, giao thức phức tạp | Opus | Opus thiết kế và nghiệm thu, có reviewer độc lập và bằng chứng test |
| L5 | Quyết định nền tảng, ảnh hưởng toàn game | Opus chủ trì | Như L4, kèm ADR; nếu chạm định hướng game thì trình chủ dự án |

## 3. Phạm vi từng model

**Opus:** quản lý dự án; kiến trúc tổng thể; quyết định kỹ thuật quan trọng; thiết kế Bot System; thiết kế Server và Network; lỗi rất phức tạp; tích hợp nhiều module; review kiến trúc; nghiệm thu milestone.

**Sonnet:** triển khai module theo thiết kế; code nghiệp vụ; API; client Axmol; server; unit test; lỗi độ phức tạp trung bình; review code thông thường; tài liệu kỹ thuật.

**Haiku:** phân loại log; tóm tắt; đối chiếu checklist; tìm tài liệu; cập nhật trạng thái; phân loại lỗi đã biết; báo cáo theo mẫu; việc lặp lại có quy trình rõ. Haiku không tự quyết thay đổi kiến trúc, không nghiệm thu hệ thống quan trọng.

**Codex CLI và AI khác:** Master Prompt chưa xếp cấp. Đề xuất của Fable: coi là worker triển khai ngang L2–L3 và là reviewer độc lập cho code do Claude viết (và ngược lại), sau khi Opus chạy thử một vài task mẫu để đo chất lượng thực tế.

## 4. Kiểm tra độc lập

Model viết code không tự nghiệm thu toàn bộ phần mình viết. "Độc lập" nghĩa là ít nhất một trong các điều sau:

- Model khác hoặc nhà cung cấp khác review.
- Bộ test do agent khác viết từ đặc tả, không nhìn phần cài đặt.
- Opus tự chạy build và test, đọc diff.

Với L4–L5 mà chính Opus thiết kế: reviewer độc lập phải là agent khác (ví dụ Codex, hoặc một phiên mới chỉ nhận đặc tả và diff, không nhận lập luận của người viết).

## 5. Nâng cấp model khi worker không hoàn thành

1. Ghi lỗi và những gì đã làm.
2. Lưu trạng thái task.
3. Đánh giá lại độ khó.
4. Chuyển sang model mạnh hơn hoặc AI khác.
5. Giữ nguyên Task ID và lịch sử.
6. Tiếp tục từ kết quả đã có.

Ngưỡng đề xuất: hai lần review trả về vì cùng một loại lỗi, hoặc worker vượt giới hạn thử ghi trong task. Opus điều chỉnh ngưỡng theo thực tế.

Hạ cấp cũng hợp lệ: việc L3 đã có thiết kế rõ có thể tách thành nhiều task L2.

## 6. Khi hết quota hoặc mất model

| Tình huống | Xử lý |
|---|---|
| Opus hết quota tạm thời | Worker tiếp tục các task L0–L2 đã giao. Task L3+ dừng ở `review`. Không model nào thay Opus nghiệm thu L4–L5. |
| Opus không còn dùng được | Theo quy trình đổi Project Manager trong Operating Rules. PM mới là ai do chủ dự án quyết. |
| Codex hết hạn mức | Chuyển task về hàng chờ, gán lại, giữ Task ID. |

## 7. Ghi nhận để hiệu chỉnh

Mỗi task hoàn thành ghi: cấp ban đầu, cấp cuối, model, số vòng review, có phải nâng cấp không. Opus xem lại định kỳ để chỉnh bảng ở mục 2.
