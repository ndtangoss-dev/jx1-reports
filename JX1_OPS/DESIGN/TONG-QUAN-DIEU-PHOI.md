# Lớp điều phối giữa Sonnet và đám tiểu yêu ("Tổng quản") - thiết kế (Chat, 17/11 12:50)

## Kết luận
CÓ hiệu quả hơn. Nút thắt hiện tại (theo Sonnet và số đo dashboard: ~1,4 worker thực chạy trên 4 khóa) là khâu GIAO VIỆC qua Sonnet. Thêm một lớp tự động (chương trình, không phải mô hình) lo phần máy móc: xếp hàng, giao, canh, thử lại, báo. Sonnet chỉ còn soạn task và duyệt kết quả.
Lợi thêm: Sonnet chạm trần/giới hạn tuần thì hàng đợi vẫn chạy (khác hiện tại: Sonnet dừng = Codex dừng).

## Hai tầng
1. Tổng quản (chương trình, Python/PowerShell, Task Scheduler, chạy 24/7, KHÔNG tốn token): đọc hàng đợi, giao việc, canh, thử lại, ghi trạng thái.
2. Trợ lý astra (mô hình, tùy chọn, chỉ khi A-11b đạt): từ mô tả 3 dòng soạn file task đúng mẫu; tóm tắt báo cáo thành TÓM TẮT cho Sonnet. Sonnet kiểm lại file task trước khi vào hàng đợi (T4 trong A-11 đã đạt).

## Hàng đợi = thư mục TASKS/ (đã có mẫu front matter: id, agent, branch, worktree, depends_on, level, vung_file, tai_nguyen)
Thêm các trường: `model` (sol|astra), `effort`, `timeout_s` (mặc định 900, đọc-tóm tắt 400), `retry` (mặc định 2), `priority` (1-5), `readonly` (true/false), `key_pool` (any|ten-khoa).
Trạng thái trong tệp trạng thái riêng STATE/QUEUE.json (không sửa file task): ready → running → done | failed | blocked | needs_review.

## Quy tắc của Tổng quản
1. Mỗi 20 giây quét TASKS/: task `status: active`, mọi `depends_on` đã `done`, tài nguyên (`tai_nguyen`) không xung đột, worktree chưa dùng → xếp hàng theo priority rồi tuổi.
2. Chọn khe trống: mỗi khóa ≤3 worker, tổng ≤ số khóa×3 (tối đa 16 theo Q-41), chọn khóa ít tải nhất; `chay_codex.ps1` với JX_CODEX_KEY=<tên khóa>, --model, effort, --skip-git-repo-check.
3. Canh: cờ .done, quá `timeout_s` thì kill và đánh `failed(timeout)`; đọc log tìm 429/503/stream disconnected → thử lại với backoff (30 s, 2 phút, 10 phút), đổi khóa khi thử lại; hết `retry` thì `blocked`, ghi nguyên nhân. astra 503 → tạm đổi sang sol với việc đọc-tóm tắt.
4. Hoàn tất: task `readonly` (khảo sát, báo cáo): tự commit báo cáo vào nhánh task và gộp vào jx1-ops (fast-forward/rebase) nếu không xung đột; task sửa mã: dừng ở `needs_review` (Sonnet/Chat duyệt rồi gộp). Không bao giờ push main, không đụng Main VM.
5. Ngân sách: đọc dashboard hoặc cộng token từ log; dừng giao mới khi tổng ≥ 400 USD/ngày hoặc chi tích lũy ≥ 1.500 USD (Q-41); báo vào TRANG-THAI.
6. Giám sát chính nó: ghi nhịp tim mỗi phút vào STATE/QUEUE.heartbeat; Sonnet/Chat thấy ngừng >5 phút thì báo; Task Scheduler tự khởi động lại.

## Đầu ra cho người
- STATE/QUEUE.md (bảng: id, trạng thái, khóa, giờ giao/xong, giây, token, 429, thử lại), cập nhật mỗi lần đổi.
- Mỗi 30 phút: bảng hiệu quả (#041) tự tính (đồng thời trung bình, task/giờ, % cache, % lỗi, thời gian rảnh) - Sonnet chỉ chép vào chat.
- Sự kiện quan trọng (task xong, blocked, hết ngân sách) ghi một dòng vào STATE/SU-KIEN.log để monitor của Sonnet đọc.

## Vai Sonnet sau khi có Tổng quản
Soạn/duyệt task, gộp task sửa mã, giải quyết blocked, đọc TÓM TẮT, quyết định hướng. KHÔNG còn: tự chạy lệnh giao, ngồi canh .done, thử lại tay.

## Rủi ro và cách chặn
- Lỗi chương trình làm giao sai/đốt tiền: thử với task giả trước (chay_codex.ps1 có chế độ worker giả), trần chi cứng, danh sách task cho phép tự chạy (chỉ `readonly` tự gộp).
- Xung đột gộp: mỗi task một worktree/nhánh riêng, task sửa mã vào needs_review.
- Khóa bị khóa/hết hạn mức: mỗi khóa có bộ đếm lỗi; 3 lỗi 429 liên tiếp thì khóa nghỉ 10 phút.
- Mã bí mật: giá trị khóa chỉ đọc từ C:\Users\PC\.jx1keys, không ghi log.

## Giai đoạn
P1 (hôm nay, Codex 1-2 task): quét + giao + timeout + thử lại + QUEUE.md + worker giả kiểm.
P2: gộp tự động cho task readonly, bảng hiệu quả, tự dừng theo ngân sách.
P3: trợ lý astra soạn task/tóm tắt (sau A-11b).

## P3 - Trợ lý nhanh (Groq) - thêm theo thư #051 — ĐÃ HỦY 17/11 (thư #052, chủ dự án bỏ Groq; giữ làm lịch sử, không làm)
- Gọi HTTP trực tiếp tới Groq (không qua Codex), khóa JX-GROQ đọc từ file ngoài kho; script mẫu `TOOLS/groq_speed.py`.
- Chỉ nhận việc NGẮN, KHÔNG nhạy cảm (tóm tắt báo cáo, soạn task từ mô tả 3 dòng, lọc nhật ký). Cấm mã nguồn jx1-source/nội dung riêng tư; Sonnet kiểm đầu ra trước khi vào hàng đợi.
- Bộ đếm: TPM 8.000 và yêu cầu/ngày 1.000 (header thật), đọc `x-ratelimit-remaining-*` sau mỗi gọi; còn dưới 10% hoặc gặp 429 thì chuyển sang sol/astra qua Dispatcher thường.
- Ưu tiên sau E-13 P1; chưa cài đặt.
