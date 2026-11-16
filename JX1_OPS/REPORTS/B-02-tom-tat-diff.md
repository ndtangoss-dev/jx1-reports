# B-02 - Tóm tắt diff để Chat duyệt (O-01)
Nhánh `feature/visibility` (jx1-source, 8ef7430), 14 file, +537/-5. Chỉ liệt kê điểm móc; không đưa mã đầy đủ vào kho công khai. Số dòng là của bản sau sửa.

## Công tắc Enabled=0
- `ViewerCanSee` (KVisibility.cpp:178): dòng đầu `if (!enabled || cls == visObject || cls == visOther) return true;`.
- Mỗi chỗ móc đều có cổng `VisibilityEnabled()`; khi tắt, đường cũ được gọi nguyên văn (`else g_pServer->PackDataToClient(...)`), không đổi gói tin.
- `enabled` đọc từ `Settings/visibility.ini` [General] Enabled, mặc định 0 khi thiếu file.

## Điểm móc P1 (lọc hiển thị)
| Điểm | Vị trí | Việc làm |
|---|---|---|
| KRegion::BroadCast | KRegion.cpp:2245-2248, 2296-2301 | `DescribeVisibilityPacket` phân loại gói; gói REMOVE xử lý riêng (`BroadcastVisibilityRemoval`); gửi từng viewer qua `PackVisibilityData` nếu bật, ngược lại `PackDataToClient` gốc |
| KSubWorld::BroadCasts | KSubWorld.cpp:2386-2394 | cùng mẫu, theo từng người chơi cùng bản đồ |
| KSubWorld::SendSyncData | KSubWorld.cpp:1784-1787 | thêm cổng kiểm trước khi gửi đồng bộ NPC |
| KNpc::SendSyncData | KNpc.cpp:7961, 8018, 8124 | ba nhánh gửi thẳng, kiểm `ViewerCanSee` |
| KNpcSet::SyncNpc | KNpcSet.cpp:1289-1290 | `if (VisibilityEnabled() && !VisibilityCanSync(viewer, npc)) return FALSE;` |
| KObj::SyncAdd | KObj.cpp:1454, 1471 | lọc đối tượng theo chủ sở hữu |
| KNpc::Remove | KNpc.cpp:10234 | dọn trạng thái "đã thấy" khi NPC bị xóa |

## Luật trong ViewerCanSee (KVisibility.cpp:178-197)
- Không phải người thật (NPC, quái) hoặc gói loại `visObject/visOther`: luôn thấy theo luật gốc.
- Gói REMOVE: chỉ gửi nếu viewer đã từng nhận ADD (`m_VisibleNpcs`), tránh "người ma".
- Hảo hữu (`m_nOwnerPlayer`): chỉ chủ hoặc cùng tổ đội thấy (có kiểm `m_dwID` chủ để tránh slot tái dùng).
- Bot (`m_bIsBot`) thấy bởi mọi người nếu `botsVisible`; chế độ Open như gốc; cùng tổ đội nếu `partyVisible`; chế độ Group chỉ khi cùng `m_nVisGroup` khác 0.
- Chưa cài trần `MaxVisible` trong lọc này (nhóm con do Lua gán), chưa có P2 (chặn tương tác).

## Khác
- Lua: 4 hàm mới trong ScriptFuns.cpp:25671-25725 (SetVisGroup, GetVisGroup, IsBotPlayer...), KPlayer.h thêm `m_nVisGroup`, `m_bIsBot`, `m_VisibleNpcs`.
- Đội: KPlayerTeam.cpp:500, 850, 885 gọi làm mới hiển thị khi tổ đội đổi.
- Build: gs001/CoreServer 0 lỗi (A-07b nền), CHƯA chạy. Sẽ rebase lên `fix/a07c-link` (A-07e) rồi build, sau khi Chat duyệt.
