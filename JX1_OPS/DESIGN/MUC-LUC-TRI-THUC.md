# MỤC LỤC TRI THỨC JX1 (tra ở đây trước, rồi mới mở báo cáo)

Cập nhật: 17/11/2026. Quy tắc: mỗi báo cáo mới phải có dòng "liên quan: ..." và được thêm vào bảng này khi gộp. Cột Độ chắc: **chắc** = đã đo/đọc mã có file:dòng; **giả thuyết** = chưa kiểm; **khảo sát tĩnh** = chỉ đọc, chưa chạy. Đây là tóm tắt định vị, mở báo cáo để lấy số liệu; không coi mục lục là bằng chứng.

| Chủ đề | Báo cáo / tài liệu | File, hàm chính | Độ chắc |
|---|---|---|---|
| Vẽ bộ phận nhân vật, thứ tự lớp | `DESIGN/QUY-LUAT-VE-BO-PHAN.md`, `BUGS/BUG-001.md`, J-04, H-04, L-01..L-03 | `KNpcResNode.cpp` (`GetkTable`, `GetSort`), `KNpcResVN.cpp::Draw`, ini `女主角贴图顺序表.ini` | bảng đứng yên **chắc**; bảng đi bộ/chạy **giả thuyết** |
| Animation nhân vật, quái, kỹ năng, cắt khung | J-01, J-02, J-03, J-05 | `KNpcRes*.cpp` | khảo sát tĩnh |
| Hiệu ứng vũ khí, glow, tia sét, mất khung | H-04, H-14, BUG-002 | `KNpcResVN.cpp` khối glow, `KgameWorld.cpp::jxDrawBolts` | glow **chắc**; lỗi khung nhảy **chưa tái hiện** |
| Làm mượt hình ảnh, nội suy, xBRZ, FPS | L-01, L-02, L-03, H-15, `DESIGN/TOI-UU-120FPS.md` | `JxPerf.h`, `KgameWorld.cpp` | đo trên LD; máy thật theo chủ |
| Trang bị, thuộc tính, cường hóa, ấn, tài phú | H-01, H-02, H-03, H-05, H-06, H-07, H-08 | `KItem.cpp`, `Core/Src` | khảo sát tĩnh |
| Phím tắt, nút, tự động chiến đấu | H-10, H-11, H-12 | `KgameWorld*.cpp` | khảo sát tĩnh |
| Tick, độ trễ đơn | H-13, B-04a | `Core/Src/KNpc.cpp`, vòng lặp gs001 | số đo có điều kiện, xem báo cáo |
| Điểm, tiền, cửa hàng, quái, bản đồ, NPC, nhiệm vụ | I-01..I-08, `DESIGN/THE-GIOI-TONG-QUAN.md` | script Lua `gs\script`, `Settings` | khảo sát tĩnh, độ phủ hữu hạn |
| Môn phái, kỹ năng, kinh nghiệm, rơi đồ, Tống Kim | A-08a..d, A-15a..c, A-16, A-17, A-10 | `Settings`, Lua | khảo sát tĩnh |
| Mạng, gói tin, tiến trình, đăng nhập | A-01, A-02, A-04, A-06, K-01 | `KProtocolDef.h`, `KProtocolProcess.cpp`, `Bishop`, `gs001` | khảo sát tĩnh |
| Crash, gốc lỗi gs001 | A-07, A-07b..e | `gs001` | xem từng báo cáo |
| Bạn bè, đồng bản, hoạt động | A-09, A-12, A-13, A-14, D-01 | `S3Relay`, Lua | khảo sát tĩnh |
| Bot, tester, điều phối | E-01..E-13b, B-02..B-03, C-01..C-03, JIBS, TESTER | `TOOLS/jxadm`, `jxweb` | xem từng báo cáo |
| Đồ thị Graphify, cách làm mới | `STATE/DO-THI.md`, `TOOLS/lam_moi_do_thi.ps1` | `D:JX-toolsgraphify-venv` | chắc |
| Công cụ, quy trình, môi trường | `QUY-TAC-VAN-HANH.md`, `TOOLS/CONG-CU.md`, `ENVIRONMENT.md`, `DESIGN/QUY-TRINH-SUA-LOI.md`, `DESIGN/HUONG-DAN-TRA-CUU.md` | | chắc |

## Báo cáo chờ tổng hợp
- U-01 (hiểu game cho người không lập trình) và U-02 (truyền tải, exe server): đang giao Codex; khi xong thêm dòng vào bảng trên.
