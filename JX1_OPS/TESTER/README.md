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
Mặc định chỉ chấp nhận literal `127.0.0.1`, cổng 1..65535. Không DNS.
Ngoại lệ opt-in VM thử chỉ dành cho `real_login`, xem E-09a bên dưới.
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
bot rồi bước. Bí mật thật chỉ lấy từ biến môi trường, đăng ký mọi giá trị với
redactor trong bộ nhớ; không đọc/ghi credential vào file, không ghi vào
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

**gs001 thật: [CHƯA KIỂM].** PASS offline không chứng minh login/gameplay thật.
Các BUG/báo cáo mẫu trong `REPORTS/TEST` do fixture tổng hợp, không phải lỗi
đã xác nhận trên gs001. Task E-09a chỉ kiểm loopback, không chạy exe game/server,
không kết nối VM/mạng ngoài.

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

## B-03 — visibility (fixture)

`--scenario visibility --bots bot01` chạy một nhóm gồm hai phiên người chơi
A/B và một phiên Bot trong cùng worker. Mỗi bí danh bổ sung tạo một nhóm ba
phiên độc lập; workers chỉ điều phối số nhóm. Dùng duy nhất fixture
`test_tester.fake_server(3, visibility=True)`; không trỏ vào gs001 thật.

```text
python -I -m unittest discover -s JX1_OPS/TESTER -p test_visibility.py -v
```

Các bước `solo`, `shared_bot_remove`, `group_cap`, `refresh`, `disabled` kiểm
trace nhận theo tiêu chí 1,2,5,6,7 của B-01 mục 8. Parser BOT kiểm ranh giới;
`visibility.NpcView` theo dõi ADD(76), SYNC(77), REMOVE(84). Offset identity là
hợp đồng fixture, **[CHƯA KIỂM] với ABI binary**. RUN có x=phase/y=viewer chỉ
điều khiển script fixture, không phải lệnh đổi nhóm thật. Ba phiên không login
hoặc tạo người chơi trên server. Không ghi mật khẩu/khóa mới, không sửa BOT.

Tiêu chí 2 chỉ kiểm A gửi một SKILL và cả A/B nhận REMOVE cùng Bot; kết quả
kill/death thật **[CHƯA KIỂM]**. Tiêu chí 5 đối chiếu trace MaxVisible=2 rồi =1
(Bot không tính vào trần), chưa kiểm bộ cấp nhóm con server. Tiêu chí 7 so
từng byte hai trace baseline/Enabled=0 fixture, chưa có capture/ảnh gốc thật.
Tiêu chí 3/4 có hàm TODO, trả BỎ QUA và ghi gói/semantic thiếu theo E-07/E-08;
tiêu chí 8 thuộc B-04, **[CHƯA KIỂM]**. Exit 0 có thể chứa BỎ QUA.

## E-09a — real_login (chuẩn bị, chưa chạy VM)

`--scenario real_login` dùng profile codec/packet BOT hiện có, gồm năm bước:
`real_login` kiểm response login; `role` đối chiếu role yêu cầu (thiếu là FAIL,
không tự tạo); `enter_game` kiểm permit rồi LOGIC_LOGIN, SYNC_END/ACK đủ 9 byte
và CP_LOCK; `hold_session` giữ TCP 30 s, xử lý PING khi nhận; `close` đóng TCP.
Không gửi RUN/SKILL và không nhận đóng TCP là logout ứng dụng hay xác nhận lưu.
Không đoán client key, region, map hoặc chọn role đầu tiên.

`Config(..., allow_test_vm=False)` và CLI mặc định vẫn chỉ loopback. Cờ
`--allow-test-vm` chỉ hợp lệ với `real_login`; khi bật, Bishop chỉ được là
literal `192.168.56.150:56722`, permit game phải cùng host và cổng `51189`.
Main VM, host khác, hostname, IPv6, subnet, alias, khoảng trắng và cổng khác
bị chặn trước `socket.create_connection`/DNS. Không có tham số mở rộng allowlist.
Config được kiểm khi tạo và ngay trước mỗi socket; permit không được dùng để
đổi từ loopback sang VM hoặc từ VM về loopback. Các kịch bản `smoke_login`,
`full_cycle`, `visibility` chỉ dùng fixture loopback kể cả qua API trực tiếp.
Với fixture `real_login`, permit phải trả loopback; cho cổng ngẫu nhiên để test.

Thông tin mỗi bot lấy riêng từ biến môi trường (ví dụ tiền tố `JX1_BOT01_`,
tương tự tới BOT05). Không có cờ CLI truyền credential, không đọc file:

| Hậu tố | Bắt buộc / ý nghĩa |
| --- | --- |
| ACCOUNT | Tài khoản theo profile BOT, 1..16 byte |
| PASSWORD | Mật khẩu theo profile BOT, 1..16 byte |
| ROLE | Tên nhân vật có sẵn, 1..63 byte |
| CLIENT_KEY | uint32 đã biết đúng cho phiên; không tự suy/đoán |
| REGION | uint32 >0, cấu hình đăng nhập được xác nhận |
| ENTER_MAP | uint32, cấu hình được xác nhận |
| OBSERVED_ONLINE | Số online quan sát 0..99 trước thêm bot |
| ENCODING | Tùy chọn, mặc định ascii; phải khớp profile/encoding thực |

Số nhận decimal hoặc tiền tố `0x`. Thiếu/sai biến bị FAIL trước mở Bishop.
Biến được đọc ở worker; account/password/role/key cùng giá trị cấu hình được
đăng ký redactor trước validation. Không log payload auth/GUID/key, không ghi
credential vào Config, source, report hoặc BUG. Nạp biến bằng cơ chế bí mật đã
được duyệt; không ghi giá trị vào script/lịch sử shell. Không dùng chung cùng
tài khoản khi chạy nhiều bot. Admission chỉ dựa trên số online được cung cấp,
không tự truy vấn server hay điều phối tổng online giữa các worker.

Task này **không chạy** lệnh opt-in. Việc chạy VM thật cần phạm vi phê duyệt
riêng. Để xem CLI và kiểm offline:

```text
python -I JX1_OPS/TESTER/run.py --help
python -I -m unittest discover -s JX1_OPS/TESTER -p test_real_login.py -v
```

Test chính dùng fixture loopback, credential/GUID sinh ngẫu nhiên trong RAM,
key tổng hợp từ cổng fixture; không đọc credential thật. Test allowlist dùng
mock socket/DNS cho các địa chỉ ngoài loopback. Luồng dương kiểm đủ 30 s và
PING_REPLY; case âm kiểm thiếu role, env, permit sai host/cổng, chế độ CLI sai.
ABI/layout binary, client key thật, login/giữ phiên/gameplay/lưu trên gs001:
**[CHƯA KIỂM]**. Report `real_login` ghi kết quả theo profile BOT tại endpoint
cấu hình; PASS fixture không chứng minh nghiệm thu VM thật.
