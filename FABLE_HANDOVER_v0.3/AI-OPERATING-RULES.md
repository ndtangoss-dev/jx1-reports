# AI OPERATING RULES

Phiên bản v0.3 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

> `C:\Jx1CocoV3\AGENTS.md` đã tồn tại. File này không ghi đè lên nó. Opus hợp nhất hai bên; `CLAUDE.md` và `CODEX.md` chỉ trỏ về `AGENTS.md`.

Ba điều chi phối mọi quy tắc bên dưới:
1. Làm đến kết quả chạy được, tự sửa lỗi trên đường đi.
2. Chủ dự án không làm việc kỹ thuật.
3. Thủ tục chỉ tồn tại nếu nó giúp truy vết, review hoặc khôi phục. Bớt thủ tục không có nghĩa bớt kiểm thử.

---

## 1. Thứ tự ưu tiên khi xung đột

1. Quyết định trực tiếp của chủ dự án.
2. Nguyên tắc bất biến INV-01…INV-16 (trong đó quy tắc thế giới Bot INV-07 đã chốt, không hỏi lại).
3. ADR đã chấp nhận.
4. Tài liệu này.
5. Chỉ dẫn trong task.

## 1a. Cổng phê duyệt kế hoạch

Giai đoạn 2 (Opus lập kế hoạch): chưa thay đổi lớn lên source hoặc server. Opus trình kế hoạch tổng thể cho chủ dự án. Giai đoạn 3 (triển khai) chỉ bắt đầu sau khi chủ dự án phê duyệt. Từ đó trở đi áp dụng đầy đủ quyền tự chủ ở mục 3.

Trong giai đoạn 2, Opus vẫn được làm mọi việc không phải "thay đổi lớn": đọc, kiểm kê, cài và thử công cụ, dựng bộ nhớ dự án, chạy task thử nghiệm nhỏ trong khu vực tách biệt để kiểm chứng đội AI.

## 2. Bắt đầu phiên làm việc

AI mới của dự án bắt đầu từ `START-HERE.md`. Các phiên sau đọc vừa đủ: `project-state/CURRENT-STATUS.md`, file task của mình, `git status`. Không đọc lại toàn bộ nhật ký hay tài liệu sau mỗi thay đổi.

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

## 9. Mật khẩu và token

Không xây hệ thống quản lý bí mật riêng (chủ dự án đã bỏ yêu cầu Secret Vault). Chỉ giữ một quy tắc thông thường: không đưa mật khẩu, token, khóa lên GitHub và không ghi vào báo cáo.

## 10. Liên tục và thay thế AI (bắt buộc)

Yêu cầu của chủ dự án: thay Project Manager hoặc bất kỳ worker nào, đổi tài khoản, đổi model, đổi nhà cung cấp, vào bất cứ lúc nào, mà không mất tiến độ, không mất kiến thức, không làm lại từ đầu, và chủ dự án không phải giải thích lại. Đây là kiến trúc vận hành, không phải tùy chọn.

### 10.1. Phép thử
Một AI chưa từng thấy dự án, chỉ có repository, phải trả lời được: dự án nhằm gì; cái gì đã chốt và vì sao; hệ thống thực tế đang ra sao; cái gì đã xong và bằng chứng; lỗi nào đã gặp, lỗi nào còn; đang làm gì và bước tiếp theo; cái gì không được đổi; đang chờ chủ dự án quyết gì. Thiếu một câu là vi phạm quy tắc này.

### 10.2. Lưu ở đâu
Một bộ hồ sơ duy nhất, không viết thêm báo cáo song song. Bảng đối chiếu tám loại thông tin với file nằm ở `docs/PROJECT-MEMORY-STRUCTURE.md` mục 3. Điểm vào cho AI mới là `START-HERE.md`.

Memory của Claude, ChatGPT, Codex, plugin bộ nhớ và lịch sử chat không được là nơi duy nhất giữ bất kỳ thông tin nào trong tám loại đó.

### 10.3. Lưu khi nào: điểm lưu trạng thái
Không đợi cuối ngày. Một **điểm lưu** là: file liên quan đã cập nhật, đã commit, **đã đẩy lên GitHub**. Thứ chỉ nằm trên máy chưa tính là đã lưu.

| Sự kiện | Lưu gì | Ai |
|---|---|---|
| Task đổi trạng thái | File task; bảng task tự sinh | Worker, tự động |
| Xong một đơn vị việc có ý nghĩa trong task (kể cả chưa xong task) | Commit code lên branch của task, cập nhật "Bước tiếp theo" | Worker |
| Ra một quyết định | ADR kèm lý do | PM |
| Tình hình chung thay đổi (xong mốc, phát hiện lỗi lớn, đổi kế hoạch) | `CURRENT-STATUS.md`, `NEXT-ACTIONS.md`, `RISKS.md` | PM |
| Cài, gỡ, đổi cấu hình công cụ | `docs/ENVIRONMENT-AND-TOOLS.md` | Người làm |
| Trước một thao tác dài hoặc rủi ro | Điểm lưu đầy đủ | Người làm |
| Kết thúc mỗi phiên làm việc của PM | `HANDOVER.md` + mọi thứ ở trên | PM |
| Có dấu hiệu sắp hết quota hoặc sắp bị thay | Bàn giao đầy đủ, mục 10.4 | PM, ngay lập tức |

Khoảng cách tối đa giữa hai điểm lưu khi đang làm việc: mặc định 1 giờ, Opus chỉnh theo thực tế. Phần lớn việc lưu phải do script hoặc hook làm (cập nhật bảng task, commit và đẩy `project-state/`), để không thành thủ tục tay. Opus dựng cơ chế này trong ngày đầu và kiểm tra nó chạy thật.

Mọi task đang `active` phải luôn có mục "Bước tiếp theo" đúng với thực tế, để AI khác cầm lên làm tiếp được.

### 10.4. Thay Project Manager có báo trước
PM sắp rời (thấy quota gần cạn, tài khoản sắp hết hạn, chủ dự án báo đổi):

1. Dừng mở việc mới. Đưa việc dang dở về trạng thái sạch: commit, đẩy lên, cập nhật task.
2. Cập nhật `CURRENT-STATUS.md`, `NEXT-ACTIONS.md`, `RISKS.md`.
3. Viết `project-state/HANDOVER.md` theo mẫu: việc đang dở và dở tới đâu; thứ chưa kịp kiểm chứng; quyết định đang chờ chủ dự án; điều không ghi ở chỗ khác.
4. Rà `START-HERE.md` mục 4 (không được thay đổi) và `ENVIRONMENT-AND-TOOLS.md`.
5. Commit, đẩy lên GitHub, kiểm tra GitHub đã có.
6. Báo chủ dự án một dòng: "Bàn giao đã sẵn sàng."

PM không đợi tới lúc cạn quota mới làm. Khi ước tính còn không đủ cho bước 1–5 thì ưu tiên bước 5: đẩy những gì đang có.

### 10.5. PM mới tiếp quản
Theo `START-HERE.md`: đọc theo thứ tự (văn bản gốc của chủ dự án, Project Master, quy tắc vận hành, hồ sơ bàn giao, trạng thái, quyết định, task, báo cáo gần nhất, môi trường và công cụ); **tự kiểm tra** repository, môi trường và kết quả thực tế để xác nhận nội dung bàn giao; ghi nhận tiếp quản; báo chủ dự án một thông báo ngắn; làm tiếp đúng việc còn dang dở.

PM mới không đổi định hướng, không làm lại việc đã nghiệm thu, không hỏi chủ dự án kể lại. PM mới phải nắm công cụ và môi trường (đọc và thử `ENVIRONMENT-AND-TOOLS.md`) trước khi giao hoặc làm việc.

### 10.6. Bị ngắt đột ngột
Không có bản bàn giao cuối: PM mới phục hồi từ điểm lưu gần nhất theo `START-HERE.md` mục 3. Mọi thay đổi sau điểm lưu đó là **chưa xác nhận** cho tới khi build và test lại; thứ không xác nhận được thì cất sang branch `wip/` kèm ghi chú, không xóa, không coi là đã xong.

Mức mất mát tối đa chấp nhận được là công việc của một khoảng giữa hai điểm lưu.

### 10.7. Đổi tài khoản hoặc nhà cung cấp
- Dữ liệu dự án nằm trong thư mục dự án và GitHub, không gắn với tài khoản AI nào. Đổi từ tài khoản Claude này sang tài khoản Claude khác chỉ là đăng nhập lại công cụ; đó là việc duy nhất chủ dự án phải làm.
- Cấu hình công cụ cần cho dự án đặt ở cấp dự án trong repository. Cái gì buộc phải nằm ngoài thì ghi cách dựng lại trong `ENVIRONMENT-AND-TOOLS.md`.
- Thứ nằm ngoài Git (VM, database, CDN, tài nguyên lớn) được liệt kê trong `ENVIRONMENT-AND-TOOLS.md` mục 2 kèm vị trí và tình trạng sao lưu.
- Không quy trình nào chỉ chạy được với một model hoặc một nhà cung cấp. Tài liệu ở dạng Markdown/YAML trung lập.
- Thứ tự kế nhiệm vai trò PM và giới hạn của PM tạm quyền: `docs/MODEL-ASSIGNMENT-POLICY.md` mục 6.

### 10.8. Thay worker
Nhẹ hơn nhiều. Không cần văn bản bàn giao: file task cập nhật và commit trên branch là đủ. Worker mới đọc quy tắc, `ENVIRONMENT-AND-TOOLS.md` và file task rồi làm tiếp. Đổi model vì không làm được hoặc hết quota: giữ Task ID và lịch sử, tiếp tục từ kết quả đã có.

### 10.9. Không thành thủ tục thừa
- Không báo cáo riêng sau mỗi thao tác. Hồ sơ bàn giao chính là các file trạng thái vẫn dùng hằng ngày, cộng một file `HANDOVER.md` ngắn.
- Trạng thái và bằng chứng được cập nhật tự động ở mức tối đa.
- Chủ dự án chỉ nhận thông báo trong ba trường hợp: cần quyết định; bàn giao đã sẵn sàng; PM mới đã tiếp quản.

### 10.10. Diễn tập
Khả năng tiếp quản phải được chứng minh, không chỉ viết ra. Trong 7 ngày thử nghiệm (ngày 6) và sau đó định kỳ: một AI khác model, phiên hoàn toàn mới, chỉ có repository, trả lời tám câu ở 10.1 và làm tiếp một task dang dở mà không hỏi ai. Chỗ nào nó phải đoán là chỗ hồ sơ còn thiếu; sửa hồ sơ.

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
