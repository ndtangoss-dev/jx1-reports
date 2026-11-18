# NGUOI GAC (#107.4, LUAT-COT-LOI L2): chay moi 10 phut bang Task Scheduler, KHONG ton token khi phien con song.
# 1) sinh lai STATE/TIEN-DO.md  2) neu im lang >30 phut (khong commit, TRANG-THAI khong doi) hoac co thu [KHAN] chua xu ly
#    -> goi lai phien Claude Code (claude -c -p) bao doc LUAT-COT-LOI va hom thu.  3) tieu yeu chet (.done exit!=0): chay lai toi da 2 lan, cho tang dan 10 phut roi 30 phut.
# Khoa: D:\JX-wt\guard\goi.lock (het han sau 40 phut) tranh goi trung.
# TAT NGUOI GAC:  schtasks /Change /TN JX-Guard /DISABLE      BAT LAI: /ENABLE      GO HAN: schtasks /Delete /TN JX-Guard /F
$ErrorActionPreference = 'Continue'
$ops   = 'D:\jx1-ops-wt\JX1_OPS'
$repo  = 'D:\jx1-ops-wt'
$gdir  = 'D:\JX-wt\guard'
New-Item -ItemType Directory -Force $gdir | Out-Null
$log = Join-Path $gdir 'guard.log'
function Log($m) { Add-Content $log ("{0} {1}" -f (Get-Date -f 'yyyy-MM-dd HH:mm:ss'), $m) }

python -I "$ops\TOOLS\tien_do.py" 2>$null

# --- im lang? ---
$lastCommit = [DateTime]::Parse((git -C $repo log -1 --format=%cI))
$tt = (Get-Item "$ops\STATE\TRANG-THAI.md").LastWriteTime
$last = @($lastCommit, $tt) | Sort-Object -Descending | Select-Object -First 1
$silentMin = ((Get-Date) - $last).TotalMinutes
$khan = $false
$cho = Join-Path $ops 'HOP-THU\CHO-SONNET.md'
if (Test-Path $cho) {
  $s = Get-Content -Raw -Encoding UTF8 $cho
  $a = $s.IndexOf('## Chưa xử lý'); $b = $s.IndexOf('## Đã xử lý')
  if ($a -ge 0) { $sec = if ($b -gt $a) { $s.Substring($a, $b - $a) } else { $s.Substring($a) }; if ($sec -match '(?m)^## #\d+.*\[KHẨN\]') { $khan = $true } }
}
$lock = Join-Path $gdir 'goi.lock'
$lockOk = -not (Test-Path $lock) -or (((Get-Date) - (Get-Item $lock).LastWriteTime).TotalMinutes -gt 40)
if (($silentMin -gt 30 -or $khan) -and $lockOk) {
  Set-Content $lock (Get-Date -f o)
  Log ("goi phien: im lang {0:N0} phut, khan={1}" -f $silentMin, $khan)
  $prompt = 'Người gác: đọc JX1_OPS/STATE/LUAT-COT-LOI.md và hòm thư HOP-THU/CHO-SONNET.md rồi làm tiếp. Ghi một dòng trạng thái vào STATE/TRANG-THAI.md, commit và push jx1-ops.'
  Push-Location 'C:\Jx1CocoV3'
  Start-Process -WindowStyle Hidden -FilePath 'claude' -ArgumentList @('-c', '-p', $prompt, '--permission-mode', 'acceptEdits') -RedirectStandardOutput (Join-Path $gdir 'goi.out') -RedirectStandardError (Join-Path $gdir 'goi.err') | Out-Null
  Pop-Location
}

# --- tieu yeu chet: chay lai toi da 2 lan ---
$waits = @(10, 30)
Get-ChildItem 'D:\JX-wt' -Filter '*.done' -ErrorAction SilentlyContinue | ForEach-Object {
  $id = $_.BaseName
  $t = (Get-Content -Raw $_.FullName) -replace '[^\x20-\x7E]', ''
  if ($t -match 'exit=0') { return }
  $cf = Join-Path $gdir "$id.lan"
  $n = if (Test-Path $cf) { [int](Get-Content $cf) } else { 0 }
  if ($n -ge 2) { return }
  if (((Get-Date) - $_.LastWriteTime).TotalMinutes -lt $waits[$n]) { return }
  Set-Content $cf ($n + 1)
  Remove-Item $_.FullName -ErrorAction SilentlyContinue
  Push-Location $ops
  powershell -NoProfile -File TOOLS\chay_codex.ps1 -Id $id | Out-Null
  Pop-Location
  Log "chay lai $id lan $($n + 1)"
}
