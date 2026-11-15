---
task_id: AMOLX-20261115-01
status: APPROVED
scope: Read-only audit of the newly supplied AMOLX JX1 client source; assess buildability and compatibility with the existing JX1 server. Do not modify AMOLX or the canonical Cocos source.
allowed_paths:
  - TEST_RESULTS/AMOLX-01-client-compatibility.md
---

# JX1-AMOLX-01 — Kiểm tra client AMOLX có tương thích JX1 Server không

## Mục tiêu
Kiểm tra source client AMOLX mới được người dùng cung cấp, xác định:
1. Kiến trúc, engine, phiên bản, cấu trúc source và asset.
2. Có thể build/chạy được trên Windows hoặc Android/LDPlayer 14 không.
3. Giao thức và luồng đăng nhập có tương thích với JX1 Server hiện tại không.
4. Nếu có thể, kiểm thử kết nối và vào game trên môi trường VM thử nghiệm đã được xác định.

## Đường dẫn source AMOLX
`C:\JX1\jx1client-amol-main\jx1client-amol-main`

Working repository của Codex hiện tại là `C:\Jx1CocoV3`. Source AMOLX nằm ngoài repository này.

## Quy tắc truy cập và an toàn — bắt buộc
- Chỉ đọc source AMOLX; tuyệt đối không sửa, đổi tên, di chuyển, xóa hoặc ghi đè bất kỳ tệp nào trong thư mục AMOLX.
- Không sửa hoặc ghi đè client Cocos canonical tại `C:\Jx1CocoV3`.
- Không sửa source, cấu hình, dịch vụ, firewall, dữ liệu hoặc tiến trình của Main VM/server production.
- Không thay đổi sandbox, quyền truy cập, cấu hình bảo mật hoặc chạy lệnh nâng quyền để vượt giới hạn đọc.
- Trước tiên kiểm tra đường dẫn có tồn tại và thử liệt kê/đọc một số tệp văn bản nhỏ bằng quyền hiện có. Nếu sandbox chặn truy cập ngoài workspace, dừng phần kiểm tra source và báo **BỊ CHẶN – SOURCE NGOÀI WORKSPACE**; không tự ý thêm quyền hoặc thay đổi cấu hình Dispatcher.
- Không thực thi file lạ, script build tùy tiện, installer hoặc executable từ source trước khi kiểm tra nội dung và nguồn gốc. Không chạy game executable nếu chưa xác định rõ binary và môi trường thử nghiệm.
- Không dùng credential/token/mật khẩu trong source hoặc đưa thông tin nhạy cảm vào báo cáo.
- Không kết nối thử tới Main VM. Chỉ được kết nối VM thử nghiệm khi đã xác định chắc chắn địa chỉ/môi trường thử từ tài liệu JX1 hiện có; nếu không rõ thì chỉ phân tích tĩnh và báo thiếu điều kiện.
- Không tự ý tạo bản sao toàn bộ source hoặc asset dung lượng lớn. Chỉ đề xuất cách tạo bản thử riêng nếu cần sửa; phải xin duyệt trước khi thực hiện patch.

## Tối ưu thời gian và token
- Đọc `AGENTS.md` hiện có và các chỉ thị/workflow liên quan trước khi làm.
- Đọc `WORKFLOW_JX1.md`, `00_LATEST_STATUS.md`, `TEST_RESULTS/72-jx1-task-dispatcher-va-font.md` và các báo cáo giao thức/client/server có liên quan.
- Không đọc lại toàn bộ 66 báo cáo. Dùng tìm kiếm theo tên hàm, protocol, login, server list, player select, network packet và build config; chỉ mở các báo cáo liên quan trực tiếp.
- Ưu tiên kiểm kê có chọn lọc: README, CMakeLists, project Android/Windows, cấu hình mạng, mã login/server selection, packet serialization, thư viện và asset manifest.
- Dùng reasoning Medium cho kiểm kê/build thông thường; chỉ tăng High cho điểm giao thức khó. Không dùng Max xuyên suốt.
- Tránh lặp lại lệnh hoặc thử build nhiều lần nếu log đã có kết quả rõ.

## Giai đoạn A — Kiểm kê và khả năng build
1. Xác nhận source tồn tại, dung lượng, số lượng tệp và cấu trúc thư mục.
2. Đọc README, CMakeLists, cấu hình project, build scripts và các tệp khai báo dependency.
3. Xác định engine/framework và phiên bản; ngôn ngữ; NDK/SDK/toolchain; target Windows/Android; ABI 32/64-bit.
4. Kiểm kê asset theo loại và định dạng, không giải nén hàng loạt.
5. Xác định các entry point, scene khởi động, login UI, server list, chọn nhân vật và network layer.
6. Kiểm tra build prerequisites hiện có. Chỉ build nếu lệnh build đã được xác định an toàn, không chạy script không rõ nội dung và không ghi vào thư mục source gốc. Nếu cần build output, dùng thư mục build riêng ngoài source và chỉ khi quyền hiện có cho phép.

## Giai đoạn B — Đối chiếu JX1 Server
Dựa trên báo cáo JX1 đã có và code client AMOLX, đối chiếu:
- Login/authentication và cách gửi tài khoản.
- Server list, IP/port, giao thức TCP/UDP và handshake.
- Packet framing, byte order, mã hóa, nén, checksum và version negotiation nếu có.
- Chọn nhân vật, vào game, map/scene loading.
- Đồng bộ vị trí, trạng thái nhân vật, NPC/quái, combat và các packet thiết yếu.
- Khác biệt giữa protocol AMOLX và protocol của client Cocos đang hoạt động.

Với từng mục, trích đường dẫn file/hàm và bằng chứng. Phân loại:
**TƯƠNG THÍCH / CẦN ĐIỀU CHỈNH / KHÔNG TƯƠNG THÍCH / CHƯA ĐỦ BẰNG CHỨNG**.
Không suy luận tương thích chỉ từ tên file hoặc việc cùng dùng Cocos.

## Giai đoạn C — Build và chạy thử (chỉ khi đủ điều kiện an toàn)
- Nếu toolchain sẵn có và build không làm thay đổi source, build ra thư mục riêng.
- Nếu tạo được APK, cài lên LDPlayer 14 và ghi lại package name, version, ABI, launch result, crash/logcat.
- Chỉ thử login/kết nối với VM thử nghiệm đã được xác nhận. Không dùng Main VM.
- Nếu thiếu tài khoản test, server test hoặc cấu hình endpoint, không tự tạo credential hay đổi server; ghi rõ BỊ CHẶN.
- Ghi lại bước thực tế đạt được: build, install, launch, login, character select, enter map. Không gộp các bước này thành một kết quả chung.

## Bàn giao
Tạo báo cáo tiếng Việt tại:
`TEST_RESULTS/AMOLX-01-client-compatibility.md`

Báo cáo phải gồm:
1. Tóm tắt kết luận và mức độ tin cậy.
2. Kiến trúc/engine/toolchain/ABI và cấu trúc source.
3. Danh sách tệp/hàm quan trọng đã kiểm tra.
4. Bảng đối chiếu protocol và luồng đăng nhập với JX1 server.
5. Kết quả build, LDPlayer 14 và kết nối server theo từng bước.
6. Log/lỗi/bằng chứng và lệnh đã chạy.
7. Phần bị chặn, chưa kiểm thử, giả thuyết và rủi ro.
8. Kết luận theo một trong ba hướng: **Có thể dùng ngay / Có thể chuyển đổi sau khi sửa / Không phù hợp**, kèm lý do.
9. Đề xuất bước tiếp theo nhỏ nhất, không tự triển khai patch.

Chỉ ghi kết quả đã có bằng chứng. Không tuyên bố hoàn thành nếu chỉ mới kiểm kê hoặc build thành công.
