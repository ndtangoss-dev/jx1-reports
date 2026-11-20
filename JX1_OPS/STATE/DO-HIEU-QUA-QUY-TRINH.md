# ĐO HIỆU QUẢ VÁ QUY TRÌNH (Q-99/Q-100) — Chat ghi, đại vương xem

## Mốc trước khi vá (06:59–11:52, 20/11) — đo từ kho
- Quyết định Chat ra: 12 (Q-88..Q-98b) trong ~5 giờ → đổi hướng lớn 4 lần (tài phú client → thuộc tính; vá tại chỗ → chuỗi gốc → nút mới).
- Thư Chat→A/B: ~20. Bản gs001 nạp hỏng/hoàn tác: 2 (B-040 sập, B-041 bỏ). Restart gs001: ≥4 (≈40–60 phút chờ).
- Tiêu chí cường hóa (Q-94) đạt bằng số thật: 0/8.
- Báo cáo có "ĐÃ TRA ĐỒ THỊ": 0. Dẫn sổ tay/MA-NGUON trong A-B.md: 0.
- Tiểu yêu chạy: 0 (5 khóa rảnh cả buổi).

## Chỉ số theo dõi sau vá (Chat cập nhật mỗi giờ)
| Giờ | Tiêu chí (c) đạt /8 | Bước hồ sơ ĐÃ KIỂM | Quyết định đổi hướng mới | Báo cáo có ĐÃ TRA ĐỒ THỊ / tổng | Báo cáo bị trả lại | DANG-LAM cập nhật (A/B) | Tiểu yêu chạy / KT xong | Restart gs001 |
|---|---|---|---|---|---|---|---|---|
| 12:10 | 0 | 0 | 0 | B: có (B-046) / A: chưa | 0 | chưa / chưa | 0 / 0 | 0 |
| 12:13 | 1 (TC1 nút mới mở UI Give gốc) | 2 (bước 1 nạp Lua, bước 3 nút mới+vc27) | 0 | A: ảnh có, chưa ghi dòng tra đồ thị / B: có | 0 | A có / B có (hook SessionStart+Graphify B đã kiểm) | 0 / 0 (9 KT ready, Tổng quản chưa giao) | 0 |

Nghiệm thu hình ảnh 12:13 (Chat xem ảnh DESIGN/ANH-NGHIEM-THU/q97-*):
- q97-nut-cuonghoa-moi-man-chinh: nút mới là ô vuông nhỏ biểu tượng lửa cạnh nút Auto (góc phải trên). ĐẠT chức năng; CHƯA ĐẠT dễ thấy: nhỏ, không có chữ "Cường hóa" như các nút bên cạnh (Xếp Hạng, Sơn Động, Auto) → yêu cầu thêm nhãn chữ cùng kiểu.
- q97-ui-giao-goc: cửa sổ "Giao" gốc mở cùng Hành Trang; lời nhắc gốc ghi "1 mảnh trang bị và 1 viên đá cường hóa" (không phải lời nhắc của B "đồ đang mặc hãy tháo ra") → client đang hiện mô tả cũ, cần sửa chữ theo luật ta (thủy tinh 3 loại).
- q97-giao-xac-nhan: thông báo lỗi gốc, chữ dịch tối nghĩa ("tảng đá phối hợp không đúng") → callback đang về sysError gốc, chưa tới Lua B (B đang tra).

| 12:27 | Cuong hoa: A van tra sysError Xac nhan, TC2-8 chua kiem. Tieu yeu: B bao 12:25 Tong quan da nhan KT-01/02/03A/03B (4 chay, 5 cho), da hon 0 luc 12:15. Chua co 'A Xong/A Chat' nao trong kho. |

## Q-102 (Codex sửa mã, B chỉ viết task) — số đo thật tới 21:35, 20/11 (B ghi theo #B-069)
Nguồn: git log kho, A-B.md, REPORTS/SC-001.md. Số token Codex: CHƯA ĐO (B không có số liệu token của Codex; cần Tổng quản/A gửi nếu muốn).

| Task | B giao (commit) | Kết quả / lúc | Thời gian tới kết quả | Lỗi/ghi chú |
|---|---|---|---|---|
| SC-001 (Lua cấp đồ) | ~19:14 (910075a0) | BLOCKED, báo cáo gộp 20:35 (d1669bea) | ~1 giờ 20 | Thiếu qh_bothu.lua + ref/gmroleitem.lua trong kho (B đã ghi trước "thiếu thì BLOCKED"; A đặt file 20:30). Sau đó nguyên nhân thật = online.lua (A, #321 20:45) nên SC-001 gần như vô nghĩa |
| SC-002 (server C++) | ~19:14 | PARTIAL: worktree thiếu KItem.cpp/KPlayerDBFuns.cpp (#B-065, 21:05) | ~1 giờ 50, chưa có diff | Task ghi đường dẫn đúng nhưng worktree không cắt từ nhánh qh-b035-b02c; B đã thêm yêu cầu |
| SC-003 (client APK) | ~19:14 | HUỶ 21:12 (Q-103, A làm trực tiếp) | — | Chưa có diff nào |
| SC-004 (port giật lag) | 20:59 | HUỶ 21:12 | ~13 phút | B thử `git apply --check`: 31/33/34 không áp sạch |

Nhận xét (B, CHỈ ĐỌC KHO, chưa là kết luận chủ):
- Tới 21:35: 0 diff mã do Codex giao ra; 2/4 task chặn vì thiếu đầu vào (file/worktree), 2/4 huỷ. Chưa thể nói Q-102 nhanh hơn cách A tự sửa; hiện chậm hơn do chặn đầu vào.
- Việc tìm ra nguyên nhân mất đồ đến từ đối chiếu BAI_HOC phiên trước (A, 20:45), không từ Codex hay đọc mã của B (B-056..060 đọc mã đều không thấy đường lỗi).
- Cải tiến đề xuất: trước khi giao Codex, Tổng quản chạy kiểm tiền điều kiện (file vung_file tồn tại trong worktree, file tham chiếu có mặt) rồi mới đặt status ready; B thêm dòng "Tiền điều kiện" vào TASKS/_MAU-SUA-CODE.md.
