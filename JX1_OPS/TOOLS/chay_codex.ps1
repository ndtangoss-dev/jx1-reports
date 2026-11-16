# Chay mot worker Codex TACH KHOI phien Claude Code (dong phien / cham han muc van khong chet).
# Ly do: shell cua Claude Code nam trong mot Job Object, tien trinh con (Start-Process) cung nam trong job do [da do bang IsProcessInJob];
# co bi giet khi dong phien hay khong thi CHUA kiem. Task Scheduler chay tien trinh trong job rieng cua no, khong gan voi phien.
# Dung: chay_codex.ps1 -Id 0-11 [-PromptFile D:\JX-wt\0-11.prompt.txt] [-Codex <duong dan codex.exe>]
# Mac dinh: -C D:\JX-wt\<Id> --sandbox workspace-write, log ra D:\JX-wt\<Id>.codex.log, co the dong dung de worker ghi 'xong' vao file task.
param([Parameter(Mandatory)][string]$Id, [string]$PromptFile, [string]$Codex = 'C:\Users\PC\.codex\.sandbox-bin\codex.exe')
$ErrorActionPreference = 'Stop'
$wt = "D:\JX-wt\$Id"
if (-not (Test-Path $wt)) { throw "Khong co worktree $wt" }
if (-not $PromptFile) { $PromptFile = "$wt.prompt.txt" }
if (-not (Test-Path $PromptFile)) { throw "Khong co prompt $PromptFile" }
$log = "$wt.codex.log"
$run = "$wt.run.ps1"
@"
Get-Content -Raw -Encoding UTF8 '$PromptFile' | & '$Codex' exec -C '$wt' --sandbox workspace-write - *> '$log'
Set-Content -Encoding UTF8 '$wt.done' ('exit=' + `$LASTEXITCODE + ' ' + (Get-Date -Format s))
"@ | Set-Content -Encoding UTF8 $run
Remove-Item "$wt.done" -ErrorAction SilentlyContinue
$n = "JX-codex-$Id"
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$run`""
$s = New-ScheduledTaskSettingsSet -ExecutionTimeLimit ([TimeSpan]::Zero) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName $n -Action $a -Settings $s -Force | Out-Null
Start-ScheduledTask $n
"Da giao ${Id}: task $n; log $log; xong khi co $wt.done. Don task sau khi xong: Unregister-ScheduledTask $n -Confirm:`$false"
