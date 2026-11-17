# QUY LUẬT VẼ BỘ PHẬN NHÂN VẬT (cập nhật 17/11, Sonnet)

## 1. Dữ liệu quyết định thứ tự vẽ
- Nam: `Settings\NpcRes\男主角贴图顺序表.ini` (1007 byte, chỉ có [DEFAULT]). Nữ: `女主角贴图顺序表.ini` (17924 byte, ~500 dòng, nhiều mục theo hành động). Mã hóa GBK. Tên file lấy từ cột "人物贴图顺序表" của `人物类型.txt` (`KNpcResNode.cpp:365-370`).
- Mỗi dòng là một "bảng sort": danh sách số bộ phận, vẽ từ trái sang phải (số đầu bị bỏ, thường -1). Bộ phận: mũ 0-3, giáp 4-7, vũ khí 8-11, ngựa 12-15, áo choàng 16-19 (`CoreUseNameDef.h`).
- Cấu trúc ini: `[DEFAULT]` Dir1..Dir24 (8 hướng đầu dùng cho đi bộ, đứng; 9..24 dùng cho cưỡi/phát sinh). `[<TênHànhĐộng>]` ghi đè: `DirN=` (cả hướng) và `LineK=<số khung>,<bảng>` (ghi đè riêng một khung). Hành động không có mục thì dùng DEFAULT.
- Tra cứu: `CSortTable::GetkTable` nạp (`KNpcResNode.cpp:1219-1380`), `GetSort` chọn (`:1390-1446`). Khung "đặc biệt" khớp khi `nFrameNo == số đầu của LineK`.
- Client truyền `nFrameNo` là khung TUYỆT ĐỐI = hướng*số_khung_mỗi_hướng + khung (`KNpcResVN.cpp:46,67`; bản gốc `KNpcRes.cpp:271` giống hệt). Các số trong `LineK` của ini (0..52) nhỏ, nên ở hướng khác 0 chúng có thể khớp sai khung hoặc không khớp. CHƯA kiểm tra đó là chủ ý của tác giả hay lỗi.

## 2. Số liệu đã đo (nữ, thương, đứng act=38, DEFAULT)
Hướng(0..7) → bảng: xem bảng trong BUG-001. Hướng 0-3 vẽ lớp 9 (thân thương) TRƯỚC giáp; hướng 4-7 vẽ lớp 9 SAU giáp. Đối xứng gương: hướng 1↔7, 2↔6, 3↔5 mà dữ liệu không đối xứng.

## 3. Việc cần làm để hiểu hết (xếp hàng chờ)
- Lập bảng đầy đủ nữ/nam × hành động (đứng, đi bộ FreeWalk, chạy FreeRun, đánh) × 8 hướng × khung đặc biệt.
- Xác định hành động đi bộ thực tế trong client là mục nào (FreeWalk/FreeRun/RangeW…), vì thương dùng mục "RangeW*" khi đứng nhưng không có RangeWWalk.
- Kiểm tra giả thuyết khung tuyệt đối vs khung trong hướng với `LineK`.
- Nhân vật nam chỉ có DEFAULT: kiểm nam có cùng triệu chứng không.
