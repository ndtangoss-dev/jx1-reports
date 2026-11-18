# CHUA CHAY. Bo so sanh xingchi vs Gemini: cung mot viec doc, worktree nhap. Dung khi Chat bao "chu duyet Gemini mien phi".
# Dung: .\so_sanh.ps1 -Provider gemini|xingchi -Tasks R-06a,R-07a,K-03a -Parallel 1|2|4|7
param([ValidateSet('gemini','xingchi')][string]$Provider='gemini',[string[]]$Tasks=@('R-06a','R-07a','K-03a'),[int]$Parallel=1)
$ErrorActionPreference='Stop'
$out="D:\JX-wt\so-sanh\$Provider-p$Parallel-$(Get-Date -f HHmmss)"; New-Item -ItemType Directory -Force $out | Out-Null
$codex='C:\Users\PC\AppData\Local\OpenAI\Codex\bin\b6c7fc9497179c98\codex.exe'
$rows=@(); $jobs=@()
foreach($i in 1..$Parallel){ foreach($t in $Tasks){
  $wt="D:\JX-wt\so-sanh\nhap-$Provider-$t-$i"
  if(-not (Test-Path $wt)){ git -C D:\jx1-ops-wt worktree add -f --detach $wt origin/jx1-ops | Out-Null }
  $prompt="D:\JX-wt\$t.prompt.txt"; if(-not (Test-Path $prompt)){ continue }
  $jobs += Start-Job -ArgumentList $Provider,$t,$i,$wt,$prompt,$out,$codex -ScriptBlock {
    param($p,$t,$i,$wt,$prompt,$out,$codex)
    $sw=[Diagnostics.Stopwatch]::StartNew(); $log="$out\$t-$i.log"
    if($p -eq 'gemini'){ $env:CODEX_HOME='D:\JX-keys\codex-home-gemini'; $env:LITELLM_LOCAL_KEY=(Get-Content 'D:\JX-keys\litellm_master.txt').Trim()
      Get-Content -Raw -Encoding UTF8 $prompt | & $codex exec --json --sandbox workspace-write --config 'approval_policy="never"' -C $wt - *> $log }
    else { $env:CODEX_HOME='C:\Users\PC\.codex'; $k=(Get-Content -Raw 'C:\Users\PC\.jx1keys\JX-K4.txt').Trim()
      Get-Content -Raw -Encoding UTF8 $prompt | & $codex exec --json --sandbox workspace-write --model 'gpt-6.1-sol' --config 'model_provider="xingchi"' --config 'approval_policy="never"' --config "model_providers.xingchi.experimental_bearer_token=`"$k`"" -C $wt - *> $log }
    [pscustomobject]@{task=$t;n=$i;exit=$LASTEXITCODE;giay=[int]$sw.Elapsed.TotalSeconds;http429=(Select-String -Path $log -Pattern '429' -SimpleMatch -ErrorAction SilentlyContinue).Count;loi=(Select-String -Path $log -Pattern 'turn.failed' -SimpleMatch -ErrorAction SilentlyContinue).Count;bytes_log=(Get-Item $log).Length}
  }}}
$jobs | Wait-Job | Receive-Job | Export-Csv "$out\ketqua.csv" -NoTypeInformation -Encoding UTF8
Write-Host "Xong: $out\ketqua.csv  (so sanh do day bao cao voi REPORTS da gop bang tay)"
