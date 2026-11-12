# 23 - Kế hoạch sao lưu VM cũ sang ổ D để giải phóng ổ C

Ngày: 2026-11-11. **Chỉ kiểm tra và lập kế hoạch.** Chưa copy, di chuyển, xóa, hủy đăng ký hay đổi cấu hình VirtualBox. Không động tới CDN, forwarder, SQL Server, 5 exe, VM `JX-Server-D`.

## TÓM TẮT 5 DÒNG
1. VM cũ `JX-Server` (đang tắt) + đĩa nền nằm ở `C:\VMs\JX-Server` (102,68 GB) và `C:\VMs\JX-disk` (40,01 GB), tổng 142,69 GB; ổ C còn 19,8 GB.
2. Có **20 file trạng thái đã lưu `.sav` = 70,08 GB** (snapshot chụp lúc VM đang chạy) và đĩa nền được `.vbox` tham chiếu bằng **đường dẫn tuyệt đối** `C:/VMs/JX-disk/Windows 10 x64.vmdk`. Vì vậy chỉ copy thư mục `JX-Server` là chưa đủ.
3. Đề xuất 2 lớp: **B** = sao chép nguyên văn cả 2 thư mục sang `D:\VMs\Backup\JX-Server-C-archive` (an toàn, làm được ngay khi `JX-Server-D` đang chạy); **A** = `clonevm --mode all` để có bản VM đăng ký được, UUID mới, **chỉ làm khi `JX-Server-D` đã tắt**.
4. Dung lượng dự kiến: B khoảng 142,7 GB, A khoảng 142,7 GB, tổng khoảng 285 GB trên 1.638,8 GB trống. Xóa VM cũ sau này (chưa làm) sẽ đưa ổ C lên khoảng 162 GB trống.
5. Chưa chạy lệnh nào ghi dữ liệu; **chờ chủ máy duyệt từng bước.**

**Cần tôi quyết định: có** - xem mục 8.

## 1. Kết quả kiểm tra VirtualBox (VirtualBox 7.2.22r175245, chỉ đọc)
| Mục | Giá trị |
|---|---|
| Tên / UUID | `JX-Server` / `<uuid>` (hardware UUID trùng) |
| File `.vbox` | `C:\VMs\JX-Server\JX-Server.vbox` (sửa lần cuối 2026-11-11 08:42:10) |
| Thư mục snapshot | `C:\VMs\JX-Server\Snapshots` (811 file, 102,67 GB) |
| Thư mục log | `C:\VMs\JX-Server\Logs` (5 file, ~3,5 MB) |
| NVRAM | `C:\VMs\JX-Server\JX-Server.nvram` (+ 23 file `.nvram` trong Snapshots, 0,01 GB) |
| Trạng thái | `poweroff` (từ 2026-11-10 18:14:22). VM đang chạy duy nhất: `JX-Server-D` |
| Cấu hình | RAM 6144 MB, 4 CPU, EFI, vram 128, Windows 10 64-bit, NIC1 bridged `Realtek PCIe GbE Family Controller #2`, MAC `080027AD6D3F` (trùng với `JX-Server-D`) |
| Đĩa đang gắn | `SATA-0-0` = `Snapshots\{<uuid>}.vmdk` (đĩa trạng thái hiện tại) |
| Snapshot | **24**, một chuỗi tuyến tính từ `0-nguyenban` đến `apk-bat-dau`; dấu `*` ở `truoc-doi-ip-roledb` (không diễn giải thêm) |

Chuỗi snapshot theo thứ tự: `0-nguyenban`, `sach-1`, `sach-2-ip`, `truoc-GA`, `buoc0-truoc-winrm`, `b1-truoc-sql`, `b2-truoc-account`, `c1-truoc-sua-ip`, `c2-truoc-cau-hinh`, `c2-truoc-chay-exe`, `c2-truoc-goddess`, `c2-truoc-s3relay`, `c2-truoc-bishop`, `c2-truoc-gs001`, `c2-truoc-mo-lan`, `buoc1-truoc-kiem-git`, `buoc2-ke-hoach-tailscale`, `buoc3-chuan-bi-client`, `buoc4-claude-md`, `truoc-xoa-tk-that`, `truoc-don-du-lieu-that`, `truoc-xoa-saoluu-dmp`, `truoc-doi-ip-roledb`, `apk-bat-dau`.

## 2. Vị trí toàn bộ ổ đĩa ảo (từ `list hdds` và `.vbox`)
- Đĩa nền: `C:/VMs/JX-disk/Windows 10 x64.vmdk` (UUID `dc6ec777…`, định dạng `twoGbMaxExtentSparse`, file mô tả 1.439 byte + 16 extent `-s001…-s016.vmdk`), **nằm NGOÀI thư mục VM**. Tham chiếu tuyệt đối trong `.vbox`.
- 24 đĩa chênh lệch (differencing) `Snapshots\{uuid}.vmdk`: 23 đĩa cho snapshot + 1 đĩa trạng thái hiện tại, nối tiếp từ `dc6ec777` đến `fc58d1dc`. Dữ liệu thật nằm trong 768 file extent `.vmdk` (32,58 GB) trong `Snapshots`.
- `C:\VMs\JX-Server\JX-Server.vdi` (2.097.152 byte): còn đăng ký trong media registry nhưng **không thấy gắn vào SATA**; chưa rõ công dụng (có thể là đĩa rỗng ban đầu). Không ảnh hưởng.
- Ngoài thư mục VM còn tham chiếu: `C:/Program Files/Oracle/VirtualBox/VBoxGuestAdditions.iso` (nằm trong thư mục cài đặt VirtualBox, không cần sao lưu). Ổ DVD hiện là `emptydrive`.
- Trong `C:\VMs\JX-disk` còn file của VMware (`.vmx`, `.vmsd`, `.vmxf`, log, `caches`...), không phải của VirtualBox; vẫn nên sao chép nguyên khi lưu trữ.
- `JX-Server-D.vbox` không có dòng nào tham chiếu `C:\`; đĩa của nó `D:\VMs\JX-Server-D\Snapshots\{fc58d1dc-…}.vmdk` có UUID `f32d34f1…` khác bản cũ nên **bản D độc lập hoàn toàn với ổ C** (chỉ trùng tên file). Xóa VM cũ không làm hỏng `JX-Server-D`, nhưng vẫn phải chờ chủ máy duyệt.

## 3. Dung lượng thực tế
| Thư mục | Dung lượng | File |
|---|---|---|
| `C:\VMs\JX-Server` | 102,68 GB | 820 |
| - `Snapshots\*.sav` (trạng thái lưu) | 70,08 GB | 20 (lớn nhất 13,15 GB, 4,17 GB, 3,35 GB) |
| - `Snapshots\*.vmdk` (extent + mô tả) | 32,58 GB | 768 |
| - `Snapshots\*.nvram` | 0,01 GB | 23 |
| `C:\VMs\JX-disk` | 40,01 GB | 270 |
| **Tổng** | **142,69 GB** | **1.090** |

Ổ C: 19,8 GB trống / 476,3 GB. Ổ D: 1.638,8 GB trống / 1.863,0 GB; `D:\VMs` đã có `JX-Server-D` (41,8 GB).

## 4. Thư mục đích đề xuất
- Gốc: `D:\VMs\Backup\` (chưa tồn tại; kiểm tra: `D:\VMs\Backup`, `...\JX-Server-C-archive`, `...\JX-Server-C-clone`, `D:\VMs\JX-Server-C-backup` đều chưa có). Nằm cùng ổ D với VM đang chạy nhưng tách khỏi `D:\VMs\JX-Server-D`.
- Lớp B (lưu trữ nguyên văn): `D:\VMs\Backup\JX-Server-C-archive\JX-Server` và `...\JX-Server-C-archive\JX-disk`. Giữ cấu trúc hai thư mục anh em như trên C.
- Lớp A (bản đăng ký được): `D:\VMs\Backup\JX-Server-C-clone\` do `clonevm` tạo.

## 5. Phương án sao chép
### Lớp B - sao chép nguyên văn (làm được khi `JX-Server-D` đang chạy)
Chỉ đọc nguồn, không dùng `/MIR`, `/MOVE`, `/PURGE`. Không đụng VirtualBox.
```powershell
# Tạo thư mục đích rồi chép; /IPG giãn nhịp để đỡ tranh ổ D với VM đang chạy
New-Item -ItemType Directory -Force 'D:\VMs\Backup\JX-Server-C-archive' | Out-Null
robocopy 'C:\VMs\JX-Server' 'D:\VMs\Backup\JX-Server-C-archive\JX-Server' /E /COPY:DAT /DCOPY:DAT /R:1 /W:1 /IPG:5 /NP /LOG:C:\Jx1CocoV3\docs-analysis\out\robocopy-jxserver.log
robocopy 'C:\VMs\JX-disk'   'D:\VMs\Backup\JX-Server-C-archive\JX-disk'   /E /COPY:DAT /DCOPY:DAT /R:1 /W:1 /IPG:5 /NP /LOG:C:\Jx1CocoV3\docs-analysis\out\robocopy-jxdisk.log
```
Ghi chú: bản này **không đăng ký** vào VirtualBox. `.vbox` bên trong vẫn trỏ `C:/VMs/JX-disk/...` và trùng UUID với VM cũ, nên chỉ dùng để khôi phục khi cần (xem mục 7).

### Lớp A - `clonevm --mode all` (chỉ khi `JX-Server-D` đã tắt)
```powershell
$vb='C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'
& $vb clonevm JX-Server --mode all --name JX-Server-C-clone --basefolder 'D:\VMs\Backup' --register
```
Không dùng `keepallmacs`/`keepdisknames`: bản clone nhận **UUID, hardware UUID và MAC mới**, nên không đụng `JX-Server` (`eb2814ff…`) hay `JX-Server-D` (`be011bd7…`). Hệ điều hành bên trong vẫn có IP tĩnh `<LAN-IP>`, nên **không bao giờ bật clone cùng lúc với VM đang dùng**.
Chưa kiểm chứng: `--mode all` có sao chép cả 20 file `.sav` hay không (mục 6 bước A4 sẽ phát hiện). Nếu thiếu, lớp B là bản giữ đủ.

## 6. Quy trình xác minh
### Sau lớp B
1. Số file và byte: kỳ vọng 820 + 270 file; tổng 142,69 GB (`Get-ChildItem -Recurse -File | Measure-Object Length -Sum` cho từng cặp nguồn/đích).
2. So sánh không ghi: `robocopy <nguồn> <đích> /E /L /NJH /NJS /NDL /NC /NS` không liệt kê file nào khác.
3. Băm SHA256 toàn bộ file hai phía (`Get-FileHash`), lưu danh sách vào `docs-analysis/out` (git bỏ qua) và so khớp. Ước tính 30-40 phút cho 285 GB đọc.
4. Đếm: `.sav` = 20 (70,08 GB), `.vmdk` = 768 trong `Snapshots`, `.nvram` = 23, `JX-disk` có 16 extent `-sNNN.vmdk`.
5. Nguồn không đổi: `JX-Server.vbox` vẫn có thời điểm sửa 08:42:10, `list vms` không đổi.

### Sau lớp A
- A1. `VBoxManage list vms`: có 3 VM, 3 UUID khác nhau (`eb2814ff…`, `be011bd7…`, UUID mới). Không có thông báo trùng UUID khi `--register`.
- A2. `VBoxManage snapshot JX-Server-C-clone list`: đủ **24** snapshot, đúng tên và đúng thứ tự mục 1.
- A3. `showvminfo --machinereadable` của `JX-Server-C-clone` so với bản cũ: RAM 6144, 4 CPU, EFI, vram 128, `ostype` Windows 10 (64-bit), NIC1 bridged cùng bộ điều hợp. Khác biệt duy nhất được chấp nhận: UUID, hardware UUID, MAC.
- A4. Thư mục `D:\VMs\Backup\JX-Server-C-clone`: có **20 file `.sav`** (khoảng 70 GB) và tổng khoảng 142-143 GB; số file `.nvram` khớp.
- A5. `Select-String` trong `JX-Server-C-clone.vbox`: không còn tham chiếu `C:/VMs`. `list hdds` cho thấy toàn bộ chuỗi đĩa của clone nằm dưới `D:\`.
- A6. `showmediuminfo disk <uuid>` cho đĩa cuối của clone báo `State: created`/`Accessible`. Không khởi động clone. Thử khởi động chỉ làm khi ngắt cáp NIC (`modifyvm --cableconnected1 off`), cần duyệt riêng.

## 7. Khôi phục từ lớp B (nếu một ngày VM cũ không còn trên C)
1. Chép thư mục `JX-disk` về đúng `C:\VMs\JX-disk` (hoặc sửa đường dẫn đĩa nền trong `.vbox` bằng byte, giữ `.bak`) rồi đăng ký bằng `VBoxManage registervm`. Chỉ làm khi `JX-Server` cũ đã được gỡ đăng ký, vì trùng UUID.
2. Cách khác: khôi phục bằng `clonevm` từ bản A nếu A đã đạt.

## 8. Rủi ro và việc cần chủ máy quyết
| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Sao chép 142 GB tranh ổ D với `JX-Server-D` đang chạy, game có thể giật | Trung bình | `/IPG:5`, làm lúc không chơi; theo dõi ping |
| `clonevm` qua `VBoxSVC` dùng chung với VM đang chạy; trước đây `VBoxSVC` từng crash khiến VM phải tắt cứng (với snapshot live) | Cao nếu VM D chạy | Chỉ làm lớp A khi `JX-Server-D` đã tắt (chủ máy tắt) |
| `clonevm --mode all` có thể không mang theo `.sav` | Trung bình | Bước A4; lớp B là bản dự phòng đầy đủ |
| Clone lỗi giữa chừng để lại thư mục dở | Thấp | Chỉ xóa thư mục dở khi được duyệt |
| `.vbox` của lớp B trỏ đĩa nền trên C và trùng UUID | Thấp | Không đăng ký lớp B; xem mục 7 |
| Windows Defender quét làm chậm | Thấp | Không đổi cấu hình Defender |
| Nhầm lệnh gây mất dữ liệu | Cao | Chỉ dùng lệnh ở mục 5; không `/MIR`, `/MOVE`, `unregistervm` |

**Chờ duyệt, theo thứ tự đề xuất:**
1. Làm lớp B ngay (khoảng 20-30 phút ước tính, không đụng VirtualBox)?
2. Lớp A: chủ máy tắt `JX-Server-D` lúc nào để làm?
3. Xóa VM cũ để lấy lại khoảng 142,7 GB (ổ C từ 19,8 GB lên khoảng 162 GB): **không làm trong kế hoạch này**, sẽ hỏi riêng sau khi A/B đạt.

## Chưa kiểm tra
- `--mode all` có giữ `.sav` không.
- Tốc độ copy thực tế trên máy này (số phút là ước tính từ lần clone 41,1 GB mất 6 phút).
- `JX-Server.vdi` có cần cho gì không.
- Dấu `*` trong danh sách snapshot nghĩa chính xác là gì.
