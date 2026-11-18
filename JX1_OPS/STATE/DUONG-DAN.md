# ĐƯỜNG DẪN (#121.2) — mọi nơi trên PC mà hệ thống đọc/ghi

Chỉ ghi tên khóa, không ghi giá trị. Cột "Trong kho" = có nằm trong nhánh `jx1-ops` hay không.

| Đường dẫn | Ai đọc/ghi | Dùng để | Trong kho |
|---|---|---|---|
| `C:\Jx1CocoV3` | Sonnet (Claude Code), Codex (đọc) | Repo dự án chính; `CLAUDE.md`, `AGENTS.md`; chỉ commit cục bộ, KHÔNG push | không (repo khác) |
| `C:\Jx1CocoV3\.claude\settings.json` | Claude Code | Hook: SessionStart, PreCompact, Stop (`stop_guard.py`), hook thư 10 phút | không |
| `D:\jx1-ops-wt` (nhánh `jx1-ops`, thư mục `JX1_OPS`) | Sonnet, Chat, Tổng quản, người gác | Kho vận hành: HOP-THU, STATE, TASKS, TOOLS, REPORTS; push lên `ndtangoss-dev/jx1-ops` | có |
| `D:\JX-wt\<ID>` | Tiểu yêu (Codex), Tổng quản | Worktree mỗi việc, nhánh `task/<ID>` | không |
| `D:\JX-wt\<ID>.codex.log`, `.done`, `.nhip` | `chay_codex.ps1`, Tổng quản | Log, dấu xong (`exit=N`), nhịp sống | không |
| `D:\JX-wt\guard\` (`guard.log`, `goi.lock`, `goi.out`, `goi.err`, `canchu.stamp`) | `guard.ps1` | Nhật ký người gác; khóa theo PID phiên `claude` đã gọi; log lỗi gọi | không |
| `D:\JX-wt\tong_quan\` (`khoa.json`, `lan.json`, `breaker.json`, `astra.txt`, `push.stamp`) | `tong_quan.py` | Khóa nào giữ việc nào, số lần chạy lại, trạng thái cầu dao, danh sách việc thử astra | không |
| `C:\Users\PC\.jx1keys\` (`JX-K2`…`JX-K6`) | `chay_codex.ps1` đọc lúc chạy | Khóa xingchi cho tiểu yêu, mỗi tệp một khóa (chỉ tên) | không, CẤM đưa vào kho |
| `C:\Users\PC\.codex\` (`config.toml`, `auth.json`) | Codex | Cấu hình, đăng nhập Codex mặc định | không |
| `C:\Users\PC\.claude\projects\C--Jx1CocoV3\` | Claude Code; người gác đọc ngày giờ | Lịch sử chat `*.jsonl`, `memory\` | không |
| `C:\Users\PC\.claude\projects\C--Jx1CocoV3\memory\` | Sonnet | Bộ nhớ riêng của phiên | không |
| Task Scheduler `JX-Guard` (5 phút) | Windows | Chạy `TOOLS/guard.ps1` | script có, tác vụ không |
| Task Scheduler `JX-TongQuan` (3 phút) | Windows | Chạy `TOOLS/tong_quan.py` | script có, tác vụ không |
| Task Scheduler `JX-codex-<ID>` | `chay_codex.ps1` | Một tác vụ cho mỗi tiểu yêu | không |
| Task Scheduler `JX-CDN-8080` và các tác vụ cổng | Windows | Máy chủ CDN/APK/bảng tiến độ | script ở `docs-analysis/scripts` (repo chính) |
| `JX1_OPS/STATE/GO-CUA.log` | Sonnet | Nhật ký gõ cửa Chat | có |
| `JX1_OPS/HOP-THU/{CHO-SONNET,TU-SONNET,SO-TAY-CHAT}.md` | Chat ↔ Sonnet | Hòm thư; dòng `GÕ CỬA:` ở SO-TAY-CHAT | có |
| `D:\JX-build\qh9A` | Sonnet, tiểu yêu | Bản A của client/server để thử (bản duy nhất làm việc) | không |
| `D:\VMs\JX-Server-D` | VirtualBox | VM thử | không |

## Đổi tài khoản Claude trên PC (#122.2)
Mở Claude Code ở `C:\Jx1CocoV3`, `/login` tài khoản mới, rồi `/tiep-tuc`. Người gác và Tổng quản không phải cài lại (chạy bằng Task Scheduler, không gắn tài khoản Claude). Gõ cửa chỉ hoạt động khi Sonnet và Chat cùng tài khoản; nếu không, xem luật MAT-KET-NOI-CHAT ở `LUAT-COT-LOI.md` L7.
