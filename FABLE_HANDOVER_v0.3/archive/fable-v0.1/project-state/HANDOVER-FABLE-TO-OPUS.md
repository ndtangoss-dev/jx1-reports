# HANDOVER PACKAGE – FABLE → OPUS

Ngày 2026-11-16. Từ: Fable – Prompt Architect. Đến: Claude Opus – Project Manager / Chief Architect.

Sau tài liệu này Fable hết vai trò. Opus là đầu mối điều hành duy nhất và chịu trách nhiệm trước chủ dự án.

---

## 1. Fable đã làm và chưa làm

**Đã làm:** đọc Master Prompt, kiểm tra tính nhất quán, chuẩn hóa thành 8 tài liệu dưới đây.

**Chưa làm, và không thuộc vai trò Fable:**
- Chưa đọc GitHub. Master Prompt không có URL repo của dự án.
- Chưa đọc `C:\Jx1CocoV3`, server, VM, database, CDN.
- Chưa xác minh commit `2a1c0d9`.
- Chưa xác minh tài khoản, model, quota.
- Chưa đánh giá Orchestrator, Graphify, Archify, Claude-Mem, OmniRoute, Headroom, Claude Code Setup, Task Observer. Fable không mở các repo này, nên không có nhận định nào về chúng.
- Không sửa source, không chạm server.

**Giới hạn đầu vào:** file Master Prompt Fable nhận được bị cắt giữa mục 21 (dừng ở "Sửa module dùng chung mà không kiể…"). Mọi nội dung sau đó Fable không thấy. Chủ dự án cần gửi phần còn lại cho Opus.

## 2. Danh sách bàn giao

| # | Đầu ra theo Master Prompt | File |
|---|---|---|
| 1 | Project Master Specification | `docs/00-PROJECT-MASTER.md` |
| 2 | Product Requirements | `docs/01-PRODUCT-REQUIREMENTS.md` |
| 3 | AI Operating Rules | `AI-OPERATING-RULES.md` |
| 4 | Model Assignment Policy | `docs/MODEL-ASSIGNMENT-POLICY.md` |
| 5 | Task Template | `tasks/TASK-TEMPLATE.md` |
| 6 | Project Memory Structure | `docs/PROJECT-MEMORY-STRUCTURE.md` |
| 7 | Development Roadmap Draft | `docs/ROADMAP-DRAFT.md` |
| 8 | Handover Package | file này |

Tất cả ở trạng thái bản nháp v0.1. Opus xác minh, sửa, rồi mới commit vào repo.

## 3. Kết quả kiểm tra tính nhất quán

### 3.1. Điểm cần chủ dự án làm rõ

| # | Vấn đề | Ghi ở |
|---|---|---|
| C-01 | Tống Kim "20 người": tổng hay mỗi phe. Master Prompt đã yêu cầu không tự đặt. | Q-01 |
| C-02 | "Bot nhất quán trong thế giới chung" cùng với "người chơi không thấy nhau": chưa nói hai người chơi ẩn nhau có cùng tác động lên một Bot hay một con quái không. Đây là quyết định nền tảng nhất của server. | Q-02 |
| C-03 | Yêu cầu thiết kế Party/Team nhưng người chơi không thấy nhau ở khu vực thường. | Q-03, Q-04 |
| C-04 | "Kiếm Thế/JX1" là hai game khác nhau trong cách gọi thông thường. | Q-07 |
| C-05 | Yêu cầu hiệu năng không có con số. | Q-05 |
| C-06 | Master Prompt bị cắt. | Q-09 |

### 3.2. Điểm Opus tự xử lý

| # | Vấn đề | Fable đã xử lý thế nào |
|---|---|---|
| C-07 | Mục 10 và mục 17 đều liệt kê trường của task, khác nhau một phần. | Gộp thành một mẫu. |
| C-08 | Cấu trúc đề xuất có `AGENTS.md` trong khi local đã có `AGENTS.md`. | Đặt tên file mới là `AI-OPERATING-RULES.md`, yêu cầu hợp nhất, không ghi đè. |
| C-09 | Ba file ACTIVE/BLOCKED/COMPLETED lặp lại thông tin của thư mục `tasks/`. | Đề xuất sinh tự động. |
| C-10 | Phần III yêu cầu nghiên cứu GitHub và local nhưng không nói ai làm; Fable không có quyền truy cập. | Giao cho Opus ở M0. |
| C-11 | Codex và "AI khác" không có trong bảng phân cấp L0–L5. | Đề xuất tạm, chờ Opus đo. |
| C-12 | "Không hỏi chủ dự án cho bước thông thường" cùng với nhiều quyết định phải trình chủ dự án. | Không mâu thuẫn nếu gom câu hỏi vào đầu báo cáo ngày và làm việc khác trong lúc chờ. Đã ghi thành quy tắc. |
| C-13 | L4–L5 do Opus vừa thiết kế vừa nghiệm thu, trong khi cấm tự viết tự nghiệm thu. | Yêu cầu reviewer độc lập là agent khác, không nhận lập luận của người viết. |
| C-14 | Tên thư mục `Jx1CocoV3` gợi ý client hiện có dùng Cocos2d-x. `[HYP]` | Opus xác minh ở M0. Nếu đúng thì liên quan trực tiếp tới việc chuyển sang Axmol. |

### 3.3. Rủi ro Fable thấy cần nói thẳng

| # | Rủi ro | Mức | Gợi ý |
|---|---|---|---|
| R-01 | **PM chạy trên tài khoản dùng thử 7 ngày.** Dự án dài hạn nhưng người điều hành duy nhất có thể biến mất sau một tuần. Chưa rõ gói này có Opus trong Claude Code không. | Cao | Xác minh ngay trong ngày đầu. Chủ dự án quyết phương án sau ngày 7. M0–M1 phải để lại tài liệu đủ cho PM khác. |
| R-02 | **Bản quyền.** Client, server và tài nguyên JX1 gốc thuộc về chủ sở hữu của nó; source bán qua quảng cáo cũng chưa rõ nguồn gốc pháp lý. INV-01…03 (xây độc lập, chỉ tham khảo) đi đúng hướng, nhưng nếu sao chép code hoặc dùng lại hình ảnh, âm thanh, tên riêng thì sản phẩm khó "vận hành thực tế" hợp pháp. | Cao | Chủ dự án quyết (Q-08). Về kỹ thuật: thư mục source gốc chỉ đọc, không copy code vào repo mới, tài nguyên có nguồn rõ ràng. Fable không phải luật sư; nếu định phát hành thương mại nên hỏi tư vấn pháp lý. |
| R-03 | Hạn mức Codex "1.000 USD" chưa xác minh. | Trung bình | Không lập kế hoạch dựa trên con số này trước khi kiểm tra. |
| R-04 | Phạm vi rất lớn (22 hệ thống, 12+ hoạt động, 3 nền tảng, 2 công cụ admin) so với nguồn lực chưa đo. | Cao | Lát cắt dọc M2 là phép thử thật đầu tiên về tốc độ của đội AI. Dùng kết quả đó để ước lượng phần còn lại và báo chủ dự án trung thực. |
| R-05 | Visual Studio 2026, Axmol, iOS: tương thích toolchain chưa kiểm tra. | Trung bình | Build mẫu ở M0. |
| R-06 | Nhiều công cụ bộ nhớ và nén context chồng nhau. | Trung bình | Bảng quyết định ở M0, cài tối thiểu. |
| R-07 | Bot "giống người thật nhất có thể" mà người chơi không biết đó là Bot. | Cần chủ dự án cân nhắc | Q-06. |

## 4. Việc đầu tiên của Opus

Theo thứ tự:

1. Xác minh tài khoản: model nào dùng được, hạn mức, ngày hết hạn. Ghi vào `agents/registry/` và `RISKS.md`.
2. Lấy URL repo GitHub và phần còn thiếu của Master Prompt từ chủ dự án.
3. `git status`, `git log`, so sánh local `C:\Jx1CocoV3` với remote. Xác minh `2a1c0d9` và HEAD.
4. Đọc `AGENTS.md` hiện có và `HANDOVER-FIX34.md`. Đây là trạng thái gần nhất do AI trước để lại.
5. Lập chỉ mục báo cáo 00–66 kèm nhãn tin cậy (giao Haiku/Sonnet đọc, Opus kiểm tra mẫu).
6. Đối chiếu 8 tài liệu của Fable với thực tế, sửa chỗ sai, hợp nhất `AI-OPERATING-RULES.md` vào `AGENTS.md`.
7. Tạo cấu trúc bộ nhớ, commit, viết `CURRENT-STATUS.md` đầu tiên.
8. Đánh giá Orchestrator trên Windows với Claude Code và Codex CLI, rồi các công cụ còn lại.
9. Gửi chủ dự án báo cáo ngày đầu tiên, mở đầu bằng các câu hỏi Q-01…Q-09.
10. Chưa mở worker viết code trước khi xong M1.

## 5. Bảng đánh giá công cụ (Opus điền)

| Công cụ | Giá trị | Chi phí | Rủi ro | Tương thích | Quyết định |
|---|---|---|---|---|---|
| Orchestrator | | | | | |
| Graphify | | | | | |
| Archify | | | | | |
| Claude-Mem | | | | | |
| OmniRoute | | | | | |
| Headroom | | | | | |
| Claude Code Setup | | | | | |
| Task Observer | | | | | |

Lưu ý khi điền: Claude-Mem và cấu trúc `project-state/` cùng lưu tri thức; Headroom và cơ chế nén sẵn có của Claude Code cùng nén context; OmniRoute đổi model có thể làm mất tương thích tool. Mỗi công cụ phải kiểm tra có chạy trên Windows không.

## 6. Xác nhận tiếp nhận

Opus ghi vào đây sau khi đọc xong:

- Ngày giờ tiếp nhận:
- Model và công cụ:
- Những điểm trong tài liệu Fable đã sửa sau khi đối chiếu thực tế:
