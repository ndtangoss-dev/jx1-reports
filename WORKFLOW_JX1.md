> **HẾT HIỆU LỰC từ 2026-11-16.** Quy trình hiện hành nằm trên nhánh `jx1-ops`, thư mục `JX1_OPS/` (bắt đầu từ `JX1_OPS/README.md`). Nội dung dưới đây giữ lại để tra cứu lịch sử.

# QUY TRÌNH LÀM VIỆC CHÍNH THỨC – JX1

**Chuẩn thực thi Codex Direct CLI:** [PROMPTS/CODEX_DIRECT_CLI_RULES.md](PROMPTS/CODEX_DIRECT_CLI_RULES.md)  
**Trạng thái dự án:** [00_LATEST_STATUS.md](00_LATEST_STATUS.md)  
**Repository báo cáo:** `ndtangoss-dev/jx1-reports`

Tài liệu Direct CLI Rules là chuẩn chi tiết về cách Codex thực thi, giới hạn thao tác, tiết kiệm token, kiểm chứng và bàn giao. Nội dung dưới đây xác định vai trò, quy trình quyết định và ranh giới an toàn.

## 1. Vai trò

- **Người dùng:** quyết định mục tiêu, ưu tiên, phê duyệt thay đổi rủi ro và nghiệm thu.
- **ChatGPT:** phân tích yêu cầu, xác định phạm vi, viết prompt ngắn và đủ, tạo prompt sau khi được duyệt, đọc/đối chiếu báo cáo và đề xuất bước tiếp theo.
- **Codex CLI:** executor kỹ thuật mặc định cho JX1; làm trực tiếp trong workspace được chỉ định, theo prompt đã duyệt và quy tắc Direct CLI.
- **Claude Code/agent khác:** chỉ tham gia khi được giao riêng cho QA độc lập hoặc nhiệm vụ phụ; không đồng thời sửa cùng vùng source với Codex.

## 2. Quy trình chuẩn — Direct CLI

1. Người dùng nêu mục tiêu hoặc vấn đề.
2. ChatGPT kiểm tra trạng thái/báo cáo nền có liên quan, tránh yêu cầu làm lại việc đã hoàn thành.
3. ChatGPT soạn một prompt có mục tiêu, phạm vi, file/path đã biết, quyền, đầu ra, tiêu chí nghiệm thu và giới hạn thời gian/công việc.
4. Người dùng duyệt; ChatGPT đưa prompt lên GitHub và cung cấp commit SHA + chỉ thị kích hoạt ngắn.
5. Người dùng kích hoạt **phiên Codex CLI hiện có**. Codex đọc prompt ghim một lần và làm thẳng vào phần việc chính. Không Dispatcher, không polling queue.
6. Codex tạo một báo cáo cuối, kiểm tra diff/status một lần, commit/push báo cáo nếu có quyền.
7. Người dùng báo đã có báo cáo; ChatGPT đọc đúng file, kiểm chứng kết luận và cùng người dùng quyết định nhiệm vụ tiếp theo.

Không coi việc tạo prompt là bằng chứng Codex đã nhận/chạy. Không coi dòng tiến độ là bằng chứng hoàn thành. Chỉ xác nhận thực thi khi có bằng chứng trong phiên; chỉ xác nhận push khi có commit SHA và URL.

## 3. Prompt bắt buộc phải ngắn và có điểm kết thúc

Mỗi prompt chỉ gồm:
- Mục tiêu và kết quả cần bàn giao.
- Phạm vi file/thư mục cụ thể; đường dẫn đã biết.
- Những việc được phép và bị cấm.
- Các kiểm tra thiết yếu và bằng chứng phải ghi.
- Một đường dẫn báo cáo cuối.
- Giới hạn thời gian/công việc; điều kiện dừng khi thiếu dữ liệu hoặc bị chặn.

Không yêu cầu Codex tự khám phá lại toàn dự án, kiểm tra cấu hình lặp, đọc lại toàn bộ lịch sử hoặc tạo báo cáo trung gian. Chi tiết áp dụng tại [CODEX_DIRECT_CLI_RULES.md](PROMPTS/CODEX_DIRECT_CLI_RULES.md).

## 4. Quyền và an toàn

Codex được tự thực hiện thao tác kỹ thuật thông thường nằm trong prompt đã duyệt. Phải hỏi người dùng trước khi:
- Tác động Main VM, server production hoặc dữ liệu quan trọng.
- Xóa/ghi đè dữ liệu không thể khôi phục hoặc source chính.
- Thay đổi kiến trúc lớn, quyền truy cập, bảo mật hoặc credential.
- Thực hiện thao tác có thể gián đoạn dịch vụ.

Bất di bất dịch:
- Giữ nguyên Cocos client canonical nếu chưa được duyệt.
- Không can thiệp Main VM/production nếu chưa được duyệt.
- Không reset/clean/ghi đè thay đổi local của người dùng.
- Không tiết lộ secret/token/mật khẩu.
- Không bypass sandbox/approval policy.
- Không tuyên bố test/build/runtime thành công nếu chưa có bằng chứng.

## 5. Báo cáo và trạng thái

Mọi báo cáo phải phân biệt:
- **ĐÃ XÁC MINH:** có bằng chứng trực tiếp.
- **CHƯA KIỂM THỬ:** chưa chạy kiểm thử cần thiết.
- **CHƯA XÁC MINH:** thiếu bằng chứng để kết luận.
- **GIẢ THUYẾT:** nhận định cần kiểm chứng.
- **BỊ CHẶN:** không thể tiếp tục do quyền/phụ thuộc/môi trường.

Trạng thái cuối của task: `DONE`, `PARTIAL`, `BLOCKED`, hoặc `FAILED`. Báo cáo phải nêu phát hiện, file/symbol/line, kiểm tra đã chạy, phần chưa xác minh, blocker và commit/link nếu đã push.

## 6. Dispatcher

Dispatcher và `PROMPTS/DISPATCH_QUEUE.json` là cơ chế cũ/legacy, **không thuộc quy trình Direct CLI hiện hành**. Không bật, polling, sửa queue hoặc gọi Dispatcher cho nhiệm vụ mới trừ khi người dùng chọn lại cơ chế đó một cách rõ ràng.

## 7. Ngôn ngữ

Trao đổi và báo cáo bằng tiếng Việt. Giữ nguyên tên file, symbol, API, lệnh và thông báo lỗi gốc khi cần chính xác; giải thích bằng tiếng Việt.
