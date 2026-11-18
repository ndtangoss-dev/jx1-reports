# Đề xuất thử client (xin chủ duyệt) — CHƯA THỰC HIỆN CA NÀO

Đợt #168, 18/11/2026. Lấy từ `REPORTS/N-06.md` §7. Mọi ca đều chưa chạy; đây chỉ là các ca ít rủi ro nhất để chủ cân nhắc.

**Chung cho cả 5 ca:** dùng LDPlayer + APK bản A (ghi phiên bản/SHA-256 APK và exe), VM thử `JX-Test-36`, hai tài khoản chuyên thử TEST-A/TEST-B (bí danh kế hoạch, chưa chắc đã tồn tại; không ghi mật khẩu vào báo cáo). Không đổi cấu hình server ở C01–C03. Chủ duyệt riêng việc mở CDN/forwarder cho LDPlayer nếu cần.

| Ca | Mục đích | Cần gì | Các bước | Hoàn tác | Rủi ro |
|---|---|---|---|---|---|
| **C01** đường chuẩn | Có bằng chứng thật cho chuỗi đăng nhập: khu → login → danh sách nhân vật → vào thế giới | LDPlayer + APK, TEST-A, chuỗi server đang lên | Đăng nhập, chọn nhân vật, vào game, ghi 5 mốc giao diện, rồi thoát bình thường | Thoát game, kiểm online/khóa nhân vật | Thấp. Chỉ tạo một phiên. |
| **C03** đích permit | Xác nhận cổng thật client nối sau khi đăng nhập (56732 không phải gameplay; không giả định 51189/56766) | Ngay trong lần chạy C01; chỉ đọc cổng nối | Đối chiếu địa chỉ/cổng permit với listener gs001 | Không có | Thấp. Chỉ quan sát. |
| **C02** lỗi phân tầng | Biết người chơi thấy mã/thông báo gì khi sai thông tin, thiếu quyền, lệch version | TEST-A, một tài khoản test hết hạn do chủ cấp trạng thái | Mỗi lỗi thử 1 lần, ghi mã/thông báo | Không đổi DB; nếu bị khóa tài khoản thì chủ mở lại | Thấp-vừa: giới hạn số lần để khỏi kích hoạt cơ chế khóa. |
| **C04** Notify all player | Xem tin Announcer hiện ở đâu trên client | C01 đạt; hai client online; câu ASCII ngắn | Bấm Send ở Bishop một lần (một GS), quan sát cả hai client | Không cần; tin chỉ hiện | Vừa: mã nguồn có đặt lại timer vòng GS; theo dõi, không dùng kiểu có dấu `*` (đuổi người). |
| **C05** tiếng Việt | Xem chữ Việt có dấu hiển thị ra sao | C04 đạt | Gửi một câu Việt có dấu, ngắn (xa giới hạn 260) | Không cần | Thấp. Chữ có thể vỡ mã. |

**Không đề xuất lúc này:** C07–C13 (chuyển GS, Goddess gián đoạn, tắt PaySys/Relay, Announcer dấu `*`, root 7777): chạm dữ liệu nhân vật hoặc tiến trình server, cần backup và duyệt riêng.

**Cần chủ quyết:** có cho thử C01+C03 trước không (rủi ro thấp nhất), rồi C02, C04, C05. Quyết qua Chat.
