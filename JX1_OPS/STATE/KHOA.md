# KHÓA VÙNG FILE VÀ TÀI NGUYÊN

Sonnet ghi khi giao việc, xóa khi task xong hoặc dừng. Trước khi giao task mới, so với bảng này (quy tắc mục 12.2). Hai task chồng vùng file hoặc cùng tài nguyên thì không chạy song song.

## Vùng luôn tuần tự (mỗi lúc một task)
Giao thức gói tin; cấu trúc DB; hàm Lua dùng chung; lõi `KNpc`, `KPlayer`, `KSubWorld`, `KRegion`; cấu hình server.

## Đang giữ
| Task | Worker | Vùng file | Tài nguyên | Từ lúc | Commit gần nhất |
|---|---|---|---|---|---|
| 0-02b | sonnet | không | VM-Test-36 (đang chạy, Host-only, gs001 A2T2 lên; KHÔNG bật lại bridged) | 2026-11-16 18:30 | — |
| U-01 | codex | DESIGN/HIEU-GAME-*, DESIGN/QUY-LUAT-VE-BO-PHAN.md, REPORTS/U-01.md (chỉ đọc source) | không | 2026-11-17 | đang chạy (JX-codex-U-01) |
| U-02 | codex | DESIGN/TRUYEN-TAI-VA-EXE-SERVER.md, REPORTS/U-02.md (chỉ đọc source) | không | 2026-11-17 | — đang chạy |
| U-03 | codex | DESIGN/BANG-THU-TU-VE.md, REPORTS/U-03.md (chỉ đọc source) | không | 2026-11-17 | đang chạy |
| R-01 | codex | REPORTS/A-01..A-07*, _CHIMUC/R-01.tsv | không | 2026-11-17 | — đang chạy |
| R-02 | codex | REPORTS/A-08..A-17*, AMOLX-DONG | không | 2026-11-17 | — đang chạy |
| R-03 | codex | REPORTS/B,C,D,F,G,K,O,P-* | không | 2026-11-17 | — đang chạy |
| R-04 | codex | REPORTS/E-* | không | 2026-11-17 | — chờ chạy |
| R-05 | codex | REPORTS/H-* | không | 2026-11-17 | — chờ chạy |
| R-06 | codex | REPORTS/I-*, J-* | không | 2026-11-17 | — chờ chạy |
| R-07 | codex | REPORTS/L,M,X,JIBS,TEST,daily | không | 2026-11-17 | — chờ chạy |
| S-01 | codex | DESIGN/BANG-KY-NANG-THEO-PHAI.md, REPORTS/S-01.md | không | 2026-11-17 | — đang chạy |
