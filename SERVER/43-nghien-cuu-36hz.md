# 43 - Nghiên cứu các mục phụ thuộc nhịp cho 36 Hz (Phase 4, tĩnh)

**TÓM TẮT 5 DÒNG**
1. Số liệu kiểm kê giữ nguyên từ báo cáo 34 §5 (skills 1.721 dòng, missles 462 - 24% Speed lẻ, npcs 2.436 - 13% tốc độ lẻ, ~950 dòng Lua ×18, 16 trường giao thức).
2. Không sửa dữ liệu/Lua bằng tay: đề xuất "đơn vị 18 Hz ở biên" - server chạy 36 nhịp/giây nhưng mọi giá trị đọc từ bảng, Lua và gói tin vẫn ở đơn vị 18 Hz, quy đổi tại chỗ nạp/API.
3. Tốc độ lẻ giải bằng bộ cộng dồn nửa bước (mỗi nhịp đi speed/2, phần dư cộng sang nhịp sau) -> quãng đường sau mỗi 2 nhịp bằng đúng 18 Hz, không sai số tích lũy.
4. Giao thức không đổi -> client 18 Hz cũ vẫn chơi được; client chỉ hưởng lợi gói đồng bộ dày hơn; client 36 Hz là tùy chọn sau.
5. Tất cả là thiết kế, CHƯA cài, CHƯA chạy. A2 (báo cáo 39) đã dùng ms nên không phụ thuộc nhịp.

Cần tôi quyết định: không

## 1. Bốn nhóm giá trị theo nhịp và cách giữ thời gian thực
| Nhóm | Ví dụ | Cách ở 36 Hz |
|---|---|---|
| Số khung (thời lượng) | `WaitTime`, `TimePerCast`, `LifeTime`, `DmgInterval`, `StandFrame..DeathFrame`, `AttackSpeed/CastSpeed`, thời gian trạng thái | ×2 khi nạp bảng; khi gửi client/Lua trả về: ÷2 (luôn chẵn nên chính xác) |
| Tốc độ (đơn vị/nhịp) | `WalkSpeed`, `RunSpeed`, `Missle Speed`, `Zspeed` | Bộ cộng dồn: `acc += speed; step = acc >> 1; acc &= 1` -> 2 nhịp 36 Hz = 1 nhịp 18 Hz chính xác |
| Bộ đếm `% N` theo `m_nGameLoop` (19 chỗ) | hồi máu, AI, đồng bộ | N×2, hoặc dùng `m_nGameLoop>>1` (giữ nguyên lịch 18 Hz) |
| Mốc thời gian Lua/hẹn giờ | `AddTimer`, `SetFightState`, hệ số 18 trong 952 dòng | Quy đổi trong `ScriptFuns.cpp` (nhân 2 tham số khung khi vào, chia 2 khi trả) - không sửa file Lua |

Điểm cần kiểm từng chỗ (chưa làm): 113 dòng dùng `m_dwCurrentTime`, 87 dòng số 18 viết thẳng, mỗi chỗ phải được phân loại vào một trong 4 nhóm; chỗ nào nhầm sẽ làm hiệu ứng nhanh/chậm gấp đôi.

## 2. Giao thức (16 trường)
Giữ đơn vị 18 Hz trên dây: server chia 2 trước khi gửi (`nWaitTime`, thời gian trạng thái, khung thế giới), tốc độ gửi giá trị gốc. Client cũ không đổi. Đồng bộ vị trí có thể gửi mỗi 2 nhịp 36 Hz (= 18 lần/giây, gấp đôi hiện tại 9 lần/giây, xem đề xuất B báo cáo 34).

## 3. Rủi ro
- Mã nguồn lệch exe đang chạy (báo cáo 41): phải chạy bản 18 Hz tự dựng ổn định trên VM thử TRƯỚC, rồi mới đổi nhịp.
- Bỏ sót một chỗ quy đổi = lỗi gameplay khó thấy; cần bài kiểm thời gian thực (đo thời lượng chiêu/trạng thái/đạn trên server 18 vs 36).
- CPU server một luồng ×2 (chưa đo).
- Thứ tự sự kiện trong một nhịp 18 Hz có thể tách thành 2 nhịp 36 Hz -> va chạm đạn/sát thương có thể lệch 1 nhịp (27,8 ms). Cần thử.

## 4. Thứ tự đề xuất
1. Chạy bản 18 Hz + A2 trên VM thử, so với exe gốc (Phase 2 động).
2. Thêm hằng `LOGIC_FPS` và hàm quy đổi tập trung; vẫn đặt 18 -> build phải hành xử giống hệt.
3. Đặt 36, bật từng nhóm, đo thời lượng bằng log.
