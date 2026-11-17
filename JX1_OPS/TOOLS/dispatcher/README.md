# Dispatcher P1b — E-13 / E-13b

Chạy bằng Python chuẩn, không cần cài thư viện. Mặc định chỉ lập kế hoạch,
không ghi STATE và không khởi chạy worker:

```powershell
python -I JX1_OPS/TOOLS/dispatcher/dispatcher.py --dry-run
python -I JX1_OPS/TOOLS/dispatcher/test_dispatcher.py
```

Test tạo dữ liệu tạm ngay trong thư mục dispatcher và tự dọn; chỉ sinh tiến trình
`python -I` làm worker giả. Không đọc khóa thật, không gọi Codex/VM/mạng/Git.
Muốn chạy fixture riêng, tạo TASKS giả có tệp `.fake-tasks-only`, dùng STATE riêng:

```powershell
python -I JX1_OPS/TOOLS/dispatcher/dispatcher.py --fake-worker --tasks-dir <TASKS-gia> --state-dir <STATE-gia> --until-idle --interval 0.1 --max-seconds 30
```

## Giao thật — PM thực hiện riêng, chưa kiểm runtime

Chỉ PM chạy khi đã duyệt prompt/worktree và ngân sách. Bắt buộc
`--run-real --allow-task <ID>` (lặp cho từng task), `--budget-file <snapshot.json>`
và `--probe-url <HTTPS-endpoint>/v1/responses` do PM xác nhận.
Không bỏ allowlist để quét/giao toàn bộ backlog. Công cụ không tự sinh prompt;
cần `<worktree>.prompt.txt` đã duyệt, worktree đúng `<worktree-root>/<ID>`.
Không sửa `chay_codex.ps1`; gọi launcher hiện có với `-Id`, `-PromptFile`,
`-Model`, `-Effort`, env `JX_CODEX_KEY` chỉ là tên khóa. Launcher hiện có mới
chịu trách nhiệm đọc khóa khi PM giao thật. Dispatcher chỉ glob tên `*.txt`
khi lập kế hoạch/giao việc; chỉ hàm thăm dò trong chế độ thật mới đọc nội dung
khóa từ `--keys-dir` (mặc định `C:\Users\PC\.jx1keys`). Không ghi khóa,
response body hoặc chi tiết exception vào STATE/log; không theo HTTP redirect.

Snapshot ngân sách JSON do PM/dashboard cấp, UTF-8, thời gian UTC có timezone:

```json
{"date":"2026-11-17","updated_at":"2026-11-17T12:00:00+00:00","daily_usd":0,"cumulative_usd":0}
```

Snapshot phải cùng ngày UTC, không cũ quá 300 giây. Thiếu/sai/cũ: dừng giao mới.
Trần 400 USD/ngày, 1.500 USD tích lũy; dự phòng mỗi lượt qua front matter
`budget_usd` (mặc định 10 USD). Tổng snapshot + mọi dự phòng + lượt mới phải
nhỏ hơn trần. Dự phòng giữ bảo thủ cả khi worker xong, PM phải đối soát khi
bảo trì trạng thái; không tự xóa QUEUE để giải phóng khi còn worker chạy.
Đây là cổng chặn giao mới, chưa phải giới hạn chi phí cứng của provider;
token chỉ thống kê từ `turn.completed`, không suy tiền từ token.

## Quy tắc và vận hành

- Chỉ task `status: active`, `agent: codex`, tên file trùng `id`, chưa `.done`.
  Ngoại lệ duy nhất: lượt thử lại đang được QUEUE quản lý có `.done` lỗi cũ.
- Front matter hỗ trợ scalar và list inline `[A, B]`, không hỗ trợ YAML nhiều
  dòng/nested; dữ liệu lỗi vào `scan_errors`, không giao. `retry` 0–2 tương ứng
  tối đa 3 lượt; `priority` 1–5 tăng dần rồi tuổi file.
- `depends_on` phải `done` trong QUEUE hoặc có `TASKS/<ID>.done`; task sửa mã
  `needs_review` không tự mở phụ thuộc. Không tự commit/gộp/push (thuộc P2).
- Không trùng worktree/tài nguyên `tai_nguyen`; mỗi khóa tối đa 3, toàn cục
  tối đa `min(16, số khóa * 3)`. `key_pool: any|tên-khóa`.
- 429/503/stream disconnected trong lỗi transport: chờ 30/120 giây cho 2 lượt
  thử lại, ưu tiên đổi khóa. 3 lỗi 429 liên tiếp: khóa nghỉ 600 giây, lưu STATE.
  astra 503 + `readonly: true`: lượt sau dùng sol. Output/usage có số 429/503
  không được coi là lỗi. Lỗi vĩnh viễn hoặc hết lượt: `blocked`.
- Riêng `.done` có `exit=1` và chẩn đoán transport cuối là
  `429 exceeded retry limit` (cũng nhận thứ tự `exceeded retry limit ... 429`):
  chờ 20 giây, không tăng `failures` hay dùng hết `retry`. Từ lần đó, mọi lượt
  giao cách nhau ít nhất 20 giây, kể cả khi đổi khóa; trạng thái giãn giao được
  lưu qua restart. `attempts` vẫn đếm mọi lượt, `rate_limit_retries` đếm riêng.
- Watchdog theo `st_mtime_ns` của `<worktree>.codex.log`: mtime không tăng
  600 giây thì dừng worker; task `readonly: true` dùng 300 giây cho khảo sát
  đọc/tóm tắt. Log chưa xuất hiện cũng tính từ lúc giao. Mtime mới được lưu vào
  QUEUE; hạn chờ dùng đồng hồ monotonic. Watchdog chạy lại tối đa hai lần riêng
  (`watchdog_retries`), ưu tiên khóa ít worker hơn trong `key_pool` được phép.
  Với khóa có cùng tải, ưu tiên đổi khóa. `.done` mới hợp lệ được xử lý trước
  watchdog/timeout, còn `.done` từ lượt trước không kết thúc lượt mới.
- Watchdog thật gọi `Stop-ScheduledTask JX-codex-<ID>` và kiểm tra Scheduled
  Task không còn `Running` trước khi cho chạy lại. Stop lỗi/chưa xác nhận:
  giữ slot/tài nguyên, `blocked`, dừng giao mới để PM xử lý. Không thử stop lặp
  mỗi tick. **[CHƯA KIỂM]** cây tiến trình con thực tế trên Task Scheduler.
- Nếu ít nhất ba worker cùng quá hạn watchdog trong một vòng quét, lưu
  `provider_incident.active`, dừng các worker đứng và tạm ngừng mọi giao mới.
  Thăm dò đầu sau 120 giây, rồi mỗi 120 giây: POST nhỏ `/v1/responses`, model
  `gpt-6.1-sol`, `max_output_tokens: 16`, `store: false`, timeout 15 giây,
  User-Agent `codex_cli_rs/0.166.0`. Chỉ response HTTP 200 với
  `status: completed` và không có `error` mới mở lại giao việc ngay trong tick.
  Thăm dò lỗi vẫn giữ trạng thái dừng; không tự thay endpoint/config provider.
  `--fake-worker` mặc định dùng probe giả thất bại; test tiêm hàm giả để hồi phục.
- `STATE/TRANG-THAI.md` có khối `dispatcher-provider` ghi “sự cố nhà cung cấp”
  hoặc đã hồi phục; giữ nguyên nội dung PM bên ngoài khối này. `.seen-all`
  trong STATE là JSON ánh xạ đường dẫn `.done` sang mtime nanosecond: mỗi lần
  mtime đổi phát lại `done-observed` vào `SU-KIEN.log`, kể cả cùng tên, qua restart.
  File `.seen-all` kiểu chỉ lưu tên cũ được chuyển đổi khi thấy marker.
- Timeout giả: kill/reap và thử lại. Timeout thật: Stop-ScheduledTask rồi
  `blocked`, chặn giao mới để PM xác minh cây tiến trình đã hết trước khi reset;
  không tự thử lại khi chưa chắc worker cũ đã chết.
- Mỗi vòng quét mặc định 20 giây; `QUEUE.json`, `QUEUE.md`, `SU-KIEN.log` mỗi
  đổi trạng thái; `QUEUE.heartbeat` mỗi tối đa 60 giây. Dừng vòng chạy sẽ stop
  worker do dispatcher quản lý và ghi blocked. Heartbeat quá 5 phút cần PM kiểm.
- Lock độc quyền `dispatcher.lock`: khi crash giữ lock, PM kiểm PID/Scheduled
  Task trước khi bỏ lock. Sau restart, `running/launching` thành `blocked`,
  chặn giao mới. Không nhận lại worker cũ hoặc chạy trùng. Không có auto-service
  hay tự cài Task Scheduler cho chính dispatcher trong P1.
- Chạy thật kế thừa giới hạn launcher: đường dẫn worktree mặc định `D:\JX-wt`,
  launcher chưa có tham số `--skip-git-repo-check`; không truyền tham số không
  được hỗ trợ. Kiểm runtime hai task thật do PM làm sau E-13.

E-13b được kiểm bằng 26 test offline, gồm worker Python giả có kill/reap thật,
đồng hồ giả cho mốc 300/600/120/20 giây, HTTP/Stop-ScheduledTask đều mock.
Chưa chạy Codex thật, chưa đọc khóa thật, chưa gọi API hoặc điều khiển VM.
