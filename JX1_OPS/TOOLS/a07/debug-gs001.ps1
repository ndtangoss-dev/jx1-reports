[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][ValidateSet('JX-Test-36')][string]$VmName,
    [Parameter(Mandatory=$true)][string]$ExePath,
    [Parameter(Mandatory=$true)][string]$SymbolPath,
    [Parameter(Mandatory=$true)][string]$CdbPath,
    [string]$CaptureRoot = 'D:\JX-build\a07\captures',
    [Parameter(Mandatory=$true)][switch]$IsolationAndDefenderChecked,
    [string[]]$ProgramArguments = @()
)
$ErrorActionPreference = 'Stop'
$machine = Get-CimInstance Win32_ComputerSystem
if (($machine.Manufacturer+' '+$machine.Model) -notmatch 'VirtualBox|innotek') { throw 'Khong phai guest VirtualBox. CAM chay exe server tren may that.' }
if (-not $IsolationAndDefenderChecked) { throw 'Can co bang chung mang co lap, Defender va log/audit trong VM theo task.' }
if (-not (Test-Path -LiteralPath $ExePath -PathType Leaf)) { throw 'Khong tim thay gs001.exe.' }
if ([IO.Path]::GetFileName($ExePath) -ne 'gs001.exe') { throw 'Script chi danh cho gs001.exe.' }
if (-not (Test-Path -LiteralPath $CdbPath -PathType Leaf)) { throw 'Can duong dan cdb.exe x64 cua Debugging Tools.' }
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$session = Join-Path $CaptureRoot $stamp
# Giu command-file cdb don gian: duong dan capture khong co ky tu command/quote/khoang trang.
if ($session -notmatch '^[A-Za-z]:\\[A-Za-z0-9_\\.:-]+$') { throw 'CaptureRoot chi duoc dung duong dan Windows khong khoang trang/ky tu lenh.' }
New-Item -ItemType Directory -Path $session -Force | Out-Null
Get-ChildItem -LiteralPath (Split-Path -Parent $ExePath) -File | Where-Object Extension -in '.exe','.dll','.pdb' | Get-FileHash -Algorithm SHA256 | Export-Csv -NoTypeInformation -LiteralPath (Join-Path $session 'hashes.csv')
$dump = Join-Path $session 'first-av.dmp'
$commands = @('.lines -e',
    ('sxe -c ".exr -1;.ecxr;r;kv;lm;!analyze -v;.dump /ma '+$dump+'" av'),
    '.echo A-07: first-chance AV se luu dump va dung cho lenh; khong tu continue.',
    'g')
$commandFile = Join-Path $session 'capture.cdb'
$commands | Set-Content -LiteralPath $commandFile -Encoding ASCII
Push-Location -LiteralPath (Split-Path -Parent $ExePath)
try {
    # Khong .symfix: dung PDB local, khong tu ket noi symbol server/Internet.
    & $CdbPath '-lines' '-y' $SymbolPath '-logo' (Join-Path $session 'cdb.log') '-cf' $commandFile $ExePath @ProgramArguments
    Write-Host "cdb exit=$LASTEXITCODE; bang chung local: $session"
} finally { Pop-Location }
