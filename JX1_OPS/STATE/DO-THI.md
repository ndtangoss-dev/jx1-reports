# TRẠNG THÁI ĐỒ THỊ GRAPHIFY

Làm mới thủ công 17/11/2026 22:57 bằng `graphify update .` (AST, không LLM). Lần sau dùng `TOOLS/lam_moi_do_thi.ps1` (ghi đè file này).

| Gốc | Đường dẫn | Đồ thị lúc | Ghi chú |
|---|---|---|---|
| client bản A | D:\JX-build\qh9A\Classes | 17/11 22:56 | Trước đó đồ thị trỏ nhầm D:\Android\b\Client\Classes (cũ, 16/11 21:41); nay `scan_root` = qh9A (kiểm bằng `graphify explain "jxDrawBolts"` ra `gamescene/KgameWorld.h L114`). Nhiều file nguồn GBK, đọc cp1252: tên tiếng Trung trong đồ thị có thể sai. |
| server src18 | D:\JX-build\src18 | 16/11 21:39 | `update` báo không file nào đổi (2457 file quét) nên không dựng lại; đồ thị còn đúng. 1472 file không có bộ trích xuất bị bỏ qua. |

Hook SessionStart/PreToolUse của Graphify đã có trong `C:\Jx1CocoV3\.claude\settings.json` (đường dẫn `D:/JX-tools/graphify-venv/Scripts/graphify.exe`). Qh9A không phải kho git nên không dùng git hook; làm mới bằng script trên.
