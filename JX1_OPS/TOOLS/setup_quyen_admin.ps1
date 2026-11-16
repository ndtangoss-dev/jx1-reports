# setup_quyen_admin.ps1 - CHU MAY CHAY ADMIN DUNG 1 LAN (Q-28). Hoan tac: setup_quyen_admin.ps1 -Remove
# Lam gi: (1) tao C:\ProgramData\JX1_ADMIN (chi Admin/SYSTEM ghi; ban chi doc script va ghi thu muc req); (2) ghi bo thuc thi jx1_admin_runner.ps1 + config\allowed.json
# (chi giu ban cu neu da co); (3) dang ky 4 scheduled task JX1-ADMIN-{kill-test-vm,firewall,trustedhosts,service} chay SYSTEM/Highest, va cho tai khoan cua ban quyen chay (schtasks /run) khong can UAC.
# Moi viec: danh sach co dinh, tham so kiem chat theo allowed.json, khong the diet Main VM JX-Server-D, ghi log o C:\ProgramData\JX1_ADMIN\log.
param([switch]$Remove, [string]$UserName = ($env:USERDOMAIN + '\' + $env:USERNAME), [string]$Base = 'C:\ProgramData\JX1_ADMIN')
$ErrorActionPreference = 'Stop'
$id = [Security.Principal.WindowsIdentity]::GetCurrent()
if (-not (New-Object Security.Principal.WindowsPrincipal $id).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    throw 'Can chay PowerShell bang Run as administrator.'
}
$jobs = 'kill-test-vm', 'firewall', 'trustedhosts', 'service'

if ($Remove) {
    foreach ($j in $jobs) { Unregister-ScheduledTask -TaskName "JX1-ADMIN-$j" -Confirm:$false -ErrorAction SilentlyContinue }
    & netsh advfirewall firewall show rule name=all | Select-String '^[^:]+:\s+(JX1-AUTO-\S+)\s*$' | ForEach-Object { & netsh advfirewall firewall delete rule name="$($_.Matches[0].Groups[1].Value)" | Out-Null }
    Write-Host "Da go 4 task va cac luat JX1-AUTO-*. Thu muc $Base giu lai (xoa tay neu muon)."
    return
}

$sid = (New-Object Security.Principal.NTAccount($UserName)).Translate([Security.Principal.SecurityIdentifier]).Value
# Chong gai-san: neu thu muc da ton tai tu truoc (co the do tai khoan thuong tao), khong tin ACL/chu so huu/lien ket cu.
$ps = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
if (Test-Path $Base) {
    $it = Get-Item $Base -Force
    if ($it.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "$Base la lien ket/junction, dung lai. Xoa no (Admin) roi chay lai." }
    & takeown.exe /F $Base /R /D Y | Out-Null
    & icacls $Base /setowner '*S-1-5-32-544' /T /C | Out-Null
    & icacls $Base /reset /T /C | Out-Null
    # xoa moi lien ket con sot ben trong
    Get-ChildItem $Base -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint } | ForEach-Object { throw "Co lien ket trong ${Base}: $($_.FullName). Xoa roi chay lai." }
}
foreach ($d in 'bin', 'config', 'req', 'log') { New-Item -ItemType Directory -Force -Path (Join-Path $Base $d) | Out-Null }
# Quyen: SYSTEM + Administrators toan quyen, chu so huu Administrators; nguoi dung chi doc/chay, rieng req\ duoc ghi (khong co quyen doi ACL)
& icacls $Base /setowner '*S-1-5-32-544' /T /C | Out-Null
& icacls $Base /inheritance:r /grant:r '*S-1-5-18:(OI)(CI)F' '*S-1-5-32-544:(OI)(CI)F' "*${sid}:(OI)(CI)RX" | Out-Null
& icacls (Join-Path $Base 'req') /grant:r "*${sid}:(OI)(CI)M" | Out-Null

$runner = Join-Path $Base 'bin\jx1_admin_runner.ps1'
$code = @'
# jx1_admin_runner.ps1 - bo thuc thi viec Admin co gioi han (Q-28). Chay boi scheduled task JX1-ADMIN-<job> (SYSTEM, Highest).
# Tep nay nam trong C:\ProgramData\JX1_ADMIN\bin (chi Administrators/SYSTEM ghi duoc). Yeu cau (req\<job>.json) la DU LIEU KHONG TIN CAY:
# moi truong deu duoc kiem chat theo danh sach trong config\allowed.json (chi Admin sua). Khong co tham so tu do, khong chay lenh tu yeu cau.
# Ket qua: log\<job>.result.json va log\admin.log. -DryRun: kiem tra tham so, khong thay doi he thong (dung de thu khong can Admin).
param(
    [Parameter(Mandatory)][ValidateSet('kill-test-vm', 'firewall', 'trustedhosts', 'service')][string]$Job,
    [switch]$DryRun,
    [string]$Base = 'C:\ProgramData\JX1_ADMIN'
)
$ErrorActionPreference = 'Stop'
$VBM = 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'
$VBDIR = 'C:\Program Files\Oracle\VirtualBox'
$reqId = ''

function Log([string]$m) {
    $line = '{0} [{1}] id={2} {3}' -f (Get-Date -Format 's'), $Job, $reqId, $m
    try { Add-Content -Path (Join-Path $Base 'log\admin.log') -Value $line -Encoding UTF8 } catch {}
}
function Finish([bool]$ok, [string]$msg) {
    Log ('{0}: {1}' -f $(if ($ok) { 'OK' } else { 'TU CHOI/LOI' }), $msg)
    $o = [ordered]@{ id = $reqId; job = $Job; ok = $ok; dryrun = [bool]$DryRun; msg = $msg; time = (Get-Date -Format 's') }
    try { ($o | ConvertTo-Json -Compress) | Set-Content -Path (Join-Path $Base ('log\' + $Job + '.result.json')) -Encoding UTF8 } catch {}
    exit $(if ($ok) { 0 } else { 1 })
}
function Fail([string]$m) { Finish $false $m }

try {
    $cfgPath = Join-Path $Base 'config\allowed.json'
    if (-not (Test-Path $cfgPath)) { Fail 'thieu config\allowed.json' }
    $cfg = Get-Content -Raw -Encoding UTF8 $cfgPath | ConvertFrom-Json

    $reqPath = Join-Path $Base ('req\' + $Job + '.json')
    if (-not (Test-Path $reqPath)) { Fail 'khong co yeu cau' }
    # Doc DUNG MOT LAN, khoa doc quyen (FileShare None), toi da 4097 byte, tu choi lien ket (reparse point); roi xoa. Khong kiem-roi-doc tach doi nen khong the bi doi tep giua chung.
    if ((Get-Item $reqPath -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { Remove-Item $reqPath -Force; Fail 'yeu cau la lien ket (reparse point)' }
    $fs = $null
    try {
        $fs = [IO.File]::Open($reqPath, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::None)
        $buf = New-Object byte[] 4097
        $n = $fs.Read($buf, 0, 4097)
    }
    finally { if ($fs) { $fs.Dispose() } }
    Remove-Item $reqPath -Force   # doc mot lan, khong cho chay lai yeu cau cu
    if ($n -gt 4096) { Fail 'yeu cau qua lon' }
    $raw = [Text.Encoding]::UTF8.GetString($buf, 0, $n)
    try { $req = $raw | ConvertFrom-Json } catch { Fail 'yeu cau khong phai JSON' }
    if ($req.id -isnot [string] -or $req.id -notmatch '^[A-Za-z0-9_-]{1,40}$') { Fail 'id yeu cau khong hop le' }
    $reqId = $req.id

    switch ($Job) {

        'kill-test-vm' {
            $vm = [string]$req.vm
            if ($vm -ieq [string]$cfg.mainvm) { Fail ('TU CHOI: ' + $vm + ' la Main VM, khong bao gio diet') }
            if ($vm -cne [string]$cfg.testvm) { Fail ('chi chap nhan VM ' + $cfg.testvm + ', nhan: ' + $vm) }
            if (-not (Test-Path $VBM)) { Fail 'khong thay VBoxManage' }
            function Get-VmPid([string]$name) {
                $info = & $VBM showvminfo $name --machinereadable 2>$null
                $lf = ($info | Where-Object { $_ -like 'LogFldr=*' } | Select-Object -First 1)
                if (-not $lf) { return $null }
                $dir = ($lf -replace '^LogFldr="', '' -replace '"$', '') -replace '\\\\', '\'
                $log = Join-Path $dir 'VBox.log'
                if (-not (Test-Path $log)) { return $null }
                $m = Select-String -Path $log -Pattern 'Process ID:\s+(\d+)' | Select-Object -First 1
                if ($m) { return [int]$m.Matches[0].Groups[1].Value } else { return $null }
            }
            $targetPid = Get-VmPid $cfg.testvm
            if (-not $targetPid) { Fail ('khong xac dinh duoc PID cua ' + $cfg.testvm + ' tu VBox.log') }
            $mainPid = Get-VmPid $cfg.mainvm
            if ($mainPid -and $mainPid -eq $targetPid) { Fail ('TU CHOI: PID ' + $targetPid + ' trung PID Main VM') }
            $p = Get-Process -Id $targetPid -ErrorAction SilentlyContinue
            if (-not $p) { Finish $true ('tien trinh ' + $targetPid + ' khong con') }
            if ($p.ProcessName -ne 'VBoxHeadless' -or -not $p.Path -or -not $p.Path.StartsWith($VBDIR, [StringComparison]::OrdinalIgnoreCase)) {
                Fail ('PID ' + $targetPid + ' khong phai VBoxHeadless cua VirtualBox (' + $p.ProcessName + ')')
            }
            if ($DryRun) { Finish $true ('DRYRUN: se diet VBoxHeadless PID ' + $targetPid + ' (VM ' + $cfg.testvm + '); Main PID ' + $mainPid) }
            Stop-Process -Id $targetPid -Force
            $dead = $p.WaitForExit(15000)
            Finish $dead ('da diet VBoxHeadless PID ' + $targetPid + ' (VM ' + $cfg.testvm + '); thoat=' + $dead)
        }

        'firewall' {
            $action = [string]$req.action
            if ($action -notin 'add', 'remove', 'remove-all') { Fail 'action phai la add, remove hoac remove-all' }
            if ($action -eq 'remove-all') {
                $names = @(& netsh advfirewall firewall show rule name=all | Select-String '^[^:]+:\s+(JX1-AUTO-\S+)\s*$' | ForEach-Object { $_.Matches[0].Groups[1].Value.Trim() })
                if ($DryRun) { Finish $true ('DRYRUN: se xoa ' + $names.Count + ' luat JX1-AUTO-*') }
                foreach ($n in $names) { & netsh advfirewall firewall delete rule name="$n" | Out-Null }
                Finish $true ('da xoa ' + $names.Count + ' luat JX1-AUTO-*')
            }
            $port = 0
            if (-not [int]::TryParse([string]$req.port, [ref]$port) -or $port -notin @($cfg.ports | ForEach-Object { [int]$_ })) { Fail ('cong khong nam trong danh sach cho phep: ' + $req.port) }
            $remote = [string]$req.remote
            $ip = $null
            if (-not [Net.IPAddress]::TryParse($remote, [ref]$ip) -or $remote -notin @($cfg.ips)) { Fail ('dia chi khong nam trong danh sach cho phep: ' + $remote) }
            $tag = [string]$req.tag
            if ($tag -notmatch '^[a-z0-9]{1,16}$') { Fail 'tag phai la a-z0-9, toi da 16 ky tu' }
            $name = 'JX1-AUTO-{0}-{1}-{2}' -f $tag, $port, ($remote -replace '[^0-9a-fA-F]', '_')
            if ($DryRun) { Finish $true ('DRYRUN: ' + $action + ' luat ' + $name + ' TCP ' + $port + ' tu ' + $remote) }
            if ($action -eq 'add') {
                & netsh advfirewall firewall delete rule name="$name" 2>&1 | Out-Null
                $out = & netsh advfirewall firewall add rule name="$name" dir=in action=allow protocol=TCP localport=$port remoteip=$remote profile=any
                if ($LASTEXITCODE -ne 0) { Fail ('netsh loi: ' + ($out -join ' ')) }
                Finish $true ('da them luat ' + $name)
            }
            else {
                $out = & netsh advfirewall firewall delete rule name="$name"
                Finish ($LASTEXITCODE -eq 0) ('xoa luat ' + $name + ': ' + (($out | Select-Object -First 1) -join ''))
            }
        }

        'trustedhosts' {
            $action = [string]$req.action
            if ($action -notin 'add', 'remove') { Fail 'action phai la add hoac remove' }
            $h = [string]$req.host
            $ip = $null
            if ($h -eq '*' -or -not [Net.IPAddress]::TryParse($h, [ref]$ip) -or $h -notin @($cfg.trustedhosts)) { Fail ('host khong nam trong danh sach cho phep: ' + $h) }
            $cur = [string](Get-Item WSMan:\localhost\Client\TrustedHosts).Value
            $list = @($cur -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
            if ($action -eq 'add') { if ($h -notin $list) { $list += $h } } else { $list = @($list | Where-Object { $_ -ne $h }) }
            $new = $list -join ','
            if ($DryRun) { Finish $true ('DRYRUN: TrustedHosts se la "' + $new + '"') }
            Set-Item WSMan:\localhost\Client\TrustedHosts -Value $new -Force
            Finish $true ('TrustedHosts = "' + $new + '"')
        }

        'service' {
            $action = [string]$req.action
            if ($action -notin 'start', 'enable-manual', 'enable-auto') { Fail 'action phai la start, enable-manual hoac enable-auto (khong co stop/disable)' }
            $svc = [string]$req.name
            if ($svc -notin @($cfg.services)) { Fail ('dich vu khong nam trong danh sach cho phep: ' + $svc) }
            if (-not (Get-Service -Name $svc -ErrorAction SilentlyContinue)) { Fail ('khong co dich vu ' + $svc) }
            if ($DryRun) { Finish $true ('DRYRUN: ' + $action + ' ' + $svc) }
            $msg = @()
            if ($action -eq 'enable-manual') { $msg += (& sc.exe config $svc start= demand) -join ' ' }
            if ($action -eq 'enable-auto') { $msg += (& sc.exe config $svc start= auto) -join ' ' }
            $s = Get-Service -Name $svc
            if ($s.Status -ne 'Running') { try { Start-Service -Name $svc; $msg += 'da start' } catch { $msg += ('start loi: ' + $_.Exception.Message) } }
            $s = Get-Service -Name $svc
            Finish ($s.Status -eq 'Running') ($svc + ' = ' + $s.Status + '; ' + ($msg -join ' | '))
        }
    }
}
catch {
    Finish $false ('ngoai le: ' + $_.Exception.Message)
}
'@
Set-Content -Path $runner -Value $code -Encoding UTF8   # ban chep nam trong ProgramData (Admin-only); tac vu chi chay ban nay, khong doc tu repo/worktree

$cfgPath = Join-Path $Base 'config\allowed.json'
if (-not (Test-Path $cfgPath)) {
    $cfg = [ordered]@{
        testvm       = 'JX-Test-36'
        mainvm       = 'JX-Server-D'
        ips          = @('192.168.1.50', '192.168.56.150', '192.168.56.1')
        ports        = @(56722, 51189, 8080, 8091, 8092)
        trustedhosts = @('192.168.1.50', '192.168.56.150')
        services     = @('WinRM', 'DoSvc', 'BITS', 'wuauserv', 'InstallService', 'Tailscale')
    }
    $cfg | ConvertTo-Json | Set-Content -Path $cfgPath -Encoding UTF8
}

$sddl = "D:(A;;FA;;;SY)(A;;FA;;;BA)(A;;GRGX;;;$sid)"
$svcCom = New-Object -ComObject 'Schedule.Service'; $svcCom.Connect()
foreach ($j in $jobs) {
    $n = "JX1-ADMIN-$j"
    $a = New-ScheduledTaskAction -Execute $ps -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$runner`" -Job $j"
    $p = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest
    $s = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 5) -MultipleInstances IgnoreNew -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    Register-ScheduledTask -TaskName $n -Action $a -Principal $p -Settings $s -Force | Out-Null
    $svcCom.GetFolder('\').GetTask($n).SetSecurityDescriptor($sddl, 0)
    Write-Host "Da dang ky $n"
}
Write-Host ('Quyen thu muc: ' + ((& icacls $Base) -join ' | '))
Write-Host ('allowed.json hien hanh (kiem lai): ' + (Get-Content -Raw $cfgPath))
$h = (Get-FileHash $runner -Algorithm SHA256).Hash
Write-Host "Xong. SHA256 bo thuc thi: $h"
Write-Host "Sua danh sach cho phep (IP, cong, dich vu) tai $cfgPath (can Admin). Thu: schtasks /run /tn JX1-ADMIN-service (can req\service.json)."
