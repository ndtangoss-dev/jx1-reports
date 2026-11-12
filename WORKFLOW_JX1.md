# QUY TRÌNH LÀM VIỆC CHÍNH THỨC – DỰ ÁN JX1

Áp dụng cho toàn bộ các Phase JX1 từ ngày tài liệu này được duyệt.

## 1. Vai trò

### Chủ dự án – Người dùng
- Quyết định mục tiêu sản phẩm, gameplay và ưu tiên.
- Mô tả yêu cầu/lỗi bằng lời, ảnh, video hoặc trải nghiệm thực tế.
- Duyệt các phương án có ảnh hưởng lớn đến kiến trúc, gameplay, dữ liệu hoặc Main VM.
- Trải nghiệm APK trên điện thoại thật và nghiệm thu.

### ChatGPT – Phân tích và điều phối
- Phân tích yêu cầu, làm rõ vấn đề và xác định phạm vi.
- Đề xuất phương án kỹ thuật, tiêu chí nghiệm thu và kế hoạch.
- Soạn prompt/chỉ thị rõ ràng cho Claude Code.
- Sau khi người dùng duyệt, tạo/cập nhật prompt trên GitHub.
- Đọc báo cáo, phản biện kết quả, tổng hợp tiến độ và đề xuất bước tiếp theo.
- Không tuyên bố Claude đã nhận/chạy lệnh nếu chưa có bằng chứng.

### Claude Code – Thực thi kỹ thuật
- Đọc chỉ thị và tài liệu dự án trên GitHub.
- Tự kiểm tra source, môi trường, build tools, emulator/ADB và VM trong phạm vi quyền được cấp.
- Thực hiện phân tích, sửa code, build, test, thu thập log và báo cáo.
- Cập nhật tài liệu, trạng thái và kết quả trên GitHub.
- Không tự ý can thiệp Main VM, dữ liệu quan trọng, xóa/ghi đè source hoặc commit nhánh chính nếu chưa được phép.

## 2. Phân vai model trong Claude

- **Haiku:** QA, kiểm thử, tái hiện lỗi, đọc/triage log, đo đạc, kiểm thử hồi quy và cung cấp bằng chứng.
- **Opus:** phân tích sâu, thiết kế giải pháp, sửa code, xử lý lỗi và phối hợp build.
- **Claude Code:** điều phối các vai trò, quản lý source/backup, tích hợp, build, test và bàn giao.
- Nếu môi trường không có quyền truy cập emulator/VM hoặc không hỗ trợ gọi model phụ, Claude phải nêu rõ; không giả vờ đã giao việc.

## 3. Quy trình chuẩn cho mỗi nhiệm vụ

1. Người dùng mô tả yêu cầu hoặc kết quả mong muốn.
2. ChatGPT phân tích, xác định phạm vi, rủi ro, phương án và tiêu chí nghiệm thu.
3. ChatGPT tạo prompt. Người dùng duyệt trước khi giao nhiệm vụ, trừ các thao tác đã được ủy quyền rõ.
4. ChatGPT đưa prompt và chỉ thị lên repository báo cáo.
5. Claude Code đọc prompt, kiểm tra trạng thái mới nhất và xác minh môi trường trước khi thao tác.
6. Haiku kiểm thử/tái hiện; Opus phân tích và sửa; Claude Code điều phối và tích hợp.
7. Haiku kiểm thử lại, chạy hồi quy và thu thập bằng chứng.
8. Claude cập nhật báo cáo, diff, backup, APK và SHA256 nếu có.
9. ChatGPT đọc/đối chiếu kết quả và trình bày cho người dùng.
10. Người dùng kiểm tra thực tế và nghiệm thu hoặc yêu cầu vòng sửa tiếp theo.

## 4. Phân cấp quyền

### Có thể tự thực hiện trong phạm vi nhiệm vụ đã duyệt
- Đọc source/tài liệu, phân tích log, chạy test, build thử.
- Tạo backup, diff, log và artifact phiên bản mới.
- Sửa code trong phạm vi đã duyệt, kiểm thử trên môi trường thử nghiệm.
- Cập nhật báo cáo và trạng thái GitHub.

### Phải hỏi người dùng trước
- Thay đổi kiến trúc lớn hoặc hành vi gameplay chưa được duyệt.
- Tác động Main VM, server production hoặc dữ liệu quan trọng.
- Xóa/ghi đè dữ liệu không thể khôi phục, source chính hoặc bản phát hành.
- Thay đổi quyền truy cập, bảo mật hoặc thông tin đăng nhập.

## 5. Quy tắc GitHub

Repository báo cáo: `ndtangoss-dev/jx1-reports`.

- `00_LATEST_STATUS.md`: trạng thái mới nhất đã xác minh.
- `PROMPTS/`: prompt và chỉ thị thực thi.
- `FIX_HISTORY/`: lịch sử các bản Fix.
- `TEST_RESULTS/`: kết quả QA.
- `PATCH_NOTES/`: ghi chú patch.
- `CLIENT/`: công việc Client.
- `SERVER/`: công việc Server.

Quy tắc:
- ChatGPT tạo/cập nhật prompt sau khi người dùng duyệt.
- Claude lấy prompt và thực thi khi được kích hoạt hoặc khi cơ chế tự động đã được cấu hình.
- Claude cập nhật báo cáo sau khi làm việc.
- Không xem việc file xuất hiện trên GitHub là bằng chứng Claude đã nhận hoặc bắt đầu chạy.
- Không commit source chính nếu chưa được người dùng cho phép.

## 6. Trạng thái báo cáo bắt buộc

- **ĐÃ XÁC MINH:** có log, số đo, test hoặc bằng chứng thực tế.
- **CHƯA KIỂM THỬ:** đã sửa/build nhưng chưa kiểm tra đủ.
- **BỊ CHẶN:** thiếu quyền, môi trường hoặc điều kiện.
- **GIẢ THUYẾT:** nhận định chưa được xác minh.

Build thành công không đồng nghĩa nhiệm vụ hoàn thành. Báo cáo phải nêu rõ phần đã làm, chưa làm, lỗi còn lại và bằng chứng.

## 7. Quy tắc giao tiếp

- Claude tự làm thao tác kỹ thuật thông thường nếu có quyền và công cụ.
- Không yêu cầu người dùng chạy lệnh/copy log nếu Claude có thể tự lấy.
- Không hỏi duyệt lại từng bước nhỏ đã nằm trong phạm vi được duyệt.
- Chỉ hỏi khi có rủi ro hoặc quyết định ngoài phạm vi.
- ChatGPT không nhìn thấy phiên Claude Code đang chạy trên máy người dùng nếu không có báo cáo/kết nối tương ứng; phải phân biệt rõ đã đăng lệnh, đã tải prompt và đã thực thi.

## 8. Cơ chế nhận nhiệm vụ từ GitHub

GitHub repository không tự đánh thức Claude Code. Claude chỉ đọc file khi được người dùng/phiên Claude kích hoạt hoặc khi người dùng đã thiết lập một watcher/automation riêng.

Quy trình mặc định hiện tại:
1. ChatGPT tạo prompt và file chỉ thị trên GitHub.
2. Người dùng mở phiên Claude Code và gửi lệnh ngắn: “Đọc PROMPTS/00_CLAUDE_START_HERE.md trong ndtangoss-dev/jx1-reports, kiểm tra nhiệm vụ mới và thực hiện theo quy trình.”
3. Claude đọc `00_LATEST_STATUS.md`, file chỉ thị bắt đầu, rồi prompt nhiệm vụ có trạng thái đã duyệt.
4. Claude xác nhận nhiệm vụ đã đọc, môi trường truy cập được và bắt đầu theo đúng thứ tự.

Nếu muốn tự động nhận mà không cần nhắc Claude, phải cài một cơ chế riêng (ví dụ GitHub Actions/webhook hoặc tiến trình polling chạy trên máy có Claude Code/API/agent được cấu hình). Cơ chế đó cần xác thực an toàn, giới hạn repository, tránh chạy lặp và yêu cầu phê duyệt cho hành động rủi ro. Chưa được coi là đã bật tự động cho tới khi cài đặt và kiểm thử thành công.

## 9. Nguyên tắc bất di bất dịch

1. Người dùng quyết định hướng phát triển và nghiệm thu.
2. ChatGPT phân tích, lập kế hoạch, viết nhiệm vụ và phản biện báo cáo.
3. Claude Code thực thi kỹ thuật.
4. Haiku QA; Opus sửa code.
5. Không bịa kết quả hoặc tuyên bố test khi chưa có bằng chứng.
6. Bảo vệ Main VM, source chính và dữ liệu quan trọng.
7. Mọi thay đổi quan trọng có backup, diff và báo cáo.
8. Chỉ đóng nhiệm vụ khi có bằng chứng và người dùng nghiệm thu.