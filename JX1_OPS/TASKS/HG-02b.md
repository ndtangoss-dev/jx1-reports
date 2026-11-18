---
id: HG-02b
title: (lần 2) Hiểu game: trạng thái chiến đấu và nút đánh
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/HG-02b
worktree: D:\JX-wt\HG-02b
depends_on: []
backlog_ref: "#195 hang doi viec, muc [SONNET-THÊM] hiểu game"
vung_file: [JX1_OPS/DESIGN/HIEU-TRANG-THAI-CHIEN-DAU.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "lam lai: ban dau PARTIAL do worktree thieu source"
---

## Mục tiêu và tiêu chí xong
Giải thích vì sao nút đánh ngoài trạng thái chiến đấu làm nhân vật ngồi: `mainSkillattack`, cờ 0x02, `SetFightMode`, `SetFightState`; đề xuất cách bật chiến đấu trên Test-36 để quan sát vung kiếm (chỉ đề xuất).
Đầu ra: `JX1_OPS/DESIGN/HIEU-TRANG-THAI-CHIEN-DAU.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình.

## Nguồn cần đọc
- `Folder/Client2912-.../Classes/gamecore/KNpcAI.cpp`, `KProtocolProcess.cpp`, `gameserver/Sources/Core/Src/KNpc.cpp`, `ScriptFuns.cpp` (tìm bằng tên hàm).

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).

## Nguồn bổ sung (sửa lỗi lần trước)
Nguồn thật (đọc được, đường dẫn tuyệt đối): client C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KNpcAI.cpp và C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocolProcess.cpp; server C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp và C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\ScriptFuns.cpp. Worktree của bạn KHÔNG có mã nguồn: hãy đọc trực tiếp các đường dẫn tuyệt đối này (chỉ đọc; ghi chỉ ở tệp đầu ra).

## Kết quả
- DONE: đã đối chiếu 4/4 tệp nguồn. Khi chế độ chiến đấu tắt, nhánh nút đánh ra lệnh ngồi rồi thoát; bit 0x02 đồng bộ trạng thái mà SetFightState thay đổi qua SetFightMode.
- Giữ nguyên tài liệu đầu ra đã có; chi tiết bằng chứng và bàn giao tại [báo cáo HG-02b](../REPORTS/HG-02b.md).
- Test-36 chỉ là đề xuất; chưa chạy build, game, exe, VM hoặc mạng.
- Không commit theo yêu cầu. Sandbox từ chối ghi tệp nhịp ngoài worktree.
