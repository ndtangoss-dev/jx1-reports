# BÀN GIAO

File ngắn. Chỉ ghi điều không có ở chỗ khác. Ai tiếp quản đọc file này sau `README.md`.

## Bản bàn giao hiện tại
- Thời điểm: 2026-11-18 10:47 (hook PreCompact tự ghi đè)
- Việc đang chạy (TASKS status running): F-01, K-03a, K-03b, K-03c, K-03d, K-03e, R-02, R-03, R-04, R-04b, R-05a, R-05b, R-05c, R-05d, R-06a, R-06c, R-07a, R-07b, T-02, T-03, T-04
- Thư cuối đã nhận: #124
- Sắp nén ngữ cảnh: PM mới đọc LUAT-COT-LOI.md, TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md rồi lịch sử chat; chi tiết việc dở ở dòng trạng thái cuối TRANG-THAI.md.

## Nhật ký tiếp quản
| Thời điểm | Ai (model, tài khoản) | Kết quả tự kiểm tra | Sai lệch đã sửa |
|---|---|---|---|
| 2026-11-16 | Sonnet PM, phiên Claude Code `C:\Jx1CocoV3` | Đã đọc README, quy tắc, backlog; nhánh khớp | Chưa có |
| 2026-11-16 22:40 | Sonnet PM, cập nhật bản bàn giao (thử vòng 0-08) | Đã ghi lại việc dở và điều chưa kiểm | Bản cũ ghi "không có việc dở", đã sửa |

## Đổi tài khoản / phiên mới (#108.4)
- Khi chuyển tài khoản Claude: đăng nhập lại Claude Code, rồi gõ `/tiep-tuc`. Bước đầu của `/tiep-tuc` là đọc `STATE/LUAT-COT-LOI.md`. Hook SessionStart (startup, resume, compact) cũng tự in file này vào ngữ cảnh (`TOOLS/hook_luat.py`).
