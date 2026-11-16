# E-01 — Client một Bot, thử nghiệm offline

Trạng thái **PARTIAL**: codec và phiên theo profile nguồn đã có; chưa phải client đã đăng nhập được server thật. Bộ nhận GS hiện chỉ tách `CLIENT_SYNC_END` và `PING_COMMAND`. Khi nhận các gói đồng bộ thế giới khác, client đóng kết nối và báo ID chưa hỗ trợ. Không bỏ qua hay quét tìm byte sync bên trong payload.

Chi tiết còn thiếu và dẫn nguồn: [E-01-thieu-giao-thuc.md](../REPORTS/E-01-thieu-giao-thuc.md).

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

Profile wire là little-endian Windows, pack(1), int/uint/BOOL 32 bit, bool 1 byte, GUID giữ nguyên 16 byte. ASCII là mặc định cho chuỗi; `--encoding` chỉ dùng khi đã xác minh encoding runtime. Không suy encoding runtime từ encoding source.

Không lưu payload, mật khẩu, MD5, GUID hay khóa phiên. Các literal tài khoản/khóa trong test là dữ liệu tổng hợp offline. CLI đóng socket khi lỗi và không tự đăng nhập lại; thao tác logout có payload tùy biến chưa triển khai.
