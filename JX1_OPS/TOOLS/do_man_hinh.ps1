# CHI DOC: do 15 phut xem vi sao man hinh khong tat. Khong doi cai dat, khong kill, khong gui phim/chuot.
# Chay bang PowerShell Admin KHI CHU KHONG DUNG MAY:  powershell -ExecutionPolicy Bypass -File <duong dan>\do_man_hinh.ps1
# Hoan tac: khong can (chi ghi file CSV). Dung som: Ctrl+C. Ket qua: JX1_OPS\out\man-hinh-do.csv
param([int]$Phut = 15, [int]$Giay = 15)
Add-Type @'
using System;using System.Runtime.InteropServices;using System.Text;
public class MhDo{
[StructLayout(LayoutKind.Sequential)]struct LII{public uint cb;public uint t;}
[DllImport("user32.dll")]static extern bool GetLastInputInfo(ref LII p);
[DllImport("user32.dll")]static extern IntPtr GetForegroundWindow();
[DllImport("user32.dll")]static extern int GetWindowText(IntPtr h,StringBuilder s,int n);
[DllImport("user32.dll")]static extern uint GetWindowThreadProcessId(IntPtr h,out uint pid);
public static double IdleS(){var l=new LII();l.cb=8;GetLastInputInfo(ref l);return ((uint)Environment.TickCount-l.t)/1000.0;}
public static string Fg(){IntPtr h=GetForegroundWindow();var sb=new StringBuilder(200);GetWindowText(h,sb,200);uint pid;GetWindowThreadProcessId(h,out pid);return pid+"|"+sb.ToString();}}
'@
$out = Join-Path (Split-Path $PSScriptRoot -Parent) 'out'
New-Item -ItemType Directory -Force $out | Out-Null
$f = Join-Path $out 'man-hinh-do.csv'
"gio,nhan_roi_s,pid_cuasotruoc,tieude_cuasotruoc,exe_cuasotruoc,DISPLAY_requests" | Out-File $f -Encoding utf8
$den = (Get-Date).AddMinutes($Phut)
while ((Get-Date) -lt $den) {
  $fg = [MhDo]::Fg(); $p = $fg.Split('|')[0]; $t = ($fg.Substring($fg.IndexOf('|')+1)) -replace '[",\r\n]',' '
  $exe = ''; try { $exe = (Get-Process -Id ([int]$p) -EA Stop).ProcessName } catch {}
  $req = ''
  try { $txt = (powercfg /requests) -join "`n"
        if ($txt -match '(?s)DISPLAY:\s*(.*?)\n\s*\nSYSTEM') { $req = ($Matches[1] -replace '\s+',' ').Trim() } } catch {}
  ('{0},{1:N1},{2},"{3}",{4},"{5}"' -f (Get-Date -Format 'HH:mm:ss'), [MhDo]::IdleS(), $p, $t, $exe, $req) | Out-File $f -Append -Encoding utf8
  Start-Sleep -Seconds $Giay
}
