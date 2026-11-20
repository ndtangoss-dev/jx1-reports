# BÀN GIAO CHAT 20/11 22:25 (sắp hết hạn mức 5h = 93%, hồi 23:50)
Xưng hô chỉ trong khung chat: chủ = "đại vương", Chat = "thuộc hạ", mở bằng "Bẩm đại vương,", cảm ơn = "đa tạ", Codex = "lũ tiểu yêu". Không ra lệnh Sonnet dừng. Báo ngắn, giản dị (app điện thoại).

## Bối cảnh nhanh
Chat (Claude) giám sát A (`claude.ai/code/session_01PpRP1PcdpB7P3nazKmHHy2`) và B (`session_01PpRP1SJncG8RhRdEMDkUYc`) qua repo `ndtangoss-dev/jx1-reports` nhánh `jx1-ops`, thư mục `JX1_OPS/`. Chủ muốn tự vào LDPlayer (emulator-5556) test cường hóa + giật lag; chỉ mời khi cường hóa đạt số đo thật (cửa chặn #327).
Tín hiệu A/B gõ thật vào khung chat này: `A Xong`/`A Chat`/`B Xong`/`B Chat` (L15). Đã chạy 20/11 21:10. "B Xong #B-074" đến 22:25 chưa đọc.

## Kết quả đã có (số thật, A đo)
- Mất đồ sau relog: KHÔNG do exe B-039 (bisect 3 DLL + exe: 20/20). Thủ phạm = hook `QHBV_Book` trong `OnLine` (cấp sách lúc OnLine, chạy trước nạp). A đã gỡ dòng `QHBV_Book()` khỏi online.lua (.bak-331); CHƯA kiểm relog sau restart gs001. Test-36 đang chạy B-039 đầy đủ.
- Cường hóa đồ xanh +1..+3 trên LD: ĐÚNG trừ bạc (200/400/800 vạn), thủy tinh (1/2/4 mỗi loại), relog giữ đồ+cấp, không cộng dồn, mặc/tháo đúng. Tỉ lệ: thông báo 95/90/85 là của lần KẾ TIẾP, roll thật đúng spec (chưa đo nhiều lần).
- Q-104 (chủ): làm tròn GẦN NHẤT (51→54, 10→11 đúng). Không sửa.
- Còn lệch: dòng sát thương cơ bản không tăng (loại 28, 29, 30; 40 chưa xác minh) → SC-002 (Codex, status ready): thêm 28/29/30 vào `JxQhScalable`, giữ EnChanceRong +5%; A xác nhận dòng "14/37" là dòng nào (B đã sửa: 14, 37 KHÔNG phải sát thương).
- Đồ vàng +1 (server + tooltip APK vc28 SHA 7ec4c13c…df145e, đã cài LD) CHƯA ĐO: túi atestvaihero không có đồ vàng, biểu tượng nháy; A gợi ý dùng lệnh bài GM "Nhận Thẻ GM". Đây là điều kiện nghiệm thu.
- Chưa có: tài khoản test riêng cho chủ (không phải tkchuvuong/atestvaihero) có sẵn 10 xanh + thủy tinh + bạc; ảnh cửa sổ Giao đầy đủ (q328-*), bảng kỳ vọng so với số đo.

## Quyết định chủ trong phiên này
- Test-36 là bãi thử, tự do làm; bản gốc không đụng. (Q-103) APK/client do A làm trực tiếp (không Codex); server C++ vẫn qua Codex theo Q-102. Bảo vật bán giá 1 bạc, ĐƯA ĐỒ VÀO KỲ TRÂN CÁC CÓ SẴN (phím Bảo vật cạnh nút bánh răng, shop id 99–102, hàng nằm trong buysell/goods của CLIENT PAK) — cần sửa cả server và client; việc này xếp sau cường hóa (SC-005). Chủ sẽ tự thao tác LDPlayer A đang dùng: A không động vào LD khi chủ thử (#326).
- Tìm nguồn phiên trước (máy thật `C:\Jx1CocoV3`, đã được cấp quyền đọc `docs-analysis` và `.git`; tóm tắt đã lọc ở `HIEU-GAME/09-cong-cu-gm/NGUON-PHIEN-TRUOC-JX1COCOV3.md`). Bài học phiên trước: tooltip VN ở `vn/gameui/KuiItemdescVN.cpp`; vá giật lag có ở `docs-analysis/patches/31,33,34,47` nhưng B kiểm: 31/33/34 KHÔNG áp sạch vào qh9A → port tay (SC-004, A làm khi tới lượt).

## Việc kế tiếp (theo thứ tự)
1. Đọc `B Xong #B-074` (không có việc gì mới ngoài SC-002), hỏi A kết quả relog sau khi gỡ hook (cần restart gs001 ~7-10 phút), đo vàng +1 (lệnh bài GM), lập tài khoản test riêng cho chủ.
2. SC-002 qua Tổng quản/Codex → exe mới → A nạp + đo dòng sát thương. Gate #327: chỉ mời chủ khi (1) nạp đồ ổn, (2) xanh +1..+3 đúng, (3) vàng +1 ≈5% ở server + tooltip, (4) chỉ số nhân vật đúng khi mặc/tháo, (5) ảnh + bảng kỳ vọng. Chưa đạt → CHƯA KIỂM, không mời.
3. Giật lag (SC-004) sau cùng, A port tay vào `D:\JX-build\qh9A`.
4. Cuối cùng: gỡ hook test (qh_bothu.lua, sách TEST-36, gmroleitem.lua, systemtest_hook.lua, baowubox/online hook) trước server thật.

## Cảnh báo / việc chủ
- Hạn mức tuần ~60–69% (reset Thu 26/11 01:00); dồn việc nặng cho Codex.
- Nhắc chủ: xóa `tkchuvuong-matkhau.txt` trên OneDrive; Tailscale trên điện thoại. Không dùng tkchuvuong cho test (dành chủ tự chơi).
- Lịch: `send_later` kiểm 20 phút đang chạy (trigger trig_01QQJtsMK5umBQBxJnb6RgWV ~22:32); đã đặt thức dậy 23:52 sau khi hạn mức 5h hồi 23:50. Khi thức: ReadNotifications, đặt lại send_later 20 phút, fetch/rebase, đọc TU-SONNET.md, A-B.md, CUONG-HOA.md (d11+), DANG-LAM.md, TASKS/SC-*.
- Quy trình đẩy: `git fetch --depth=50 origin jx1-ops -q && git rebase FETCH_HEAD -q && git -c push.negotiate=true push -q origin HEAD:jx1-ops`; trailer commit `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>` + `Claude-Session: https://claude.ai/code/session_01PpRP1RsTM84wYR3832CGxc`.
- Nhắc A/B qua Chrome khi đứng: A ô nhập (540,700), B (770,700) trên màn 1568x751; gõ không dấu; đóng tab sau.
