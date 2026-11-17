# B-02c - build và thử Enabled=0 trên VM thử

## TÓM TẮT 5 DÒNG
1. B-02c (REMOVE an toàn, dọn m_VisibleNpcs, P2 chặn nhắm/skill/AoE người thật) do Codex viết, commit 026c628 nhánh `feature/visibility-c` (jx1-source worktree D:\JX-wt\B-02c); PM dựng bằng build-check (checkpoint-b02c) exit 0, cả 5 project.
2. Defender trong VM thử: không phát hiện mối đe dọa (4 file); Defender trên máy thật lỗi WMI/0x80004005, chưa quét ở đó.
3. Đã đưa lên VM thử JX-Test-36 (bản trước lưu `*.b02b`), gs001 chạy, nghe 51189, Bishop 56722 còn, sống ≥207 s với Enabled=0 (mặc định, không có visibility.ini).
4. SHA-256 (đầu 16): gs001_nohe 3211C8F37F122160, CoreServer 886962168A3DBADA, Engine C9B6C200CA49CC89, LuaLibDll 7D8F2F200F548705; HEVA tắt bằng editbin.
5. CHƯA KIỂM: Enabled=0 giống hệt gốc (so gói/ảnh), Enabled=1 Solo, tick/băng thông 100 bot + 20 người (điều kiện O-01); chưa gộp nhánh, chờ Chat duyệt.
