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

## E-05b — full_cycle

```text
python -I JX1_OPS/TESTER/run.py --scenario full_cycle --bots bot01..bot05 --host 127.0.0.1 --port PORT_MAY_CHU_GIA --out JX1_OPS/REPORTS/TEST --workers 5
```

Chỉ dùng fixture `test_full_cycle.cycle_server`, khác giao thức hội thoại của
fixture smoke. Mỗi bot có hai phiên Bishop/game liên tiếp. Kịch bản dùng API
`packets`/`Channel` cho login/role list/permit, `Session.poll/run/hold/skill/close`
cho game. Không dùng `Session.login` vì API đó gắn guard VM; giữ guard nguyên.
Permit vẫn được validate theo đích logic BOT, nhưng socket luôn mở đúng cổng
loopback trong Config; không mở địa chỉ permit. Nhân vật, map, tọa độ, skill,
NPC đều là dữ liệu fixture; mật khẩu ngẫu nhiên chỉ ở RAM, không đọc credential
thật và không log payload auth/GUID/khóa. Giá trị sync tổng hợp lấy từ cổng fixture.

`full_cycle` có 10 bước theo thứ tự:

| Bước | Hành vi offline / giới hạn |
| --- | --- |
| login | Kiểm login response và role list bằng API BOT |
| create_character | BỎ QUA nếu đã có; nếu chưa có, ghi thiếu request/response tạo nhân vật |
| enter_game | SELECT_ROLE, permit, LOGIC_LOGIN, poll tới IN_GAME |
| walk_30s | Gửi RUN một lần, hold đủ 30 s; chưa chứng minh nhân vật di chuyển liên tục hay tới đích |
| attack_one | Gửi một SKILL tới một NPC fixture; chưa chứng minh hit/kill |
| verify_kill | BỎ QUA: BOT chỉ tách/bỏ qua NPC/death/skill, chưa giải mã kết quả chiến đấu |
| logout | Đóng socket BOT; BỎ QUA xác nhận logout vì thiếu request/response ứng dụng |
| reenter | Login và sync lại; BỎ QUA nếu nhân vật chưa được tạo |
| verify_role | So sánh tên/giới tính/hệ/level trong role list trước/sau; khác là FAIL |
| verify_persistence | BỎ QUA: chưa có snapshot/giải mã toàn bộ trạng thái và xác nhận lưu |

Khi chưa có nhân vật, login PASS, 9 bước sau BỎ QUA có lý do; không gửi gói tạo
nhân vật suy đoán. Phiên giả bình thường: 6 PASS, 4 BỎ QUA/bot. Exit 0 có thể
có BỎ QUA, không có nghĩa toàn bộ gameplay đã được kiểm. Test CLI chạy hai bot
song song với 30 s thật (không rút ngắn thời gian); thời hạn bước đi là 35 s.
Thông tin nhân vật còn nguyên trên gs001 thật: **[CHƯA KIỂM]**.
