# GS001 bản đồ nhanh (Chat, từ A-05/A-08/A-09/A-10/B-02). Dán đầu prompt Codex; KHÔNG sửa phần này giữa các lần giao để tận dụng cache.
Thư mục nguồn: S=server Core/Src, H=header, G=game data. Dòng là gần đúng, kiểm lại trước khi sửa.
- Phát sóng: KRegion.cpp:2223-2301 (BroadCast), KSubWorld.cpp:1784,2366-2394, KNpc.cpp:7718,7822,7961-8124,14993-15030, KNpcSet.cpp:1284-1290, KObj.cpp:1454-1621. MAX_BROADCAST_COUNT=100 (KRegion.h:15).
- Lọc hiển thị: KVisibility.cpp/.h (nhánh feature/visibility). Cấu hình Settings/visibility.ini.
- Đồng bạn: KNpcAI.cpp:3303-3446 (ProcessCompanion, chọn vai), KNpc.h:398 (m_TongBanNum), KItemList.cpp:1382-1394, KSkillList.cpp:64-111, KSkills.cpp:267-358, KMissle.cpp:1378.
- Kinh nghiệm: AddOwnExp (một người), AddExp(exp,level,1) chia đội cự ly 768; GetNextExp = ngưỡng cấp hiện tại; SetTimer(18,id)=1 giây.
- Boss xanh: GoldType 2-4 (KNpcGold.cpp:326-350); chết: KNpc::OnDeath (KNpc.cpp:2590-2668). Lửa trại: script huozhong.lua, gouhuo.lua; NPC 2078, skill 1705.
- Nhịp 18 Hz, một luồng, trần 500 người, MAX_NPC=100000. Build: v143 x64, KHÔNG dùng /RTC1; xem REPORTS/A-07e-rtc.md.
- Quy tắc: không đụng main, không đưa mã nguồn vào kho công khai.
