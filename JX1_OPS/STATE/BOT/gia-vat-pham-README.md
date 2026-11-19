# gia-vat-pham.csv (BOT GĐ1, #220/#237)
- Nguồn: `gs/Settings/item/004/*.txt` (cột 11 "Giá", cột 12 "Cấp"), 14 bảng, 1034 dòng. `ma_mon` = bảng:số dòng (dòng 1 là tiêu đề).
- `ten` là TCVN3 đọc thô bằng latin1 (chưa đổi sang Unicode) [CHƯA LÀM].
- `he_so_ban`=0,5 và `gia_san_mac_ca`=gia_goc/2 là GIẢ ĐỊNH, chưa kiểm hệ số bán lại thật của game. `do_hiem`, `thanh_thi_ban`, `nhom_kho_hom_nay` để trống cho chủ/Bot điền; món quan trọng chủ sửa tay.
- Bảng unique/GoldItem/platinaequip chưa đưa vào.

## Cập nhật (B, 19/11): tên đã đổi sang Unicode
- Cột mới cuối file: `ten_unicode` (TCVN3 → Unicode bằng `TOOLS/bot_tcvn3.py`, chạy: `python -I TOOLS/bot_tcvn3.py <vào> <ra>`).
- 17 dòng tên rác (ví dụ `ặặắẫàÄÅỷãỗ`, `Â¿ÃÃÃÃ`) là tên GBK/ký tự lạ, không phải TCVN3: để nguyên, bot không bán theo tên mà theo `ma_mon`.
- Vài tên gốc trong game có thể gõ sai chính tả (ví dụ "Trãm Mã Kiếm"): giữ nguyên như game.
