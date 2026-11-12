# Phase 48 - Thu thap tai nguyen BEN TRONG guest VM thu (khong do Host).
# Chay tren may Host, lenh do chay trong guest qua WinRM (Invoke-Command). Chi doc bo dem hieu nang san co
# cua Windows (Get-Counter) va bang ket noi TCP; khong cai phan mem, khong doi cau hinh/dich vu.
# Dung: .\collect_guest_metrics.ps1 -Milestone A -Seconds 600 -Cred <PSCredential> -Guest <ip/host> -OutDir <thu muc>
param([string]$Milestone='A',[int]$Seconds=600,[pscredential]$Cred,[string]$Guest,[string]$OutDir='.')
$ErrorActionPreference='Stop'
$procs='gs001','Bishop','Goddess','Sword3PaySys','sqlservr','wsmprovhost'
$ctr=@('\Processor(_Total)\% Processor Time','\Processor(*)\% Processor Time','\Processor(_Total)\% User Time','\Processor(_Total)\% Privileged Time','\Processor(_Total)\% Interrupt Time','\Processor(_Total)\% DPC Time','\Process(_Total)\% Processor Time','\Process(Idle)\% Processor Time','\Memory\Available MBytes','\Memory\Committed Bytes',
 '\Memory\Cache Bytes','\Memory\Pages/sec','\Memory\Page Faults/sec','\Paging File(_Total)\% Usage','\System\Processor Queue Length',
 '\Network Interface(*)\Bytes Received/sec','\Network Interface(*)\Bytes Sent/sec','\Network Interface(*)\Packets Received/sec','\Network Interface(*)\Packets Sent/sec')
foreach($p in $procs){ $ctr+="\Process($p)\% Processor Time","\Process($p)\Working Set","\Process($p)\Private Bytes","\Process($p)\Thread Count","\Process($p)\Handle Count" }
$t0=[DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
# Luong 2: dem ket noi moi 5 s (gs001 cong 51189, Bishop 56722)
$conn=Start-Job -ArgumentList $Guest,$Cred,$Seconds -ScriptBlock { param($g,$c,$s)
  Invoke-Command -ComputerName $g -Credential $c -ArgumentList $s -ScriptBlock { param($s)
    $end=(Get-Date).AddSeconds($s); while((Get-Date) -lt $end){
      $gid=(Get-Process gs001 -ea 0).Id
      $e=Get-NetTCPConnection -State Established -ea 0
      [pscustomobject]@{epoch=[DateTimeOffset]::UtcNow.ToUnixTimeSeconds(); gs_players=($e|?{$_.OwningProcess -eq $gid -and $_.LocalPort -eq 51189}|measure).Count;
        bishop_clients=($e|?{$_.LocalPort -eq 56722}|measure).Count; gs_all=($e|?{$_.OwningProcess -eq $gid}|measure).Count }
      Start-Sleep 5 } } }
# Luong 1: bo dem hieu nang 1 s
$rows=Invoke-Command -ComputerName $Guest -Credential $Cred -ArgumentList ($ctr -join ";"),$Seconds -ScriptBlock { param($ctrs,$s) $ctr=[string[]]($ctrs -split ";")
  Get-Counter -Counter $ctr -SampleInterval 1 -MaxSamples $s -ErrorAction SilentlyContinue | % {
    $o=[ordered]@{ epoch=[DateTimeOffset]::new($_.Timestamp).ToUnixTimeSeconds() }
    foreach($c in $_.CounterSamples){ $o[$c.Path -replace '^\\\\[^\\]+\\','' -replace '\s+','_']=[math]::Round($c.CookedValue,3) }
    [pscustomobject]$o } }
$cn=Receive-Job $conn -Wait -AutoRemoveJob
New-Item -ItemType Directory -Force $OutDir | Out-Null
$rows | select * -ExcludeProperty PSComputerName,RunspaceId,PSShowComputerName | Export-Csv "$OutDir\phase48-raw-$Milestone.csv" -NoTypeInformation -Encoding UTF8
$cn | select epoch,gs_players,bishop_clients,gs_all | Export-Csv "$OutDir\phase48-conn-$Milestone.csv" -NoTypeInformation -Encoding UTF8
"milestone=$Milestone start=$t0 samples=$(@($rows).Count) expected=$Seconds conn_samples=$(@($cn).Count)"



