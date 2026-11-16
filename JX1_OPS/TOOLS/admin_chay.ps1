# admin_chay.ps1 - PM kich hoat viec Admin da dang ky bang setup_quyen_admin.ps1 (Q-28), khong can UAC.
# Dung: admin_chay.ps1 -Job firewall -Json '{"action":"add","port":8080,"remote":"192.168.56.150","tag":"cdn"}'
#       admin_chay.ps1 -Job kill-test-vm -Json '{"vm":"JX-Test-36"}'
param([Parameter(Mandatory)][ValidateSet('kill-test-vm', 'firewall', 'trustedhosts', 'service')][string]$Job, [Parameter(Mandatory)][string]$Json, [int]$WaitSec = 60, [string]$Base = 'C:\ProgramData\JX1_ADMIN')
$ErrorActionPreference = 'Stop'
$o = $Json | ConvertFrom-Json
$id = 'r' + (Get-Date -Format 'HHmmssfff')
$o | Add-Member -NotePropertyName id -NotePropertyValue $id -Force
$res = Join-Path $Base "log\$Job.result.json"
Remove-Item $res -ErrorAction SilentlyContinue
($o | ConvertTo-Json -Compress) | Set-Content -Path (Join-Path $Base "req\$Job.json") -Encoding UTF8
& schtasks.exe /run /tn "JX1-ADMIN-$Job" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "schtasks /run loi (chua chay setup_quyen_admin.ps1?)" }
$t = [Diagnostics.Stopwatch]::StartNew()
while ($t.Elapsed.TotalSeconds -lt $WaitSec) {
    if (Test-Path $res) { $r = Get-Content -Raw -Encoding UTF8 $res | ConvertFrom-Json; if ($r.id -eq $id) { $r | Format-List | Out-String; if (-not $r.ok) { exit 1 }; return } }
    Start-Sleep -Milliseconds 500
}
throw "het $WaitSec s chua co ket qua cho $id"
