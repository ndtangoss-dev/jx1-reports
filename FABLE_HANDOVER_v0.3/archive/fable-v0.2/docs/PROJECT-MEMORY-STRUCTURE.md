# PROJECT MEMORY STRUCTURE

Phiên bản v0.2 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

Phép thử: một AI hoàn toàn mới, chỉ đọc được repo, tiếp quản được dự án mà không hỏi chủ dự án câu nào. Bộ nhớ chính là Git, ở định dạng trung lập (Markdown, YAML). Memory riêng của Claude hoặc Codex và lịch sử chat không phải nguồn.

So với v0.1: bảng trạng thái sinh tự động, bàn giao ngắn, báo cáo ngày hai lớp. Giữ nguyên 7 file `project-state/` mà Master Prompt nêu ở mục 16 và mục 23.

---

## 1. Cây thư mục

```
/project-root
├── AGENTS.md                  Quy tắc chung (nguồn duy nhất)
├── CLAUDE.md, CODEX.md        Chỉ trỏ về AGENTS.md + phần riêng của công cụ
│
├── docs/
│   ├── 00-PROJECT-MASTER.md … 11-SECURITY-RULES.md
│   ├── 12-DECISIONS/          ADR
│   ├── MODEL-ASSIGNMENT-POLICY.md
│   ├── SECRET-VAULT.md
│   └── PROJECT-MEMORY-STRUCTURE.md
│
├── project-state/
│   ├── CURRENT-STATUS.md      PM viết: dự án đang ở đâu
│   ├── NEXT-ACTIONS.md        PM viết: các bước tiếp theo theo thứ tự
│   ├── RISKS.md               PM viết
│   ├── HANDOVER.md            Ghi chú cho AI kế nhiệm, chỉ những điều không có ở chỗ khác
│   ├── ACTIVE-TASKS.md        SINH TỰ ĐỘNG từ tasks/
│   ├── BLOCKED-TASKS.md       SINH TỰ ĐỘNG
│   └── COMPLETED-TASKS.md     SINH TỰ ĐỘNG
│
├── tasks/
│   ├── TASK-TEMPLATE.md
│   └── backlog/ active/ review/ completed/
│
├── agents/
│   ├── registry/              Mỗi agent một file: model, quota đã đo, cấp task
│   └── reports/               Chỉ báo cáo chi tiết khi thật cần
│
├── architecture/              Kết quả Graphify, Archify nếu dùng
│
└── reports/DAILY-REPORTS/     YYYY-MM-DD.md

Ngoài repo:  %USERPROFILE%\.jx1-vault\   Secret Vault (không bao giờ trong Git)
```

**Cách giảm trùng lặp mà vẫn giữ cấu trúc chủ dự án đã nêu:**

| File | v0.2 | Lý do |
|---|---|---|
| `ACTIVE-TASKS.md`, `BLOCKED-TASKS.md`, `COMPLETED-TASKS.md` | Giữ tên, nội dung do script sinh ra từ `tasks/` | Không ai phải chép tay thông tin đã có trong file task |
| `HANDOVER.md` | Giữ, nhưng ngắn | Bàn giao worker nằm trong file task; file này chỉ dành cho đổi PM |
| `agents/assignments/` | Đề xuất bỏ | Trường `agent` trong task đã đủ |

Master Prompt cho phép Opus điều chỉnh cấu trúc theo công cụ thực tế. Nếu Orchestrator đã có bảng task riêng, Opus có thể gộp tiếp.

## 2. Tài liệu đã có ở `C:\Jx1CocoV3`

Không xóa, không đổi tên `AGENTS.md`, `docs-analysis`, báo cáo 00–66, `HANDOVER-FIX34.md`. Opus lập một file chỉ mục ghi mỗi báo cáo cũ còn đúng, lỗi thời hay mâu thuẫn.

## 3. Nguồn sự thật duy nhất

| Thông tin | Nơi duy nhất |
|---|---|
| Quy tắc cho AI | `AGENTS.md` |
| Yêu cầu sản phẩm | `docs/01-PRODUCT-REQUIREMENTS.md` |
| Quyết định kiến trúc | `docs/12-DECISIONS/` |
| Trạng thái một task | File task |
| File đã sửa, lịch sử thay đổi | Git |
| Kết quả build và test | CI / log, task chỉ ghi tóm tắt |
| Dự án đang ở đâu | `project-state/CURRENT-STATUS.md` |
| Bí mật | Secret Vault |

Thông tin đã có ở một nơi thì nơi khác chỉ trỏ tới, không chép lại.

## 4. Cập nhật

| Cái gì | Khi nào | Bằng cách nào |
|---|---|---|
| File task | Khi task đổi trạng thái | Agent thực hiện; trường trạng thái tự động |
| Ba bảng task trong `project-state/` | Mỗi lần task thay đổi | Script hoặc hook, không sửa tay |
| `CURRENT-STATUS.md`, `NEXT-ACTIONS.md`, `RISKS.md` | Khi có thay đổi quan trọng, không chờ cuối ngày | Opus |
| `HANDOVER.md` | Cuối mỗi phiên của PM | Opus |
| ADR | Khi ra quyết định L4–L5 | Opus |
| Báo cáo ngày | 22:00 giờ Việt Nam (UTC+7) | Opus (Haiku soạn nháp từ dữ liệu task), qua scheduler thật |

## 5. Mẫu CURRENT-STATUS.md

```markdown
# CURRENT STATUS — <ngày giờ> — <agent>
## Dự án đang ở đâu
- Milestone: M_ — <tên> — <bao nhiêu tiêu chí thoát đã đạt>
- Cái gì đang chạy được thật: ...
- Nhánh tích hợp: <hash> — build đạt/lỗi — test <qua>/<tổng>
## Đang chờ chủ dự án quyết
## Thay đổi lớn từ lần cập nhật trước
```

## 6. Mẫu ADR

`docs/12-DECISIONS/ADR-0001-<tên-ngắn>.md`

```markdown
# ADR-0001: <quyết định>
- Trạng thái: đề xuất | chấp nhận | bị thay bởi ADR-xxxx
- Ngày / Người quyết / Cấp (L4 | L5)
## Bối cảnh
## Phương án đã xét
## Quyết định
## Hệ quả và rủi ro
## Bằng chứng
```

ADR không sửa sau khi chấp nhận; muốn đổi thì viết ADR mới.

## 7. Mẫu báo cáo cuối ngày

`reports/DAILY-REPORTS/YYYY-MM-DD.md`. Hai lớp: lớp chính cho chủ dự án, phụ lục kỹ thuật giữ đủ các mục của mẫu trong Master Prompt (mục 22.2). Khi hai yêu cầu khác nhau, văn bản mới hơn của chủ dự án được ưu tiên: phần chính không có log, commit, diff.

```markdown
# JX1 – BÁO CÁO NGÀY DD/MM/YYYY
Project Manager: <model thực tế>   |   Trạng thái: Đúng tiến độ / Có nguy cơ / Chậm tiến độ

## Cần anh quyết định
<Mỗi mục: câu hỏi, các lựa chọn và hệ quả, đề xuất của Opus.
 Không có thì ghi: "Không có quyết định cần chủ dự án xử lý.">

## 1. Hôm nay đã hoàn thành
<Kết quả đã chạy thử. Tách rõ "đã chạy được" với "đã viết, đang kiểm tra".>

## 2. Cái gì đã chạy được
<Thứ nhìn thấy, dùng được. Kèm ảnh, video hoặc cách mở thử nếu có.>

## 3. Lỗi đã phát hiện và tự sửa
## 4. Lỗi còn tồn tại
## 5. Tiến độ chung
<Mốc hiện tại, khả năng đạt mốc, điều chỉnh nếu cần.>
## 6. Ngày mai
<5–10 việc ưu tiên và kết quả mong đợi.>

<Nếu có task còn chạy sau giờ báo cáo: ghi rõ ở đây.>

---
## Phụ lục kỹ thuật (không cần đọc)
- Task: hoàn thành X/Y · đang chạy · bị chặn · milestone
- Hiệu suất đội AI: | Agent/Model | Nhiệm vụ | Kết quả | Trạng thái |
- Bằng chứng: commit, PR, build, test, file báo cáo
- Rủi ro kỹ thuật
- Tài nguyên: quota Claude, mức dùng Codex, chi phí, nhà cung cấp chạm giới hạn
  (chỉ ghi khi có dữ liệu đáng tin; không có thì ghi "không có dữ liệu")
- Đánh giá của Opus: tiến độ, chất lượng, khả năng hoàn thành milestone
```

Quy tắc: chỉ ghi "hoàn thành" cho việc đã chạy thử và qua kiểm tra độc lập. Sự cố nghiêm trọng gửi riêng, ngay lập tức: chuyện gì, ảnh hưởng gì, đã làm gì, cần anh làm gì. Máy không hoạt động lúc 22:00 thì gửi vào thời điểm sớm nhất sau đó và ghi rõ lý do trễ.

## 8. Agent registry

Mỗi agent một file ngắn: công cụ, tên model đã xác minh, cấp task được nhận, quota và mức song song đã đo, ngày hết hạn tài khoản, phạm vi bí mật được dùng.
