---
id: XD-HG16d
title: "XD HG-16d: nhanh tao ho so nhan vat phia Bishop/Goddess"
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-HG16d
worktree: D:\JX-wt\XD-HG16d
depends_on: []
backlog_ref: "XD (dong HG-16)"
vung_file: [JX1_OPS/REPORTS/XD-HG16d.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---


## Mục tiêu và tiêu chí xong
Phần còn thiếu của HG-16: nhánh TẠO hồ sơ nhân vật mới phía gateway. Đọc tĩnh C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gateway/Sources (Bishop: GameServer.cpp, SmartClient.cpp, Intercessor.cpp; Goddess: DBTable.cpp, IDBRoleServer.cpp). Trả lời: gói tạo nhân vật đi từ Bishop sang Goddess thế nào; Goddess ghi bảng nào; có kiểm tên trùng/số nhân vật tối đa/giới hạn hệ ở đâu (file:dòng); lúc nào server ép chỉ số/đồ khởi đầu. Đầu ra `JX1_OPS/REPORTS/XD-HG16d.md`: TÓM TẮT 5 DÒNG, nhãn THẤY/TÀI LIỆU/CHƯA KIỂM, >=8 dẫn file:dòng, mục "Chưa kiểm". Xem `JX1_OPS/DESIGN/HIEU-TAO-NHAN-VAT-MOI.md` để không lặp.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh, chỉ viết tệp đầu ra. Không sửa mã, không exe, VM, mạng, không đụng Main VM, không đọc khóa/dump tài khoản. Mỗi lần đọc <= 400 dòng.
- Cuối tệp task ghi "## Kết quả" 3–5 dòng.
