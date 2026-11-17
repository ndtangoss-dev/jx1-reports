---
name: jx1-read-server
description: Định vị và đọc source server JX1 cho câu hỏi tĩnh qua GS001 và Graphify có sẵn; không tự build hay chạy server.
---
# Đọc server JX1
- Lấy root/version từ task; không mặc định bản đồ là bản đang chạy.
- Đọc mục liên quan trong JX1_OPS/CONTEXT-PACK/GS001-MAP.md; dòng chỉ là gợi ý.
- Cần caller/callee: tra phần liên quan trong <root>/graphify-out/GRAPH_REPORT.md hoặc
  graph.json đúng root. Xem dòng Graphify tại JX1_OPS/TOOLS/CONG-CU.md nếu cần vị trí/hạn chế.
  Không tự update graph, cài hook, sửa CLAUDE.md hoặc tạo lại graph trong task chỉ đọc.
- Graph có thể cũ/trích thiếu do encoding/cú pháp. Thiếu thì dùng rg -n giới hạn thư mục;
  thiếu rg báo một lần, dùng Select-String, không cài. Không đọc toàn graph/source.
- Mở file thật ở root được giao, kiểm symbol và dòng hiện tại, lần caller/callee cần thiết.
  Tóm tắt/cạnh graph không thay bằng chứng source.
- Trả root/version + file:dòng + symbol + giới hạn. Không suy runtime từ source;
  build/exe/VM/sửa mã cần quyền task, skill không cấp quyền.
