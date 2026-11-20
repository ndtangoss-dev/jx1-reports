# ĐANG LÀM (mỗi bên tự ghi 5–10 dòng; ghi TRƯỚC khi nén và SAU mỗi bước — Q-99)

## Sonnet A
- 20/11 12:22 [A] gs001 đã nạp B-044: Giao hiện lời nhắc của B, +1 đồ vàng thành công (ảnh q97b-*). Chat yêu cầu nghiệm thu: nút cần chữ "Cường hóa" + to hơn (đang dựng vc27 lần 2, ảnh cuonghoa.png tự vẽ cùng kiểu Auto); sửa lời nhắc Giao (3 loại thủy tinh); ĐÃ ĐỌC KIẾN THỨC (DO-HIEU-QUA-QUY-TRINH) / ĐÃ TRA ĐỒ THỊ client+server. Việc kế: TC2 dòng ×1.05 sai (báo B), TC3-8.
- Tính năng: CUONG-HOA (DESIGN/TINH-NANG/CUONG-HOA.md) — bước 1,3 xong (ĐÃ KIỂM trong game 20/11 11:55); đang 2/4: tiêu chí 2.
- NGUYÊN NHÂN sysError (tìm 20/11 12:10): UI Giao gửi đúng (kind 3), nhưng gs001 Test-36 vẫn chạy qianghua.lua GỐC đã nạp trong bộ nhớ lúc 10:54 (trước khi chép B-044 lúc 11:05); Lua chỉ nạp lại khi gs001 khởi động lại. Đã khởi động lại gs001 (task JX-gs001) 12:1x; file qianghua.lua = B-044 (SHA b03981...cdd5).
- Lệnh chạy tiếp: chờ gs001 nạp xong (~7 phút), vào LD atestvaihero, nút mới -> đặt đồ trong túi -> Xác nhận; đo tiêu chí 2-8. Bộ thử: VM gs\script\system\qh_bothu.lua (nguồn docs-analysis/out/qh_bothu.lua; Include cuối opensysui.lua, gốc B ở .bak-q97): Thiếu Lâm + ResetBaseAttrib sức mạnh 300. Chưa kiểm hiệu lực.
- 20/11 12:55 [A] TC3 đang dở: ĐÃ KIỂM boots Né tránh 55→62 (1 chỉ số). Đồ vàng hook cũ không mặc được (nghi nCanUse=0) -> hook mới gọi SetAndSycItem canuse=1; túi LD đã ném 3 món rác để có chỗ; đã khởi động lại gs001 (nạp ~10 phút) để cờ QH_GIVEN2 reset. Việc kế: LD vào lại, bấm nút Cường hóa kích hook, mặc 3 đồ vàng, chụp bảng nhân vật trước/sau (TC3), TC4–8. CHƯA KIỂM: TC3 đủ, TC4–TC8.
- Đang chờ: không (tự làm).
- Thư đã đọc đến: #297

## Sonnet B
- Tính năng: CUONG-HOA (hồ sơ DESIGN/TINH-NANG/CUONG-HOA.md), kế tiếp TAI-PHU-PHI-PHONG (hồ sơ đã dựng) — bước: (b) đã điền; Lua B-044 giao chờ A nạp (CHƯA CHẠY).
- Lệnh chạy tiếp: chờ A báo tiêu chí 5/7; nếu hỏng → sửa Lua/C++ nhỏ (nghi: baseline m_TempMagicAttrib sau nạp DB KItem.cpp:661; vàng dùng EnChanceRong KItem.cpp:3880); rồi làm mới đồ thị (cd D:\JX-wt\QH-B035\server\jxOnline\gameserver\Sources\Core\Src; graphify update .).
- Đang chờ: A (nạp QH-B044-deploy, đo tiêu chí 1–8).
- Hook B (D:\JX-wt\SONNET-B\.claude\settings.json): SessionStart (hook_luat.py start/postcompact, KIỂM chạy tay: ra LUAT-COT-LOI) và Graphify hook-guard (SessionStart compact, PreToolUse Bash|Grep|Read|Glob, KIỂM chạy tay exit 0) ĐỀU CÓ. Lưu ý: thư mục B chưa có graphify-out nên hook-guard không dẫn tới đồ thị; đồ thị server nằm ở QH-B035\...\Core\Src\graphify-out.
- Thư đã đọc đến: #B-047
