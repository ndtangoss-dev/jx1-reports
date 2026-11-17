# B-04a: draft collector; PM runs only inside the approved test VM.
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][ValidateRange(1,2147483647)][int]$TargetPid,
    [Parameter(Mandatory=$true)][string]$OutputDirectory,
    [ValidateRange(360,3600)][int]$DurationSeconds = 660,
    [Parameter(Mandatory=$true)][switch]$ApprovedTestVm
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if (-not $ApprovedTestVm) { throw 'Only run inside the approved test VM.' }
# This acknowledgement is not VM detection and does not authorize server startup.
$target = Get-Process -Id $TargetPid
if ($target.ProcessName -notmatch '^gs001(?:_nohe)?$') { throw 'Target must be gs001/gs001_nohe.' }
$started = $target.StartTime.ToUniversalTime()
$cores = [Environment]::ProcessorCount
$baseline = $target.TotalProcessorTime.TotalSeconds
$dir = New-Item -ItemType Directory -Path $OutputDirectory -ErrorAction Stop
$csvPath = Join-Path $dir.FullName 'cpu.csv'
$metaPath = Join-Path $dir.FullName 'cpu-meta.json'
$clock = [Diagnostics.Stopwatch]::StartNew()
$previous = 0.0
$state = 'PARTIAL'
$writer = $null
try {
    $writer = [IO.StreamWriter]::new($csvPath, $false, [Text.UTF8Encoding]::new($false))
    $writer.WriteLine('elapsed_s,interval_s,cpu_percent')
    while ($clock.Elapsed.TotalSeconds -lt $DurationSeconds) {
        Start-Sleep -Milliseconds 1000
        $target.Refresh()
        if ($target.HasExited -or $target.StartTime.ToUniversalTime() -ne $started) {
            throw 'Target exited/restarted. Discard this run; do not join across PID lifetimes.'
        }
        $nowCpu = $target.TotalProcessorTime.TotalSeconds
        $now = $clock.Elapsed.TotalSeconds
        $interval = $now - $previous
        $percent = 100.0 * ($nowCpu - $baseline) / ($interval * $cores)
        if ($percent -lt 0 -or $percent -gt 100.01) { throw 'Invalid CPU counter delta.' }
        $culture = [Globalization.CultureInfo]::InvariantCulture
        $writer.WriteLine(('{0},{1},{2}' -f $now.ToString('F6',$culture),
            $interval.ToString('F6',$culture), $percent.ToString('F6',$culture)))
        $writer.Flush()
        $previous = $now
        $baseline = $nowCpu
    }
    $state = 'COMPLETE'
} finally {
    $clock.Stop()
    if ($null -ne $writer) { $writer.Dispose() }
    [ordered]@{
        status=$state; pid=$TargetPid; process_start_utc=$started.ToString('o')
        logical_processors=$cores; duration_s=$clock.Elapsed.TotalSeconds
        cpu_basis='process CPU / wall seconds / VM logical processors * 100'
    } | ConvertTo-Json | Set-Content -LiteralPath $metaPath -Encoding UTF8
    $target.Dispose()
}
