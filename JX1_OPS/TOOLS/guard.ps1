# NGUOI GAC (#107.4, sua theo #111/#112): chay moi 5 phut bang Task Scheduler, KHONG ton token khi phien con song.
# 1) sinh lai STATE/TIEN-DO.md  2) neu im lang >30 phut hoac co thu [KHAN] CHUA XAC NHAN -> goi lai phien Claude Code (claude -c -p)
#    3) tieu yeu chet (.done exit!=0): chay lai toi da 2 lan, cho 10 roi 30 phut.
# KHOA THEO TIEN TRINH: goi.lock giu PID cua claude da goi. Con song -> dang thuc; da thoat -> mo khoa ngay.
#   Tran an toan 15 phut: con chay >15 phut ma khong ghi gi vao kho (khong commit moi) -> kill, goi lai o lan sau.
# [KHAN] chua xac nhan (TU-SONNET.md chua co dong "Nhan #N") bo qua khoa.
# KHONG goi khi phien tuong tac dang giua luot (file jsonl phien o C:\Users\PC\.claude\projects\C--Jx1CocoV3 vua ghi <90 giay).
# TAT NGUOI GAC:  schtasks /Change /TN JX-Guard /DISABLE      BAT LAI: /ENABLE      GO HAN: schtasks /Delete /TN JX-Guard /F
$ErrorActionPreference = 'Continue'
$q = [char]34
$env:GIT_TERMINAL_PROMPT = '0'; $env:GCM_INTERACTIVE = 'never'   # #125
[Console]::OutputEncoding = [Text.Encoding]::UTF8   # git show tra UTF-8
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

$fp = Start-Process -WindowStyle Hidden -PassThru -FilePath git -ArgumentList ('-C ' + $q + $repo + $q + ' fetch -q origin jx1-ops'); if (-not $fp.WaitForExit(120000)) { Stop-Process -Id $fp.Id -Force -EA SilentlyContinue; Log 'git fetch qua 120 giay, bo qua (#125)' }   # #119: doc hom thu tu ban moi nhat tren remote, khong tu worktree cu
# --- [KHAN] chua xac nhan: co trong "Chua xu ly" cua CHO-SONNET va TU-SONNET chua co "Nhan #N" ---
$khan = $false
$cho = Join-Path $ops 'HOP-THU\CHO-SONNET.md'
$tu  = Join-Path $ops 'HOP-THU\TU-SONNET.md'
if ($true) {
  $s = (git -C $repo show 'origin/jx1-ops:JX1_OPS/HOP-THU/CHO-SONNET.md') -join "`n"
  if ($true) {
    $sec = $s   # #119: Chat them thu o CUOI file (sau "Da xu ly"), nen quet ca file; chi tinh thu so >= 110
    $tus = (git -C $repo show 'origin/jx1-ops:JX1_OPS/HOP-THU/TU-SONNET.md') -join "`n"
    foreach ($m in [regex]::Matches($sec, '(?m)^## #(\d+).*\[KHẨN\]')) {
      if ([int]$m.Groups[1].Value -ge 110 -and $tus -notmatch ('Nhận #' + $m.Groups[1].Value + '\b')) { $khan = $true }
    }
  }
}


# --- #122: lan goi truoc loi dang nhap / het han muc -> bao [CAN-CHU] vao TU-SONNET (toi da 1 lan/30 phut) ---
$ge = Join-Path $gdir 'goi.err'; $go = Join-Path $gdir 'goi.out'
$gtxt = ''
foreach ($f in @($ge, $go)) { if (Test-Path $f) { $gtxt += (Get-Content $f -Raw -ErrorAction SilentlyContinue) } }
if ($gtxt -match '(?i)401|login|usage limit|rate limit|weekly limit|hit your') {
  $stamp = Join-Path $gdir 'canchu.stamp'
  if (-not (Test-Path $stamp) -or ((Get-Date) - (Get-Item $stamp).LastWriteTime).TotalMinutes -gt 30) {
    $line = "`n[CAN-CHU] Claude Code chua dang nhap / het han muc luc {0} (nguoi gac: {1})" -f (Get-Date -f 'HH:mm'), (($gtxt -replace '\s+',' ').Trim().Substring(0, [Math]::Min(120, ($gtxt -replace '\s+',' ').Trim().Length)))
    Add-Content -Path (Join-Path $ops 'HOP-THU\TU-SONNET.md') -Value $line -Encoding UTF8
    Set-Content $stamp 'x'
    Log 'ghi [CAN-CHU] het han muc / dang nhap'
    git -C $repo add -- 'JX1_OPS/HOP-THU/TU-SONNET.md' 2>$null
    git -C $repo commit -qm 'Nguoi gac: CAN-CHU dang nhap/han muc' -- 'JX1_OPS/HOP-THU/TU-SONNET.md' 2>$null
    $pp = Start-Process -WindowStyle Hidden -PassThru -FilePath git -ArgumentList ('-C ' + $q + $repo + $q + ' push -q origin HEAD:jx1-ops')
    if (-not $pp.WaitForExit(120000)) { Stop-Process -Id $pp.Id -Force -EA SilentlyContinue; Log 'git push qua 120 giay (#125)' }
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
if ($jl -and ((Get-Date) - $jl.LastWriteTime).TotalSeconds -lt 120) { $live = $true }

if ($env:GUARD_FAKE_KHAN -eq '1') { $khan = $true; $live = $false }
Log ("chay: im {0:N0} phut, khan={1}, busy={2}, live={3}" -f $silentMin, $khan, $busy, $live)
if (($silentMin -gt 30 -or $khan) -and ($khan -or -not $busy) -and -not $live) {
  Log ("goi phien: im lang {0:N0} phut, khan={1}" -f $silentMin, $khan)
  $prompt = 'Người gác: đọc JX1_OPS/STATE/LUAT-COT-LOI.md và hòm thư HOP-THU/CHO-SONNET.md rồi làm tiếp. Ghi một dòng trạng thái vào STATE/TRANG-THAI.md, commit và push jx1-ops.'
  Push-Location 'C:\Jx1CocoV3'
  $tools = 'Bash(git:*) Bash(python TOOLS/*) Bash(powershell -File TOOLS/*) PowerShell(git:*) PowerShell(python TOOLS/*) PowerShell(powershell -File TOOLS/*)'
  $argStr = '-c -p ' + $q + $prompt + $q + ' --permission-mode acceptEdits --allowedTools ' + $q + $tools + $q   # #126: PS 5.1 khong tu bao dau nhay quanh arg co dau cach
  if ($env:GUARD_DRY -eq '1') { Log ('DRY: claude ' + $argStr); $proc = $null }
  else { $proc = Start-Process -WindowStyle Hidden -PassThru -FilePath 'claude' -ArgumentList $argStr -RedirectStandardOutput (Join-Path $gdir 'goi.out') -RedirectStandardError (Join-Path $gdir 'goi.err') }
  Pop-Location
  if ($proc) { Set-Content $lock ("{0} {1}" -f $proc.Id, (Get-Date -f o)) }
} elseif ($live -and ($silentMin -gt 30 -or $khan)) { Log 'phien tuong tac dang giua luot, khong goi' }

# --- #118.6: guard khong chay lai tieu yeu nua; chi bat lai Tong quan neu no chet ---
$tq = Get-ScheduledTaskInfo -TaskName 'JX-TongQuan' -ErrorAction SilentlyContinue
if (-not $tq) { Log 'JX-TongQuan chua dang ky' }
elseif (((Get-Date) - $tq.LastRunTime).TotalMinutes -gt 10) { Start-ScheduledTask -TaskName 'JX-TongQuan'; Log 'bat lai JX-TongQuan (qua 10 phut chua chay)' }
