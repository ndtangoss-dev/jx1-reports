# Quy luật vẽ bộ phận nhân vật

**Trạng thái: PARTIAL.** Bản worktree này không có `人物类型.txt` hoặc `KNpcResNode.cpp`; vì vậy các kết quả về bảng sort dưới đây được dẫn lại từ báo cáo đã có, chưa đối chiếu độc lập với tệp ini/source mà task chỉ định. Không suy ra runtime từ các số liệu tĩnh.

## Cách hiểu kết quả hiện có

Theo khảo sát tĩnh J-04, cấu trúc legacy có sức chứa 6 nhóm, mỗi nhóm 4 phần, tổng 24 section; các khoảng section được ghi nhận như sau. Đây là sức chứa, không khẳng định mọi nhóm đang xuất hiện trong gameplay hiện tại.

| Section | Bộ phận được gắn trong báo cáo J-04 |
|---|---|
| 0–3 | Mũ/đầu |
| 4–7 | Áo/thân |
| 8–11 | Vũ khí |
| 12–15 | Ngựa |
| 16–19 | Phi phong |
| 20–23 | Cánh |

Thứ tự vẽ được chọn theo hành động, hướng và khung; không có một thứ tự che cố định cho mọi tư thế. Bảng sort thực tế mới quyết định bộ phận nào ở trước hoặc sau trong từng trường hợp. Báo cáo J-04 cũng lưu ý action phụ thuộc trạng thái, vũ khí và cưỡi ngựa. `walk=12` trong J-01 là số bước logic khởi tạo, không phải tên mục action trong ini hay số khung ảnh.

## Ma trận nam/nữ × hành động × 8 hướng

Mỗi ô là chuỗi section theo thứ tự được vẽ. Dấu `—` nghĩa là chưa có bảng đo cho hướng đó. Dòng nữ/đứng là số liệu được ghi trong BUG-001; các dòng khác chưa được đo. Đây chưa phải ma trận đầy đủ để kết luận hành vi cho mọi giới và hành động.

| Giới | Hành động | Hướng 0 | Hướng 1 | Hướng 2 | Hướng 3 | Hướng 4 | Hướng 5 | Hướng 6 | Hướng 7 | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| Nữ | Đứng, act=38, DEFAULT | 14,16,13,1,4,9,7,5,6,12,8,0 | 14,16,13,9,7,4,1,5,12,6,8,0 | 9,7,12,13,14,5,16,4,1,0,6,8 | 9,7,12,13,5,14,16,4,1,0,8,6 | 12,13,8,6,5,14,16,4,1,0,7,9 | 8,6,12,13,5,14,16,4,1,0,9,7 | 8,6,12,13,14,5,16,4,1,0,9,7 | 14,16,13,4,1,8,6,5,12,0,9,7 | Đã ghi trong BUG-001; chưa đọc lại ini |
| Nữ | Đi bộ | — | — | — | — | — | — | — | — | Chưa đo; chưa rõ action thực tế |
| Nữ | Chạy | — | — | — | — | — | — | — | — | Chưa đo; chưa rõ action thực tế |
| Nữ | Đánh | — | — | — | — | — | — | — | — | Chưa đo |
| Nam | Đứng | — | — | — | — | — | — | — | — | Chưa đo |
| Nam | Đi bộ | — | — | — | — | — | — | — | — | Chưa đo; chưa rõ action thực tế |
| Nam | Chạy | — | — | — | — | — | — | — | — | Chưa đo; chưa rõ action thực tế |
| Nam | Đánh | — | — | — | — | — | — | — | — | Chưa đo |

Nguồn bảng nữ/đứng: `JX1_OPS/BUGS/BUG-001.md:6–8`. Giới hạn về thứ tự động theo action/hướng/khung và thiếu bảng sort thực tế: `JX1_OPS/REPORTS/J-04-lop-chong-nhan-vat.md:60–73`.

## Hành động đi bộ

**CHƯA XÁC MINH:** chưa thể trả lời nhân vật đi bộ dùng mục `FreeWalk`, `FreeRun`, `RangeW` hay mục nào khác trong bảng ini. Bản ghi cũ nêu các tên này như ứng viên, nhưng không có `人物类型.txt` để tra tên file và không có `KNpcResNode.cpp` để xác nhận cách nạp/chọn action tại các dòng `365–370` và `1219–1446`. `walk=12` là thời lượng logic khởi tạo theo J-01, không giải quyết được tên mục sort.

## Các điểm còn cần dữ liệu

- Đo bảng sort cho nam và nữ ở đứng, đi bộ, chạy và đánh, đủ tám hướng; xác định đúng action runtime trước khi điền ma trận.
- Đọc riêng bảng nam và nữ từ đúng `人物类型.txt` và các ini mà cột `人物贴图顺序表` chỉ tới.
- Đối chiếu cách chọn `DirN`/`LineK` với `KNpcResNode.cpp`; kiểm tra giả thuyết số khung tuyệt đối và khung trong từng hướng.
- Xác định bảng sort cụ thể đang được nạp trước khi kết luận vũ khí bị che ở một hướng hay hành động.

**Nguồn đọc được:** `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md` (bản trước), `JX1_OPS/BUGS/BUG-001.md`, `JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md`, `JX1_OPS/REPORTS/J-04-lop-chong-nhan-vat.md`. Các nhận định source/ini trong báo cáo trước chưa được xác minh lại trong worktree này.
