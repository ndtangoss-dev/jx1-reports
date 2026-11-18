---
id: HG-03c
title: Hiểu game: cường hóa Lua → client, phần còn thiếu (SynPlayerItem và tooltip +N)
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-03c
worktree: D:\JX-wt\HG-03c
depends_on: []
backlog_ref: "#202 duong 70%: nhom Hieu game (BACKLOG, HG-03c)"
vung_file: [JX1_OPS/DESIGN/HIEU-CAP-CUONG-HOA-LUA-2.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K3"
---

## Mục tiêu và tiêu chí xong
Tiếp HG-03b (xem `JX1_OPS/REPORTS/HG-03b.md`): (1) đọc định nghĩa `SynPlayerItem` ở server và dữ liệu gói gửi đi (nEnChance có nằm trong gói không?); (2) tìm hàm client dựng tooltip và chỗ hiện "+N" / glow đọc cấp (nEnChance/m_EnChance); (3) kết luận: cấp từ Lua có tới được chỗ vẽ không, hay bị mất ở bước nào; ghi file:dòng cho từng bước.
Đầu ra: `JX1_OPS/DESIGN/HIEU-CAP-CUONG-HOA-LUA-2.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình, có ít nhất 1 sơ đồ mermaid. Xong khi: tệp tồn tại, trả lời đủ các câu hỏi ở trên (mỗi câu có nhãn), điều chưa biết ghi CHƯA KIỂM, không bịa.

## Nguồn cần đọc
- Báo cáo: `HG-03b.md`, `H-03-cuong-hoa.md`, `H-04-hieu-ung-vu-khi.md`
- Worktree của bạn KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`. Có thể tra nhanh bằng `D:/JX-tools/graphify-venv/Scripts/graphify.exe query "<câu hỏi>"` chạy trong `D:/JX-build/src18/jxOnline` (đồ thị server 51.690 nút).

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).

## Kết quả

- DONE phần khảo sát tĩnh. Đã nộp [tài liệu kết quả](../DESIGN/HIEU-CAP-CUONG-HOA-LUA-2.md) và [báo cáo HG-03c](../REPORTS/HG-03c.md).
- [THẤY] Gói `s2c_syncequipitem` mang cấp cường hóa. Client cập nhật theo ID và loại đồ trước khi tooltip đọc cấp và dựng `+N`.
- [CHƯA KIỂM] Điểm glow đọc cấp trong Client2912, bố cục gói của binary và hành vi thực tế trong game.
- Phạm vi chỉ đọc tĩnh. Tổng quan phụ trách commit. Tệp nhịp nằm ngoài vùng sandbox cho phép ghi.
