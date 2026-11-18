# Kế hoạch tái hiện hiệu ứng vũ khí (W-02) — kết quả quan sát

Đợt #192, 18–19/11/2026. **Chỉ quan sát, không sửa mã.** Chạy trên Test-36 (`JX-Test-36`) với client trong LDPlayer `T36test` (bản A, qh9A). Server-D và Main VM không bị chạm. Mạng tạm đã gỡ, `online.lua` đã khôi phục (xem mục 5).

**TÓM TẮT 5 DÒNG**
1. [THẤY] Có đúng hiệu ứng W-01 mô tả: +6 ánh trắng mỏng dọc lưỡi, +12 ánh vàng kèm sét bám thân kiếm, +15 sét trắng-xanh dày hơn bao quanh lưỡi (ảnh trong `ANH/W02-*`).
2. [THẤY] Cấp phải **ép bằng cờ** `/sdcard/jxwglow_<N>`: vũ khí phát bằng Lua (`AddItem` + `SetItemEnChance`) vào túi và mặc được nhưng **không hiện glow** và tooltip không có "+N". Tức đường cấp thật (server → `nEnChance` ở client) chưa được tái hiện, chỉ tái hiện được phần vẽ.
3. [THẤY] Đang di chuyển ở +15, hình sét **đổi dạng từng khung** và có khung sét nằm lệch khỏi lưỡi kiếm (khi nhân vật đổi hướng, kiếm bị thân che) — phù hợp H4/H5 nhưng chưa đủ để kết luận.
4. [CHƯA KIỂM] Chưa quan sát được vung kiếm thật: ở khu thành không có mục tiêu; nút đánh khi không ở trạng thái chiến đấu làm nhân vật **ngồi** (khớp mô tả `mainSkillattack`). Chưa quay video, chỉ chụp liên tiếp (~mỗi 0,15–0,3 giây).
5. Cần tôi quyết định: không. Bước tiếp (tái hiện sai khung khi vung) cần một mục tiêu đánh được hoặc cách bật trạng thái chiến đấu trên Test-36.

## 1. Điều kiện thử
| Mục | Giá trị |
|---|---|
| Server | Test-36, `gs001` khởi động lại sau khi chèn `JXW02Give()` vào `online.lua` |
| Client | LDPlayer instance 1 `T36test`, APK qh9A đã cài sẵn; **SHA-256 đã kiểm 19/11: `8da22c0c…`, KHÁC qh9A `47eb28e3` (xem `HIEU-HIEU-UNG-VU-KHI.md`)** |
| Nhân vật | `T36nv1`, Kim, Nam, cấp 1, Ba Lăng Huyện |
| Vũ khí | 3 vũ khí phát lúc đăng nhập (đao, côn/trượng, thương) trong túi; chỉ mặc đao "Yêu Đao [cấp 1]" (đòi sức mạnh +20, vẫn mặc được) |
| Cờ | `/sdcard/jxtrace` có sẵn; `jxwglow_6`, `jxwglow_12`, `jxwglow_15` đặt lần lượt rồi xóa; `jxlayeroff`, `jxhide_*` không dùng |
| Cách chụp | `screencap` liên tiếp qua `ldconsole adb`, cắt quanh nhân vật, ghép thành bảng |

## 2. Bảng quan sát
| Cấp | Hành động | Hướng | Khung chụp | Thấy gì | Ảnh |
|---|---|---|---|---|---|
| (không ép, kiếm "+6" Lua) | đứng | xuống | 6 | không glow, không sét | `W02-p6-stand-sheet.png` |
| +6 (ép) | đứng | xuống | 6 | ánh trắng mỏng dọc lưỡi, vành chân sáng đổi giữa khung | `W02-f6-stand-sheet.png` |
| +12 (ép) | đứng | xuống | 4 | ánh vàng, sét trắng bám cả thân kiếm; hình sét khác nhau mỗi khung | `W02-f12-stand-sheet.png` |
| +12 (ép) | bấm nút đánh | — | 8 | nhân vật ngồi (không ở trạng thái chiến đấu), không có vung | `W02-f12-atk-sheet.png` |
| +15 (ép) | đứng | xuống | 4 | sét trắng-xanh bao quanh lưỡi, dày hơn +12 | `W02-f15-stand2-sheet.png` |
| +15 (ép) | di chuyển (đổi hướng) | nhiều | 8 | sét đổi dạng mỗi khung; khung 2 sét nằm ở thân/chân khi kiếm bị che | `W02-f15-move-sheet.png` |

Ngoài ra: `W02-bag2.png` (túi có 3 vũ khí), `W02-eq3.png` (tooltip: đao, sát thương 3–11, không có dòng cấp cường hóa).

## 3. Đối chiếu với W-01 (`HIEU-HIEU-UNG-VU-KHI.md`)
| Điều W-01 nói | Quan sát | Kết quả |
|---|---|---|
| Glow từ +6, trắng | thấy ánh trắng nhẹ ở +6 | khớp |
| +12–14 vàng và sét | thấy vàng + sét ở +12 | khớp |
| +15 xanh điện, sét mạnh hơn | thấy dày hơn, tông trắng-xanh | khớp |
| Sét theo đồng hồ tường, đổi mỗi 50 ms | hình sét khác nhau ở mọi khung liền kề, kể cả khi đứng yên | phù hợp H5 |
| Sét trong mask section trội; có thể lệch (H4) | khi di chuyển có khung sét nằm lệch khỏi lưỡi | phù hợp H4, chưa chắc |
| Ép cấp bằng `jxwglow_N` chỉ cần section vũ khí có ảnh | đúng, cần mặc vũ khí | khớp |

## 4. Điều chưa biết, bước tái hiện kế
- **Vì sao cấp Lua không tới được client:** `SetItemEnChance(idx, n, sync)` đã gọi với `sync=1`, nhưng tooltip không có "+N" và glow không hiện. Chưa biết do hàm chỉ sửa trường khác, thiếu bước đồng bộ, hay client đọc cấp từ chỗ khác. Cần đọc `ScriptFuns.cpp:10912` và đường `s2cSyncItem` trước khi nói "glow thật không hoạt động".
- **Vung kiếm:** cần mục tiêu đánh được (quái hoặc nhân vật khác) hoặc bật trạng thái chiến đấu; ở Ba Lăng Huyện đã biết không bật được khi đi bộ qua cổng (CLAUDE.md, "Điểm chưa rõ"). Thử sang bản đồ có quái trên Test-36.
- **Quay video:** chuỗi `screencap` chỉ ~3–7 khung/giây; nên dùng `screenrecord` rồi tách khung để đo chu kỳ 800 ms của H5.
- **Cả hai vũ khí còn lại** (côn, thương) chưa mặc, chưa chụp.
- Không có thay đổi mã nào; mọi giả thuyết H1–H5 vẫn [CHƯA KIỂM] về nguyên nhân.

## 5. Hoàn tác đã làm
| Việc | Trạng thái |
|---|---|
| Cờ `/sdcard/jxwglow_*` trong T36test | đã xóa (`jxtrace` có sẵn từ trước, giữ nguyên) |
| `iptables -t nat -F OUTPUT` trong T36test, tắt T36test | đã chạy; `ldconsole quit --index 1` |
| Forwarder phụ (PID 167564) | đã dừng; forwarder chính PID 21276 và CDN PID 11072 vẫn chạy |
| Luật tường lửa `JX1-AUTO-T36-56722-51189-host` trên Test-36 | đã xóa |
| `online.lua` trên Test-36 | khôi phục từ `online.lua.bak-w02` (4116 byte); `gs001` đang chạy vẫn giữ bản đã nạp tới lần khởi động lại sau |
| Vũ khí đã phát cho `T36nv1` | còn trong dữ liệu nhân vật trên Test-36 (Test-36 là máy thử, không phải Server-D) |
