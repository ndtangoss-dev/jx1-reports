# Command Code — cách cài và chạy (Q-72, #238 bước 1; tra tài liệu 19/11, CHƯA cài thử)
Nguồn: commandcode.ai/docs, /docs/headless (đọc qua WebFetch; chưa chạy thật).
- Cài: `npm i -g command-code` (lệnh `cmd`; trên Windows dùng `command-code` hoặc `cmdc` vì `cmd` trùng shell). **Máy thật chưa có Node/npm** (kiểm 19/11: không có node.exe) → cần cài Node LTS trước = cài phần mềm ngoài, [CAN-CHU] duyệt.
- Đăng nhập: `cmd login` một lần (mở trình duyệt) — CHỦ tự làm. Chạy tự động: biến môi trường `COMMAND_CODE_API_KEY` (không ghi vào kho). Kiểm: `cmd status`.
- Headless: `cmd -p "<lệnh>"` hoặc `echo "<lệnh>" | cmd -p`; `-m <mô hình>`, `--effort <mức>`; ghi tệp/chạy shell cần `--yolo` (CHỈ trong worktree riêng, tệp cho phép); `--accept-edits`, `--plan`, `-t` tin dự án.
- Mô hình rẻ: free `glyph-cluster:free`, `flint-v1.0:free` (≤1000 yêu cầu/ngày), `inkling-2-small:free` (≤200/ngày) — có thể giới hạn thời gian. Danh sách: /docs/reference/cli/models.
- Giới hạn: tín dụng 10 USD một lần theo lời chủ; không mua gói trả phí khi chưa hỏi chủ.
- Nhắc: dữ liệu `.commandcode/` (học phong cách) để ngoài worktree/kho.

## Tiến độ #239 (19/11 14:10)
- [ĐÃ KIỂM] Node LTS v26.13.1 (nodejs.org, bản zip portable win-x64, 41.166.246 byte) tải về `D:\JX-node\node.zip`; SHA-256 khớp SHASUMS256.txt chính thức: e2edda75bfb089654705cf65a13b58933bfd5f57148e8ebda916f58a2474f1f7. Chữ ký GPG chưa kiểm.
- Giải nén + `npm i -g command-code` bị bộ phân loại quyền của Claude Code CHẶN ("Undermining Oversight": cài gói npm ngoài). Không lách. CẦN CHỦ cho phép trực tiếp trong khung chat Code (hoặc chủ tự chạy 3 lệnh dưới), rồi mới tiếp.
- Lệnh chủ tự chạy (PowerShell, không cần Admin): `Expand-Archive D:\JX-node\node.zip D:\JX-node -Force; $env:Path="D:\JX-node\node-v26.13.1-win-x64;$env:Path"; npm config set prefix D:\JX-node\npm-global; $env:Path="D:\JX-node\npm-global;$env:Path"; npm i -g command-code; command-code --version`
