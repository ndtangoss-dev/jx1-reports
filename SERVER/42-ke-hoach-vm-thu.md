# 42 - Kế hoạch VM thử (Phase 3)

**TÓM TẮT 5 DÒNG**
1. Đề xuất: full clone `JX-Server-D` (đang tắt) thành `JX-Test-36` trên D:, MAC mới, mạng **Host-only** (không ra LAN/Tailscale).
2. Dung lượng: VM gốc 42 GB; clone cần khoảng 45 GB; ổ D trống 1.491 GB.
3. VM thử có DB, nhân vật, cấu hình riêng (bản copy trong clone); không chạm EXE/cấu hình VM chính.
4. Host-only = IP riêng (vd <LAN-IP>), không trùng <LAN-IP>; hai VM có thể bật cùng lúc nếu RAM đủ (mỗi VM 6 GB).
5. Chưa tạo gì. Chờ duyệt.

Cần tôi quyết định: có

## Cấu hình VM chính (đọc bằng VBoxManage)
4 CPU, 6144 MB RAM, NIC1 bridged Realtek, MAC 080027AD6D3F, đĩa vmdk qua snapshot `{fc58d1dc...}`.

## Các bước dự kiến (sau khi duyệt)
1. `VBoxManage clonevm JX-Server-D --name JX-Test-36 --basefolder D:\VMs --mode machine --options keepdisknames? (không) --register` (clone trạng thái hiện tại, MAC tự sinh mới).
2. Đổi NIC1 sang hostonly (`vboxnet`/"VirtualBox Host-Only Ethernet Adapter"); không bridged.
3. Bật VM thử, trong VM đặt IP tĩnh host-only, sửa `gs00N_cfg.ini` Ip theo IP mới (theo byte, có .bak).
4. Chép bản build (`D:\JX-build\_bin_v2_\gs\*`) vào một thư mục riêng trong VM thử, giữ bản gốc.
5. Chạy EXE mới: hỏi riêng từng lần.

## Rủi ro
- Clone mang theo dữ liệu tài khoản thật trong DB -> chỉ ở D:, không xuất ra báo cáo.
- Đổi tên máy Windows trong clone không bắt buộc với host-only, nhưng nên đổi nếu sau này chuyển bridged.
- Tôi không có mật khẩu WinRM `<vm-admin>`; thao tác trong VM thử cần chủ máy đăng nhập hoặc cấp mật khẩu qua biến môi trường.
- Thử từ điện thoại cần bridged/Tailscale -> để sau, xin duyệt riêng.

## Kết quả thực hiện (2026-11-12 00:21)
- VM `JX-Test-36` (UUID <uuid>) tại `D:\VMs\Test\JX-Test-36`, MAC mới `080027CAE833`, NIC1 Host-only, ISO `jxbuild18-a2.iso` gắn SATA 1. Bật kiểu GUI. `JX-Server-D` vẫn `poweroff`, không đụng tới.
- Hai lần clone trước hỏng (lần 1 bị tôi dừng nhầm vì tưởng treo; lần 2 lỗi `VERR_ALREADY_EXISTS` ở NVRAM). Thư mục thừa `D:\VMs\JX-Test-36` (khoảng 42 GB, không đăng ký VM) chưa xóa, chờ duyệt.
- VM không có VirtualBox Guest Additions (là VMware Tools, có lỗi khi khởi động) nên Guest Control không dùng được. Windows tự đăng nhập <vm-user>; điều khiển bằng `keyboardputstring` + `screenshotpng`; PowerShell Admin qua UAC trong VM.
- Script `CHUAN_BI_VM_THU.PS1`: đổi IP <LAN-IP> -> <LAN-IP> trong 9 file cấu hình (`.bak-vmthu`), IP NIC <LAN-IP>/24; tạo `C:\JX\ServerA2\gs` (copy gs + 4 bin build, SHA256 khớp máy thật) + `Settings\CmdLane.ini`.
- Kiểm tra: SQL Express chạy, DB `account` ONLINE, <vm-user> là sysadmin; ra Internet bị chặn (<IP>:443 False); chưa có tiến trình server nào; 6 task `JX-*` Ready (trỏ tới bản gốc trong `C:\JX\ServerNew`).
- Chưa chạy EXE server nào trong VM thử.

## Chạy server gốc trong VM thử (2026-11-12 00:40-00:53)
- Đã chạy: PaySys (PID 572, nghe 5002), Goddess (5980, "Enable DB", nghe 5001), Bishop (6172, `[enable]`, nghe 56722/56732). Điền login Bishop bằng `C:\JX\sql\ui3.ps1` (netpass đọc trong VM, không ghi ra báo cáo).
- gs001 GỐC (PID 5048, `C:\JX\ServerNew\_bin_v2_\gs\gs001.exe`, task `JX-gs001`): nạp xong, nghe 51189 và 56732; nối Goddess 5001 và Bishop 56732 (ESTABLISHED). Bishop báo "Khởi động hoàn tất", GameServer <LAN-IP>:61802. Chưa đọc được dòng "Server start succeeded" trong log (lệnh tìm kiếm không hiện kết quả).
- Lỗi "reconnect failed" tới Tong/Chat/Transfer là đúng vì S3Relay chưa chạy (theo quy định).
- Chưa chạy: S3Relay (đúng quy định), A2.
- Chưa dừng được gs001 gốc: `Stop-Process` báo Access denied (tiến trình chạy Admin qua task). Cửa sổ PowerShell không quyền Admin bị kẹt hộp thoại Find của console; chưa có chuột để bấm Cancel.
- Một lần gõ lệnh đã rơi vào cửa sổ console gs001 (không thấy phản hồi). Ghi nhận để kiểm tra log gs001.
- Phát hiện: VM đang Host-only, IP <LAN-IP>. Card Host-only trên máy thật chỉ có <IP>, không nằm trong <LAN-IP>/24 -> máy thật và LDPlayer KHÔNG kết nối được VM này. Muốn test bằng LDPlayer cần đổi cấu hình mạng trên máy thật (ngoài VM, cần duyệt) hoặc chuyển VM thử sang bridged.
- Cấu hình IP công khai gs001 vẫn là <TAILSCALE-IP> (Tailscale máy thật), chưa sửa trong bản ServerA2.
- 00:55: vẫn chưa dừng gs001 gốc. Cửa sổ PowerShell không quyền Admin trong VM bị kẹt chu kỳ Find <-> Start menu khi gửi phím (Esc, Alt+F4 không thoát). Lệnh `Stop-ScheduledTask JX-gs001` chưa được chạy hợp lệ. Cần người bấm trong VM: đóng cửa sổ PowerShell bị kẹt, rồi báo lại.
- Trạng thái VM: gs001 gốc vẫn chạy, A2 chưa khởi động, S3Relay chưa chạy.

## WinRM từ máy thật tới VM thử (2026-11-12 ~01:05)
- Máy thật: TrustedHosts đổi từ `*` sang `<LAN-IP>` (Set-Item, phiên Admin). WinRM Running, Automatic.
- `Test-WSMan <LAN-IP>` thất bại (0x80070... WinRM không hoàn tất thao tác); `Test-NetConnection <LAN-IP> -Port 5985`: TCP False, Ping False.
- Nguyên nhân: VM thử dùng card Host-only (dải 192.168.56.x), còn IP <LAN-IP> nằm trên NIC ảo đó. Máy thật không có địa chỉ trong <LAN-IP>/24 trên card Host-only (<LAN-IP>), và route <LAN-IP>/24 đi qua card Realtek <LAN-IP> không tới được VM.
- <LAN-IP> (MAC <mac>) trả ping, không có 5985; khả năng cao là DHCP server của VirtualBox Host-only, chưa xác minh.
- Chưa thử Invoke-Command: không tới được VM. Dự kiến: <vm-user> không mật khẩu thường bị chặn đăng nhập mạng (LimitBlankPasswordUse) - CHƯA KIỂM CHỨNG.
- Không đổi JX-Server-D.

## Chuyển JX-Test-36 sang Bridged (2026-11-12 ~01:20)
- `controlvm JX-Test-36 nic1 bridged "Realtek PCIe GbE Family Controller #2"` (card LAN đang dùng, <LAN-IP>). MAC VM thử 080027CAE833. Không đụng JX-Server-D (poweroff, MAC 080027AD6D3F, vẫn bridged cấu hình cũ, không khởi động).
- IP VM: vẫn tĩnh <LAN-IP>/24 (đặt từ trước). CHƯA chuyển DHCP: chưa kiểm tra dải DHCP của router.
- Ping hai chiều: OK (TTL 128, <1 ms). ARP: <LAN-IP> = <mac>.
- WinRM: Test-WSMan trả "Access denied" (code 5) = dịch vụ có trả lời, chỉ từ chối xác thực. Invoke-Command với <vm-user> mật khẩu trống bị từ chối "Access denied". Dừng theo bước 5. Không đặt mật khẩu.
- TrustedHosts máy thật = <LAN-IP>.
- Cổng từ máy thật tới VM: 56722 OPEN (Bishop), 51189 OPEN (gs001), 5001/5002/56732 CLOSED từ LAN (nội bộ, đúng thiết kế), 3389/445/5985 chưa đối chiếu đủ (test bị treo, dừng).
- Portproxy + forwarder trên máy thật vẫn trỏ <LAN-IP> (VM cũ đã tắt): đường Tailscale <TAILSCALE-IP>:56722/51189 hiện KHÔNG tới VM thử. Muốn sửa cần đổi forwarder/portproxy (cần duyệt).
- gs001 vẫn là bản gốc đang chạy, IP quảng bá <TAILSCALE-IP> (Tailscale). Chưa đổi cấu hình, chưa khởi động lại.
- Điện thoại qua LAN: chưa kiểm chứng; APK hiện nhúng <LAN-IP> (cần build lại nếu dùng LAN).
