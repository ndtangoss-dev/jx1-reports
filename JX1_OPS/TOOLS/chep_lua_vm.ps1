# Chép chuẩn Lua/dữ liệu lên VM Test-36 (LUAT v2 điều 9). Dùng: powershell -File chep_lua_vm.ps1 -Nguon <file trong kho> -Dich <đường dẫn trên VM> [-NapNong]
# Làm: SHA nguồn / VM trước / VM sau, .bak-<giờ>, Select-String dòng hàm chính, nhắc chạy lại menu sách trên LD.
param([Parameter(Mandatory)][string]$Nguon, [Parameter(Mandatory)][string]$Dich, [string]$HamChinh = 'qhbv_menu', [string]$VM = '192.168.56.150')
. C:\Jx1CocoV3\docs-analysis\scripts\jxlab_cred.ps1
if ($VM -ne '192.168.56.150') { throw 'Chi Test-36 (192.168.56.150)' }
$sha0 = (Get-FileHash $Nguon -Algorithm SHA256).Hash
$cred = Get-JxCred
if (-not $cred) { throw '[KET-GO] Get-JxCred rong: khong goi Get-Credential, khong xin mat khau' }
$s = New-PSSession -ComputerName $VM -Credential $cred
$bak = $Dich + '.bak-' + (Get-Date -Format 'HHmmss')
$truoc = Invoke-Command -Session $s -ScriptBlock { param($d,$b) $h = (Get-FileHash $d).Hash; Copy-Item $d $b -Force; $h } -ArgumentList $Dich,$bak
Copy-Item $Nguon -Destination $Dich -ToSession $s -Force
$sau = Invoke-Command -Session $s -ScriptBlock { param($d) (Get-FileHash $d).Hash } -ArgumentList $Dich
Invoke-Command -Session $s -ScriptBlock { param($d,$h) Select-String -Path $d -Pattern $h -Context 0,2 | Out-String } -ArgumentList $Dich,$HamChinh
Remove-PSSession $s
"nguon : $sha0"; "VM truoc: $truoc (bak: $bak)"; "VM sau : $sau"
if ($sha0 -ne $sau) { Write-Error 'SHA KHONG KHOP - chep loi' } else { 'SHA khop.' }
'NHAC: nap nong (menu qhbv_reload) roi mo sach Ho tro tren LD, tap 1 muc cu + 1 muc moi truoc khi bao xong.'
