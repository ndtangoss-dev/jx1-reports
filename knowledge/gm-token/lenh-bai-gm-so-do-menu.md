# Lệnh bài GM: sơ đồ menu và phân loại an toàn

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Nhân vật: jxt36a | Môi trường: VM thử 36Hz (không phải Main VM)

## Cách mở
Nhận "Lệnh bài GM x 1" từ NPC Lễ Quan (npcs/le-quan.md), rồi dùng vật phẩm trong hành trang. Trạng thái: VERIFIED (p46qa-14.png nhận vật phẩm; p46qa-18.png bảng GM mở).

## Phần đầu bảng (chỉ đọc)
Bảng hiển thị dòng thông tin: số GS và số người online, ID bản đồ (53), tọa độ ô (ví dụ 203/199) và tọa độ X/Y*32. Đây là nguồn đọc tọa độ chính xác cho QA. READ_ONLY. VERIFIED (p46qa-18.png). Không ghi lại các giá trị ID tài khoản.

## Menu chính (11 nút, đã đếm trên p46qa-18.png)

Chú giải duyệt: "CẦN DUYỆT" = không thực thi nếu chưa có phê duyệt cụ thể của người dùng. "Tạm" = phân loại tạm theo nhãn, chưa xác minh.

| # | Nhãn (đúng như hiển thị) | Phân loại | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 1 | Admin Quản Lý 1 | IRREVERSIBLE_OR_RISKY (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT. Có thể là công cụ quản trị tài khoản/người chơi. Chỉ cho phép mở để kiểm kê nếu người dùng đồng ý, không bấm mục con. |
| 2 | Admin Quản Lý 2 | IRREVERSIBLE_OR_RISKY (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT, như trên. |
| 3 | ReloadScript GM | IRREVERSIBLE_OR_RISKY (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT. Nghi nạp lại script phía server, ảnh hưởng toàn server và mọi người chơi; trên VM thử có thể chấp nhận được, nhưng vẫn cần duyệt vì có thể làm lỗi script đang chạy. |
| 4 | Nhận Các Loại Điểm | GAME_STATE_CHANGE | VERIFIED (mở được menu con) | Xem gm-token/nhan-cac-loai-diem.md. |
| 5 | Goi npc test | GAME_STATE_CHANGE (tạm theo nhãn, chưa xác minh) | NOT_TESTED | Nghi gọi/tạo NPC thử. Có thể hoàn tác nếu NPC tự biến mất: UNKNOWN. |
| 6 | SetFightState | GAME_STATE_CHANGE (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT nếu rủi ro: đổi trạng thái chiến đấu của nhân vật. Liên quan lỗi đã biết "không bật được trạng thái chiến đấu khi qua cổng Ba Lăng". Nếu dùng để chẩn đoán phải ghi trạng thái trước/sau và hoàn tác được hay không. |
| 7 | Quản Lý Server | IRREVERSIBLE_OR_RISKY (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT. Nghi tác động tiến trình/cấu hình server. Cấm bấm mục con nếu chưa duyệt. |
| 8 | Đổi màu - PK - Hồ trợ GM | REVERSIBLE (tạm theo nhãn, chưa xác minh; có thể GAME_STATE_CHANGE) | NOT_TESTED | Nghi đổi màu tên/chế độ PK. Sai chính tả "Hồ trợ" là nguyên văn trên giao diện. |
| 9 | Reset số lần vượt ải | IRREVERSIBLE_OR_RISKY (tạm theo nhãn, chưa xác minh) | NOT_TESTED | CẦN DUYỆT. Reset dữ liệu tiến trình, khó hoàn tác. Không liên quan test giật/kỹ năng. |
| 10 | Open Các Tính Năng Game | GAME_STATE_CHANGE (tạm theo nhãn, chưa xác minh) | NOT_TESTED | Nghi mở/bật tính năng; có thể gồm mục hữu ích (ngựa, dịch chuyển) nhưng chưa biết: UNKNOWN. Nên mở kiểm kê menu con trước khi chọn. |
| 11 | Đóng. | READ_ONLY | DISCOVERED | Đóng bảng (chưa bấm trong mẫu ảnh đã xem). |

## Menu con đã mở: Nhận Các Loại Điểm
Xem file riêng. Tóm tắt: Nhận Cấp Độ (VERIFIED); Các Loại Điểm (xem file riêng); Nhận Kỹ Năng 15x (DISCOVERED); Trang trước; Đóng.

## Chưa làm / UNKNOWN
- Nội dung menu con của mục 1, 2, 3, 5, 6, 7, 8, 9, 10: chưa mở.
- Menu có cuộn hay nhiều trang không: chỉ nút "Trang trước" thấy ở menu con (chắc có "Trang sau" hay trang kế: UNKNOWN). Phải kiểm kê trang kế khi mở lại.
- Mục mà Phase 46 cần nhưng chưa biết nằm ở đâu: nhận ngựa, nhận tiền. Tiền/xu đã nhận được (p46qa-70.png), ngựa đã có ("Mã Bài - Ngựa 8x x 1", p46qa-85.png) nhưng nguồn nhận (GM hay Bảo Vật) chưa xác định.
- Cách hoàn tác bất kỳ thay đổi nào: chưa xác minh. Cách hoàn tác thực tế duy nhất là khôi phục snapshot/nhân vật của VM thử do Opus quản lý.

## Quy tắc thực thi
1. READ_ONLY: được thử trong VM thử.
2. REVERSIBLE/GAME_STATE_CHANGE: chỉ trên jxt36a, ghi trạng thái trước/sau (HUD, hành trang, bảng kỹ năng).
3. IRREVERSIBLE_OR_RISKY và mọi mục CẦN DUYỆT: chỉ kiểm kê giao diện, không bấm; muốn thực thi phải có duyệt riêng của người dùng cho từng mục.
4. Không nhập lệnh/giá trị không hiểu.
