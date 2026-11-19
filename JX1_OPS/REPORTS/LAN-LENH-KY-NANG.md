# Làn lệnh kỹ năng gs001: vì sao chỉ ~15% lệnh được chạy (thư #277, mục 1)

Người viết: Sonnet A, 19/11/2026. Chỉ đọc mã, chưa sửa gì. Nhãn: THẤY = đọc trực tiếp mã; TÀI LIỆU = báo cáo cũ; CHƯA KIỂM = chưa chạy thử.

## TÓM TẮT 5 DÒNG
1. gs001 bản A2T2 có "làn lệnh" (CmdLane) cho người chơi: MỘT ô hành động (`m_CmdAct`) và MỘT ô di chuyển (`m_CmdMove`) cho mỗi nhân vật. Không có hàng đợi.
2. Lệnh kỹ năng mới tới khi ô đang có kỹ năng cũ thì ghi đè (đếm `skill_over`): đó là 291/525 lệnh lúc chủ đánh 21:49–21:51.
3. Khi nhân vật đang diễn chiêu (`nAI==0`), kỹ năng đang chờ bị bỏ (đếm `busy discard act`) trừ khi `BufferBusy=1`; mặc định là 0: đó là 154/525.
4. Còn lại 80/525 chạy (525-291-154). Kỹ năng chờ quá `TtlActMs` (mặc định 250 ms) cũng bị hủy (`expired_act`).
5. Đòn bẩy cấu hình có sẵn: `Settings\CmdLane.ini` (`BufferBusy`, `TtlActMs`, `Enable`). Sửa mã exe thì KHÔNG cần cho bước đầu. Hiệu quả thật CHƯA KIỂM.

## Bảng chi tiết (diff gốc `docs-analysis/patches/a2-cmdlane/a2-cmdlane.diff`; số dòng là dòng trong diff, trùng khớp mã ở `S/Core/Src/KNpc.cpp:6764-6892` theo `REPORTS/H-13-tick-do-tre-don.md:88`)
| # | Điều | Nhãn | Chỗ |
|---|---|---|---|
| 1 | Mỗi nhân vật có hai ô: `m_CmdMove` (đi/chạy), `m_CmdAct` (kỹ năng/điều khiển) | THẤY | diff:26-27 |
| 2 | Kỹ năng mới: nếu ô act đã có thì `skill_overwritten++`, xóa lệnh di chuyển chờ, rồi ghi đè ô act | THẤY | diff:204-211 |
| 3 | Lệnh điều khiển cứng (ngồi, nhảy, đứng hệ thống...) xóa kỹ năng đang chờ (`skill_cleared_by_ctl`) | THẤY | diff:212-217 |
| 4 | Lệnh đi/chạy tới thì ô move bị thay (`move_superseded`) | THẤY | diff:192-203 |
| 5 | Dừng mềm (SoftStop) bị nuốt nếu kỹ năng đang chờ (`stop_absorbed`) | THẤY | diff:180-191 |
| 6 | Mỗi tick xử lý: kỹ năng chờ quá `TtlActMs` (250) bị hủy; move quá `TtlMoveMs` (120) bị hủy | THẤY | diff:228-235 |
| 7 | Nếu `nAI==0` (đang diễn chiêu): move bị bỏ (`busy_discard_move`); skill bị bỏ (`busy_discard_act`) trừ khi `BufferBusy=1` thì giữ lại (`busy_kept_skill`); hurt/revive vẫn chạy | THẤY | diff:239-261 |
| 8 | Khi rảnh: chạy ô act; nếu có move đi kèm mà chiêu bị từ chối (hồi chiêu...) thì chạy move sau | THẤY | diff:263-285 |
| 9 | Cấu hình đọc MỘT lần từ `\Settings\CmdLane.ini`: Enable (1), TtlActMs (250, kẹp 30–1000), TtlMoveMs (120), BufferBusy (0), Stats (1) | THẤY | diff:84-109 |
| 10 | Tắt hẳn làn: `Enable=0` (về đường cũ `ProcCommandLegacy`) | THẤY | diff:173, 293-303 |
| 11 | Số đo 525/80/291/154 lúc chủ đánh 21:49–21:51 | TÀI LIỆU | `STATE/BAN-GIAO.md:38` |
| 12 | Vì sao đánh thường "chạy sát quái mới ra đòn": client gửi lệnh kỹ năng liên tục, nhưng mỗi lệnh đè lệnh trước; chiêu nào đang diễn thì lệnh kế bị bỏ | GIẢ THUYẾT hợp với #1–#7 | CHƯA KIỂM |

## Điều CHƯA KIỂM
- Exe đang chạy trên Test-36 có đúng bản mã trên không (số đếm trong console khớp tên bộ đếm là chứng cứ gián tiếp).
- `Settings\CmdLane.ini` có tồn tại trên Test-36 không, và đọc từ thư mục nào (H-13:267 ghi "file override chưa xác minh").
- `BufferBusy=1` có làm hết "quái đánh mãi không chết" không, hay chỉ thêm độ trễ (kỹ năng chờ rồi chạy sau chiêu trước, tối đa `TtlActMs`).
- Nguyên nhân tick nặng 40–116 ms lúc nạp nhân vật là chuyện KHÁC, không thuộc làn lệnh.

## Đề xuất (chỉ ở cấu hình Test-36, có `.bak`, hoàn tác bằng chép lại `.bak`)
1. Đặt `BufferBusy=1`, `TtlActMs=400` trong `Settings\CmdLane.ini` của gs001 Test-36; khởi động lại gs001 (cấu hình đọc một lần).
2. Đo lại bằng `CmdLane_stat.log` (delta giữa hai mẫu 60 s) và `jx_net.log` khi chủ chơi vc23.
3. Không sửa exe/mã nguồn server. Nếu cần (vd. nhiều ô kỹ năng) thì ghi [CAN-CHU].
