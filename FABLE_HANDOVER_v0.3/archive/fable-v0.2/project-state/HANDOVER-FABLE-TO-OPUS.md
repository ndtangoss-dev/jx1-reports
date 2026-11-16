# HANDOVER PACKAGE – FABLE → OPUS

Phiên bản v0.2 – 2026-11-16. Từ: Fable – Prompt Architect. Đến: Claude Opus – Project Manager / Chief Architect.

> **Trạng thái: chưa gửi.** Theo yêu cầu của chủ dự án, gói này chỉ được chuyển cho Opus sau khi chủ dự án xem v0.2 và cho phép. Khi đó Fable kết thúc vai trò; Opus là Project Manager duy nhất.

Opus: anh là người điều hành, không phải người thừa hành tài liệu này. Mọi thứ Fable viết là điểm xuất phát đã chuẩn hóa từ yêu cầu của chủ dự án. Phần nào ghi "đề xuất của Fable" thì anh toàn quyền thay.

---

## 1. Tài liệu đã tạo

| # | Đầu ra | File | Ghi chú v0.2 |
|---|---|---|---|
| 1 | Project Master Specification | `docs/00-PROJECT-MASTER.md` | Thêm triết lý vận hành, ba giai đoạn, tiêu chuẩn thành công |
| 2 | Product Requirements | `docs/01-PRODUCT-REQUIREMENTS.md` | Thêm nhóm yêu cầu về trải nghiệm chủ dự án |
| 3 | AI Operating Rules | `AI-OPERATING-RULES.md` | Viết lại: tự sửa lỗi, phối hợp trực tiếp, ba vùng quyền, báo cáo |
| 4 | Model Assignment Policy | `docs/MODEL-ASSIGNMENT-POLICY.md` | Thêm vai trò Codex, tự nâng cấp, tự chuyển khi hết quota |
| 5 | Task Template | `tasks/TASK-TEMPLATE.md` | Rút gọn |
| 6 | Project Memory Structure | `docs/PROJECT-MEMORY-STRUCTURE.md` | Bảng trạng thái tự sinh, báo cáo ngày hai lớp |
| 7 | Development Roadmap Draft | `docs/ROADMAP-DRAFT.md` | Thêm kế hoạch thử nghiệm 7 ngày |
| 8 | Handover Package | file này | |
| + | Secret Vault | `docs/SECRET-VAULT.md` | Mới |
| + | Completeness Report | `FABLE-MASTER-PROMPT-COMPLETENESS-REPORT.md` | Mới, viết cho chủ dự án |

Bản v0.1 lưu nguyên tại `archive/fable-v0.1/`.

## 2. Quyết định đã chuẩn hóa

Đây là những điều chủ dự án đã nêu rõ; Fable chỉ ghi lại thành dạng có ID.

- Định hướng game: INV-01…INV-10. Không ai ngoài chủ dự án được đổi.
- Chủ dự án không làm việc kỹ thuật (INV-16, PR-OWN-01).
- Opus là Project Manager duy nhất, có quyền điều hành cao nhất trong máy phát triển và workspace.
- Phân cấp L0–L5: Opus quản lý và việc khó; Sonnet triển khai chính; Haiku việc nhẹ; Codex thực thi và review quan trọng.
- Thang tự sửa lỗi 9 bước; lỗi nhỏ không lên Opus; chủ dự án không chuyển log.
- Worker phối hợp trực tiếp; không báo cáo riêng cho mỗi thao tác.
- Ba vùng quyền Xanh / Vàng / Đỏ. Vùng Đỏ đúng bằng danh sách "Nhóm C" của Master Prompt.
- Một file Secret Vault trên máy local.
- Báo cáo cuối ngày 22:00 giờ Việt Nam, một nguồn duy nhất là Opus, sự cố nghiêm trọng báo ngay.
- Ba giai đoạn, có cổng phê duyệt kế hoạch tổng thể trước khi triển khai.
- Mười tiêu chuẩn thành công.

## 3. Fable chưa làm (thuộc việc của Opus)

- Chưa đọc GitHub. Các văn bản Fable nhận không có URL repo của dự án.
- Chưa đọc `C:\Jx1CocoV3`, server, VM, database, CDN.
- Chưa xác minh commit `2a1c0d9`, tài khoản, model, quota.
- Chưa mở và chưa đánh giá Orchestrator, Graphify, Archify, Claude-Mem, OmniRoute, Headroom, Claude Code Setup, Task Observer. Fable không có nhận định nào về chúng.
- Chưa thử công cụ Secret Vault nào trên máy thật.
- Không sửa source, không chạm server, không cài plugin, không tạo worker.

## 4. Vấn đề còn chưa rõ

### 4.1. Cần chủ dự án trả lời
Chín câu Q-01…Q-09 trong `docs/01-PRODUCT-REQUIREMENTS.md` mục H. Quan trọng nhất cho kiến trúc: Q-02 (hai người chơi ẩn nhau cùng tác động lên một Bot), Q-01 (Tống Kim), Q-05 (quy mô), Q-07 (bản game làm mẫu).

### 4.2. Điểm Fable đã dung hòa, Opus nên xem lại

| # | Hai yêu cầu | Fable xử lý |
|---|---|---|
| D-01 | Mẫu báo cáo ngày trong Master Prompt có commit, PR, bảng agent; yêu cầu mới hơn nói không bắt chủ dự án đọc log, commit, diff. | Báo cáo hai lớp: phần chính bằng lời thường, phụ lục kỹ thuật giữ đủ mục của mẫu gốc. |
| D-02 | Master Prompt liệt kê 7 file `project-state/`; yêu cầu mới nói không lặp thông tin đã có trong task. | Giữ đủ 7 file, ba file danh sách task do script sinh. |
| D-03 | "Không tự ý merge vào nhánh chính", "Codex không tự ý merge"; đồng thời "Opus không được là nút thắt". | Đề xuất: merge tự động vào nhánh *tích hợp* cho L0–L2 khi CI qua và reviewer độc lập đồng ý, theo luật do Opus đặt; nhánh chính chỉ Opus. Đây là đề xuất, Opus quyết. |
| D-04 | Quy trình thay AI 8 bước có "cập nhật HANDOVER"; yêu cầu mới nói không cần báo cáo bàn giao dài cho mỗi lần đổi worker. | Đổi worker: file task + commit là đủ. `HANDOVER.md` chỉ dùng khi đổi PM. |
| D-05 | Giai đoạn 2 "chưa thay đổi lớn lên source hoặc server"; kế hoạch 7 ngày lại cần giao task song song từ ngày 3. | Dùng task nhỏ, tách biệt, không đụng source gốc và server; trình kế hoạch tổng thể cuối ngày 2. |
| D-06 | L4–L5 Opus vừa thiết kế vừa nghiệm thu; cấm tự viết tự nghiệm thu. | Reviewer độc lập là agent khác, chỉ nhận đặc tả và diff. |
| D-07 | "Mỗi task có commit và báo cáo"; yêu cầu mới nói không tạo báo cáo Markdown riêng cho mọi thao tác. | Mục "Kết quả" trong file task là báo cáo của task. Báo cáo riêng chỉ khi có kết quả nghiên cứu, lỗi nghiêm trọng, quyết định, bàn giao quan trọng. |
| D-08 | "Một file bí mật duy nhất" và "worker không đọc toàn bộ". | Một file, nhiều phạm vi, cấp qua broker. Giới hạn thật được nêu trong `SECRET-VAULT.md` mục 5. |

### 4.3. Rủi ro

| # | Rủi ro | Mức | Gợi ý |
|---|---|---|---|
| R-01 | PM chạy trên tài khoản Claude Pro dùng thử 7 ngày; chưa rõ gói này có Opus trong Claude Code không và hạn mức bao nhiêu. | Cao | Xác minh trong giờ đầu tiên. Ngày 6 diễn tập đổi PM. Hỏi chủ dự án Q-09. |
| R-02 | Bản quyền: code và tài nguyên JX1 gốc thuộc chủ sở hữu của nó; source mua qua quảng cáo chưa rõ nguồn gốc pháp lý. Sao chép code hoặc dùng lại hình ảnh, âm thanh, tên riêng sẽ cản việc vận hành thực tế. | Cao | Source gốc chỉ đọc, không chép code sang repo mới, tài nguyên có nguồn rõ. Chủ dự án quyết Q-08; nếu phát hành thương mại nên hỏi tư vấn pháp lý. |
| R-03 | Hạn mức Codex "1.000 USD" chưa xác minh. | Trung bình | Không lập kế hoạch dựa trên con số này trước khi kiểm tra. |
| R-04 | Phạm vi rất lớn so với nguồn lực chưa đo. | Cao | Dùng số đo của 7 ngày và lát cắt M2 để ước lượng, báo chủ dự án trung thực. |
| R-05 | Tương thích Visual Studio 2026, Axmol, iOS chưa kiểm tra. | Trung bình | Build mẫu ngày 1. |
| R-06 | Nhiều công cụ bộ nhớ và nén context chồng nhau. | Trung bình | Cài tối thiểu, theo bảng quyết định. |
| R-07 | Cách ly bí mật giữa các worker chỉ là kỷ luật quy trình nếu tất cả chạy cùng một tài khoản Windows. | Trung bình | Xem `SECRET-VAULT.md` mục 5; đạt mức 2 trước khi vault chứa bí mật production. |
| R-08 | Giá trị bí mật lọt vào ngữ cảnh của AI sẽ được gửi tới nhà cung cấp model. | Trung bình | AI làm việc với tên bí mật; giá trị đi qua broker tới tiến trình. |

## 5. Điểm Opus cần xác minh

1. Model, hạn mức, ngày hết hạn của tài khoản Claude; loại hạn mức Codex; số phiên song song thực tế.
2. URL repo; `git status`, `git log`; so local với remote; commit `2a1c0d9`; HEAD.
3. `AGENTS.md` hiện có và `HANDOVER-FIX34.md`: trạng thái gần nhất do AI trước để lại.
4. Báo cáo 00–66: cái nào còn đúng, lỗi thời, mâu thuẫn.
5. Tên thư mục `Jx1CocoV3` gợi ý client hiện có dùng Cocos2d-x `[HYP]`; nếu đúng thì liên quan trực tiếp tới hướng Axmol.
6. Server clone, VM, database, CDN, Tailscale: cái gì đang chạy, cái gì là production (vùng Đỏ).
7. Bí mật hiện đang nằm rải rác ở đâu (file cấu hình, script, báo cáo cũ, lịch sử Git) để gom về vault và thu hồi cái đã lộ.
8. Orchestrator trên Windows với Claude Code và Codex CLI; bảy công cụ còn lại.
9. Có scheduler nào chạy được báo cáo 22:00 khi máy bật mà không có phiên chat mở.
10. Mọi nội dung trong 10 tài liệu của Fable so với thực tế.

## 6. Việc đầu tiên của Opus

1. Mục 5.1 (tài khoản). Nếu không có Opus hoặc hạn mức quá thấp: báo chủ dự án ngay.
2. Mục 5.2–5.4 (kiểm kê).
3. Hợp nhất `AI-OPERATING-RULES.md` vào `AGENTS.md`; tạo cấu trúc bộ nhớ; commit; viết `CURRENT-STATUS.md`.
4. Dựng Secret Vault và thử khôi phục.
5. Dựng scheduler báo cáo.
6. Gửi báo cáo ngày đầu tiên, mở đầu bằng Q-01…Q-09.
7. Theo kế hoạch 7 ngày trong `docs/ROADMAP-DRAFT.md`; trình kế hoạch tổng thể cuối ngày 2.
8. Chưa mở worker viết code game trước khi kế hoạch được duyệt.

## 7. Mười bảy báo cáo Opus phải bàn giao (Master Prompt mục 25)

Mỗi báo cáo phải có bằng chứng hoặc ghi rõ giả định và phần chưa xác minh.

| | Báo cáo | Tài liệu Fable làm điểm xuất phát |
|---|---|---|
| A | Executive Summary | — (viết cho chủ dự án, lời thường) |
| B | Current State Audit | — (kết quả kiểm kê mục 5) |
| C | Product Requirements | `docs/01-PRODUCT-REQUIREMENTS.md` |
| D | Target Architecture | — |
| E | AI Team Architecture | `AI-OPERATING-RULES.md`, `docs/00` mục 4 |
| F | Model Assignment Policy | `docs/MODEL-ASSIGNMENT-POLICY.md` |
| G | Task Management System | `tasks/TASK-TEMPLATE.md` |
| H | Git Strategy | `AI-OPERATING-RULES.md` mục 8 |
| I | Persistent Project Memory | `docs/PROJECT-MEMORY-STRUCTURE.md` |
| J | Plugin/Skill Evaluation | Bảng mục 8 dưới đây |
| K | Development Roadmap | `docs/ROADMAP-DRAFT.md` phần B |
| L | QA and Testing | `AI-OPERATING-RULES.md` mục 4, 7 |
| M | Risk Register | Mục 4.3 file này |
| N | Seven-Day Trial Plan | `docs/ROADMAP-DRAFT.md` phần A |
| O | Implementation Runbook | — |
| P | AI Handover Protocol | `AI-OPERATING-RULES.md` mục 10 |
| Q | Daily Reporting Protocol | `AI-OPERATING-RULES.md` mục 11, mẫu trong Memory Structure |

Để tránh trùng lặp: nơi tài liệu sẵn có đã đủ thì báo cáo tương ứng chính là tài liệu đó sau khi Opus xác minh, không viết bản thứ hai.

## 8. Bảng đánh giá công cụ (Opus điền)

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

Phân loại: Bắt buộc / Nên cài / Có thể cài sau / Không cần thiết / Trùng chức năng / Không tương thích. Lưu ý chỗ dễ trùng: Claude-Mem với `project-state/`; Headroom với cơ chế nén sẵn có; OmniRoute đổi model có thể mất tương thích tool.

## 9. Trạng thái sẵn sàng tiếp quản

- Nội dung: Fable đã đọc đủ Master Prompt (30 mục) và văn bản yêu cầu khắc phục (13 mục); 10 tài liệu đã phản ánh cả hai.
- Chưa sẵn sàng về thủ tục: chờ chủ dự án xem v0.2 và cho phép gửi.
- Không phụ thuộc lịch sử chat: mọi thứ Opus cần nằm trong gói này, trừ URL repo và 9 câu trả lời của chủ dự án.

## 10. Xác nhận tiếp nhận (Opus điền)

- Ngày giờ tiếp nhận:
- Model và công cụ thực tế:
- Những điểm đã sửa sau khi đối chiếu với thực tế:
