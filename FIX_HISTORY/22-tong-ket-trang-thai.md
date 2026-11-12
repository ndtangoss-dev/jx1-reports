# 22 - Tổng kết trạng thái hiện tại

Ngày: 2026-11-11. Chỉ là tài liệu: báo cáo này không thay đổi hệ thống.

## TÓM TẮT 5 DÒNG
1. Game chạy thật từ điện thoại: đăng nhập `<test-account>`, vào gs001, ping khoảng 150 ms. Mọi thứ đang chạy trên VM `JX-Server-D` ở ổ D.
2. Đường vào đi qua Tailscale: CDN `<TAILSCALE-IP>:8080` và TCP Forwarder `:56722`, `:51189`, chỉ nhận điện thoại `<TAILSCALE-IP>`.
3. Task `JX-Forwarder-Tailscale` đã đăng ký (Ready) nhưng **chưa từng chạy**; forwarder tự khởi động sau reboot **chưa được thử**.
4. VM cũ `JX-Server` trên ổ C và 24 snapshot **vẫn phải giữ, chưa xóa**.
5. **Không được xem hệ thống là độc lập hoàn toàn cho đến khi kiểm tra reboot thành công.**

**Cần tôi quyết định: không** (các việc còn treo ở mục 9-10, chờ chủ máy).

## 1. VM `JX-Server-D` (ổ D)
- `D:\VMs\JX-Server-D\JX-Server-D.vbox`, 41,8 GB, 37 file, không có snapshot. Nhân bản từ `JX-Server` ngày 2026-11-11 (báo cáo 17), giữ MAC `080027AD6D3F`, IP bridged `<LAN-IP>`. Đang `running` (khởi động 08:43; phiên `mu1` đăng nhập 08:44; autologon tắt; `autostart-enabled=off` nên VirtualBox không tự bật VM).
- Hai VM cùng MAC/IP nên không bao giờ bật cả hai cùng lúc. Ổ D còn 1.638,8 GB trống.
- Dự án tạm dừng tạo snapshot khi VM chạy (live snapshot từng làm `VBoxSVC` crash).

## 2. SQL Server và 5 EXE (trong VM)
- SQL Server `MSSQL$SQLEXPRESS`: Running, Automatic.
- 5 exe chạy bằng tác vụ `JX-*` (user `<vm-user>`, Interactive). Giờ khởi động hôm nay: `Sword3PaySys` 09:04 (cổng 5002), `Goddess` 09:06 (5001), `S3Relay` 09:08 (5003-5005, 7776), `Bishop` 09:14 (56722, 56732), `gs001` 09:15 (51189; 772 bản đồ nạp, 28 lỗi do thiếu `.wor`). Đọc lại hôm nay: cả 5 tiến trình còn chạy, các cổng trên đều đang nghe.
- Tác vụ `JX-UI` trỏ tới `C:\JX\sql\console.ps1 -TargetPid 7600`; 6 script trợ giúp còn trong `C:\JX\sql` (báo cáo 19 mục 4).
- Dữ liệu và log thật (tài khoản `<test-account>`) nằm trong VM; `account.sql` còn trong lịch sử git (báo cáo 06).

## 3. CDN cổng 8080 (máy thật)
- `cdn_server.py` PID 18284 (từ 09:37), bind `<TAILSCALE-IP>:8080`, `--allow <TAILSCALE-IP>`. Chỉ đọc; nguồn khác 403, POST 501. Log `docs-analysis/out/cdn-8080.log` (git bỏ qua).
- Cổng 80 bị `http.sys` giữ cho `ReportServer` (Running, Automatic); chủ máy cấm dừng/đổi nên dùng 8080. Client lấy địa chỉ từ `down=` trong `package.ini` của APK.
- CDN **không** tự khởi động lại sau reboot và chưa có tác vụ nào cho nó.

## 4. TCP Forwarder cổng 56722 và 51189 (máy thật)
- `tcp_forwarder.py` PID 18888 (từ 10:10:37): `<TAILSCALE-IP>:56722` → `<LAN-IP>:56722` và `:51189` → `<LAN-IP>:51189`. Chỉ nhận `<TAILSCALE-IP>`, từ chối bind `0.0.0.0`/`::`, không ghi nội dung gói.
- Tồn tại vì `iphlpsvc`/`portproxy` không nghe sau khi máy thật reboot (nguyên nhân gốc chưa kiểm chứng; báo cáo 19). Hai luật `portproxy` vẫn nằm trong cấu hình, không đụng.
- Dừng: `docs-analysis/scripts/dung_forwarder.ps1`.

## 5. Task `JX-Forwarder-Tailscale`
- Ready, user `<hostname>\PC`, Interactive, Limited, trigger `AtLogOn` (user trên), chạy `khoi_dong_forwarder.ps1`. Chưa từng chạy. Chi tiết: báo cáo 21.
- Thiết kế: chờ địa chỉ Tailscale tới 180 s; thoát mã 3 nếu cổng đã có người nghe (hiện forwarder 18888 chiếm chúng); `Wait-Process` để giữ tiến trình con.
- **Chưa kiểm chứng bằng reboot:** Task Scheduler có giữ forwarder sống không, có chờ đúng Tailscale không. `forwarder.log` bị ghi đè mỗi lần khởi động.

## 6. Cấu hình Tailscale
- Máy thật `desktop-5ngfn70` `<TAILSCALE-IP>`; điện thoại `xiaomi-13t-pro` `<TAILSCALE-IP>` (lúc kiểm tra: offline, thấy lần cuối 4 phút trước).
- `gs001_cfg.ini` `[GameServer] Ip` và `localIp` trong VM đặt `<TAILSCALE-IP>` (`Ip` phải chứa `localIp`). Client: `0_Address` mã hóa trỏ `<TAILSCALE-IP>`; `down=` trỏ `<TAILSCALE-IP>:8080`.
- Firewall: theo ghi nhận cũ, luật `Tailscale-In` cho mọi cổng vào địa chỉ Tailscale của máy thật, nên giới hạn người truy cập do `--allow` của hai script Python đảm nhiệm; VM có 6 luật `JX*`. **Không đọc lại được luật `Tailscale-In` hôm nay** (lệnh trả về trống). Không thay đổi Firewall trong đợt này.
- Chưa kiểm ACL phía quản lý Tailscale.

## 7. File sao lưu và phương án hoàn tác
| Việc | Sao lưu / công cụ |
|---|---|
| `package.ini` APK (đổi `down=`) | `D:\Android\b\backup-cdn8080\package.ini.orig`; bản chế độ Tailscale cũ ở `D:\Android\b\mode-tailscale\` (build.gradle, network_security_config.xml, package.ini, strings.xml) |
| APK | `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` (78.901.355 byte, SHA256 `82674B16…`); APK cũ trong `D:\Android\b\apk\` |
| Forwarder đang chạy | `dung_forwarder.ps1` |
| Task tự khởi động | `huy_dang_ky_forwarder.ps1` (không dừng forwarder) |
| Tailscale/portproxy/Firewall (nếu từng dùng) | `tailscale_mo_cong.ps1` / `tailscale_hoan_tac.ps1` |
| ReportServer | `tam_dung_reportserver.ps1` / `bat_lai_reportserver.ps1` (chưa dùng; chủ máy cấm dừng) |
| VM trên ổ C | `JX-Server` + 24 snapshot là bản hoàn tác của bản clone |

## 8. VM cũ và snapshot (BẮT BUỘC GIỮ)
- `JX-Server` vẫn đăng ký, đang tắt; khoảng 142,7 GB trong `C:\VMs`, ổ C còn 20,2 GB.
- 24 snapshot **chưa được xóa** (số 24 từ lần kiểm tra khi nhân bản; hôm nay không đếm lại). `C:\VMs\JX-disk\Windows 10 x64.vmdk` là đĩa nền của chuỗi snapshot, **không xóa riêng**.
- Chỉ xóa sau khi chủ máy duyệt rõ ràng, hỏi riêng, bằng `unregistervm JX-Server --delete`.

## 9. Những vấn đề chưa kiểm chứng
1. Forwarder tự khởi động sau reboot máy thật (task chưa từng chạy).
2. Nguyên nhân thật khiến `portproxy` không nghe sau reboot (giả thuyết: `iphlpsvc` lên trước adapter Tailscale).
3. CDN không tự chạy sau reboot; chưa có phương án.
4. 6 tác vụ `JX-*` trong VM có trigger tự chạy khi khởi động hay không; VM khởi động lại thì 5 exe có tự lên không.
5. Vì sao hai kết nối đầu (#2, #3) đóng sau 0,2 s trước khi đăng nhập được.
6. Nguồn chữ "XÁC NHẬN TÊN TÀI KHOẢN"/"Lưu tài khoản" trên màn đăng nhập (không có trong `Classes`).
7. Ba Lăng Huyện: đi bộ qua cổng không bật trạng thái chiến đấu; 28 bản đồ thiếu `.wor`; cổng 7777 của `S3Relay` không nghe; script NPC `5石?对话.lua` báo lỗi nạp.
8. Luật `Tailscale-In` và ACL Tailscale chưa đọc lại hôm nay.
9. Dữ liệu thật vẫn có trong lịch sử git; chưa dọn.

## 10. Việc cuối cùng còn treo
Dừng CDN/forwarder, chạy script hoàn tác nếu đã dùng, xóa dữ liệu thật và snapshot cũ một lần (sau khi chủ máy duyệt), tắt WinRM và xóa `TrustedHosts` trên máy thật, nhắc chủ máy.

**Kết luận:** hệ thống chạy được, nhưng chỉ khi các tiến trình hiện tại còn sống. Sau reboot máy thật hoặc VM, CDN, forwarder (hoặc task) và 5 exe trong VM chưa được thử lại, nên chưa được xem là độc lập.
