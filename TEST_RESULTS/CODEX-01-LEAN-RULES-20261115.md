# CODEX-01 — Đồng bộ quy tắc Direct CLI

Ngày: 15/11/2026. Task ID: `CODEX-01-LEAN-RULES-20261115`.
Prompt đã đọc đúng tại commit `cf9fe73c60003b3a4278f46c9fd8b5848973612a`, file `PROMPTS/CODEX-01-LEAN-RULES-20261115.md`, blob `cac64fa41c6cb0170dc233a39f334af90bae1913`.

## Kết quả

Đã cập nhật `C:\Jx1CocoV3\AGENTS.md`: Direct CLI do người dùng kích hoạt, không Dispatcher/queue; đọc prompt ghim một lần, đọc đúng tài liệu cần, không preflight/model/config/remote/workspace lặp; một báo cáo cuối; resume từ checkpoint; đơn vị công việc 5–10 phút có đầu ra kiểm chứng được; yêu cầu lớn được chia nhỏ và mỗi lượt bàn giao một đơn vị. Giữ nguyên cấu hình Sol Max hiện tại; không kiểm tra hay thay đổi cấu hình.

Đã loại bỏ quy định báo cáo/commit mỗi bước, bắt buộc ghi bài học sau từng lỗi và phụ thuộc công cụ AskUserQuestion. Quy định snapshot được làm rõ: tác vụ chỉ đọc/tài liệu không yêu cầu snapshot; thay đổi VM vẫn theo phê duyệt, snapshot dự án vẫn tạm dừng. Làm rõ thao tác kỹ thuật thường lệ đã duyệt được tự thực hiện, báo cáo/quy tắc đã lọc được gửi GitHub khi được yêu cầu.

Các rào chắn giữ nguyên: không tác động Main VM/production hoặc sửa Cocos canonical chưa duyệt; không chạy exe server chưa duyệt; không xóa/ghi đè dữ liệu không thể khôi phục; không reset/clean thay đổi local; không lộ secret/credential; không bypass sandbox/approval/UAC. Phần điều khiển VM, thông tin dự án và bản đồ code local được giữ nguyên.

## Nguồn đối chiếu và mâu thuẫn

Đã đọc ba file chuẩn trên `ndtangoss-dev/jx1-reports`, `main`:

| File | Blob SHA khi đọc |
|---|---|
| `PROMPTS/CODEX_DIRECT_CLI_RULES.md` | `75dae3da8e09228344e73db57b73b78474bfcf2b` |
| `WORKFLOW_JX1.md` | `61779eff30d823a2db4bb03aabc4f8c972d87e00` |
| `PROMPTS/00_CODEX_START_HERE.md` | `efb0c9192ba2d43a19b939ff8464fa0d16f53dc0` |

Ba tài liệu khớp Direct CLI, không sửa chúng. Direct CLI Rules ghi ngân sách tổng task nhỏ 10–15 phút/audit 30–45 phút; prompt CODEX-01 đã được người dùng duyệt quy định cụ thể hơn: đơn vị 5–10 phút. AGENTS áp dụng đơn vị 5–10 phút, không tự sửa tài liệu chuẩn ngoài phạm vi. Không thay đổi prompt AMOLX-02.

## Công việc đang dở được bảo toàn

Checkpoint AMOLX-02 trong ngữ cảnh hiện có đã được xem một lần: đã có đối chiếu enum/packet tĩnh, báo cáo `TEST_RESULTS/AMOLX-02-PROTOCOL-AUDIT-20261115.md` chưa tạo/commit/push. Không chạy lại audit, không build/kết nối hay sửa source trong CODEX-01. Điểm tiếp tục: dùng bằng chứng đã thu, hoàn thiện các mục còn thiếu của prompt AMOLX-02 và tạo báo cáo; cần người dùng giao tiếp đơn vị đó sau bàn giao này. Không xem audit đã hoàn thành.

## Kiểm chứng và Git

Trước ghi đã kiểm tra `git status --short --branch` một lần: nhánh local `master`; `docs-analysis/BAI_HOC.md` có thay đổi tracked, nhiều báo cáo/output/backup/script untracked đã có từ trước. Chúng được giữ nguyên và không đưa vào commit CODEX-01. HEAD đã có bằng chứng trong phiên: `2a1c0d91023df05e65a78e9fc2d953eb79b0e16d`.

Chỉ thay đổi local `AGENTS.md` và tạo báo cáo này. Kiểm chứng là xem diff và các quy tắc được cập nhật; không cần unit test/build cho thay đổi hướng dẫn. Không chạy preflight, model/config check, CLI help, Dispatcher, Scheduler, test game hay thao tác VM/server. Không tuyên bố test chưa chạy là đạt.

GitHub `main` chưa có `AGENTS.md` (API trả 404). Bản AGENTS trên repository báo cáo sẽ chỉ chứa quy tắc Direct CLI và rào chắn dùng chung; phụ lục vận hành local có chi tiết truy cập nội bộ không được công khai. Báo cáo này nêu rõ sự khác biệt đó. Repository local chưa có remote theo bằng chứng phiên trước; gửi commit riêng lên GitHub bằng connector hiện có, không đổi remote/credential/config. SHA/URL commit được xác minh và cung cấp khi bàn giao; không tự nhúng SHA chứa chính file vì sẽ làm SHA thay đổi.

## Trạng thái bàn giao

`DONE` sau khi commit chứa quy tắc và báo cáo được xác minh trên GitHub. Không có blocker kỹ thuật được ghi nhận ở thời điểm soạn báo cáo; nếu commit bị chặn, giữ nguyên bản local và công bố `BỊ CHẶN – CHƯA PUSH` cùng lỗi thực tế. Mọi thay đổi có sẵn ngoài CODEX-01 được giữ nguyên.

Cần tôi quyết định: không.
