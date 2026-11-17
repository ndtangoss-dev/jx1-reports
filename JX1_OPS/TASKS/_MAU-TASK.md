---
id: <MA-TASK>
title: <kết quả cần đạt>
status: backlog          # giữ hệ trạng thái task hiện hữu; không đổi chỉ để hợp mẫu
level: <PM giao>         # task cũ có L0–L5 hoặc green; không suy quyền từ mức
agent: codex
branch: task/<MA-TASK>
worktree: D:\JX-wt\<MA-TASK>
depends_on: []
backlog_ref: null        # có thì ghi; thiếu không chặn task đã duyệt
vung_file: []            # liệt kê đủ vùng được sửa, gồm báo cáo
tai_nguyen: []           # mặc định không VM/mạng/build/exe
updated: <YYYY-MM-DD>
---

## Mục tiêu và tiêu chí xong
<Một đầu ra kiểm chứng được; thiết kế khoảng 5–10 phút. PM tách task lớn trước;
worker không tự bỏ dở phạm vi đã duyệt khi hết mốc thời gian.>

## Nguồn cần đọc
- Prompt/task này, commit ghim nếu có: <đường dẫn@SHA hoặc không ghim>.
- Nguồn tối thiểu: <file + mục/symbol; không yêu cầu cả repo/workflow/STATE>.
- Chỉ đọc `STATE/QUYET-DINH.md` khi task dẫn quyết định cụ thể hoặc có mâu thuẫn cần giải.
- Dùng đường dẫn task/prompt hiện tại; không tái dùng root của task khác.
- Map/Graphify/tóm tắt chỉ định vị: kiểm lại file thật và dòng hiện tại.

## Phạm vi và quyền đã duyệt
- Được sửa: <khớp vung_file; đường dẫn báo cáo bên dưới cũng là đầu ra được phép>.
- Không sửa/chạy: <source/canonical/Main VM/exe/mạng… theo task>.
- Build/test/kết nối được phép: <lệnh, bản copy/VM, đích; hoặc KHÔNG>.
- Commit: <có/không>; push: <có/không>; không suy push từ quyền commit.
- Kiểm tra Git status/branch một lần trước ghi. Sai worktree/branch: giữ nguyên, báo PM,
  không tự checkout/reset. Thiếu trường mẫu không tự chặn mục tiêu/phạm vi đã rõ.

## Báo cáo cuối
`JX1_OPS/REPORTS/<MA-TASK>.md` — nếu đã triển khai, dùng `jx1-report`, thêm
`jx1-parameters` khi cần; thiếu skill thì dùng trực tiếp mẫu dưới, không tự cài.
Một báo cáo: `TOM TAT 5 DONG`, `DA XAC MINH / CHUA XAC MINH`, `file:dòng`, test thực
chạy/chưa chạy, mọi lỗi/cách thử/kết quả, `DONE/PARTIAL/BLOCKED/FAILED`, SHA/link hoặc
lý do chưa commit/push, bước tiếp tục. Khảo sát thêm `MUC SO THONG SO` và
`DE XUAT TOI UU`; không đo thì ghi chưa đo.

## Kết quả (chỉ cập nhật task nếu thuộc vùng được sửa)
<Đường dẫn báo cáo; commit/test; phần thiếu; bước tiếp tục hoặc không còn việc.>
