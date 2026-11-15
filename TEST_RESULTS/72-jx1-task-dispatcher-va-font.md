# Báo cáo 72 — JX1 Task Dispatcher và font tiếng Việt

Cập nhật: 15/11/2026

## TÓM TẮT 5 DÒNG
1. Đã tạo dispatcher Python stdlib, manifest task được duyệt, state bền vững, khóa một tiến trình, hash pin và kiểm tra phạm vi thay đổi.
2. Đã cập nhật workflow/start-here, tạo manifest và chạy task fixture từ GitHub qua Dispatcher đến báo cáo upload thành công.
3. 10 unit tests đạt; task giả tạo đúng file UTF-8 cùng báo cáo local/remote, không sửa source game.
4. Launcher JX1 đặt input/output/code page UTF-8; Cascadia Mono và Consolas có glyph tiếng Việt; lỗi `cp1252` khi xem trạng thái đã sửa và có test hồi quy.
5. Task Scheduler đang `Running`, quyền `Limited`; đã kiểm thử tạm dừng/bật lại và state fixture vẫn `COMPLETED`.

## Môi trường và cấu hình
- Phiên công cụ: PowerShell 7.6.9; launcher thủ công hiện dùng Windows PowerShell 5.1.19041.5007.
- Trước sửa: console input CP437, output encoding UTF-8, active code page 437.
- Helper launcher đặt code page/input/output thành 65001 và thử chọn `Cascadia Mono` bằng API console chỉ trong console hiện tại. Không thay đổi encoding toàn hệ thống hoặc registry.
- GDI glyph check: Cascadia Mono `COVERED`; Consolas `COVERED` với `ă â ê ô ơ ư đ`, các dấu thanh và combining marks được kiểm tra.
- PowerShell helper trong phiên automation không có console handle (`GetCurrentConsoleFontEx` trả lỗi 6), nên host tự quản lý font. Không dùng Computer Use để điều khiển/đọc TUI vì skill hiện hành cấm tự động hóa Windows Terminal/PowerShell/Codex CLI. Hiển thị trực quan TUI và nhập bằng bàn phím: **CHƯA KIỂM THỬ**.
- `CODEX_HOME/config.toml` mặc định đang là `gpt-6-luna / xingchi / xhigh`; Dispatcher ghi đè tường minh mỗi lượt thành `gpt-6.1-sol / xingchi / max`. Codex CLI `0.166.0-alpha.5.1`; preflight read-only với các override mục tiêu đã trả `JX1_DISPATCHER_PREFLIGHT_OK`. Event JSON không nêu model/provider, nên bằng chứng là tham số CLI, định nghĩa provider và preflight.

## Thay đổi
- `docs-analysis/scripts/jx1_task_dispatcher.py`: polling GitHub API mỗi 60 giây với ETag; chỉ nhận queue entries được duyệt; prompt/tài liệu được tải tại commit đã ghim và xác minh Git blob SHA; giới hạn kích thước/đường dẫn; Task ID at-most-once; queue/status state nguyên tử; khóa `msvcrt`; resume session hoặc `BLOCKED` khi không thể resume; kiểm tra Git diff trước/sau; báo cáo tiếng Việt, secret scan, upload dùng Git Credential Manager khi có quyền.
- `docs-analysis/scripts/install_jx1_task_dispatcher.ps1`: Task Scheduler tại logon cho user hiện tại, `Interactive`, `Limited`, `IgnoreNew`, thời hạn chạy vô hạn, restart tối đa 3 lần.
- `docs-analysis/scripts/uninstall_jx1_task_dispatcher.ps1`, `enable_jx1_task_dispatcher.ps1`, `disable_jx1_task_dispatcher.ps1`, `status_jx1_task_dispatcher.ps1`: rollback/vận hành; gỡ task không xóa state, log hay report.
- `docs-analysis/scripts/configure_jx1_codex_console.ps1`: UTF-8 và font theo console; `test_jx1_font_coverage.ps1`: kiểm tra glyph.
- `tmp_start_xingchi_codex.ps1`: gọi helper UTF-8/font trước khi mở Codex. Đây là file untracked đã tồn tại; thay đổi giới hạn vào launcher JX1.
- `docs-analysis/scripts/test_jx1_task_dispatcher.py`, `test_jx1_task_dispatcher_live.py`: unit tests và integration fixture opt-in.
- `docs-analysis/BAI_HOC.md`: thêm các lỗi/biện pháp mạng, sandbox, logger test và byte encoding.

## Kiểm thử thực tế
- Unit: `python.exe -B -I docs-analysis/scripts/test_jx1_task_dispatcher.py` — 10/10 đạt, bao gồm phục hồi session và xuất JSON tiếng Việt khi stdout ban đầu là `cp1252`.
- `python.exe -B -I docs-analysis/scripts/jx1_task_dispatcher.py --status` — sau sửa, JSON status và tiếng Việt in được; trước sửa phát sinh `UnicodeEncodeError`.
- Codex CLI: preflight read-only và task giả qua `Dispatcher.run_task` đạt; Task ID `LIVEFIX-F9764FEC0E`, trạng thái `COMPLETED`.
- Fixture: `docs-analysis/out/jx1-dispatcher-fixture-20261115/DISPATCHER_LIVEFIX-F9764FEC0E.txt`; đúng nội dung `JX1_DISPATCHER_FIXTURE_OK`.
- Báo cáo fixture: `docs-analysis/reports/dispatcher-livefix-f9764fec0e.md`.
- Git path audit: chỉ hai file fixture/report trên thay đổi trong lượt fixture; `Folder` và `SwordOnline` không có thay đổi mới. File `.bak-qh` hiện thấy dưới `SwordOnline` là thay đổi untracked có từ trước.
- GitHub GET từ sandbox bị chặn socket; GET chỉ đọc ngoài sandbox trả HTTP 200. Dispatcher sẽ polling từ tiến trình Task Scheduler trên host.
- Git Credential Manager trả credential dưới tài khoản Windows hiện tại mà không in token; upload report trả thành công và report đọc lại được từ GitHub.
- Task Scheduler `JX1-Task-Dispatcher`: `Running`, trigger `AtLogOn`, `Interactive`, `Limited`, `IgnoreNew`, `PT0S`, restart 3 lần/1 phút. Đã chạy script disable/enable: trạng thái chuyển `Disabled` rồi trở lại `Running`; state giữ nguyên và fixture vẫn `COMPLETED` sau khi tiến trình khởi động lại. Chưa reboot Windows thật.
- Truy vấn Scheduler trong sandbox bị `Access denied`; truy vấn chỉ đọc có quyền sau đó xác nhận task tại `\\`, trạng thái `Running`, `Interactive`, `Limited`.
- Queue approval commit `8c5df242a1b539188513e26536460196c6379d03` được nhận trong 7 giây; task bắt đầu `2026-11-15T03:49:26Z`, hoàn tất `2026-11-15T03:53:10Z`, upload report `UPLOADED`. Sau kiểm thử, manifest được đổi sang `COMPLETED`.

## GitHub
- `ndtangoss-dev/jx1-reports/WORKFLOW_JX1.md` cập nhật dispatcher workflow, approval manifest, sandbox và vận hành.
- `PROMPTS/00_CODEX_START_HERE.md` cập nhật quy trình tự nhận task và phương án thủ công.
- Tạo `PROMPTS/DISPATCH_QUEUE.json`; chỉ còn fixture `LIVEFIX-20261115-DISPATCHER-01` ở trạng thái `COMPLETED`, không còn task được duyệt chờ chạy.
- Commit workflow: `65878e5b7ff06bc8fb9cf87684c32d173b621ca2`.
- Commit start-here: `b35c3904bbedb23dd9406498e1ae431c40fcb151`.
- Commit queue: `24531873431794ca124a50e85d33eb9316858655`.
- Commit fixture prompt: `806ff7e88b5ec165a4f1a2faf3be08a223818dc1`.
- Commit queue completion: `1af2d05aaf3c37000a229353c417fa10d6f4279c`.

## Cài đặt và rollback
- Cài đặt: `docs-analysis/scripts/install_jx1_task_dispatcher.ps1`; task đã được đăng ký và khởi chạy, script từ chối ghi đè task cùng tên.
- Rollback: `docs-analysis/scripts/uninstall_jx1_task_dispatcher.ps1`; chỉ xóa `JX1-Task-Dispatcher`, giữ nguyên state, logs, reports và credentials.
- Tạm dừng/tiếp tục: các script `disable_...` và `enable_...`.
- Đã xác minh: task có state `Running`; state/log ghi nhận khởi động, polling, `QUEUED → RUNNING → COMPLETED`; manifest không còn task pending.

## Giới hạn và rủi ro còn lại
- `allowed_paths` được thêm vào prompt và kiểm tra bằng Git diff sau lượt chạy; sandbox của CLI giới hạn bên ngoài `C:\Jx1CocoV3`, không cô lập từng thư mục bên trong. Nếu phát hiện file ngoài phạm vi, dispatcher đánh dấu `BLOCKED`, giữ nguyên thay đổi để tránh ghi đè dữ liệu người dùng.
- Task chạy bằng `workspace-write` với `approval_policy=on-request`. Khi Codex cần phê duyệt tương tác, dispatcher không tự duyệt; task dừng/đánh dấu `BLOCKED`.
- Khởi động lại Windows chưa kiểm thử; cấu hình trigger tại đăng nhập và state/session ID đã xác minh tĩnh, nhưng reboot/resume thật còn **CHƯA KIỂM THỬ**.
- TUI và nhập bàn phím thực tế chưa được xác minh bằng hình ảnh; helper font chỉ được kiểm tra bằng GDI glyph coverage và code page.
- Cấu hình mặc định toàn cục trong `config.toml` khác model/effort mục tiêu; Dispatcher và launcher truyền override rõ ràng. Nếu chạy CLI trực tiếp ngoài hai lối này, phải xác minh/chỉ định lại cấu hình.

Cần tôi quyết định: không

