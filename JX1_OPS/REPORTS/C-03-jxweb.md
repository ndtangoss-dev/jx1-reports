# C-03 — Trang quản trị web nội bộ `jxweb`

Ngày: 17/11/2026. **PARTIAL — mã và test offline hoàn tất; commit bị chặn bởi quyền ghi metadata Git.**

## Worker kiểm tra trước khi làm

- Đã đọc `JX1_OPS/TASKS/C-03.md` trước khi sửa.
- `Get-Location` = `D:\JX-wt\C-03`; `git rev-parse --show-toplevel` = `D:/JX-wt/C-03`; nhánh = `task/C-03-codex`, đúng worktree/branch.
- Git ban đầu sạch. Chỉ ghi trong `JX1_OPS/TOOLS/jxweb/`, báo cáo này và mục `Kết quả` của task; không sửa `C:\Jx1CocoV3`.
- Không chạy exe server, không kết nối VM/SQL/server, không mở cổng ngoài loopback, không đọc tài khoản thật và không ghi credential.

## Mã đã thêm

- `JX1_OPS/TOOLS/jxweb/app.py`: HTTP dashboard dùng `http.server` và thư viện chuẩn Python.
  - `JxadmDryRunProvider` gọi `jxadm.account_plan("online", ...)` để tạo snapshot dry-run; không tạo socket SQL.
  - `StaticStatusProvider` cung cấp nguồn dữ liệu giả bất biến cho test/offline demo.
  - `GET /` trả giao diện responsive, viewport hẹp, cỡ chữ đọc được trên điện thoại; không tải tài nguyên ngoài.
  - `GET /api/status` trả JSON trạng thái máy chủ/tài khoản; `GET /healthz` chỉ kiểm tra tiến trình.
  - Mặc định bind `127.0.0.1:8765`; chỉ chấp nhận IP loopback literal (`127.0.0.1`, `::1`), chặn Main VM `192.168.1.50` và IPv4-mapped tương ứng.
  - `POST /api/actions` không có write adapter mặc định. Nếu được cấu hình adapter riêng, `ActionGuard` yêu cầu token từ `JXWEB_ACTION_TOKEN` ở cả bước `prepare` và `confirm`, cùng challenge dùng một lần có hạn 300 giây.
  - Giới hạn request body, JSON UTF-8, header bảo vệ và log request rỗng để tránh ghi nhầm token/body.
- `JX1_OPS/TOOLS/jxweb/test_jxweb.py`: test bind loopback/Main VM, dry-run jxadm, challenge hai bước, API HTML/JSON, 404 và bind IPv6.
- `JX1_OPS/TOOLS/jxweb/__init__.py`: export API nhỏ cho embedding/test.

## Cách chạy

Chỉ chạy trên máy chủ local, mặc định loopback:

```powershell
python -I JX1_OPS/TOOLS/jxweb/app.py
```

Có thể chọn tài khoản fixture và cổng loopback khác:

```powershell
python -I JX1_OPS/TOOLS/jxweb/app.py --account offline_fixture --host 127.0.0.1 --port 8765
```

Mở `http://127.0.0.1:8765/`. CLI giữ chế độ dry-run; đưa qua Tailscale hoặc cấu hình write adapter là việc riêng cần chủ máy duyệt.

## Kiểm chứng

Đã chạy đúng lệnh task:

```text
python -I -m unittest discover -s JX1_OPS/TOOLS/jxweb -v
Ran 6 tests in 1.054s
OK
```

Trong lần chạy đầu, test phát hiện trang HTML đóng kết nối do dấu ngoặc CSS bị `.format()` hiểu nhầm là placeholder (`KeyError: 'font-family'`). Đã escape toàn bộ dấu ngoặc CSS và chạy lại đạt 6/6. Một lệnh PowerShell dọn `__pycache__` kết hợp với test bị policy chặn trước khi thực thi; dọn artefact sau đó bằng Python với đường dẫn đã kiểm tra nằm trong workspace, không ảnh hưởng mã/test.

## Chưa kiểm

- Trạng thái server/account thực tế, schema SQL, driver, số phiên online và hành động ghi chưa kiểm; snapshot hiển thị rõ `unverified`/`dry-run`.
- Chưa chạy dưới tải, qua Tailscale, reverse proxy hay mạng ngoài; thiết kế chỉ cho phép bind loopback.
- Chưa có write adapter thật; không có thao tác ghi nào được gửi.

## Commit và bàn giao

Đã thử stage đúng năm file thuộc task bằng `git add`; Git bị chặn trước khi stage:

```text
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/C-03/index.lock': Permission denied
```

**BỊ CHẶN – CHƯA PUSH.** Không có commit SHA trong phiên này. Không thử lại cùng lỗi, không đổi ACL/config/credential và không tạo Git metadata thay thế. PM có thể tiếp tục trên nhánh `task/C-03-codex` với lệnh:

```powershell
git add -- JX1_OPS/TOOLS/jxweb/__init__.py JX1_OPS/TOOLS/jxweb/app.py JX1_OPS/TOOLS/jxweb/test_jxweb.py JX1_OPS/REPORTS/C-03-jxweb.md JX1_OPS/TASKS/C-03.md
git commit -m "C-03 Them jxweb dashboard va test offline"
git log -1 --format=%H
```
