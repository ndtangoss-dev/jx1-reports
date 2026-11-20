# ĐANG LÀM (mỗi bên tự ghi 5–10 dòng; ghi TRƯỚC khi nén và SAU mỗi bước — Q-99)

## Sonnet A
- Tính năng: CUONG-HOA (DESIGN/TINH-NANG/CUONG-HOA.md) — bước: 1,3 xong (ĐÃ KIỂM trong game 20/11 11:55); đang ở 2/4: bộ thử qh_bothu.lua + tiêu chí 2
- Lệnh chạy tiếp: LD emulator-5556 đang đăng nhập atestvaihero, vc27 đã cài. Hook tạm: VM gs\script\systemtest_hook.lua (+1 dòng Include cuối opensysui.lua, gốc B ở .bak-q97) -> đổi thành qh_bothu.lua; ảnh q97-*.png ở docs-analysis/out/ld. Vấn đề: bấm Xác nhận Give (chỉ côn / côn+đá) đều ra sysError (không tới Lua B) -> tra Give(...,1,1,...) trong ScriptFuns/KuiGive_New
- Đang chờ: không (tự làm). Hook chưa áp môn phái/sức mạnh (tooltip côn vẫn đỏ).
- Thư đã đọc đến: #297

## Sonnet B
- Tính năng: CUONG-HOA (hồ sơ DESIGN/TINH-NANG/CUONG-HOA.md), kế tiếp TAI-PHU-PHI-PHONG (hồ sơ đã dựng) — bước: (b) đã điền; Lua B-044 giao chờ A nạp (CHƯA CHẠY).
- Lệnh chạy tiếp: chờ A báo tiêu chí 5/7; nếu hỏng → sửa Lua/C++ nhỏ (nghi: baseline m_TempMagicAttrib sau nạp DB KItem.cpp:661; vàng dùng EnChanceRong KItem.cpp:3880); rồi làm mới đồ thị (cd D:\JX-wt\QH-B035\server\jxOnline\gameserver\Sources\Core\Src; graphify update .).
- Đang chờ: A (nạp QH-B044-deploy, đo tiêu chí 1–8).
- Hook B (D:\JX-wt\SONNET-B\.claude\settings.json): SessionStart (hook_luat.py start/postcompact, KIỂM chạy tay: ra LUAT-COT-LOI) và Graphify hook-guard (SessionStart compact, PreToolUse Bash|Grep|Read|Glob, KIỂM chạy tay exit 0) ĐỀU CÓ. Lưu ý: thư mục B chưa có graphify-out nên hook-guard không dẫn tới đồ thị; đồ thị server nằm ở QH-B035\...\Core\Src\graphify-out.
- Thư đã đọc đến: #B-047
