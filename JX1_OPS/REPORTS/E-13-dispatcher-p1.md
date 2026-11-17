TÓM TẮT 5 DÒNG
1. DONE: đã thêm dispatcher P1, mặc định dry-run; chỉ giao thật khi PM chỉ rõ allowlist và snapshot ngân sách.
2. Lượt CLI 5 task giả đạt `done: 5`, `scan_errors: []`; 11 kiểm thử offline đạt.
3. Có giới hạn 3 worker/khóa, tài nguyên/worktree, timeout, retry, QUEUE, heartbeat và cổng ngân sách.
4. Không chạy Codex thật, Scheduled Task thật, VM, exe game/server hoặc mạng; không đọc nội dung khóa.
5. [CHƯA KIỂM] Hai task thật và đường dừng Scheduled Task do PM kiểm; chưa commit/push trong lượt này.

## Phạm vi và cách tích hợp

Đọc đúng task E-13, DESIGN/TONG-QUAN-DIEU-PHOI.md, chay_codex.ps1,
stop_guard.py, mailbox_hook.py và mục Dispatcher cũ trong ENVIRONMENT.md.
Git ban đầu: nhánh `task/E-13`, chỉ `?? JX1_OPS/TASKS/E-13.md`; giữ nguyên
nội dung task có sẵn, chỉ nối mục kết quả theo yêu cầu riêng trong task.

ENVIRONMENT.md chỉ nhắc `jx1_task_dispatcher.py`, không cho vị trí mã.
Không tìm thấy tại TOOLS hoặc các đường dẫn cụ thể đã thử
`D:\JX-tools\jx1_task_dispatcher.py`, `D:\JX-tools\dispatcher\jx1_task_dispatcher.py`,
`C:\Jx1CocoV3\jx1_task_dispatcher.py`, `C:\Jx1CocoV3\tools\jx1_task_dispatcher.py`,
`C:\Jx1CocoV3\scripts\jx1_task_dispatcher.py`.
Không quét rộng tìm mã cũ. Mở rộng quy trình launcher hiện có bằng scheduler
Python trong vùng dispatcher; không sửa/chép launcher và hook ngoài phạm vi.
[CHƯA KIỂM] Mã dispatcher cũ có thể nằm nơi khác chưa được chỉ định.

## Kết quả triển khai

- `TOOLS/dispatcher/dispatcher.py`: quét front matter tối thiểu, priority/tuổi,
  trạng thái riêng, depends_on, resource/worktree lock, key pool, 3 worker/khóa
  và tối đa 16; chỉ lấy tên file khóa qua metadata, không mở nội dung.
- Retry tối đa 2 (3 lượt), đổi khóa/backoff, astra → sol cho readonly gặp 503,
  nghỉ khóa 10 phút sau 3 lỗi 429 liên tiếp; lưu cooldown qua restart.
- Timeout fake kill/reap được kiểm; timeout thật giữ blocked và dừng giao mới
  chờ PM xác minh cây tiến trình. Đây là giới hạn an toàn có chủ ý của P1 vì
  launcher thật chạy tách qua Task Scheduler; không nhận là đã kiểm kill-tree.
- QUEUE.json/QUEUE.md, SU-KIEN.log, heartbeat 60 giây, lock độc quyền, lưu
  launching trước spawn để tránh giao trùng khi crash; restart chặn worker cũ.
- Snapshot ngân sách UTC tối đa 300 giây, chặn 400 USD/ngày, 1.500 USD tích lũy
  bằng snapshot + dự phòng bảo thủ. [CHƯA KIỂM] Đồng bộ dashboard/chi phí thực;
  dự phòng không phải hard cap provider và không chặn worker đã chạy vượt dự phòng.
- `README.md`: lệnh kiểm, cách PM vận hành riêng, schema/giới hạn và xử lý lock.
  P2 (gộp tự động, bảng hiệu quả) không nằm trong lần này.

## Bằng chứng kiểm thử

Lệnh: `python -I JX1_OPS/TOOLS/dispatcher/test_dispatcher.py`.

Kết quả chạy cuối: `Ran 11 tests`, `OK` (exit 0);
`CLI 5 fake tasks: {"states": {"done": 5}, "scan_errors": []}`.
Test sinh fixture/STATE riêng trong thư mục dispatcher rồi tự dọn.

Đã kiểm dry-run không tạo STATE; 5 worker đồng thời/giới hạn 3 mỗi khóa;
dependency, tài nguyên, priority; retry 503 đổi khóa/fallback; timeout hai lượt
rồi blocked; 429 cooldown; bỏ done/task agent khác và chặn metadata lỗi;
không mở file khi khám phá tên khóa; ngân sách thiếu/cũ/trần/dự phòng;
lock độc quyền và restart; đối số launcher qua mock, không thực thi launcher.

Trong tự rà soát đã sửa trước bàn giao: lưu launching trước spawn; giữ dự phòng
khi snapshot mới tới; không nhầm token/output 429/503 thành transport error;
cho phép retry quản lý nội bộ vượt qua `.done` lỗi cũ. Các kiểm thử cuối đạt.
Không gặp lỗi chạy lệnh/test cần thử lại hoặc lỗi quyền truy cập.

## Chưa xác minh và bước PM

[CHƯA KIỂM] Hai task thật; Codex/provider; Scheduled Task launch/stop và cây con;
đọc log Codex thật; đường dẫn binary trong launcher; monitor heartbeat bên ngoài.
Launcher chưa hỗ trợ `--skip-git-repo-check`, dispatcher giữ nguyên giao diện có
sẵn, không giả nhận đã truyền cờ này. PM duyệt prompt/ngân sách, dry-run allowlist,
rồi chạy hai task thật sau; không bật VM hoặc chạy exe game/server để kiểm.

## Trạng thái bàn giao

DONE trong phạm vi P1 và kiểm offline. Không build dự án/game vì không liên quan
và không được yêu cầu. Chỉ tạo/sửa vùng dispatcher, báo cáo E-13 và mục kết quả
task được task yêu cầu rõ. Commit SHA: chưa có (không tạo commit trong lượt này).
Chưa push: task không yêu cầu công bố; không dùng mạng theo ràng buộc người dùng.
