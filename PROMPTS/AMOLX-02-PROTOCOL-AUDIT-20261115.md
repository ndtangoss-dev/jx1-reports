---
task_id: AMOLX-02-PROTOCOL-AUDIT-20261115
status: READY_FOR_DIRECT_CLI
scope: Read-only protocol compatibility audit for AMOLX against JX1 canonical client and server source. No code changes, no build, no network connections.
allowed_paths:
  - TEST_RESULTS/AMOLX-02-PROTOCOL-AUDIT-20261115.md
---

# AMOLX-02 — Protocol Compatibility Audit

## Mục tiêu

Xác định bằng chứng tĩnh, có thể truy vết, về mức độ tương thích protocol giữa AMOLX, client Cocos canonical và source server JX1 hiện có. Tập trung vào enum command ID, packet layout, login/Bishop handoff và các handler gameplay thiết yếu.

Báo cáo bàn giao trước:
`TEST_RESULTS/AMOLX-SESSION-HANDOVER-20261115.md`

Source AMOLX đã xác minh:
`C:\JX1\jx1client-axmol-main\jx1client-axmol-main`

Workspace:
`C:\Jx1CocoV3`

## Nguyên tắc bắt buộc

- Chỉ đọc source trong nhiệm vụ này. Không sửa, format, generate hoặc ghi vào bất kỳ source file nào.
- Không build, không chạy Gradle, không cài APK, không kết nối socket/server, không packet capture.
- Không truy cập Main VM hoặc thay đổi server.
- Không sửa client Cocos canonical.
- Không thay đổi Dispatcher, Task Scheduler, Codex config, sandbox, ACL hoặc credential.
- Không suy đoán source server hiện có khớp executable server đang chạy. Phân biệt rõ source-level evidence và runtime evidence.
- Không dùng tài khoản thật; không đưa mật khẩu, token, IP nhạy cảm hoặc secret vào báo cáo.
- Không đọc lại toàn bộ báo cáo lịch sử. Chỉ mở báo cáo protocol/client/server có liên quan trực tiếp và ghi rõ nguồn.
- Nếu không tìm thấy file hoặc không đủ bằng chứng, ghi CHƯA XÁC MINH, không tự điền.

## Nguồn cần kiểm tra

1. AMOLX:
   - `Source/gamecore/KProtocolDef.h`
   - `Source/gamecore/KProtocol.h`
   - `Source/gamecore/KProtocolProcess.cpp`
   - `Source/network/ClientStage.cpp`
   - `Source/network/SocketClient.cpp`
   - `Source/network/Cipher.h`
   - `Source/network/KSG_EncodeDecode.cpp/.h`
   - Các packet struct/header được include bởi các file trên.
2. Cocos canonical:
   - Header protocol và packet struct tương ứng trong cây Client2912 đã được chỉ ra trong báo cáo bàn giao.
3. JX1 server source:
   - Các enum/command definition, packet struct và dispatch/handler tương ứng trong cây SwordOnline đã được chỉ ra trong báo cáo bàn giao.
4. Báo cáo hiện có:
   - `00_LATEST_STATUS.md`
   - `TEST_RESULTS/AMOLX-SESSION-HANDOVER-20261115.md`
   - Chỉ các báo cáo protocol/server/client liên quan trực tiếp.

## Công việc

### A. Kiểm kê enum và ID

- Trích xuất toàn bộ enum command liên quan C2S và S2C từ cả ba phía: AMOLX, Cocos canonical, server source.
- Ghi giá trị số thực tế của từng enum, không chỉ so sánh tên hoặc thứ tự văn bản.
- Xác định enum có implicit auto-increment, explicit assignment, conditional compile hoặc alias.
- Tạo bảng cho từng command: direction, numeric ID, symbolic name, AMOLX value, Cocos value, server value, tình trạng, file:line.
- Tập trung xác minh 9 mục được báo cáo thiếu:
  `s2c_npcsettmpcamp`, `s2c_npcstand`, `s2c_gm_synroleaction`, `s2c_queryiteminfo`, `s2c_returnitemlock`, `s2c_findpath_state`, `s2c_refitemsync`, `s2c_chestpwsync`, `s2c_extendchat_new`.
- Xác định chính xác vị trí đầu tiên mà giá trị numeric ID lệch, bao nhiêu mục phía sau bị dịch chuyển, và liệu có ngoại lệ/explicit ID làm thay đổi kết quả.
- Không kết luận chỉ từ việc thiếu tên enum: kiểm tra cách server/client dispatch theo ID.

### B. Packet layout và serialization

Với các packet cốt lõi, so sánh:
- struct/field order, field width, signedness, packing/alignment.
- fixed-size vs variable-size, length prefix, header/framing.
- byte order, checksum/compression/encryption nếu source thể hiện.
- serialization/deserialization và giới hạn buffer.
- version/protocol negotiation.

Ưu tiên:
- login request/response.
- server selection và Bishop handoff.
- `tagLogicLogin`.
- chọn nhân vật / danh sách nhân vật.
- enter world/map.
- movement, NPC/monster sync, chat và combat/skill packet.

Mỗi kết luận phải có đường dẫn file, symbol/hàm và số dòng hoặc vùng mã đủ để Codex khác kiểm tra lại.

### C. Login và chuyển server

Lần theo chuỗi:
- login packet được tạo ở đâu;
- command ID và cấu trúc packet;
- xác thực/response parse;
- địa chỉ/cổng/GUID nhận từ Bishop;
- socket chuyển sang game server;
- `tagLogicLogin` và phản hồi;
- packet đầu tiên sau khi vào world.

Chỉ phân tích code tĩnh. Không gửi request hoặc kết nối endpoint.

### D. Phân biệt nguồn chuẩn

Lập bảng nguồn và độ tin cậy:
- AMOLX source.
- Cocos canonical source.
- JX1 server source.
- Báo cáo/log cũ có bằng chứng executable thực tế.

Nếu các nguồn mâu thuẫn, ghi rõ mâu thuẫn. Không tự chọn một nguồn làm chuẩn cho executable production khi chưa có bằng chứng. Đề xuất cách xác minh an toàn sau này, không thực hiện trong task này.

## Đầu ra

Tạo duy nhất báo cáo:
`TEST_RESULTS/AMOLX-02-PROTOCOL-AUDIT-20261115.md`

Báo cáo tiếng Việt, gồm:
1. Executive summary và kết luận có mức tin cậy.
2. Bảng nguồn và giới hạn bằng chứng.
3. Bảng enum/ID C2S, S2C và phân tích điểm lệch.
4. Bảng packet layout/serialization cho packet cốt lõi.
5. Sơ đồ/diễn giải login → Bishop → game server → world.
6. Danh sách handler/packet gameplay có nguy cơ lỗi.
7. Các mâu thuẫn và câu hỏi chưa xác minh.
8. Đề xuất patch tối thiểu theo thứ tự, nhưng KHÔNG thực hiện patch.
9. Lệnh kiểm tra đã chạy và file đã đọc.
10. Kết luận phân loại: TƯƠNG THÍCH / CẦN ĐIỀU CHỈNH / KHÔNG TƯƠNG THÍCH / CHƯA ĐỦ BẰNG CHỨNG cho từng hạng mục.

## Nghiệm thu

- Mọi ID so sánh phải là giá trị số đã tính/đọc được.
- Mọi kết luận quan trọng có file/symbol/line evidence.
- Không gọi source server là production truth nếu chưa đối chiếu executable.
- Không có source file nào bị thay đổi.
- Không build, không network, không server operation.
- Báo cáo được commit và push lên `ndtangoss-dev/jx1-reports` nhánh `main`.
- Chỉ commit báo cáo mới và file cần thiết trực tiếp cho báo cáo; không gom các thay đổi cục bộ khác.
- Nếu không push được, giữ báo cáo local và báo chính xác lỗi; không thay đổi credential để vượt lỗi.

Khi xong, thông báo commit SHA, link báo cáo, các phát hiện quan trọng, phần chưa xác minh và trạng thái git.
