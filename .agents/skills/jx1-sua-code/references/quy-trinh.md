# Quy trình chi tiết + lệnh (dùng khi SKILL.md chưa đủ)

## Gốc mã và đồ thị
| Phần | Gốc đọc | Gốc sửa (worktree dự án) | Đồ thị |
|---|---|---|---|
| Server C++ gs001 | `D:\JX-build\src18` (đồ thị cũ) | `D:\JX-wt\QH-B035\server\jxOnline\gameserver\Sources` (nhánh qh-b035-b02c) | `...\QH-B035\...\Core\Src\graphify-out` (mới), src18 lệch số dòng |
| Client Cocos | `D:\JX-build\qh9A\Classes` | task chỉ định (bản sao của qh9A) | `D:\JX-build\qh9A\Classes\graphify-out` |
| Script Lua server | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\script` | bản sao trong worktree, A chép lên VM | không có đồ thị → `rg -n` |
| Dữ liệu item | `...\gs\Settings\item` (+ `004`) | không sửa trừ khi task nói | `JX1_OPS/DU-LIEU/VAT-PHAM/` |

Graphify: `D:\JX-tools\graphify-venv\Scripts\graphify.exe query "<câu>"` | `explain "<Hàm>()"` | `path "<A>" "<B>"`.
Làm mới đồ thị CHỈ khi task cho: `JX1_OPS/TOOLS/lam_moi_do_thi.ps1`.

## Mã hóa
Nguồn C++/Lua gốc là GBK. Đọc: `Get-Content -Encoding 936` hoặc python `open(p, encoding='gbk', errors='replace')`.
Ghi lại đúng GBK, không đổi CRLF. Chữ Việt trong Lua/ini của dự án có thể là TCVN3 — giữ nguyên mã của file.
Ghi trong báo cáo: chữ Hán gốc + pinyin + tiếng Việt.

## Build
- Server (VS2022 x64): `python A07b\build-check.py --checkpoint=checkpoint-qh-<mã>` trong
  `D:\JX-wt\QH-B035\server\jxOnline\gameserver\Sources`. Phải 5/5 dự án exit 0
  (LuaLibDll, Engine, Common, CoreServer, GameServer). Đầu ra `A07b\checkpoint-qh-<mã>\out\gs001.exe`.
  Lỗi `__asm` trong Common = sai cấu hình x64/nguồn sai gốc (đừng sửa Common).
- Client APK: `assembleDebug` theo `REPORTS/L-03-quy-trinh-dung-apk.md`; tăng versionCode;
  đầu ra ghi SHA256 + versionCode. Ký bằng khóa dự án đã có, không tạo khóa mới.
- Lua: không build; kiểm cú pháp bằng `luac -p` nếu có, nếu không thì đọc lại hàm đã sửa.

## Kiểm tĩnh trước khi giao
- `git diff --stat` chỉ gồm file trong vung_file.
- Mọi đường gọi tới hàm đã sửa (graphify `explain` hoặc `rg`) vẫn hợp lệ; nêu các caller.
- Nếu sửa công thức ở server: tìm bản sao ở client (và ngược lại) — ghi có/không.
