# TASK TEMPLATE

Phiên bản v0.3 – 2026-11-16. Rút gọn so với v0.1: bỏ nhật ký dạng bảng, bỏ báo cáo riêng cho từng task, phần bằng chứng trỏ về Git và CI.

Mỗi task là một file `<TASK-ID>.md` trong `tasks/backlog|active|review|completed/`. Phần đầu YAML để máy đọc và để cập nhật trạng thái tự động; phần thân để AI tiếp quản đọc.

**Task ID:** `<KHU VỰC>-<4 chữ số>`, ổn định, không tái sử dụng. Khu vực đề xuất: `INV`, `ARC`, `SRV`, `NET`, `DB`, `BOT`, `GP`, `ACT`, `CLI`, `UI`, `BLD`, `QA`, `SEC`, `ADM`, `DOC`, `OPS`.

---

```markdown
---
id: BOT-0001
title: <kết quả cần đạt, một dòng>
status: backlog          # backlog | active | review | completed | blocked
priority: P1             # P0 chặn milestone | P1 | P2 | P3
difficulty: L2           # L0–L5
agent: <tên trong agents/registry>
reviewer: <agent khác, hoặc auto cho L0–L1>
branch: task/BOT-0001-<mô-tả-ngắn>
worktree: <đường dẫn | none>
depends_on: []
updated: 2026-11-16
---

## Mục tiêu
<Vì sao cần và kết quả cuối là gì. 2–4 câu.>

## Phạm vi
- Làm: ...
- Không làm: ...
- File/module được sửa: ...
- File/module không được sửa: ...

## Đầu vào
<Tài liệu, ADR, hợp đồng liên quan.>

## Tiêu chí nghiệm thu
- [ ] <điều kiện kiểm chứng được>

## Lệnh build và test
<lệnh chính xác>

---
## Kết quả            <!-- agent điền khi chuyển sang review -->
- Commit: <hash>     (file đã sửa xem trong commit)
- Test: <lệnh đã chạy → qua/lỗi, số liệu thật>
- Còn thiếu hoặc lỗi còn lại: ...

## Đã thử nhưng không được
<Chỉ ghi khi có. Vài dòng, để AI sau không lặp lại.>

## Review
<Reviewer: đạt | trả lại + lý do cụ thể.>

## Bước tiếp theo
<Một việc cụ thể. Luôn có, kể cả khi blocked.>
```

---

## Quy tắc

- Sáu thứ phải luôn đọc được từ file task và Git, để bất kỳ AI nào tiếp quản được: trạng thái, kết quả, file đã sửa, test, lỗi, bước tiếp theo.
- Không viết báo cáo riêng cho task trừ khi có kết quả nghiên cứu, lỗi nghiêm trọng, quyết định hoặc bàn giao quan trọng.
- Trường `status` và `updated` do công cụ cập nhật khi file di chuyển giữa các thư mục, không sửa tay ở nơi khác.
- Tiêu chí nghiệm thu phải kiểm chứng được bằng lệnh hoặc quan sát cụ thể.
- Đổi agent: sửa trường `agent`, không tạo task mới.
- Sửa file ngoài phạm vi sau khi thỏa thuận với worker khác: thêm một dòng vào "Phạm vi".
- Opus có thể chuyển sang JSON/YAML thuần nếu Orchestrator yêu cầu, miễn giữ các trường trên.
