# ĐƯỜNG VÀO VM TEST-36 DÙNG CHUNG (A và B) — Q-79 / #249

Công cụ: `JX1_OPS/TOOLS/vm_chay.py` (danh sách trắng, chỉ tới 192.168.56.150 = Test-36, không bao giờ Main VM).
Mật khẩu lấy từ Credential Manager của máy thật (`jxlab_cred.ps1`); người gọi không thấy, không in, không ghi file.

```
python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py chain-up          # chạy task JX-ChainUp (idempotent) + 8 dòng chain_up.log
python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py ports             # cổng nghe 5001-5005/56722/56732/51189 + tiến trình
python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py log bishop 50     # n dòng cuối log mới nhất (bishop|goddess|relay|gs; n<=200)
python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py ten-co Cctesterone  # tên nhân vật có trong roledb không (CO/KHONG)
```
Giới hạn đã biết: `chain-up` thấy chuỗi đã sống thì không khởi động lại (không kill). `ten-co` chỉ đọc byte ASCII của `gw\database\roledb` (Berkeley DB); dữ liệu chưa ghi xuống đĩa có thể chưa thấy; tên phải ASCII 3-24 ký tự. Khi cần lệnh mới: thêm vào BLOCKS trong tệp, giữ danh sách trắng.
Kiểm 19/11 17:00: ports OK; ten-co T36nv1=CO; Tsbaone, Cctesterone = KHONG (nghĩa là các nhân vật này CHƯA được tạo trong Test-36).
