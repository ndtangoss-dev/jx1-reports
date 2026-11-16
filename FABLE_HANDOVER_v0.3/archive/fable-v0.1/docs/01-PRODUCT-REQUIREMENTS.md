# 01 – PRODUCT REQUIREMENTS

Phiên bản v0.1 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

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
| PR-BOT-07 | Trạng thái Bot nhất quán giữa những người chơi được phép nhìn thấy. | Chốt |
| PR-BOT-08 | Không có bản sao Bot độc lập tách khỏi thế giới chung. | Chốt |

Các phần phải thiết kế (tài liệu `06-BOT-SYSTEM.md`): Bot AI, Scheduler, Behavior, Progression, Inventory, Combat, Navigation, Persistence, Population Management, Synchronization, Instance và World State.

## C. Hiển thị người chơi và instance

| ID | Yêu cầu | Trạng thái |
|---|---|---|
| PR-VIS-01 | Người chơi thật không nhìn thấy nhau ở khu vực thông thường. | Chốt |
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

Không chấp nhận: code chỉ build được mà không chạy đúng; placeholder báo là hoàn thành; test giả; tự viết tự nghiệm thu; đổi giao thức mà không cập nhật tài liệu; sửa module dùng chung mà không kiểm tra ảnh hưởng (mục cuối bị cắt trong file gốc, Fable suy ra phần còn lại).

---

## G. Câu hỏi mở cho chủ dự án

| ID | Câu hỏi | Vì sao cần |
|---|---|---|
| Q-01 | Tống Kim 20 người là tổng hay mỗi phe? Chỗ trống có được lấp bằng Bot không? | Quyết định matchmaking và sức chứa instance. |
| Q-02 | Ở khu vực thông thường, hai người chơi không thấy nhau có cùng tác động lên một Bot hoặc một con quái không? Ví dụ người A giết Bot X thì người B có thấy X chết không? | Đây là quyết định nền tảng của World State. INV-07 nghiêng về "có", nhưng cần xác nhận vì ảnh hưởng toàn bộ server. |
| Q-03 | Party giữa người chơi thật ở khu vực thông thường: có cho phép và có thấy nhau không? | Master Prompt yêu cầu thiết kế Party/Team nhưng chưa nêu luật hiển thị. |
| Q-04 | Chat, giao dịch, bang hội giữa người chơi thật có tồn tại không khi họ không thấy nhau? | Xác định phạm vi hệ thống xã hội và kinh tế. |
| Q-05 | Chỉ tiêu quy mô: bao nhiêu người chơi đồng thời, bao nhiêu Bot, trên cấu hình server nào? | Không có số thì không thiết kế và test hiệu năng được. |
| Q-06 | Bot có được người chơi nhận ra là Bot không (tên, ký hiệu), hay phải không phân biệt được? | Ảnh hưởng thiết kế hành vi, chat và vấn đề minh bạch với người chơi. |
| Q-07 | Tên gọi: Master Prompt viết "Kiếm Thế/JX1". JX1 thường là Võ Lâm Truyền Kỳ 1, Kiếm Thế là một game khác. Bản tham chiếu gameplay chính là bản nào, phiên bản nào? | Tránh worker nghiên cứu sai tài liệu tham khảo. |
| Q-08 | Tài nguyên hình ảnh, âm thanh, bản đồ lấy từ đâu? Dùng lại của JX1 gốc hay làm mới? | Xem rủi ro bản quyền trong gói bàn giao. |
| Q-09 | Phần cuối Master Prompt bị cắt ở mục 21. Các mục sau đó (ví dụ định dạng báo cáo cuối ngày, lộ trình) là gì? | Fable đã soạn bản đề xuất thay thế, cần đối chiếu với bản gốc. |
