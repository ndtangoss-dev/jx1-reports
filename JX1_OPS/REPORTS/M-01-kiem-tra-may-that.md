# M-01 - Kiểm tra máy thật: tiến trình ẩn, RAM, ổ C (17/11/2026 13:35)

Chỉ đọc/đo, không tắt, gỡ hay xóa gì. Không đưa PID hay khóa vào báo cáo. Mọi con số bên dưới là đo lúc 13:30-13:35.

## TÓM TẮT
1. RAM: tổng working set ~16 GB (máy thật; WMI lỗi nên không đọc được tổng RAM vật lý). Nhóm lớn: Chrome 24 tiến trình ~4,7 GB; Claude desktop + Claude Code 16 tiến trình ~3,1 GB; ChatGPT/Codex app 12 tiến trình ~1,1 GB; Memory Compression ~1 GB; codex (worker) 8 tiến trình ~0,8 GB; node 11 ~0,45 GB; VBoxHeadless 6 ~0,14 GB.
2. Hai VM đang chạy: JX-Server-D (VM chính) và JX-Test-36 (VM thử). Hợp lệ theo quy tắc hiện tại (Q-18/Q-19), không phải VM cũ JX-Server.
3. Ổ C: 476 GB, trống 138 GB. Lớn nhất: LDPlayer 21,4 GB, Thùng rác 20 GB, Temp\claude 9,5 GB, Documents\SHAREit 9,6 GB, Downloads (ISO Win10 5,7 GB), C:\Jx1CocoV3 14,2 GB, C:\JX1 10 GB, Chrome data 4,7 GB.
4. Tự khởi động đáng ngờ về tốn tài nguyên: Run key có Steam, RiotClient, Grass, IDMan, CocCoc, Iriun Webcam, UniKey, OSLink; dịch vụ không phải Windows: CloudflareWARP, MySQL57, Sentinel x3, SHAREit, UltraViewer, HP Print Scan Doctor, Foxit x2, Corel.
5. Không thấy tiến trình codex mồ côi của task đã giết: mọi tiến trình codex của worker đều thuộc một task đang chạy (8 tiến trình; 2 tiến trình cũ từ 16/11 và ChatGPT/Codex app 15/11 là của app, không phải worker).

## Bảng đề nghị (chủ duyệt từng mục; chưa làm gì)
| Mục | Đang làm gì | RAM/Dung lượng | An toàn tắt/gỡ? | Cách tắt/gỡ | Rủi ro |
|---|---|---|---|---|---|
| Temp\claude (bộ đệm phiên Claude Code) | file tạm/đầu ra tác vụ nền | 9,5 GB | HỎI (chỉ sau khi đóng phiên) | xóa thư mục con cũ khi không có phiên | phiên đang mở có thể mất đầu ra tác vụ |
| Documents\SHAREit | thư mục nhận file SHAREit | 9,6 GB | HỎI (có thể là dữ liệu của chủ) | chủ xem rồi xóa/dời sang D | mất file nếu không sao lưu |
| Downloads\Win10_22H2 ISO | ảnh cài Windows | 5,7 GB | HỎI | dời sang D | cần lại nếu dựng VM mới |
| Thùng rác ổ C | file đã xóa | 20 GB | CÓ (chủ quyết) | Empty Recycle Bin | xóa vĩnh viễn |
| LDPlayer | giả lập Android | 21 GB | KHÔNG (đang dùng test) | giữ | dự án dùng |
| C:\Jx1CocoV3 | kho làm việc chính | 14,2 GB | KHÔNG | giữ | - |
| C:\JX1 | bản cũ/dữ liệu JX | 10 GB | HỎI | xem nội dung rồi dời sang D | chưa rõ nội dung |
| Chrome data (AppData\Local\Google) | hồ sơ/trình duyệt | 4,7 GB | HỎI | Chrome > xóa dữ liệu duyệt | đăng xuất site |
| CocCoc | trình duyệt Cốc Cốc + task cập nhật | 2,1 GB + tự chạy | CÓ nếu không dùng | gỡ ứng dụng hoặc tắt khởi động cùng Windows | mất hồ sơ Cốc Cốc |
| Steam, RiotClient, Grass, IDMan, Iriun, UniKey, OSLink (Run) | tự mở khi đăng nhập | Iriun 157 MB đang chạy | CÓ (tắt khởi động cùng Windows) | Task Manager > Startup > Disable | mất tiện ích khi không mở tay; Grass là app chia sẻ băng thông, nên rà lại |
| MySQL57 (dịch vụ) | cơ sở dữ liệu | chưa đo | HỎI (có thể dự án cần) | đặt Manual | nếu client/server dùng thì hỏng |
| Sentinel x3, Corel, Foxit x2, HP Doctor, SHAREit, CloudflareWARP, UltraViewer | dịch vụ nền của phần mềm khác | nhỏ | HỎI từng mục | đặt Manual | UltraViewer/WARP có thể đang dùng để điều khiển từ xa |
| Task Scheduler JX-*: ADMIN-firewall/kill-test-vm/service/trustedhosts | tác vụ ADMIN của dự án (đang Ready) | không | KHÔNG | giữ | dùng cho vận hành |
| Task JX-codex-<ID> | worker Codex | ~100 MB mỗi worker | KHÔNG khi đang chạy | tự gỡ khi task xong | - |

## Chưa kiểm tra
- Tổng RAM vật lý và RAM theo Private Bytes chính xác (WMI lỗi; dùng Get-Process).
- Kích thước hiberfil/pagefile (không đọc được bằng Get-Item).
- VBoxHeadless dùng RAM của VM thật (chỉ thấy phần tiến trình máy chủ; RAM cấp cho VM do VirtualBox giữ, đo bằng `VBoxManage showvminfo` nếu cần).
- Chi tiết top 20 thư mục trong Program Files (47 GB) và Program Files (x86) (17,7 GB).
- Hoàn tác: các thay đổi trên đều chưa làm; khi làm sẽ ghi lệnh hoàn tác cạnh từng mục.
