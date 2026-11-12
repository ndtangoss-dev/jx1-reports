# 26 - Chuẩn bị reboot Windows và khôi phục phiên làm việc

Ngày: 2026-11-11. Chỉ kiểm tra và tạo script khôi phục. Không đổi cấu hình, không dừng CDN/forwarder, không tắt VM, không commit.

## TÓM TẮT 5 DÒNG
1. **CDN sẽ KHÔNG tự chạy lại sau reboot** (không có task, Run key, Startup hay dịch vụ nào cho `cdn_server.py`). Forwarder có task `JX-Forwarder-Tailscale` (đăng nhập `PC`) nhưng **chưa từng chạy, chưa thử qua reboot**.
2. Sau reboot, VM `JX-Server-D` sẽ không tự bật (`autostart-enabled=off`) và 6 task `JX-*` trong VM không có trigger nào: game chỉ chạy lại khi chủ máy duyệt bật VM và từng exe.
3. **Chưa an toàn để reboot khi `JX-Server-D` còn chạy**: cách VirtualBox xử lý VM khi Windows tắt là chưa kiểm chứng, và lần trước lưu trạng thái VM đang chạy từng làm `VBoxSVC` crash. Khuyến nghị tắt VM bằng ACPI trước (cần chủ máy cho phép).
4. Đã tạo script khôi phục `quay_lai_jx1.ps1` (resume đúng phiên `a0880e5a-…`, có lời nhắc ngữ cảnh); chạy thử bằng `claude` giả thì đúng, chưa chạy với `claude` thật.
5. Git chưa commit; các file chờ rà soát nằm ở mục 6.

**Cần tôi quyết định: có** - cách xử lý `JX-Server-D` trước khi reboot (mục 3).

## 1. CDN và forwarder: cơ chế tự khởi động (máy thật, chỉ đọc)
| Mục | CDN `cdn_server.py` | Forwarder `tcp_forwarder.py` |
|---|---|---|
| Scheduled Task | **không có** (0 task có `cdn_server` trong tham số) | `\JX-Forwarder-Tailscale`, `Ready` |
| Trigger | - | `MSFT_TaskLogonTrigger`, user `<hostname>\PC`, bật |
| Chạy dưới tài khoản | - | `PC`, `Interactive`, `RunLevel Limited` (không Admin) |
| Run key / Startup / dịch vụ | không có (HKCU/HKLM Run, thư mục Startup rỗng, không dịch vụ tên jx/cdn/forward) | không có ngoài task |
| Hành động | - | `powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Jx1CocoV3\docs-analysis\scripts\khoi_dong_forwarder.ps1"`, working directory trống (script dùng `$PSScriptRoot`) |
| Điều kiện | - | `ExecutionTimeLimit PT0S`, `MultipleInstances IgnoreNew`, `StartWhenAvailable`, chạy cả khi dùng pin, không yêu cầu mạng/nhàn rỗi |
| Lần chạy cuối | - | chưa từng chạy (`1999-11-30`, mã 267011) |
- Script `khoi_dong_forwarder.ps1` còn đúng: bind `<TAILSCALE-IP>`, chỉ nhận `<TAILSCALE-IP>`, VM `<LAN-IP>`, cổng `56722` và `51189`; chờ địa chỉ Tailscale tối đa 180 s; thoát mã 3 nếu cổng đã có người nghe; chạy `python.exe` (`C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe`) ẩn rồi `Wait-Process`.
- Dịch vụ `Tailscale` `Automatic`/Running; `iphlpsvc` Running; 2 luật `portproxy` vẫn còn trong cấu hình.

**Dự đoán sau reboot (chưa kiểm chứng):**
- CDN: **không chạy**, cổng 8080 sẽ trống. Muốn tự chạy phải tạo task riêng (chưa làm).
- Forwarder: máy thật không tự đăng nhập (`AutoAdminLogon=0`), nên task chỉ chạy sau khi chủ máy đăng nhập. Khi đó: nếu `portproxy` đã nghe lại 56722/51189 thì script thoát mã 3 (không chạy trùng); nếu không, script chờ Tailscale rồi mở forwarder. Rủi ro đã biết: task chạy trước khi Tailscale có địa chỉ thì chờ tối đa 180 s; `python` phải nằm trong PATH của người dùng; chưa thử `Wait-Process` giữ task ở trạng thái Running.
- Bên trong VM (đọc lại bằng `Get-ScheduledTask`, `Export-ScheduledTask` và `schtasks /query /xml`): 6 task `JX-*` (user <vm-user>, `InteractiveToken`) **không có trigger**. Đã giải quyết mâu thuẫn trong báo cáo 19 và 22: đọc ba cách đều không thấy trigger, nên 5 exe **sẽ không tự lên** khi VM khởi động. Autologon của VM cũng tắt (`0`).
- Hệ quả: sau reboot trò chơi ngừng cho tới khi bật `JX-Server-D`, đăng nhập `<vm-user>` và chạy từng exe (mỗi exe cần chủ máy duyệt theo quy tắc an toàn).

## 2. Trạng thái trước reboot
- VirtualBox: `JX-Server-D` `running` (RAM 6144, cáp mạng `on`, MAC `080027AD6D3F`); `JX-Server` `poweroff`, cáp `off`, cùng MAC (không được bật mạng khi `JX-Server-D` còn chạy). Cả hai `autostart-enabled=off`. `JX-Server-D` không có snapshot.
- Trong VM: 5 exe + SQL Server chạy (kiểm tra lần gần nhất), ping `<LAN-IP>` đáp.
- Máy thật: CDN PID 18284 (từ 09:37) và forwarder PID 18888 (từ 10:10:37) nghe `<TAILSCALE-IP>:8080/51189/56722`.

## 3. Phần cần chủ máy quyết: `JX-Server-D` trước khi reboot
- VM đang chạy qua cửa sổ `VirtualBoxVM`. Không có cấu hình riêng về hành động khi đóng (`GUI/DefaultCloseAction` không đặt) nên hành vi khi Windows tắt là **chưa kiểm chứng**; có thể là lưu trạng thái hoặc tắt cứng. Lần trước, lưu trạng thái khi server đã nạp đầy bộ nhớ (gs001 khoảng 1,3 GB) từng làm `VBoxSVC` crash và VM tắt cứng.
- **Khuyến nghị:** tắt `JX-Server-D` bằng ACPI (`VBoxManage controlvm JX-Server-D acpipowerbutton`, chờ `poweroff`), để SQL Server đóng sạch. Cái giá: game ngừng cho tới khi bật lại VM và chạy lại 5 exe. Forwarder/CDN không bị ảnh hưởng.
- Tôi **chưa tắt VM**; chờ chủ máy cho phép hoặc tự tắt.

## 4. Script khôi phục phiên Claude Code
- Lệnh duy nhất sau reboot (mở PowerShell, dán):
  `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Jx1CocoV3\docs-analysis\scripts\quay_lai_jx1.ps1`
- Đường dẫn: `C:\Jx1CocoV3\docs-analysis\scripts\quay_lai_jx1.ps1`, kèm lời nhắc `quay_lai_jx1_prompt.txt` (UTF-8, cùng thư mục).
- Chức năng: chuyển vào `C:\Jx1CocoV3`; in trạng thái chỉ đọc (cổng 8080/56722/51189, task forwarder); nếu có bản ghi phiên thì chạy `claude --resume <uuid> "<lời nhắc>"`; nếu `claude` thoát lỗi trong vòng 15 giây hoặc không thấy bản ghi phiên thì mở phiên mới tại đúng thư mục với cùng lời nhắc. Không khởi động VM, không `VBoxManage`, không `git`, không xóa/sửa gì, không chứa mật khẩu.
- Đã kiểm: cú pháp (0 lỗi), 0 ký tự không ASCII trong `.ps1` (chạy đúng trên PowerShell 5.1 và 7), quét bí mật 0 dòng, đường dẫn tồn tại (thư mục dự án, `claude.exe` ở `C:\Users\<user>\.local\bin`, bản ghi phiên 23 MB, file lời nhắc), `claude --help` xác nhận `--resume <mã>` và `[prompt]`. Chạy thử toàn bộ script với `claude` giả: gọi đúng `--resume <mã> <lời nhắc>`, 3 tham số, lời nhắc 770 ký tự còn nguyên tiếng Việt; một chương trình exe thật cũng nhận đúng 3 tham số. Đã bỏ dấu nháy kép trong lời nhắc vì PowerShell 5.1 không thoát chúng khi gọi chương trình ngoài.
- **Chưa kiểm:** chưa chạy với `claude` thật (sẽ mở một phiên mới và tốn lượt); chưa biết `--resume` kèm lời nhắc đầu có hoạt động đúng trên phiên cũ 23 MB không (nếu không, phương án dự phòng mở phiên mới kèm ngữ cảnh).
- `quay_lai_phien.ps1` (571 byte, SHA256 `DBBC417C…`) giữ nguyên, không sửa; nó chỉ chuyển thư mục và `claude --resume <mã>` (không lời nhắc, dự phòng là danh sách chọn phiên). Có thể dùng làm phương án phụ.

## 5. Sau reboot (Phần 4, chỉ đọc; phiên mới đọc mục này)
1. CDN có chạy không: `Get-Process python` và `netstat -ano | Select-String '100\.95\.186\.86:8080'`; dự đoán: không.
2. Forwarder có chạy không: task `JX-Forwarder-Tailscale` (`Get-ScheduledTaskInfo`: giờ chạy, mã kết quả), `docs-analysis\out\khoi-dong-forwarder.log` (dòng "Da khoi dong forwarder PID ..." hoặc "BO QUA" hoặc "BO CUOC"), `docs-analysis\out\forwarder.log`.
3. PID mới của CDN và forwarder.
4. Cổng 8080, 56722, 51189 có `LISTENING` trên `<TAILSCALE-IP>` không; ai nghe (forwarder hay `portproxy`/`svchost`).
5. Thử nối TCP tới hai cổng forwarder (`Test-NetConnection <TAILSCALE-IP> -Port 56722`; nối từ chính máy thật sẽ bị forwarder từ chối vì chỉ cho điện thoại, nên chỉ kết luận "cổng nghe", không kết luận "game chạy"; không có dữ liệu bị gửi).
6. `JX-Server-D` (trạng thái `VBoxManage list runningvms`, tình trạng sau reboot: dự đoán `poweroff` hoặc `saved`), `JX-Server` vẫn `poweroff`.
7. Nếu task không tự chạy: xác định nguyên nhân (không đăng nhập, Python không trong PATH, Tailscale chưa có địa chỉ, `portproxy` đã nghe, lỗi script), chỉ báo cáo, **chưa tự sửa**.
- Không tự khởi động `JX-Server-D` hay `JX-Server`, không bật mạng `JX-Server`.

## 6. Git: các file chờ rà soát (chưa commit)
| File | Trạng thái | Ghi chú sơ bộ |
|---|---|---|
| `docs-analysis/BAI_HOC.md` | sửa (+17 dòng) | các bài học về `portproxy`, task, sao lưu, `registervm`, xóa ổ C. Quét bí mật: chỉ có dòng cũ (đã commit) nhắc luật cho phép `ConvertTo-SecureString`, không phải mật khẩu |
| `docs-analysis/reports/24-sao-luu-vm-cu-sang-o-d.md` | mới | báo cáo sao lưu; quét bí mật 0 dòng |
| `docs-analysis/reports/25-ke-hoach-vm-doc-lap-tren-d.md` | mới | kế hoạch và kết quả VM độc lập, xóa C; quét 0 dòng |
| `docs-analysis/reports/26-chuan-bi-reboot.md` | mới | báo cáo này |
| `docs-analysis/out/robocopy-ketqua.txt` | mới | 4 dòng mã thoát và giờ; thư mục `out/` chỉ bỏ qua `*.log`, `*.pid`, `tailscale/`. **Không nên commit** (tệp nhật ký tạm) |
| `docs-analysis/scripts/quay_lai_phien.ps1` | mới | 571 byte, không có thông tin nhạy cảm |
| `docs-analysis/scripts/quay_lai_jx1.ps1` + `quay_lai_jx1_prompt.txt` | mới | script khôi phục; nhắc IP nội bộ trong lời nhắc là không nhạy cảm; đề nghị commit sau khi chạy thử thật |
Đề nghị sơ bộ (sẽ rà soát đầy đủ sau reboot): commit 24, 25, 26, `BAI_HOC.md`, hai script khôi phục; **không** commit `robocopy-ketqua.txt`. Cần chủ máy duyệt trước khi commit.

## 7. Phạm vi đã giữ
Không đổi Scheduled Task, firewall, VirtualBox, VM, mạng; không khởi động/tắt VM; không dừng CDN/forwarder; không xóa dữ liệu; không sửa source game; không reboot; không commit. Chỉ thêm 3 file: báo cáo 26, `quay_lai_jx1.ps1`, `quay_lai_jx1_prompt.txt`, và chạy thử trong thư mục tạm của phiên.

## 8. Cập nhật: đã tắt `JX-Server-D` (chủ máy cho phép, lúc hoàn tất báo cáo)
- Chủ máy chọn "Tắt ACPI ngay". Đã chạy `VBoxManage controlvm JX-Server-D acpipowerbutton` (chỉ khi `JX-Server-D` là VM duy nhất đang chạy); VM về `poweroff` sau 92 giây, không phải tắt cứng.
- Sau đó: không còn VM nào chạy; `JX-Server-D` và `JX-Server` đều `poweroff`; `JX-Server` vẫn cáp ngắt; CDN PID 18284 và forwarder PID 18888 vẫn chạy và nghe 8080/56722/51189.
- Hệ quả: trò chơi đang ngừng cho tới khi chủ máy bật lại `JX-Server-D` và 5 exe sau reboot. Việc kiểm tra trong mục 3 đã được xử lý, **an toàn để reboot** về phía VM. Chưa đổi gì khác.
- Bằng chứng tắt an toàn (đọc `D:\VMs\JX-Server-D\Logs\VBox.log`, chỉ đọc): `ACPI: Entering S5 power state (power down)` rồi `RUNNING` → `POWERING_OFF` → `OFF` → `TERMINATED`, `Machine state changed to 'PoweredOff'`. Nghĩa là chính Windows trong VM đã chạy xong quy trình shutdown rồi mới yêu cầu cắt nguồn ảo; không có suspend/savestate, reset hay poweroff cưỡng bức (11 dòng khớp mẫu "forced/reset" chỉ là bộ đếm `ForcedFlag`/`ForcedActions` và `Resetting MMIO2` của trình ảo hóa). Không có file `.sav` của `JX-Server-D`.
- **Chưa kiểm chứng trực tiếp:** SQL Server và 5 exe đã kết thúc ra sao. VM đang tắt, không thể đọc tiến trình qua WinRM và không được bật VM; chỉ suy ra gián tiếp từ việc Windows vào S5. Khi VM được bật lại (cần chủ máy duyệt), đọc `ERRORLOG` của SQL Server (tìm dòng dừng theo yêu cầu của Service Control Manager) và log `gw`/`gs` để xác nhận.
