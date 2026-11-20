"""B-052: xuat thong ke vat pham tu Settings\\item (chi DOC file du lieu, khong chay exe).
Dung: python -I xuat_vat_pham.py <thu-muc-item> <thu-muc-dich>
Ma hoa: tieu de/ten Han = GBK; ten Viet = TCVN3 (ABC). Moi o tu chon theo heuristic (xem README)."""
import csv, os, re, sys, zipfile
from xml.sax.saxutils import escape

SRC = sys.argv[1]
DST = sys.argv[2]

# TCVN3 (ABC) chu thuong + chu hoa co dau co ban
_T = {}
def _put(start, s):
    for i, ch in enumerate(s):
        _T[start + i if isinstance(start, int) else start[i]] = ch
for codes, s in [
    ("A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE", "ĂÂÊÔƠƯĐăâêôơưđ"),
    ("B5 B6 B7 B8 B9", "àảãáạ"),
    ("BB BC BD BE C6", "ằẳẵắặ"),
    ("C7 C8 C9 CA CB", "ầẩẫấậ"),
    ("CC CE CF D0 D1", "èẻẽéẹ"),
    ("D2 D3 D4 D5 D6", "ềểễếệ"),
    ("D7 D8 DC DD DE", "ìỉĩíị"),
    ("DF E1 E2 E3 E4", "òỏõóọ"),
    ("E5 E6 E7 E8 E9", "ồổỗốộ"),
    ("EA EB EC ED EE", "ờởỡớợ"),
    ("EF F1 F2 F3 F4", "ùủũúụ"),
    ("F5 F6 F7 F8 F9", "ừửữứự"),
    ("FA FB FC FD FE", "ỳỷỹýỵ"),
]:
    for c, ch in zip(codes.split(), s):
        _T[int(c, 16)] = ch

def tcvn(b):
    return "".join(_T.get(x, chr(x)) if x >= 0x80 else chr(x) for x in b)

def dec(b):
    """Giai ma 1 o: >25% chu Latin -> TCVN3, nguoc lai GBK."""
    if not any(x >= 0x80 for x in b):
        return b.decode("ascii", "replace")
    if len(re.findall(rb"[A-Za-z]", b)) > 0.25 * len(b):   # nhieu chu Latin -> ten Viet TCVN3
        return tcvn(b)
    try:
        return b.decode("gbk")
    except UnicodeDecodeError:
        return tcvn(b)

def read_table(path):
    raw = open(path, "rb").read()
    lines = raw.replace(b"\r\n", b"\n").split(b"\n")
    while lines and not lines[-1].strip():
        lines.pop()
    rows = []
    for i, ln in enumerate(lines):
        cells = ln.split(b"\t")
        if i == 0:
            rows.append([c.decode("gbk", "replace") for c in cells])
        else:
            rows.append([dec(c) for c in cells])
    return rows

def write_csv(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)

EQUIP = {"meleeweapon", "rangeweapon", "armor", "helm", "boot", "belt", "cuff", "ring", "pendant", "amulet",
         "mantle", "horse", "golditem", "platinaequip", "unique", "signet", "pifeng", "mask", "yinjian", "shipin"}
OTHER = {"potion", "questkey", "mine", "medmaterialbase", "charm", "townportal", "minebase", "plantitem", "key"}
TONG_HEADER = ["nguon", "file", "dong", "ten", "genre", "detail", "particular", "cap", "gia", "ngu_hanh", "mo_ta",
               "dong_thuoc_tinh_goc(loai:min-max)", "yeu_cau(loai:gia_tri)", "du_lieu_tho_con_lai",
               "dong_thuoc_tinh_doc_duoc", "yeu_cau_doc_duoc", "ban_trung"]

def norm_equip(src, fn, rows):
    out = []
    for i, r in enumerate(rows[1:], start=2):
        if not r or not r[0].strip():
            continue
        r = r + [""] * (47 - len(r))
        attrs = []
        for k in range(7):
            t, a, b = r[13 + 3 * k: 16 + 3 * k]
            if t.strip() and t.strip() != "0" or (a.strip() not in ("", "0")):
                attrs.append(f"{t}:{a}-{b}")
        reqs = []
        for k in range(6):
            t, v = r[34 + 2 * k: 36 + 2 * k]
            if t.strip() and t.strip() != "0" or v.strip() not in ("", "0"):
                reqs.append(f"{t}:{v}")
        out.append([src, fn, i, r[0], r[1], r[2], r[3], r[11], r[10], r[9], r[8],
                    ";".join(attrs), ";".join(reqs), "|".join(r[46:]).strip("|")])
    return out

def norm_other(src, fn, rows):
    hdr = rows[0]
    def col(*names):
        for n in names:
            for j, h in enumerate(hdr):
                if h.strip().lower() == n.lower():
                    return j
        return None
    ci = {k: col(*v) for k, v in {"ten": ("名称", "Name"), "genre": ("ItemGenre", "道具种类"), "detail": ("DetailType", "具体类别"),
                                  "cap": ("Level", "等级", "nLevel"), "gia": ("Price", "价格", "nPrice")}.items()}
    out = []
    for i, r in enumerate(rows[1:], start=2):
        if not r or not r[0].strip():
            continue
        g = lambda k: r[ci[k]] if ci[k] is not None and ci[k] < len(r) else ""
        out.append([src, fn, i, g("ten"), g("genre"), g("detail"), "", g("cap"), g("gia"), "", "", "", "",
                    "|".join(r)])
    return out

def col_letter(n):
    s = ""
    while n:
        n, m = divmod(n - 1, 26)
        s = chr(65 + m) + s
    return s

def write_xlsx(path, sheets):
    """sheets: list[(ten, rows)] - xlsx toi gian bang zipfile (khong co openpyxl)."""
    used = set()
    def sname(n):
        n = re.sub(r"[\[\]:*?/\\]", "_", n)[:31] or "S"
        base, k = n, 1
        while n in used:
            k += 1
            n = base[:28] + str(k)
        used.add(n)
        return n
    names = [sname(n) for n, _ in sheets]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>' +
                   "".join(f'<Override PartName="/xl/worksheets/sheet{i+1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(sheets))) + "</Types>")
        z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml", '<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>' +
                   "".join(f'<sheet name="{escape(n)}" sheetId="{i+1}" r:id="rId{i+1}"/>' for i, n in enumerate(names)) + "</sheets></workbook>")
        z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
                   "".join(f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i+1}.xml"/>' for i in range(len(sheets))) + "</Relationships>")
        for i, (_, rows) in enumerate(sheets):
            parts = ['<?xml version="1.0" encoding="UTF-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>']
            for ri, r in enumerate(rows, start=1):
                parts.append(f'<row r="{ri}">')
                for ci, v in enumerate(r, start=1):
                    v = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(v))
                    parts.append(f'<c r="{col_letter(ci)}{ri}" t="inlineStr"><is><t xml:space="preserve">{escape(v)}</t></is></c>')
                parts.append("</row>")
            parts.append("</sheetData></worksheet>")
            z.writestr(f"xl/worksheets/sheet{i+1}.xml", "".join(parts))

def load_bang():
    f = os.path.join(DST, "BANG-LOAI-THUOC-TINH.csv")
    b = {}
    if os.path.exists(f):
        for r in list(csv.reader(open(f, encoding="utf-8-sig")))[1:]:
            t = r[4] or r[3]
            lab = t.split(":")[0].strip() if ":" in t else t
            lab = re.sub(r"#\w+[~+\-]?", "", lab).strip() if ":" not in t else lab
            b[r[0]] = (lab if r[6] == "DA TRA" else "CHUA RO(" + r[1] + ")")
    return b

def doc_duoc(txt, b):
    out = []
    for part in txt.split(";"):
        if not part:
            continue
        t, _, v = part.partition(":")
        lab = b.get(t.strip(), "CHUA RO(loai " + t + ")") if t.strip() else "CHUA RO(loai trong)"
        m = re.match(r"^(-?\d+)-(-?\d+)$", v)
        if m:
            lo, hi = m.groups()
            v = lo if lo == hi else lo + "~" + hi
        out.append(lab + " " + v)
    return "; ".join(out)

SAOLUU = re.compile(r"(_cu|copy|bak|-bak|_old)|_\.txt$|_$", re.I)

def ban_trung(src, fn, root_in_004):
    base = os.path.splitext(fn)[0]
    tag = []
    if SAOLUU.search(fn) or base.endswith("_"):
        tag.append("nghi_ban_phu(ten file _/Copy/cu/bak)")
    if src == "item" and fn.lower() in root_in_004:
        tag.append("trung_ten_file_voi_004")
    return "|".join(tag)

def main():
    tong = []
    per_folder = {}
    readme = []
    for dp, dn, fns in os.walk(SRC):
        rel = os.path.relpath(dp, SRC).replace("\\", "/")
        folder = "item" if rel == "." else "item_" + rel.replace("/", "_")
        for fn in sorted(fns):
            p = os.path.join(dp, fn)
            base, ext = os.path.splitext(fn)
            if ext.lower() not in (".txt", ".ini"):
                continue
            if ext.lower() == ".ini":
                text = "\n".join("\t".join(dec(c) for c in ln.split(b"\t")) for ln in open(p, "rb").read().replace(b"\r\n", b"\n").split(b"\n"))
                os.makedirs(os.path.join(DST, folder), exist_ok=True)
                open(os.path.join(DST, folder, fn + ".txt"), "w", encoding="utf-8-sig").write(text)
                readme.append((folder, fn, "ini", len(text.split("\n")), "-"))
                continue
            rows = read_table(p)
            if not rows:
                readme.append((folder, fn, 'rong', 0, 0))
                continue
            write_csv(os.path.join(DST, folder, base + ".csv"), rows)
            key = base.lower().rstrip("_")
            kind = "-"
            if key in EQUIP and len(rows[0]) >= 40:
                n = norm_equip(folder, fn, rows); kind = "tong(equip)"
            elif key in OTHER:
                n = norm_other(folder, fn, rows); kind = "tong(khac)"
            else:
                n = []
            tong += n
            per_folder.setdefault(folder, []).extend(n)
            readme.append((folder, fn, kind, len(rows) - 1, len(rows[0])))
    b = load_bang()
    f004 = {fn.lower() for fn in os.listdir(os.path.join(SRC, "004"))} if os.path.isdir(os.path.join(SRC, "004")) else set()
    for r in tong:
        r += [doc_duoc(r[11], b), doc_duoc(r[12], b), ban_trung(r[0], r[1], f004)]
    for rs in per_folder.values():
        for r in rs:
            if len(r) == 14:
                r += [doc_duoc(r[11], b), doc_duoc(r[12], b), ban_trung(r[0], r[1], f004)]
    write_csv(os.path.join(DST, "TONG-VAT-PHAM.csv"), [TONG_HEADER] + tong)
    write_xlsx(os.path.join(DST, "VAT-PHAM.xlsx"), [("TONG", [TONG_HEADER] + tong)] +
               [(f, [TONG_HEADER] + r) for f, r in sorted(per_folder.items()) if r])
    with open(os.path.join(DST, "_muc_luc_tam.tsv"), "w", encoding="utf-8") as f:
        for r in readme:
            f.write("\t".join(map(str, r)) + "\n")
    print("TONG", len(tong), "file", len(readme))

main()
