YÊU CẦU KHẮC PHỤC VÀ HOÀN THIỆN MASTER PROMPT – FABLE

Bạn vẫn đang đảm nhiệm vai trò Fable – Prompt Architect.

Gói bàn giao v0.1 của bạn đã được chủ dự án nhận và kiểm tra. Tuy nhiên, có một vấn đề nghiêm trọng: bạn chỉ nhận được Master Prompt bị cắt giữa mục 21. Vì vậy, 8 tài liệu bạn tạo ra chưa phản ánh đầy đủ toàn bộ yêu cầu của chủ dự án.

Yêu cầu hiện tại không phải bàn giao cho Opus ngay. Bạn phải quay lại kiểm tra toàn bộ nguồn đầu vào, đọc đầy đủ Master Prompt và hoàn thiện lại bộ tài liệu.

1. KHÔI PHỤC TOÀN BỘ MASTER PROMPT

Hãy kiểm tra toàn bộ lịch sử hội thoại hiện có với chủ dự án, bao gồm:

- Master Prompt ban đầu.
- Phần bổ sung về phân cấp model Claude.
- Quy định vai trò Fable và Opus.
- Quy định báo cáo cuối ngày.
- Các nội dung tiếp nối sau mục 21.
- Những yêu cầu bổ sung mà chủ dự án đã nêu sau khi gửi Master Prompt.

Không được chỉ đọc bản Master Prompt đã bị cắt trong lần tiếp nhận trước.

Không được tự viết phần còn thiếu bằng suy luận rồi coi đó là nội dung nguyên bản.

Nếu lịch sử hội thoại có đầy đủ nội dung, hãy khôi phục và đối chiếu.

Nếu lịch sử không còn đủ nội dung, hãy nói rõ phần nào không thể khôi phục. Không tự tuyên bố đã đọc đầy đủ.

Chủ dự án sẽ cung cấp lại phần thiếu nếu thực sự cần thiết.

2. ĐỐI CHIẾU VỚI 8 TÀI LIỆU V0.1

Bạn đã tạo 8 tài liệu:

1. "docs/00-PROJECT-MASTER.md"
2. "docs/01-PRODUCT-REQUIREMENTS.md"
3. "AI-OPERATING-RULES.md"
4. "docs/MODEL-ASSIGNMENT-POLICY.md"
5. "tasks/TASK-TEMPLATE.md"
6. "docs/PROJECT-MEMORY-STRUCTURE.md"
7. "docs/ROADMAP-DRAFT.md"
8. "project-state/HANDOVER-FABLE-TO-OPUS.md"

Hãy đọc lại toàn bộ 8 tài liệu và so sánh với Master Prompt đầy đủ.

Phải xác định:

- Nội dung nào đã được phản ánh đúng.
- Nội dung nào bị thiếu do Master Prompt bị cắt.
- Nội dung nào bạn tự đề xuất.
- Nội dung nào mâu thuẫn với yêu cầu của chủ dự án.
- Nội dung nào cần sửa.
- Nội dung nào không cần thiết và có thể đơn giản hóa.

Không giữ lại một quy định chỉ vì nó đã có trong bản v0.1.

3. ĐIỀU CHỈNH TRIẾT LÝ VẬN HÀNH: AI TỰ TRIỂN KHAI, CHỦ DỰ ÁN CHỈ XEM KẾT QUẢ

Đây là yêu cầu quan trọng nhất cần bổ sung vào toàn bộ hệ thống.

Chủ dự án không biết lập trình và không muốn phải quản lý cấu trúc kỹ thuật.

Không yêu cầu chủ dự án:

- Đọc code.
- Hiểu cấu trúc source.
- Chọn file cần sửa.
- Chọn branch.
- Tạo Git Worktree.
- Chạy lệnh PowerShell.
- Tự sửa lỗi.
- Đọc log kỹ thuật dài.
- Điều phối các AI.
- Tự tổng hợp báo cáo của worker.

Toàn bộ các việc này thuộc trách nhiệm của đội AI.

Chủ dự án chỉ cần:

1. Nêu mục tiêu.
2. Cung cấp quyền và tài nguyên.
3. Đưa ra quyết định quan trọng khi thực sự cần.
4. Xem kết quả thực tế.
5. Nhận báo cáo dễ hiểu, ngắn gọn.

AI phải tự triển khai công việc đến kết quả hoàn chỉnh trong phạm vi được giao.

Không dừng lại chỉ vì gặp lỗi thông thường.

4. ƯU TIÊN TỰ PHÁT HIỆN VÀ TỰ SỬA LỖI

Thay đổi quy trình xử lý lỗi thành:

1. Phát hiện lỗi qua build, test, runtime hoặc review.
2. Tự phân tích nguyên nhân.
3. Tự sửa lỗi.
4. Chạy lại test liên quan.
5. Kiểm tra hồi quy.
6. Nếu vẫn lỗi, thử phương án khác.
7. Nếu vượt khả năng, chuyển cho worker chuyên môn hoặc model mạnh hơn.
8. Opus chỉ tiếp nhận khi cần giải quyết xung đột, vấn đề kiến trúc hoặc lỗi khó.
9. Chỉ báo chủ dự án khi có rủi ro lớn hoặc cần quyết định thuộc quyền chủ dự án.

Không chuyển lỗi nhỏ lên Opus nếu worker có thể tự xử lý.

Không yêu cầu chủ dự án làm trung gian chuyển log giữa các AI.

Không báo lỗi là đã sửa khi chưa kiểm thử lại.

5. GIẢM BÁO CÁO VÀ TRAO ĐỔI NỘI BỘ KHÔNG CẦN THIẾT

Không biến mọi thao tác thành một vòng báo cáo thủ công.

Mục tiêu là tăng tốc độ thực thi.

Quy định:

- Worker có thể phối hợp trực tiếp khi có phụ thuộc.
- Worker có thể yêu cầu worker khác hỗ trợ trong phạm vi quyền hạn.
- Không cần Opus phê duyệt từng thao tác nhỏ.
- Không cần tạo một báo cáo Markdown riêng cho mọi thao tác.
- Không yêu cầu AI đọc lại toàn bộ nhật ký sau mỗi thay đổi.
- Không lặp lại thông tin đã có trong Git, task hoặc log.
- Tự động cập nhật trạng thái khi task thay đổi.
- Chỉ lưu báo cáo chi tiết khi có kết quả, lỗi, quyết định hoặc bàn giao quan trọng.

Opus quản lý trạng thái chung và chịu trách nhiệm cuối cùng, nhưng không được trở thành nút thắt khiến các worker phải chờ nhau.

Giữ những bằng chứng cần thiết để truy vết, review và khôi phục công việc. Đơn giản hóa thủ tục không có nghĩa bỏ kiểm thử hoặc bỏ kiểm soát chất lượng.

6. QUYỀN QUẢN TRỊ VÀ TỰ CHỦ

Chủ dự án muốn cấp quyền quản trị tối đa để AI tự làm việc.

Hãy thiết kế hệ thống theo nguyên tắc:

- Tự đọc và phân tích tài liệu.
- Tự cài đặt công cụ cần thiết.
- Tự cấu hình môi trường.
- Tự tạo và quản lý worker.
- Tự chạy lệnh.
- Tự build và test.
- Tự sửa lỗi.
- Tự quản lý Git và worktree.
- Tự tạo báo cáo.
- Tự khôi phục sau lỗi.
- Tự tiếp quản công việc khi thay AI.

Trong phạm vi máy phát triển và workspace của dự án, hãy cho Opus quyền điều hành cao nhất có thể.

Không hỏi chủ dự án cho những thao tác thông thường.

Tuy nhiên, phải phân biệt:

- Thao tác trong workspace phát triển.
- Thao tác trên server đang vận hành.
- Thao tác với dữ liệu quan trọng.
- Thao tác bảo mật.
- Thao tác gây phát sinh chi phí.
- Thao tác có thể làm mất dữ liệu không thể khôi phục.

Không được hiểu "quyền tối đa" là cho phép công khai mật khẩu, xóa dữ liệu quan trọng hoặc phá hủy môi trường mà không có khả năng khôi phục.

Các hành động không thể khôi phục phải có cơ chế bảo vệ phù hợp.

7. MỘT FILE LOCAL DUY NHẤT QUẢN LÝ BÍ MẬT

Chủ dự án muốn tất cả thông tin bí mật thống nhất tại một file trên máy local.

Hãy thiết kế một cơ chế Secret Vault tập trung.

Yêu cầu:

- Một file dữ liệu bí mật duy nhất trên máy local.
- Không đưa file này vào Git.
- Không đưa vào ZIP bàn giao.
- Không đưa vào báo cáo.
- Không ghi mật khẩu, token, API key, credential hoặc khóa bảo mật vào task.
- Không để worker không cần quyền đọc toàn bộ bí mật.
- Chỉ cấp thông tin cần thiết cho đúng công việc.
- Có quyền truy cập giới hạn.
- Có cơ chế sao lưu và khôi phục an toàn.
- Có phương án mã hóa phù hợp với Windows.
- Có hướng dẫn thay đổi và thu hồi credential.

Hãy đánh giá phương án lưu trữ thực tế, ví dụ một file mã hóa trên local được mở bằng Windows Credential Manager hoặc cơ chế bảo vệ khóa tương đương.

Không lưu mật khẩu giải mã cạnh file dữ liệu.

Không yêu cầu chủ dự án phải hiểu kỹ thuật mã hóa. Opus phải thiết kế và triển khai cơ chế phù hợp, giải thích ngắn gọn cách sử dụng.

Lưu ý: Một file duy nhất là nguồn dữ liệu bí mật tập trung, không có nghĩa tất cả worker được phép đọc toàn bộ nội dung.

8. PHÂN CẤP MODEL THEO ĐỘ KHÓ

Giữ nguyên mục tiêu sử dụng đúng model cho đúng công việc.

- Opus: quản lý, kiến trúc, quyết định khó, xử lý lỗi phức tạp, nghiệm thu.
- Sonnet: triển khai phần lớn công việc kỹ thuật.
- Haiku: công việc nhẹ, tóm tắt, phân loại, kiểm tra đơn giản.
- Codex CLI: đội ngũ thực thi và review kỹ thuật quan trọng.
- AI khác: có thể thay thế khi cần.

Phân loại task L0–L5.

Không dùng Opus cho mọi việc.

Không bắt Opus đọc và báo cáo mọi thao tác nhỏ.

Phải có cơ chế tự chuyển task sang model mạnh hơn khi gặp khó khăn và chuyển sang model khác khi hết quota.

Phải kiểm tra model nào thực sự khả dụng trong tài khoản.

9. QUY TRÌNH BÁO CÁO CHO CHỦ DỰ ÁN

Opus là người duy nhất chịu trách nhiệm báo cáo tổng hợp cho chủ dự án.

Không gửi các báo cáo kỹ thuật rời rạc từ worker.

Mỗi ngày có một báo cáo cuối ngày, mặc định 22:00 giờ Việt Nam nếu có scheduler hoạt động.

Báo cáo phải tập trung vào:

1. Hôm nay đội AI đã hoàn thành kết quả gì?
2. Game hoặc hệ thống nào đã chạy được?
3. Những lỗi nào đã phát hiện và tự sửa?
4. Những lỗi nào còn tồn tại?
5. Tiến độ chung.
6. Ngày tiếp theo sẽ làm gì?
7. Có vấn đề gì thực sự cần chủ dự án quyết định?

Không bắt chủ dự án đọc log, commit, diff hay báo cáo kỹ thuật dài.

Có thể đính kèm liên kết tới tài liệu kỹ thuật để tham khảo, nhưng phần chính phải dễ hiểu với người không biết lập trình.

Nếu có số liệu, phải là số liệu thực tế.

Không báo hoàn thành nếu chưa chạy thử.

Nếu có sự cố nghiêm trọng, báo ngay, không chờ cuối ngày.

10. BÀN GIAO VÀ THAY THẾ AI

Bất kỳ model hoặc tài khoản nào cũng có thể bị thay thế.

AI mới phải tự đọc bộ nhớ dự án và tiếp tục công việc.

Không yêu cầu chủ dự án giải thích lại.

Không phụ thuộc vào lịch sử chat.

Không phụ thuộc vào memory riêng của Claude hoặc Codex.

Tất cả kiến thức quan trọng phải có định dạng trung lập, đọc được bởi nhiều AI.

Giữ Task ID, trạng thái, kết quả, file đã sửa, test, lỗi và bước tiếp theo.

Nếu AI cũ mất kết nối, AI mới phải khôi phục được trạng thái.

Không bắt buộc tạo báo cáo bàn giao dài cho mỗi lần đổi worker. Chỉ cần trạng thái và bằng chứng đủ để AI mới tiếp tục.

11. KHÔNG THAY ĐỔI ĐỊNH HƯỚNG GAME

Giữ nguyên các nguyên tắc đã được chủ dự án xác nhận:

- Game được xây dựng hoàn toàn tự chủ.
- Client và server JX1 gốc chỉ là tài liệu tham khảo.
- Chưa chuyển sang Unity.
- Client mục tiêu là Axmol.
- Server mới được thiết kế độc lập.
- Bot là thành phần trung tâm.
- Bot được quản lý chung trong thế giới game.
- Người chơi thật chỉ nhìn thấy nhau trong những hoạt động có giới hạn.
- Không biến game thành MMORPG thông thường.

Không tự quyết định những điểm gameplay còn bỏ ngỏ.

12. ĐẦU RA CỦA FABLE

Sau khi khôi phục và đọc đủ Master Prompt, hãy cập nhật toàn bộ 8 tài liệu.

Có thể bổ sung tài liệu nếu thực sự cần, nhưng tránh tạo nhiều file trùng lặp.

Tạo một báo cáo:

"FABLE-MASTER-PROMPT-COMPLETENESS-REPORT.md"

Báo cáo phải cho biết:

- Bạn đã đọc được toàn bộ Master Prompt chưa?
- Master Prompt có bao nhiêu mục?
- Đã khôi phục được phần nào sau mục 21?
- Có phần nào không thể khôi phục?
- Những yêu cầu nào bị thiếu trong v0.1?
- Những tài liệu nào đã được cập nhật?
- Những quy định nào đã được đơn giản hóa?
- Cơ chế tự sửa lỗi đã được bổ sung ra sao?
- Cơ chế Secret Vault được thiết kế thế nào?
- Quyền hạn Opus đã được phân định ra sao?
- Báo cáo cuối ngày được thiết kế thế nào?

Đặt phiên bản mới là v0.2.

Không xóa bản v0.1. Lưu lại để có lịch sử đối chiếu.

13. GIAI ĐOẠN NÀY CHƯA BÀN GIAO CHO OPUS

Chưa gửi gói bàn giao cho Opus triển khai.

Chưa sửa source.
Chưa sửa server.
Chưa cài plugin.
Chưa tạo worker viết code.

Trước tiên hoàn thành việc đọc đầy đủ Master Prompt và cập nhật tài liệu.

Sau đó gửi chủ dự án một báo cáo tổng hợp dễ hiểu, nêu rõ:

- Đã đọc đầy đủ hay chưa.
- Những gì đã sửa.
- Những gì còn thiếu.
- Gói bàn giao mới đã sẵn sàng hay chưa.

Ưu tiên số một: Đọc đủ yêu cầu của chủ dự án. Ưu tiên số hai: Thiết kế đội AI tự triển khai và tự sửa lỗi. Ưu tiên số ba: Giảm tối đa công việc kỹ thuật và báo cáo nội bộ không cần thiết cho chủ dự án.