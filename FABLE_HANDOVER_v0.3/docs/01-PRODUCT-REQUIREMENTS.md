# 01 – PRODUCT REQUIREMENTS

Phiên bản v0.3 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao. Thay đổi so với v0.2: chốt quy tắc thế giới Bot (mục B), bỏ câu hỏi Q-02, bỏ yêu cầu Secret Vault.

Cột **Nguồn**: `OWNER` = chủ dự án yêu cầu trực tiếp; `AD` = lấy từ bài quảng cáo bán source, là mục tiêu tham chiếu, chưa xác minh khả thi.
Cột **Trạng thái**: `Chốt` = không đổi nếu chủ dự án không đồng ý; `Cần xác minh` = Opus kiểm tra khả thi trước khi chốt kiến trúc; `Cần chủ dự án quyết` = xem câu hỏi mở.

---

## A. Nền tảng và công nghệ

| ID | Yêu cầu | Nguồn | Trạng thái |
|---|---|---|---|
| PR-PLAT-01 | Client viết bằng Axmol. | OWNER | Chốt |
| PR-PLAT-02 | Không dùng Unity ở giai đoạn này. | OWNER | Chốt |
| PR-PLAT-03 | Client chạy trên Android. | AD | Cần xác minh |
| PR-PLAT-04 | Client chạy trên iOS. | AD | Cần xác minh (cần máy Mac và tài khoản Apple Developer) |
| PR-PLAT-05 | Client Windows dạng EXE. | AD | Cần xác minh |
| PR-PLAT-06 | Server x64, kiến trúc riêng. | OWNER + AD | Chốt hướng, thiết kế do Opus |
| PR-PLAT-07 | Biên dịch bằng Visual Studio 2026. | AD | Cần xác minh phiên bản Axmol và toolchain hỗ trợ |
| PR-PLAT-08 | Database MySQL. | AD | Cần xác minh phiên bản và mô hình lưu trữ |
| PR-PLAT-09 | Web Admin. | AD | Cần xác định phạm vi chức năng |
| PR-PLAT-10 | Mobile Admin. | AD | Cần xác định: app riêng hay web responsive |
| PR-PLAT-11 | Tối ưu bộ nhớ, xử lý nhiều NPC và người chơi. | AD | Cần chỉ tiêu định lượng (xem Q-05) |
| PR-PLAT-12 | UI hỗ trợ kéo thả, Auto Batch. | AD | Cần xác minh nghĩa cụ thể của "kéo thả" (editor UI hay thao tác trong game) |

Không mặc định sao chép cách triển khai của người bán source.

## B. Bot

| ID | Yêu cầu | Trạng thái |
|---|---|---|
| PR-BOT-01 | Người chơi gặp, chiến đấu và tham gia hoạt động cùng Bot. | Chốt |
| PR-BOT-02 | Bot hành xử giống người chơi thật nhất có thể. | Chốt, cần tiêu chí đo |
| PR-BOT-03 | Bot có cấp độ, trang bị, kỹ năng, trạng thái, hành vi và tiến trình riêng. | Chốt |
| PR-BOT-04 | Bot biết di chuyển, săn quái, chiến đấu, dùng kỹ năng, hồi máu, chuyển bản đồ, làm nhiệm vụ. | Chốt |
| PR-BOT-05 | Bot tham gia các hoạt động phù hợp. | Chốt, danh sách theo từng hoạt động |
| PR-BOT-06 | Mọi Bot do một hệ thống chung quản lý. | Chốt |
| PR-BOT-07 | Bot là thực thể chung trong một thế giới dùng chung; tất cả người chơi thấy và tương tác với cùng một Bot. | Chốt |
| PR-BOT-08 | Không có bản sao Bot riêng cho từng người chơi. | Chốt |
| PR-BOT-09 | Người chơi A giết Bot thì Bot chết đối với người chơi B và mọi người chơi khác. | Chốt |
| PR-BOT-10 | Trạng thái, vị trí, sinh tử và hoạt động của Bot được đồng bộ thống nhất cho mọi người chơi. | Chốt |
| PR-BOT-11 | Việc người chơi thật không thấy nhau ở bản đồ thông thường không tách thế giới Bot: hai người chơi ẩn nhau vẫn ở cùng một thế giới Bot. | Chốt |

**Quy tắc thế giới Bot (chủ dự án đã chốt, không phải câu hỏi mở):**

- Bot là thực thể chung, tồn tại trong một thế giới dùng chung.
- Tất cả người chơi đều nhìn thấy và tương tác với cùng một Bot.
- Người chơi A giết Bot thì Bot đó chết đối với người chơi B và mọi người chơi khác.
- Trạng thái, vị trí, sinh tử và hoạt động của Bot được đồng bộ thống nhất. Không có bản sao Bot riêng cho từng người.
- Người chơi thật không nhìn thấy nhau ở bản đồ thông thường, nhưng điều đó tuyệt đối không có nghĩa thế giới Bot bị tách riêng. Việc ẩn chỉ áp dụng giữa người chơi thật với nhau.

Hệ quả kỹ thuật để Opus thiết kế, không hỏi lại chủ dự án về quy tắc trên: server giữ một trạng thái Bot duy nhất và là nơi quyết định; cần luật xử lý khi nhiều người chơi không thấy nhau cùng đánh một Bot (ai được tính công, phần thưởng chia thế nào) và cách hiển thị để người chơi không thấy Bot "tự mất máu" khó hiểu. Những thứ Bot tương tác trong thế giới chung (ví dụ quái Bot đang săn) cũng phải nhất quán với trạng thái Bot.

Các phần phải thiết kế (tài liệu `06-BOT-SYSTEM.md`): Bot AI, Scheduler, Behavior, Progression, Inventory, Combat, Navigation, Persistence, Population Management, Synchronization, Instance và World State.

## C. Hiển thị người chơi và instance

| ID | Yêu cầu | Trạng thái |
|---|---|---|
| PR-VIS-01 | Người chơi thật không nhìn thấy nhau ở khu vực thông thường. Chỉ ẩn người chơi thật với nhau, không ẩn và không tách Bot. | Chốt |
| PR-VIS-02 | Người chơi thật chỉ nhìn thấy và tương tác với nhau trong hoạt động được quy định. | Chốt |
| PR-VIS-03 | Mỗi hoạt động có giới hạn số người riêng. | Chốt |
| PR-VIS-04 | Tống Kim giới hạn 20 người. | Cần chủ dự án quyết: 20 tổng hay 20 mỗi phe (Q-01) |

Các phần phải thiết kế: Visibility Rules, Instance Management, Matchmaking, Event Capacity, Party và Team, đồng bộ trạng thái, quyền hiển thị nhân vật, giới hạn người tham gia.

## D. Hoạt động

Mỗi hoạt động là một module độc lập, dùng chung hệ thống nền (instance, matchmaking, phần thưởng, lịch, bot tham gia). Nguồn: bài quảng cáo, là danh sách mục tiêu.

| ID | Hoạt động |
|---|---|
| PR-ACT-01 | Dã Tẩu |
| PR-ACT-02 | Boss Sát Thủ 2x–9x |
| PR-ACT-03 | Tiểu Hoàng Kim, Đại Hoàng Kim |
| PR-ACT-04 | Nhiệm Vụ Hoàng Kim |
| PR-ACT-05 | Câu cá |
| PR-ACT-06 | Vận tiêu |
| PR-ACT-07 | Tống Kim Sơ, Trung, Cao |
| PR-ACT-08 | Hạt Huy Hoàng |
| PR-ACT-09 | Thuyền Phong Lăng Độ |
| PR-ACT-10 | Vượt Ải |
| PR-ACT-11 | Liên Đấu |
| PR-ACT-12 | Hoa Đăng |
| PR-ACT-99 | Hoạt động mở rộng khác |

Với từng hoạt động Opus phải ghi: luật chơi, người thật có thấy nhau không, sức chứa, vai trò của Bot, phần thưởng, lịch, hệ thống nền dùng chung.

## E. Hệ thống phải có thiết kế

Core Server; Network Gateway và Session; Authentication và Account; Character và Progression; World và Map; Monster và NPC; Bot AI và Scheduler; Combat; Skill; Inventory và Equipment; Quest; Activity/Event; Database và Persistence; Axmol Client Core; UI Framework; Asset Pipeline; Audio và Effects; Web Admin; Mobile Admin; Logging và Monitoring; Build/Deployment; Automated Testing.

Không chia việc trước khi có phân tích phụ thuộc và hợp đồng API, schema, giao thức thống nhất.

## F. Yêu cầu chất lượng cho mỗi module

Yêu cầu chức năng, thiết kế, API/interface contract, unit test, integration test, performance test khi cần, tài liệu, tiêu chí nghiệm thu.

Không chấp nhận: code chỉ build được mà không chạy đúng; placeholder báo là hoàn thành; test giả; tự viết tự nghiệm thu; đổi giao thức mà không cập nhật tài liệu; sửa module dùng chung mà không kiểm tra ảnh hưởng. Opus phải thiết lập quy trình reviewer độc lập.

---

## G. Yêu cầu về hệ thống AI và trải nghiệm của chủ dự án

| ID | Yêu cầu |
|---|---|
| PR-OWN-01 | Chủ dự án không phải đọc code, chọn file, chọn branch, tạo worktree, chạy lệnh, sửa lỗi, đọc log dài, điều phối AI hay chuyển log giữa các AI. |
| PR-OWN-02 | Đội AI tự phát hiện và tự sửa lỗi; chỉ báo chủ dự án khi có rủi ro lớn hoặc cần quyết định thuộc quyền chủ dự án. |
| PR-OWN-03 | Một báo cáo tổng hợp mỗi ngày do Opus gửi, 22:00 giờ Việt Nam, đọc hiểu được mà không cần biết lập trình. |
| PR-OWN-05 | Thay Project Manager hoặc bất kỳ AI, model, tài khoản, nhà cung cấp nào, bất cứ lúc nào kể cả khi bị ngắt đột ngột, mà không mất tiến độ, kiến thức và chủ dự án không phải giải thích lại. AI kế nhiệm tiếp quản chỉ từ repository và hồ sơ bàn giao. Bắt buộc. |
| PR-OWN-08 | Trạng thái được lưu thường xuyên lên GitHub, không chỉ cuối ngày. |
| PR-OWN-09 | Về việc thay AI, chủ dự án chỉ nhận thông báo khi cần quyết định, khi bàn giao đã sẵn sàng, hoặc khi PM mới đã tiếp quản. |
| PR-OWN-06 | Trong máy phát triển và workspace, Opus có quyền điều hành cao nhất; hành động không thể khôi phục có cơ chế bảo vệ. |
| PR-OWN-07 | Chủ dự án phê duyệt kế hoạch tổng thể một lần trước khi triển khai; sau đó thao tác thông thường không hỏi lại. |

## H. Câu hỏi mở cho chủ dự án

AI không tự quyết các điểm này. Opus đưa vào báo cáo đầu tiên kèm đề xuất. (Q-02 về thế giới Bot đã được chủ dự án chốt, xem mục B; không hỏi lại. Q-09 về PM sau thời gian dùng thử đã được trả lời bằng yêu cầu thay thế PM, xem `AI-OPERATING-RULES.md` mục 10.)

| ID | Câu hỏi | Ảnh hưởng tới |
|---|---|---|
| Q-01 | Tống Kim 20 người là tổng cả trận hay 20 mỗi phe? Thiếu người thì có cho Bot vào cho đủ không? | Cách ghép trận. |
| Q-03 | Người chơi thật có được lập tổ đội với nhau ở bản đồ thường không, và khi đó có thấy nhau không? | Hệ thống tổ đội. |
| Q-04 | Người chơi thật có chat, giao dịch, lập bang hội với nhau không? | Phạm vi hệ thống xã hội và kinh tế. |
| Q-05 | Mục tiêu quy mô: khoảng bao nhiêu người chơi cùng lúc và bao nhiêu Bot? | Thiết kế và kiểm tra hiệu năng. |
| Q-06 | Người chơi có được biết nhân vật nào là Bot không? | Hành vi và chat của Bot. |
| Q-07 | Master Prompt viết "Kiếm Thế/JX1". Bản game dùng làm mẫu chính là bản nào, phiên bản nào? | Tài liệu tham khảo cho mọi worker. |
| Q-08 | Hình ảnh, âm thanh, bản đồ của game mới lấy từ đâu: làm mới hay dùng lại của game gốc? | Khả năng phát hành hợp pháp (xem rủi ro trong gói bàn giao). |
