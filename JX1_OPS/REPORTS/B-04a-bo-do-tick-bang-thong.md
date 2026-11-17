## TÓM TẮT 5 DÒNG
1. DONE trong phạm vi B-04a: viết bộ đo dự thảo và hướng dẫn cho PM; chưa chạy script đo, không truy cập mạng/VM, không chạy exe game/server.
2. Thêm PowerShell lấy CPU một PID gs001 có sẵn và Python phân tích tick log, đếm byte metadata theo phiên, so sánh CSV original/Enabled=0/Enabled=1.
3. Hướng dẫn quy định O-01 100 bot + 20 người thật, warmup 60 s + đo 600 s, ba lượt lặp, dữ liệu cùng mốc và không ghép phiên sau reset.
4. Chỉ kiểm cú pháp: Python AST và PowerShell AST đều OK; nguồn tick thật, adapter byte/capture, runtime đủ tải và kết luận hiệu năng [CHƯA KIỂM].
5. Ngưỡng tăng 5% tick/byte, 5 điểm phần trăm CPU là đề xuất chờ PM duyệt; chưa tạo commit, chưa push vì chỉ bàn giao local và yêu cầu không mạng thật.

# B-04a — Script đo tick và băng thông gs001 (chưa chạy)

## Phạm vi và bằng chứng đầu vào

- Nhánh kiểm tra một lần trước ghi: `task/B-04a`; trạng thái ban đầu chỉ có
  `?? JX1_OPS/TASKS/B-04a.md`. Giữ nội dung task có sẵn, chỉ thêm `## Kết quả`
  theo yêu cầu chính task, không sửa frontmatter hay file ngoài phạm vi.
- `DESIGN/B-01-LOC-HIEN-THI.md:65–66`, mục 7: ViewerCanSee chạy theo người
  xem × nguồn × gói; yêu cầu đo trước/sau, nêu 18 Hz. Tiêu chí 8 ở dòng 76
  chỉ ghi “không tăng đáng kể”, không có ngưỡng số đã duyệt.
- `REPORTS/B-02c-build-va-thu.md`, dòng tóm tắt 3/5: Enabled=0 sống ≥207 s;
  so gói/ảnh gốc, Enabled=1 và tải 100 bot + 20 người chưa kiểm.
- Đọc phần STATE liên quan bằng tìm có giới hạn, cùng các quyết định/bàn giao:
  `STATE/QUYET-DINH.md` Q-27 ghi mọi con số đo tải Bot tính ở 18 Hz;
  `STATE/TRANG-THAI.md:199` còn cần B-04. Không lấy quyền PM trong tài liệu
  cũ để mở rộng quyền worker. Điều kiện 100 bot + 20 người theo task;
  chưa có bằng chứng đạt điều kiện đó trong lượt này.
- Đọc `TESTER/visibility.py`, `TESTER/README.md` để giữ bộ đo độc lập khỏi
  fixture hiện tại; không tái sử dụng socket fixture làm số liệu gs001.

## Đầu ra

| File | Nội dung |
|---|---|
| `TOOLS/b04a_cpu.ps1` | Đọc PID gs001/gs001_nohe đang chạy, mẫu CPU ~1 s, Stopwatch, chuẩn hóa theo logical CPU VM; CSV + metadata COMPLETE/PARTIAL; không khởi động server |
| `TOOLS/b04a_metrics.py` | CLI offline `packet-counters`, `analyze`, `compare`; chỉ stdlib; xuất sessions.csv, summary.csv và comparison CSV |
| `TESTER/B-04a-HUONG-DAN.md` | Điều kiện PM chạy, ma trận đo, hợp đồng log/counter/capture, lệnh mẫu, giới hạn và bảng tiêu chí |

Tick lấy duration xử lý mỗi vòng từ log/console có semantic do PM xác nhận;
regex bắt buộc có nhóm elapsed_s/tick_ms, không đoán định dạng gs001.
Byte tính theo phiên ổn định và hướng client, hỗ trợ counter có sẵn hoặc đếm
metadata gói do PM xuất từ một điểm capture đã duyệt; không lưu payload.
Không có tích hợp instrumentation vào source/client/server ở task này.
Không tự thu capture, không cài tool, không sửa mạng/quyền/cấu hình game.

CPU thiếu coverage, tick thiếu <90% mẫu dự kiến, O-01 sai số lượng, mép
counter thiếu/lặp hoặc bộ đếm giảm sẽ bị từ chối; baseline zero không được
coi là PASS tăng trưởng. Các điều kiện nguồn thật, đồng hồ, capture drop,
người thật, CPU metadata COMPLETE và tải giữ nguyên cần PM kiểm thủ công.
Output không ghi đè; CLI lỗi exit 2 chỉ in loại lỗi, không phản chiếu log gốc.
Exit 0 là tạo CSV thành công, không phải chứng nhận O-01.

## Kiểm chứng đã thực hiện

| Kiểm tra | Kết quả |
|---|---|
| `python -I -c` gọi `ast.parse` trên đúng `TOOLS/b04a_metrics.py` | exit 0, `Python AST: OK (no script execution)` |
| PowerShell `Language.Parser.ParseFile` trên đúng `TOOLS/b04a_cpu.ps1` | exit 0, `PowerShell AST: OK (no script execution)` |
| Thực thi collector, analyzer, compare, self-test/fixture | **Chưa chạy** theo yêu cầu script chưa chạy |
| Build gs001, kết nối mạng/VM, chạy game/server | **Không thực hiện** theo giới hạn task |

AST chỉ chứng minh cú pháp, không chứng minh logic số học hoặc hoạt động thực
tế. Không tạo CSV đo giả để trình bày như runtime. Khi PM được phép chạy,
thực hiện đúng hướng dẫn và giữ kết quả nội bộ; báo cáo này không chứa secret.

## Lỗi, xử lý và phần còn lại

- Lần đọc task đầu bằng encoding mặc định của PowerShell hiển thị sai dấu;
  các lần đọc tài liệu tiếp theo dùng UTF8 và output UTF8. Không ghi lại file
  gốc để chữa lỗi hiển thị; nội dung cũ được giữ.
- `rg` không có: lỗi `The term 'rg' is not recognized as the name of a cmdlet`.
  Chuyển một lần sang `Select-String` trong đúng `STATE/*.md`, đã lấy được
  phần liên quan; không cài tool hoặc quét rộng repository.
- Blocker hoàn thành phần viết script: không có. Phần chạy thật [CHƯA KIỂM]:
  cần PM xác nhận log tick mỗi vòng, export byte theo phiên/capture đầy đủ,
  đồng hồ chung, load 100 bot + 20 người và ngưỡng nghiệm thu trước khi đo.
- Nhánh thử 36 Hz không tự thay cho chuẩn 18 Hz; không so chéo Hz. Tick
  processing không thay chứng cứ scheduler cadence; số byte bằng nhau không
  thay kiểm gói/ảnh Enabled=0 hoặc kiểm gameplay Enabled=1.

## Trạng thái bàn giao

**DONE** — hoàn tất thiết kế/viết script chưa chạy, hướng dẫn, bảng tiêu chí
và báo cáo trong phạm vi B-04a. Hiệu năng runtime **[CHƯA KIỂM]**.

Commit SHA: **chưa tạo**, bàn giao file local; task không yêu cầu commit.
Push/link GitHub: **chưa thực hiện**, yêu cầu lượt này cấm mạng thật; không
thử push, không có lỗi GitHub và không thay credential/config.
