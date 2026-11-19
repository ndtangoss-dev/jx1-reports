TÓM TẮT 1: [NGUỒN] DONE — hoàn tất kiểm tra tên vai và sinh tên Bot offline theo hợp đồng BOT-02.
TÓM TẮT 2: [NGUỒN] Tên chỉ chữ ASCII dài 6–16 byte, không trùng hoa thường; lý do lỗi ngắn bằng tiếng Việt.
TÓM TẮT 3: [NGUỒN] Đã tạo hàm, 7 kiểm thử offline và báo cáo; đã ghi kết quả vào cuối file task.
TÓM TẮT 4: [CHƯA KIỂM] Lệnh unittest với -I -m không nạp được package trong worktree; hai lệnh thay thế chạy đạt 7/7.
TÓM TẮT 5: [NGUỒN] Không commit/push theo yêu cầu; chỉ chạy kiểm thử offline, không build, exe/VM hay mạng.

# BOT-02 — Kiểm tên vai Bot trước khi tạo (offline)

Loại: công cụ
Chủ đề: Kiểm tra tên vai theo quy tắc task và sinh tên Bot không trùng trước khi tạo.
Từ khóa: tên vai, ten_vai, kiem_ten, gen_ten, ASCII, Bot, BOT-02
Trạng thái: DONE — triển khai hoàn tất, kiểm thử offline đạt; lưu ý lệnh gọi unittest nguyên trạng không tương thích đường dẫn của Python cô lập.
Độ phủ: đã phủ 3 trên 3 tệp thuộc vung_file: mã, kiểm thử và báo cáo.
Liên quan: JX1_OPS/TASKS/BOT-02.md; JX1_OPS/STATE/TESTER/KIEN-THUC/tao-nhan-vat/NUT-GIAO-DIEN.md; JX1_OPS/TOOLS/bot_tao_role.py; JX1_OPS/DESIGN/CHUAN-BAO-CAO.md
Cần tôi quyết định: không

## Sơ đồ

~~~mermaid
flowchart TD
    A[kiem_ten: nhận tên và danh sách đã có] --> B{Tên kiểu chuỗi?}
    B -- Không --> X[Từ chối, trả lý do tiếng Việt]
    B -- Có --> C{Dài 6–16 byte?}
    C -- Không --> X
    C -- Có --> D{Chỉ gồm chữ ASCII?}
    D -- Không --> X
    D -- Có --> E{Trùng không phân biệt hoa thường?}
    E -- Có --> X
    E -- Không --> F[Chấp nhận tên]
    G[gen_ten: kiểm tiền tố và thứ tự n] --> H[Sinh hậu tố chỉ gồm chữ cái]
    H --> I{Đã có tên này?}
    I -- Có --> H
    I -- Không --> J[Trả tên Bot duy nhất]
~~~

## Phạm vi và độ phủ

| Phần tử | Trạng thái | Bằng chứng |
|---|---|---|
| kiem_ten — kiểm kiểu, độ dài, chữ ASCII, trùng không phân biệt hoa thường và lý do lỗi | Đã phủ | JX1_OPS/BOT/ten_vai.py:41; JX1_OPS/BOT/ten_vai.py:55; JX1_OPS/BOT/ten_vai.py:63 |
| gen_ten — sinh tên chữ ASCII 6–16 byte và bỏ qua tên đã có | Đã phủ | JX1_OPS/BOT/ten_vai.py:80; JX1_OPS/BOT/ten_vai.py:95; JX1_OPS/BOT/ten_vai.py:102 |
| Kiểm thử các tiêu chí task và nhánh sinh tên | Đã phủ; 7/7 đạt | JX1_OPS/BOT/test_ten_vai.py:7; JX1_OPS/BOT/test_ten_vai.py:12; JX1_OPS/BOT/test_ten_vai.py:25; JX1_OPS/BOT/test_ten_vai.py:33 |
| Báo cáo kết quả trong phạm vi | Đã phủ | JX1_OPS/REPORTS/BOT-02.md |
| Chỉ mục TSV theo khuôn báo cáo | Chưa phủ | Ngoài vung_file; không tạo để giữ phạm vi |

## Giải mã tên

Các tên ví dụ được giữ nguyên; các chuỗi dưới đây dùng ASCII trong UTF-8, không cần giải mã GBK hoặc TCVN3.

| Tên gốc | Mã hóa | Chữ đúng | Nguồn |
|---|---|---|---|
| Cctesterone | ASCII / UTF-8 | Cctesterone | JX1_OPS/TASKS/BOT-02.md:21 |
| T36nv2 | ASCII / UTF-8 | T36nv2 | JX1_OPS/TASKS/BOT-02.md:21 |
| Ts baone | ASCII / UTF-8 | Ts baone | JX1_OPS/TASKS/BOT-02.md:21 |
| Tsbaone | ASCII / UTF-8 | Tsbaone | JX1_OPS/STATE/TESTER/KIEN-THUC/tao-nhan-vat/NUT-GIAO-DIEN.md:20 |
| BOT-02 | ASCII / UTF-8 | BOT-02 | JX1_OPS/TASKS/BOT-02.md:2 |

## Sắp theo cấu trúc game

Không áp dụng cấu trúc phái, nhánh kỹ năng, trang bị, quái, NPC hoặc bản đồ vì đầu vào là chuỗi tên vai. gen_ten sắp thứ tự theo tham số n và bỏ qua tên đã tồn tại.

## Cách triển khai

kiem_ten từ chối kiểu không phải chuỗi; kiểm độ dài UTF-8 6–16 byte; chỉ nhận chữ ASCII; so trùng không phân biệt hoa thường và trả kết quả cùng lý do tiếng Việt. gen_ten kiểm tiền tố/thứ tự, tạo hậu tố chữ cái, kiểm độ dài và tiếp tục qua tên đã có. Bằng chứng: JX1_OPS/BOT/ten_vai.py:41; JX1_OPS/BOT/ten_vai.py:80.

Không chạy JX1_OPS/TOOLS/bot_tao_role.py vì script có thao tác kết nối. Task yêu cầu kiểm thử offline, không yêu cầu gọi server: JX1_OPS/TOOLS/bot_tao_role.py:14.

## Đã xác minh

- Task quy định độ dài 6–16 byte, chỉ chữ ASCII, không trùng hoa thường và các ca kiểm thử: JX1_OPS/TASKS/BOT-02.md:19; JX1_OPS/TASKS/BOT-02.md:21.
- Bảy kiểm thử bao phủ tên hợp lệ, độ dài biên, ký tự/số/khoảng trắng, trùng hoa thường, đầu vào sai và sinh tên: JX1_OPS/BOT/test_ten_vai.py:7; JX1_OPS/BOT/test_ten_vai.py:33.
- Lệnh task python -I -m unittest JX1_OPS.BOT.test_ten_vai -v đã chạy nhưng lỗi trước khi nạp kiểm thử: ModuleNotFoundError: No module named 'JX1_OPS' do Python cô lập không thêm thư mục hiện hành vào đường dẫn import.
- python -m unittest JX1_OPS.BOT.test_ten_vai -v: đạt, 7/7.
- python -I -c "import sys; sys.path.insert(0, r'D:/JX-wt/BOT-02'); import unittest; import JX1_OPS.BOT.test_ten_vai as tests; unittest.main(module=tests, verbosity=2)": đạt, 7/7.
- Lượt thử trung gian phát hiện cách ánh xạ thứ tự n sang hậu tố cần ổn định; sau khi điều chỉnh generator, toàn bộ 7 test đạt.
- rg không khả dụng trong shell; dùng Select-String giới hạn vào các tệp nguồn đã chỉ định, không cài công cụ.
- Không chạy build, exe, VM, client, server hoặc mạng; không xác minh hành vi runtime.

## Chưa xác minh

- Tài liệu nút giao diện ghi bộ lọc client dài 6–24 byte và mô tả quy tắc khác với ràng buộc 6–16 byte, chỉ chữ ASCII của task: JX1_OPS/STATE/TESTER/KIEN-THUC/tao-nhan-vat/NUT-GIAO-DIEN.md:24; đối chiếu với JX1_OPS/TASKS/BOT-02.md:19. Mục này giữ nguyên làm phát hiện; triển khai hiện theo hợp đồng cụ thể của task.
- Tài liệu cũng ghi Tsbaone không có khoảng trắng từng bị UI từ chối nhưng nguyên nhân chưa rõ; task yêu cầu kiểm Ts baone có khoảng trắng: JX1_OPS/STATE/TESTER/KIEN-THUC/tao-nhan-vat/NUT-GIAO-DIEN.md:27; JX1_OPS/TASKS/BOT-02.md:21.
- Chưa chạy lệnh unittest nguyên trạng thành công với -I -m; đã xác minh 7 test bằng hai lệnh nêu trên.
- Tệp nhịp D:/JX-wt/BOT-02.nhip không ghi được do quyền hệ thống từ chối đường dẫn ngoài worktree. Không tạo TSV ngoài phạm vi.

## Bàn giao

Không commit/push theo yêu cầu; PM tổng hợp commit. Báo cáo kết quả task đã cập nhật tại JX1_OPS/TASKS/BOT-02.md. Bước tiếp theo: PM xử lý chỉ mục TSV ngoài phạm vi và cân nhắc khác biệt giữa chính sách 6–16 byte của task với mô tả UI 6–24 byte nếu cần khớp client thực tế.

## Phát hiện khi chuẩn hóa

- NUT-GIAO-DIEN.md:24 mô tả độ dài client 6–24 byte, trong khi task quy định Bot 6–16 byte; chưa xác minh việc giới hạn trong task là chính sách Bot chủ động hay yêu cầu tương đương client.
- Metadata task ở JX1_OPS/TASKS/BOT-02.md:8 ghi nhánh task/BOT-02-ten-vai; git status ban đầu cho nhánh task/BOT-02 như caller chỉ định, nên giữ nguyên nhánh hiện tại.
- Tên Tsbaone và Ts baone khác nhau; không gộp hai trường hợp hoặc đổi kết luận ghi trong tài liệu cũ.
- Chưa tạo chỉ mục TSV vì không thuộc vung_file.
- Ghi chú nhịp ngoài worktree bị hệ thống từ chối; không thay đổi quyền.
- Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
