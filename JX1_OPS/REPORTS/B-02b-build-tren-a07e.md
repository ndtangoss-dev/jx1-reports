# B-02b - Dựng B-02 (lọc hiển thị) trên nền A-07e

## TÓM TẮT
1. Nhánh `feature/visibility` (đã rebase lên `fix/a07c-link`, c85cc1a) dựng thành công, 5 dự án exit 0 (LuaLibDll, Engine, Common, CoreServer, GameServer).
2. Codex bị 429 ba lần (04:59, 05:10, 05:34); lần 3 dừng sau khi xong Engine+LuaLibDll. PM tự dựng nốt CoreServer+GameServer (`--resume`).
3. Checkpoint: `D:\JX-wt\B-02\...\A07b\checkpoint-b02b-a07e\out` (không có /RTC1, theo A-07e).
4. SHA-256 (16 ký tự đầu): gs001.exe 65423806add0fc06, CoreServer.dll 188bf620dcce948c, Engine.dll e1845d868f946b6d, LuaLibDll.dll 829dcde95a288510. Chưa gỡ HEVA, chưa chạy, chưa quét Defender.
5. Chưa chạy trên VM: chờ Chat duyệt `B-02-tom-tat-diff.md` (O-01). Mặc định `Enabled=0`.

Cần tôi quyết định: không
