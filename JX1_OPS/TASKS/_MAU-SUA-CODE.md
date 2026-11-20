---
id: SC-<so>
title: <sửa gì, ngắn>
status: ready
level: L3
agent: codex
loai: sua-code
skill: jx1-sua-code
effort: high
priority: 1
owner: B
branch: task/SC-<so>
worktree: D:\JX-wt\SC-<so>
depends_on: []
vung_file: ['<file được sửa, đúng đường dẫn>']
build: server | client | lua | khong
updated: <ngày>
---

## Lỗi / mục tiêu (lời chủ nguyên văn nếu có)
## Bằng chứng đã có (số đo của A, ảnh, log)
## Nghi phạm và chỗ bắt đầu (Sonnet B ghi: hàm, file:dòng ước lượng, hồ sơ tính năng)
## Tiêu chí xong (đo được)
- Build sạch; diff chỉ trong vung_file; có công tắc (C++).
- KỊCH BẢN KIỂM ĐỘNG cho A: thao tác → số kỳ vọng.
## Tiền điều kiện (Tổng quản kiểm trước khi đặt status ready)
- Mọi file trong vung_file và file tham chiếu tồn tại trong worktree/kho (liệt kê đường dẫn); worktree cắt từ nhánh đúng. Thiếu thì chưa giao, không để Codex BLOCKED (bài học SC-001/SC-002 20/11).
## Quyền
- Được: đọc mã, sửa vung_file trong worktree, build theo `build`.
- Cấm: VM/Test-36/LD/gs001 đang chạy, phát APK, Main VM, mạng ngoài, commit/push (Tổng quản gộp).
## Báo cáo cuối
`JX1_OPS/REPORTS/SC-<so>.md` theo `.agents/skills/jx1-sua-code/references/ban-giao.md`.
