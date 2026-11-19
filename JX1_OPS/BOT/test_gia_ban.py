import csv
import unittest

from JX1_OPS.BOT import gia_ban


class TestGiaBan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bang = gia_ban.BangGia()
        with open(gia_ban.CSV_MAC_DINH, encoding="utf-8", newline="") as f:
            cls.dong = list(csv.DictReader(f))

    def test_tam_mon_mau_khop_bang(self):
        mau = self.dong[:: len(self.dong) // 8][:8]
        self.assertEqual(len(mau), 8)
        for d in mau:
            mong_doi = max(float(d["gia_goc"]) * float(d["he_so_ban"]), float(d["gia_san_mac_ca"]))
            self.assertEqual(self.bang.gia_ban(d["ma_mon"]), mong_doi)

    def test_tra_theo_ten_co_dau_khong_phan_biet_hoa_thuong(self):
        self.assertEqual(self.bang.gia_ban("meleeweapon:3"), self.bang.gia_ban("CANG KIẾM"))
        self.assertEqual(self.bang.tim("thiết trủy thủ")["ma_mon"], "meleeweapon:2")

    def test_ten_loi_gbk_khong_lam_hong(self):
        self.assertEqual(len(self.bang.theo_ma), len(self.dong))
        for d in self.dong:
            self.bang.gia_ban(d["ma_mon"])

    def test_khong_co_va_thieu_gia(self):
        self.assertIsNone(self.bang.tim("khong-co-mon-nay"))
        with self.assertRaises(KeyError):
            self.bang.gia_ban("khong-co-mon-nay")
        self.assertEqual(self.bang.mon_thieu_gia(), [])


if __name__ == "__main__":
    unittest.main()
