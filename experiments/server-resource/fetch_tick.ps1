# Lay cac dong tick (SvrFPS) cua gs001 tu log console TRONG guest va gan epoch uoc tinh.
# epoch(dong) ~= epoch_doc - (GameLoop_cuoi - GameLoop)/36 ; sai so <= 60 s (log in 1 dong/phut).
param([pscredential]$Cred,[string]$Guest,[string]$Out)
$r=Invoke-Command -ComputerName $Guest -Credential $Cred -ScriptBlock {
  $l=Get-Content C:\JX\dbgout\T4c-console.txt | ? { $_ -match 'SvrFPS' }
  [pscustomobject]@{epoch=[DateTimeOffset]::UtcNow.ToUnixTimeSeconds(); lines=$l} }
# GameLoop dat lai khi sang ngay (Time=Nd): chi dung cac dong sau lan dat lai cuoi cung
$gl=@($r.lines | % { [long](([regex]'GameLoop=\s*(\d+)').Match($_).Groups[1].Value) }); $k=0; for($i=1;$i -lt $gl.Count;$i++){ if($gl[$i] -lt $gl[$i-1]){ $k=$i } }; $r.lines=@($r.lines[$k..($r.lines.Count-1)])
$last=[int](([regex]'GameLoop=\s*(\d+)').Match($r.lines[-1]).Groups[1].Value)
$r.lines | % { $g=[int](([regex]'GameLoop=\s*(\d+)').Match($_).Groups[1].Value); "$([int]($r.epoch - ($last-$g)/36)) $_" } | Set-Content $Out -Encoding utf8
"tick lines: $($r.lines.Count) -> $Out"

