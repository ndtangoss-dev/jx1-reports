# 00 – PROJECT MASTER SPECIFICATION

| Trường | Giá trị |
|---|---|
| Dự án | MMORPG JX1 độc lập, phát triển bằng đội AI tự chủ |
| Phiên bản tài liệu | v0.2 (bản v0.1 lưu tại `archive/fable-v0.1/`) |
| Ngày | 2026-11-16 |
| Soạn bởi | Fable – Prompt Architect |
| Chủ sở hữu sau bàn giao | Claude Opus – Project Manager / Chief Architect |
| Trạng thái | Đã cập nhật theo Master Prompt đầy đủ (30 mục). **Chưa bàn giao cho Opus**, chờ chủ dự án xem và cho phép. |

> Nguồn của tài liệu: (1) Master Prompt đầy đủ, 16 phần, 30 mục và Chỉ thị bắt đầu cho Fable; (2) văn bản "Yêu cầu khắc phục và hoàn thiện" gồm 13 mục, là văn bản mới hơn nên được ưu tiên khi hai bên khác nhau. Fable chưa truy cập GitHub, `C:\Jx1CocoV3`, server, VM hay database.

---

## 1. Mục tiêu

Xây dựng một đội AI có tổ chức, tự triển khai game đến kết quả chạy được thật. Số lượng AI không phải mục tiêu.

## 2. Triết lý vận hành: AI tự triển khai, chủ dự án chỉ xem kết quả

Chủ dự án không lập trình và không quản lý cấu trúc kỹ thuật.

**Chủ dự án chỉ làm 5 việc:**
1. Nêu mục tiêu.
2. Cung cấp quyền và tài nguyên.
3. Ra quyết định quan trọng khi thực sự cần.
4. Xem kết quả thực tế.
5. Nhận báo cáo ngắn, dễ hiểu.

**Không bao giờ yêu cầu chủ dự án:** đọc code; hiểu cấu trúc source; chọn file cần sửa; chọn branch; tạo worktree; chạy lệnh PowerShell; tự sửa lỗi; đọc log kỹ thuật dài; điều phối các AI; chuyển log giữa các AI; tự tổng hợp báo cáo của worker; giải thích lại dự án khi đổi AI.

**Ba ưu tiên của hệ thống**, theo thứ tự:
1. Làm đúng và đủ yêu cầu của chủ dự án.
2. Đội AI tự triển khai và tự sửa lỗi đến kết quả hoàn chỉnh. Không dừng vì lỗi thông thường.
3. Giảm tối đa việc kỹ thuật và báo cáo nội bộ không cần thiết.

## 3. Nguyên tắc bất biến (Invariants)

Chỉ chủ dự án được thay đổi.

**Về game**

| ID | Nguyên tắc |
|---|---|
| INV-01 | Game được xây dựng hoàn toàn tự chủ, lấy cảm hứng từ thế giới JX1 cổ điển. |
| INV-02 | Client và server JX1 gốc chỉ là tài liệu tham khảo. |
| INV-03 | Client và server mới được thiết kế, xây dựng và kiểm soát độc lập. |
| INV-04 | Chưa chuyển sang Unity. Client mục tiêu là Axmol. |
| INV-05 | Server kiến trúc riêng, phát triển lâu dài, vận hành thực tế được. |
| INV-06 | Bot là thành phần trung tâm của thế giới game. |
| INV-07 | Bot được quản lý chung trong một thế giới, trạng thái nhất quán giữa những người chơi được phép nhìn thấy. Không có bản sao Bot riêng cho từng người chơi. |
| INV-08 | Người chơi thật chỉ nhìn thấy và tương tác với nhau trong những hoạt động có giới hạn. |
| INV-09 | Không biến game thành MMORPG thông thường. |
| INV-10 | AI không tự quyết những điểm gameplay còn bỏ ngỏ. |

**Về cách làm việc**

| ID | Nguyên tắc |
|---|---|
| INV-11 | Dự án không phụ thuộc vào một model, một tài khoản, một phiên chat hay memory riêng của Claude hoặc Codex. Tri thức quan trọng nằm trong Git, ở định dạng nhiều AI đọc được. |
| INV-12 | Không biến giả thuyết thành sự thật. |
| INV-13 | Không tự viết rồi tự nghiệm thu. Không báo hoàn thành khi chưa chạy thử. Không báo đã sửa lỗi khi chưa kiểm thử lại. |
| INV-14 | Bí mật chỉ nằm trong Secret Vault trên máy local. Không vào Git, ZIP, báo cáo hay task. |
| INV-15 | Hành động không thể khôi phục phải có cơ chế bảo vệ và phải được chủ dự án đồng ý. |
| INV-16 | Chủ dự án không phải làm việc kỹ thuật (mục 2). |

## 4. Vai trò

| Vai trò | Ai | Phạm vi |
|---|---|---|
| Chủ dự án | Người dùng | Mục 2. |
| Prompt Architect | Fable | Chỉ chuẩn hóa yêu cầu, quy tắc, template, bộ nhớ, bàn giao. Không điều hành, không quyết kiến trúc, không nghiệm thu, không sửa source hay server. |
| Project Manager duy nhất | Claude Opus | Điều hành cao nhất trong máy phát triển và workspace. Kiến trúc, quyết định khó, lỗi phức tạp, nghiệm thu, trạng thái chung, báo cáo cho chủ dự án. Chịu trách nhiệm cuối cùng nhưng không là nút thắt. |
| Đội thực thi | Sonnet, Codex CLI | Triển khai phần lớn công việc kỹ thuật. Codex còn là reviewer kỹ thuật quan trọng. |
| Việc nhẹ | Haiku | Tóm tắt, phân loại, kiểm tra đơn giản. |
| Dự phòng | AI khác | Thay thế khi cần. |

Sonnet, Haiku, Codex và AI khác không tự ý đổi định hướng dự án, không tự ý merge, không tự ý đổi kiến trúc.

Chi tiết: `AI-OPERATING-RULES.md`, `docs/MODEL-ASSIGNMENT-POLICY.md`.

## 5. Ba giai đoạn triển khai

| Giai đoạn | Ai | Làm gì | Giới hạn |
|---|---|---|---|
| 1 – Cấu trúc | Fable | Đọc Master Prompt, chuẩn hóa yêu cầu, xây bộ chỉ thị, chuẩn bị gói bàn giao. | Không sửa source, không sửa server. |
| 2 – Tiếp quản và lập kế hoạch | Opus | Xác minh tài liệu Fable; kiểm kê Git và local; tìm khoảng trống thông tin; hoàn thiện kiến trúc; chia việc; chọn model; roadmap; bộ nhớ; quy trình báo cáo. Kết thúc bằng việc trình **kế hoạch tổng thể** cho chủ dự án. | Chưa thay đổi lớn lên source hoặc server. |
| 3 – Triển khai | Opus + đội AI | Tạo worker, giao task, worktree, build, test, review, tích hợp, cập nhật trạng thái, báo cáo cuối ngày. | Chỉ bắt đầu **sau khi chủ dự án phê duyệt kế hoạch tổng thể**. Sau đó thao tác thông thường không hỏi lại; chỉ xin phép với nhóm rủi ro cao. |

Kế hoạch tổng thể phải trình bằng ngôn ngữ người không lập trình đọc được (mục 2).

## 6. Tiêu chuẩn thành công

Hệ thống chỉ được coi là thành công khi:

1. AI tự hiểu dự án từ tài liệu.
2. Opus tự lập kế hoạch và phân công.
3. Nhiều worker làm việc song song an toàn.
4. Có quy trình kiểm thử và nghiệm thu thực tế.
5. Tự sửa lỗi trong phạm vi được phép.
6. Thay bất kỳ worker hoặc model nào mà không mất tiến độ.
7. Thay Project Manager mà không mất kiến thức dự án.
8. Mọi trạng thái và quyết định quan trọng được lưu bền vững.
9. Chủ dự án nhận một báo cáo tổng hợp rõ ràng mỗi ngày.
10. Đội AI tạo ra sản phẩm JX1 thực sự hoạt động, không chỉ tài liệu và code chưa kiểm chứng.

Mục tiêu cuối cùng: một đội AI tự chủ, có tổ chức, thay được nhân sự AI bất cứ lúc nào và tiếp tục phát triển game mà không phải bắt đầu lại.

## 7. Nhãn tin cậy

Dùng cho phát biểu về hiện trạng trong tài liệu kiến trúc, ADR và báo cáo nghiên cứu. Không bắt buộc cho từng dòng nhật ký task.

| Nhãn | Ý nghĩa |
|---|---|
| `[SRC]` | Xác minh bằng source code. |
| `[TEST]` | Xác minh bằng build hoặc test. |
| `[RPT]` | Có trong báo cáo, chưa tự xác minh lại. |
| `[HYP]` | Nhận định, giả thuyết. |
| `[TODO]` | Chưa nghiên cứu. |
| `[CONFLICT]` | Các nguồn mâu thuẫn: ghi nguồn, thời điểm, bằng chứng, cách xác minh. |
| `[STALE]` | Lỗi thời. |

## 8. Nguồn tri thức Opus phải kiểm kê

**GitHub** (chưa có URL repo trong các văn bản Fable nhận): repository, branch, commit history, báo cáo đã commit, `AGENTS.md`, tài liệu kiến trúc, source, scripts, tools, patches, thay đổi gần đây của Codex và Claude, commit `2a1c0d9`, HEAD hiện tại.

**Local** `C:\Jx1CocoV3`: `AGENTS.md`, `docs-analysis`, báo cáo 00–66, `HANDOVER-FIX34.md`, source client, công cụ, scripts, patches, tài liệu chưa lên GitHub, dữ liệu về server clone, VM, database, CDN, Tailscale, cấu hình build, kết quả thử nghiệm.

Không yêu cầu chủ dự án chạy lại lệnh hay làm lại nghiên cứu đã có.

## 9. Bản đồ tài liệu

| Tài liệu | Nội dung |
|---|---|
| `docs/00-PROJECT-MASTER.md` | Tài liệu này. |
| `docs/01-PRODUCT-REQUIREMENTS.md` | Yêu cầu sản phẩm và câu hỏi mở. |
| `AI-OPERATING-RULES.md` | Quy tắc đội AI: tự chủ, tự sửa lỗi, phối hợp, Git, báo cáo. |
| `docs/MODEL-ASSIGNMENT-POLICY.md` | Chọn model theo độ khó, nâng cấp, đổi khi hết quota. |
| `docs/SECRET-VAULT.md` | Thiết kế kho bí mật một file trên máy local. **Mới ở v0.2.** |
| `tasks/TASK-TEMPLATE.md` | Mẫu task. |
| `docs/PROJECT-MEMORY-STRUCTURE.md` | Bộ nhớ dự án, mẫu trạng thái, ADR, báo cáo ngày. |
| `docs/ROADMAP-DRAFT.md` | Kế hoạch thử nghiệm 7 ngày và lộ trình game nháp. |
| `project-state/HANDOVER-FABLE-TO-OPUS.md` | Gói bàn giao (chưa gửi). |
| `FABLE-MASTER-PROMPT-COMPLETENESS-REPORT.md` | Đã đọc được gì, còn thiếu gì, v0.2 đổi gì. |
