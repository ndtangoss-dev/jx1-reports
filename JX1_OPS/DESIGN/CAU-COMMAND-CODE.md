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

## Đã cài (#241, chủ cho phép; 19/11)
- [ĐÃ KIỂM] Node v26.13.1 + npm 11.20.0 giải nén ở `D:\JX-node\node-v26.13.1-win-x64`; `npm i -g command-code` thêm 301 gói vào `D:\JX-node\npm-global` (prefix riêng, không Admin); `command-code --version` = 1.91.1.
- PATH chỉ trong phiên: `$env:Path="D:\JX-node\npm-global;D:\JX-node\node-v26.13.1-win-x64;$env:Path"`.
- Đăng nhập: CHỦ tự làm (xem BAO-CAO-CHU). Chưa đăng nhập, chưa kiểm ảnh/mô hình/tín dụng.

## Kiểm sau khi chủ đăng nhập (#242, 19/11 14:40)
- `command-code status`: Authenticated (tài khoản đã đăng nhập); lệnh KHÔNG in số tín dụng. Mô hình free nên chưa tốn tín dụng; số dư [CHƯA KIỂM] (xem ở trang web của Command Code nếu chủ muốn).
- Đọc ảnh: [ĐÃ KIỂM] `-m flint-v1.0:free -p` đọc được `shot.jpg` (ảnh chụp LD), nhận ra màn đăng nhập và nút "Đăng nhập"/"Thoát". Thư mục thử `D:\JX-cmdc-test` (ngoài kho).
- Chưa giao tester đăng nhập→tạo nhân vật (cần worktree riêng + hòm cầu riêng, LD không đang bị tiểu yêu khác dùng).

## Tín dụng và mô hình (#245, 19/11 15:15)
- Chủ đã đăng ký gói Go (1 đô/tháng, Q-76). KHÔNG nạp/nâng thêm. Chỉ dùng một khóa (khóa đã đăng nhập).
- Số tín dụng: `/usage` chỉ chạy trong phiên tương tác (`-p "/usage"` bị hiểu thành đường dẫn). `command-code status` không in số. Trước/sau mỗi lượt: [CHƯA ĐỌC ĐƯỢC từ dòng lệnh]; cần ai mở phiên tương tác `command-code` gõ `/usage` (B hoặc chủ) rồi ghi số vào đây.
- Mô hình ĐÃ KIỂM đọc ảnh: `flint-v1.0:free` (#242, ảnh chụp LD, nhận ra nút Đăng nhập/Thoát). Các mô hình khác chưa kiểm.

## Số dư tín dụng (B, 19/11 17:20)
- `command-code status`: đã đăng nhập, nhà cung cấp Command Code. Không hiện số dư.
- `command-code -p "/usage"` (không tương tác) chỉ trả lời "/usage chỉ hiện trong phiên tương tác", dẫn tới trang web commandcode.ai/usage. B không mở được phiên tương tác từ Bash. Số trước/sau: CHƯA ĐO; cách đo: chủ gõ `/usage` trong phiên tương tác của mình hoặc mở trang web, hoặc cấp quyền B dùng trình duyệt trong phiên chủ đã đăng nhập. Mô hình `flint-v1.0:free` là bản miễn phí nên chi phí dự kiến 0.
