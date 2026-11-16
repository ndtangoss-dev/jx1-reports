# DEVELOPMENT ROADMAP – BẢN NHÁP

Phiên bản v0.1 – 2026-11-16 – Fable soạn. Opus chịu trách nhiệm hoàn thiện và có quyền đổi thứ tự khi có căn cứ.

Bản nháp này không có mốc thời gian: Fable chưa biết hiện trạng source, năng lực thực tế của worker và hạn mức tài khoản. Opus gắn thời gian sau M0. Mỗi milestone kết thúc khi đạt đủ tiêu chí thoát, không phải khi hết thời gian.

Nguyên tắc sắp xếp: xác minh trước khi thiết kế, hợp đồng trước khi song song, một lát cắt dọc chạy thật trước khi mở rộng, Bot vào sớm vì là nền tảng.

---

## M0 – Kiểm kê và xác minh

Chủ yếu L1–L3, Opus chủ trì, Haiku và Sonnet hỗ trợ đọc và tóm tắt.

- Kiểm kê GitHub: branch, HEAD, commit `2a1c0d9`, thay đổi gần đây.
- Kiểm kê `C:\Jx1CocoV3`: so với GitHub, tìm tài liệu chưa đẩy lên.
- Lập chỉ mục báo cáo 00–66 và `HANDOVER-FIX34.md` kèm nhãn tin cậy.
- Kiểm kê server clone, VM, database, CDN, Tailscale, cấu hình build.
- Xác minh tài khoản, model, quota, khả năng song song.
- Đánh giá Orchestrator và các công cụ ở Phần VIII theo bảng quyết định.
- Thử build Axmol mẫu trên Windows với toolchain mục tiêu.

**Thoát:** `CURRENT-STATUS.md` phản ánh đúng thực tế; danh sách mâu thuẫn và lỗ hổng tri thức; bảng quyết định công cụ; agent registry có số liệu đo thật; chủ dự án đã trả lời các câu hỏi Q-01…Q-09 có ảnh hưởng tới M1.

## M1 – Kiến trúc và hợp đồng

L4–L5, Opus làm, có reviewer độc lập.

- ADR: mô hình thế giới và hiển thị (Bot dùng chung, người chơi ẩn nhau), kiến trúc server, ngôn ngữ và thư viện server, giao thức mạng, mô hình lưu trữ MySQL, chiến lược branch.
- Tài liệu 02–11 ở mức đủ để chia việc.
- Hợp đồng: định dạng gói tin, schema lõi, interface giữa các module.
- Bộ khung repo, CI build và test tối thiểu.
- Chiến lược kiểm thử, gồm cách test Bot bằng mô phỏng không cần client.

**Thoát:** ADR nền tảng được chấp nhận; quyết định chạm định hướng game đã được chủ dự án duyệt; một worker mới đọc tài liệu là viết được module theo hợp đồng.

## M2 – Lát cắt dọc đầu tiên

Đăng nhập → tạo nhân vật → vào một bản đồ → di chuyển, với client Axmol Windows, server x64, MySQL.

- Gateway, session, tài khoản, lưu nhân vật.
- Client: tải bản đồ, hiển thị nhân vật, di chuyển, đồng bộ vị trí.
- Asset pipeline tối thiểu cho một bản đồ và một nhân vật.
- Build thử Android (và iOS nếu có máy Mac) ở mức chạy được, để lộ sớm vấn đề nền tảng.

**Thoát:** thao tác được từ đầu đến cuối trên máy thật, có integration test tự động cho luồng đăng nhập và di chuyển.

## M3 – Chiến đấu lõi

- Quái và NPC, sinh và hồi sinh.
- Combat, skill, trạng thái, hồi máu.
- Vật phẩm rơi, túi đồ, trang bị cơ bản.

**Thoát:** nhân vật săn quái, lên cấp, nhặt và mặc đồ; công thức chiến đấu có unit test.

## M4 – Bot System v1

Thiết kế L5, triển khai L3–L4.

- Bot là thực thể phía server dùng chung đường mã với nhân vật người chơi ở mức có thể.
- Scheduler và quản lý dân số theo bản đồ.
- Hành vi: di chuyển, săn quái, dùng skill, hồi máu, chuyển bản đồ.
- Tiến trình, túi đồ, lưu trữ Bot.
- Đồng bộ: hai client khác nhau thấy cùng một Bot ở cùng trạng thái.
- Mô phỏng tải: N Bot không cần client.

**Thoát:** Bot sống qua lần khởi động lại server với đúng trạng thái; test nhất quán giữa hai client qua; đo được chi phí CPU và bộ nhớ mỗi Bot, so với chỉ tiêu Q-05.

## M5 – Tiến trình và nhiệm vụ

- Hệ thống nhiệm vụ, Bot làm nhiệm vụ.
- Hoàn thiện kỹ năng, trang bị, tiến trình nhân vật.
- UI framework và các màn hình chính.
- Âm thanh và hiệu ứng.

**Thoát:** vòng chơi đơn hoàn chỉnh từ cấp thấp tới một mốc cấp do Opus đặt.

## M6 – Instance, hiển thị và hoạt động nhiều người đầu tiên

- Visibility Rules, Instance Management, Matchmaking, Event Capacity, Party và Team.
- Tống Kim làm hoạt động mẫu: người thật thấy nhau, có giới hạn, Bot tham gia theo Q-01.
- Khung Activity dùng chung: lịch, đăng ký, phần thưởng.

**Thoát:** test tự động chứng minh người chơi không thấy nhau ở khu vực thường và thấy nhau trong Tống Kim; giới hạn sức chứa được thực thi phía server.

## M7 – Các hoạt động còn lại

Mỗi hoạt động một module trên khung của M6. Phần này song song hóa tốt, phù hợp nhiều worker L2–L3. Thứ tự do Opus và chủ dự án chọn: Dã Tẩu, Boss Sát Thủ, Hoàng Kim, Nhiệm Vụ Hoàng Kim, Câu cá, Vận tiêu, Hạt Huy Hoàng, Thuyền Phong Lăng Độ, Vượt Ải, Liên Đấu, Hoa Đăng.

**Thoát theo từng hoạt động:** luật chơi có tài liệu, integration test, Bot tham gia đúng thiết kế.

## M8 – Quản trị và vận hành

- Web Admin, Mobile Admin.
- Logging, monitoring, cảnh báo.
- Triển khai, sao lưu, khôi phục.
- Bản phát hành Android, iOS, Windows.

**Thoát:** dựng lại được môi trường từ đầu theo tài liệu; khôi phục database từ bản sao lưu đã được thử.

## M9 – Gia cố

- Test tải theo chỉ tiêu Q-05, tối ưu bộ nhớ, Auto Batch.
- Rà soát bảo mật: xác thực, chống gian lận, quyền admin.
- Chạy dài ngày để tìm rò rỉ và lệch trạng thái Bot.

**Thoát:** đạt chỉ tiêu hiệu năng đã thống nhất; không còn lỗi mức nghiêm trọng mở.

---

## Phụ thuộc chính

```
M0 → M1 → M2 → M3 → M4 → M5
                    └──→ M6 → M7
M2 ───────────────────────────→ M8 (bắt đầu sớm phần logging, deploy)
M4, M6 ───────────────────────→ M9
```

Chạy song song an toàn: sau M1, phía client và phía server có thể tách worker vì đã có giao thức. Sau M6, các hoạt động tách worker. Trước M1 không nên mở nhiều worker viết code.

## Rủi ro ảnh hưởng lộ trình

- Tài khoản PM chỉ là bản dùng thử 7 ngày: M0 và M1 phải để lại tài liệu đủ cho PM khác tiếp quản.
- iOS cần phần cứng và tài khoản riêng.
- Chưa có chỉ tiêu quy mô: M4 và M9 không có đích đo.
- Nguồn tài nguyên hình ảnh chưa rõ: có thể chặn M2 trở đi.
