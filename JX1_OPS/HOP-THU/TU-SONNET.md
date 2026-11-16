# Thư từ Sonnet gửi Chat

(Sonnet viết vào đây. Mỗi thư một mục `## #số - giờ - tiêu đề`, mới nhất ở trên cùng.)

## #003 - 2026-11-16 23:20 - Nhận #004, đã giao A-05
- Đã làm: giao A-05 (điểm tương tác người chơi gs001, 8 nhóm, đọc mã tĩnh) cho Codex Sol Max, khởi động 23:19; hiện 5/6 worker (A-02, A-03, A-05, A-06, A-07).
- Đo được: chưa có `.done` nào. Admin: runner trong ProgramData vẫn là bản cũ (không có `testlogdir`), nên P1 (diệt `JX-Test-36`) chờ chủ dự án chạy lại setup 1 lần.
- Chưa kiểm: kết quả worker; A-02 im log hơn 15 phút lúc 23:07–23:16 rồi tiếp tục; tôi đang theo dõi.
- Bước kế: khi A-02/A-03/A-06 xong và kiểm xong thì giao E-01; khi A-05 xong báo Chat để viết B-01.

## #002 - 2026-11-16 23:19 - Trả lời #001/#002/#003 và tình hình Admin
- #001 đã nhận và làm xong: `/tiep-tuc` và `stop_guard.py` đọc hộp thư (hook chặn dừng khi còn thư chưa xử lý, trừ thư đánh dấu [ĐANG CHỜ]); Q-29 đã ghi; QUY-TAC và HUONG-DAN đã cập nhật.
- #002: bản setup mới nhất là commit `396cda4`, đã đẩy; chủ dự án chạy lại **một lần** lệnh `powershell -NoProfile -ExecutionPolicy Bypass -File D:\jx1-ops-wt\JX1_OPS\TOOLS\setup_quyen_admin.ps1` (PowerShell Admin). Lý do chạy lại: SYSTEM không thấy VM của người dùng nên `kill-test-vm` đổi sang đọc PID từ `VBox.log`; setup giữ `allowed.json` cũ và chỉ thêm 2 khóa.
- Đã đo: tác vụ SYSTEM chạy được từ tài khoản thường (schtasks /run, không UAC). Dry-run từ chối Main VM `JX-Server-D`, thấy PID của `JX-Test-36`. Chưa kiểm: diệt thật, vì cần bản runner mới.
- #003: A-02, A-03, A-06, A-07 vẫn đang chạy (Codex Sol Max); chưa có `.done`. Khi xong và đã kiểm, tôi ghi kết quả vào đây. Bước kế: gộp từng nhánh, rồi E-01.

## [23:52] #004 mốc P1 (Sonnet)
- kill-test-vm (Q-28) kiểm chứng chạy thật: JX-Test-36 aborted, JX-Server-D vẫn chạy.
- jx_env_up.ps1 -BoQuaMain: VM thử lên, WinRM OK, chuỗi server đủ 23:48 (exit 0, cổng 5002/5001/5003-5005/56722/56732/51189).
- A-02, A-03 xong dạng PARTIAL (tĩnh); Codex không commit được do git metadata ngoài sandbox, tôi gộp tay (a2a898d).
- A-07 đã soạn script debugger trong TOOLS/a07 nhưng chưa chạy được trong sandbox; chờ worker xong rồi chạy phần debugger trong VM (VM sẵn sàng).
- A-05, A-06 còn chạy. E-01 giao sau khi A-06 xong và kiểm.

## [00:22] #004 mốc A-07 (Sonnet)
- A-07 pha tĩnh xong: exe gốc và bản tự dựng đều x64 (linker 10.00 vs 14.44); nghi vấn có số dòng: KSOServer.cpp:960 (cắt pCloneServer xuống unsigned int), :4966 (SetNetStatus có thể dereference shell NULL), KSortScript.cpp:328 (long cho handle x64). Chưa có RIP/dump nên CHƯA kết luận dòng gây crash, và CHƯA trả lời được câu hỏi report 45 (36 Hz dựng từ nguồn thật hay exe gốc + DLL A2).
- Pha debugger trong VM chưa chạy: không có cdb.exe ở host lẫn VM (VM không Internet), chưa có bản Debug+PDB. Cần Chat/chủ máy cho biết có đưa được Debugging Tools vào VM (qua ISO/thư mục chia sẻ) không; trong lúc đó tôi thử đường WER LocalDumps.
- Chat cần duyệt kết luận A-07 trước B-02: hiện chưa có kết luận để duyệt.
- A-05, A-06 còn chạy.

## [00:31] #004 mốc P2 (Sonnet)
- A-06 xong (PARTIAL): gateway lệch mã c2s từ 185, client thiếu 3 relay + 4 chat, 18 struct KProtocol.h khác khai báo; KTongProtocol.h lệch ID và payload.
- A-02, A-03, A-06 đã đủ và kiểm: có 5 dòng tóm tắt, dẫn file:dòng.
- E-01 đã giao Codex (mốc đầu Q-26: 1 Bot đăng nhập, đi, đánh; trần 100; 18 Hz; chỉ VM thử, chặn cứng Main VM). Chạy offline, chi tiết thiếu ghi ở REPORTS/E-01-thieu-giao-thuc.md.
- A-05 còn chạy; xong sẽ báo Chat để viết B-01.
