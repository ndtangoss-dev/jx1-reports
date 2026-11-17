# HƯỚNG DẪN TRA CỨU (1–2 trang)

Mục tiêu: trả lời "cái này ở đâu, ai gọi ai, đã có báo cáo chưa" mà không đọc lại cả mã. Thứ tự: **MỤC LỤC → Graphify → báo cáo → file thật**.

## A. Tra đồ thị Graphify
Công cụ: `D:\JX-tools\graphify-venv\Scripts\graphify.exe`. Chạy tại thư mục có `graphify-out/` (hoặc thêm `--graph <đường dẫn>\graph.json`).
- Client bản A: `D:\JX-build\qh9A\Classes\graphify-out\`. Server: `D:\JX-build\src18\graphify-out\` và `...\src18\jxOnline\graphify-out\`.
- `graphify query "<câu hỏi>"` – hỏi tự nhiên, trả về cụm nút liên quan. `graphify path "A" "B"` – đường nối hai hàm/lớp. `graphify explain "X"` – nút X và hàng xóm (caller/callee). `graphify section "<tiêu đề>"` – in một mục Markdown.
- `GRAPH_REPORT.md` chỉ đọc khi cần nhìn toàn cảnh (nút trung tâm, cộng đồng); `graph.html` để xem trực quan.
- Năm ví dụ thật:
  1. "Ai quyết định thứ tự vẽ vũ khí?" → `graphify explain "GetSort"` rồi `path "KNpcResVN::Draw" "GetSort"`; mở `KNpcResNode.cpp` quanh `:1390`.
  2. "Client nhận cờ chiến đấu ở đâu?" → `graphify query "fight mode flag 0x02 KProtocolProcess"`.
  3. "Nhân vật ngồi khi bấm phím chính?" → `graphify explain "mainSkillattack"`.
  4. "Server gửi địa chỉ gs cho client ở đâu?" → `graphify query "GameServer Ip localIp KSOServer"` (đồ thị server).
  5. "Trap cổng làng chạy thế nào?" → `graphify explain "CheckTrap"`.
- Đồ thị là bản định vị, số dòng có thể lệch: luôn mở file thật tại dòng chỉ tới trước khi kết luận.

## B. Tra tài liệu
1. Mở `DESIGN/MUC-LUC-TRI-THUC.md`, tìm chủ đề, xem cột Độ chắc.
2. Mở báo cáo ghi trong cột; đọc TÓM TẮT 5 DÒNG và dòng "liên quan: ...", đi tiếp theo liên kết.
3. `BUGS/` và `STATE/BAI_HOC`: lỗi giống thế đã gặp chưa.

## C. Khi nào tin đồ thị, khi nào mở file thật
- Tin để **chọn chỗ nhìn** (hàm nào, file nào, ai gọi). Mở file thật để **kết luận** (giá trị, điều kiện, dòng).
- Kiểm gốc đồ thị: `type graphify-out\.graphify_root` phải đúng bản đang sửa (bài học L-01: từng đọc nhầm bản). Xem ngày/commit ở `STATE/DO-THI.md`; đồ thị cũ hơn mã thì chạy `graphify update .` trước khi tra.
- Đồ thị không có dữ liệu `.ini`, `.lua` kèm dữ liệu, PAK: tra các thứ đó bằng báo cáo I-xx/A-xx và `grep`.
