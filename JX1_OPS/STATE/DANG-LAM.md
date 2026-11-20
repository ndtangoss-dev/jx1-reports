# ĐANG LÀM (mỗi bên tự ghi 5–10 dòng; ghi TRƯỚC khi nén và SAU mỗi bước — Q-99)

## Sonnet A
- 20/11 12:22 [A] gs001 đã nạp B-044: Giao hiện lời nhắc của B, +1 đồ vàng thành công (ảnh q97b-*). Chat yêu cầu nghiệm thu: nút cần chữ "Cường hóa" + to hơn (đang dựng vc27 lần 2, ảnh cuonghoa.png tự vẽ cùng kiểu Auto); sửa lời nhắc Giao (3 loại thủy tinh); ĐÃ ĐỌC KIẾN THỨC (DO-HIEU-QUA-QUY-TRINH) / ĐÃ TRA ĐỒ THỊ client+server. Việc kế: TC2 dòng ×1.05 sai (báo B), TC3-8.
- Tính năng: CUONG-HOA (DESIGN/TINH-NANG/CUONG-HOA.md) — bước 1,3 xong (ĐÃ KIỂM trong game 20/11 11:55); đang 2/4: tiêu chí 2.
- NGUYÊN NHÂN sysError (tìm 20/11 12:10): UI Giao gửi đúng (kind 3), nhưng gs001 Test-36 vẫn chạy qianghua.lua GỐC đã nạp trong bộ nhớ lúc 10:54 (trước khi chép B-044 lúc 11:05); Lua chỉ nạp lại khi gs001 khởi động lại. Đã khởi động lại gs001 (task JX-gs001) 12:1x; file qianghua.lua = B-044 (SHA b03981...cdd5).
- Lệnh chạy tiếp: chờ gs001 nạp xong (~7 phút), vào LD atestvaihero, nút mới -> đặt đồ trong túi -> Xác nhận; đo tiêu chí 2-8. Bộ thử: VM gs\script\system\qh_bothu.lua (nguồn docs-analysis/out/qh_bothu.lua; Include cuối opensysui.lua, gốc B ở .bak-q97): Thiếu Lâm + ResetBaseAttrib sức mạnh 300. Chưa kiểm hiệu lực.
- 20/11 12:55 [A] TC3 đang dở: ĐÃ KIỂM boots Né tránh 55→62 (1 chỉ số). Đồ vàng hook cũ không mặc được (nghi nCanUse=0) -> hook mới gọi SetAndSycItem canuse=1; túi LD đã ném 3 món rác để có chỗ; đã khởi động lại gs001 (nạp ~10 phút) để cờ QH_GIVEN2 reset. Việc kế: LD vào lại, bấm nút Cường hóa kích hook, mặc 3 đồ vàng, chụp bảng nhân vật trước/sau (TC3), TC4–8. CHƯA KIỂM: TC3 đủ, TC4–TC8.
- 20/11 13:10 [A] ĐÃ KIỂM TC3 (áo vàng +1 mặc: Sinh lực 910->1083, Nội lực 100->300, Né tránh 5->725, 3 chỉ số, ảnh q97c-tc3-*) và TC4 (tháo: về 910/910, 100/100, Né 5, ảnh q97c-tc4-sau). LỆCH cần báo B: (1) dòng tooltip 'Phòng thủ vật lý +36%' không làm bảng Phòng thủ nhích (0%); (2) 'Điểm tài phú' bảng luôn 0 dù mặc Sa Di +7 và áo vàng (TC8). CHƯA KIỂM: TC2 (x1.05 từng dòng), TC5 (đăng nhập lại +1 lần 2), TC6, TC7, TC8.
- 20/11 13:30 [A] TC5 xong, KHÔNG ĐẠT: +1->+2 sau đăng nhập chỉ Sinh lực/Phòng thủ tăng (không phải mọi dòng, không x1.05); mặc +2 bảng lệch tooltip (Sinh +153 vs 216); tài phú/phòng thủ bảng vẫn 0. Đã báo B trong A-B.md và TU-SONNET 13:25. CHƯA KIỂM: TC6, TC7, TC8. Việc kế: chờ B sửa, rồi đo lại; trong lúc chờ làm HANG-DOI-VIEC.
- 20/11 14:07 [A] #299: đã nạp B-049 (SHA 790b5a2d…6c9 đã kiểm trên VM; bản cũ lưu gs001.exe.bak-b049pre = DE3D6F0C…, tức mức B-040/041, không phải B-039), khởi động lại gs001 MỘT lần lúc 14:07, chờ nạp ~10 phút (chưa kiểm 0xC0000005). Việc kế: đo lại TC2–TC5, TC7, TC8 trong LD; trong lúc chờ truy trường client đọc Phòng thủ%/Điểm tài phú.
- 20/11 14:25 [A] ĐÃ KIỂM B-049: đồ vàng +0→+1 vẫn ×1,25 (Sinh 148→185), Né/Nội không đổi; tài phú dòng công bố 0 dù mặc +1. KHÔNG ĐẠT, đã báo B. CHƯA KIỂM: TC3–TC8.
- 20/11 15:05 [A] #300: menu Lua 'Bao vat' mien phi (bo xanh/vang, thuy tinh, bac) thay cua hang vi KBuySell::Buy tu choi gia<=0; chep qh_bothu.lua len VM (.bak-q300), restart gs001 MOT lan (nap ~10 phut, B-049 da nap san). Go hook TEST: khoi phuc opensysui.lua .bak-q97, xoa qh_bothu.lua. Viec ke: LD bam Cuong hoa -> menu -> lay do, mac, chup anh, ghi dong thuoc tinh vao CUONG-HOA.md. CHUA KIEM.
- 20/11 14:47 [A] #300: AddItem chỉ nhét vừa vài món (túi server đầy rác). Thêm tùy chọn menu "Don sach tui" (ClearAllItem: xóa hết + tự thoát), chép lên VM, restart gs001 14:47 (nạp ~10 phút). Việc kế: LD vào lại -> Cường hóa -> Don sach tui -> vào lại -> bộ xanh -> mặc, chụp, ghi dòng thuộc tính vào CUONG-HOA.md. CHƯA KIỂM.
- 20/11 15:25 [A] #300 KẸT (3 lần): menu Bảo vật hiện đúng (ảnh q300-m3) nhưng túi nhân vật đầy rác nên AddItem chỉ nhét vài món; ClearAllItem và DelAllHanhTrang đều ScriptError 4 trên exe đang chạy (log gs001 14:58, 15:13). Thủ công "Rao" trong LD chưa vứt được. Cần: nhân vật mới túi trống (đổi tên hook) hoặc B thêm hàm dọn túi vào exe. Đã thấy trong túi: bộ vàng Mộng Long Thiếu Lâm (str 135, Hoàng Kim) có dòng tooltip (ảnh q300-one). CHƯA KIỂM: bộ xanh, nâng cấp +1/+2/+3.
- 20/11 15:25 [A] #300 TIẾN: tìm ra gốc bộ xanh trơn: AddItem luck=0 làm dòng ma thuật không rơi (KItemGenerator.cpp:959 nDecide = rand/(1+luck*20/100)); đổi luck=1000, restart gs001 15:24 (nạp ~10 phút). Dọn túi bằng tooltip "Ném" (ĐÃ KIỂM, vị trí nút = ô -106,+78). Bộ vàng Mộng Long đã mặc sẵn. Việc kế: relogin LD, menu Bộ XANH, đo +1/+2/+3 CHƯA KIỂM.
- 20/11 15:44 [A] #302: theo chủ chốt, dùng vai túi trống: tk tkatest02, vai atestqhhai (đã tạo bằng bot_tao_role). Đổi cổng hook qh_bothu.lua sang tiền tố 'atest' (hook TEST, nằm trong danh sách gỡ), chép VM, restart gs001 15:43 (nạp ~10 phút; gộp, không đổi exe). Việc kế: LD đăng nhập atestqhhai -> menu Bảo vật -> bộ xanh/vàng/thủy tinh/bạc -> mặc, đo +1/+2/+3, chụp, ghi CUONG-HOA.md. CHƯA KIỂM.
- 20/11 16:20 [A] #303 (Q-101, gộp #300/#302): sách = item script có sẵn (6,1,0) + script mới \script\itemaowubox.lua gọi qhbv_menu (chỉ tên 'atest'); online.lua (.bak-q303) tự cấp lại sách khi đăng nhập; menu: Dọn hành trang (giữ sách, FindItemEx(3,i,j)+RemoveItemByIndex), Đồ xanh (luck 1000 có dòng), Đồ vàng, Thủy tinh, Bạc, Thiết lập Thiếu Lâm; nút Cường hóa về UI Giao gốc. Chép VM, restart gs001 16:20 (nạp ~10 phút). Vai atestqhhai (tkatest02) kẹt vào game; tạo thêm tkatest03/atestqhba (native_place 54). Việc kế: LD vào atestqhba -> bấm sách -> menu -> mặc, +1/+2/+3, chụp, ghi CUONG-HOA.md. CHƯA KIỂM.
- Đang chờ: B (đồ vàng ×1,05 + qh_wealth).
- Thư đã đọc đến: #B-054.
- HÀNG ĐỢI B (L19, 20/11 16:35):
  - P0 #B-050 vá client EnChanceRong (DESIGN/QH-B049-client) — CHỜ A áp + build APK (CHƯA CHẠY).
  - P0 #B-051 Lua tài phú bảng=0 (QH-B044-deploy) — XONG, CHƯA CHẠY, CHỜ A nạp cùng 1 lần restart gs001 với B-050/B-049 (gộp theo L19.3).
  - P1 #B-052 thống kê vật phẩm — XONG 16:20 (commit 0f368a17, DU-LIEU/VAT-PHAM), đã báo Chat "B Xong".
  - P1 KT-01..06 — XONG, Chat đã duyệt.
  - P2 Phòng thủ% bảng = 0 (KNpc.cpp magic_physicsres_p) — CHỜ A truy client; Né tránh/Nội lực chưa nhân (thiếu id trong JxQhScalable) — CHỜ id từ A.
  - P1 #B-054 bảng đối chiếu loại thuộc tính + cột đọc được + ban_trung — XONG 20/11 (đợi Chat gửi chủ).
  - BỎ: không có.

## Sonnet B
- Tính năng: CUONG-HOA + TAI-PHU-PHI-PHONG — bước: server EnChanceRong (B-049, A nạp, đồ vàng vẫn ×1.25 do CLIENT) → vá client B-050 (DESIGN/QH-B049-client, CHƯA CHẠY) → Lua B-051 sửa bảng tài phú=0 (QH-B044-deploy/qianghua.lua + opensysui.lua, CHƯA CHẠY).
- Lệnh chạy tiếp: chờ A áp vá client + nạp Lua B-051 (1 lần restart gs001), đo lại tài phú bảng và đồ vàng ×1.05; sau đó Phòng thủ% (A truy client: CoreShell.cpp:1627, trường m_CurrentPhysicsResist).
- Đang chờ: A (vá client B-050, nạp Lua B-051 cùng đợt restart gs001).
- Hook B (D:\JX-wt\SONNET-B\.claude\settings.json): SessionStart (hook_luat.py start/postcompact, KIỂM chạy tay: ra LUAT-COT-LOI) và Graphify hook-guard (SessionStart compact, PreToolUse Bash|Grep|Read|Glob, KIỂM chạy tay exit 0) ĐỀU CÓ. Lưu ý: thư mục B chưa có graphify-out nên hook-guard không dẫn tới đồ thị; đồ thị server nằm ở QH-B035\...\Core\Src\graphify-out.
- Thư đã đọc đến: #B-054.
- HÀNG ĐỢI B (L19, 20/11 16:35):
  - P0 #B-050 vá client EnChanceRong (DESIGN/QH-B049-client) — CHỜ A áp + build APK (CHƯA CHẠY).
  - P0 #B-051 Lua tài phú bảng=0 (QH-B044-deploy) — XONG, CHƯA CHẠY, CHỜ A nạp cùng 1 lần restart gs001 với B-050/B-049 (gộp theo L19.3).
  - P1 #B-052 thống kê vật phẩm — XONG 16:20 (commit 0f368a17, DU-LIEU/VAT-PHAM), đã báo Chat "B Xong".
  - P1 KT-01..06 — XONG, Chat đã duyệt.
  - P2 Phòng thủ% bảng = 0 (KNpc.cpp magic_physicsres_p) — CHỜ A truy client; Né tránh/Nội lực chưa nhân (thiếu id trong JxQhScalable) — CHỜ id từ A.
  - P1 #B-054 bảng đối chiếu loại thuộc tính + cột đọc được + ban_trung — XONG 20/11 (đợi Chat gửi chủ).
  - BỎ: không có.
