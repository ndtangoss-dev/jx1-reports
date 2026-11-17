# KHÓA VÙNG FILE VÀ TÀI NGUYÊN

Sonnet ghi khi giao việc, xóa khi task xong hoặc dừng. Trước khi giao task mới, so với bảng này (quy tắc mục 12.2). Hai task chồng vùng file hoặc cùng tài nguyên thì không chạy song song.

## Vùng luôn tuần tự (mỗi lúc một task)
Giao thức gói tin; cấu trúc DB; hàm Lua dùng chung; lõi `KNpc`, `KPlayer`, `KSubWorld`, `KRegion`; cấu hình server.

## Đang giữ
| Task | Worker | Vùng file | Tài nguyên | Từ lúc | Commit gần nhất |
|---|---|---|---|---|---|
| 0-02b | sonnet | không | VM-Test-36 (đang chạy, Host-only, gs001 A2T2 lên; KHÔNG bật lại bridged) | 2026-11-16 18:30 | — |
| U-01 | codex | DESIGN/HIEU-GAME-*, DESIGN/QUY-LUAT-VE-BO-PHAN.md, REPORTS/U-01.md (chỉ đọc source) | không | 2026-11-17 | đang chạy (JX-codex-U-01) |
| U-02 | codex | DESIGN/TRUYEN-TAI-VA-EXE-SERVER.md, REPORTS/U-02.md (chỉ đọc source) | không | 2026-11-17 | — (chưa chạy) |
