# PP-02 Chuẩn bị phi phong client (đọc tĩnh 22/11, chưa sửa theo CH-04)

- Vẽ: `KgameWorld::PaintPifeng(type, node, x, y)` (gamescene/KgameWorld.cpp:11189), gọi tại :9869 và :10765 với `Npc[i].m_PifengType`.
- Dữ liệu: `\Ui\npcbobo.ini` mục `[FortuneRank]`: `count` (mặc định 11), `nTime`, khóa `Spr_N` → tên spr. Loại > count bị kẹp về count.
- Đã có sửa [pfl] (chưa commit trong repo chính): đổi loại thì xóa sprite cũ (so userData), khóa Spr_N khớp KNpc.cpp:10815.
- Vị trí: setPositionX(-20) cố định, chưa tách theo giới/hướng.
- Việc còn lại sau khi chủ duyệt CH-04: bảng 11 bộ theo giới (cần SO-TAY-NHAN-CAP), offset theo hướng, kiểm spr tồn tại trong PAK.
Chưa kiểm: nội dung npcbobo.ini thực tế, hiển thị trên LD.
