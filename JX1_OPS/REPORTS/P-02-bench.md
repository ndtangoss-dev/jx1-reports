# P-02 — Bộ đo chuẩn một lệnh

Ngày: 2026-11-17. Trạng thái cuối: **PARTIAL** — nội dung và test offline **DONE**; stage/commit **BLOCKED**. Đo thật **chưa kiểm**.

## Worker kiểm tra trước

- Đã đọc task tại worktree `D:\JX-wt\P-02`; `git status --short --branch` xác nhận đúng nhánh `task/P-02-codex`, Git ban đầu sạch.
- Task có `backlog_ref: P-02`, tiêu chí xong và lệnh unittest cụ thể. Thư mục bench chưa có khi bắt đầu; đã tạo mới.
- Mã chỉ trong `JX1_OPS/TOOLS/bench/`; một báo cáo này trong `JX1_OPS/REPORTS/`. Cập nhật kết quả `JX1_OPS/TASKS/P-02.md` theo yêu cầu trực tiếp của người dùng.
- Nguồn `C:\Jx1CocoV3` chỉ đọc. Không chạy exe game/server, không kết nối VM/SQL/server; không sửa canonical, quyền, credential hoặc Git config.

## Cách chạy

Không cần thư viện ngoài, dùng Python 3.10 trở lên. Từ worktree:

```powershell
python -I JX1_OPS/TOOLS/bench/jx1_bench.py
```

Mặc định đọc `sample_metrics.json` bên cạnh script; đường dẫn không phụ thuộc current directory. Chạy dữ liệu đã xuất về file cục bộ:

```powershell
python -I JX1_OPS/TOOLS/bench/jx1_bench.py --input JX1_OPS/TOOLS/bench/sample_metrics.json --json
```

Hai lệnh đều chỉ phân tích file; không tự thu thập, chạy collector hay mở kết nối. File mẫu là **dữ liệu giả lập**, không phải số đo gs001 hoặc client thật. Không dùng file nguồn/log nhạy cảm làm artifact commit.

## Mã và hợp đồng dữ liệu

| File/trường | Nội dung |
|---|---|
| `jx1_bench.py` | CLI, kiểm tra target/schema, tính tick/băng thông/FPS; exit 0 khi hợp lệ, 2 nếu input bị từ chối |
| `sample_metrics.json` | Fixture `sample_kind: synthetic_offline`; bốn mẫu tick, bốn snapshot mạng và ba cửa sổ FPS |
| `test_jx1_bench.py` | 12 unittest chạy offline |
| `.gitignore` | Loại bytecode/cache Python khỏi tập file Git trong bench |
| `target` | Bắt buộc đúng `{"name":"JX-Test-36","ip":"192.168.56.150"}` |
| `tick_samples` | Danh sách object có `tick_ms`: một thời lượng tick gs001 đã được chuẩn hóa sang ms trên mỗi mẫu |
| `network_mode: cumulative` | Snapshot cùng **một interface guest**, có `time_s` là thời gian đo tương đối tăng nghiêm ngặt, `rx_bytes`/`tx_bytes` là byte cộng dồn; cần ít nhất hai snapshot |
| `network_mode: interval` | Nếu collector đã lấy hiệu số: mỗi object có `rx_bytes`/`tx_bytes` trong cửa sổ và `interval_s > 0`; phải khai báo mode rõ ràng |
| `frame_samples` | Mỗi cửa sổ có đúng một trong `frames` hoặc `fps`, luôn có `interval_s > 0` |
| `--input` | Chỉ file cục bộ UTF-8/UTF-8 BOM; đường dẫn UNC/network bị chặn trước khi mở file |

Quy ước tính:

- Tick trung bình = tổng thời lượng tick / số mẫu; p95 nội suy tuyến tính trên vị trí `(n - 1) × 0.95`.
- Băng thông = `8 × tổng byte hiệu số / tổng giây / 1,000,000` Mbps. Fixture RX từ 50,000,000 đến 54,500,000 byte trong 4.5 giây cho 8 Mbps; TX tương ứng 4 Mbps. Không cộng trực tiếp các giá trị counter cộng dồn và không lấy trung bình số học các tốc độ có cửa sổ khác nhau.
- Counter giảm/reset/wrap hoặc thời gian lặp/đi lùi bị từ chối; cần tách lần đo mới. Không tự sửa counter hoặc bỏ mẫu.
- FPS trung bình = tổng frame / tổng giây; với input fps thì quy đổi frame = fps × giây. Min và p05 là thống kê trên **FPS từng cửa sổ**, không phải frame time hay “1% low”.
- Băng thông là toàn interface guest, chưa phân bổ cho riêng tiến trình gs001. Không gộp nhiều interface hoặc nhiều swapchain client vào cùng chuỗi.
- Reject series rỗng, giá trị âm/phi số/NaN/Infinity và interval không dương. Giá trị 0 hợp lệ cho chuỗi không có lưu lượng/frame.

Rào chắn Main VM: từ chối chuỗi chứa `192.168.1.50` trong đường dẫn input, key hoặc value của payload. Ngoài ra target chỉ nhận đúng VM thử. Đây là khóa input của analyzer offline; không phải phép đo hay chứng minh cô lập mạng runtime.

## Kiểm chứng đã chạy

Lệnh bắt buộc, sau thay đổi mã cuối cùng:

```text
python -I -m unittest discover -s JX1_OPS/TOOLS/bench -v
Ran 12 tests in 0.259s

OK
```

Các test xác nhận công thức có trọng số thời gian, hiệu số counter, reset/bad time, mode và baseline bắt buộc, chặn target/Main VM ở metadata và đường dẫn trước file read, schema lỗi, UTF-8 BOM, JSON lỗi, CLI exit 2 không in bảng dở, CLI bảng/JSON chạy từ thư mục khác. Lượt đầu 4 test cũng pass; sau rà soát đã bổ sung counter cộng dồn và tăng lên 12 test, kết quả trên là lượt cuối.

Lệnh một dòng đã chạy riêng, exit 0:

```text
target: JX-Test-36 (192.168.56.150)
chi so                | gia tri | don vi | so mau
----------------------+---------+--------+-------
gs001 tick trung binh | 51.00   | ms     | 4
gs001 tick p95        | 53.70   | ms     | 4
guest RX              | 8.00    | Mbps   | 4
guest TX              | 4.00    | Mbps   | 4
guest tong            | 12.00   | Mbps   | 4
client FPS trung binh | 59.00   | FPS    | 3
client FPS thap nhat  | 58.00   | FPS    | 3
client FPS p05        | 58.10   | FPS    | 3
```

## Lỗi đã gặp, cách xử lý và giới hạn

| Sự việc | Cách đã thử/kết quả | Còn tồn tại |
|---|---|---|
| Bench chưa tồn tại, `Get-ChildItem` báo không tìm thấy path | Tạo mới đúng thư mục được giao | Không |
| `rg : The term 'rg' is not recognized` | Chuyển sang `git ls-files` và PowerShell, không cài công cụ | Không ảnh hưởng kết quả |
| `collect_guest_metrics.ps1` / `fetch_tick.ps1` không tìm thấy trong lượt đọc nguồn | Tìm theo đúng tên; hai đường dẫn gốc `C:\Jx1CocoV3\experiments`, `C:\Jx1CocoV3\server-resource` trả MISSING; không sao chép/chạy script khác | Adapter với output collector thực tế **chưa kiểm**; không khẳng định script không tồn tại ở mọi vị trí/nhánh khác |
| `apply_patch`: `Failed to write file ...` (3 lần) | Ghi trực tiếp bằng PowerShell UTF-8 trong workspace thành công | Không |
| Soạn cập nhật task gặp `Khong tim thay cac muc ket qua task`; một lần gọi JS dùng `Buffer` không có; một lần literal JS/PowerShell báo `SyntaxError` | Sửa cách ghép literal/here-string; ghi nội dung thành công, đọc/diff xác nhận | Không |
| Xóa `__pycache__` bị `blocked by policy` (2 lần) | Không thử xóa thêm; giữ cache do unittest tạo, thêm ignore Python và dùng danh sách stage cụ thể | Cache còn local, không thuộc tập commit |
| Wrapper kiểm whitespace cho file mới coi exit 1 của `git diff --no-index --check` là lỗi | Diff có khác biệt với NUL nên exit 1 dù output kiểm whitespace trống; đã sửa phân loại kết quả, không sửa file chỉ vì exit 1 | Không |
| Stage Git thất bại | `git add -- ...` trả `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/P-02/index.lock': Permission denied` | **BLOCKED**: metadata ngoài writable root; không đổi quyền/config, không dựng Git metadata thay thế |

## Chưa kiểm

- Collector tick thực tế và ý nghĩa trường tick do gs001 cung cấp: **chưa kiểm**. Không giả định schema JSON đã tương thích trực tiếp với script chưa đọc được.
- Counter/interface mạng guest và nguồn đếm frame/FPS client thật: **chưa kiểm**.
- Đo trên JX-Test-36, runtime gs001/client, VM/SQL/server/mạng: **chưa kiểm**.
- Build/game test: **chưa kiểm**, ngoài phạm vi “chỉ soạn và test phân tích bằng dữ liệu mẫu”.
- Không có bằng chứng đo runtime từ fixture; Python thực tế của phiên đã chạy suite nêu trên.

## Commit và bước tiếp theo

**BỊ CHẶN – CHƯA PUSH.** Chưa stage, chưa tạo commit; **chưa có commit SHA hoặc link GitHub**. Không chạy push vì người dùng chỉ yêu cầu commit. Nguyên nhân còn tồn tại là quyền ghi index Git ngoài workspace; không phải lỗi test.

Các file local được giữ để PM gộp. Trong phiên có quyền hợp lệ trên metadata Git, PM kiểm tra/stage đúng tập sau và commit trên `task/P-02-codex`:

```powershell
git add -- JX1_OPS/TOOLS/bench/.gitignore JX1_OPS/TOOLS/bench/__init__.py JX1_OPS/TOOLS/bench/jx1_bench.py JX1_OPS/TOOLS/bench/sample_metrics.json JX1_OPS/TOOLS/bench/test_jx1_bench.py JX1_OPS/REPORTS/P-02-bench.md JX1_OPS/TASKS/P-02.md
git commit -m "P-02 Them bo do tick bang thong FPS va test offline"
```

Khi có task runtime được duyệt riêng: tái dùng collector nguồn nếu lấy được, chuẩn hóa output về hợp đồng trên, chọn interface/process/khung đo đúng và thử trên JX-Test-36; giữ khóa Main VM. Không chạy bước này trong P-02.
