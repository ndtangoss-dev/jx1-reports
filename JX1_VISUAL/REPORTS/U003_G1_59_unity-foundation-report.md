# U003 G1 – Báo cáo nền tảng Unity (nhiệm vụ 59)

**Trạng thái G1: PARTIAL.** Phần chạy được và đã kiểm chứng: dựng project, pipeline SPR (kể cả TYPE_FRAME), map 45, ani001, nhân vật 8 hướng, che khuất tạm bằng Y-sort. **KIpoTree CHƯA port** (xem mục 6). Không gộp các mức: code đã viết ✔ · project mở/biên dịch được ✔ · build Windows ✔ · chạy bản Windows ✔ · build APK ✔ (xem báo cáo 60) · APK cài/chạy ✘ · thiết bị thật ✘.

## 1. Mục tiêu
G1.1–G1.5 của `U003_G1_G2_59_unity-build-first-apk.md`: kiểm môi trường, project độc lập, pipeline asset, animation, map/render.

## 2. Đã làm (file/thư mục)
- **Môi trường (G1.1):** Unity 6000.2.14f1 có sẵn, module Android (SDK/NDK/OpenJDK kèm theo) và Windows standalone có sẵn; không cài gì mới. Ổ D còn >1,3 TB. Không có GPU/RAM đọc được qua WMI (máy lỗi WMI) – chưa đo.
- **Project:** `D:\JX1_U003` (ngoài `D:\JX1_U003_work`), chỉ module built-in, không thêm package. Không đụng U001/U002, PAK, source, VM, server.
- **Pipeline asset (G1.3):** `Tools/export_spr.py`, `export_names.py`, `map_parse.py`, `build_data.py`, `char_sheet.py` (trong project, không đẩy lên repo công khai). Mỗi SPR → atlas PNG + JSON (W,H,Center,hướng,khung/hướng,interval, offset từng khung) kèm **nguồn gốc** (pak, entry id, đường dẫn). Atlas là dữ liệu dẫn xuất, tái tạo được từ PAK; PAK không nằm trong build.
- **TYPE_FRAME:** `export_spr.extract` triển khai theo `XPackFile::GetSprHeader/GetSprFrame` (`XPackFile.cpp:597-740`): entry SPR có cờ 0x10000000 và dữ liệu bắt đầu bằng `SPR\0` → header+palette thô, bảng (csize,lsize) mỗi khung, khung nén UCL riêng (lsize<0: lưu thô). Trước đó 2 ảnh `菩提树2/3.spr` lỗi `lookbehind overrun`; sau khi hỗ trợ: **35/35 ảnh map45 giải được**. `pak_extract.py` không bị sửa.
- **Asset đã xuất:** ani001 (st, wlk, bat, die, at), nhân vật 5 bộ phận × 6 hành động (thân/đầu/tóc/tay trái/tay phải; ST03, WK01, AT01, MG02, IJ01, DE01), đạn 181, cast kl_16, nổ Bz_dian3, đạn 193, icon 375, 35 ảnh map, font số `number_16_r`, joystick `yaoganz/x` (từ Resources client).
- **Dữ liệu runtime:** `map45.json` (96 vùng: ground/cover/buildin), `char_order.json`.
- **Code Unity** (`Assets/Scripts/Runtime`): `Core.cs` (Mps, Cfg, SprSheet), `MapView.cs`, `Actors.cs`, `Game.cs`, `Skill375.cs`, `GameUI.cs`, `AutoTest.cs`; `Editor/U003Editor.cs` (import atlas RGBA32 không nén; build Windows/Android).

## 3. Class/hàm chính
`Mps.ToWorld` (screen_x = mps_x, screen_y = mps_y/2 − z·887/1024, y Unity đảo dấu; 1 đơn vị = 1 px); `SprSheet.Load/Get` (anchor); `MapView.Build/UpdateVisible/OrderForY`; `Game` (vòng mô phỏng bước cố định 1/60 s, quái, người chơi, damage number); `Skill375`; `GameUI` (joystick/nút/overlay IMGUI).

## 4. Quyết định kỹ thuật
- **Anchor** theo `ccgetTxtData` (BC 58 mục E): Center header ≠ 0 → dùng Center; ngược lại rộng >160 → (160,192); ngược lại (0,0); offset khung cộng qua pivot. ani001 = (160,192) (đúng quyết định 16); đạn/hiệu ứng dùng Center của header (m181 = 196,345).
- **Ground** (BC 58 F2, `KScenePlaceRegionC.cpp:789-790`): vị trí `(h·32+left, v·32·2+top)` MPS, góc trái-trên; cover theo `bOrder/nLayer`; buildin vẽ tại `oPos1` tuyệt đối với anchor header.
- **Hướng sprite** 0..7 (S,SW,W,NW,N,NE,E,SE) theo bảng g05_dirmap, tính từ vector trên màn hình.
- **Thứ tự bộ phận nhân vật:** `男主角贴图顺序表` section DEFAULT, khoá Dir = 2·d+1 (**giả định**, chưa đối chiếu client gốc).
- **Vùng map:** x=96..107, y=95..102 (96/96 `Region_C.dat` có mặt); chỉ bật các vùng nằm trong khung nhìn (+320 px).

## 5. Phần nào theo gốc, phần nào là U003
Theo gốc/đã xác minh: pipeline SPR, anchor, công thức MPS, vị trí ground, hướng sprite, ani001 clip. Là lựa chọn U003/giả định: bộ trang bị nhân vật (thân 001, đầu 001, tay 001, **tóc `MA_HR_012`** vì `MA_HR_001` không có trong PAK – chưa xác minh ý nghĩa), tốc độ khung nhân vật, thời lượng clip ani001 lấy từ `interval` header (gốc không dùng interval cho NPC, BC 55/58), khung nhìn 540 px chiều cao.

## 6. Hoàn thành / chưa / lược giản
- ✔ Scene dựng được; nhân vật + ani001 hiển thị 8 hướng; map render; ảnh/log lưu cục bộ (`D:\JX1_U003_work\shots3`, không đẩy lên repo công khai vì chứa asset game).
- ✔ Quan sát: 8 quái ani001 quanh người chơi đều quay mặt vào người chơi ở cả 8 hướng ⇒ mapping hướng nhất quán.
- ✘ **KIpoTree chưa port.** Hiện dùng **Y-sort tạm** (`MapView.OrderForY`, bước 8 MPS) cho buildin/nhân vật/quái/đạn. Nhánh Tree/Line/Clone: **chưa chạy**. Rect 96 vùng này có 0 Tree/Line/Above, chỉ Point (352 đối tượng), nên chưa có dữ liệu thử Tree; cảnh tổng hợp có Tree **chưa tạo**. Quan sát: con hổ đi sau tượng ngựa được che đúng bằng Y-sort (không thay cho kiểm thử KIpoTree).
- ✘ Obstacle (ý nghĩa giá trị chưa rõ, BC 58) không dùng: nhân vật chỉ bị giới hạn trong hình chữ nhật chơi.
- ✘ Chưa đối chiếu ảnh client gốc (anchor, blend, thứ tự bộ phận); blend dùng alpha thường (HYPOTHESIS, BC 58).
- Lược giản: không có `pst`, không có ngựa/áo choàng/vũ khí; âm thanh không có.

## 7. Lệnh build/test và kết quả
- `Unity.exe -batchmode -nographics -createProject D:\JX1_U003` → OK.
- `-executeMethod U003Ed.U003Build.BuildWindows` → `Build Succeeded`, 0 lỗi (log `D:\JX1_U003_work\logs\build_win3.log`).
- Chạy `JX1_U003.exe -screen-width 960 -screen-height 540` với biến `U003_AUTOTEST` → ghi ảnh + `autotest_result.txt`, thoát mã 0.

## 8. Ảnh/log
Cục bộ: `D:\JX1_U003_work\shots3\g1_01_scene_player.png`, `g1_02_player_8dirs.png`, `g1_03_ani001_8dirs.png`; log `D:\JX1_U003_work\logs\`.

## 9. Lỗi gặp và cách sửa
1. `菩提树2/3.spr`: `lookbehind overrun` → hỗ trợ TYPE_FRAME (mục 2).
2. `MA_HR_001_*.spr` không có → chọn `MA_HR_012` (giả định, mục 5).
3. Kịch bản test lần đầu cast lúc auto còn bật → đặt auto tắt từ đầu; lần 2 quái đi khỏi ô mục tiêu nên 0 va chạm (đúng quy tắc đạn đứng yên) → cố định AI quái trong bài test skill.
4. Heredoc làm mất `\`/chèn NUL khi sửa file Python trong shell → dùng công cụ ghi file.

## 10. Hiệu năng
Bản Windows (cửa sổ 960×540): FPS đo trong test 52–60, GC ~6–7 MB. **Chưa đo trên Android.** 6.822 sprite ground/cover/object dựng một lần, bật/tắt theo vùng.

## 11. APK
Xem báo cáo 60.

## 12. Giới hạn/rủi ro
Thứ tự vẽ tạm; giả định thứ tự bộ phận; không có ảnh gốc để so; Hz client chưa biết (18 tick/s là lựa chọn prototype); chưa kiểm tra bộ nhớ/FPS thiết bị thật.

## 13. Bước tiếp theo
(1) Cài APK lên thiết bị/emulator, đo FPS. (2) Đọc `KIpotBranch/KIpoTree/KIpotLeaf` và các hàm `SM_*` còn UNKNOWN rồi port + cảnh Tree tổng hợp. (3) Đối chiếu ảnh client gốc.
