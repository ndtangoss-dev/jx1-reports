# BẢNG NÚT EXE SERVER (đợt #157; cột "Đọc tĩnh" đã điền, cột "THỬ" còn trống)

Nguồn: `gateway/Sources/MultiServer/Goddess/{Goddess.rc,Goddess.cpp,IDBRoleServer.cpp}`, `Bishop/{Network.cpp,Application.cpp}` (đọc bằng GBK, không chạy exe). Nhãn [NGUỒN] = đọc thẳng từ mã; [GIẢ THUYẾT] = suy từ tên. Mã nguồn có thể không khớp exe đang chạy (chưa dựng lại từ nguồn).

## Goddess
| Nút / ô | Tác dụng (đọc tĩnh) | Rủi ro | Hoàn tác | THỬ |
|---|---|---|---|---|
| Start + Open port | mở cổng nghe, mặc định 5001 (`Goddess.cfg [Setting] Port`) [NGUỒN] | thấp | tắt exe | chưa |
| Max char create | số nhân vật tối đa/tài khoản → `MaxRoleCount` (mặc định 3), có hiệu lực sau khi tắt/bật [NGUỒN] | thấp | đặt lại giá trị cũ | ĐÃ THỬ 18/11 17:0x–17:12 (VM thử): đặt 3→4 (sửa byte, có sao lưu), dừng/khởi lại Goddess, `MaxRoleCount=4` đã ghi; tạo nhân vật thứ 4 CHƯA thử (cần client; testlocal đã đủ 3); đặt lại 3, khởi lại lúc 17:12, kiểm lại tệp = 3. Sau khởi lại Bishop mất nối Goddess: phải bấm Reconnect DB của Bishop (xem dòng dưới) |
| Backup time | `BackupSleepTime` (mặc định 3); đơn vị chưa rõ [NGUỒN] | thấp | đặt lại | chưa |
| MAX Player | `MaxPlayerCount` (500); ô bị khóa (WS_DISABLED) trong .rc [NGUỒN] | thấp | — | chưa |
| Data type DB/SQL + Set up database | đặt `g_dataType` (`dataOpenModel` 0=DB, SQL) [NGUỒN] | CAO nếu đổi khi có dữ liệu | đặt lại, khôi phục bản sao | chưa |
| Copy DB to MySQL / Copy MySQL to DB | chép dữ liệu giữa hai kiểu lưu trữ [GIẢ THUYẾT, chưa đọc hàm] | CAO (ghi đè) | chỉ từ bản sao | chưa |
| Pause (backup) | tạm dừng/tiếp tục luồng sao lưu tự động (IDC_BTN_BACKUP_SUS_RES) [NGUỒN tên] | thấp-vừa | bấm lại | chưa |
| Manual backup | SQL: `copySqldataTobakSql()`; DB: `DoManualBackup()`, lỗi báo "Unable to start manual backup" [NGUỒN] | thấp (nên thử trước) | xóa tệp sao lưu sinh ra | ĐÃ THỬ 17:07 và 17:17: tạo thư mục `gw\database\<ngày_giờ>\` gồm `.bak` + `.txt` (bảng tài khoản/nhân vật/cấp/bạc/vàng); không lỗi, không ngắt GS |
| Save nhat ky | `RemoveLogFiel()` = lưu trữ (archive) tệp nhật ký, báo "归档日志文件成功" [NGUỒN] | thấp | — | ĐÃ THỬ: bấm xong không lỗi, hộp báo thành công (chữ GBK vỡ); không ngắt GS |
| Restart | tắt luồng khách + đóng DB + mở lại DB + mở lại luồng khách [NGUỒN] | vừa: GS mất kết nối tạm | — | chưa |
| 合区 (Hợp khu) | gộp khu nguồn vào khu đích, có hậu tố tên và "Cap do loc" (lọc theo cấp) [NGUỒN StartMergeReg] | RẤT CAO | chỉ từ bản sao | chưa |
| 清除数据 + 区/全部 | xóa dữ liệu nhân vật của khu N, hoặc TẤT CẢ khu nếu đánh dấu "全部" [NGUỒN ClearRoleData] | RẤT CAO | từ bản sao | KHÔNG BẤM |
| 删除角色 | xóa MỘT nhân vật theo tên (`DelRoleData`) [NGUỒN] | cao | từ bản sao | chưa |
| 角色转区 | chuyển nhân vật sang khu khác [GIẢ THUYẾT] | cao | — | chưa |
| 开始删除 (theo tài khoản) | xóa nhân vật của một tài khoản [GIẢ THUYẾT] | cao | từ bản sao | chưa |
| 开始改名 | đổi tên nhân vật [GIẢ THUYẾT] | vừa | đổi lại | chưa |
| EnterMap/IDMap + "Bat dau" | `ChangeRoleInfo(tên, mã bản đồ)`: chỉnh bản đồ của nhân vật OFFLINE; lỗi "无此角色数据" [NGUỒN] | vừa (cứu nhân vật kẹt) | ghi lại bản đồ cũ | chưa |
| Add Money (Vang/Bac, Check online) | cộng vàng (0) hoặc bạc (1) cho nhân vật tên Role; "Check online" chọn online/offline [NGUỒN] | vừa | chưa có nút trừ | ĐÃ THỬ 18/11 17:17: Bac, Role=jxt36a (offline), 1000 → bạc 2409400 → 2410400 (+1000, đọc từ `.txt` Manual backup); hộp báo thành công. Ô Money là CỘNG thêm |
| Remove Role + "Nhan vat level" | **XÓA HÀNG LOẠT mọi nhân vật có cấp nhỏ hơn N** khỏi DB, không hỏi lại (`MoveRoleLevel`, IDBRoleServer.cpp:1426-1455) [NGUỒN]. Nặng hơn "xóa một nhân vật" Chat đã ghi | RẤT CAO | từ bản sao | KHÔNG BẤM |
| Backup + hộp Body/Me chong/Kho/Box1-3/All | sao lưu từng phần đồ của một nhân vật (Account + Nhan vat) [GIẢ THUYẾT] | thấp | xóa tệp | chưa |
| 找回BAK (khung phải, ngoài vùng ảnh) | tìm/khôi phục nhân vật từ tệp bak: 选, 查找, 恢复, 恢复全部数据 [NGUỒN .rc] | RẤT CAO | — | KHÔNG BẤM |
| 临时修复技能 | `ClearRoleSkillData` cho từng tên trong danh sách (nút + / -) [NGUỒN] | vừa | — | chưa |
| Close | thoát Goddess | vừa | bật lại | không bấm |

## Bishop
Cấu hình `Bishop.cfg [Network]`: `RoleSvrIP/Port` (Goddess), `AccSvrIP/Port` (PaySys), `ClientOpenPort`, `GameSvrOpenPort`, `TwoRevivePos`, `bsMaxPlayerCount`, `ForBitOpenCount` (giới hạn mở nhiều cửa), `BishopVer` [NGUỒN Network.cpp]. Danh sách tài khoản/IP lưu ở `acclist_vip.cfg`, `accforbitlist.cfg`, `ipforbitlist.cfg` [NGUỒN]; nạp bản đồ từ `maps\WorldSet_<gs>.ini` (GameServer.cpp:489); tin hệ thống `Settings\msg\systemmsg.ini`.

| Nút / ô | Tác dụng | Rủi ro | Hoàn tác | THỬ |
|---|---|---|---|---|
| Announcer (Notify all player) | gửi một câu tới mọi người chơi [GIẢ THUYẾT từ ảnh] | thấp | — | ĐÃ THỬ: "Notify all player" + 1 câu thử, bấm Send; không lỗi, gs001 vẫn chạy |
| Announcer kiểu * | báo GS tắt an toàn / đuổi người chơi [ảnh] | cao | — | KHÔNG BẤM |
| save setting | ghi `Bishop.cfg` [NGUỒN] | vừa | sao `Bishop.cfg.bak` trước | chưa |
| Add to filter list / VIP / Forbid | ghi 3 tệp `*.cfg` danh sách [NGUỒN] | vừa | xóa dòng | chưa |
| Birth role setting | giá trị khởi đầu nhân vật mới [GIẢ THUYẾT] | vừa | đặt lại | chưa |
| Exit | tắt Bishop | vừa | bật lại | không bấm |

## Kế hoạch thử (mục 6; chưa thử gì, chờ chủ duyệt từng bước)
1. (đọc) Bishop: chụp tab Information; cần chủ duyệt việc bấm tab.
2. Sao lưu `Goddess.cfg`, `Bishop.cfg`, 3 tệp `*.cfg` danh sách (copy trong VM thử).
3. Goddess "Manual backup", kiểm có tệp sinh ra. Hoàn tác: xóa tệp đó.
4. Bishop Announcer "Notify all player" 1 câu. Không cần hoàn tác.
5. Goddess "Save nhat ky" (thấp rủi ro).
6. Đổi Max char create 3→4 trên VM thử: tắt Goddess, đổi, bật lại, tạo nhân vật thử, trả về 3.
7. Add Money cho nhân vật TEST đã có, ghi trước/sau.
Không bấm: Remove Role, 清除数据, 合区, 恢复全部数据, Copy DB/MySQL, Exit, Close, Announcer kiểu *.
Người duyệt từng bước: chủ (qua Chat). VM: chỉ JX-Test-36.


### Phát hiện thêm (đợt #161, 18/11)
- "Information" của Bishop không phải tab: là nhãn tĩnh, bấm không đổi gì (ảnh `ANH/exe-server/4b-Bishop-sau-bam-Information.png`).
- Dừng/khởi lại Goddess làm Bishop mất kết nối DB (hộp "提示" lỗi kết nối): bấm **Reconnect DB** của Bishop (nút thứ hai trên hàng dưới của khung trái). Không bấm nhầm Reconnect Pay (đổi cổng PaySys). Sau đó gs001 tự nối lại ("Database server reconnect OK"), SvrFPS 18/18.
- `ipforbitlist.cfg` không tồn tại trên VM thử; đã sao `Goddess.cfg`, `Bishop.cfg`, `acclist_vip.cfg`, `accforbitlist.cfg` vào `C:\JX\bak-161\` trong VM thử.