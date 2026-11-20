---
name: jx1-sua-code
description: Sửa mã nguồn JX1 (server C++ gs001, client Cocos qh9A, script Lua) theo task Sonnet giao; tra kiến thức và đồ thị trước, sửa nhỏ có công tắc, build, rồi giao gói cho Sonnet A nạp và đo trong game. Dùng khi task có level sửa mã (agent: codex, loai: sua-code).
---
# Sửa mã JX1 (Codex làm, Sonnet chỉ đạo)

Vai: Codex ĐỌC + SỬA + BUILD + KIỂM TĨNH. Sonnet B viết task và duyệt diff; Sonnet A nạp lên Test-36,
đo trong game, nghiệm thu. Codex KHÔNG chạm VM/Test-36/LDPlayer/gs001 đang chạy, không phát APK.

## 7 bước (không bỏ bước; mỗi bước ghi một dòng vào báo cáo)
1. **Đọc task một lần**: mục tiêu, vung_file, quyền build, tiêu chí xong, KỊCH BẢN KIỂM ĐỘNG mà A sẽ chạy.
   Thiếu tiêu chí đo được (số trước → số sau) thì ghi BLOCKED, không đoán.
2. **Đọc kiến thức có sẵn** (≤ 3 file): `JX1_OPS/HIEU-GAME/README.md` → nhánh đúng chủ đề →
   hồ sơ tính năng `JX1_OPS/DESIGN/TINH-NANG/<TEN>.md` nếu task nêu. Ghi `ĐÃ ĐỌC KIẾN THỨC: ...`.
3. **Tra đồ thị trước khi mở mã**: `graphify query|explain|path` đúng gốc (bảng gốc ở
   `references/ban-do-ma.md`). Ghi `ĐÃ TRA ĐỒ THỊ: <lệnh> → <file:dòng>`. Đồ thị lệch/thiếu → `rg -n` giới hạn thư mục.
4. **Lần đủ chuỗi, không sửa giữa chuỗi khi chưa thấy hết**: nút/gói tin → server handler → Lua →
   C++ → đồng bộ về client → hiển thị. Cùng một công thức thường có BẢN SAO ở client (xem bẫy trong
   `references/ban-do-ma.md`). Viết chuỗi 5–10 dòng file:dòng vào báo cáo trước khi sửa.
5. **Sửa nhỏ nhất, đúng logic gốc**: sửa trong hàm gốc của game, không dựng đường song song.
   Có công tắc tắt/bật (biến/macro/ini) khi đụng C++. Giữ ý chú thích gốc (GBK). Chỉ sửa trong vung_file.
   Ưu tiên Lua (A nạp nóng bằng ReloadScript ~30 s) hơn C++ (phải thay exe/APK + restart ~10 phút).
6. **Build + kiểm tĩnh** (chỉ khi task cho build): lệnh build trong `references/quy-trinh.md`.
   Build phải exit 0 ở mọi dự án; ghi SHA256 đầu ra. Không chạy exe đã build.
7. **Giao gói** đúng mẫu `references/ban-giao.md`: patch, đường dẫn exe/APK/Lua + SHA256,
   cách hoàn tác, KỊCH BẢN KIỂM ĐỘNG cho A (thao tác + số kỳ vọng), DA XAC MINH / CHUA XAC MINH.

## Luật cứng
- "XONG" chỉ khi build sạch + diff đúng phạm vi; còn kết quả trong game luôn là CHƯA KIỂM cho tới khi A đo.
- Không bịa số dòng: mở file thật, đọc ≤ 400 dòng mỗi lần. Nguồn có thể KHÔNG khớp exe đang chạy — ghi rõ bản (worktree + commit).
- Tối đa 3 lần thử cùng một lỗi build; quá thì PARTIAL kèm log lỗi.
- Không sửa bản gốc/canonical; làm trong worktree task. Không commit/push nếu task không bảo (Tổng quản gộp).
- Không đụng tiền thật, tài khoản thật, Main VM, khóa/mật khẩu.
