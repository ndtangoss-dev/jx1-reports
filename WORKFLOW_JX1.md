# QUY TRÌNH LÀM VIỆC CHÍNH THỨC – DỰ ÁN JX1

Áp dụng cho toàn bộ các Phase JX1 từ ngày tài liệu này được cập nhật.

## 1. Vai trò

### Chủ dự án – Người dùng
- Quyết định mục tiêu sản phẩm, gameplay và ưu tiên.
- Mô tả yêu cầu/lỗi bằng lời, ảnh, video hoặc trải nghiệm thực tế.
- Duyệt prompt trước khi giao nhiệm vụ, trừ các thao tác đã được ủy quyền rõ.
- Duyệt phương án ảnh hưởng lớn đến kiến trúc, gameplay, dữ liệu hoặc Main VM.
- Trải nghiệm APK trên điện thoại thật và nghiệm thu.

### ChatGPT – Phân tích và điều phối
- Phân tích yêu cầu, làm rõ vấn đề và xác định phạm vi.
- Đề xuất phương án kỹ thuật, rủi ro và tiêu chí nghiệm thu.
- Soạn prompt/chỉ thị thực thi rõ ràng, có phạm vi và điều kiện dừng.
- Sau khi người dùng duyệt, tạo/cập nhật prompt trên GitHub.
- Đọc báo cáo, phản biện kết quả, tổng hợp tiến độ và đề xuất bước tiếp theo.
- Không tuyên bố Codex đã nhận/chạy lệnh nếu chưa có bằng chứng.

### Codex CLI – Agent thực thi kỹ thuật chính
- Là agent thực thi mặc định cho JX1; khi Dispatcher bật, nhận việc bằng `codex exec` không tương tác trên Windows. TUI là phương án thủ công khi Dispatcher tắt.
- Đọc chỉ thị, workflow, trạng thái mới nhất và prompt đã duyệt từ GitHub.
- Xác minh đúng repo, working directory, model/provider/session và quyền trước khi thao tác.
- Tự kiểm tra source, môi trường, build tools, emulator/ADB và VM trong phạm vi được cấp.
- Thực hiện phân tích, sửa code, build, test, thu thập log và báo cáo theo prompt đã duyệt.
- Cập nhật tài liệu, trạng thái và kết quả trên GitHub khi có quyền truy cập.
- Không tự ý can thiệp Main VM, dữ liệu quan trọng, xóa/ghi đè source hoặc commit nhánh chính nếu chưa được phép.

### Claude Code – Công cụ phụ/đối chiếu (nếu được giao riêng)
- Không còn là agent thực thi mặc định trong quy trình này.
- Chỉ thực hiện QA độc lập, review hoặc nhiệm vụ riêng khi ChatGPT/người dùng giao rõ.
- Không đồng thời sửa cùng file/nhánh với Codex CLI.

## 2. Model và phiên làm việc Codex

- Phiên Codex CLI hiện được dự kiến sử dụng Xingchi provider, model `gpt-6.1-sol`, reasoning effort `max`.
- Đây là cấu hình phiên đã được kiểm tra gọi API thực tế. Phiên TUI được xác minh bằng `/status`; Dispatcher truyền tường minh ba giá trị và chạy preflight chỉ đọc trước mỗi task.
- Trước khi thực thi nhiệm vụ JX1, Codex phải xác nhận:
  - Working directory đúng repo/source được giao.
  - Model/provider/effort thực tế đúng yêu cầu nhiệm vụ (mặc định: `gpt-6.1-sol` / `xingchi` / `max`).
  - Đã đọc đúng prompt và trạng thái mới nhất.
- Nếu model/provider/effort không đúng hoặc không xác minh được, báo **BỊ CHẶN** và không âm thầm tiếp tục bằng model/provider khác.
- Không ghi API Key, token, mật khẩu hoặc thông tin xác thực vào prompt, báo cáo hay GitHub.

## 3. Quy trình chuẩn cho mỗi nhiệm vụ

1. Người dùng mô tả yêu cầu hoặc kết quả mong muốn.
2. ChatGPT phân tích, xác định phạm vi, rủi ro, phương án và tiêu chí nghiệm thu.
3. ChatGPT soạn prompt; người dùng duyệt trước khi giao nhiệm vụ, trừ các thao tác đã được ủy quyền rõ.
4. ChatGPT tạo/cập nhật prompt và chỉ thị trên repository báo cáo.
5. Khi Dispatcher đã cài, nó tự nhận task từ manifest mỗi 60 giây. Nếu Dispatcher tắt, người dùng có thể kích hoạt CLI thủ công theo `PROMPTS/00_CODEX_START_HERE.md`.
6. Codex đọc workflow, trạng thái mới nhất, chỉ thị bắt đầu và đầy đủ prompt nhiệm vụ đã được duyệt.
7. Codex xác minh phiên, source, môi trường, backup và quyền; sau đó xác nhận nhiệm vụ đã nhận rồi thực hiện trong phạm vi đã duyệt.
8. Codex tự kiểm thử/tái hiện, chạy hồi quy và thu thập bằng chứng phù hợp. Nếu có agent QA độc lập được giao riêng, phải ghi rõ agent và bằng chứng; không giả vờ đã giao subagent khi không có.
9. Codex cập nhật báo cáo, diff, backup, log, APK và SHA256 nếu có; cập nhật `00_LATEST_STATUS.md` khi trạng thái dự án thực sự thay đổi.
10. Codex bàn giao trong phiên CLI: việc đã làm, chưa làm, file thay đổi, lệnh/test và kết quả, bằng chứng, rủi ro, việc còn chặn, đường dẫn báo cáo và commit/PR GitHub nếu có.
11. ChatGPT đọc/đối chiếu kết quả và trình bày cho người dùng.
12. Người dùng kiểm tra thực tế và nghiệm thu hoặc yêu cầu vòng sửa tiếp theo.

## 4. Phân cấp quyền

### Có thể tự thực hiện trong phạm vi nhiệm vụ đã duyệt
- Đọc source/tài liệu, phân tích log, chạy test và build thử.
- Tạo backup, diff, log và artifact phiên bản mới.
- Sửa code trong phạm vi đã duyệt, kiểm thử trên môi trường thử nghiệm.
- Cập nhật báo cáo và trạng thái GitHub.
- Chạy các lệnh quản trị thông thường cần thiết trong môi trường thử nghiệm nếu không làm phát sinh rủi ro ngoài phạm vi.

### Phải hỏi người dùng trước
- Thay đổi kiến trúc lớn hoặc hành vi gameplay chưa được duyệt.
- Tác động Main VM, server production hoặc dữ liệu quan trọng.
- Xóa/ghi đè dữ liệu không thể khôi phục, source chính hoặc bản phát hành.
- Thay đổi quyền truy cập, bảo mật hoặc thông tin đăng nhập.
- Thao tác không thể đảo ngược hoặc có thể làm gián đoạn dịch vụ đang chạy.

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
- Codex CLI đọc prompt đã duyệt khi được kích hoạt; không tự nhận nhiệm vụ chỉ vì file xuất hiện trên GitHub.
- Codex cập nhật báo cáo sau khi làm việc, chỉ ghi kết quả có bằng chứng.
- Không commit source chính nếu chưa được người dùng cho phép.
- Không đưa API Key, token, mật khẩu, IP/tài khoản nhạy cảm hoặc dữ liệu truy cập vào GitHub.
- Nếu Codex không có quyền GitHub hoặc không có local clone/remote phù hợp, báo **BỊ CHẶN**; không tuyên bố đã push. Có thể lưu báo cáo cục bộ và bàn giao đường dẫn để ChatGPT cập nhật GitHub.

## 6. Trạng thái báo cáo bắt buộc

- **ĐÃ XÁC MINH:** có log, số đo, test hoặc bằng chứng thực tế.
- **CHƯA KIỂM THỬ:** đã sửa/build nhưng chưa kiểm tra đủ.
- **BỊ CHẶN:** thiếu quyền, môi trường hoặc điều kiện.
- **GIẢ THUYẾT:** nhận định chưa được xác minh.

Build thành công không đồng nghĩa nhiệm vụ hoàn thành. Báo cáo phải nêu rõ phần đã làm, chưa làm, lỗi còn lại và bằng chứng.

## 7. Quy tắc giao tiếp và tự chủ

- Codex tự làm thao tác kỹ thuật thông thường nếu có quyền và công cụ.
- Ưu tiên tự đọc file, chạy lệnh và lấy log; không yêu cầu người dùng copy/paste lệnh hoặc log nếu Codex có thể tự thực hiện.
- Người dùng thường điều khiển máy bằng điện thoại qua remote desktop; vì vậy ưu tiên chỉ thị ngắn, thao tác ít, không yêu cầu nhập lệnh dài thủ công.
- Không hỏi duyệt lại từng bước nhỏ đã nằm trong phạm vi.
- Chỉ hỏi khi có rủi ro hoặc quyết định ngoài phạm vi.
- Nếu Computer Use bị policy chặn, chuyển sang terminal/tool thực thi lệnh được cấp quyền; không tìm cách vượt chính sách.
- ChatGPT không nhìn thấy phiên Codex CLI đang chạy trên máy người dùng nếu không có báo cáo/kết nối tương ứng; phải phân biệt rõ đã đăng prompt, Codex đã tải prompt và Codex đã thực thi.

## 8. Nhận nhiệm vụ bằng JX1 Task Dispatcher

### Hàng đợi được duyệt
- Dispatcher Windows cài bằng Task Scheduler tên `JX1-Task-Dispatcher`, chạy tại đăng nhập của người dùng hiện tại với quyền `Limited`; không lưu mật khẩu.
- Dispatcher kiểm tra `PROMPTS/DISPATCH_QUEUE.json` trên nhánh `main` mặc định mỗi 60 giây. Chỉ các mục có `status` bằng `APPROVED` hoặc `ĐƯỢC DUYỆT` mới được nhận. Có file prompt nhưng không có mục trong hàng đợi thì không có quyền thực thi.
- Sau khi người dùng duyệt prompt, ChatGPT:
  1. Đưa prompt và tài liệu tham chiếu lên GitHub.
  2. Lấy commit SHA chứa các nội dung đó cùng Git blob SHA của từng file.
  3. Thêm một mục vào `PROMPTS/DISPATCH_QUEUE.json` với các trường `task_id`, `status`, `scope`, `approved_commit`, `prompt_path`, `prompt_sha`, `allowed_paths`, `references` (mỗi mục gồm `path` và `sha`), `approved_by` và `approved_at`.
  4. Dùng Task ID duy nhất; không tái sử dụng Task ID đã chạy, bị chặn hoặc thất bại.
- Dispatcher ghim prompt và tài liệu theo `approved_commit`, xác minh blob SHA, đường dẫn tương đối và giới hạn kích thước trước khi truyền nội dung cho Codex. Các file chỉ được tải về như dữ liệu; không có trường lệnh shell trong manifest.
- Khi khởi tạo lần đầu, các mục đã có sẵn được bỏ qua để tránh chạy lại prompt cũ. Task mới chuyển qua `QUEUED`, `RUNNING`, `COMPLETED`, `BLOCKED` hoặc `FAILED`; state, lock, status và log được giữ tại `%LOCALAPPDATA%\JX1TaskDispatcher`.
- Khóa file và Task Scheduler `IgnoreNew` bảo đảm chỉ một task chạy tại một thời điểm. Task ID chỉ được dispatch một lần. Sau reboot, task đang dở chỉ được resume bằng session ID đã lưu; nếu session không thể xác minh/phục hồi thì chuyển `BLOCKED`, không chạy prompt lại.

### Cấu hình thực thi
- Mỗi lượt dùng `CODEX_HOME=C:\Users\PC\.codex`, working directory `C:\Jx1CocoV3`, provider `xingchi`, model `gpt-6.1-sol`, reasoning `max`.
- Dispatcher gọi `codex exec --json`, sandbox `workspace-write`, approval policy `on-request`; cấm `--dangerously-bypass-approvals-and-sandbox`. Một lệnh cần phê duyệt tương tác, model không khớp, report thiếu hoặc thay đổi ngoài `allowed_paths` sẽ dừng và ghi `BLOCKED`.
- Agent chỉ ghi bên trong repo làm việc. Dispatcher so sánh Git working tree trước/sau và chặn việc công bố nếu có file ngoài phạm vi. Việc này là kiểm tra hậu kỳ, còn sandbox giới hạn bên ngoài working directory.
- Báo cáo tiếng Việt được tạo tại `docs-analysis/reports/dispatcher-<task_id>.md`. Dispatcher quét thông tin bí mật trước khi tải báo cáo lên `TEST_RESULTS/dispatcher-<task_id>.md`. Upload dùng Git Credential Manager nếu đã có credential phù hợp; không có credential thì giữ báo cáo local và ghi `BLOCKED – CHƯA PUSH`.

### Vận hành và phương án thủ công
- Cài: `docs-analysis/scripts/install_jx1_task_dispatcher.ps1`.
- Xem trạng thái: `docs-analysis/scripts/status_jx1_task_dispatcher.ps1`; state và log nằm trong `%LOCALAPPDATA%\JX1TaskDispatcher`.
- Tạm dừng/tiếp tục: `disable_jx1_task_dispatcher.ps1` / `enable_jx1_task_dispatcher.ps1`.
- Gỡ Task Scheduler (giữ state, log và báo cáo): `uninstall_jx1_task_dispatcher.ps1`.
- Nếu Dispatcher tắt, Codex chỉ nhận task khi người dùng kích hoạt thủ công. Không coi GitHub push là bằng chứng Codex đã tải hoặc thực thi prompt.

## 9. Nguyên tắc bất di bất dịch

1. Người dùng quyết định hướng phát triển và nghiệm thu.
2. ChatGPT phân tích, lập kế hoạch, viết nhiệm vụ và phản biện báo cáo.
3. Codex CLI là agent thực thi mặc định cho JX1.
4. Claude chỉ tham gia khi được giao vai trò phụ/đối chiếu riêng.
5. Không bịa kết quả hoặc tuyên bố test khi chưa có bằng chứng.
6. Bảo vệ Main VM, source chính và dữ liệu quan trọng.
7. Mọi thay đổi quan trọng có backup, diff và báo cáo.
8. Chỉ đóng nhiệm vụ khi có bằng chứng và người dùng nghiệm thu.


## 10. Ngôn ngữ giao tiếp và báo cáo (bắt buộc)

- Ngôn ngữ mặc định khi Codex trao đổi với người dùng là **tiếng Việt**.
- Mọi xác nhận nhận nhiệm vụ, câu hỏi làm rõ, kế hoạch, cập nhật tiến độ, giải thích lỗi, kết luận và báo cáo bàn giao phải viết bằng tiếng Việt.
- Giữ nguyên tiếng Anh đối với tên model/provider, tên file/thư mục, tên biến/hàm/class, API, lệnh terminal, thông báo lỗi gốc và thuật ngữ kỹ thuật khi cần chính xác.
- Khi trích dẫn log hoặc lỗi tiếng Anh, giữ nguyên đoạn gốc cần thiết và giải thích ý nghĩa bằng tiếng Việt ngay bên cạnh.
- Không tự chuyển toàn bộ câu trả lời sang tiếng Anh chỉ vì log, tài liệu hoặc source code sử dụng tiếng Anh.
- Chỉ dùng tiếng Anh cho phần giao tiếp/báo cáo khi người dùng yêu cầu rõ ràng.
- Nếu prompt nhiệm vụ hoặc tài liệu kỹ thuật yêu cầu định dạng đầu ra cụ thể, giữ nguyên cấu trúc đó nhưng viết nội dung diễn giải bằng tiếng Việt.
