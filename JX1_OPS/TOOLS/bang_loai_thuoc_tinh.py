"""B-054: bang so loai thuoc tinh -> enum (KMagicAttrib.h) -> Han (MagicDesc.ini) -> Viet (MagicDesc_mobile.ini).
Chi DOC file. Dung: python -I bang_loai_thuoc_tinh.py <KMagicAttrib.h> <Settings-dir> <out.csv>"""
import csv, re, sys
H, S, OUT = sys.argv[1:4]
sys.argv = ["x", "x", "x"]
_src = open(__file__.replace("bang_loai_thuoc_tinh", "xuat_vat_pham"), encoding="utf-8").read().split("def read_table")[0]
exec(_src.split("SRC = sys.argv[1]")[0] + _src.split("DST = sys.argv[2]")[1])   # lay tcvn/dec

def enum():
    raw = open(H, "rb").read().decode("gbk", "replace")
    body = raw.split("enum MAGIC_ATTRIB", 1)[1].split("};", 1)[0].split("{", 1)[1]
    n = -1; tab = []
    for ln in body.split("\n"):
        code, _, cm = ln.partition("//")
        for m in re.finditer(r"\b(magic_\w+)\s*(=\s*(\d+))?\s*,?", code):
            n = int(m.group(3)) if m.group(3) else n + 1
            tab.append((n, m.group(1), cm.strip()))
    return tab

def desc(fn):
    d = {}
    for ln in open(S + "/" + fn, "rb").read().replace(b"\r\n", b"\n").split(b"\n"):
        if b"=" not in ln or ln.lstrip().startswith(b"#"):
            continue
        k, v = ln.split(b"=", 1)
        v = v.split(b"//")[0]
        d[k.strip().decode("ascii", "replace")] = dec(v.strip(b" \t")).strip()
    return d

han, viet = desc("MagicDesc.ini"), desc("MagicDesc_mobile.ini")
rows = [["so_loai", "ten_enum", "ghi_chu_trong_ma(Han)", "mo_ta_Han(MagicDesc.ini)", "mo_ta_Viet(MagicDesc_mobile.ini)", "dang_gia_tri", "trang_thai"]]
for n, e, cm in enum():
    k = e[len("magic_"):]
    h, v = han.get(k, ""), viet.get(k, "")
    f = []
    if k.endswith("_p"): f.append("phan tram")
    elif k.endswith("_v"): f.append("gia tri")
    elif k.endswith("_b"): f.append("co/khong")
    t = h or v
    if "#d1~" in t: f.append("min-max")
    if "#s1" in t: f.append("ngu hanh")
    if "#m1" in t: f.append("mon phai")
    if "#x1" in t: f.append("gioi tinh")
    rows.append([n, e, cm, h, v, "; ".join(f), "DA TRA" if (h or v) else "CHUA RO (khong co mo ta hien thi)"])
with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    csv.writer(f).writerows(rows)
print(len(rows) - 1, "enum;", sum(1 for r in rows[1:] if r[6] == "DA TRA"), "co mo ta")
