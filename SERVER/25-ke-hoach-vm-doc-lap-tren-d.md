# 25 - Kế hoạch tạo VM độc lập trên ổ D để giải phóng ổ C

Ngày: 2026-11-11. **Chỉ kiểm tra và lập kế hoạch.** Chưa đăng ký bản sao, chưa clone, chưa sửa `.vbox`, chưa xóa gì trên ổ C. Chưa commit.

## TÓM TẮT 5 DÒNG
1. Bản sao ở `D:\VMs\Backup\JX-Server-archive` chỉ phụ thuộc ổ C ở **một** chỗ: đĩa nền `C:/VMs/JX-disk/Windows 10 x64.vmdk` (dòng 15 của `.vbox`). Mô tả đĩa chênh lệch không có đường dẫn ổ khác.
2. Không cần clone: cách ngắn nhất là gỡ đăng ký VM cũ (không xóa file), sửa đúng 1 đường dẫn trong `.vbox` bản sao (có `.bak`), rồi `registervm` từ ổ D. Giữ nguyên 24 snapshot và 20 file `.sav`, không chép thêm dữ liệu.
3. Thử khởi động ở chế độ không có mạng (`--cableconnected1 off`, headless), kiểm tra bằng ảnh chụp màn hình và trạng thái VM.
4. Ước tính 15-20 phút, không cần tắt `JX-Server-D`; có rủi ro nhỏ với `VBoxSVC` dùng chung (mục 4).
5. Sau khi đạt, xóa hai thư mục trên C (duyệt riêng) sẽ đưa ổ C từ 19,8 GB lên khoảng 162 GB trống.

**Cần tôi quyết định: có** - xem mục 5.

## 1. Cấu trúc bản sao (đọc `JX-Server.vbox` trong `D:\VMs\Backup\JX-Server-archive\JX-Server`)
- Máy: tên `JX-Server`, UUID `{<uuid>}`, `snapshotFolder=Snapshots`, `currentSnapshot={82dc4b07-…}` (= `truoc-doi-ip-roledb`), 24 phần tử `<Snapshot>`.
- Media registry nằm **trong chính file `.vbox`**: 26 `HardDisk` (đĩa nền, `JX-Server.vdi` và 24 đĩa chênh lệch). `VirtualBox.xml` toàn cục **không** có `<MediaRegistry>` và không chứa UUID đĩa nền; nó chỉ có 2 `MachineEntry`: `eb2814ff…` (`C:\VMs\JX-Server\JX-Server.vbox`) và `be011bd7…` (`D:\VMs\JX-Server-D\JX-Server-D.vbox`).
- Đường dẫn tuyệt đối trong `.vbox`: chỉ 2 chỗ.
  - Dòng 15: `C:/VMs/JX-disk/Windows 10 x64.vmdk` (đĩa nền `dc6ec777…`) - **phụ thuộc ổ C**.
  - Dòng 66: `C:/Program Files/Oracle/VirtualBox/VBoxGuestAdditions.iso` - nằm trong thư mục cài đặt VirtualBox, không liên quan ổ dữ liệu.
  - Các đĩa còn lại dùng đường dẫn tương đối `Snapshots/{uuid}.vmdk` và `JX-Server.vdi`.
- 24 file mô tả đĩa chênh lệch (< 5 KB): 0 dòng chứa ký tự ổ đĩa hay `parentFileNameHint`; extent là tên tương đối. Mô tả đĩa nền `Windows 10 x64.vmdk` cũng dùng tên tương đối (16 extent trong cùng thư mục `JX-disk`).
- Không có `stateFile` trong 3 snapshot đầu đã xem; 20 file `.sav` nằm trong `Snapshots` (đã xác nhận có đủ). Chưa xem `stateFile` của cả 24 snapshot.
- Hệ quả: UUID máy và UUID đĩa trùng VM cũ đang đăng ký, nên **không `registervm` được khi VM cũ vẫn còn đăng ký**. Vì đĩa chỉ ghi trong `.vbox` nên gỡ đăng ký VM cũ là đủ để giải phóng các UUID đó.

## 2. Các cách tạo VM độc lập từ bản sao
| Cách | Thao tác | Dữ liệu thêm | Thời gian | Cần tắt VM D | Ghi chú |
|---|---|---|---|---|---|
| **Y (khuyến nghị)** | gỡ đăng ký VM cũ, sửa 1 đường dẫn, `registervm` từ D | 0 | vài phút | không | giữ nguyên snapshot và `.sav`; bản sao thành VM thật, không còn bản nguyên vẹn riêng |
| Z | `clonevm --mode all` từ VM cũ | +142,7 GB | 25-35 phút | **nên** tắt | UUID mới, không sửa `.vbox`; bản sao B còn nguyên vẹn; chưa chắc giữ `.sav` |
| X | sửa UUID máy và 25 UUID đĩa trong `.vbox` và VMDK | 0 | lâu | không | nhiều thao tác nhạy cảm, không khuyến nghị |

## 3. Kế hoạch Y chi tiết (mỗi bước chờ duyệt)
Thay đổi trên **VirtualBox** và **file `.vbox` bản sao**; không đụng file nào trên C.
1. Gỡ đăng ký VM cũ (không xóa file):
   `VBoxManage unregistervm JX-Server`
   Không có `--delete`. File trên C giữ nguyên. Hoàn tác: `VBoxManage registervm C:\VMs\JX-Server\JX-Server.vbox`.
2. Sao lưu rồi sửa đúng một đường dẫn trong bản sao, sửa theo byte:
   `Copy-Item "D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vbox" "...\JX-Server.vbox.bak"`
   thay `C:/VMs/JX-disk/Windows 10 x64.vmdk` bằng `D:/VMs/Backup/JX-Server-archive/JX-disk/Windows 10 x64.vmdk` (giữ nguyên mã hóa UTF-8, xuống dòng, không sửa chỗ nào khác). Kiểm tra bằng `Select-String` chỉ còn tham chiếu `C:/Program Files/...` (VBoxGuestAdditions.iso).
3. Đăng ký từ ổ D:
   `VBoxManage registervm "D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vbox"`
   Nếu báo trùng UUID hoặc không đọc được đĩa: dừng, báo cáo, khôi phục bằng bước hoàn tác ở bước 1.
4. Kiểm tra sau đăng ký (chỉ đọc): `VBoxManage list vms` (đúng 2 VM: `JX-Server` mới và `JX-Server-D`), `snapshot JX-Server list` (24), `list hdds` (mọi đĩa của VM nằm dưới `D:\`, không còn đường dẫn `C:\VMs`), `showvminfo --machinereadable` (`CfgFile` ở ổ D, RAM 6144, 4 CPU, EFI).
5. Ngắt mạng trước khi bật (bắt buộc, vì Windows trong VM có IP tĩnh `<LAN-IP>` trùng `JX-Server-D`): `VBoxManage modifyvm JX-Server --cableconnected1 off`. Hoàn tác: `--cableconnected1 on`.
6. Khởi động thử: `VBoxManage startvm JX-Server --type headless`. Chờ khoảng 90 giây.
7. Xác nhận hoạt động (chỉ đọc): `showvminfo` trả `VMState="running"`; `controlvm JX-Server screenshotpng <scratchpad>\jx-old-test.png` để xem màn hình đăng nhập hoặc desktop; nếu có Guest Additions thì `guestproperty enumerate`. Vì mạng ngắt nên không dùng WinRM.
8. Tắt VM: `VBoxManage controlvm JX-Server acpipowerbutton`, kiểm `poweroff`. Chưa làm gì khác với VM.
9. Giải phóng ổ C (duyệt riêng, xóa thật): `Remove-Item -Recurse` hai thư mục `C:\VMs\JX-Server` và `C:\VMs\JX-disk`. Trước đó xác nhận VM đã đăng ký từ D và `list hdds` không còn tham chiếu `C:\VMs`. Thêm tùy chọn kiểm chứng độc lập: đổi tên tạm `C:\VMs\JX-disk` rồi khởi động lại VM; không bắt buộc.

Thời gian ước tính: bước 1-4 khoảng 5 phút, bước 5-8 khoảng 5-10 phút.

## 4. Rủi ro
| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| `VBoxSVC` dùng chung với `JX-Server-D` đang chạy; trước đây từng crash (kèm snapshot live) và VM phải tắt cứng. Các lệnh trên nhẹ nhưng việc khởi động VM thứ hai thêm tải | Thấp-trung bình | làm lúc không chơi game; cân nhắc tắt `JX-Server-D` trước (anh quyết) |
| RAM: VM thử dùng 6 GB; máy thật 47,9 GB, đang trống 31,2 GB | Thấp | đủ |
| Bước 3 lỗi sau khi đã gỡ đăng ký VM cũ | Thấp | file trên C nguyên vẹn; `registervm` lại VM cũ |
| Đĩa nền lỗi do sửa sai đường dẫn | Thấp | `.bak`; so sánh trước/sau; chỉ sửa 1 chỗ |
| Bật mạng nhầm gây trùng IP `<LAN-IP>` với `JX-Server-D` | **Cao** | ngắt cáp trước khi `startvm`; kiểm `cableconnected1=off` trước khi bật |
| Khởi động làm thay đổi đĩa trạng thái hiện tại của bản sao | Thấp | các snapshot là đĩa cha bất biến; chỉ đĩa `fc58d1dc` (trạng thái hiện tại) ghi thêm; bản trên C còn nguyên cho tới bước 9 |
| Sau bước 9 không còn bản nguyên vẹn riêng của VM cũ | Trung bình | các snapshot vẫn khôi phục được; nếu cần bản nguyên vẹn thì chép thêm 142,7 GB (khoảng 20 phút) trước khi khởi động thử |

## 5. Cần làm thêm để giải phóng ổ C (ngắn nhất)
1. Chủ máy duyệt bước 1-4 (gỡ đăng ký VM cũ không xóa, sửa 1 đường dẫn, đăng ký từ D, kiểm tra).
2. Chủ máy duyệt bước 5-8 (ngắt mạng, khởi động thử, xác nhận, tắt).
3. Chủ máy duyệt bước 9 (xóa `C:\VMs\JX-Server` và `C:\VMs\JX-disk`).
Nếu muốn **ngắn hơn nữa**: làm bước 1-4 rồi xóa ở bước 9, thử khởi động sau trên ổ D. Dữ liệu đã khớp SHA256 và `.vbox` đã đăng ký đọc được đĩa, nhưng chưa chứng minh VM khởi động được; tôi khuyến nghị giữ bước 5-8 trước khi xóa.

## Chưa kiểm tra
- Bước đăng ký có thành công thật không (chưa thử).
- Máy khách bên trong có Guest Additions hay không (chỉ đoán qua tên snapshot `truoc-GA`).
- `stateFile` của cả 24 snapshot (mới xem 3).
- Trạng thái `*` của snapshot hiện tại: `currentSnapshot` trỏ `truoc-doi-ip-roledb`, nhưng `apk-bat-dau` hiện là con của nó trong cây; chưa rõ vì sao.

## Kết quả thực hiện (cập nhật 2026-11-11, sau khi chủ máy duyệt bước 1-8) - DỪNG Ở BƯỚC 5
- Bước 1 (kiểm tra trước): `JX-Server-D` đang chạy (ping đáp, 5 exe + SQL chạy), CDN 18284 và forwarder 18888 còn sống.
- Bước 2: `VBoxManage unregistervm JX-Server` (không `--delete`) thành công, exit 0. File trên C còn đủ 820 + 270 file, `JX-Server.vbox` trên C vẫn có giờ sửa 08:42:10.
- Bước 3-4: đã tạo `JX-Server.vbox.bak` trong `D:\VMs\Backup\JX-Server-archive\JX-Server`; sửa theo byte đúng 1 vị trí (dòng 15), đúng đường dẫn đĩa nền, XML hợp lệ, BOM giữ nguyên; chỉ còn tham chiếu `C:/Program Files/Oracle/VirtualBox/VBoxGuestAdditions.iso`.
- **Bước 5 THẤT BẠI**: `VBoxManage registervm "D:\...\JX-Server.vbox"` báo `E_INVALIDARG (0x80070057)` (`OpenMachine`). Đã dừng, không thử cách khác. Chưa chạy bước 6-8.
- Nguyên nhân (từ `VBoxSVC.log` lúc 04:41:09 UTC): `Cannot register the hard disk 'D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vdi' {<uuid>} because a hard disk 'C:\VMs\JX-Server\JX-Server.vdi' with UUID {7b13c650-...} already exists`. Đĩa `JX-Server.vdi` (2 MB, không gắn vào VM, `State: created`) vẫn còn đăng ký trong VirtualBox ở vị trí C sau khi gỡ đăng ký VM. `list hdds` xác nhận. Các đĩa khác (đĩa nền và 24 đĩa chênh lệch) đã được giải phóng. **Mục 1 của báo cáo này đánh giá sai: đĩa mồ côi đó có ảnh hưởng.**
- Trạng thái hiện tại: VM cũ chưa đăng ký, bản D chưa đăng ký; ổ C nguyên vẹn; `JX-Server-D` vẫn chạy bình thường; không mất dữ liệu.
- Hướng xử lý đề xuất (chờ duyệt, chưa làm): (a) `VBoxManage closemedium disk <uuid>` (không `--delete`; chỉ gỡ đăng ký đĩa mồ côi, file trên C giữ nguyên) rồi `registervm` lại; (b) hoặc hoàn tác bằng `VBoxManage registervm C:\VMs\JX-Server\JX-Server.vbox`.

## Kết quả lần thực hiện thứ hai (2026-11-11, sau khi chủ máy duyệt gỡ đăng ký đĩa mồ côi) - HOÀN TẤT BƯỚC 1-8, CHƯA XÓA C
- Kiểm tra đĩa mồ côi: `showmediuminfo disk <uuid>` và `list hdds` đều chỉ ra `C:\VMs\JX-Server\JX-Server.vdi` (2 MB, `State: created`, không có dòng "In use by VMs"); `JX-Server-D` không tham chiếu đĩa này; VM duy nhất đang chạy là `JX-Server-D`. SHA256 file trước: `C41DDA1905EF0D7C…`.
- `VBoxManage closemedium disk 7b13c650-…` (không `--delete`): exit 0. File VDI trên C không đổi (2.097.152 byte, giờ sửa 2026-11-09 22:49:15, SHA256 giống trước).
- `registervm "D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vbox"`: **thành công**, exit 0. VM mang tên `JX-Server`, UUID `<uuid>`.
- Kiểm tra sau đăng ký: `snapshot list` đủ **24**; 27 đĩa đăng ký, trong đó 26 dưới `D:\VMs\Backup\JX-Server-archive` và 1 dưới `D:\VMs\JX-Server-D`, **0 đĩa dưới `C:\`**; `.vbox` không còn `C:/VMs` (chỉ còn `C:/Program Files/Oracle/VirtualBox/VBoxGuestAdditions.iso`); 20 file `.sav`; cấu hình RAM 6144, 4 CPU, EFI, vram 128, Windows 10 64-bit, NIC bridged. So với `.bak`, `.vbox` chỉ khác đường dẫn đĩa nền (đã duyệt).
- Ngắt mạng: `modifyvm JX-Server --cableconnected1 off`, xác nhận `cableconnected1="off"` và `.vbox` có thêm `cable="false"` (thay đổi duy nhất so với bản duyệt); `JX-Server-D` vẫn `cableconnected1="on"`, không đổi. Lưu ý: MAC của VM thử nghiệm `080027AD6D3F` trùng `JX-Server-D`, nên chỉ an toàn khi cáp ngắt.
- Khởi động `startvm JX-Server --type headless`: thành công. Ảnh chụp lúc ~100 giây: "Please wait"; lúc ~3 phút: màn hình đăng nhập Windows của người dùng `<vm-user>` ("Welcome"). Ảnh trong scratchpad: `jx-old-test-1.png`, `jx-old-test-2.png`, `jx-old-test-3.png`. Không đăng nhập vào Windows, không dùng mạng.
- Tắt: `controlvm acpipowerbutton`, `poweroff` sau 117 giây (`VBox.log`: `PoweredOff`, `VBoxHeadless: exiting`).
- `JX-Server-D` trong suốt quá trình: vẫn `running`, ping 3/3, 5 exe + SQL chạy, CDN 18284 và forwarder 18888 còn sống, 3 cổng vẫn nghe.
- Trên C: `C:\VMs\JX-Server` 820 file, `C:\VMs\JX-disk` 270 file, `JX-Server.vbox` giờ sửa 08:42:10. Chưa xóa gì. Ổ C 19,7 GB trống, ổ D 1.495,9 GB.
- Lỗi/cảnh báo: `VBox.log` có các dòng `supR3HardenedErrorV ... VERR_LDRVI_NOT_SIGNED` (cảnh báo nạp DLL không ký của phía máy thật, không thấy lỗi nghiêm trọng, chưa kiểm tra có xuất hiện ở `JX-Server-D` không). `VBoxSVC.log` có `E_ACCESSDENIED ... SnapshotWrap` (25 dòng, trùng lúc đăng ký lỗi lần đầu), `VBOX_E_NOT_SUPPORTED ... not encrypted` và `VBOX_E_OBJECT_NOT_FOUND ... NVMe port 0` (các câu hỏi của `VBoxManage showvminfo`, không có ổ NVMe), `Recording not started`. Không có `Guru Meditation`, không có `FATAL`. Chưa kiểm chứng đây đều lành tính.
- Chưa kiểm chứng: VM chưa đăng nhập vào Windows nên chưa biết dịch vụ bên trong (SQL, 5 exe) còn nguyên; chưa chứng minh VM chạy khi C không còn (đĩa dưới D, nhưng chưa thử đổi tên `C:\VMs`).

## Giải phóng ổ C (2026-11-11, sau khi chủ máy chính thức duyệt xóa) - HOÀN TẤT
- Kiểm tra trước khi xóa, tất cả đạt: `JX-Server` trên D `poweroff` và đăng ký từ `D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vbox`; chỉ `JX-Server-D` đang chạy (ping 2/2); không đĩa nào đăng ký dưới `C:\`; 27 đĩa đều thuộc `D:\VMs\Backup\JX-Server-archive` (26) hoặc `D:\VMs\JX-Server-D` (1); 24 snapshot; bản sao D có JX-Server 821 file / 102,92 GB (820 + `JX-Server.vbox.bak`), JX-disk 270 file / 40,01 GB, 20 file `.sav`; `C:\VMs` chỉ chứa `JX-Server` và `JX-disk`; không reparse point; CDN và forwarder sống.
- Đã xóa **đúng hai thư mục**: `C:\VMs\JX-Server` (820 file) và `C:\VMs\JX-disk` (270 file) bằng `Remove-Item -LiteralPath ... -Recurse -Force`, mất 3 giây. `C:\VMs` (thư mục cha, đang rỗng) vẫn còn. Không xóa gì khác.
- Sau khi xóa: hai thư mục không còn; ổ C trống **162,4 GB** / 476,3 GB (trước đó 19,7 GB, tăng khoảng 142,7 GB).
- `JX-Server-D` vẫn `running` (cable on, ping 3/3, 5 exe + SQL chạy); CDN 18284 và forwarder 18888 còn sống, 3 cổng 8080/56722/51189 vẫn nghe trên `<TAILSCALE-IP>`.
- `JX-Server` trên D vẫn đăng ký, `poweroff`, `cableconnected1="off"`, 24 snapshot, 0 đĩa tham chiếu `C:\`.
- **Hệ quả:** thư mục `D:\VMs\Backup\JX-Server-archive` hiện là bản duy nhất của VM cũ, đồng thời là VM đã đăng ký. 24 snapshot còn nguyên; chỉ đĩa trạng thái hiện tại bị ghi lúc khởi động thử. `JX-Server.vbox.bak` là bản `.vbox` trước khi sửa đường dẫn đĩa.
- Chưa làm: chưa đăng nhập vào Windows của VM thử nghiệm; chưa chứng minh VM chạy hoàn toàn độc lập sau khi C bị xóa (chưa khởi động lại sau khi xóa).
- Chưa commit: `BAI_HOC.md` (sửa), báo cáo 24, 25, `docs-analysis/out/robocopy-ketqua.txt`, `quay_lai_phien.ps1`.
