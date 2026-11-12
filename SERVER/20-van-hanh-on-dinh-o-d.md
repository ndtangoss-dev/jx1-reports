# 20 - Khôi phục tự động 2 cổng và vận hành ổn định trên ổ D

Ngày: 2026-11-11

## TÓM TẮT 5 DÒNG
1. Sau mỗi lần máy thật khởi động lại, `portproxy` không đáng tin: luật còn nhưng không nghe. Forwarder Python chạy được mà không cần Admin.
2. Đề xuất chính: tác vụ của người dùng, chạy lúc bạn đăng nhập, chờ địa chỉ Tailscale rồi mở forwarder (`khoi_dong_forwarder.ps1`); chưa đăng ký, chờ duyệt.
3. Phương án gốc (Admin): `Restart-Service iphlpsvc` sau khi Tailscale lên; chỉ soạn thành đề xuất, chủ máy đã dặn không tự làm.
4. VM đang chạy là `JX-Server-D` (ổ D còn 1.638,8 GB trống, VM 41,8 GB); VM cũ trên C chiếm khoảng 142,7 GB, giữ nguyên, ổ C chỉ còn 20,2 GB.
5. Việc cần chủ máy: duyệt đăng ký tác vụ forwarder; xác nhận có trigger tự chạy cho 6 tác vụ `JX-*` trong VM.

**Cần tôi quyết định: có** - mục 1 (đăng ký tác vụ forwarder) và mục 4 (khi nào dọn VM cũ).

## 1. Phương án khôi phục 2 cổng 56722 / 51189 sau reboot máy thật

| # | Phương án | Cần Admin | Ưu | Nhược |
|---|---|---|---|---|
| A | Tác vụ người dùng lúc đăng nhập chạy `khoi_dong_forwarder.ps1` (chờ địa chỉ Tailscale tối đa 180 s) | Không | Không đụng dịch vụ hệ thống, hoàn tác bằng 1 lệnh, đã có sẵn forwarder chạy tốt | Chỉ chạy khi bạn đăng nhập; mất khi tắt tiến trình |
| B | Admin: tác vụ lúc khởi động (SYSTEM) chạy `Restart-Service iphlpsvc` sau khi Tailscale có địa chỉ | Có | Giữ `portproxy` chuẩn, không cần Python | Đụng `iphlpsvc` (chủ máy đã dặn không tự làm); nguyên nhân gốc chưa kiểm chứng nên chưa chắc đủ |
| C | Làm tay: chạy `khoi_dong_forwarder.ps1` mỗi lần bật máy | Không | Không đổi cấu hình nào | Dễ quên |

**Khuyến nghị: A, dự phòng C.** B chỉ xét nếu chủ máy muốn và có mặt để chạy `.ps1` Admin.

Script đã soạn (chỉ kiểm cú pháp, **chưa chạy**) trong `docs-analysis/scripts`:
- `khoi_dong_forwarder.ps1`: chờ địa chỉ `<TAILSCALE-IP>`, bỏ qua nếu cổng đã có tiến trình nghe (tránh đụng `portproxy` hoặc forwarder đang chạy), rồi chạy `tcp_forwarder.py` ẩn. Log `docs-analysis/out/khoi-dong-forwarder.log`.
- `dang_ky_forwarder.ps1` / `huy_dang_ky_forwarder.ps1`: tạo / xóa tác vụ `JX-Forwarder-Tailscale` (trigger đăng nhập của người dùng hiện tại). Không đụng portproxy, tường lửa, dịch vụ.
- Dừng forwarder: `dung_forwarder.ps1`.

Điều kiện: đăng ký tác vụ đổi cấu hình trên máy thật (Task Scheduler của người dùng, không phải Admin) nên **chờ chủ máy duyệt**.

Nếu portproxy tự hồi phục trong tương lai, hai cổng sẽ có hai bên cùng muốn bind: script A thoát an toàn (mã 3) khi cổng đã có người nghe. Ngược lại, nếu forwarder chiếm cổng trước thì portproxy có thể không bind được; xử lý khi gặp.

## 2. Kiểm tra sau mỗi lần máy thật khởi động lại (3 lệnh)
1. `ipconfig | Select-String <TAILSCALE-IP>` có địa chỉ Tailscale.
2. `netstat -ano | Select-String '<TAILSCALE-IP>:(56722|51189|8080)\s.*LISTENING'` đủ 3 cổng.
3. Từ điện thoại mở app; log `docs-analysis/out/forwarder.log` thấy `NHAN ket noi`.

## 3. Thứ tự bật lại hệ thống (ổ D)
1. Máy thật: Tailscale lên, chạy `khoi_dong_forwarder.ps1` (hoặc tác vụ A), chạy `cdn_server.py` (lệnh trong báo cáo 18).
2. VBox: `VBoxManage startvm JX-Server-D --type headless` (chủ máy duyệt). Chỉ một VM chạy, vì trùng MAC/IP `<LAN-IP>`.
3. Trong VM: SQL Server (tự chạy), rồi 5 exe theo thứ tự `Sword3PaySys`, `Goddess`, `S3Relay` (login root), `Bishop`, `gs001`. Mỗi exe hỏi chủ máy.
4. Có tự khởi động hay không phụ thuộc trigger của 6 tác vụ `JX-*` (chưa chắc, báo cáo 19 mục 4) và phiên `<vm-user>` đăng nhập (autologon đang tắt).
- Quan sát hôm nay: VM `JX-Server-D` đang chạy từ 08:43, phiên `mu1` đăng nhập lúc 08:44, 5 exe đang chạy (gs001 98 MB).

## 4. Dung lượng và dọn dẹp
- Ổ D: 1.638,8 GB trống / 1.863,0 GB. `D:\VMs\JX-Server-D` 41,8 GB, 37 file. Dư chỗ cho nhiều bản sao lưu.
- Ổ C: chỉ 20,2 GB trống. VM cũ `JX-Server` + 24 snapshot + `C:\VMs\JX-disk` khoảng 142,7 GB. **Không xóa** theo lệnh chủ máy; xóa sau cùng bằng `VBoxManage unregistervm JX-Server --delete`, hỏi riêng.
- Chưa tạo snapshot (dự án đang tạm dừng snapshot khi VM chạy). Đề xuất sao lưu khi VM đã tắt: `clonevm` hoặc sao chép thư mục VM sang `D:\VMs\backup-<ngày>` (cần chủ máy duyệt và VM tắt hẳn).
- Log đang tăng: `docs-analysis/out/forwarder.log`, `cdn-8080.log` (CDN đã ghi khoảng 191 dòng yêu cầu). Cần xoay vòng hoặc xóa khi dừng; không đưa vào git.

## 5. Còn mở
- Nguyên nhân thật của lỗi `portproxy` (chưa kiểm chứng).
- Trigger của 6 tác vụ `JX-*` (kết quả đọc mâu thuẫn).
- Dọn cuối: dừng CDN/forwarder, tắt WinRM, xóa `TrustedHosts`, xóa dữ liệu thật và snapshot cũ một lần, nhắc chủ máy.
