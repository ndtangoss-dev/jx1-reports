# PP-03 Kiểm kê menu/hook thử cần gỡ trước server thật (đọc tĩnh, 22/11)

Nguồn: A đọc 4 file Lua trong docs-analysis/out; phần C++ lấy từ B-112 (02:40). Chưa sửa gì.

## Phía Lua (script nạp nóng, Test-36)
| Tệp | Tag | Việc | Gỡ thế nào |
|---|---|---|---|
| atest_hook.lua | Q-97 | hook thử tài khoản atest* | xóa tệp + dòng include |
| baowubox.lua | Q-101 | hộp bảo vật thử | xóa tệp + mục menu |
| qh_bothu.lua, qh_vm_now.lua | Q-101/#303/#306, SC-006 | menu thử cường hóa: nạp thủy tinh, "Mỗi món túi +6", chỉnh cấp | xóa tệp; bỏ mục khỏi menu sách |
| lenhbaitanthu.lua | — | mục "[TEST-36] Hỗ trợ Cường hóa (atest)" | xóa mục menu |
| hotrotanthu | — | menu hỗ trợ tân thủ thử | rà lại khi gỡ (chưa đọc nội dung) |

## Phía C++ (B-112, 15 điểm ghi qh_dump.log, I/O đồng bộ)
KItem.cpp:3827-3830 [QH-TEST SC-006]; KItemList.cpp 1170,1176,1183,1235,1254,1894,2228,3206,3213 [pifeng-*]; KProtocolProcess.cpp 8371,8487,8513,8577. Đề xuất B: gom macro QH_DUMP bật bằng #ifdef (chờ Chat duyệt).

## Phía client
vc38 giữ cửa sổ Cường hóa mở (m_qhKeepOpen) là tính năng thật, không gỡ. Dòng "[QH]|E|" là giao thức thật.

Chưa kiểm: nội dung hotrotanthu; menu GM phía Lua trên VM.
