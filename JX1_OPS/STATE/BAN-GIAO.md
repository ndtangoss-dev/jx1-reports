# BÀN GIAO

File ngắn. Chỉ ghi điều không có ở chỗ khác. Ai tiếp quản đọc file này sau `README.md`.

## Bản bàn giao hiện tại
- Thời điểm: 2026-11-16 22:40
- Từ: Sonnet PM (phiên Claude Code `C:\Jx1CocoV3`) → PM kế nhiệm hoặc chính phiên sau khi `/tiep-tuc`
- Điểm lưu: commit mới nhất của nhánh `jx1-ops`
- Việc đang dở: **0-07** (đã có `docs-analysis/scripts/jx_env_up.ps1` chạy tốt khi môi trường đã lên; CHƯA thử qua tắt bật VM thử vì VM thử không tự đăng nhập `mu1`, mà `JX-ChainUp` cần phiên desktop; nối `jx_mainvm_ensure.ps1` đã làm nhưng Main VM không trả lời ping 192.168.1.50 lúc 22:14, chưa tìm nguyên nhân; đổi tên máy VM thử còn lại). Sau đó **0-08** (thử trọn vòng tạm dừng) rồi giai đoạn A.
- Đã xong giai đoạn 0: 0-01…0-06, 0-09, 0-10 (xem bảng "Tiến độ task" trong TRANG-THAI).
- Chưa kiểm chứng: bản Tailscale của Bảng tiến độ (cổng 8092, cần Tailscale bật + script Admin); `/tiep-tuc` trong phiên mới sau khi cài hook Graphify và hook Stop; Windows Terminal (không cài được).
- Điều cần biết:
  - Q-18…Q-22 trong `STATE/QUYET-DINH.md`: tự chủ với Main VM, bật/tắt chuỗi server VM thử, câu hỏi chờ không dừng lượt, **không kết thúc lượt bằng câu hỏi (Q-21)**, trần Codex tạm.
  - Hook Stop `TOOLS/stop_guard.py` chặn dừng lượt khi còn task; muốn dừng hợp lệ ghi thẻ `[DUNG-CAN-CHU yyyy-mm-dd HH:MM]` vào TRANG-THAI.
  - Bảng tiến độ: Artifact `https://claude.ai/artifact/7bUxS1STLrmZ6btueV3eiy`, PM xuất bản lại sau mỗi mốc lớn.

## Nhật ký tiếp quản
| Thời điểm | Ai (model, tài khoản) | Kết quả tự kiểm tra | Sai lệch đã sửa |
|---|---|---|---|
| 2026-11-16 | Sonnet PM, phiên Claude Code `C:\Jx1CocoV3` | Đã đọc README, quy tắc, backlog; nhánh khớp | Chưa có |
| 2026-11-16 22:40 | Sonnet PM, cập nhật bản bàn giao (thử vòng 0-08) | Đã ghi lại việc dở và điều chưa kiểm | Bản cũ ghi "không có việc dở", đã sửa |

## Đổi tài khoản / phiên mới (#108.4)
- Khi chuyển tài khoản Claude: đăng nhập lại Claude Code, rồi gõ `/tiep-tuc`. Bước đầu của `/tiep-tuc` là đọc `STATE/LUAT-COT-LOI.md`. Hook SessionStart (startup, resume, compact) cũng tự in file này vào ngữ cảnh (`TOOLS/hook_luat.py`).
