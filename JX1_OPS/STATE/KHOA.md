# KHÓA VÙNG FILE VÀ TÀI NGUYÊN

Sonnet ghi khi giao việc, xóa khi task xong hoặc dừng. Trước khi giao task mới, so với bảng này (quy tắc mục 12.2). Hai task chồng vùng file hoặc cùng tài nguyên thì không chạy song song.

## Vùng luôn tuần tự (mỗi lúc một task)
Giao thức gói tin; cấu trúc DB; hàm Lua dùng chung; lõi `KNpc`, `KPlayer`, `KSubWorld`, `KRegion`; cấu hình server.

## Đang giữ
| Task | Worker | Vùng file | Tài nguyên | Từ lúc | Commit gần nhất |
|---|---|---|---|---|---|
| 0-02b | sonnet | không | VM-Test-36 (đang chạy, Host-only, gs001 A2T2 lên; KHÔNG bật lại bridged) | 2026-11-16 18:30 | — |
| A-06 | codex (tách phiên, task JX-codex-A-06) | JX1_OPS/REPORTS/A-06-* | không | 2026-11-16 22:55 | — |
| A-05 | codex (tách phiên, task JX-codex-A-05) | JX1_OPS/REPORTS/A-05-* | không (đọc mã tĩnh) | 2026-11-16 23:19 | — |
