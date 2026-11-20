# MỤC LỤC TRI THỨC JX1

Cập nhật: 20/11/2026. Đây là bản đồ tra cứu; mở sổ tay và báo cáo để lấy bằng chứng `file:dòng`. Độ chắc: **chắc** = đã đọc mã có dòng; **khảo sát tĩnh** = chỉ đọc tài liệu/mã, chưa chạy; **chưa kiểm** = chưa có bằng chứng triển khai/runtime.

| Chủ đề và câu hỏi người chơi tra ở đây | Nhánh HIEU-GAME | Sổ tay | REPORTS liên quan | Hàm chính / điểm vào | Độ chắc |
|---|---|---|---|---|---|
| Trang bị, cường hóa, ma pháp, độ bền: món đồ có điều kiện gì và cộng thuộc tính nào? | `01-trang-bi-cuong-hoa` | `HIEU-BANG-SORT-VA-ITEM`, `HIEU-CAP-CUONG-HOA-LUA`, `HIEU-CAP-CUONG-HOA-LUA-2`, `HIEU-DO-BEN-SUA-DO`, `HIEU-HIEU-UNG-VU-KHI`, `SO-TAY-GHEP-TACH-DO`, `SO-TAY-NGUA-PHI-PHONG`, `SO-TAY-THUOC-TINH-MA-PHAP`, `SO-TAY-TRANG-BI` | `H-01..H-08`, `A-17`, `H-04` | `KItemList::Equip/UnEquip`, `KItem::EnChance`, `ApplyMagicAttribToNPC` | khảo sát tĩnh |
| Nhân vật và thuộc tính: tạo nhân vật, nhập phái, lên cấp, PK và hồi sinh diễn ra thế nào? | `02-nhan-vat-thuoc-tinh` | `HIEU-CAP-KINH-NGHIEM`, `HIEU-MON-PHAI`, `HIEU-TAO-NHAN-VAT-MOI`, `SO-TAY-NHAN-VAT`, `SO-TAY-PK-CHET-HOI-SINH` | `A-08a`, `A-15a..c`, `HG-10`, `SO-01` | `KPlayer::LevelUp`, `KPlayerDBFuns`, `KPlayerFaction` | khảo sát tĩnh |
| Kỹ năng và chiến đấu: buff, sát thương, đội và Tống Kim được tính/đồng bộ ra sao? | `03-ky-nang-chien-dau` | `HIEU-BUFF-TRANG-THAI`, `HIEU-CONG-THUC-SAT-THUONG`, `HIEU-TRANG-THAI-CHIEN-DAU`, `SO-TAY-KY-NANG`, `SO-TAY-KY-NANG-CAP`, `SO-TAY-TO-DOI`, `SO-TAY-TONG-KIM-BANG-HOI` | `A-08a`, `A-15a..c`, `D-01`, `H-13` | `KNpc::AddState`, `KSkills`, `KPlayer::AddExp` | khảo sát tĩnh |
| Quái, NPC và bản đồ: map, trap, hội thoại, hồi sinh và rơi đồ nằm ở đâu? | `04-quai-npc-ban-do` | `HIEU-BAN-DO-TRAP`, `HIEU-NAP-VA-CHUYEN-BAN-DO`, `HIEU-QUAI-HOI-SINH-VAT-PHAM-ROI`, `SO-TAY-AI-QUAI`, `SO-TAY-HOP-THOAI-NPC`, `SO-TAY-QUAI-NPC-BAN-DO`, `SO-TAY-QUAI-VANG`, `SO-TAY-ROI-DO` | `I-03`, `I-04`, `I-05`, `K-02`, `HG-09`, `HG-12` | `KSubWorldSet`, `KSubWorld`, `KNpc::NewWorld`, `KNpc::Activate` | khảo sát tĩnh |
| Nhiệm vụ và kinh tế: task-value/Lua, cửa hàng, kho, giao dịch và lịch sự kiện chạy thế nào? | `05-nhiem-vu-kinh-te` | `HIEU-GIAO-DICH-KHO-DO`, `SO-TAY-CUA-HANG`, `SO-TAY-GIAO-DICH-KHO`, `SO-TAY-KINH-TE`, `SO-TAY-NHIEM-VU`, `SO-TAY-NHIEM-VU-LUA`, `SO-TAY-THOI-GIAN-SU-KIEN` | `I-02`, `I-07`, `I-08`, `D-01` | `KPlayerTask`, `ScriptFuns`, `KItemList` | khảo sát tĩnh |
| Mạng và gói tin: đăng nhập, chat, đồng bạn, relay và đồng bộ thế giới đi qua đâu? | `06-mang-goi-tin` | `HIEU-DANG-NHAP-VAO-GAME`, `SO-TAY-BAN-BE-ONLINE`, `SO-TAY-CHAT`, `SO-TAY-DONG-BAN`, `SO-TAY-GOI-TIN`, `SO-TAY-S3RELAY`, `SO-TAY-THONG-BAO-HE-THONG`, `SO-TAY-VONG-LAP-SERVER` | `A-01`, `A-02`, `A-06`, `A-09`, `K-01`, `N-06` | `KProtocolProcess`, `KSOServer`, `S3Relay::MainLoop` | khảo sát tĩnh |
| Server và lưu trữ: hồ sơ tài khoản/nhân vật và cấu hình GameServer đọc từ đâu? | `07-server-luu-tru` | `SO-TAY-GODDESS-LUU-NHAN-VAT`, `SO-TAY-TAI-KHOAN-PAYSYS`, `SO-TAY-TEP-CAU-HINH-GS` | `A-01`, `A-04`, `N-06` | `GamePlayer`, `KPlayerDBFuns`, `KFile` | khảo sát tĩnh; triển khai chưa kiểm |
| Giao diện và tài nguyên client: người chơi thấy gì và PAK/SPR được nạp thế nào? | `08-giao-dien` | `HIEU-GAME-CHO-NGUOI-KHONG-LAP-TRINH`, `SO-TAY-GIAO-DIEN`, `SO-TAY-TAI-NGUYEN-CLIENT` | `SO-01`, `SO-02`, `K-02` | `KGameWorld`, `KUi`, `KPakList`, `KNpcRes` | khảo sát tĩnh |
| Công cụ và GM: lệnh quản trị đi qua client/server nào, giới hạn gì? | `09-cong-cu-gm` | `HIEU-LENH-GM`, `SO-TAY-CHONG-GIAN-LAN` | `H-13`, `C-01`, `C-02`, `E-01` | `KProtocolProcess::ProcessGMCmd`, `KGMCommand`, `KJxAdm` | khảo sát tĩnh; không chạy lệnh |

## Bằng chứng và cách tra

- 52 sổ tay đã được chuyển từ `DESIGN/` vào `HIEU-GAME/`; ánh xạ đầy đủ ở `HIEU-GAME/README.md`.
- `MA-NGUON/*.md` là bản đồ định vị mã tự sinh; Graphify chỉ định vị, phải kiểm file thật và dòng trong sổ tay/báo cáo.
- Các báo cáo cũ về QA (minimap, NPC, kỹ năng cấp 200...) vẫn được tra theo các mục `REPORTS/` hiện hữu; không xem mục lục này là bằng chứng runtime.
