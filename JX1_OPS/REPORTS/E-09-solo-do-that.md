# E-09 — bộ lọc tầm nhìn Enabled=1 chế độ Solo, đo thật trên Test-36 (#216, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] Bật `gs\Settings\visibility.ini` (Enabled=1, BotsVisibleToAll=1, PartyMutualVisible=0; map không khai báo = Solo) trên Test-36, khởi động lại gs001 (08:16), chờ nạp xong (~08:25).
2. [ĐÃ KIỂM] Số bản ghi người chơi khác (S2C 74/75) một Bot nhận trong cửa sổ đo: Enabled=0 là 385 / 25 s (~616 quy đổi 40 s); Enabled=1 Solo là 116 / 40 s khi LD client `T36nv1` cùng online. Giảm ~81% nhưng KHÔNG về 0.
3. [ĐÃ KIỂM] Ảnh LD client (`JX1_OPS/ANH/t36-e09-solo-ld.png`): thấy NPC, không thấy nhân vật `BotLb02`; chat vẫn nhận "Công bố" khi Bot vào game.
4. [CHƯA KIỂM] Vì sao còn 116 bản ghi (map chưa khai báo có thật là Solo? bản ghi 74/75 gồm cả NPC-người?); chưa đối chiếu Group/Open. Nên E-09 CHƯA đóng.
5. Cần tôi quyết định: không.

Số đo: `python -I -X utf8 JX1_OPS/TOOLS/bench/contar_nguoi_choi.py 40` → `player_74_75 116 npc_77 1726`. Baseline Enabled=0: `player_74_75 385 npc_77 2900` (25 s). Một phiên đo mỗi chế độ, chưa lặp.
