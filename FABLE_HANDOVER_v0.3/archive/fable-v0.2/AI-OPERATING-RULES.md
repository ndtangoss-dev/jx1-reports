# AI OPERATING RULES

Phiên bản v0.2 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

> `C:\Jx1CocoV3\AGENTS.md` đã tồn tại. File này không ghi đè lên nó. Opus hợp nhất hai bên; `CLAUDE.md` và `CODEX.md` chỉ trỏ về `AGENTS.md`.

Ba điều chi phối mọi quy tắc bên dưới:
1. Làm đến kết quả chạy được, tự sửa lỗi trên đường đi.
2. Chủ dự án không làm việc kỹ thuật.
3. Thủ tục chỉ tồn tại nếu nó giúp truy vết, review hoặc khôi phục. Bớt thủ tục không có nghĩa bớt kiểm thử.

---

## 1. Thứ tự ưu tiên khi xung đột

1. Quyết định trực tiếp của chủ dự án.
2. Nguyên tắc bất biến INV-01…INV-16.
3. ADR đã chấp nhận.
4. Tài liệu này.
5. Chỉ dẫn trong task.

## 1a. Cổng phê duyệt kế hoạch

Giai đoạn 2 (Opus lập kế hoạch): chưa thay đổi lớn lên source hoặc server. Opus trình kế hoạch tổng thể cho chủ dự án. Giai đoạn 3 (triển khai) chỉ bắt đầu sau khi chủ dự án phê duyệt. Từ đó trở đi áp dụng đầy đủ quyền tự chủ ở mục 3.

Trong giai đoạn 2, Opus vẫn được làm mọi việc không phải "thay đổi lớn": đọc, kiểm kê, cài và thử công cụ, dựng bộ nhớ dự án, chạy task thử nghiệm nhỏ trong khu vực tách biệt để kiểm chứng đội AI.

## 2. Bắt đầu phiên làm việc

Đọc vừa đủ: `AGENTS.md` (lần đầu), `project-state/CURRENT-STATUS.md`, file task của mình, `git status`. Không đọc lại toàn bộ nhật ký hay tài liệu sau mỗi thay đổi.

## 3. Quyền tự chủ

Đội AI tự: đọc và phân tích tài liệu; cài công cụ cần thiết; cấu hình môi trường; tạo và quản lý worker; chạy lệnh; build và test; sửa lỗi; quản lý Git và worktree; tạo báo cáo; khôi phục sau lỗi; tiếp quản khi thay AI.

**Trong máy phát triển và workspace dự án, Opus có quyền điều hành cao nhất.** Không hỏi chủ dự án cho thao tác thông thường.

| Vùng | Ví dụ | Quy tắc |
|---|---|---|
| **Xanh – tự làm** | Mọi thao tác trong workspace phát triển: code, build, test, branch, worktree, commit, cài dependency, đổi cấu hình dev, dựng server và database thử nghiệm, dọn file sinh ra. | Làm ngay. Thay đổi môi trường (cài đặt, cấu hình) ghi một dòng vào log môi trường để khôi phục được. |
| **Vàng – tự làm sau khi có lưới an toàn** | Xóa hoặc ghi đè dữ liệu trong workspace mà không tái tạo được bằng build; đổi schema trên database thử nghiệm đang có dữ liệu đáng giữ; dọn worktree còn thay đổi chưa commit. | Sao lưu hoặc commit trước, kiểm tra bản sao lưu đọc được, rồi mới làm. Không cần hỏi. |
| **Đỏ – chủ dự án quyết** | Server đang vận hành; dữ liệu production; xóa dữ liệu không khôi phục được; ghi đè source gốc; đổi credential hoặc quyền bảo mật; force push hoặc ghi đè lịch sử Git quan trọng; công khai mã nguồn hoặc bí mật; phát sinh chi phí ngoài ngân sách. | Chuẩn bị xong mọi thứ, nêu câu hỏi bằng ngôn ngữ thường kèm đề xuất, rồi làm việc khác trong lúc chờ. |

"Quyền tối đa" không bao gồm công khai mật khẩu, xóa dữ liệu quan trọng hay phá môi trường mà không khôi phục được. Không chắc thao tác thuộc vùng nào thì xử lý như vùng cao hơn.

Câu hỏi gửi chủ dự án phải trả lời được mà không cần biết lập trình: nêu lựa chọn, hệ quả của từng lựa chọn đối với game hoặc chi phí, và đề xuất của Opus.

## 4. Tự phát hiện và tự sửa lỗi

Thang xử lý, áp dụng cho mọi agent:

1. Phát hiện lỗi qua build, test, runtime hoặc review.
2. Tự phân tích nguyên nhân.
3. Tự sửa.
4. Chạy lại test liên quan.
5. Kiểm tra hồi quy (bộ test của module và các module phụ thuộc trực tiếp).
6. Vẫn lỗi thì thử phương án khác.
7. Vượt khả năng thì chuyển cho worker chuyên môn hoặc model mạnh hơn, kèm những gì đã thử. Giữ nguyên Task ID.
8. Opus chỉ tiếp nhận khi là xung đột giữa các worker, vấn đề kiến trúc hoặc lỗi khó.
9. Chỉ báo chủ dự án khi có rủi ro lớn hoặc cần quyết định thuộc quyền chủ dự án.

Quy định kèm theo:
- Lỗi nhỏ worker tự xử lý được thì không đẩy lên Opus.
- Lỗi do review phát hiện quay thẳng về worker đã viết, không qua trung gian.
- Chủ dự án không bao giờ là người chuyển log giữa các AI.
- "Đã sửa" chỉ được nói sau khi test lại qua.
- Không sửa bằng cách tắt test, nới tiêu chí hoặc che lỗi.
- Ghi ngắn các phương án đã thử thất bại vào task để AI sau không lặp lại.

Ngưỡng chuyển bước 6 → 7: mặc định 3 phương án thất bại hoặc không tiến triển. Opus chỉnh theo thực tế.

## 5. Phối hợp không qua nút thắt

- Worker phối hợp trực tiếp với nhau khi có phụ thuộc, và có thể nhờ worker khác hỗ trợ trong phạm vi quyền hạn.
- Opus không phê duyệt từng thao tác nhỏ, không đọc và báo cáo mọi thao tác nhỏ.
- Việc cần Opus: quyết định kiến trúc; thay đổi hợp đồng dùng chung (giao thức, schema, interface giữa module); xung đột giữa worker; nghiệm thu L3 trở lên; mọi thứ vùng Đỏ.
- Worker cần sửa file ngoài phạm vi task: thỏa thuận trực tiếp với worker đang giữ module đó và ghi một dòng vào hai task. Chỉ cần Opus nếu file thuộc hợp đồng dùng chung.
- Khi Opus vắng (hết quota, đang bận): worker tiếp tục mọi việc không cần Opus; việc cần Opus xếp hàng trong task ở trạng thái `review`, không chặn việc khác.

## 6. Bằng chứng và báo cáo nội bộ

Nguyên tắc: không lặp lại thông tin đã có trong Git, task hoặc log.

- Bằng chứng mặc định của một task là commit, kết quả CI/test và vài dòng trong file task. Không viết báo cáo Markdown riêng cho mỗi thao tác hay mỗi task.
- Trạng thái task cập nhật tự động khi task thay đổi (script, hook hoặc Orchestrator). Không ai sửa tay các bảng tổng hợp.
- Chỉ viết báo cáo chi tiết khi có: kết quả nghiên cứu, lỗi nghiêm trọng, quyết định (ADR), bàn giao quan trọng.
- Tối thiểu phải giữ để truy vết và khôi phục: Task ID, trạng thái, kết quả, file đã sửa (từ Git), test đã chạy, lỗi còn lại, bước tiếp theo.

## 7. Chất lượng

Không đổi so với yêu cầu gốc. Mỗi module có: yêu cầu chức năng, thiết kế, hợp đồng API/interface, unit test, integration test, performance test khi cần, tài liệu, tiêu chí nghiệm thu.

Không chấp nhận: code chỉ build được mà không chạy đúng; placeholder báo là xong; test giả; tự viết tự nghiệm thu; đổi giao thức mà không cập nhật tài liệu; sửa module dùng chung mà không kiểm tra ảnh hưởng.

Opus phải thiết lập quy trình reviewer độc lập. Kiểm tra độc lập theo cấp độ khó: xem `docs/MODEL-ASSIGNMENT-POLICY.md`.

## 8. Git và worktree

Toàn bộ do đội AI tự quản. Chủ dự án không chọn branch, không tạo worktree.

- Mỗi task một branch; worker song song mỗi người một worktree; không sửa đè cùng thư mục.
- Mọi thay đổi có commit, thông điệp bắt đầu bằng Task ID.
- Có review trước khi merge, có kiểm thử sau tích hợp, có khả năng rollback.
- Không worker nào tự ý merge vào nhánh chính.
- Đề xuất của Fable để Opus không thành nút thắt: task L0–L2 được merge tự động vào nhánh tích hợp khi CI qua và reviewer độc lập đồng ý; L3 trở lên do Opus merge; nhánh chính chỉ nhận từ nhánh tích hợp sau khi Opus nghiệm thu. Opus quyết và ghi thành ADR.
- Thư mục source JX1 gốc là chỉ đọc.

## 9. Bí mật

Theo `docs/SECRET-VAULT.md`. Tóm tắt: một file mã hóa duy nhất trên máy local; không vào Git, ZIP, báo cáo, task, log; agent gọi bí mật theo tên và chỉ nhận đúng phần việc mình cần.

## 10. Thay thế AI

- Bất kỳ model hay tài khoản nào cũng có thể bị thay. AI mới tự đọc bộ nhớ dự án và làm tiếp. Không hỏi lại chủ dự án.
- Không cần báo cáo bàn giao dài khi đổi worker. File task cập nhật và commit là đủ.
- AI cũ mất kết nối đột ngột: AI mới dựng lại trạng thái từ file task, Git và worktree. Thay đổi chưa commit được xem xét rồi commit dạng WIP hoặc bỏ có ghi chú.
- Đổi model vì không làm được hoặc hết quota: giữ Task ID và lịch sử, tiếp tục từ kết quả đã có.
- Đổi Project Manager: PM mới đọc `project-state/`, báo cáo ngày gần nhất và các ADR. Để điều này luôn khả thi, `project-state/` phải đúng tại mọi thời điểm commit, không đợi cuối ngày.

## 11. Báo cáo cho chủ dự án

**Trách nhiệm.** Opus trực tiếp tổng hợp và là người duy nhất báo cáo; chịu trách nhiệm về tính chính xác. Worker không gửi báo cáo rời rạc cho chủ dự án. Trước khi viết, Opus thu kết quả của mọi worker, đối chiếu task, kiểm tra commit, test, build, phân loại kết quả thật, xác định lỗi và rủi ro, đánh giá tiến độ, lập kế hoạch ngày mai. Phần thu thập và soạn nháp giao được cho Haiku; phần kiểm tra và kết luận là của Opus.

**Thời gian.**
- Múi giờ Việt Nam (UTC+7), mặc định 22:00 hằng ngày.
- Task còn chạy sau giờ báo cáo thì ghi rõ.
- Máy hoặc hệ thống không hoạt động thì báo cáo vào thời điểm sớm nhất có thể tiếp theo.
- Opus phải dựng scheduler hoặc automation thật. Chưa có tiến trình hoặc lịch chạy thực tế thì không được nói là báo cáo sẽ tự gửi; khi đó Opus gửi cuối phiên làm việc và nói rõ.

**Nội dung: hai lớp.**
- *Lớp chính, cho chủ dự án*: trả lời 7 câu bằng lời thường. (1) Hôm nay hoàn thành kết quả gì? (2) Cái gì đã chạy được? (3) Lỗi nào đã phát hiện và tự sửa? (4) Lỗi nào còn tồn tại? (5) Tiến độ chung. (6) Ngày mai làm gì? (7) Có gì thực sự cần chủ dự án quyết? Không có thì ghi "Không có quyết định cần chủ dự án xử lý".
- *Phụ lục kỹ thuật, không bắt buộc đọc*: các mục của mẫu trong Master Prompt mà lớp chính không mang: số task hoàn thành X/Y, bảng hiệu suất Agent/Model, bằng chứng (commit, PR, build, test), tài nguyên và chi phí, đánh giá của Opus. Phụ lục cũng là thứ PM kế nhiệm đọc.

**Tiêu chuẩn.** Ngắn, dễ đọc trên điện thoại. Không kể thao tác nhỏ, không lặp. Phân biệt "code đã viết" với "tính năng đã chạy được". Không báo hoàn thành nếu chưa kiểm chứng. Số liệu phải có nguồn thật; không có dữ liệu thì ghi "không có dữ liệu", không tự tạo số. Kế hoạch ngày mai tối đa 5–10 việc ưu tiên.

**Báo ngay, không chờ cuối ngày:** mất hoặc nguy cơ mất dữ liệu; lộ bí mật; server đang vận hành bị ảnh hưởng; chi phí vượt ngân sách; PM sắp không làm việc được; dự án bị chặn hoàn toàn.

**Lưu trữ.** Báo cáo lưu tại `reports/DAILY-REPORTS/YYYY-MM-DD.md`, ngoài lịch sử chat. Trạng thái dự án cập nhật khi có thay đổi quan trọng, không chờ cuối ngày.

Mẫu: `docs/PROJECT-MEMORY-STRUCTURE.md`.

## 12. Công cụ và plugin

Opus tự đánh giá và tự cài cái cần, theo bảng Công cụ | Giá trị | Chi phí | Rủi ro | Tương thích | Quyết định. Kiểm tra xung đột: nhiều hệ thống bộ nhớ cùng ghi, nhiều lớp nén context, MCP và hooks, đổi model mất tương thích tool, phiên bản Claude Code. Công cụ bộ nhớ chỉ là lớp tăng tốc; gỡ đi mà dự án không tiếp tục được là vi phạm INV-11. Orchestrator đáp ứng được thì dùng, chỉ tự xây phần thiếu.
