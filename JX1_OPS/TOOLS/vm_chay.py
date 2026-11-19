"""Duong vao VM Test-36 dung chung cho A va B (Q-79 / #249). Danh sach TRANG, khong shell tuy y.
Chi toi 192.168.56.150 (Test-36). Mat khau lay tu Credential Manager may that (jxlab_cred.ps1), khong in ra, khong ghi file.
Lenh:
  chain-up                  chay task JX-ChainUp (script idempotent: chuoi da song thi chi kiem tra), in chain_up.log cuoi
  ports                     cong nghe 5001-5005, 5002, 56722, 56732, 51189 + tien trinh chuoi
  log <bishop|goddess|relay|gs> [n]   n dong cuoi (mac dinh 50, toi da 200) cua log moi nhat
  do-gs [giay]              DO (chi doc): CPU%% gs001 trung binh [giay, mac dinh 10, toi da 60], RAM, so luong, so ket noi TCP tai 56722/51189, byte NIC gui/nhan
  ten-co <Ten>              ten nhan vat co trong roledb khong (chi doc, tim byte ASCII; khong xuat du lieu khac)
  tao-tk-test <tk>          (Q-45, #255) tao tai khoan test tk[a-z0-9]{4,12} tren Test-36 (db account: Account_Info + Account_Habitus 1 nam).
                            Mat khau sinh ngau nhien, cat o %LOCALAPPDATA%/jx1-secrets/<tk>.txt (ngoai kho), KHONG in ra.
                            Hoan tac: xoa-tk-test <tk> (chi tk do lenh nay tao, co file bi mat).
Chay: python -I -X utf8 vm_chay.py <lenh> [doi so]. Khong mat khau/khoa trong tep."""
import hashlib
import os
import re
import secrets
import subprocess
import sys
from pathlib import Path

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
    "do-gs": r"""$n = %(n)d; $pr = Get-Process gs001 -ErrorAction Stop
$c0 = $pr.CPU; $t0 = Get-Date; $a0 = Get-NetAdapterStatistics; $s0 = ($a0 | Measure-Object SentBytes -Sum).Sum; $r0 = ($a0 | Measure-Object ReceivedBytes -Sum).Sum; Start-Sleep $n
$pr = Get-Process gs001; $dt = ((Get-Date) - $t0).TotalSeconds; $a1 = Get-NetAdapterStatistics; $s1 = ($a1 | Measure-Object SentBytes -Sum).Sum; $r1 = ($a1 | Measure-Object ReceivedBytes -Sum).Sum
$cpus = (Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors
'gs001 CPU%%=' + [math]::Round(($pr.CPU - $c0) / $dt / $cpus * 100, 2) + ' (tren ' + $cpus + ' CPU, ' + [math]::Round($dt,1) + ' s) RAM_MB=' + [math]::Round($pr.WorkingSet64/1MB,1) + ' thread=' + $pr.Threads.Count + ' handle=' + $pr.HandleCount
'NIC gui_B/s=' + [math]::Round(($s1 - $s0) / $dt) + ' nhan_B/s=' + [math]::Round(($r1 - $r0) / $dt)
'TCP ESTABLISHED 56722=' + @(Get-NetTCPConnection -State Established -LocalPort 56722 -ErrorAction SilentlyContinue).Count + ' 51189=' + @(Get-NetTCPConnection -State Established -LocalPort 51189 -ErrorAction SilentlyContinue).Count""",
    "ten-co": r"""$fs = [IO.File]::Open('""" + ROOT + r"""\gw\database\roledb', 'Open', 'Read', 'ReadWrite'); $b = New-Object byte[] $fs.Length; [void]$fs.Read($b, 0, $b.Length); $fs.Close()
$t = [Text.Encoding]::ASCII.GetBytes('%(name)s'); $hit = $false
for ($i = 0; $i -le $b.Length - $t.Length -and -not $hit; $i++) { if ($b[$i] -eq $t[0]) { $k = 1; while ($k -lt $t.Length -and $b[$i+$k] -eq $t[$k]) { $k++ }; if ($k -eq $t.Length) { $hit = $true } } }
if ($hit) { 'CO' } else { 'KHONG' }""",
}

SQLCMD = r"C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE"
TK = re.compile(r"tk[a-z0-9]{4,12}")
SECRETS = Path(os.environ.get("LOCALAPPDATA", ".")) / "jx1-secrets"


def sql(q):
    return goi("& '%s' -S '.\\SQLEXPRESS' -E -d account -W -h -1 -Q \"%s\" 2>&1" % (SQLCMD, q))


def tao_tk(tk):
    if not TK.fullmatch(tk):
        sys.exit("ten tk phai la tk + 4..12 chu thuong/so")
    if sql("SET NOCOUNT ON; SELECT COUNT(*) FROM Account_Info WHERE cAccName='%s'" % tk).split()[-1:] != ["0"]:
        sys.exit("tk da ton tai hoac khong kiem duoc")
    pw = secrets.token_urlsafe(9)[:12].replace("-", "x").replace("_", "y")
    md5 = hashlib.md5(pw.encode("ascii")).hexdigest().upper()
    out = sql("INSERT INTO Account_Info (cAccName,cPassword,cSecPassword,iClientID) VALUES ('%s','%s','%s',0); "
              "INSERT INTO Account_Habitus (cAccName,iFlag,dBeginDate,dEndDate,iLeftSecond,nExtPoint,iClientID) "
              "VALUES ('%s',0,'2026-11-19','2027-11-19',31000000,0,0)" % (tk, md5, md5, tk))
    if sql("SET NOCOUNT ON; SELECT COUNT(*) FROM Account_Habitus h JOIN Account_Info i ON i.cAccName=h.cAccName WHERE h.cAccName='%s'" % tk).split()[-1:] != ["1"]:
        sys.exit("INSERT khong thanh cong: " + out.replace(md5, "<md5>").strip()[-200:])
    SECRETS.mkdir(parents=True, exist_ok=True)
    (SECRETS / (tk + ".txt")).write_text(pw, "utf8")
    print(tk, "da tao (Account_Info + Account_Habitus 1 nam) | mat khau o", SECRETS / (tk + ".txt"))


def xoa_tk(tk):
    if not TK.fullmatch(tk) or not (SECRETS / (tk + ".txt")).exists():
        sys.exit("chi xoa tk do tao-tk-test tao (co file bi mat)")
    print(sql("DELETE FROM Account_Habitus WHERE cAccName='%s'; DELETE FROM Account_Info WHERE cAccName='%s'" % (tk, tk)).strip()[-80:])
    (SECRETS / (tk + ".txt")).unlink()


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
    elif cmd == "do-gs":
        n = int(a[1]) if len(a) > 1 and a[1].isdigit() else 10
        print(goi(BLOCKS["do-gs"] % {"n": max(1, min(n, 60))}))
    elif cmd == "ten-co":
        if len(a) < 2 or not re.fullmatch(r"[A-Za-z0-9]{3,24}", a[1]):
            sys.exit("ten-co <Ten ASCII 3-24>")
        print(a[1], goi(BLOCKS["ten-co"] % {"name": a[1]}))
    elif cmd == "tao-tk-test" and len(a) > 1:
        tao_tk(a[1])
    elif cmd == "xoa-tk-test" and len(a) > 1:
        xoa_tk(a[1])
    else:
        sys.exit("lenh khong co trong danh sach: " + cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
