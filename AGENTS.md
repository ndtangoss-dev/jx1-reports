# AGENTS.md — JX1 Direct CLI

Áp dụng từ 17/11/2026 cho repository báo cáo `ndtangoss-dev/jx1-reports`.

## Vào việc

- Làm theo prompt/task đã duyệt trong worktree được giao; đọc một lần, dùng commit ghim nếu có. Không dùng Dispatcher/polling queue. Giữ model/provider/reasoning/CODEX_HOME hiện tại; không chạy lại preflight, `/status`, CLI help hay kiểm kê môi trường.
- Kiểm tra Git status/branch một lần trước ghi; giữ nguyên local có sẵn. Chỉ sửa vùng được giao, gồm báo cáo được task/prompt chỉ định. Thiếu metadata mẫu không tự chặn task đã duyệt; hỏi khi thiếu mục tiêu/phạm vi hoặc có mâu thuẫn thật.
- Chỉ đọc tài liệu/source cần trả lời task. Không mặc định đọc workflow, STATE, lịch sử, mọi báo cáo hoặc mọi skill. Tài liệu sâu khi cần: `PROMPTS/CODEX_DIRECT_CLI_RULES.md`, `WORKFLOW_JX1.md`, `PROMPTS/00_CODEX_START_HERE.md`; xác nhận file tồn tại trước khi dùng, không tìm repo khác nếu thiếu.
- Nếu skill JX1 đã được triển khai, chỉ nạp skill đúng việc: đọc server, đọc client, báo cáo hoặc sổ thông số. Không giả định `.agents/skills` đã tồn tại. Bản đồ/Graphify/tóm tắt chỉ định vị; kiểm file thật và dòng hiện tại trước kết luận. Bản thảo chờ PM triển khai nằm ở `JX1_OPS/REPORTS/M-02.md`.
- Ưu tiên `rg`; thiếu thì báo một lần và dùng `Select-String`/`Get-ChildItem` giới hạn thư mục, không cài. Không tạo parser/script phụ khi trích xuất trực tiếp đủ.

## Hoàn tất task

- Trao đổi/báo cáo bằng tiếng Việt. Tự làm thao tác thông thường đã duyệt, không hỏi lại quyền, không MessageBox. Mốc 5–10 phút để thiết kế đơn vị việc, không phải hạn buộc bỏ dở phạm vi đã duyệt. Resume checkpoint một lần, không làm lại phần có bằng chứng.
- Theo đuổi đủ phạm vi; gặp lỗi thì phân tích và sửa an toàn trong lượt, tối đa 3 lần/cùng lỗi. Chỉ dừng vì cần quyết định/quyền ngoài phạm vi, rủi ro hoặc blocker không xử lý an toàn; giữ nguyên việc dở, nêu bước tiếp tục.
- Một báo cáo cuối đúng đường dẫn: `TOM TAT 5 DONG`, `DA XAC MINH / CHUA XAC MINH`, `file:dòng`, test thực chạy/chưa chạy, lỗi/cách thử/kết quả, trạng thái `DONE/PARTIAL/BLOCKED/FAILED`. Chỉ sửa `docs-analysis/BAI_HOC.md` khi được giao và cần thiết.
- Sau sửa xem diff một lần; chỉ stage/commit file thuộc task khi được yêu cầu. Không lặp kiểm tra Git nếu chưa có lỗi/mâu thuẫn mới. Nêu SHA khi commit thành công; chỉ nhận push khi có bằng chứng GitHub. Bị chặn ghi `BỊ CHẶN – CHƯA PUSH`, lỗi thật, báo PM qua báo cáo; không sửa quyền/credential/config để vượt lỗi.

## Rào chắn luôn áp dụng

- Không reset/clean/checkout phá hủy, sửa bản gốc/Cocos canonical hay Main VM/production chưa duyệt; không ghi khóa/mật khẩu, tiết lộ truy cập nội bộ hoặc bypass sandbox/approval. Không gửi source/binary/dump/log nhạy cảm/dữ liệu dự án ra ngoài; chỉ commit/push tài liệu đã lọc khi được yêu cầu. VirusTotal chỉ tra hash.
- Cấm chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`. Exe/DLL/cấu hình game là không tin cậy; exe chỉ chạy trong VM, từng exe server cần duyệt riêng, kể cả `S3RelayServer.exe`. Không suy runtime từ source, không nhận build/test đạt nếu chưa chạy; chỉ build/test/kết nối khi task cho phép.
- Đọc source/báo cáo không cần snapshot; snapshot VM vẫn tạm dừng, không tự chụp, cần duyệt cụ thể trước khi đổi trạng thái. Không công khai phụ lục nội bộ `C:\Jx1CocoV3\AGENTS.md`.
- Làm trên bản copy; giữ bản hoàn tác khi sửa cấu hình được phép. Thay quyền/credential/bảo mật, cấu hình ngoài VM chưa duyệt hoặc thao tác có thể gián đoạn dịch vụ phải hỏi trước.
- Lệnh Admin máy thật: chỉ khi task cho phép, soạn `.ps1` kèm hoàn tác trong `docs-analysis/scripts` để chủ máy tự chạy; không vượt UAC.
- Trước exe đã duyệt trong VM: cô lập mạng đúng phạm vi, quét Defender, lưu SHA-256, bật log/audit; chỉ mở cổng/địa chỉ đã duyệt, không port-forward Internet. Hộp thoại/thao tác chưa được hướng dẫn thì dừng thao tác đó và hỏi.
