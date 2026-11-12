# JX1_VISUAL — Khu vực nghiên cứu Visual

Khu vực làm việc riêng cho chuyên môn **Visual** của dự án JX1 Cocos V3: định dạng và đường nạp tài nguyên hình ảnh (PAK, SPR), render 2D, camera, animation, UI, độ mượt và chất lượng hình ảnh.

## Vai trò
| Bên | Vai trò |
|---|---|
| ChatGPT | Chuyên gia Visual: đọc báo cáo, phân tích kỹ thuật, đánh giá kết quả, soạn đề xuất nhiệm vụ tiếp theo |
| Claude Code | Lập trình viên/người nghiên cứu trực tiếp trên source: thực hiện nhiệm vụ, kiểm chứng bằng mã nguồn, viết báo cáo |
| Người dùng | Duyệt nhiệm vụ. Claude chỉ làm khi có chỉ thị đã được duyệt |

## Quy trình phối hợp
1. Claude hoàn thành nhiệm vụ và đăng báo cáo vào [`REPORTS/`](REPORTS/).
2. Người dùng thông báo cho ChatGPT.
3. ChatGPT đọc báo cáo, phân tích và đề xuất nhiệm vụ tiếp theo.
4. ChatGPT soạn nhiệm vụ; **người dùng duyệt nội dung**.
5. Sau khi được duyệt, nhiệm vụ mới được đưa vào [`TASKS/`](TASKS/).
6. Người dùng gửi Claude một prompt ngắn để đọc `TASKS/` và thực hiện.
7. Claude **không tự chọn hoặc tự triển khai** nhiệm vụ chưa được người dùng duyệt.

## Cấu trúc
| Thư mục | Nội dung |
|---|---|
| [`TASKS/`](TASKS/) | Nhiệm vụ đã duyệt (Claude đọc ở đây trước khi làm) |
| [`REPORTS/`](REPORTS/) | Báo cáo kết quả của Claude |
| [`HISTORY/`](HISTORY/) | Lịch sử thực hiện, quyết định kỹ thuật, kết quả kiểm chứng, thay đổi quan trọng |
| [`REFERENCES/`](REFERENCES/) | Tài liệu tham khảo đã xác minh: sơ đồ pipeline, định dạng asset |

## Quy tắc đánh số
- Báo cáo: `V001_ten-bao-cao.md`; nhiệm vụ: `V001_TASK_ten-nhiem-vu.md`; lịch sử: `V001_HISTORY_ten-su-kien.md`.
- Mã `V###` tăng tuần tự theo từng loại tài liệu (báo cáo, nhiệm vụ, lịch sử có dãy riêng), **không tái sử dụng**, không đổi số sau khi đã đăng.
- Báo cáo trả lời nhiệm vụ nào thì ghi mã nhiệm vụ đó ở phần đầu. Báo cáo khởi đầu (chưa có nhiệm vụ) đánh số trước.

## Nội dung một báo cáo
Mục tiêu · Phạm vi · Phương pháp · File/code đã kiểm tra · Phát hiện · Bằng chứng · Kết luận · Vấn đề chưa giải quyết · Đề xuất tiếp theo.
Mọi nhận định gắn nhãn **VERIFIED / PROBABLE / UNKNOWN / BLOCKED**.

## Bảo mật
Không đưa lên: mật khẩu, token, khóa, IP riêng, thông tin tài khoản, giá trị cấu hình nhạy cảm (kể cả `accinfo`/`accpint` trong `paklist.ini`), dữ liệu thô, script phân tích, dump, cơ sở dữ liệu, binary, mã nguồn hay asset game. Nếu phải che thông tin, báo cáo ghi rõ đã hiệu chỉnh.

## Liên kết
- Báo cáo chung (không thuộc Visual, chỉ để tham chiếu): [JX1_INVENTORY_RESEARCH](../JX1_INVENTORY_RESEARCH/README.md), trong đó có [TECHNICAL_ARCHITECTURE_REVIEW](../JX1_INVENTORY_RESEARCH/TECHNICAL_RESEARCH/TECHNICAL_ARCHITECTURE_REVIEW.md) (mục A3 nói về render/camera).
- Báo cáo: [V001](REPORTS/V001_asset-format-research.md), [V002](REPORTS/V002_full-technical-feasibility-audit.md).
