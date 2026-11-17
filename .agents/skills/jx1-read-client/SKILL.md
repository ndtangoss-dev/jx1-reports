---
name: jx1-read-client
description: Đọc source client JX1/Cocos theo root task để giải thích UI, render hoặc gamecore; không tự build APK hay chạy client.
---
# Đọc client JX1
- Ghi root/version task cho phép. Folder/Client2912... và D:\Android\b\Client là hai
  nguồn khác nhau, không thay thế lẫn nhau. Root thiếu thì tra task/nguồn được dẫn;
  vẫn không rõ thì hỏi, không quét ổ đĩa.
- Tìm đúng symbol trong Classes/gameui, gamescene, gamecore hoặc engine; chỉ sang Cocos
  khi cần chứng minh API/framework.
- Có Graphify đúng root (kiểm graphify-out/.graphify_root khớp root đang đọc) thì tra phần liên quan graphify-out/GRAPH_REPORT.md hoặc graph.json;
  dòng Graphify ở JX1_OPS/TOOLS/CONG-CU.md là gợi ý lịch sử. Không tự update/cài hook.
- Dùng rg -n giới hạn thư mục; thiếu báo một lần, dùng Select-String, không cài.
  Mở file thật tóm tắt/graph trỏ tới, kiểm symbol, caller và dòng hiện tại.
- Tách active code/comment, mặc định/source và giá trị lưu/runtime, source trên đĩa/APK cài.
  FPS/RAM, ACK, chất lượng ảnh chưa đo phải ghi CHUA XAC MINH.
- Trả root + file:dòng + symbol; build/APK/LDPlayer/VM/exe/sửa mã cần quyền cụ thể từ task.
