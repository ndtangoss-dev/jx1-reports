---
id: XD-W02c
title: Tra nguyên nhân SetItemEnChance không tới client
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-W02c
worktree: D:\JX-wt\XD-W02c
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-W02c.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao"
---

## Mục tiêu và tiêu chí xong
Việc phụ cho **W-02**/HG-03b: đọc `ScriptFuns.cpp` quanh dòng ~10912 (SetItemEnChance), đường `s2c_syncequipitem`/ITEM_SYNC.m_EnChance ở server và `KProtocolProcess.cpp` ở client; xác định bước nào chặn hoặc có thể chặn "+N" và glow; mỗi nhận định ghi THẤY/CHƯA KIỂM kèm file:dòng; đề xuất 1 phép thử Test-36 nhỏ nhất.
Đầu ra: `JX1_OPS/REPORTS/XD-W02c.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế có bằng chứng hoặc ghi rõ thiếu gì.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- DONE khảo sát: đã viết `JX1_OPS/REPORTS/XD-W02c.md`, truy vết setter → dựng/gửi `s2c_syncequipitem` → bộ nhận → tooltip.
- [THẤY] Server có gán `m_EnChance`; client có thể bỏ gán cấp khi không tìm ID hoặc vật phẩm không xanh/tím/vàng. Nguyên nhân runtime W-02 vẫn [CHƯA KIỂM].
- Đề xuất đúng một phép thử Test-36: đồng bộ lại một vật phẩm sẵn có bằng delta=0, đối chiếu ID/cấp và nhánh client; chưa chạy thử, build, exe, VM hoặc mạng.
- Không commit/push; Tổng quan commit hộ. Tệp nhịp `D:\JX-wt\XD-W02c.nhip` ngoài writable root nên chưa ghi; không vượt sandbox.
