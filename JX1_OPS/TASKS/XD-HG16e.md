---
id: XD-HG16e
title: "XD HG-16e: nhanh tao ho so nhan vat Bishop/Goddess (duong dan dung)"
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-HG16e
worktree: D:\JX-wt\XD-HG16e
depends_on: []
backlog_ref: "XD (dong HG-16)"
vung_file: [JX1_OPS/REPORTS/XD-HG16e.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---


## Mục tiêu và tiêu chí xong
Phần còn thiếu của HG-16: nhánh TẠO hồ sơ nhân vật mới phía gateway. Đọc tĩnh (đường dẫn ĐÚNG, chỉ đọc) C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gateway/Sources/MultiServer/Bishop/{GameServer.cpp,Intercessor.cpp,SmartClient.cpp} và C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gateway/Sources/MultiServer/Goddess/{DBTable.cpp,IDBRoleServer.cpp} (lần trước đường dẫn sai nên không mở được). Trả lời: gói tạo nhân vật đi từ Bishop sang Goddess thế nào; Goddess ghi bảng nào; có kiểm tên trùng/số nhân vật tối đa/giới hạn hệ ở đâu (file:dòng); lúc nào server ép chỉ số/đồ khởi đầu. Đầu ra `JX1_OPS/REPORTS/XD-HG16e.md`: TÓM TẮT 5 DÒNG, nhãn THẤY/TÀI LIỆU/CHƯA KIỂM, >=8 dẫn file:dòng, mục "Chưa kiểm". Xem `JX1_OPS/DESIGN/HIEU-TAO-NHAN-VAT-MOI.md` để không lặp.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh, chỉ viết tệp đầu ra. Không sửa mã, không exe, VM, mạng, không đụng Main VM, không đọc khóa/dump tài khoản. Mỗi lần đọc <= 400 dòng.
- Cuối tệp task ghi "## Kết quả" 3–5 dòng.

