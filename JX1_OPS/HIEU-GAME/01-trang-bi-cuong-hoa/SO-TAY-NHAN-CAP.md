# SỔ TAY: nhãn "[cấp N]" trên tooltip trang bị (S-2, A, 21/11)
Nguồn đọc mã qh9A (chưa thử trên máy, chỉ đọc mã):
- Tooltip: `Classes/vn/gameui/KuiItemdescVN.cpp` (~dòng 1230-1283). `nItemLevel = Item[uId].GetLevel()` (dòng 171).
- Trang bị thường (`nItemGenre == 0`): chuỗi `CLIENT_UI_CAP_ITEM` = "%s [cấp %d]" (file `string_vn.xml`), tên trang bị + cấp.
- Cách đổi `LevelItem` thành số hiện: nếu >10 và <100, chia theo chữ số: bội 10 thì `Level/(Level/10)` (ra 10), ngược lại `Level % 10` (chữ số cuối); 100-999 tương tự với 100. Vì vậy cấp lưu dạng "10+n" hiện là n (đây có thể là chỗ cường hóa +N được mã hóa vào Level; CHƯA kiểm với dữ liệu thật).
- Khoáng/hạt (`item_mine`, loại 200-205, 131, 132, 147): chuỗi `CLIENT_UI_CAP_HT` = "[Cấp %d]" gắn sau tên.
- Bản gốc/khác: `gameui/KuiItemdesc.cpp` dùng "[%d]Lv" (dòng 921, 1953); `[%d]级` đã bị comment.
Chưa kiểm: giá trị GetLevel() do server gửi thế nào cho phi phong; Chưa kiểm hiển thị thực tế.
