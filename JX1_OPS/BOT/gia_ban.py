"""BOT GD1: doc bang gia vat pham, tinh gia ban (offline, chi thu vien chuan).

gia_ban = max(gia_goc * he_so_ban, gia_san_mac_ca); he so doc tu file, khong doan.
"""
import csv
import os
import unicodedata

CSV_MAC_DINH = os.path.join(os.path.dirname(__file__), "..", "STATE", "BOT", "gia-vat-pham.csv")


class ThieuGia(ValueError):
    """Mon co trong bang nhung thieu/loi truong gia."""


def _khoa_ten(s):
    return unicodedata.normalize("NFC", s).casefold().strip()


class BangGia:
    def __init__(self, duong_dan=CSV_MAC_DINH):
        self.theo_ma = {}
        self.theo_ten = {}
        with open(duong_dan, encoding="utf-8", newline="") as f:
            for dong in csv.DictReader(f):
                self.theo_ma[dong["ma_mon"]] = dong
                ten = (dong.get("ten_unicode") or "").strip()
                if ten:
                    self.theo_ten.setdefault(_khoa_ten(ten), dong)

    def tim(self, khoa):
        """Tra theo ma_mon truoc, roi theo ten co dau (khong phan biet hoa thuong). None neu khong co."""
        return self.theo_ma.get(khoa) or self.theo_ten.get(_khoa_ten(khoa))

    def gia_ban(self, khoa):
        dong = self.tim(khoa)
        if dong is None:
            raise KeyError(khoa)
        try:
            goc = float(dong["gia_goc"])
            he_so = float(dong["he_so_ban"])
            san = float(dong["gia_san_mac_ca"])
        except (TypeError, ValueError):
            raise ThieuGia("mon %s thieu gia_goc/he_so_ban/gia_san_mac_ca" % dong["ma_mon"])
        return max(goc * he_so, san)

    def mon_thieu_gia(self):
        thieu = []
        for ma, dong in self.theo_ma.items():
            try:
                self.gia_ban(ma)
            except ThieuGia:
                thieu.append(ma)
        return thieu
