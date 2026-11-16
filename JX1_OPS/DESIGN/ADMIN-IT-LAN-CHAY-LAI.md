# #008 - Giam so lan chu may phai chay lai setup Admin (Sonnet, 2026-11-17)

## Hien trang (da kiem trong ma)
- setup_quyen_admin.ps1 tao C:\ProgramData\JX1_ADMIN (chu so huu Administrators, nguoi thuong chi doc/chay, rieng req\ ghi duoc), 4 task JX1-ADMIN-<job> chay SYSTEM, runner jx1_admin_runner.ps1 + allowed.json. Setup giu allowed.json cu, chi them khoa moi.
- Yeu cau (req\<job>.json) la du lieu KHONG tin cay; runner kiem theo allowed.json. => Thay doi LOGIC runner hoac them LOAI viec moi = phai chay lai setup (vi chi Admin ghi duoc bin\).

## Nguyen tac khong doi
Nguoi dung thuong khong bao gio duoc ghi ma chay duoi SYSTEM. Moi cach "tu cap nhat" phai co thu ma nguoi dung thuong khong gia mao duoc.

## De xuat (de chu may chon 1 cau)
A. **Cho phep thay doi tham so khong can chay lai** (da co): them IP/cong/vm vao danh sach cho phep -> van phai Admin (allowed.json). De xuat A+: tach allowed.json thanh 2 phan: `allowed.fixed.json` (Admin) va `allowed.requests\` khong dung. KHONG nen: de nguoi thuong sua danh sach cho phep.
B. **Nang cap runner bang chu ky**: chu may tao 1 khoa ky (private key giu offline/the USB hoac trong may chu may, khong dua cho PM), public key dat trong bin\ luc setup. Runner chi nhan ban cap nhat `bin\update\*.ps1` neu co chu ky hop le. Moi lan sua runner: chu may chay 1 lenh ky (khong can UAC), khong phai chay lai setup. Nhuoc: chu may van phai thao tac moi lan, nhung lenh ngan va khong dong vao he thong. PM khong the tu ky.
C. **Giu nguyen, gom nhieu loi vao mot ban**: PM dry-run moi truong hop, danh sach loi biet truoc gom vao 1 setup duy nhat; chi chay lai khi co loi moi. Don gian nhat, khong them be mat tan cong.

Khuyen nghi: C ngay bay gio (khong rui ro), B chi khi chu may muon va chap nhan giu khoa ky. Khong trien khai A/B qua dem: la thay doi bao mat ngoai quyen ca dem.

## Danh sach loi/diem da biet can gom vao ban setup ke tiep
1. kill-test-vm: SYSTEM khong thay VM cua nguoi dung -> da doi sang doc PID tu VBox.log (da co o commit 396cda4).
2. (Cac muc con lai chua duoc chu may bao; PM chua phat hien loi moi tu 00:05. Se bo sung khi gap.)
