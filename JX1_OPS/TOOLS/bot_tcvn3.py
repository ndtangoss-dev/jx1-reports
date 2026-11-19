"""Doi ten TCVN3 (doc tho bang latin1) sang Unicode cho gia-vat-pham.csv. Chay: python -I bot_tcvn3.py <csv_vao> <csv_ra>"""
import csv
import sys

_T = {0xA1: "Ă", 0xA2: "Â", 0xA3: "Ê", 0xA4: "Ô", 0xA5: "Ơ", 0xA6: "Ư", 0xA7: "Đ",
      0xA8: "ă", 0xA9: "â", 0xAA: "ê", 0xAB: "ô", 0xAC: "ơ", 0xAD: "ư", 0xAE: "đ"}
for base, chars in (
    (0xB5, "àảãáạ"), (0xBB, "ằẳẵắ"), (0xC6, "ặ"), (0xC7, "ầẩẫấậ"), (0xCC, "è"), (0xCE, "ẻẽéẹ"),
    (0xD2, "ềểễếệ"), (0xD7, "ìỉ"), (0xDC, "ĩíị"), (0xDF, "ò"), (0xE1, "ỏõóọ"), (0xE5, "ồổỗốộ"),
    (0xEA, "ờởỡớợ"), (0xEF, "ù"), (0xF1, "ủũúụ"), (0xF5, "ừửữứự"), (0xFA, "ỳỷỹýỵ"),
):
    for i, c in enumerate(chars):
        _T[base + i] = c


def tcvn3(s):
    try:
        raw = s.encode("latin-1")
    except UnicodeEncodeError:
        return s
    return "".join(_T.get(b, chr(b)) for b in raw)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8", newline="") as f, open(sys.argv[2], "w", encoding="utf-8", newline="") as g:
        r = csv.DictReader(f)
        w = csv.DictWriter(g, r.fieldnames + ["ten_unicode"])
        w.writeheader()
        for row in r:
            row["ten_unicode"] = tcvn3(row["ten"])
            w.writerow(row)
