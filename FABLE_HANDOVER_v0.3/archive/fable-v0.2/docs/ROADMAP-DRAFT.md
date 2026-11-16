# DEVELOPMENT ROADMAP – BẢN NHÁP

Phiên bản v0.2 – 2026-11-16 – Fable soạn. Opus hoàn thiện và được đổi thứ tự khi có lý do kỹ thuật.

Gồm hai phần: **A** là kế hoạch thử nghiệm 7 ngày lấy từ Master Prompt (mục 24), **B** là lộ trình xây game do Fable đề xuất để Opus dùng làm điểm xuất phát. Phần B chưa có mốc thời gian vì chưa đo được tốc độ thật của đội AI; kết quả phần A là căn cứ để ước lượng.

---

## Ba giai đoạn (Master Prompt mục 26–28)

1. **Fable cấu trúc.** Xong khi chủ dự án chấp nhận bộ tài liệu v0.2.
2. **Opus tiếp quản và lập kế hoạch.** Chưa thay đổi lớn lên source hoặc server. Kết thúc khi Opus trình kế hoạch tổng thể.
3. **Triển khai.** Chỉ sau khi chủ dự án phê duyệt kế hoạch tổng thể.

---

# PHẦN A – THỬ NGHIỆM 7 NGÀY CLAUDE PRO

**Mục tiêu:** chứng minh đội AI nhận mục tiêu, chia việc, triển khai, kiểm thử, bàn giao và làm tiếp được khi thay model. Không phải cài thật nhiều plugin hay mở thật nhiều worker. Không tiêu quota chỉ để tăng số worker.

Bảy ngày này không đủ để làm xong game. Sản phẩm của nó là một hệ thống làm việc đã được kiểm chứng và một kế hoạch tổng thể.

| Ngày | Chủ đề | Việc | Kết quả kiểm chứng được (đề xuất của Fable) |
|---|---|---|---|
| 1 | Kiểm kê và chuẩn bị | Kiểm kê GitHub và local; kiểm tra tài khoản, model, công cụ; kiểm tra Claude Code và Codex; chuẩn hóa tài liệu nền; dựng bộ nhớ dự án | `CURRENT-STATUS.md` đúng thực tế; agent registry có số đo thật; Secret Vault dựng và thử khôi phục xong; báo cáo ngày đầu tiên |
| 2 | Kiến trúc | Xác minh yêu cầu sản phẩm; thiết kế kiến trúc mục tiêu; thiết kế Bot System; thiết kế hệ thống AI; roadmap | Bản kiến trúc nháp, các câu hỏi Q-01…Q-09 đã gửi chủ dự án; **kế hoạch tổng thể trình chủ dự án phê duyệt** |
| 3 | Điều phối | Thử Orchestrator; nối Claude Code và Codex; tạo worker; kiểm tra worktree; giao việc song song | Ít nhất 2 worker khác nhà cung cấp hoàn thành task song song không giẫm lên nhau |
| 4 | Review và tích hợp | Thử PR; chạy CI; review; xử lý merge conflict; tự sửa lỗi | Một lỗi cố ý được phát hiện, quay về đúng worker và sửa xong mà chủ dự án không can thiệp |
| 5 | Tối ưu | Thử Claude-Mem, Graphify, Archify, Headroom, OmniRoute; đo token và chi phí | Bảng quyết định công cụ điền đủ, có số đo trước và sau |
| 6 | Thay thế AI | Thay worker; thay model; khôi phục task; tiếp quản từ báo cáo; kiểm tra không mất tiến độ | Một task dang dở được AI khác làm tiếp chỉ từ repo; một lần diễn tập đổi PM |
| 7 | Nghiệm thu | Bài kiểm tra thực tế; đánh giá chất lượng, tốc độ, chi phí, mức tự chủ; quyết định tiếp tục hay điều chỉnh | Báo cáo nghiệm thu với các chỉ số bên dưới, bằng số đo thật |

**Chỉ số đánh giá:** thời gian hoàn thành; số task hoàn thành; tỷ lệ nghiệm thu; số lỗi; số lỗi tự sửa; xung đột khi chạy song song; token và chi phí; thời gian cần chủ dự án can thiệp; khả năng thay thế AI; khả năng khôi phục sau khi mất phiên.

**Ba điểm cần lưu ý:**

- *Task dùng để thử là task gì?* Ngày 3–6 cần task thật để giao. Trong khi đó giai đoạn 2 chưa cho phép thay đổi lớn lên source hoặc server. Đề xuất: dùng các task nhỏ, có ích và tách biệt (bộ khung repo mới, CI, script sinh bảng trạng thái, build mẫu Axmol, công cụ đọc dữ liệu tham khảo). Không đụng source gốc, không đụng server đang chạy.
- *Phê duyệt giữa chừng.* Đề xuất Opus trình kế hoạch tổng thể cuối ngày 2 để việc triển khai thật có thể bắt đầu ngay khi được duyệt, không phải đợi hết 7 ngày.
- *Đồng hồ 7 ngày.* Nếu thời gian dùng thử đã bắt đầu chạy thì giai đoạn Fable đang tiêu vào đó. Ngày 6 (thay thế AI) cũng là buổi diễn tập cho tình huống thật ở ngày 8.

---

# PHẦN B – LỘ TRÌNH XÂY GAME (ĐỀ XUẤT)

Nguyên tắc: xác minh trước khi thiết kế; hợp đồng trước khi song song; một lát cắt chạy thật từ đầu đến cuối trước khi mở rộng; Bot vào sớm vì là nền tảng. Mỗi mốc kết thúc khi đạt tiêu chí thoát.

## M0 – Kiểm kê và xác minh *(trùng ngày 1 của phần A)*
Kiểm kê GitHub (HEAD, commit `2a1c0d9`) và `C:\Jx1CocoV3`; chỉ mục báo cáo 00–66 và `HANDOVER-FIX34.md` kèm nhãn tin cậy; kiểm kê server clone, VM, database, CDN, Tailscale; tài khoản và quota; Secret Vault; scheduler báo cáo; build mẫu Axmol với toolchain mục tiêu.
**Thoát:** trạng thái dự án đúng thực tế; danh sách mâu thuẫn và lỗ hổng tri thức; vault đạt tiêu chí nghiệm thu; báo cáo 22:00 chạy bằng lịch thật.

## M1 – Kiến trúc và hợp đồng *(bắt đầu ngày 2)*
ADR cho: mô hình thế giới và hiển thị, kiến trúc server, giao thức mạng, lưu trữ MySQL, chiến lược Git. Tài liệu 02–11 đủ để chia việc. Hợp đồng gói tin, schema lõi, interface giữa module. CI tối thiểu. Chiến lược test, gồm test Bot bằng mô phỏng không cần client.
**Thoát:** kế hoạch tổng thể được chủ dự án phê duyệt; các câu hỏi gameplay chặn kiến trúc đã có câu trả lời; một worker mới đọc tài liệu là viết được module theo hợp đồng.

## M2 – Lát cắt đầu tiên chạy thật
Đăng nhập → tạo nhân vật → vào một bản đồ → di chuyển. Client Axmol Windows, server x64, MySQL. Build thử Android (và iOS nếu có máy Mac) để lộ sớm vấn đề nền tảng.
**Thoát:** chủ dự án tự mở game và đi lại được; có test tự động cho luồng này.

## M3 – Chiến đấu lõi
Quái và NPC; combat, skill, trạng thái, hồi máu; vật phẩm rơi, túi đồ, trang bị cơ bản.
**Thoát:** săn quái, lên cấp, nhặt và mặc đồ được; công thức có unit test.

## M4 – Bot System v1
Bot là thực thể phía server; scheduler và quản lý dân số; hành vi di chuyển, săn quái, dùng skill, hồi máu, chuyển bản đồ; tiến trình, túi đồ, lưu trữ; đồng bộ giữa các client; mô phỏng tải không cần client.
**Thoát:** Bot giữ đúng trạng thái qua lần khởi động lại server; hai client thấy cùng một Bot ở cùng trạng thái; đo được chi phí mỗi Bot so với chỉ tiêu Q-05.

## M5 – Tiến trình và nhiệm vụ
Nhiệm vụ, Bot làm nhiệm vụ; hoàn thiện kỹ năng, trang bị; UI chính; âm thanh, hiệu ứng.
**Thoát:** vòng chơi đơn hoàn chỉnh tới một mốc cấp do Opus đặt.

## M6 – Hiển thị, instance và hoạt động nhiều người đầu tiên
Visibility Rules, Instance Management, Matchmaking, Event Capacity, Party và Team. Tống Kim làm hoạt động mẫu. Khung hoạt động dùng chung.
**Thoát:** test tự động chứng minh người chơi không thấy nhau ở bản đồ thường và thấy nhau trong Tống Kim; giới hạn số người được server thực thi.

## M7 – Các hoạt động còn lại
Mỗi hoạt động một module trên khung M6: Dã Tẩu, Boss Sát Thủ, Hoàng Kim, Nhiệm Vụ Hoàng Kim, Câu cá, Vận tiêu, Hạt Huy Hoàng, Thuyền Phong Lăng Độ, Vượt Ải, Liên Đấu, Hoa Đăng. Phần này hợp với nhiều worker song song.
**Thoát theo từng hoạt động:** có tài liệu luật chơi, test tích hợp, Bot tham gia đúng thiết kế.

## M8 – Quản trị và vận hành
Web Admin, Mobile Admin; logging, monitoring; triển khai, sao lưu, khôi phục; bản Android, iOS, Windows.
**Thoát:** dựng lại môi trường từ đầu theo tài liệu; khôi phục database từ bản sao lưu đã thử.

## M9 – Gia cố
Test tải theo Q-05; tối ưu bộ nhớ, Auto Batch; rà bảo mật; chạy dài ngày tìm rò rỉ và lệch trạng thái Bot.
**Thoát:** đạt chỉ tiêu hiệu năng đã thống nhất; không còn lỗi nghiêm trọng mở.

## Phụ thuộc

```
M0 → M1 → M2 → M3 → M4 → M5
                    └──→ M6 → M7
M2 ──→ M8 (logging, triển khai làm sớm)        M4, M6 ──→ M9
```

Trước khi xong M1 không mở nhiều worker viết code game. Sau M1, client và server tách worker được. Sau M6, các hoạt động tách worker được.

## Rủi ro ảnh hưởng lộ trình
- PM chạy trên tài khoản dùng thử 7 ngày.
- iOS cần máy Mac và tài khoản Apple Developer.
- Chưa có chỉ tiêu quy mô (Q-05).
- Nguồn hình ảnh, âm thanh chưa rõ (Q-08), có thể chặn từ M2.
