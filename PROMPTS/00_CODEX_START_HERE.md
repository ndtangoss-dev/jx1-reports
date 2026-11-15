# CODEX CLI — ĐIỂM BẮT ĐẦU (DIRECT CLI)

Repository: `ndtangoss-dev/jx1-reports`  
Quy trình: [WORKFLOW_JX1.md](../WORKFLOW_JX1.md)  
Quy tắc thực thi: [CODEX_DIRECT_CLI_RULES.md](CODEX_DIRECT_CLI_RULES.md)

## Khi người dùng kích hoạt một task

1. Đọc đúng prompt đã ghim tại commit được cung cấp **một lần**.
2. Dùng workspace/đường dẫn đã được chỉ định. Kiểm tra Git status một lần trước khi ghi file.
3. Nếu phiên/model/provider đã được xác nhận trong phiên hiện tại, không chạy lại preflight, /status, config check hoặc CLI help.
4. Không đọc toàn bộ workflow/status/lịch sử. Chỉ đọc tài liệu và source liên quan trực tiếp được prompt chỉ định.
5. Làm ngay phần việc chính. Không Dispatcher, không polling queue, không tạo kế hoạch/tiến độ trung gian.
6. Không fetch lại prompt, source, report hoặc Git refs đã có, trừ khi mất ngữ cảnh, gặp lỗi, hoặc cần xác minh trước khi push.
7. Nếu resume cùng session, tiếp tục từ kết quả/checkpoint gần nhất; không khởi động lại task.
8. Nếu thiếu dữ liệu, ghi rõ `CHƯA XÁC MINH` và lý do; chuyển sang phần còn lại, không tìm kiếm vô hạn.
9. Tạo một báo cáo cuối tại đúng đường dẫn trong prompt. Kiểm tra diff/status một lần; chỉ commit file thuộc task.
10. Push nếu có quyền. Nếu không, ghi `BỊ CHẶN – CHƯA PUSH`, giữ báo cáo local và nêu chính xác lý do.

## Điều cấm

- Không tự mở rộng phạm vi.
- Không lặp kiểm tra workspace/config/model/remote/refs.
- Không đọc lại báo cáo lịch sử không liên quan.
- Không tạo parser/script hoặc báo cáo trung gian nếu không cần thiết.
- Không sửa source trong task read-only.
- Không tác động Main VM, production hoặc Cocos canonical nếu chưa được duyệt.
- Không reset/clean/ghi đè thay đổi local.
- Không tiết lộ secret hoặc bypass sandbox/approval.

## Bàn giao

Trả lời ngắn bằng tiếng Việt: trạng thái `DONE/PARTIAL/BLOCKED/FAILED`; phát hiện chính kèm file/symbol/line; file đã tạo/thay đổi; kiểm tra và kết quả; phần chưa xác minh; commit SHA + link báo cáo hoặc lý do chưa push.

**Không tuyên bố hoàn thành nếu thiếu bằng chứng.**
