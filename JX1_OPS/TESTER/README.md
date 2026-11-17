# E-05a — Khung tester offline

Python 3.9+, chỉ thư viện chuẩn. Mỗi bot giữ state trong một process `spawn`
riêng. `--workers 1` chạy tuần tự (mặc định), `2..5` chạy song song. Bước FAIL
dừng bot đó, các bước còn lại BỎ QUA; bot khác tiếp tục. Watchdog hủy process
quá hạn, không để hàm treo chạy nền. Có sai số điều phối khoảng một vòng poll
5 ms và tối đa hai lần chờ dừng process 100 ms; startup process có hạn riêng 10s.
Không có cơ chế Python bảo đảm thời gian thực cứng khi hệ điều hành bị treo.
Không gọi API có process spawn từ stdin/REPL trên Windows; dùng file có guard
`if __name__ == "__main__":` hoặc CLI. `python -I -c` dùng được với callable
cấp module đã import, không phải callable định nghĩa ngay trong chuỗi lệnh.

## Chạy và kiểm thử

Từ gốc worktree:

```text
python -I -m unittest discover -s JX1_OPS/TESTER -v
python -I -m unittest discover -s JX1_OPS/BOT -v
python -I JX1_OPS/TESTER/run.py --help
python -I JX1_OPS/TESTER/run.py --scenario smoke_login --bots bot01..bot05 --host 127.0.0.1 --port PORT_MAY_CHU_GIA --out JX1_OPS/REPORTS/TEST --workers 5
```

`PORT_MAY_CHU_GIA` phải là số cổng fixture đang nghe; không tự chạy gs001.
Thiếu/sai cấu hình: usage và exit 2. Có FAIL: exit 1; tất cả PASS/BỎ QUA: exit 0.
Chỉ chấp nhận IPv4 literal `127.0.0.1`, cổng 1..65535. Không DNS, VM hay server thật.
`smoke_login` không cần tài khoản, mật khẩu hay khóa thật.

Cú pháp module có cùng CLI khi Python đã tìm thấy package:

```text
python -m JX1_OPS.TESTER.run --scenario smoke_login --bots bot01..bot05 --host 127.0.0.1 --port PORT_MAY_CHU_GIA --out JX1_OPS/REPORTS/TEST
```

**Giới hạn câu lệnh của task:** `python -I -m JX1_OPS.TESTER.run ...` không thể
resolve package chưa cài trong checkout: `-I` bỏ cwd và PYTHONPATH trước khi
module được nạp. Không thể bootstrap từ bên trong module chưa tìm thấy.
Không cài package/sửa Python hoặc cấu hình ngoài phạm vi. Cách chạy file trực
tiếp ở trên giữ `-I`; bootstrap thêm duy nhất đường dẫn tuyệt đối từ `__file__`,
không lấy cwd. Test discover theo đường dẫn vẫn chạy nguyên lệnh yêu cầu.

## API kịch bản

`core.Scenario(name, steps)` chứa các `core.Step(name, run, expected, timeout,
severity="major")`. Tên scenario dùng `[a-z][a-z0-9_]*`; tên bước không trùng.
`run(context)` là hàm cấp module có thể pickle trên Windows, nhận đúng một bot:

- `context.bot`: bí danh bot01..bot05; `context.config`: host/port/secrets.
- `context.state`: state chỉ của bot, tồn tại giữa các bước; đối tượng có
  `close()` được đóng khi kết thúc. Timeout hủy process và socket thuộc process.
- Hàm tự kiểm kỳ vọng: raise hoặc trả `False` để FAIL; `None`/`True` để PASS;
  raise `SkipStep` để BỎ QUA. Không coi chuỗi `expected` là assertion tự động.
- `context.log(text)` tối đa 20 dòng x 400 ký tự/bước. stdout/stderr tự do bị
  bỏ, không ghi file và không phát ra console.
- `context.packet("gửi" hoặc "nhận", payload)` tối đa 4 gói/bước, 256 byte/gói;
  giữ hướng, ID đầu payload, độ dài gốc; body che bằng `00` **trước IPC**.
  Đây là hex đã che, không phải capture có thể phát lại. Không ghi raw key,
  GUID, password, login payload hay body unknown.

`run_scenario(scenario, bots, Config(...), workers=1)` trả `Result` theo thứ tự
bot rồi bước. Cấu hình bí mật thật khi E-05b nối sau phải lấy từ môi trường/tệp
ngoài kho và truyền mọi giá trị vào `Config.secrets` trong bộ nhớ; không ghi vào
source/CLI/report. Redactor tự nhận các biến môi trường có tên chứa
PASSWORD/PASSWD/SECRET/TOKEN/KEY/ACCOUNT/ROLE, che giá trị, hex, MD5 và biến thể
uint32 của khóa, cùng cặp nhãn bí mật. Hàm kịch bản phải đăng ký bí mật tự đọc
qua `Config.secrets`; không log bí mật tự biến đổi/encoding khác ngoài hợp đồng.

`smoke_login` dùng `BOT.Channel.handshake` và `BOT.Session.poll` với vector
ACCOUNT_BEGIN, WORLD_SYNC/PING/END tổng hợp từ `BOT/test_bot.py` và
`BOT/test_worldsync.py`. Không gọi `Session.login`, không đổi guard đích BOT.
Fixture `fake_server` trong test mở socket loopback, kiểm PING_REPLY, ACK END
9 byte, CP_LOCK và đóng socket. Không có server thật trong khung này.

## Báo cáo và BUG

`reporting.write_report` ghi `<yyyy-mm-dd>-<scenario>.md`; chạy lại cùng ngày
giữ bản cũ, thêm hậu tố `-2`, `-3`... Bảng bot x bước có PASS/FAIL/BỎ QUA và
giây từng bước; chi tiết gồm log và gói lỗi đã che. Nhánh/commit lấy Git chỉ đọc,
có timeout; không đọc credential hay tự đổi cấu hình Git.

FAIL sinh BUG-NNN tăng từ số lớn nhất hiện có. Fingerprint SHA-256 dựa trên
scenario + tên bước + thông báo đã che. BUG có dòng `Status: OPEN` sẽ được
khử trùng và thêm `tái hiện lần N` với bot/nhánh/commit; đóng bằng đổi thành
`Status: CLOSED` để lần sau sinh BUG mới. Mỗi BUG ghi bước tái hiện, kỳ vọng,
thực tế, log, độ nặng blocker/major/minor, bot, nhánh/commit.

`.tester.lock` chống hai writer dùng cùng thư mục; lượt thứ hai thoát lỗi,
không chờ vô hạn. Nếu host bị tắt đột ngột, người vận hành kiểm tra process
trước khi tự xóa lock cũ. Không ghi đè báo cáo. Không dùng thư mục báo cáo
không tin cậy hoặc chứa symlink.

**gs001 thật: chưa kiểm.** PASS offline không chứng minh login/gameplay thật.
Các BUG/báo cáo mẫu trong `REPORTS/TEST` do fixture tổng hợp, không phải lỗi
đã xác nhận trên gs001. Không chạy exe game/server, không kết nối VM/mạng ngoài.
