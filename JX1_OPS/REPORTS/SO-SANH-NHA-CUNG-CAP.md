# So sánh nhà cung cấp cho tiểu yêu: Gemini miễn phí và xingchi (đợt #178, 18/11/2026)

**TÓM TẮT 5 DÒNG**
1. Gemini miễn phí chạy được về kỹ thuật: Codex nối qua LiteLLM (127.0.0.1:4000) và gọi được mô hình.
2. Nhưng gói miễn phí của khóa này chỉ cho **20 lượt gọi mỗi ngày cho mỗi mô hình** (`GenerateRequestsPerDayPerProjectPerModel-FreeTier`, giá trị 20). Một tiểu yêu đọc việc cần hàng chục lượt, nên 3 việc đầu tiên đã dùng hết hạn mức.
3. Kết quả chạy 1 song song: R-06a, R-07a, K-03a đều **thất bại** (exit 1, 7–9 lần 429 mỗi việc, 0 báo cáo mới). Google báo thử lại sau khoảng 17 giờ.
4. Theo luật "không lách hạn mức, không đổi khóa/tạo dự án khác", thuộc hạ **không chạy** các mức 2, 4, 7 song song (chắc chắn cũng hụt). Gemini miễn phí **không dùng được làm đường chính hay dự phòng thực tế** cho tiểu yêu; xingchi vẫn là đường chính. Không chuyển Tổng quản sang Gemini.
5. Cần Chat quyết: bỏ hẳn nhánh Gemini miễn phí, hay chờ chủ cân nhắc gói trả phí (ngoài phạm vi đã duyệt).

Cần tôi quyết định: không (chờ Chat quyết hướng).

## Đã làm
| Bước | Kết quả |
|---|---|
| Cài LiteLLM trong `D:\JX-keys\venv` (ngoài kho, không đụng Python hệ thống) | Được. Lần đầu bị ngắt giữa chừng, cài lại bằng `--force-reinstall` rồi mới import được |
| Chạy proxy `127.0.0.1:4000` | Phải đặt khóa chủ (`LITELLM_MASTER_KEY`) thì proxy mới khởi động; khóa ngẫu nhiên lưu `D:\JX-keys\litellm_master.txt`, không vào kho |
| Mô hình | `gemini-2.5-flash` trả 404 "không còn cho người dùng mới". Dùng `gemini-3-flash-preview` (hoạt động) và `gemini-3.5-flash-lite`. Các bản `gemini-3.5/3.6/3.7/3.8-flash` trả 503 (quá tải) lúc thử |
| Thử một lượt nhỏ qua `/v1/responses` | Đạt: `status=completed`, lite 7 giây |
| Bộ so sánh `-Parallel 1`, 3 việc đọc | Thất bại như trên. Thời gian 437–597 giây mỗi việc, phần lớn là LiteLLM/Codex thử lại sau 429 |

## Bảng đo
| Chỉ số | Gemini miễn phí (`gemini-3-flash-preview`) | xingchi (`gpt-6.1-sol`, đã gộp trước đó) |
|---|---|---|
| Việc xong | 0/3 | 3/3 (exit=0) |
| Báo cáo | không có bản mới | R-06a 8,7 KB; R-07a 9,0 KB; K-03a 36,9 KB |
| Lần 429 | 7, 9, 8 | không đo ở đợt này |
| `turn.failed` | 1 mỗi việc | không đo |
| Tổng thời gian | 559 s, 437 s, 597 s (hỏng) | [chưa đo lại cùng bộ; số từ tệp .pid không đáng tin] |
| Trần song song | không có ý nghĩa: hạn mức ngày đã cạn ở mức 1 | chưa đo trong đợt này |

## Điều chưa kiểm tra
- Chưa biết gói trả phí hay mô hình khác (lite) đủ cho tiểu yêu: lite có hạn mức riêng nhưng chưa thử bộ 3 việc trên lite.
- Chưa so độ đủ nội dung vì Gemini không ra báo cáo.
- Bản lite thử một lượt nhỏ đạt, nhưng không có bằng chứng gọi công cụ ổn định.

## Dữ liệu và khóa
Chỉ gửi 3 prompt đọc không nhạy cảm. Đã quét: khóa Gemini không có trong kho và không có trong log chạy (0 khớp). Khóa nằm ở `D:\JX-keys\gemini.txt` (ngoài kho).

## Hoàn tác
Đã dừng LiteLLM. Muốn xóa hẳn: xóa `D:\JX-keys\venv`, `codex-home-gemini`, `litellm_master.txt`, `litellm.out/err`; thu hồi khóa trong AI Studio.

## Sửa trong TOOLS/nha-cung-cap
`litellm_gemini.yaml`: đổi tên mô hình sang 3.x (ghi UTF-8 không BOM, BOM làm LiteLLM hỏng); `so_sanh.ps1`: dùng khóa chủ LiteLLM thay chuỗi 'local'.
