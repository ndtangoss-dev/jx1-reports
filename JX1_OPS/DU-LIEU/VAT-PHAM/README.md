# THỐNG KÊ VẬT PHẨM / TRANG BỊ (B-052)

Trạng thái: **CHỈ ĐỌC DỮ LIỆU** (chưa chạy game/server). Sinh bằng `JX1_OPS/TOOLS/xuat_vat_pham.py` từ
`C:\Jx1CocoV3\...\ServerNew\_bin_v2_\gs\Settings\item` (chỉ đọc, không sửa nguồn).

## File chính
- `TONG-VAT-PHAM.csv` (UTF-8 BOM): một dòng một vật phẩm, cột `nguon` = thư mục nguồn (`item` = thư mục gốc, `item_004` = thư mục `004`). 27.240 dòng.
- `VAT-PHAM.xlsx`: sheet `TONG` + mỗi thư mục nguồn một sheet. (Tự viết bằng zipfile, CHƯA mở thử bằng Excel.)
- `item/`, `item_004/`, `item_004_itemvalue/`: CSV từng bảng gốc, giữ NGUYÊN mọi cột (không bỏ gì). File `.ini` chép sang `.ini.txt`.

## Cột của TONG
| Cột | Trạng thái |
|---|---|
| nguon, file, dong | ĐÃ GIẢI MÃ (chỗ lấy dòng trong bảng gốc; dong = số dòng trong file, tính cả tiêu đề) |
| ten, mo_ta | ĐÃ GIẢI MÃ chữ (Hán = GBK, Việt = TCVN3 → UTF-8) |
| genre, detail, particular | ĐÃ ĐỌC NGUYÊN SỐ; ý nghĩa từng số CHƯA LIỆT KÊ |
| cap, gia, ngu_hanh | ĐÃ ĐỌC theo vị trí cột (bảng trang bị); CHƯA đối chiếu với mã nguồn từng loại |
| dong_thuoc_tinh_goc | dạng `loại:min-max`; **loại là SỐ THÔ, CHƯA RÕ** nghĩa (vd 30, 31) |
| yeu_cau | dạng `loại:giá_trị`; loại là SỐ THÔ, CHƯA RÕ |
| du_lieu_tho_con_lai | các cột phía sau, CHƯA RÕ |
Bảng không phải trang bị (potion, questkey, mine, key…): chỉ lấy tên/cấp/giá nếu tìm thấy cột tiêu đề; phần còn lại nằm ở `du_lieu_tho_con_lai`. Cần cột đầy đủ → xem CSV từng bảng.

## Cần biết
- Mã hóa đoán theo từng ô: >25% chữ Latin → TCVN3, còn lại → GBK. Đã soát mẫu, 0 ký tự lỗi; vài tên hiếm có thể sai dấu.
- Thư mục gốc và `004` có BẢN TRÙNG/CŨ (`*_`, `*- Copy`, `*_cu`, `*bak*`, `GoldItem_.txt`). Dòng trùng ID giữa hai nơi KHÔNG được loại bỏ. Server nạp thư mục nào: CHƯA KIỂM (client đọc `004`: KBasPropTbl.cpp:16–23).
- GoldMagic / nhóm combine: nằm trong các bảng tương ứng ở `item_004`/`item_004_itemvalue`, chưa gộp vào TONG.

## Mục lục bảng (thư mục, file, loại, số dòng dữ liệu, số cột)
| Thư mục | File | Vào TONG | Dòng | Cột |
|---|---|---|---|---|
| item | AbradeRate.ini | ini | 69 | - |
| item | ArmorRes_.txt | - | 471 | 3 |
| item | CharmRes.txt | - | 31 | 2 |
| item | ChiBangRes.txt | - | 27 | 2 |
| item | GoldItemSuit.ini | ini | 403 | - |
| item | GoldMagic.txt | - | 3820 | 12 |
| item | GolditemRes.txt | - | 5656 | 3 |
| item | GolditemRes_.txt | - | 5656 | 3 |
| item | HelmRes_.txt | - | 401 | 3 |
| item | HorseRes.txt | - | 321 | 3 |
| item | Key.txt | tong(khac) | 31 | 46 |
| item | KeyRes.txt | - | 33 | 2 |
| item | Magic.ini | ini | 328 | - |
| item | MeleeRes_.txt | - | 471 | 3 |
| item | PiFengRes.txt | - | 27 | 2 |
| item | PlantItem.txt | tong(khac) | 3555 | 59 |
| item | PlantRes.txt | - | 997 | 3 |
| item | PlatinaequipRes.txt | - | 4942 | 3 |
| item | RangeRes_.txt | - | 91 | 3 |
| item | TownPortal.txt | tong(khac) | 1 | 8 |
| item | armor.txt | tong(equip) | 290 | 46 |
| item | armorres.txt | - | 291 | 3 |
| item | atlas_compound.txt | - | 153 | 54 |
| item | belt.txt | tong(equip) | 20 | 46 |
| item | boot.txt | tong(equip) | 40 | 46 |
| item | cuff.txt | tong(equip) | 20 | 46 |
| item | helm.txt | tong(equip) | 140 | 46 |
| item | helmres.txt | - | 141 | 2 |
| item | horse.txt | tong(equip) | 124 | 89 |
| item | magicattrib.txt | - | 369 | 29 |
| item | magicattrib_.txt | - | 1331 | 27 |
| item | magicattrib_ge.txt | - | 3045 | 12 |
| item | magicattriblevel_index.txt | - | 48 | 6 |
| item | magicattriblevel_index_.txt | - | 99 | 8 |
| item | magicattriblevel_rong.txt | - | 39 | 6 |
| item | magicscript.txt | - | 1377 | 19 |
| item | mantle.txt | tong(equip) | 3 | 46 |
| item | meleeres.txt | - | 61 | 2 |
| item | meleeweapon.txt | tong(equip) | 60 | 46 |
| item | minebase.txt | tong(khac) | 48 | 6 |
| item | npcdroprate.ini | ini | 418 | - |
| item | other_compound.txt | - | 21 | 27 |
| item | pendant.txt | tong(equip) | 20 | 46 |
| item | potion.txt | tong(khac) | 25 | 28 |
| item | rangeres.txt | - | 30 | 2 |
| item | rangeweapon.txt | tong(equip) | 30 | 46 |
| item | ring.txt | tong(equip) | 10 | 46 |
| item_004 | Charm.txt | tong(khac) | 2 | 47 |
| item_004 | GoldItem.txt | tong(equip) | 5945 | 65 |
| item_004 | GoldItem_.txt | tong(equip) | 5945 | 65 |
| item_004 | GoldMagic.txt | - | 4360 | 12 |
| item_004 | Mask.txt | tong(equip) | 966 | 51 |
| item_004 | PiFeng.txt | tong(equip) | 14 | 53 |
| item_004 | ShiPin.txt | tong(equip) | 260 | 45 |
| item_004 | TownPortal.txt | tong(khac) | 1 | 8 |
| item_004 | YinJian.txt | tong(equip) | 13 | 53 |
| item_004 | amulet.txt | tong(equip) | 20 | 53 |
| item_004 | armor.txt | tong(equip) | 290 | 53 |
| item_004 | armorres.txt | - | 291 | 3 |
| item_004 | atlas_compound.txt | - | 203 | 53 |
| item_004 | belt.txt | tong(equip) | 20 | 51 |
| item_004 | bianshi.txt | - | 377 | 19 |
| item_004 | boot.txt | tong(equip) | 40 | 51 |
| item_004 | brokenequip.txt | - | 1 | 8 |
| item_004 | cuff.txt | tong(equip) | 20 | 51 |
| item_004 | ext_suite_activate_count.txt | - | 282 | 3 |
| item_004 | fusion.txt | - | 371 | 25 |
| item_004 | fusion__.txt | - | 371 | 25 |
| item_004 | helm.txt | tong(equip) | 141 | 51 |
| item_004 | helmres.txt | - | 141 | 2 |
| item_004 | horse.txt | tong(equip) | 321 | 51 |
| item_004 | horseres.txt | - | 331 | 3 |
| item_004 | magicattrib.txt | - | 369 | 29 |
| item_004 | magicattrib_Cu.txt | - | 330 | 29 |
| item_004 | magicattrib_Minopt.txt | - | 330 | 29 |
| item_004 | magicattrib_ge.txt | - | 4322 | 12 |
| item_004 | magicattriblevel-bak-v1.txt | - | 480 | 37 |
| item_004 | magicattriblevel.txt | - | 480 | 37 |
| item_004 | magicattriblevel_cu.txt | - | 480 | 37 |
| item_004 | magicattriblevel_index-bak-v1.txt | - | 100 | 8 |
| item_004 | magicattriblevel_index.txt | - | 48 | 6 |
| item_004 | magicattriblevel_index_cu.txt | - | 100 | 9 |
| item_004 | magicattribÔ­À´.txt | - | 1330 | 27 |
| item_004 | magicscript.txt | - | 5546 | 30 |
| item_004 | magicscript_stack.txt | - | 473 | 11 |
| item_004 | mantle.txt | tong(equip) | 3 | 46 |
| item_004 | medmaterialbase.txt | rong | 0 | 0 |
| item_004 | meleeres.txt | - | 61 | 2 |
| item_004 | meleeweapon.txt | tong(equip) | 70 | 53 |
| item_004 | meleeweapon_cu.txt | - | 470 | 53 |
| item_004 | mine - Copy.txt | - | 237 | 24 |
| item_004 | mine-bak.txt | - | 214 | 33 |
| item_004 | mine.txt | tong(khac) | 321 | 24 |
| item_004 | mine_NEW.txt | - | 235 | 33 |
| item_004 | mine_bk.txt | - | 202 | 33 |
| item_004 | mine_goc.txt | - | 218 | 33 |
| item_004 | pendant.txt | tong(equip) | 20 | 51 |
| item_004 | platinaequip - Copy.txt | - | 5670 | 72 |
| item_004 | platinaequip.txt | tong(equip) | 5670 | 72 |
| item_004 | potion.txt | tong(khac) | 49 | 33 |
| item_004 | questkey.txt | tong(khac) | 1326 | 23 |
| item_004 | questkey_.txt | tong(khac) | 1326 | 32 |
| item_004 | questkey_cu.txt | - | 202 | 32 |
| item_004 | questkey_new.txt | - | 1326 | 32 |
| item_004 | questkey_stack.txt | - | 760 | 2 |
| item_004 | rangeres.txt | - | 30 | 2 |
| item_004 | rangeweapon.txt | tong(equip) | 30 | 53 |
| item_004 | rangeweapon_cu.txt | - | 90 | 53 |
| item_004 | ring.txt | tong(equip) | 10 | 51 |
| item_004 | signet.txt | tong(equip) | 1 | 46 |
| item_004 | suite_activate_count.txt | - | 292 | 2 |
| item_004 | unique.txt | rong | 0 | 0 |
| item_004 | ÐÂmagicattrib.txt | - | 1330 | 27 |
| item_004_itemvalue | equip_enchasable_level.txt | - | 10 | 3 |
| item_004_itemvalue | equip_enchasable_magic_pos.txt | - | 6 | 2 |
| item_004_itemvalue | equip_enchasable_socket.txt | - | 6 | 2 |
| item_004_itemvalue | equip_enchasable_type.txt | - | 50 | 5 |
| item_004_itemvalue | equip_gold.txt | - | 491 | 4 |
| item_004_itemvalue | equip_normal_magic.txt | - | 7 | 2 |
| item_004_itemvalue | magicattrib_combine.txt | - | 49 | 50 |
| item_004_itemvalue | ore.txt | - | 10 | 2 |
