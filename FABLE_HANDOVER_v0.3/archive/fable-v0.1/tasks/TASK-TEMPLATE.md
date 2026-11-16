# TASK TEMPLATE

Phiên bản v0.1 – 2026-11-16. Gộp hai danh sách trường ở mục 10 và mục 17 của Master Prompt thành một mẫu.

Mỗi task là một file Markdown có phần đầu YAML, đặt tên `<TASK-ID>.md`, nằm trong `tasks/backlog|active|review|completed/`. Dạng này đọc được với Claude, Codex và công cụ tự động.

**Task ID:** `<KHU VỰC>-<số 4 chữ số>`, không bao giờ đổi và không tái sử dụng. Khu vực đề xuất: `INV` (kiểm kê), `ARC` (kiến trúc), `SRV`, `NET`, `DB`, `BOT`, `GP` (gameplay), `ACT` (hoạt động), `CLI` (client), `UI`, `BLD` (build), `QA`, `SEC`, `ADM` (admin), `DOC`, `OPS`.

Sao chép từ dòng dưới.

---

```markdown
---
id: BOT-0001
title: <một dòng, nêu kết quả cần đạt>
status: backlog          # backlog | active | review | completed | blocked
priority: P1             # P0 chặn milestone | P1 | P2 | P3
difficulty: L2           # L0–L5, theo MODEL-ASSIGNMENT-POLICY
milestone: M4
agent: <tên trong agents/registry, ví dụ sonnet-w2 | codex-w1>
reviewer: <agent khác với agent thực hiện>
branch: task/BOT-0001-<mô-tả-ngắn>
worktree: <đường dẫn, hoặc "none">
depends_on: []           # danh sách Task ID
blocks: []
created: 2026-11-16
updated: 2026-11-16
max_attempts: 3          # vượt thì chuyển blocked và báo Opus
---

## Mục tiêu
<Vì sao cần task này và kết quả cuối là gì. 2–4 câu.>

## Phạm vi
- Làm: ...
- Không làm: ...

## File và module
- Được phép sửa: ...
- Không được sửa: ...

## Tài liệu đầu vào
- docs/... (mục nào)
- ADR-...
- Báo cáo liên quan: ...

## Tiêu chí nghiệm thu
- [ ] <điều kiện kiểm chứng được, có lệnh hoặc quan sát cụ thể>
- [ ] ...

## Lệnh build và test
<lệnh chính xác, chạy từ thư mục nào>

## Kết quả bàn giao
- Code tại: ...
- Tài liệu cập nhật: ...
- Báo cáo: agents/reports/BOT-0001.md

---
<!-- Phần dưới do agent thực hiện và reviewer điền -->

## Nhật ký
| Thời điểm | Agent | Việc đã làm | Kết quả |
|---|---|---|---|

## Bằng chứng
- Commit: <hash>
- File đã sửa: ...
- Đầu ra build/test: <dán phần chính hoặc trỏ tới file log>
- Chưa làm hoặc còn thiếu: ...

## Thử nghiệm thất bại
<Đã thử gì, vì sao không được. Để AI kế tiếp không lặp lại.>

## Kết quả review
- Reviewer: ...
- Kết luận: đạt | trả lại
- Ghi chú: ...

## Next action
<Một việc cụ thể tiếp theo và ai làm. Luôn điền, kể cả khi blocked.>
```

---

## Quy tắc điền

- Trường phần đầu YAML là bắt buộc trước khi chuyển sang `active`, trừ `worktree` khi không chạy song song.
- Tiêu chí nghiệm thu phải kiểm chứng được. "Code sạch", "hoạt động tốt" không phải tiêu chí.
- `reviewer` khác `agent`. Với L0–L1 có thể ghi `auto` nếu kiểm tra bằng script và checklist.
- Khi đổi agent: thêm dòng vào Nhật ký, sửa trường `agent`, không tạo task mới.
- "Next action" là thứ AI tiếp quản đọc đầu tiên.
- Opus có thể chuyển sang JSON hoặc YAML thuần nếu Orchestrator yêu cầu, miễn giữ đủ các trường trên.
