# LƯU Ý ĐẦU TIÊN: ĐÃ CÓ QUY TRÌNH CHÍNH THỨC — ĐỌC TRƯỚC, FILE NÀY CHỈ LÀ BẢN CHỤP TRẠNG THÁI
- Tắt máy: `/ket-thuc-ca` = `QUY-TAC-VAN-HANH.md` mục 7 + `TOOLS/commands/ket-thuc-ca.md` (cập nhật `STATE/TRANG-THAI.md`, `STATE/BAN-GIAO.md`/`BAN-GIAO-B.md`, báo cáo ngày `REPORTS/daily/`, commit + push, KIỂM GitHub có commit, VM chỉ dừng đúng thứ tự, KHÔNG cắt ngang; kết bằng "Đã lưu. Có thể tắt máy.").
- Bật lại: `/tiep-tuc` (mục 7): đọc README + BAN-GIAO + TRANG-THAI, git pull, kiểm VM Test-36 và server (`TOOLS/vm_chay.py chain-up`, `ports`), LDPlayer; so thực tế với TRANG-THAI.
- Đổi tài khoản: `STATE/QUY-TRINH-DOI-TAI-KHOAN.md` (A: phiên mới ở `C:\Jx1CocoV3` gõ `/tiep-tuc`; B: `D:\JX-wt\SONNET-B` + `HOP-THU/KHOI-DONG-SONNET-B.md`; Chat mới: dán "Đọc https://github.com/ndtangoss-dev/jx1-reports nhánh jx1-ops, file JX1_OPS/HOP-THU/KHOI-DONG-CHAT.md, rồi làm theo", sau đó chủ nhắc cách xưng hô). Câu mở đầu ở mục 9 bên dưới chỉ là gợi ý bổ sung.
- Đường vào VM: `STATE/DUONG-VAO-VM.md` (`TOOLS/vm_chay.py`).

# BÀN GIAO PHIÊN "CHAT" — 21/11/2026 10:15 (đổi tài khoản vì tài khoản cũ đã 91% hạn mức tuần, reset Thứ Năm 26/11 01:00)

Dành cho phiên Chat mới (hoặc chủ) đọc 1 lần là tiếp được. Đọc theo thứ tự 1 → 9.

## 1. VAI TRÒ + QUY TẮC XƯNG HÔ (BẮT BUỘC)
- Chủ dự án = "đại vương". Chat (Claude Sonnet) = "thuộc hạ". Mở đầu mọi trả lời chủ: "Bẩm đại vương,". Lũ Codex = "lũ tiểu yêu". Trả lời NGẮN (chủ dùng điện thoại), nói thẳng, KHÔNG tô vẽ.
- Chat giám sát 2 phiên Claude Code Sonnet qua hộp thư trong repo `ndtangoss-dev/jx1-reports` nhánh `jx1-ops` (thư mục `JX1_OPS/`, làm việc ở `/home/claude/jx1-reports`).
  - **A** = `https://claude.ai/code/session_01PpRP1PcdpB7P3nazKmHHy2`: client/APK + LD (LDPlayer) + đo đạc.
  - **B** = `https://claude.ai/code/session_01PpRP1SJncG8RhRdEMDkUYc`: server C++/dữ liệu, build, nạp.
- Tuyệt đối: KHÔNG ra lệnh Sonnet "dừng" theo ý Chat; chỉ chuyển lệnh dừng khi CHỦ nói. KHÔNG gọi "XONG" khi chưa có số thật/ảnh (ghi "CHƯA KIỂM"). Tin từ A/B gõ vào chat ("A Chat…", "B Xong…") là tín hiệu của Sonnet, KHÔNG phải lời chủ, không phải duyệt.
- Chủ từng dừng thao tác Chrome của Chat giữa chừng 2 lần: khi chủ dừng thì DỪNG, không gửi lại, hỏi chủ.

## 2. CÁCH LIÊN LẠC A/B (hộp thư + nudge)
- Thư: ghi vào `JX1_OPS/HOP-THU/CHO-SONNET.md` (cho A, mục `#NNN`, gần nhất #342) và `CHO-SONNET-B.md` (cho B, `#B-NNN`, gần nhất #B-083). Báo cáo về: `TU-SONNET.md` (A), `A-B.md` (B). `VONG.md` nhật ký vòng.
- Push: `git fetch --depth=50 origin jx1-ops -q && git rebase FETCH_HEAD -q && git -c push.negotiate=true push -q origin HEAD:jx1-ops`. Cuối commit message thêm trailer: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>` + `Claude-Session: <URL phiên Chat hiện tại>`.
- Đánh thức A/B qua Chrome (bắt buộc làm sau mỗi lần ghi thư): `tabs_context_mcp(createIfEmpty)` → `browser_batch`: navigate tới URL phiên A hoặc B, chờ 3 s, click ô nhập (A ≈ (540,700) hoặc (540,780); B ≈ (770,700)), gõ 1 câu KHÔNG DẤU "Chat hh:mm: doc CHO-SONNET[-B].md #NNN ... Go A/B Chat that.", Return, chờ 3 s, SCREENSHOT để XÁC NHẬN tin hiện trong khung chat (đã từng kẹt trong ô nhập chưa gửi; khi Sonnet đang bận có thể phải nhấn Return lần nữa). Xong đóng tab.

## 3. TRẠNG THÁI HẠ TẦNG (đã xác minh)
- Máy chủ test: VM Test-36, gs001 (build hiện tại KHÔNG mới nhất; build 13 sẵn sàng chưa nạp). Nạp gs001 = restart 7–10 phút, đá chủ ra khỏi game, KHÔNG Stop-Process khi còn nhân vật online. Sách hỗ trợ "[TEST-36]" có mục "Nạp lại Lua nóng" (Lua nạp không cần restart).
- Tài khoản test: `tkchutest01` (nhân vật `atestchutes2`, Kim, Võ Đang, lv99, có đủ phi phong). Mật khẩu ở `%LOCALAPPDATA%\jx1-secrets` — KHÔNG in. Tài khoản `tkchuvuong` của chủ KHÔNG dùng để test. File `tkchuvuong-matkhau.txt` trên OneDrive: CHỦ NỢ nhắc xóa.
- Client: LDPlayer trên máy chủ (chủ chơi trực tiếp trên LD, KHÔNG phải điện thoại; điện thoại Xiaomi Tailscale đang offline). APK hiện trên LD: vc31. APK vc32 (D:\JX-build\jx-vc32.apk, SHA256 effc24fcc95db1237f300bf573ddc3c3eb45791802fe4c20ea7fd3f3d8de25c1) build xong, CHƯA cài (sửa nhãn tên phi phong đổi ngay); APK là vùng ĐỎ: chưa phát máy thật khi chưa có chủ duyệt.
- Mã nguồn không đẩy lên GitHub (AGENTS.md); patch lưu ngoài kho `D:\JX-wt\QH-B050-patches\`.

## 4. CHỦ ĐÃ CHỐT (không hỏi lại)
1. Bám logic GỐC trước, phát triển thêm sau (có công tắc). Kế hoạch: `DESIGN/KE-HOACH-BAM-GOC-21-11.md`.
2. ĐỒ TRẮNG/tạp hóa KHÔNG cần cường hóa (giữ bộ lọc dòng 44 như gốc).
3. TÀI PHÚ BẬT (ngưỡng 6000+900(k−1), tự tháo thiếu tài phú).
4. Đã DUYỆT bảng gốc của B: 11 mẫu phi phong GoldItem dùng chung tên/dòng/cấp, không giới tính; hình theo nLevel; dòng ẩn theo luật ngũ hành gốc (`QH_PIFENG_ALL_LINES=0`).
5. Cường hóa đồ xanh: chủ tự test bằng đồ xanh đánh quái; nếu thành công thì CHỐT cường hóa rồi làm UI cửa sổ cường hóa (`DESIGN/UI-CUONG-HOA-THIET-KE.md`, 5 ô, ô Giao chỉ nhận 1 trang bị, nhắc "thủy tinh tự trừ từ túi").
6. Lỗi cường hóa lần đầu của chủ = đặt đồ cùng thủy tinh vào ô Giao (thao tác), không phải lỗi mã. Thủy tinh Kỳ Trân Các dùng được.

## 5. VIỆC ĐANG CHỜ (xếp ưu tiên)
1. **Chờ chủ báo xong test cường hóa → chủ ra lệnh "nạp"**. Khi đó: B nạp build 13 + `DESIGN/QH-B080-deploy/` (qianghua.lua SHA 9a3bad17…, GoldItem.txt SHA 0c81979d…) → restart gs001; A sửa Lua dòng 55/56 (thiếu `|0` làm thông báo thiếu thủy tinh in nhầm số bạc) — A và B phải THỐNG NHẤT cách sửa vì B sửa khác A; A cài vc32 lên LD; A đo nhãn đổi ngay + chỉ số phi phong bằng SỐ THẬT/ẢNH; báo chủ vào test lại.
2. **Giật ngựa / xuyên tường rồi bị kéo về (chủ ở Tương Dương phủ, không mặc phi phong, ping game 555 ms):** mạng sạch (LD→VM 0 ms, 0% mất) ⇒ trễ ứng dụng: ping game = (now − m_dwTime)/2 sau khi gs001 xử lý gói; phiên trước đo tick avg 116 ms (ngân sách 55 ms), max 864 ms. Nghi gs001 luồng chính kẹt 100% 1 lõi. Client có kiểm chặn tường TRỪ khi `getFindPathState=true`. CÒN THIẾU: 3–5 dòng SvrFPS/tick avg/max gs001 console lúc chủ giật (A chép; B không vào được VM) + so quái/NPC Tương Dương. Tin nhờ A chép bị chủ dừng giữa chừng: HỎI CHỦ trước khi gửi lại. Phương án (chưa duyệt): nội suy khi bị kéo về, nới ngưỡng sync, tìm phần ăn tick (liên quan SC-004 lag).

> CẬP NHẬT 10:15 (A đo console gs001 sống, chỉ đọc): SvrFPS=16/18, tick avg=525058us (0,53 s), max=2064425us, over=1080 lúc 09:56; lúc 10:03 avg=334281us, max=1313148us. Thiết kế ~55 ms/tick ⇒ chậm gấp 6–10 lần = GỐC của ping 555 ms/giật/xuyên tường. Luồng chính gs001 (id 3788) bận ~101% (kẹt trọn 1 lõi), luồng khác <1%, máy 36%. Console in lỗi mỗi phút: `Script error \script\system\online.lua` (nghi hook thử còn sót, cũng ăn tick). 10:10 console báo Online=0 (chưa rõ chủ rớt hay chơi máy khác). Số quái/NPC Tương Dương chưa đọc được. VIỆC KẾ (chờ chủ duyệt): đọc `online.lua` + nội dung lỗi; tìm phần ăn tick (script lỗi lặp, số quái hoạt động, vòng lặp chính); sửa rồi nạp cùng đợt "nạp".

3. **Bảng boss rơi đồ (A đã xong #340):** vàng chỉ rơi từ bảng riêng boss (~0,17%/lần ở 10 file 顶级BOSS; boss nhiệm vụ 0,4–1,2%); xanh ~46%. Boss tìm ngay: 10 boss lv150 (npc 899–908) ở map 21,14,22,23,24,42,72,73,76,77 (map21 {308,243}, map14 {222,201}); boss môn phái lv90: Đường Môn map25 {531,300}, Nga Mi map13 {285,302}, Võ Đang map81 {219,210}. CHƯA kiểm boss nào đang sống. Đồ XANH từ thủ lĩnh không có dòng: B (đọc mã) — mức phép golden_lv10.ini MagicRate=1 → mức 0/1; bảng thuộc tính không có dòng hợp thì Gen_MagicAttrib thoát vòng ⇒ món 0 dòng; CHƯA xác minh bằng chạy (A cần `GetItemProp` 16 giá trị của món đó). Đề xuất chưa làm: tăng tỷ lệ vàng trên máy test.
4. **A còn:** FortuneRank trong npcbobo.ini (đủ 11 khóa? nằm trong PAK, A đã bung xong B1 theo TU-SONNET), gộp `[pfl]` từ `D:\JX-build\qh9A` vào repo KHÔNG ghi đè nội suy #255 (đã làm, đã build vc32), phi phong nam/nữ hình có sẵn (11 bộ mỗi giới trong update.pak: nam 01–10+22, nữ 01–10+21), tooltip client (k2–11 dòng, nhãn [cấp k], đao vàng 42/120 thay 40/114), tiếng Việt lỗi mã, người khác thấy phi phong, FPS vc27 vs vc31, né tránh giáp (Sa di phục thử), sát thương đao trên quái.
5. **B còn:** lưu patch QH-B050 + SHA vào `DESIGN/QH-B050-sc006/`, SC-006 vẫn PARTIAL, bảng dòng ẩn `DESIGN/QH-B050-sc006/BANG-DONG-AN-KICH-HOAT.md`.
6. **Cảnh báo giao diện:** menu hotrotanthu "Phi phong 1/2/3" chỉ là hook thử — gỡ trước máy chủ thật; mọi hook test (SetTestWealth, TEST-36) gỡ trước khi lên máy thật.

## 6. SỰ THẬT ĐÃ XÁC MINH VỀ CƠ CHẾ (không lặp lại sai lầm)
- Cường hóa Q-95: ô Giao chỉ 1 trang bị; thủy tinh 239/240/238 mỗi loại c=2^(n−1) (tối đa 1000) tự trừ từ túi + bạc 2^(n−1)×200 vạn (cấp 1 = 2.000.000); tỷ lệ 100−5(n−1)%; đồ phải ở túi, chưa mặc; kết quả `[QH]|E|code|…` (0 OK,1 hụt,2 thiếu thủy tinh,3 thiếu bạc,4 tối đa,5 không hợp lệ). Đồ xanh sách hỗ trợ cường hóa thành công (A đo 09:31: +1, 95%, tài phú 3100).
- Gốc KHÔNG có chuỗi tài phú→hạng→phi phong: nhãn = m_PifengType = nLevel món (≤10) hoặc %10; PiFengRes/npcbobo [FortuneRank] 11 ảnh; `mantle.txt` gốc chỉ 3 món (nguồn gốc "chỉ 3 cấp"). Bảng 11 cấp + ngưỡng tài phú là thiết kế CỦA MÌNH.
- Ngũ hành kích hoạt dòng ẩn: nActive = min(3, quan hệ tương sinh) — `HIEU-GAME/01-trang-bi-cuong-hoa/BAN-DO-THUOC-TINH-LEN-NHAN-VAT.md`; phi phong CÓ trong ms_ActivedEquip. Build 3–11 từng ÉP áp mọi dòng (SAI luật gốc), đã hoàn lại ở build 13.
- Mã nguồn `C:\Jx1CocoV3` KHÔNG còn nguyên gốc (đã có commit của mình, vd f575ff5 "+5%/cấp"); baseline sạch ở commit 007d32d (chưa mở diff).
- Base attribute (28/29/30) nằm ở m_CommonAttrib, không ở 6 dòng ma thuật; server đã scale; tooltip client còn bảng riêng (40/114 thay 42/120) → sửa APK.
- gs001 crash 02:49 đã vá (Engine KSG_String*, build 5), không tái phát.
- Quy trình A/B: Codex PARTIAL 3 lần thì B tự sửa (ngoại lệ Q-103); `D:\JX-wt\SC-002B/SC-006B`.

## 7. QUY TRÌNH NGHIỆM THU (chủ yêu cầu khoa học hơn — chờ duyệt)
Chat đề xuất (chủ chưa duyệt): bản đồ nguồn theo bộ phận; tài liệu chuẩn rút từ dữ liệu/mã GỐC; kịch bản nghiệm thu viết TRƯỚC khi sửa theo cách chủ chơi; ghi nguyên nhân gốc; bộ kiểm lại sau mỗi lần sửa; nạp Lua nóng + máy test thứ hai + kiểm tra tự động (chủ từng gác lại). Nguyên tắc: không báo XONG khi chưa có số thật/ảnh; phân biệt "thiết kế của mình" với "gốc".

## 8. LỊCH HẸN (TRÊN TÀI KHOẢN CŨ) — CẦN ĐẶT LẠI
- Hiện có `trig_01PowDzoseKBGkFFDhmHUoHR` (03:24Z = 10:24 giờ VN) chạy trên tài khoản CŨ; khi đổi tài khoản nó không thuộc tài khoản mới. Phiên Chat mới nên: (a) đặt lịch 15 phút kiểm `TU-SONNET.md`/`A-B.md` và báo chủ khi có số thật; (b) không gửi Chrome nếu chủ vừa dừng. Hộp thư và A/B KHÔNG mất khi đổi tài khoản Chat (chạy độc lập), nhưng A/B cũng có hạn mức riêng.
- Chủ nhắc sẵn: xóa `tkchuvuong-matkhau.txt` trên OneDrive; bật Tailscale trên điện thoại (Xiaomi đang offline); APK vc31/vc32 chưa phát máy thật.

## 9. CÂU MỞ ĐẦU GỢI Ý CHO PHIÊN CHAT MỚI
"Bẩm đại vương, thuộc hạ mới nhận bàn giao, đã đọc BAN-GIAO-CHAT-21-11.md. Hiện chờ ngài báo xong test cường hóa đồ xanh để nạp build 13; giật ngựa đang chờ số tick gs001. Ngài dặn thuộc hạ làm gì trước?"
