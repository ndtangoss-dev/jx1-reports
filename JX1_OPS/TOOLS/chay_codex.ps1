# Chay mot worker Codex TACH KHOI phien Claude Code (dong phien / cham han muc van khong chet).
# Ly do: shell cua Claude Code nam trong mot Job Object, tien trinh con (Start-Process) cung nam trong job do [da do bang IsProcessInJob];
# co bi giet khi dong phien hay khong thi CHUA kiem. Task Scheduler chay tien trinh trong job rieng cua no, khong gan voi phien.
# Dung: chay_codex.ps1 -Id 0-11 [-PromptFile D:\JX-wt\0-11.prompt.txt] [-Codex <duong dan codex.exe>] [-Model gpt-6.1-sol]
# Model CO DINH gpt-6.1-sol (Sol Max, Q-12) + reasoning max, goi giong Dispatcher cu / 0-03 (xem ENVIRONMENT.md). Khong dung model mac dinh gpt-6-luna cua config.toml (xingchi tra 404).
param([Parameter(Mandatory)][string]$Id, [string]$PromptFile, [string]$Codex = 'C:\Users\PC\AppData\Local\OpenAI\Codex\bin\b6c7fc9497179c98\codex.exe', [string]$Model = 'gpt-6.1-sol', [string]$Effort = 'max')
$ErrorActionPreference = 'Stop'
$wt = "D:\JX-wt\$Id"
if (-not (Test-Path $wt)) { throw "Khong co worktree $wt" }
if (-not $PromptFile) { $PromptFile = "$wt.prompt.txt" }
if (-not (Test-Path $PromptFile)) { throw "Khong co prompt $PromptFile" }
$log = "$wt.codex.log"
# Git cua worktree nam ngoai thu muc lam viec (vd D:\jx1-reports\.git): cho phep ghi de worker commit duoc.
$gd = (Get-Content "$wt\.git" -ErrorAction SilentlyContinue | Select-Object -First 1) -replace '^gitdir:\s*',''
$addDir = ''
if ($gd -and $env:JX_CODEX_ADDDIR) { $common = Split-Path (Split-Path $gd -Parent) -Parent; if (Test-Path $common) { $addDir = " --add-dir '$common'" } }
$run = "$wt.run.ps1"
# Khoa rieng cho worker (JX_CODEX_KEY=<ten>): doc luc chay tu C:\Users\PC\.jx1keys\<ten>.txt, KHONG ghi gia tri vao script/log. Khong dat = dung khoa mac dinh trong config.toml.
$keyCfg = ''; $keyLine = ''
if ($env:JX_CODEX_KEY) {
  if (-not (Test-Path "C:\Users\PC\.jx1keys\$($env:JX_CODEX_KEY).txt")) { throw "Khong co khoa $($env:JX_CODEX_KEY)" }
  $keyLine = "`$k = (Get-Content -Raw 'C:\Users\PC\.jx1keys\$($env:JX_CODEX_KEY).txt').Trim()"
  $keyCfg = " --config `"model_providers.xingchi.experimental_bearer_token=```"`$k```"`""
}
@"
`$env:CODEX_HOME = 'C:\Users\PC\.codex'; `$env:PYTHONUTF8 = '1'
$keyLine
Get-Content -Raw -Encoding UTF8 '$PromptFile' | & '$Codex' exec --json --sandbox workspace-write --model '$Model' --config 'model_provider="xingchi"' --config 'model_reasoning_effort="$Effort"' --config 'approval_policy="never"'$keyCfg -C '$wt'$addDir - *> '$log'
Set-Content -Encoding UTF8 '$wt.done' ('exit=' + `$LASTEXITCODE + ' ' + (Get-Date -Format s))
"@ | Set-Content -Encoding UTF8 $run
Remove-Item "$wt.done" -ErrorAction SilentlyContinue
$n = "JX-codex-$Id"
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$run`""
$s = New-ScheduledTaskSettingsSet -ExecutionTimeLimit ([TimeSpan]::Zero) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName $n -Action $a -Settings $s -Force | Out-Null
Start-ScheduledTask $n
python -I "$PSScriptRoot\set_status.py" $Id running 2>$null | Out-Null   # #109: dat status=running khi giao
"Da giao ${Id}: task $n; model $Model; log $log; xong khi co $wt.done. Don task sau khi xong: Unregister-ScheduledTask $n -Confirm:`$false"



