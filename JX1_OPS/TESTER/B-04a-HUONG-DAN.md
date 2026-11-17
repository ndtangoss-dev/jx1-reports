# B-04a — Bộ đo tick, byte theo phiên và CPU (chưa chạy)

Trạng thái: **DRAFT / [CHƯA KIỂM] trên gs001**. Hai script độc lập, không sửa
BOT/TESTER hiện có, không login, không mở socket, không khởi động server,
không đổi visibility.ini. Python chỉ dùng thư viện chuẩn, chạy `python -I`.
Các lệnh dưới đây là hướng dẫn cho PM, **không phải bằng chứng đã chạy**.

## Điều kiện trước khi PM chạy

- Chỉ trong VM thử đã được duyệt, mạng cô lập đúng phạm vi phê duyệt hiện có;
  không Main VM, không máy thật, không Internet, không tự chụp snapshot.
- Server, công cụ capture và tải phải được phê duyệt riêng theo quy trình dự án;
  PM kiểm SHA-256, Defender và log/audit trước khi chạy exe. Bộ này không chạy exe game.
- O-01: **100 bot + 20 người thật** cùng gs001, cùng map/vùng nhìn, hành động,
  nhóm/MaxVisible và lịch tải. Không đổi 20 người thành 20 socket fixture.
  PM ghi bằng chứng dân số ổn định suốt cửa sổ. Thiếu tải: [CHƯA KIỂM].
- `STATE/QUYET-DINH.md` Q-27 dùng 18 Hz cho đánh giá tải. B-01 mục 7 cũng nêu
  18 Hz; chỉ chọn 36 nếu PM xác nhận build/cấu hình thực tế, ghi riêng kết quả.
  Không tự sửa Hz. Ngân sách tick: `1000/Hz` = 55,56 ms hoặc 27,78 ms.
- B-02c mới chứng minh sống ≥207 s, Enabled=0; chưa chứng minh tương đương gốc,
  Enabled=1 Solo hay đủ tải. Fixture B-03 không thay cho dữ liệu này.

## Ma trận và đồng hồ

Tối thiểu 3 lượt lặp đầy đủ, mỗi lượt ba pha: `original` (gốc không bộ lọc),
`disabled` (build visibility, Enabled=0), `enabled` (cùng build, Enabled=1 Solo).
Ví dụ pair_id `o01-r1`, run_id `o01-r1-disabled`; lặp r2/r3, đảo thứ tự pha để
giảm ảnh hưởng cache/thời gian. Không đổi cấu hình giữa một cửa sổ đo.
PM tự thao tác đổi build/Enabled trên bản copy đã duyệt và giữ bản hoàn tác;
script không thực hiện đổi cấu hình hay restart.

Mỗi pha 660 s: warmup `[0,60)`, đo `[60,660)` (600 s). Cố định tài nguyên VM,
build flags, map, vị trí, mật độ Bot, nhóm, phiên bản capture và thao tác tải.
Mọi nguồn dùng **cùng mốc t=0**, không phải tự trừ timestamp dòng đầu mỗi file.
Ghi mốc UTC/offset từng nguồn vào biên bản riêng đã lọc. CPU dùng Stopwatch;
PM đối chiếu mốc mở collector với mốc log/capture, bảo đảm sai lệch ≤1 s.
Không thể đồng bộ/thiếu log toàn cửa sổ: [CHƯA KIỂM], không nội suy.
Disconnect, restart/PID đổi, counter reset, mất capture hoặc dân số đổi:
loại cả pha và chạy lại sau khi có phê duyệt; không ghép hai đời phiên.

## CPU

Script `TOOLS/b04a_cpu.ps1` chỉ đọc một PID đang chạy. PM chọn đúng PID gs001
đã có sẵn trong VM; `-ApprovedTestVm` chỉ là xác nhận của người vận hành,
không phải cơ chế phát hiện VM hay quyền chạy server. Không cần Admin nếu
tài khoản có quyền đọc process. Khi bị từ chối quyền, dừng, không vượt UAC.

```powershell
# CHỈ PM, bên trong VM thử đã duyệt; thay PID bằng PID đã xác nhận.
.\JX1_OPS\TOOLS\b04a_cpu.ps1 -TargetPid 1234 -OutputDirectory '.\measure\r1-disabled-cpu' -ApprovedTestVm
```

Thư mục đầu ra phải mới. `cpu.csv`: `elapsed_s,interval_s,cpu_percent`, mẫu
khoảng 1 s; % CPU = delta CPU process / delta wall / số logical CPU VM ×100.
Không phải CPU tổng VM; một core bận hoàn toàn trên VM 4 core ~25%.
`cpu-meta.json` lưu PID, start UTC, cores, thời gian và COMPLETE/PARTIAL.
Chỉ dùng COMPLETE; giữ file partial để chẩn đoán, không đánh giá PASS.
Python lấy trung bình có trọng số thời gian của các khoảng nằm trọn cửa sổ,
đòi phủ ≥90%; CPU max chỉ là đỉnh của mẫu 1 s, không phải đỉnh tức thời.

## Tick từ log/console

**[CHƯA KIỂM]**: các tài liệu đầu vào không cung cấp dòng log gs001 có thời
gian xử lý từng tick. PM cần xác nhận log/console thật xuất **duration xử lý
mỗi tick (ms)** và timestamp đủ chính xác. Không lấy thời gian giữa hai dòng
console, FPS hoặc thời gian sleep làm tick processing. Nếu chỉ có tick counter,
phải chuẩn bị instrumentation trong task source riêng; không tự sửa gs001 ở đây.
Console export phải có sẵn theo cơ chế đã duyệt; script không hook/inject process.

PM chỉ chuyển các số cần thiết sang file riêng, ví dụ hợp đồng **minh họa**:

```text
elapsed_s=60.000 tick_ms=2.500
elapsed_s=60.055556 tick_ms=3.000
```

File này phải có cùng t=0 với CPU và packet metadata. Regex Python cung cấp
`(?P<elapsed_s>...)`, `(?P<tick_ms>...)`; fullmatch toàn dòng, không eval.
Không có regex mặc định đoán log thật; `--log-encoding` mặc định utf-8-sig,
có thể chỉ định encoding đúng khi PM biết. Parser không sao chép nội dung log
hay dòng lỗi ra CSV/console. Dòng không khớp được đếm `ignored_log_lines`;
PM phải giải thích chúng, không mặc định coi là an toàn/đủ mẫu.
Timestamps phải tăng nghiêm ngặt; ≥90% số tick dự kiến trong cửa sổ mới phân tích.
Kiểm thủ công coverage/gap và semantic vẫn bắt buộc. P95 dùng nearest-rank,
`tick_over_budget_percent` chỉ tính trên mẫu duration xử lý, không chứng minh
nhịp scheduler thực tế; đếm tick cũng không tự chứng minh 18/36 Hz ổn định.

## Byte gói theo phiên

Chọn **một điểm quan sát**, client hoặc server, và một lớp đếm xuyên suốt.
`rx`/`tx` luôn theo **client**. Không cộng cả hai đầu kết nối; không dùng byte
cả NIC để thay cho gs001. Không thu login/handshake/payload/khóa/mật khẩu vào
đầu ra. Nếu capture riêng được phép, giữ nội bộ VM, chỉ xuất metadata; không
commit/upload capture thô, địa chỉ hay mapping danh tính.

Hai cách cấp đầu vào:

1. Counter có sẵn tại transport: đếm đúng byte trả về từ recv và số byte send
   thành công (partial send đếm phần đã gửi), mọi gói kể cả unknown, bỏ auth khỏi
   cửa sổ. Không đếm `len(buffer)` nhiều lần khi retry. Chưa có tích hợp bộ đếm
   vào client/server trong task này; adapter thật **[CHƯA KIỂM]**.
2. Capture đã được phê duyệt: PM xuất metadata từ **một** interface, lọc đúng
   120 kết nối game gs001. Gán alias cho mỗi kết nối ổn định bằng 5-tuple/stream
   và đời kết nối trong mapping riêng nội bộ. Với TCP payload dùng `tcp.len`
   (gồm retransmit nếu chưa dedup); với wire dùng `frame.len` (gồm header/ACK/
   retransmit), không lẫn hai lớp. `wire` là byte frame tại điểm capture, không
   đảm bảo gồm preamble/IFG/FCS. Không thay payload mã hóa bằng plaintext length.
   Đo retransmit cần cùng chính sách giữa các pha; kiểm capture drop và duplicate.

Input metadata cho lệnh `packet-counters`:

```csv
elapsed_s,session_id,direction,bytes
60.100,bot001,rx,128
60.200,human001,tx,24
```

`roster.csv` có đúng một cột `session_id`, đủ 100 alias bot001..bot100 và 20
human001..human020 (không tên tài khoản). Có cả phiên không phát gói để giữ
zero hợp lệ. File events phải đủ toàn cửa sổ và sắp theo elapsed_s không giảm;
`bytes` số nguyên không âm, một dòng/một gói ở lớp đã chọn. Script không thể
tự xác minh capture đủ hay Bot/người thật: PM xác nhận dân số, coverage và
ngữ nghĩa export; không có chứng cứ thì [CHƯA KIỂM], dù CSV có số 0.

```powershell
python -I JX1_OPS/TOOLS/b04a_metrics.py packet-counters --roster '.\measure\roster.csv' --events '.\measure\r1-disabled-events.csv' --out '.\measure\r1-disabled-counters.csv'
```

Hoặc cung cấp trực tiếp counter tích lũy `elapsed_s,session_id,rx_bytes,tx_bytes`
ở đúng hai mép 60 và 660 cho mọi phiên, không reset, cùng lớp đếm. Output trên
cũng theo hợp đồng này: đếm events `<edge`, nên phép trừ bao gồm `[60,660)`.
Byte/s = delta(rx+tx)/600; bit/s = byte/s×8, KiB/s = byte/s÷1024. Tổng server
là tổng 120 phiên tại một đầu; sessions.csv cho biết mức phân bố từng phiên.

## Phân tích và đối chiếu (PM chạy sau khi dữ liệu đầy đủ)

```powershell
python -I JX1_OPS/TOOLS/b04a_metrics.py analyze --run-id o01-r1-disabled --pair-id o01-r1 --variant disabled --hz 18 --tick-log '.\measure\r1-disabled-tick.log' --tick-regex 'elapsed_s=(?P<elapsed_s>\d+(?:\.\d+)?) tick_ms=(?P<tick_ms>\d+(?:\.\d+)?)' --cpu '.\measure\r1-disabled-cpu\cpu.csv' --packets '.\measure\r1-disabled-counters.csv' --byte-basis socket_payload --out '.\measure\r1-disabled-summary'
```

Regex trên chỉ dành cho format minh họa đã chuẩn hóa, không khẳng định format
gs001. Chọn `wire` nếu dữ liệu đếm frame. Chạy tương tự cho `original` và
`enabled`, mỗi pha thư mục mới; so original→disabled và disabled→enabled:

```powershell
python -I JX1_OPS/TOOLS/b04a_metrics.py compare --before '.\measure\r1-original-summary\summary.csv' --after '.\measure\r1-disabled-summary\summary.csv' --out '.\measure\r1-original-disabled.csv'
python -I JX1_OPS/TOOLS/b04a_metrics.py compare --before '.\measure\r1-disabled-summary\summary.csv' --after '.\measure\r1-enabled-summary\summary.csv' --out '.\measure\r1-disabled-enabled.csv'
```

Không ghi đè output. Lỗi dữ liệu/ghi file: exit 2, thông báo loại lỗi đã lọc,
có thể còn thư mục output dở; giữ nguyên, dùng thư mục mới khi làm lại.
Exit 0 chỉ chứng minh tạo CSV, **không phải PASS O-01**; đọc từng status trong
comparison.csv. `CHUA_KIEM` tương ứng [CHƯA KIỂM]. CSV không chứa log gốc.

## Tiêu chí đạt/trượt để PM duyệt

Ngưỡng dưới đây là **đề xuất B-04a**, chưa phải ngưỡng đã được O-01 duyệt.
`compare` mặc định dùng chúng; có tham số override, PM phải ghi ngưỡng trước đo,
không đổi sau khi thấy kết quả. Trước hết phải vượt mọi điều kiện dữ liệu.

| Hạng mục | ĐẠT (đề xuất) | TRƯỢT / [CHƯA KIỂM] |
|---|---|---|
| Điều kiện O-01 | 100 bot + 20 người thật ổn định, đủ 3 cặp lặp, cùng tải | Thiếu bằng chứng/dân số sai: [CHƯA KIỂM] |
| Nguồn/coverage | CPU COMPLETE, cùng t=0 ±1 s, tick xử lý từng vòng, capture đầy đủ không drop, không reset | Thiếu/sai semantic, capture gián đoạn: [CHƯA KIỂM], loại lượt |
| Tick P95 | Tăng ≤5% cho từng cặp, và ≤1000/Hz ms | Vượt một trong hai: TRƯỢT |
| CPU process | Trung bình tăng ≤5 điểm phần trăm (cùng cores VM) | Vượt: TRƯỢT |
| Tổng byte/s | Tăng ≤5% với cùng byte_basis/lớp/chính sách retransmit | Vượt: TRƯỢT; baseline 0: [CHƯA KIỂM] |
| original→disabled | Qua các tiêu chí hiệu năng trên; đối chiếu gói/ảnh riêng như B-01.8.7 | Byte count bằng nhau chưa chứng minh hành vi bằng nhau: [CHƯA KIỂM] nếu thiếu test |
| disabled→enabled | Qua tiêu chí hiệu năng; kiểm gameplay B-03 thật riêng | Hiệu năng không thay kiểm visibility/skill: [CHƯA KIỂM] nếu thiếu test |

Ghi mean/P95/max tick, % quá budget, CPU mean/max, byte/s và từng phiên cho
từng lượt, không gộp để che một lượt trượt. `compare` chỉ đánh giá chỉ số số
học; PM kiểm các điều kiện thủ công và lập kết luận cho cả 3 lượt. Chưa đo
runtime trong B-04a, toàn bộ kết luận hiệu năng thực tế hiện **[CHƯA KIỂM]**.
