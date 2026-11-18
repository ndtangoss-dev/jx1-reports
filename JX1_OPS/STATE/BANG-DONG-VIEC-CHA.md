# BẢNG ĐÓNG VIỆC CHA — kiểm nghiêm theo #211 (19/11/2026 03:55)

Quy tắc: ĐẠT = đúng như TIÊU ĐỀ NGUYÊN VĂN trong BACKLOG. "Offline" không thay "thật"; "PARTIAL" không thay "xong". Việc SO/HG/KC là sổ tay tài liệu: tiêu đề là "Sổ tay/Hiểu game: …", nên ĐẠT khi tệp đầu ra tồn tại, có TÓM TẮT 5 DÒNG, bằng chứng file:dòng và mục "Chưa kiểm" (kiểm bằng script, không đọc hết từng tệp). Các "PARTIAL" ghi trong tệp task của nhóm này chủ yếu do tệp nhịp `.nhip` ngoài vùng ghi, không phải thiếu nội dung.

| Việc | Tiêu đề nguyên văn (BACKLOG) | Bằng chứng | Kết luận | Ghi chú |
|---|---|---|---|---|
| C-03 | Trang quản trị web nội bộ, xem được trên điện thoại qua Tailscale | REPORTS/DONG-C03-E01.md | ĐẠT (giữ theo #211) | 6/6 test; bind 127.0.0.1; phần "xem trên điện thoại qua Tailscale" [CHƯA KIỂM] — việc riêng |
| E-01 | Client không giao diện Python: đăng nhập, vào game, đứng yên (bản sơ bộ dùng cho B-03). **Mốc đầu của Bot (Q-26): 1 Bot đăng nhập, đi, đánh; trần online ban đầu 100** | REPORTS/DONG-C03-E01.md | CHƯA ĐẠT → MỞ LẠI | tiêu đề đòi 1 Bot đăng nhập, đi, đánh trên server; mới 5/5 vé offline |
| P-02 | Bộ đo chuẩn một lệnh (tick, băng thông, khung hình) | TASKS/P-02.md | ĐẠT (giữ theo #211) | 12 test; đo thật trên Test-36 là việc riêng chưa làm |
| V-01 | Vòng tự động Chat⇄Sonnet (Q-48/Q-49) | REPORTS/V-01-dong.md | ĐẠT | vòng chạy được: VONG.md 42 CHAT-DAY / 23 SONNET-XONG, hook stop_guard |
| SO-04 | Sổ tay hiểu game: quái, NPC và bản đồ | TASKS/SO-04.md | CHƯA ĐẠT → MỞ LẠI | báo cáo thiếu mục "Chưa kiểm"; đã giao lại bổ sung |
| SO-05 | Sổ tay hiểu game: nhiệm vụ và Lua | TASKS/SO-05.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-06 | Sổ tay hiểu game: kinh tế (tiền, cửa hàng, rơi đồ) | TASKS/SO-06.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-02b | Hiểu game: trạng thái chiến đấu và nút đánh (lần 2, có nguồn tuyệt đối) | TASKS/HG-02b.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-05 | Hiểu game: gộp điều CHƯA KIỂM từ mọi báo cáo | DESIGN/DANH-SACH-CHUA-KIEM.md | ĐẠT | bảng DANH-SACH-CHUA-KIEM.md; HG-05b rà 174/174 báo cáo |
| KC-01 | Kiểm chéo chất lượng 5 báo cáo đã gộp | REPORTS/KIEM-CHEO-01.md | ĐẠT | 27 mệnh đề: 15 khớp, 4 sai, 2 thiếu mốc, 4 chỉ có tài liệu lịch sử, 2 chưa xác minh |
| KC-02 | Kiểm chéo chất lượng thêm 5 báo cáo khác | TASKS/KC-02.md | CHƯA ĐẠT → MỞ LẠI | báo cáo thiếu mục "Chưa kiểm"; đã giao lại bổ sung |
| SO-07 | Sổ tay hiểu game: Tống Kim, bang hội và hoạt động | TASKS/SO-07.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-08 | Sổ tay hiểu game: PK, chết, hồi sinh, hồi máu | TASKS/SO-08.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-09 | Sổ tay hiểu game: đồng bạn và thú cưỡi | TASKS/SO-09.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-10 | Sổ tay hiểu game: thời gian, lịch, sự kiện Lua | TASKS/SO-10.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-11 | Sổ tay hiểu game: giao diện client | TASKS/SO-11.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-12 | Sổ tay hiểu game: gói tin client–server | TASKS/SO-12.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-06 | Hiểu game: trạng thái, buff, thời gian hiệu lực | TASKS/HG-06.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-07 | Hiểu game: chợ, giao dịch, kho đồ | TASKS/HG-07.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-08 | Hiểu game: công thức sát thương | TASKS/HG-08.md | CHƯA ĐẠT → MỞ LẠI | báo cáo thiếu mục "Chưa kiểm"; đã giao lại bổ sung |
| HG-09 | Hiểu game: nạp và chuyển bản đồ | TASKS/HG-09.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-13 | Sổ tay hiểu game: tài khoản và thanh toán (PaySys) | TASKS/SO-13.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-14 | Sổ tay hiểu game: Goddess lưu nhân vật | TASKS/SO-14.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-15 | Sổ tay hiểu game: S3Relay | TASKS/SO-15.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-16 | Sổ tay hiểu game: tệp cấu hình gs/Settings | TASKS/SO-16.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-17 | Sổ tay hiểu game: tài nguyên client | REPORTS/SO-17.md | ĐẠT (tài liệu tĩnh) | phần PAK còn thiếu nguồn, đã ghi trong báo cáo |
| SO-18 | Sổ tay hiểu game: vòng lặp server | TASKS/SO-18.md | CHƯA ĐẠT → MỞ LẠI | báo cáo thiếu mục "Chưa kiểm"; đã giao lại bổ sung |
| HG-10 | Hiểu game: cấp, kinh nghiệm, điểm tiềm năng | TASKS/HG-10.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-11 | Hiểu game: môn phái và kỹ năng khởi đầu | TASKS/HG-11.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-12 | Hiểu game: quái hồi sinh và vật phẩm rơi | TASKS/HG-12.md | CHƯA ĐẠT → MỞ LẠI | báo cáo thiếu mục "Chưa kiểm"; đã giao lại bổ sung |
| HG-13 | Hiểu game: lệnh GM và công cụ quản trị | TASKS/HG-13.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-19 | Sổ tay hiểu game: hệ thống nhiệm vụ (task, Lua) | REPORTS/SO-19.md | ĐẠT (tài liệu tĩnh) | thiếu script gs\script để xác minh hai quest NPC cụ thể |
| SO-20 | Sổ tay hiểu game: cửa hàng NPC và giá | TASKS/SO-20.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-21 | Sổ tay hiểu game: tổ đội và chia kinh nghiệm/đồ | TASKS/SO-21.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-22 | Sổ tay hiểu game: kênh chat và tin nhắn | TASKS/SO-22.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-23 | Sổ tay hiểu game: ngựa, phi phong và đồ trang trí | TASKS/SO-23.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-24 | Sổ tay hiểu game: kỹ năng cấp, điểm kỹ năng và khí công | TASKS/SO-24.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| HG-15 | Hiểu game: bản đồ, cổng dịch chuyển và trap | TASKS/HG-15.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-25 | Sổ tay hiểu game: rơi đồ và tỉ lệ rơi của quái | TASKS/SO-25.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-26 | Sổ tay hiểu game: giao dịch giữa người chơi, kho và thư | TASKS/SO-26.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-27 | Sổ tay hiểu game: AI quái, tầm đánh và hồi sinh quái | TASKS/SO-27.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| SO-28 | Sổ tay hiểu game: bạn bè, danh sách đen và trạng thái online | TASKS/SO-28.md (vung_file) | ĐẠT (tài liệu tĩnh) | tệp đầu ra + TÓM TẮT + mục Chưa kiểm (script kiểm 03:50) |
| A-08a | Môn phái và kỹ năng (con của A-08; không vào mẫu số) | REPORTS/A-08a-mon-phai-ky-nang.md | ĐẠT khảo sát | bất nhất ID 1661/1702 ghi trong báo cáo |
| A-08b | Đồng bạn | REPORTS/A-08b-dong-ban.md | ĐẠT khảo sát |  |
| A-08c | Lửa trại và nướng cá | REPORTS/A-08c-lua-trai-nuong-ca.md | ĐẠT khảo sát | chưa chứng minh boss xanh sinh lửa/x2 party |
| A-08d | Kinh nghiệm | REPORTS/A-08d-kinh-nghiem.md | ĐẠT khảo sát |  |
| A-09 | Đồng bạn nhiều slot | REPORTS/A-09-dong-ban-nhieu-slot.md | ĐẠT khảo sát | có 5 dòng TÓM TẮT; tệp task còn ghi "(chưa làm)" — lỗi ghi chú |
| A-10 | Lửa trại từ boss tinh anh | REPORTS/A-10-lua-trai-boss.md | ĐẠT khảo sát | khảo sát tĩnh |
| A-12 | Khảo sát "hảo hữu mặc đồ" | REPORTS/A-12-hao-huu-mac-do.md | ĐẠT khảo sát | UI/DB chưa xác minh |
| E-01b | Bot - bộ tách bản ghi đồng bộ thế giới | REPORTS/E-01b-thieu-giao-thuc.md | ĐẠT offline | 41 test pass; server thật CHƯA KIỂM; không đủ để đóng E-01 |

## Việc cha KHÔNG đóng (còn active, nghiêm)

| Việc | Lý do | Bằng chứng |
|---|---|---|
| C-01 | tiêu đề liệt kê 8 chức năng gồm "sao lưu nhân vật"; chỉ đạt 22/22 test offline + CLI dry-run, adapter/khôi phục thật chưa kiểm | REPORTS/XD-C01.md |
| A-07 | CHƯA ĐẠT: thiếu dòng crash/dump/PDB đúng bộ | REPORTS/XD-A07.md |
| A-07b | CHƯA ĐẠT: còn chỗ ép hẹp con trỏ | REPORTS/XD-A07b.md |
| B-04 | CHƯA ĐẠT: thiếu 9 pha đo thật 100 bot + 20 người | REPORTS/XD-B04.md |
| E-05, E-09, M-01, O-01, A-07c, B-02, W-02, CL-01 | xem lý do trong REPORTS/XD-*.md và TASKS/*.md | — |

## Số liệu (03:51)

- SỐ THẬT (nghiêm): 74/101 = 73,3% (đã trừ E-01 và 5 việc thiếu mục Chưa kiểm, mở lại). Số bảng cũ trước #211: 79/101 = 78%.
- Mục tiêu: các việc mở lại là việc nhỏ, dự kiến xong trong ~30 phút; E-01 cần Test-36.

