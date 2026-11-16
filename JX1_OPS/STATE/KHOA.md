# KHÓA VÙNG FILE VÀ TÀI NGUYÊN

Sonnet ghi khi giao việc, xóa khi task xong hoặc dừng. Trước khi giao task mới, so với bảng này (quy tắc mục 12.2). Hai task chồng vùng file hoặc cùng tài nguyên thì không chạy song song.

## Vùng luôn tuần tự (mỗi lúc một task)
Giao thức gói tin; cấu trúc DB; hàm Lua dùng chung; lõi `KNpc`, `KPlayer`, `KSubWorld`, `KRegion`; cấu hình server.

## Đang giữ
| Task | Worker | Vùng file | Tài nguyên | Từ lúc | Commit gần nhất |
|---|---|---|---|---|---|
| 0-02b | sonnet | không | VM-Test-36 (đang chạy, Host-only, gs001 A2T2 lên; KHÔNG bật lại bridged) | 2026-11-16 18:30 | — |
| E-01 | codex (tách phiên, task JX-codex-E-01) | JX1_OPS/BOT/, REPORTS/E-01-* | không | 2026-11-17 00:30 | — |
| D-01 | codex (JX-codex-D-01) | JX1_OPS/REPORTS/D-01-* | không | 2026-11-17 00:45 | — |
| C-01 | codex (JX-codex-C-01) | JX1_OPS/TOOLS/jxadm/, REPORTS/C-01-* | không | 2026-11-17 00:45 | — |
