# LỊCH CÔNG VIỆC CHUNG A–B (Chat điều phối; 21/11 23:05, theo đề xuất A 23:05 và B 22:35; Q-106, Q-107)

## Bảng khóa tài nguyên dùng chung
| Tài nguyên | Đang giữ | Ghi chú |
|---|---|---|
| gs001 Test-36 (restart/nạp) | B giữ (chỉ đọc); Enabled=0 | Không restart khi A online. Nạp bản mới cần Chat duyệt + không ai chơi |
| gs001 đăng nhập atestqhhai | A (LD) | A thoát khi Chat báo / khi xong chụp ảnh |
| LD emulator-5558 + APK vc37 | A | không ảnh hưởng B |
| Worktree D:\JX-wt\SC-006B | B | A không đụng |
| qh9A client / Lua trên VM | A | B không sửa; nạp nóng Lua do A |

## Giai đoạn 1 (bây giờ → vc37 nghiệm thu): CƯỜNG HÓA
| Ai | Việc | Chạm gs001? | Song song |
|---|---|---|---|
| A | vc37 UI cường hóa (a–f + HUD), thoát atest khi xong, ảnh e, retest #359 | có (đăng nhập) | ✔ với B-P0-0/P2 |
| B | P0-0 đọc nốt sổ tay còn thiếu + khối HIỂU GAME; viết bảng tra SearchID + Describe chỉ khi cần (SC-006B, KHÔNG nạp); tiểu yêu so 36Hz cũ | không | ✔ |
| Chat | duyệt ảnh vc37; báo chủ nghiệm thu; APK vc37 + ghi chú 3 dòng | | |
| Chủ | test cường hóa vc37 trên điện thoại | có | sau khi A thoát |

## Giai đoạn 2: PHI PHONG (chỉ sau khi chủ duyệt Cường hóa)
| Ai | Việc | Chạm gs001? |
|---|---|---|
| B | SC-006 server phi phong: 11 bộ theo giới (mantle.txt/GoldItem), nạp bản đúng, đo (khung giờ riêng, A không online) | có (nạp, restart) |
| A | client phi phong: tên cạnh nhân vật (PaintPifeng), nhãn [cấp N] (SO-TAY-NHAN-CAP), mojibake, tooltip; chạy sau khi B nạp xong hoặc song song nếu chỉ build APK | đăng nhập khi test |
| Chủ | test phi phong | |

## Việc nền / sau
- A: đo khung >40ms trên LD (#363) khi di map (15 phút, A tự lên giờ không đụng B).
- B: P2 sửa SearchID (bảng tra) trong SC-006B, nạp CHỈ khi Chat xếp giờ (không ai chơi), để bật lại lọc Bot; P1 đo gói tin chỉ khi giật quay lại; 36 Hz hoãn (Q-105).
- Dài hạn: BOT, thuê VPS (chủ duyệt), nâng hiệu ứng, gỡ hook test, Obj pool 29466/30000.
