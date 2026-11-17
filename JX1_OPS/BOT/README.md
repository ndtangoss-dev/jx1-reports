# E-01 — Client một Bot, thử nghiệm offline

Trạng thái runtime **chưa kiểm**: E-01b bổ sung `worldsync.py`, tách và bỏ qua các record world/NPC/player/skill/item trước `CLIENT_SYNC_END`, rồi gửi ACK 9 byte và CP_LOCK. Bộ tách kiểm toàn bộ frame trước khi trả record, từ chối ID ngoài bảng, độ dài sai/cắt và SYNC_END lặp; không quét tìm byte sync trong dữ liệu. Record phải trọn trong frame; TCP bị chia/gộp được xử lý ở `FrameDecoder`.

Chi tiết bảng độ dài, ID chưa hỗ trợ, hai biến thể ACK và giới hạn ABI: [E-01b-thieu-giao-thuc.md](../REPORTS/E-01b-thieu-giao-thuc.md). Các giới hạn login/gameplay còn lại: [E-01-thieu-giao-thuc.md](../REPORTS/E-01-thieu-giao-thuc.md).

## Chạy offline

Từ gốc worktree, Python 3.9 trở lên, chỉ thư viện chuẩn:

```text
python -I -m unittest discover -s JX1_OPS/BOT -v
python -I JX1_OPS/BOT/cli.py --help
```

CLI không có `--connect` chỉ in hướng dẫn. `-I` hoạt động nhờ nạp package cạnh `cli.py` bằng `importlib`; không cần PYTHONPATH hay pip. Test dùng socket giả trong bộ nhớ, không mở cả socket loopback.

## Giao diện kết nối để kiểm sau

Chỉ dùng khi gs001 trong VM thử đã nạp xong. A-01 ghi nhận kết nối cổng 51189 khi server đang nạp từng gây crash. Lượt E-01 này chưa thực hiện kết nối.

Thiết lập thông tin thử bằng cơ chế biến môi trường của phiên, không ghi vào file/lệnh được lưu trong lịch sử:

| Biến | Ý nghĩa |
| --- | --- |
| `JX_BOT_ACCOUNT` | Tài khoản thử, 1..16 byte |
| `JX_BOT_PASSWORD` | Mật khẩu thử, 1..16 byte; băm MD5 chữ hoa trong bộ nhớ |
| `JX_BOT_ROLE` | Nhân vật đã có, phải khớp danh sách Bishop |
| `JX_BOT_CLIENT_KEY` | Giá trị khóa client đã đối chiếu với binary thử, uint32; không tự lấy giá trị nhận từ server làm giá trị tin cậy |

Cú pháp dưới đây dùng tên thay thế, không cung cấp giá trị region/map/online chưa kiểm:

```text
python -I JX1_OPS/BOT/cli.py --connect --host 192.168.56.150 --region REGION_DA_XAC_NHAN --enter-map MAP_DA_XAC_NHAN --observed-online SO_ONLINE
```

Các tùy chọn `--run X Y MAP`, `--skill ID X Y`, `--sit` hoặc `--stand` chỉ được gửi sau bắt tay sync thành công. Skill dùng tọa độ MPS; `X=-1` nghĩa là `Y` là NPC ID theo `NpcSkillCommand`. Không tự chọn mục tiêu, skill hay tọa độ. Sau hành động, `--seconds` quy định thời gian đứng yên và trả lời ping. Tốc độ gửi hành động tối đa 18 lần/giây. Chưa xác minh server đã thực hiện hành động.

Chỉ cho phép IPv4 literal `192.168.56.150`, cổng Bishop 56722 và gs001 51189; `--host` là tham số được kiểm, không mở rộng quyền ra VM khác. Main VM `192.168.1.50` bị chặn trước khi mở socket, kể cả khi Bishop redirect tới đó. Không DNS/IPv6/dạng địa chỉ số nguyên.

Mỗi phiên chỉ có một Bot. `--observed-online` phải là 0..99 trước khi thêm Bot, theo mức tối đa 100 của task. Đây là số người vận hành cung cấp; chưa có gói đo online hay cơ chế giữ chỗ nguyên tử để bảo đảm giới hạn toàn server khi người khác đồng thời đăng nhập.

Profile wire là little-endian Windows, pack(1), int/uint/BOOL 32 bit, bool 1 byte, GUID giữ nguyên 16 byte. Riêng luồng thế giới nhận dùng layout **header GS**: normal hiện tại 55 byte và NPC normal 227 byte; client Cocos khai báo tương ứng 31/223 byte. Không tự dò hoặc fallback ABI theo byte trong payload. Chưa xác minh profile này với binary. ASCII là mặc định cho chuỗi; `--encoding` chỉ dùng khi đã xác minh encoding runtime. Không suy encoding runtime từ encoding source.

Không lưu payload, mật khẩu, MD5, GUID hay khóa phiên. Các literal tài khoản/khóa trong test là dữ liệu tổng hợp offline. CLI đóng socket khi lỗi và không tự đăng nhập lại.

## E-10 — Tạo role và logout offline

Hợp đồng và vector: [E-07-goi-tao-nhan-vat-logout.md](../REPORTS/E-07-goi-tao-nhan-vat-logout.md).
`packets.new_player(name, gender, series, native_place, region)` trả payload
rõ C2S 69: header 14 byte + gender/series/map LE16 + tên byte + NUL.
`name` là `bytes` 6..16 byte theo giới hạn Bishop; bên gọi chịu trách nhiệm
codec và bộ lọc tên. Gender/series chỉ kiểm độ rộng BYTE, map kiểm uint16,
region kiểm uint32 >0; giá trị được runtime chấp nhận **[CHƯA KIỂM]**.
Identity và bLeave đặt 0; bLeave là chuẩn hóa BOT vì client nguồn không gán.

`packets.new_player_response(plaintext)` nhận đúng 66 byte ID 157, trả bool
ở byte 65; bỏ toàn bộ trường tên có tail chưa khởi tạo. Không dùng tên để
khớp request, không đoán mã lỗi. ID này dùng chung create/delete: bên gọi
phải đang chờ create trên Bishop. `packets.role_list` kiểm ID 55,
`nDataLen=1+67*N`, count, tổng độ dài và tên NUL; Level là một BYTE.
Các API nhận đúng một payload đã bỏ framing/XOR; không tự tách bundle Bishop.

Ví dụ payload offline: `packets.new_player(b"BotAbc", 0, 0, 53, 1)` khớp
vector 25 byte E-07; giá trị này chỉ là fixture. API chưa ghép vào luồng
login hay CLI tạo nhân vật. E-07 ghi create thành công đi thẳng permit/game,
không push role list mới; không tự gửi select-role hoặc login lại sau create.
Role list sau re-login thật, ABI/binary, tên có dấu và DB bền vững **[CHƯA KIỂM]**.

`Session.logout()` dùng cùng cleanup với `close()`: chặn hành động bằng
trạng thái CLOSED, đóng game trước rồi Bishop còn sót, giải phóng tham chiếu
và dữ liệu phiên. Channel chặn I/O sau close, bỏ pending/frame dở và trạng
thái XOR. Đóng lặp là no-op; OSError vẫn được báo sau khi thử đóng cả hai.
Thứ tự hai kênh là chính sách cleanup BOT; E-07 không chứng minh thứ tự TCP
FIN/RST runtime. Không có thread nền trong Session hiện tại.
Logout tạo **0 application byte**, không gửi frame rỗng hoặc gói save nội bộ,
không chờ ACK 56/sentinel 791030. Xác nhận lưu DB **[CHƯA KIỂM]**.

Test `test_roles_logout.py` dùng nguyên vector E-07 và socket giả; chạy cùng
lệnh unittest offline phía trên. Không cần VM, DB, exe hoặc kết nối loopback.

## E-02 — Vòng săn offline

`behavior.py` cung cấp `decode_record`, `attack_target`, `Hunt.feed` và
`Hunt.step`. Dùng cùng package `jx1bot` như CLI/test hiện có; không cần pip.
Module không mở socket, không gọi Session/CLI và không tự gửi các lệnh trả ra.
`feed` nhận một frame plaintext đã bỏ framing/XOR, kiểm toàn frame trước khi
cập nhật bảng `npcs` theo wire UINT ID. Các ID ngoài hành vi nhưng nằm trong
bảng `worldsync` được tách và bỏ qua. Profile duy nhất là GS 227 byte cho
S2C 77, không đoán/fallback Cocos 223 byte; ABI binary [CHƯA KIỂM].

Ví dụ API trong ứng dụng đã nạp package (giá trị tầm/thời gian chỉ minh họa):

```python
from jx1bot.behavior import Hunt

hunt = Hunt(("offline-session", 1, 1), search_range=500,
            attack_range=20, action_interval=1)
hunt.feed(plaintext_frame)  # vector 69/76/77/91/92, không phải capture mạng
action = hunt.step(x=1000, y=2000, map_id=1, now=0,
                   skill_id=7, eligible_ids={0x12345678})
# action là None hoặc Action(kind="run"/"attack", target_id=..., payload=...).
```

Bên gọi cung cấp vị trí quan sát bằng MPS, map ID, thời gian monotonic không
giảm, skill ID có level>0 trong danh sách S2C 69, và allowlist `eligible_ids`
đã được xác định là quái hợp lệ. Không mặc định mọi kind_normal đều thù địch.
Chọn gần nhất trong `search_range`, hòa khoảng cách lấy ID nhỏ hơn; chỉ dùng
NPC có kind_normal từ 76, không chết, không doing death/revive. Không tin
field nKind của 77 vì sender khảo sát chưa gán. ID vượt 0x7FFFFFFF vẫn lưu
UINT nhưng không chọn/gửi đánh vì handler C2S nhận Y signed và từ chối Y âm.

Ngoài `attack_range` trả RUN tới tọa độ NPC, trong tầm trả C2S 77 với X=-1,
Y=wire ID; mỗi lần tối đa một lệnh, cách nhau `action_interval`. RUN không
tự cập nhật vị trí BOT; cần vị trí quan sát mới để chuyển sang đánh. Tầm và
cooldown do bên gọi chọn, giá trị runtime [CHƯA KIỂM]. Không hardcode skill 7
từ fixture. Thay danh sách skill bằng 69 rỗng sẽ chặn hành động tiếp theo.

91 chỉ lưu vị trí/phản ứng hurt theo frame, không suy damage. Chỉ 92 xác nhận
dead, giữ tombstone kể cả khi chưa thấy spawn, không hồi sinh bởi snapshot
76/77 trễ. `target_deaths` ghi mỗi target đang chọn tối đa một lần/context;
không xác nhận BOT gây chết, không phải kill counter. Không có sequence hay
timestamp trên wire để nhận biết death stale trong cùng context [CHƯA KIỂM].
`reset_context` xóa NPC/skill/target/timer khi đổi map/phiên hoặc đã xác định
vòng đời ID mới; bên gọi phải chặn dữ liệu context cũ, không tự suy respawn.
Mất NPC/ra khỏi vùng nhìn không được coi là chết; xử lý remove/TTL chưa có.

Tên 76 giữ byte thô, tên 92 chỉ đọc trước NUL, không dùng tail bất định;
encoding tên thật [CHƯA KIỂM]. HP chỉ là ước lượng max×ratio/1000, ratio=0
không xác nhận chết; giới hạn pipeline INT/HP lớn và các thang trị khác của
E-08 vẫn [CHƯA KIỂM]. `nLifeYu` không phải lượng HP thiếu và không được dùng.
Hồi máu: **[CHƯA KIỂM] TODO** — chưa đủ packet/điều kiện hồi máu; `heal()`
báo `ProtocolError`, không dựng gói SIT/item/skill giả định.

Vòng săn độc lập với `population`: bên gọi có thể coi đang theo target là bận,
nhưng chưa có executor/ACK, đồng bộ busy hoặc tích hợp runtime giữa hai module.
Kiểm tra bằng `python -I -m unittest discover -s JX1_OPS/BOT -v`.
