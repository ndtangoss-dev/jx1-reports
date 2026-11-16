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

## Chờ chủ dự án
Không còn mục chờ về mạng: máy thật đã có Host-only `192.168.56.101`, không cần đổi. Chủ dự án chỉ cần xác nhận đã đọc báo cáo mạng trong `ENVIRONMENT.md` trước khi tôi tiếp tục dùng VM thử.
