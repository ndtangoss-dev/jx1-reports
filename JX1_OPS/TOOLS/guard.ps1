# NGUOI GAC (#107.4, sua theo #111/#112): chay moi 5 phut bang Task Scheduler, KHONG ton token khi phien con song.
# 1) sinh lai STATE/TIEN-DO.md  2) neu im lang >30 phut hoac co thu [KHAN] CHUA XAC NHAN -> goi lai phien Claude Code (claude -c -p)
#    3) tieu yeu chet (.done exit!=0): chay lai toi da 2 lan, cho 10 roi 30 phut.
# KHOA THEO TIEN TRINH: goi.lock giu PID cua claude da goi. Con song -> dang thuc; da thoat -> mo khoa ngay.
#   Tran an toan 15 phut: con chay >15 phut ma khong ghi gi vao kho (khong commit moi) -> kill, goi lai o lan sau.
# [KHAN] chua xac nhan (TU-SONNET.md chua co dong "Nhan #N") bo qua khoa.
# KHONG goi khi phien tuong tac dang giua luot (file jsonl phien o C:\Users\PC\.claude\projects\C--Jx1CocoV3 vua ghi <90 giay).
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

# --- [KHAN] chua xac nhan: co trong "Chua xu ly" cua CHO-SONNET va TU-SONNET chua co "Nhan #N" ---
$khan = $false
$cho = Join-Path $ops 'HOP-THU\CHO-SONNET.md'
$tu  = Join-Path $ops 'HOP-THU\TU-SONNET.md'
if (Test-Path $cho) {
  $s = Get-Content -Raw -Encoding UTF8 $cho
  $a = $s.IndexOf('## Chưa xử lý'); $b = $s.IndexOf('## Đã xử lý')
  if ($a -ge 0) {
    $sec = if ($b -gt $a) { $s.Substring($a, $b - $a) } else { $s.Substring($a) }
    $tus = if (Test-Path $tu) { Get-Content -Raw -Encoding UTF8 $tu } else { '' }
    foreach ($m in [regex]::Matches($sec, '(?m)^## #(\d+).*\[KHẨN\]')) {
      if ($tus -notmatch ('Nhận #' + $m.Groups[1].Value + '\b')) { $khan = $true }
    }
  }
}

# --- khoa theo tien trinh ---
$lock = Join-Path $gdir 'goi.lock'
$busy = $false
if (Test-Path $lock) {
  $parts = (Get-Content $lock -ErrorAction SilentlyContinue) -split '\s+'
  $lpid = 0; [void][int]::TryParse($parts[0], [ref]$lpid)
  $p = if ($lpid -gt 0) { Get-Process -Id $lpid -ErrorAction SilentlyContinue } else { $null }
  if ($p -and $p.ProcessName -match 'claude|node') {
    $age = ((Get-Date) - $p.StartTime).TotalMinutes
    $wrote = ([DateTime]::Parse((git -C $repo log -1 --format=%cI))) -gt $p.StartTime
    if ($age -gt 15 -and -not $wrote) {
      Stop-Process -Id $lpid -Force -ErrorAction SilentlyContinue
      Remove-Item $lock -ErrorAction SilentlyContinue
      Log "kill phien goi (pid $lpid) chay $([int]$age) phut khong ghi vao kho"
    } else { $busy = $true }
  } else { Remove-Item $lock -ErrorAction SilentlyContinue }
}

# --- phien tuong tac dang giua luot? ---
$live = $false
$jl = Get-ChildItem 'C:\Users\PC\.claude\projects\C--Jx1CocoV3' -Filter '*.jsonl' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($jl -and ((Get-Date) - $jl.LastWriteTime).TotalSeconds -lt 90) { $live = $true }

if (($silentMin -gt 30 -or $khan) -and ($khan -or -not $busy) -and -not $live) {
  Log ("goi phien: im lang {0:N0} phut, khan={1}" -f $silentMin, $khan)
  $prompt = 'Người gác: đọc JX1_OPS/STATE/LUAT-COT-LOI.md và hòm thư HOP-THU/CHO-SONNET.md rồi làm tiếp. Ghi một dòng trạng thái vào STATE/TRANG-THAI.md, commit và push jx1-ops.'
  Push-Location 'C:\Jx1CocoV3'
  $proc = Start-Process -WindowStyle Hidden -PassThru -FilePath 'claude' -ArgumentList @('-c', '-p', $prompt, '--permission-mode', 'acceptEdits') -RedirectStandardOutput (Join-Path $gdir 'goi.out') -RedirectStandardError (Join-Path $gdir 'goi.err')
  Pop-Location
  if ($proc) { Set-Content $lock ("{0} {1}" -f $proc.Id, (Get-Date -f o)) }
} elseif ($live -and ($silentMin -gt 30 -or $khan)) { Log 'phien tuong tac dang giua luot, khong goi' }

# --- tieu yeu chet: chay lai toi da 2 lan ---
$waits = @(10, 30)
Get-ChildItem 'D:\JX-wt' -Filter '*.done' -ErrorAction SilentlyContinue | ForEach-Object {
  $id = $_.BaseName
  $t = (Get-Content -Raw $_.FullName) -replace '[^\x20-\x7E]', ''
  if ($t -match 'exit=0') { return }
  $cf = Join-Path $gdir "$id.lan"
  $n = if (Test-Path $cf) { [int](Get-Content $cf) } else { 0 }
  if ($n -ge 2) { python -I "$ops\TOOLS\set_status.py" $id failed "chet $($n + 1) lan, guard bo" 2>$null | Out-Null; return }
  if (((Get-Date) - $_.LastWriteTime).TotalMinutes -lt $waits[$n]) { return }
  Set-Content $cf ($n + 1)
  Remove-Item $_.FullName -ErrorAction SilentlyContinue
  Push-Location $ops
  powershell -NoProfile -File TOOLS\chay_codex.ps1 -Id $id | Out-Null
  Pop-Location
  Log "chay lai $id lan $($n + 1)"
  # #109: danh dau running trong TASKS/<id>.md
  python -I "$ops\TOOLS\set_status.py" $id running 2>$null
}
