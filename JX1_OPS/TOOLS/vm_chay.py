"""Duong vao VM Test-36 dung chung cho A va B (Q-79 / #249). Danh sach TRANG, khong shell tuy y.
Chi toi 192.168.56.150 (Test-36). Mat khau lay tu Credential Manager may that (jxlab_cred.ps1), khong in ra, khong ghi file.
Lenh:
  chain-up                  chay task JX-ChainUp (script idempotent: chuoi da song thi chi kiem tra), in chain_up.log cuoi
  ports                     cong nghe 5001-5005, 5002, 56722, 56732, 51189 + tien trinh chuoi
  log <bishop|goddess|relay|gs> [n]   n dong cuoi (mac dinh 50, toi da 200) cua log moi nhat
  ten-co <Ten>              ten nhan vat co trong roledb khong (chi doc, tim byte ASCII; khong xuat du lieu khac)
Chay: python -I -X utf8 vm_chay.py <lenh> [doi so]. Khong mat khau/khoa trong tep."""
import re
import subprocess
import sys

VM = "192.168.56.150"
ROOT = r"C:\JX\ServerNew\_bin_v2_"
CRED = r"C:\Jx1CocoV3\docs-analysis\scripts\jxlab_cred.ps1"
LOGS = {"bishop": ROOT + r"\gw\bishop_log", "goddess": ROOT + r"\gw\goddes_log", "relay": ROOT + r"\gw\relay_log",
        "gs": ROOT + r"\gs\gameser_log"}

BLOCKS = {
    "chain-up": r"""schtasks /run /tn JX-ChainUp | Out-Null; Start-Sleep 8; Get-Content C:\JX\chain_up.log -Tail 8""",
    "ports": r"""netstat -ano | Select-String 'LISTENING' | Select-String ':(5001|5002|5003|5004|5005|56722|56732|51189)\s' | % { $_.Line.Trim() };
Get-Process Sword3PaySys,Goddess,S3RelayServer,Bishop,gs001,sqlservr -ErrorAction SilentlyContinue | % { $_.Name + ' ' + $_.Id }""",
    "log": r"""$f = Get-ChildItem '%(dir)s' -File -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($f) { '== ' + $f.Name; Get-Content $f.FullName -Tail %(n)d } else { 'khong co log' }""",
    "ten-co": r"""$fs = [IO.File]::Open('""" + ROOT + r"""\gw\database\roledb', 'Open', 'Read', 'ReadWrite'); $b = New-Object byte[] $fs.Length; [void]$fs.Read($b, 0, $b.Length); $fs.Close()
$t = [Text.Encoding]::ASCII.GetBytes('%(name)s'); $hit = $false
for ($i = 0; $i -le $b.Length - $t.Length -and -not $hit; $i++) { if ($b[$i] -eq $t[0]) { $k = 1; while ($k -lt $t.Length -and $b[$i+$k] -eq $t[$k]) { $k++ }; if ($k -eq $t.Length) { $hit = $true } } }
if ($hit) { 'CO' } else { 'KHONG' }""",
}


def goi(block):
    ps = ". '%s'; $c = Get-JxCred; Invoke-Command -ComputerName %s -Credential $c -ScriptBlock { %s }" % (CRED, VM, block)
    p = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, timeout=240)
    return (p.stdout.decode("utf8", "replace") + p.stderr.decode("utf8", "replace")).strip()


def main(a):
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd in ("chain-up", "ports"):
        print(goi(BLOCKS[cmd]))
    elif cmd == "log":
        if len(a) < 2 or a[1] not in LOGS:
            sys.exit("log <%s> [n]" % "|".join(LOGS))
        n = int(a[2]) if len(a) > 2 and a[2].isdigit() else 50
        print(goi(BLOCKS["log"] % {"dir": LOGS[a[1]], "n": max(1, min(n, 200))}))
    elif cmd == "ten-co":
        if len(a) < 2 or not re.fullmatch(r"[A-Za-z0-9]{3,24}", a[1]):
            sys.exit("ten-co <Ten ASCII 3-24>")
        print(a[1], goi(BLOCKS["ten-co"] % {"name": a[1]}))
    else:
        sys.exit("lenh khong co trong danh sach: " + cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
