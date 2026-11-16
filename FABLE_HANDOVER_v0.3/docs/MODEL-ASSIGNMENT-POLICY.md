# MODEL ASSIGNMENT POLICY

Phiên bản v0.3 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

Mục tiêu: đúng model cho đúng việc, tiết kiệm quota mà không giảm chất lượng, và không để Opus thành nút thắt. Chính sách mặc định; Opus điều chỉnh theo kết quả thực tế.

---

## 1. Xác minh trước khi áp dụng (Opus tự làm, không hỏi chủ dự án)

| Việc | Ghi kết quả vào |
|---|---|
| Model nào thực sự dùng được trong tài khoản, tên chính xác | `agents/registry/` |
| Gói Claude Pro dùng thử 7 ngày có Opus trong Claude Code không, hạn mức, ngày hết hạn | `agents/registry/`, `RISKS.md` |
| Hạn mức Codex CLI "1.000 USD" là loại gì, điều kiện, thời hạn | như trên |
| Số phiên chạy song song thực tế, giới hạn tốc độ | như trên |

Nếu kết quả làm thay đổi kế hoạch (ví dụ không có Opus), đó là sự cố báo ngay cho chủ dự án kèm phương án.

## 2. Vai trò từng model

| Model | Vai trò |
|---|---|
| **Opus** | Quản lý, kiến trúc, quyết định khó, lỗi phức tạp, nghiệm thu. Không làm việc đơn giản, không đọc và báo cáo mọi thao tác nhỏ. |
| **Sonnet** | Triển khai phần lớn công việc kỹ thuật: module, API, client Axmol, server, unit test, lỗi trung bình, review thông thường, tài liệu kỹ thuật. |
| **Haiku** | Việc nhẹ: tóm tắt, phân loại log và lỗi đã biết, đối chiếu checklist, tìm tài liệu, soạn nháp báo cáo theo mẫu. Không quyết kiến trúc, không nghiệm thu hệ thống quan trọng. |
| **Codex CLI** | Đội thực thi và review kỹ thuật quan trọng. Nhận task triển khai L2–L4 và là reviewer độc lập cho code do Claude viết (Claude review lại code của Codex). |
| **AI khác** | Thay thế khi cần. Trước khi nhận việc thật, chạy vài task mẫu để đo chất lượng. |

## 3. Phân loại độ khó

Chấm theo: độ khó, rủi ro, phạm vi thay đổi, số module liên quan, yêu cầu tư duy, khả năng kiểm thử, hậu quả nếu lỗi. Lấy cấp cao nhất mà một tiêu chí chạm tới.

| Cấp | Đặc điểm | Thực hiện | Kiểm tra độc lập | Ai cho qua |
|---|---|---|---|---|
| L0 | Tóm tắt, checklist | Haiku | Kiểm tra tự động | Tự động |
| L1 | Tài liệu, script nhỏ | Haiku / Sonnet | Kiểm tra tự động, checklist | Tự động |
| L2 | Module độc lập, API, unit test | Sonnet / Codex | Model khác review hoặc test độc lập | Reviewer + CI, không cần Opus |
| L3 | Nhiều file, nhiều module, tích hợp | Sonnet / Codex | Reviewer khác nhà cung cấp | Opus xem phần quan trọng |
| L4 | Kiến trúc, concurrency, giao thức phức tạp | Opus thiết kế; Opus hoặc Codex triển khai | Reviewer độc lập + bằng chứng test | Opus |
| L5 | Quyết định nền tảng toàn game | Opus chủ trì | Như L4, kèm ADR | Opus; chạm định hướng game thì chủ dự án |

Ai phân loại: Opus khi tạo task. Worker thấy task bị chấm thấp hơn thực tế thì tự nâng cấp và ghi lý do, không chờ.

## 4. Kiểm tra độc lập

Người viết không tự nghiệm thu. "Độc lập" là ít nhất một trong: model hoặc nhà cung cấp khác review; test do agent khác viết từ đặc tả; Opus tự chạy build, test và đọc diff.

Với L4–L5 do Opus thiết kế: reviewer là agent khác (ưu tiên Codex), chỉ nhận đặc tả và diff, không nhận lập luận của Opus.

## 5. Tự nâng cấp khi gặp khó

Tự động, không cần Opus duyệt:

1. Worker hết phương án theo thang tự sửa lỗi (mặc định 3 lần thất bại hoặc không tiến triển).
2. Ghi vào task: lỗi, đã thử gì, trạng thái hiện tại.
3. Task chuyển lên bậc kế tiếp: Haiku → Sonnet → Codex hoặc Sonnet phiên khác với hướng tiếp cận khác → Opus.
4. Giữ Task ID và lịch sử. Agent mới tiếp tục từ kết quả đã có.

Opus chỉ nhận ở bậc cuối, hoặc sớm hơn nếu nguyên nhân là kiến trúc hay xung đột giữa worker.

Hạ cấp cũng hợp lệ: việc L3 đã có thiết kế rõ được tách thành nhiều task L2.

## 6. Tự chuyển khi hết quota

| Tình huống | Xử lý tự động |
|---|---|
| Một worker hết quota | Task trở về hàng chờ với trạng thái hiện tại, giao cho model cùng bậc ở nhà cung cấp khác (Sonnet ↔ Codex). |
| Sonnet và Haiku hết | Codex nhận phần triển khai; việc L0–L1 gom lại chờ. |
| Codex hết | Sonnet nhận triển khai; review chéo tạm dùng phiên Claude khác và đánh dấu "review cùng nhà cung cấp" để Codex xem lại sau. |
| Opus hết tạm thời (vài giờ) | Worker tiếp tục mọi việc L0–L2 và phần triển khai L3. Việc cần PM xếp hàng ở `review`. |
| PM không còn dùng được, hoặc chủ dự án đổi tài khoản | Kế nhiệm theo bảng dưới và `AI-OPERATING-RULES.md` mục 10. |

**Thứ tự kế nhiệm vai trò Project Manager**

| Ưu tiên | Ai | Ghi chú |
|---|---|---|
| 1 | Opus trên tài khoản Claude khác của chủ dự án | Đầy đủ quyền PM |
| 2 | Opus khác (phiên, gói hoặc nhà cung cấp truy cập khác) | Đầy đủ quyền PM |
| 3 | Sonnet | PM tạm quyền |
| 4 | Codex | PM tạm quyền |
| 5 | AI khác | PM tạm quyền, sau khi chạy thử |

Ai tiếp quản là do chủ dự án đăng nhập công cụ nào; bảng này là thứ tự nên chọn khi có nhiều lựa chọn. Dự án không được dừng vì thiếu Opus.

**PM tạm quyền** làm đủ việc điều hành: giao việc, theo dõi, tích hợp, giữ trạng thái, báo cáo cuối ngày, tiếp tục kế hoạch đã duyệt. Giới hạn: với quyết định L4–L5 mới (kiến trúc, nền tảng), PM tạm quyền phải có reviewer độc lập từ nhà cung cấp khác đồng ý, ghi ADR có nhãn "quyết định dưới PM tạm quyền", và nêu trong báo cáo ngày để Opus kế tiếp xem lại. Quyết định chạm định hướng game vẫn thuộc chủ dự án như mọi khi.

Bảng dự phòng chỉ có nghĩa sau khi mục 1 xác minh những model nào thật sự có. OmniRoute hoặc công cụ tương đương có thể tự động hóa việc chuyển tuyến nếu Opus đánh giá là đáng dùng.

## 7. Hiệu chỉnh

Thu tự động từ dữ liệu task: cấp ban đầu, cấp cuối, model, số vòng review, có nâng cấp không. Opus xem lại khi kết thúc mỗi milestone để chỉnh bảng mục 3.
