# PROJECT MEMORY STRUCTURE

Phiên bản v0.1 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

Nguyên tắc: một AI hoàn toàn mới, chỉ có quyền đọc repo, phải tiếp quản được dự án. Bộ nhớ chính nằm trong Git. Công cụ memory và lịch sử chat chỉ là phần phụ.

Đây là cấu trúc khởi tạo. Opus điều chỉnh theo công cụ thực tế, gộp file trùng, bỏ file không ai đọc.

---

## 1. Cây thư mục

```
/project-root
├── AGENTS.md                  Quy tắc chung cho mọi AI (nguồn duy nhất)
├── CLAUDE.md                  Trỏ về AGENTS.md + phần riêng Claude Code
├── CODEX.md                   Trỏ về AGENTS.md + phần riêng Codex CLI
│
├── docs/
│   ├── 00-PROJECT-MASTER.md
│   ├── 01-PRODUCT-REQUIREMENTS.md
│   ├── 02-ARCHITECTURE.md
│   ├── 03-TECH-STACK.md
│   ├── 04-DATABASE-DESIGN.md
│   ├── 05-NETWORK-PROTOCOL.md
│   ├── 06-BOT-SYSTEM.md
│   ├── 07-GAMEPLAY-SYSTEM.md
│   ├── 08-CLIENT-ARCHITECTURE.md
│   ├── 09-SERVER-ARCHITECTURE.md
│   ├── 10-TESTING-STRATEGY.md
│   ├── 11-SECURITY-RULES.md
│   ├── 12-DECISIONS/          ADR, mỗi quyết định một file
│   ├── MODEL-ASSIGNMENT-POLICY.md
│   └── PROJECT-MEMORY-STRUCTURE.md
│
├── project-state/
│   ├── CURRENT-STATUS.md
│   ├── ACTIVE-TASKS.md
│   ├── BLOCKED-TASKS.md
│   ├── COMPLETED-TASKS.md
│   ├── RISKS.md
│   ├── NEXT-ACTIONS.md
│   └── HANDOVER.md
│
├── tasks/
│   ├── TASK-TEMPLATE.md
│   ├── backlog/  active/  review/  completed/
│
├── agents/
│   ├── registry/              Mỗi agent một file: model, công cụ, giới hạn
│   ├── assignments/
│   └── reports/               Báo cáo theo Task ID
│
├── architecture/
│   ├── graphify/
│   └── archify/
│
└── reports/
    └── DAILY-REPORTS/         YYYY-MM-DD.md
```

## 2. Quan hệ với những gì đã có

`C:\Jx1CocoV3` đã có `AGENTS.md`, `docs-analysis`, báo cáo 00–66, `HANDOVER-FIX34.md`. Cấu trúc mới không xóa hay đổi tên chúng. Opus quyết định giữ nguyên chỗ hay chuyển vào một thư mục lưu trữ, và lập một file chỉ mục ghi cấp tin cậy của từng báo cáo cũ (còn đúng, lỗi thời, mâu thuẫn).

## 3. Nguồn sự thật duy nhất

| Thông tin | Nơi duy nhất | Nơi khác chỉ được |
|---|---|---|
| Quy tắc cho AI | `AGENTS.md` | trỏ tới |
| Yêu cầu sản phẩm | `docs/01-...` | trích ID |
| Quyết định kiến trúc | `docs/12-DECISIONS/` | trích số ADR |
| Trạng thái một task | file task trong `tasks/` | tổng hợp lại |
| Dự án đang ở đâu | `project-state/CURRENT-STATUS.md` | — |
| Giao thức, schema | `docs/05-...`, `docs/04-...` | trích dẫn |

Đề xuất giảm trùng lặp: `ACTIVE-TASKS.md`, `BLOCKED-TASKS.md`, `COMPLETED-TASKS.md` được sinh tự động từ phần đầu YAML của file task bằng một script nhỏ, không sửa tay. `agents/assignments/` có thể bỏ nếu trường `agent` trong task đã đủ.

## 4. Nhịp cập nhật

| File | Khi nào | Ai |
|---|---|---|
| File task | Mỗi lần đổi trạng thái hoặc kết thúc phiên | Agent thực hiện |
| `CURRENT-STATUS.md`, `NEXT-ACTIONS.md` | Cuối mỗi phiên làm việc của PM | Opus |
| `RISKS.md` | Khi phát hiện hoặc đổi mức rủi ro | Opus |
| `HANDOVER.md` | Cuối mỗi phiên của PM, và trước mọi lần đổi AI | Opus hoặc agent rời đi |
| ADR | Khi ra quyết định L4–L5 | Opus |
| Báo cáo ngày | Cuối ngày | Opus (Haiku có thể soạn nháp từ file task) |

## 5. Mẫu CURRENT-STATUS.md

```markdown
# CURRENT STATUS — cập nhật <ngày giờ> bởi <agent>
- Milestone hiện tại: M_ — <tên> — <% tiêu chí thoát đã đạt>
- HEAD nhánh tích hợp: <hash> — build: đạt/lỗi — test: <số qua>/<tổng>
- Đang chạy: <Task ID, agent>
- Đang chặn: <Task ID, lý do>
- Quyết định chờ chủ dự án: <danh sách>
- Thay đổi lớn từ lần cập nhật trước: ...
```

## 6. Mẫu HANDOVER.md

```markdown
# HANDOVER — <ngày giờ> — từ <agent> 
## Đọc theo thứ tự
1. AGENTS.md  2. CURRENT-STATUS.md  3. file này  4. ADR mới nhất
## Việc đang dang dở
| Task | Branch/worktree | Đã xong | Còn lại | Thay đổi chưa commit |
## Điều không ghi ở chỗ khác
<bẫy đã gặp, lệnh phải chạy theo thứ tự nào, môi trường có gì đặc biệt>
## Việc đầu tiên nên làm
```

## 7. Mẫu ADR

Tên file: `docs/12-DECISIONS/ADR-0001-<tên-ngắn>.md`

```markdown
# ADR-0001: <quyết định>
- Trạng thái: đề xuất | chấp nhận | bị thay bởi ADR-xxxx
- Ngày: ...   Người quyết: Opus | Chủ dự án   Cấp: L4 | L5
## Bối cảnh
## Các phương án đã xét
## Quyết định
## Hệ quả và rủi ro
## Bằng chứng (nhãn tin cậy, thử nghiệm, nguồn)
## Yêu cầu liên quan (PR-..., INV-...)
```

ADR không sửa sau khi chấp nhận. Muốn đổi thì viết ADR mới thay thế.

## 8. Mẫu báo cáo cuối ngày

`reports/DAILY-REPORTS/YYYY-MM-DD.md`

```markdown
# Báo cáo ngày YYYY-MM-DD
## 1. Cần chủ dự án quyết
<mỗi mục: câu hỏi, các lựa chọn, đề xuất của Opus, hậu quả nếu chậm>
## 2. Tóm tắt
<3–5 dòng: hôm nay đạt được gì có thể kiểm chứng>
## 3. Tiến độ milestone
## 4. Task hoàn thành (ID, bằng chứng)
## 5. Task đang làm và bị chặn
## 6. Lỗi và rủi ro mới
## 7. Quota và chi phí đã dùng
## 8. Kế hoạch ngày mai
```

Chỉ ghi "hoàn thành" cho task đã qua review. Việc đã viết code nhưng chưa nghiệm thu ghi ở mục 5.

## 9. Agent registry

Mỗi agent một file `agents/registry/<tên>.md`: công cụ (Claude Code, Codex CLI...), tên model đã xác minh, cấp task được nhận, giới hạn quota và song song đã đo, ngày hết hạn tài khoản nếu có, ghi chú chất lượng từ các task đã làm.
