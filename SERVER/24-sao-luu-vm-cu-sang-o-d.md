# 24 - Sao lưu nguyên trạng VM cũ `JX-Server` sang ổ D (lớp B)

Ngày: 2026-11-11. Báo cáo này chưa được commit theo yêu cầu của chủ máy.

## TÓM TẮT 5 DÒNG
1. Đã sao chép `C:\VMs\JX-Server` và `C:\VMs\JX-disk` sang `D:\VMs\Backup\JX-Server-archive\{JX-Server,JX-disk}` bằng `robocopy`, chạy từ 12:18:59 đến 12:38:10 (khoảng 19 phút).
2. Cả hai lệnh trả mã thoát 1 (đã chép file, không lỗi); FAILED = 0, Mismatch = 0, không có file bị khóa.
3. 1.090 file / <IP> byte (142,69 GiB) ở nguồn và bản sao khớp tuyệt đối: tên, kích thước, giờ sửa và SHA256 từng file.
4. Đủ 24 snapshot (đọc từ `.vbox` bản sao, không dùng VirtualBox) và đủ 20 file `.sav` (70,08 GB).
5. Không xóa, không di chuyển, không sửa gì ở ổ C; không đụng VirtualBox, VM, SQL, CDN, forwarder, 5 exe.

**Cần tôi quyết định: không.** Việc xóa VM cũ để giải phóng ổ C vẫn **chưa làm** và cần duyệt riêng.

## 1. Kiểm tra trước khi chép
- Ổ D: 1.638,8 GB trống, cần khoảng 142,7 GB. Đủ.
- Đích `D:\VMs\Backup\JX-Server-archive` và `D:\VMs\Backup` chưa tồn tại, nên không có gì bị ghi đè. Lệnh có chốt dừng nếu đích đã tồn tại.
- Nguồn: `C:\VMs\JX-Server` 820 file (110.249.640.752 byte), `C:\VMs\JX-disk` 270 file (42.962.505.311 byte). Các file ở thư mục gốc `JX-Server` mở đọc được, không bị khóa.

## 2. Lệnh đã chạy
```
robocopy "C:\VMs\JX-Server" "D:\VMs\Backup\JX-Server-archive\JX-Server" /E /COPY:DAT /DCOPY:DAT /R:1 /W:1 /IPG:5 /NP /NDL /LOG:docs-analysis\out\robocopy-jxserver.log
robocopy "C:\VMs\JX-disk"   "D:\VMs\Backup\JX-Server-archive\JX-disk"   /E /COPY:DAT /DCOPY:DAT /R:1 /W:1 /IPG:5 /NP /NDL /LOG:docs-analysis\out\robocopy-jxdisk.log
```
Không dùng `/MIR`, `/MOVE`, `/PURGE`. Không dùng VBoxManage.

## 3. Kết quả robocopy
| Nguồn | Mã thoát | Dirs | Files | Bytes | Copied | Skipped | Mismatch | FAILED | Thời gian |
|---|---|---|---|---|---|---|---|---|---|
| JX-Server | 1 | 3 | 820 | 102,677 g | 820 | 0 | 0 | 0 | 13 phút 59 giây (~131 MB/s) |
| JX-disk | 1 | 5 | 270 | 40,011 g | 270 | 0 | 0 | 0 | 5 phút 11 giây (~138 MB/s) |

Mã thoát 1 của robocopy = "đã chép file, không lỗi". Harness báo task nền là "failed" chỉ vì mã thoát khác 0 của lệnh cuối cùng. Không có dòng ERROR/Access is denied/being used trong log.

## 4. Đối chiếu
- Số file và byte: JX-Server 820 / 110.249.640.752; JX-disk 270 / 42.962.505.311, cả nguồn và bản sao, khớp.
- So danh sách (tên tương đối + kích thước + giờ sửa UTC): 0 khác biệt ở cả hai thư mục.
- `.sav`: nguồn 20, bản sao 20 (70,08 GB). Snapshots của bản sao: 768 `.vmdk` + 23 `.nvram` + 20 `.sav`.
- Snapshot: `JX-Server.vbox` bản sao có **24** phần tử `<Snapshot>`, nguồn cũng 24; tên và thứ tự khớp báo cáo 23 (`0-nguyenban` đến `apk-bat-dau`).
- **SHA256:** băm toàn bộ 1.090 file ở nguồn (21,2 phút) và bản sao (22,5 phút): 1.090 dòng mỗi bên, 0 dòng khác nhau, 0 file thiếu, 0 hash lệch, mọi hash hợp lệ 64 ký tự. Tổng byte đã băm <IP>, trùng tổng byte nguồn.
- Ví dụ hash trùng khớp: `JX-Server.vbox` `F60FA8CDC3F56818…`, `Windows 10 x64.vmdk` (file mô tả đĩa nền) `2683204574727F87…`.
- Danh sách hash đầy đủ nằm ngoài kho git, trong thư mục scratchpad của phiên: `...\scratchpad\hash-nguon.txt` và `hash-ban-sao.txt`.

## 5. Không có file nào không khớp hay không chép được
Không có file không chép được, không có file lệch hash, không có file bị khóa.

## 6. Trạng thái hệ thống sau khi chép
- Ổ C: 19,8 GB trống (không đổi, chưa xóa gì). Ổ D: 1.496,1 GB trống (giảm 142,7 GB).
- Nguồn không đổi: `JX-Server.vbox` vẫn có giờ sửa 2026-11-11 08:42:10 sau khi băm xong.
- CDN PID 18284 và forwarder PID 18888 vẫn chạy.
- Lúc kiểm tra có 3 tiến trình `VirtualBoxVM` (PID 1292, 7712, 15600). Đã tra cứu sau đó, xem mục 6b.
- `git status`: chỉ có file chưa theo dõi `docs-analysis/out/robocopy-ketqua.txt` (ghi mã thoát và giờ) và `docs-analysis/scripts/quay_lai_phien.ps1`. Không có gì được commit.

## 6b. Bổ sung: ba tiến trình `VirtualBoxVM` (tra cứu sau khi sao chép, chỉ đọc)
- `VBoxManage list runningvms` chỉ xác nhận **một** VM đang chạy: `JX-Server-D`, UUID `<uuid>`. `showvminfo` báo `VMState="running"`. **Không có VM thứ hai.**
- Ba tiến trình `VirtualBoxVM` cùng phiên 1, khởi động gần nhau lúc 08:42:31, 08:42:32, 08:42:33, sau `VBoxSVC` (PID 5344, 08:42:30):
  - PID 15600 (153 MB) có cửa sổ `JX-Server-D [Running] - Oracle VirtualBox`.
  - PID 1292 (8 MB) và 7712 (5 MB) không có cửa sổ, nhiều khả năng là tiến trình phụ của cùng VM. **Chưa xác minh chắc chắn.**
- WMI trên máy thật lỗi (`Get-CimInstance Win32_Process` báo `Invalid class`, `tasklist /v` cũng lỗi), nên **chưa kiểm tra được ParentProcessId**, đường dẫn thực thi và dòng lệnh. Muốn chắc phải dùng công cụ không dựa vào WMI; chưa làm.
- Cách tra cứu: `VBoxManage list runningvms`, `VBoxManage showvminfo JX-Server-D`, `Get-Process`. Không dừng hay đổi gì.

## 7. Lưu ý về bản sao
- Bản sao là bản **lưu trữ nguyên văn**, không đăng ký vào VirtualBox, không sửa `.vbox`. `JX-Server.vbox` bên trong vẫn trỏ đĩa nền `C:/VMs/JX-disk/Windows 10 x64.vmdk` (tuyệt đối) và trùng UUID với VM cũ nên **không được `registervm` trực tiếp** khi VM cũ vẫn còn đăng ký. Cách khôi phục: báo cáo 23, mục 7.
- Lớp A (`clonevm --mode all`) hoãn theo lệnh chủ máy.
- Chưa kiểm tra: bản sao có khởi động được hay không (chưa đăng ký, chưa chạy, theo giới hạn).

## 8. Bước tiếp theo (chưa làm, chờ chủ máy)
- Xóa VM cũ trên ổ C (`unregistervm JX-Server --delete`) để lấy lại khoảng 142,7 GB, đưa ổ C lên khoảng 162 GB trống. Cần duyệt riêng; nên làm sau khi chủ máy chốt giữ bản lưu trữ này và quyết định có cần lớp A không.
