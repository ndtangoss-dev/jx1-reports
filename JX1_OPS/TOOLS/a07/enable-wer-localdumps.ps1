[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][ValidateSet('JX-Test-36')][string]$VmName,
    [string]$StateRoot = 'D:\JX-build\a07\wer-state',
    [string]$DumpRoot = 'D:\JX-build\a07\dumps',
    [switch]$Disable
)
$ErrorActionPreference = 'Stop'
if (-not [Environment]::Is64BitProcess) { throw 'Can PowerShell x64 de backup/restore dung registry view.' }
# Ten VM VirtualBox khong nhat thiet la COMPUTERNAME cua guest.
$machine = Get-CimInstance Win32_ComputerSystem
if (($machine.Manufacturer+' '+$machine.Model) -notmatch 'VirtualBox|innotek') { throw 'Khong phai guest VirtualBox. Cam thay doi WER tren may that.' }
$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw 'Can PowerShell Admin TRONG VM thu.' }
$key = 'HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\gs001.exe'
$nativeKey = 'HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\gs001.exe'
$state = Join-Path $StateRoot 'before.clixml'
$backup = Join-Path $StateRoot 'before.reg'
$restored = Join-Path $StateRoot 'restored.txt'
if ($Disable) {
    if (-not (Test-Path -LiteralPath $state)) { throw 'Khong co backup A-07; khong tu xoa key.' }
    if (Test-Path -LiteralPath $restored) { throw 'Da hoan tac; khong thay doi lan nua.' }
    $previous = Import-Clixml -LiteralPath $state
    & reg.exe delete $nativeKey /f /reg:64
    if ($LASTEXITCODE -ne 0 -and (Test-Path -LiteralPath $key)) { throw 'Khong xoa duoc key A-07 de restore.' }
    if ($previous.Existed) {
        & reg.exe import $backup /reg:64
        if ($LASTEXITCODE -ne 0) { throw "Restore loi; giu backup tai $backup va xu ly trong VM." }
    }
    'Restored' | Set-Content -LiteralPath $restored
    Write-Host 'Da restore key WER truoc A-07. Dump/backup van duoc giu.'
    return
}
if (Test-Path -LiteralPath $state) { throw 'Da co backup/checkpoint. Khong ghi de; dung -Disable de hoan tac.' }
New-Item -ItemType Directory -Path $StateRoot,$DumpRoot -Force | Out-Null
$existed = Test-Path -LiteralPath $key
if ($existed) {
    & reg.exe export $nativeKey $backup /y
    if ($LASTEXITCODE -ne 0) { throw 'Backup WER that bai; chua thay doi key.' }
}
[pscustomobject]@{Existed=$existed;Vm=$VmName} | Export-Clixml -LiteralPath $state
New-Item -Path $key -Force | Out-Null
New-ItemProperty -Path $key -Name DumpFolder -PropertyType ExpandString -Value $DumpRoot -Force | Out-Null
New-ItemProperty -Path $key -Name DumpCount -PropertyType DWord -Value 10 -Force | Out-Null
New-ItemProperty -Path $key -Name DumpType -PropertyType DWord -Value 2 -Force | Out-Null
Write-Host "Da bat WER full dump trong $VmName. Hoan tac: cung tham so va -Disable. Khong dua dump vao Git."
