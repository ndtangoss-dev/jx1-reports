# QUYẾT ĐỊNH ĐÃ CHỐT

Chỉ ghi quyết định đã chốt. Muốn đổi thì thêm dòng mới, không sửa dòng cũ.

| # | Ngày | Quyết định | Ai chốt | Nguồn |
|---|---|---|---|---|
| Q-01 | 2026-11-16 | Thế giới Bot dùng chung: mọi người chơi thấy cùng một Bot; A giết Bot thì Bot chết với tất cả; trạng thái Bot quản lý tập trung | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/03`, `owner-inputs/05` |
| Q-02 | 2026-11-16 | Bỏ Secret Vault và bảo mật phức tạp | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/03` |
| Q-03 | 2026-11-16 | Dùng lại client và server JX1 gốc; bỏ hướng client Axmol mới và server mới | Chủ dự án | `owner-inputs/05` |
| Q-04 | 2026-11-16 | Người chơi thật không thấy nhau ở bản đồ thường; chỉ thấy nhau trong hoạt động được chủ dự án bật, có giới hạn số người | Chủ dự án | `owner-inputs/05` |
| Q-05 | 2026-11-16 | Opus lập kế hoạch; Sonnet là PM có toàn quyền; Fable kết thúc | Chủ dự án | `owner-inputs/05`, `06` |
| Q-06 | 2026-11-16 | Bỏ ChatGPT, 8 phòng ban, Dispatcher | Chủ dự án | `owner-inputs/06` |
| Q-07 | 2026-11-16 | Toàn bộ quy trình và tiến độ lưu trên một nhánh riêng (`jx1-ops`) | Chủ dự án | `owner-inputs/06` |
| Q-08 | 2026-11-16 | Thay AI, tài khoản, model bất cứ lúc nào không mất tiến độ | Chủ dự án | `FABLE_HANDOVER_v0.3/docs/owner-inputs/04` |
| Q-09 | 2026-11-16 | Bot chỉ triển khai sau khi mô hình server mới được thử nghiệm và kiểm chứng | Chủ dự án | `owner-inputs/05` |
| Q-10 | 2026-11-16 | **Đồng ý** đưa source (đã lọc dữ liệu tài khoản, không PAK, APK, exe) lên repository GitHub riêng tư `jx1-source` (D1) | Chủ dự án | Tin nhắn 16:41 |
| Q-11 | 2026-11-16 | **Bỏ hẳn AMOLX**, chỉ dùng client Cocos V3 (D2) | Chủ dự án | Tin nhắn 16:41 |
| Q-12 | 2026-11-16 | Codex CLI dùng model Sol Max qua xingchi, **không đổi model**; ngân sách khoảng 2.000 USD; được dùng nhiều worker Codex để đẩy nhanh tiến độ | Chủ dự án | Tin nhắn 16:41 |
| Q-13 | 2026-11-16 | D3: nền thử chuyển đổi là VM thử `JX-Test-36` với server tự dựng 36 Hz; Main VM không đụng | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-14 | 2026-11-16 | D4: giao hàng với mọi hoạt động tắt cho người thật thấy nhau; chủ dự án bật sau | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-15 | 2026-11-16 | D5: giữ kênh chat thế giới như game gốc ở bản đồ thường | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-16 | 2026-11-16 | D6: Sonnet dùng danh sách cho phép + danh sách cấm (`TOOLS/settings.mau.json`), không bỏ qua mọi hỏi đáp. Chủ dự án duyệt `KE-HOACH-TONG-THE.md`; Codex giữ nguyên model và cấu hình; PM tự động, báo một lần mỗi ngày | Chủ dự án (duyệt mặc định) | Tin nhắn giao PM |
| Q-17 | 2026-11-16 | **Không bật VM nào ở chế độ bridged (hoặc nối thẳng vào LAN nhà) khi chủ dự án chưa cho phép.** Thay Q-13 ở điểm "dùng bridged": `JX-Test-36` dùng Host-only. Lý do: mạng nhà (mesh) sập tối 16/11 sau khi bật VM thử, chưa xác định nguyên nhân | Chủ dự án | Tin nhắn tối 16/11 |
| Q-18 | 2026-11-16 | Quyền tự chủ với Main VM `JX-Server-D`. **Được tự làm, không hỏi:** bật headless khi đang tắt; xem trạng thái; kiểm tra Windows và chuỗi server game đã lên chưa (chỉ đọc); khởi động chuỗi server đúng thứ tự trong `KHOI_DONG_CHUOI_SERVER_D.md` nếu chưa lên. **Vẫn cấm nếu chưa nói rõ:** tắt, reset, sửa cấu hình VM, đổi mạng, chụp snapshot, xóa hay sửa dữ liệu, cài đặt, sửa file trong Main VM | Chủ dự án | Tin nhắn tối 16/11 |
| Q-19 | 2026-11-16 | (1) Chuỗi server game (PaySys, Goddess, S3Relay, Bishop, gs001 và exe server đi kèm đã biết): PM tự khởi động, dừng, khởi động lại trong `JX-Test-36` bất cứ lúc nào; trong Main VM chỉ khởi động theo Q-18; không cần hỏi. (2) Exe lạ, chưa từng chạy: chỉ chạy trong VM thử, sau khi lưu SHA-256 và quét Defender; không cần hỏi. (3) Vẫn cấm: chạy exe của gói game trên máy thật; chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe` ở bất kỳ đâu. (4) Quy định "mỗi exe server cần phê duyệt riêng" trong AGENTS.md cũ trên main hết hiệu lực (ghi rõ khi làm 0-06). (5) Ưu tiên script 0-07 khởi động chuỗi bằng một lệnh, không bấm nút Startup của Bishop bằng tay qua ảnh chụp | Chủ dự án | Tin nhắn tối 16/11 |
| Q-20 | 2026-11-16 | (1) Main VM: kiểm hồ sơ mạng trước; nếu bị đổi sang Public thì đổi lại Private; cổng đã mở thì không thêm luật. (2) Nếu cổng vẫn đóng: thêm luật tường lửa Inbound mở 5985, 1433, 5002 **chỉ cho IP máy thật 192.168.1.12**; ghi luật cũ và lệnh hoàn tác vào `ENVIRONMENT.md`; không mở cho cả mạng, không tắt tường lửa. (3) Từ giờ, câu hỏi nào đang chờ chủ dự án trả lời thì PM vẫn làm các việc khác trong backlog, không dừng lượt để chờ | Chủ dự án | Tin nhắn tối 16/11 |

## Chờ chủ dự án
Không còn mục chờ về mạng: máy thật đã có Host-only `192.168.56.101`, không cần đổi. Chủ dự án chỉ cần xác nhận đã đọc báo cáo mạng trong `ENVIRONMENT.md` trước khi tôi tiếp tục dùng VM thử.
