# 00 – PROJECT MASTER SPECIFICATION

| Trường | Giá trị |
|---|---|
| Dự án | MMORPG JX1 độc lập, phát triển bằng đội AI tự chủ |
| Phiên bản tài liệu | v0.1 (bản nháp bàn giao) |
| Ngày | 2026-11-16 |
| Soạn bởi | Fable – Prompt Architect |
| Chủ sở hữu tài liệu sau bàn giao | Claude Opus – Project Manager / Chief Architect |
| Trạng thái | Chờ Opus xác minh với GitHub và local |

> Tài liệu này chuẩn hóa Master Prompt của chủ dự án. Fable **chưa** truy cập GitHub, `C:\Jx1CocoV3`, server, VM hay database. Mọi nội dung ở đây thuộc cấp tin cậy "yêu cầu của chủ dự án", chưa phải sự thật đã xác minh về hiện trạng.

---

## 1. Mục tiêu

Xây dựng một hệ thống phát triển game gồm đội AI có tổ chức, có trách nhiệm, có quy trình kiểm soát, tạo ra sản phẩm chạy được thật. Số lượng AI không phải mục tiêu.

Đội AI phải tự làm được: nghiên cứu source và tài liệu, phân tích kiến trúc, lập kế hoạch, chia việc, chọn model, chạy song song, kiểm tra và sửa lỗi, review và tích hợp, cập nhật tài liệu và trạng thái, bàn giao khi đổi AI, báo cáo chủ dự án cuối mỗi ngày.

## 2. Nguyên tắc bất biến (Invariants)

Chỉ chủ dự án được thay đổi các mục này. Mọi AI phải từ chối task vi phạm và báo lên Opus.

| ID | Nguyên tắc |
|---|---|
| INV-01 | Game được xây dựng độc lập, lấy cảm hứng từ thế giới JX1 cổ điển. |
| INV-02 | Client và server JX1 gốc chỉ là tài liệu tham khảo, không phải nền tảng bắt buộc phát triển tiếp. |
| INV-03 | Client và server mới được thiết kế, xây dựng và kiểm soát độc lập. |
| INV-04 | Không chuyển sang Unity ở giai đoạn này. Client mục tiêu dùng Axmol. |
| INV-05 | Server theo kiến trúc riêng, phát triển lâu dài, mở rộng được, vận hành thực tế được. |
| INV-06 | Bot là thành phần trung tâm của thế giới game, không phải tính năng phụ. |
| INV-07 | Bot thuộc một thế giới chung, trạng thái nhất quán giữa những người chơi được phép nhìn thấy chúng. Không tạo bản sao Bot độc lập cho từng người chơi. |
| INV-08 | Người chơi thật không nhìn thấy nhau ở khu vực thông thường. Chỉ nhìn thấy và tương tác trong các hoạt động được quy định, có giới hạn số người. |
| INV-09 | Không biến game thành MMORPG thông thường nơi mọi người chơi nhìn thấy nhau. |
| INV-10 | Dự án không phụ thuộc vào một model, một tài khoản hay một phiên chat. Tri thức quan trọng nằm trong Git và tài liệu dự án. |
| INV-11 | Không biến giả thuyết thành sự thật. Mọi thông tin phải có cấp tin cậy. |
| INV-12 | Không tự viết rồi tự nghiệm thu toàn bộ. Luôn có kiểm tra độc lập theo cấp độ khó. |

## 3. Vai trò

| Vai trò | Ai | Phạm vi |
|---|---|---|
| Chủ dự án | Người dùng | Quyết định định hướng sản phẩm, phê duyệt thao tác Nhóm C, nhận báo cáo cuối ngày. |
| Prompt Architect | Fable | Chỉ giai đoạn đầu: chuẩn hóa yêu cầu, quy tắc, template, cấu trúc bộ nhớ, bàn giao. Không điều hành worker, không quyết định kiến trúc, không nghiệm thu, không sửa source hay server. |
| Project Manager duy nhất | Claude Opus | PM, Chief Architect, Technical Director, Task Orchestrator, Integration Manager, QA Supervisor, Documentation Manager. Chịu trách nhiệm cuối về chất lượng, tiến độ, tính nhất quán. |
| Worker | Sonnet, Haiku, Codex CLI, AI khác | Thực hiện task được giao trong phạm vi file cho phép, bàn giao kèm bằng chứng. |

Chi tiết: `AI-OPERATING-RULES.md`, `MODEL-ASSIGNMENT-POLICY.md`.

## 4. Cấp tin cậy của thông tin

Mọi phát biểu về hiện trạng trong tài liệu, báo cáo, task phải gắn một nhãn:

| Nhãn | Ý nghĩa |
|---|---|
| `[SRC]` | Đã xác minh bằng source code (ghi file, dòng, commit). |
| `[TEST]` | Đã xác minh bằng build hoặc test (ghi lệnh, log, ngày). |
| `[RPT]` | Có trong báo cáo (ghi tên báo cáo), chưa tự xác minh lại. |
| `[HYP]` | Nhận định hoặc giả thuyết. |
| `[TODO]` | Chưa nghiên cứu. |
| `[CONFLICT]` | Mâu thuẫn giữa các nguồn: ghi từng nguồn, thời điểm, bằng chứng, cách xác minh. |
| `[STALE]` | Đã lỗi thời (ghi cái gì thay thế). |
| `[OWNER]` | Yêu cầu hoặc quyết định của chủ dự án. |

`[OWNER]` là nhãn Fable bổ sung để tách yêu cầu sản phẩm khỏi sự thật kỹ thuật. Opus có thể bỏ nếu thấy thừa.

## 5. Nguồn tri thức phải kiểm kê (việc của Opus)

**GitHub** (URL repo chưa có trong Master Prompt): repository, branch, lịch sử commit, báo cáo đã commit, `AGENTS.md`, tài liệu kiến trúc, source, scripts, tools, patches, kết quả phân tích, quyết định kỹ thuật, thay đổi gần đây của Codex và Claude. Kiểm tra commit `2a1c0d9` (được ghi nhận có 68 file do Claude commit) và HEAD hiện tại.

**Local** `C:\Jx1CocoV3`: `AGENTS.md`, `docs-analysis`, báo cáo 00–66, `HANDOVER-FIX34.md`, source client, công cụ phân tích, scripts, patches, báo cáo nghiên cứu JX1, tài liệu mới hơn chưa lên GitHub. Dữ liệu về server clone, VM, database, CDN, Tailscale, cấu hình build, kết quả thử nghiệm, lỗi và giải pháp đã ghi nhận.

Không yêu cầu chủ dự án chạy lại lệnh hay làm lại nghiên cứu đã có kết quả.

## 6. Bản đồ tài liệu

| Tài liệu | Nội dung |
|---|---|
| `docs/00-PROJECT-MASTER.md` | Tài liệu này. |
| `docs/01-PRODUCT-REQUIREMENTS.md` | Yêu cầu sản phẩm có ID. |
| `AI-OPERATING-RULES.md` | Quy tắc hoạt động của đội AI (Opus hợp nhất vào `AGENTS.md` hiện có). |
| `docs/MODEL-ASSIGNMENT-POLICY.md` | Phân cấp model theo độ khó, nâng cấp, nghiệm thu. |
| `tasks/TASK-TEMPLATE.md` | Mẫu task độc lập với model. |
| `docs/PROJECT-MEMORY-STRUCTURE.md` | Cấu trúc bộ nhớ dự án và các mẫu trạng thái, ADR, báo cáo ngày. |
| `docs/ROADMAP-DRAFT.md` | Lộ trình nháp theo milestone. |
| `project-state/HANDOVER-FABLE-TO-OPUS.md` | Gói bàn giao: điểm chưa nhất quán, câu hỏi mở, việc đầu tiên của Opus. |

## 7. Thuật ngữ

| Thuật ngữ | Nghĩa trong dự án |
|---|---|
| Bot | Nhân vật do server điều khiển, hành xử như người chơi, có cấp độ, trang bị, kỹ năng, tiến trình riêng và được lưu trữ. |
| Khu vực thông thường | Bản đồ ngoài các hoạt động có quy định hiển thị người chơi thật. |
| Hoạt động | Module gameplay có luật riêng (Tống Kim, Vận tiêu, Liên Đấu...). |
| Instance | Một bản chạy của bản đồ hoặc hoạt động với tập người tham gia xác định. |
| Worker | AI thực hiện task dưới sự điều phối của Opus. |
| ADR | Bản ghi quyết định kiến trúc trong `docs/12-DECISIONS/`. |
| Nhóm A/B/C | Phân loại quyền tự chủ theo mức rủi ro (xem Operating Rules). |
