# 47 - Xac minh P47 (rut gon theo yeu cau chu may)
Model QA: Sonnet 5.5. Cua so do: LDPlayer, FPS game 90, Ba Lang Huyen, cuoi ngua.

## Pham vi thuc te
- 1 doan ~70 s cuoi ngua chay xa (190/185 -> 165/200) + 6 lan doi huong; log cat theo epoch (khong dung video cho gap/regswitch).
- Cua so phu 81 s (log) co 1 lan chay bi chong cheo voi 1 tac vu cu; so lieu tuong tu.
- Khong do di bo (bo qua theo yeu cau rut gon).

## So sanh TRUOC (P47-diag) / SAU (P47)
| Tieu chi | Truoc | Sau (70 s / 81 s) | Ket luan |
|---|---|---|---|
| Doi vung | 22/30 s | 34 / 70 s; 61 / 81 s | tuong duong |
| Khoang trong clear->dung lai | 9 lan 45-68 ms | tb 0.1-0.3 ms, max 1.6 ms | PASS |
| Khung rto=0 / bio=0 | 18-23 | 0 | PASS |
| regswitch ok=0 | - | 0/34, 0/61; wait max 1 us; prep tb 68-186 us, max 150-866 us | PASS |
| Sawtooth (ti le / bien thien) | - | 1.00 / 0.08 (<=0.15) | PASS |
| ftime p50/p95/p99 | - | 16.5 / 20.3 / 24.7 ms (4251 khung); >33ms: 9; >=100ms: 1 (max 298 ms) | PASS co luu y |
| FPS thuc (JXPERF sum) | - | tb 59.9, min 55.6 (tran 60 du dat 90) | do tren LDPlayer |
| Video OpenCV mat dong loat doi tuong | 6-8 su kien/20-30 s | 0 su kien (q47: 193 khung, duong vien 0.25-0.27, khong khung nao <75% trung vi) | PASS co han che |
| CPU / RAM (1 lan) | - | jxclient 32-42% CPU; PSS TOTAL 415-430 MB (tang nhe 415->430 MB trong luc chay, chua ket luan ro ro ri) | thong tin |
| Crash | - | khong (pid 18116 giu nguyen) | PASS |

## Gioi han / chua kiem tra
- screenrecord tren LDPlayer chi ra video ngan bat thuong (10 s va 3.2 s thay vi 70 s; lap lai 2 lan). OpenCV chi phu ~3 s dau doan q47 va 10 s doan truoc do, KHONG phu toan bo 70 s. Bang chung chinh la log (gap_an, rto/bio), da phu toan cua so.
- 1 khung ~100 ms va max 298 ms trong ftime: chua doi chieu nguyen nhan (nghi nap tai nguyen luc doi vung hoac ADB input); cac khung nay khong rto/bio = 0.
- Hoi quy ra chieu: nhan 5 lan nut chinh 830,465 khi dang cuoi ngua gan quai Kim Mieu; missile_an = 0 ban ghi M (chua kich hoat ra chieu, co the do dang cuoi ngua / ngoai tam). KHONG khang dinh duoc hoi quy dan; khong crash. Can thu ra chieu xuong ngua.
- Hien thi NPC/quai/cay: 2 anh (q2/q3) thay quai, huou, cay, thung hang binh thuong, khong trung lap ro.
- Di bo xuong ngua, LDPlayer khac dien thoai: chua do.

## Ket luan
Sua loi nhap nhay khi doi vung: PASS tren cac tieu chi do duoc (khoang trong ~0 ms, 0 khung rong, regswitch on dinh, sawtooth 1.00). Hai muc chua dat bang chung day du: video toan phan va hoi quy ra chieu.
Can tôi quyet dinh: khong
