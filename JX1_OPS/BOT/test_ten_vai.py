import unittest

from JX1_OPS.BOT.ten_vai import gen_ten, kiem_ten


class KiemTenTests(unittest.TestCase):
    def test_ten_hop_le_va_gioi_han_do_dai(self):
        self.assertEqual((True, "Tên hợp lệ."), kiem_ten("Cctesterone", []))
        self.assertTrue(kiem_ten("Abcdef", [])[0])
        self.assertTrue(kiem_ten("Abcdefghijklmnop", [])[0])

    def test_tu_choi_ten_sai_dinh_dang(self):
        for ten in ("T36nv2", "Ts baone", "abc", "Abcdef ", " Abcdef", "Abc_def", "Abcdefghijklmnopq", "Ábcdef"):
            with self.subTest(ten=ten):
                self.assertFalse(kiem_ten(ten, [])[0])

    def test_tu_choi_trung_khong_phan_biet_hoa_thuong(self):
        self.assertEqual((False, "Tên đã tồn tại."), kiem_ten("Cctesterone", ["CCTESTERONE"]))
        self.assertEqual((False, "Tên đã tồn tại."), kiem_ten("Cctesterone", [b"CCTESTERONE"]))

    def test_ten_khong_phai_chuoi_va_danh_sach_khong_hop_le(self):
        self.assertFalse(kiem_ten(123, [])[0])
        self.assertEqual((False, "Danh sách tên hiện có không hợp lệ."), kiem_ten("Cctesterone", 123))

    def test_gen_ten_sinh_ten_chu_cai_va_tranh_trung(self):
        self.assertEqual("Botaaa", gen_ten("Bot", 1, []))
        self.assertEqual("Botaab", gen_ten("Bot", 2, []))
        self.assertEqual("Botaab", gen_ten("Bot", 1, ["BOTAAA", "Botaaa"]))

    def test_gen_ten_bo_qua_hau_to_da_co(self):
        self.assertEqual("abcdefb", gen_ten("abcdef", 1, ["abcdefa"]))

    def test_gen_ten_tu_choi_tham_so_khong_the_sinh_ten(self):
        for prefix, n in (("Bot1", 1), ("Bot", 0), ("Abcdefghijklmnop", 1)):
            with self.subTest(prefix=prefix, n=n):
                with self.assertRaises(ValueError):
                    gen_ten(prefix, n, [])


if __name__ == "__main__":
    unittest.main()
