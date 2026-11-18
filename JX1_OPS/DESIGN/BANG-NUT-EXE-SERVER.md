# BẢNG NÚT EXE SERVER (đợt #157; cột "Đọc tĩnh" đã điền, cột "THỬ" còn trống)

Nguồn: `gateway/Sources/MultiServer/Goddess/{Goddess.rc,Goddess.cpp,IDBRoleServer.cpp}`, `Bishop/{Network.cpp,Application.cpp}` (đọc bằng GBK, không chạy exe). Nhãn [NGUỒN] = đọc thẳng từ mã; [GIẢ THUYẾT] = suy từ tên. Mã nguồn có thể không khớp exe đang chạy (chưa dựng lại từ nguồn).

## Goddess
| Nút / ô | Tác dụng (đọc tĩnh) | Rủi ro | Hoàn tác | THỬ |
|---|---|---|---|---|
| Start + Open port | mở cổng nghe, mặc định 5001 (`Goddess.cfg [Setting] Port`) [NGUỒN] | thấp | tắt exe | chưa |
| Max char create | số nhân vật tối đa/tài khoản → `MaxRoleCount` (mặc định 3), có hiệu lực sau khi tắt/bật [NGUỒN] | thấp | đặt lại giá trị cũ | chưa |
| Backup time | `BackupSleepTime` (mặc định 3); đơn vị chưa rõ [NGUỒN] | thấp | đặt lại | chưa |
| MAX Player | `MaxPlayerCount` (500); ô bị khóa (WS_DISABLED) trong .rc [NGUỒN] | thấp | — | chưa |
| Data type DB/SQL + Set up database | đặt `g_dataType` (`dataOpenModel` 0=DB, SQL) [NGUỒN] | CAO nếu đổi khi có dữ liệu | đặt lại, khôi phục bản sao | chưa |
| Copy DB to MySQL / Copy MySQL to DB | chép dữ liệu giữa hai kiểu lưu trữ [GIẢ THUYẾT, chưa đọc hàm] | CAO (ghi đè) | chỉ từ bản sao | chưa |
| Pause (backup) | tạm dừng/tiếp tục luồng sao lưu tự động (IDC_BTN_BACKUP_SUS_RES) [NGUỒN tên] | thấp-vừa | bấm lại | chưa |
| Manual backup | SQL: `copySqldataTobakSql()`; DB: `DoManualBackup()`, lỗi báo "Unable to start manual backup" [NGUỒN] | thấp (nên thử trước) | xóa tệp sao lưu sinh ra | chưa |
| Save nhat ky | `RemoveLogFiel()` = lưu trữ (archive) tệp nhật ký, báo "归档日志文件成功" [NGUỒN] | thấp | — | chưa |
| Restart | tắt luồng khách + đóng DB + mở lại DB + mở lại luồng khách [NGUỒN] | vừa: GS mất kết nối tạm | — | chưa |
| 合区 (Hợp khu) | gộp khu nguồn vào khu đích, có hậu tố tên và "Cap do loc" (lọc theo cấp) [NGUỒN StartMergeReg] | RẤT CAO | chỉ từ bản sao | chưa |
| 清除数据 + 区/全部 | xóa dữ liệu nhân vật của khu N, hoặc TẤT CẢ khu nếu đánh dấu "全部" [NGUỒN ClearRoleData] | RẤT CAO | từ bản sao | KHÔNG BẤM |
| 删除角色 | xóa MỘT nhân vật theo tên (`DelRoleData`) [NGUỒN] | cao | từ bản sao | chưa |
| 角色转区 | chuyển nhân vật sang khu khác [GIẢ THUYẾT] | cao | — | chưa |
| 开始删除 (theo tài khoản) | xóa nhân vật của một tài khoản [GIẢ THUYẾT] | cao | từ bản sao | chưa |
| 开始改名 | đổi tên nhân vật [GIẢ THUYẾT] | vừa | đổi lại | chưa |
| EnterMap/IDMap + "Bat dau" | `ChangeRoleInfo(tên, mã bản đồ)`: chỉnh bản đồ của nhân vật OFFLINE; lỗi "无此角色数据" [NGUỒN] | vừa (cứu nhân vật kẹt) | ghi lại bản đồ cũ | chưa |
| Add Money (Vang/Bac, Check online) | cộng vàng (0) hoặc bạc (1) cho nhân vật tên Role; "Check online" chọn online/offline [NGUỒN] | vừa | chưa có nút trừ | chưa |
| Remove Role + "Nhan vat level" | **XÓA HÀNG LOẠT mọi nhân vật có cấp nhỏ hơn N** khỏi DB, không hỏi lại (`MoveRoleLevel`, IDBRoleServer.cpp:1426-1455) [NGUỒN]. Nặng hơn "xóa một nhân vật" Chat đã ghi | RẤT CAO | từ bản sao | KHÔNG BẤM |
| Backup + hộp Body/Me chong/Kho/Box1-3/All | sao lưu từng phần đồ của một nhân vật (Account + Nhan vat) [GIẢ THUYẾT] | thấp | xóa tệp | chưa |
| 找回BAK (khung phải, ngoài vùng ảnh) | tìm/khôi phục nhân vật từ tệp bak: 选, 查找, 恢复, 恢复全部数据 [NGUỒN .rc] | RẤT CAO | — | KHÔNG BẤM |
| 临时修复技能 | `ClearRoleSkillData` cho từng tên trong danh sách (nút + / -) [NGUỒN] | vừa | — | chưa |
| Close | thoát Goddess | vừa | bật lại | không bấm |

## Bishop
Cấu hình `Bishop.cfg [Network]`: `RoleSvrIP/Port` (Goddess), `AccSvrIP/Port` (PaySys), `ClientOpenPort`, `GameSvrOpenPort`, `TwoRevivePos`, `bsMaxPlayerCount`, `ForBitOpenCount` (giới hạn mở nhiều cửa), `BishopVer` [NGUỒN Network.cpp]. Danh sách tài khoản/IP lưu ở `acclist_vip.cfg`, `accforbitlist.cfg`, `ipforbitlist.cfg` [NGUỒN]; nạp bản đồ từ `maps\WorldSet_<gs>.ini` (GameServer.cpp:489); tin hệ thống `Settings\msg\systemmsg.ini`.

| Nút / ô | Tác dụng | Rủi ro | Hoàn tác | THỬ |
|---|---|---|---|---|
| Announcer (Notify all player) | gửi một câu tới mọi người chơi [GIẢ THUYẾT từ ảnh] | thấp | — | chưa (bước thử đầu) |
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
