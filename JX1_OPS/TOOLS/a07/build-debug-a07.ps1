[CmdletBinding()]
param(
    [string]$Source = 'C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver',
    [string]$BuildRoot = 'D:\JX-build\a07',
    [string]$MsBuild = 'C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe',
    [string]$IobShimObject
)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath($BuildRoot).TrimEnd('\')
$sourceRoot = (Resolve-Path -LiteralPath $Source).Path.TrimEnd('\')
if ($root -ne 'D:\JX-build\a07') { throw 'BuildRoot phai la D:\JX-build\a07 theo task.' }
if (-not (Test-Path -LiteralPath $MsBuild -PathType Leaf)) { throw "Khong tim thay MSBuild: $MsBuild" }
if (Test-Path -LiteralPath $root) { throw 'BuildRoot da ton tai: giu nguyen checkpoint, khong ghi de. Xem log truoc khi resume thu cong.' }
if ($IobShimObject -and -not (Test-Path -LiteralPath $IobShimObject -PathType Leaf)) { throw 'Khong tim thay IobShimObject.' }

$copy = Join-Path $root 'src\gameserver'
$out = Join-Path $root 'out'
$logs = Join-Path $root 'logs'
New-Item -ItemType Directory -Path $copy,$out,$logs -Force | Out-Null
# Chi copy source/resource/import library can cho Common va GameServer; khong copy runtime/du lieu.
$directories = @('Sources\MultiServer\Common','Sources\MultiServer\GameServer',
    'Sources\MultiServer\Rainbow\Interface','Sources\MultiServer\Heaven\Interface',
    'Sources\Core\Src','Sources\Engine\Src','Sources\Engine\Include','Headers','Lib\release','roledbserver')
foreach ($relative in $directories) {
    $from = Join-Path $sourceRoot $relative
    if (-not (Test-Path -LiteralPath $from)) { continue }
    $to = Join-Path $copy $relative
    & robocopy.exe $from $to '*.h' '*.hpp' '*.inl' '*.inc' '*.cpp' '*.c' '*.rc' '*.ico' '*.vcxproj' '*.lib' '*.def' /E /XJ /R:0 /W:0 /NFL /NDL /NJH /NJS /NP /XD Debug Release x64 ipch graphify-out
    if ($LASTEXITCODE -ge 8) { throw "Copy that bai ($LASTEXITCODE): $relative" }
}
$shimCopy = $null
if ($IobShimObject) {
    $shimCopy = Join-Path $out 'iob_shim.obj'
    Copy-Item -LiteralPath $IobShimObject -Destination $shimCopy
    Get-FileHash -LiteralPath $shimCopy -Algorithm SHA256 | Format-List | Out-File (Join-Path $logs 'shim-hash.txt')
}
function Set-NodeValue($document,$parent,[string]$name,[string]$value) {
    $node = $parent.ChildNodes | Where-Object LocalName -eq $name | Select-Object -First 1
    if (-not $node) { $node = $document.CreateElement($name,$document.DocumentElement.NamespaceURI); [void]$parent.AppendChild($node) }
    $node.InnerText = $value
}
$commands = Join-Path $logs 'commands.txt'
foreach ($name in @('Common','GameServer')) {
    $project = Join-Path $copy "Sources\MultiServer\$name\$name.vcxproj"
    if (-not (Test-Path -LiteralPath $project)) { throw "Thieu project: $project" }
    Copy-Item -LiteralPath $project -Destination ($project + '.a07-original')
    $xml = New-Object System.Xml.XmlDocument
    $xml.Load($project)
    $ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
    $ns.AddNamespace('m',$xml.DocumentElement.NamespaceURI)
    # Override metadata trong ban copy: MSBuild property AdditionalOptions khong du de ep co C++.
    foreach ($group in $xml.SelectNodes('//m:ItemDefinitionGroup',$ns)) {
        $cl = $group.SelectSingleNode('m:ClCompile',$ns)
        if (-not $cl) { continue }
        foreach ($pair in @(@('Optimization','Disabled'),@('DebugInformationFormat','ProgramDatabase'),
            @('BasicRuntimeChecks','EnableFastChecks'),@('RuntimeLibrary','MultiThreaded'),
            @('InlineFunctionExpansion','Disabled'),@('WholeProgramOptimization','false'),
            @('ObjectFileName','$(IntDir)'),@('ProgramDataBaseFileName','$(IntDir)compiler.pdb'),
            @('PrecompiledHeaderOutputFile',('$(IntDir)'+$name+'.pch')),
            @('AssemblerOutput','NoListing'),
            @('AdditionalOptions','/Zc:sizedDealloc- /Zc:strictStrings- /source-charset:.936 /execution-charset:.936 /showIncludes /GL-'))) {
            Set-NodeValue $xml $cl $pair[0] $pair[1]
        }
        $link = $group.SelectSingleNode('m:Link',$ns)
        if ($link) {
            $deps = (Join-Path $out 'Common.lib')+';'+(Join-Path $copy 'Lib\release\engine.lib')+';'+(Join-Path $copy 'Lib\release\CoreServer.lib')+';'+(Join-Path $copy 'Sources\MultiServer\GameServer\ms64.lib')+';Netapi32.lib;Ws2_32.lib;odbc32.lib;odbccp32.lib;legacy_stdio_definitions.lib'
            if ($shimCopy) { $deps += ';'+$shimCopy }
            foreach ($pair in @(@('OutputFile',(Join-Path $out 'gs001.exe')),@('GenerateDebugInformation','true'),
                @('ProgramDatabaseFile',(Join-Path $out 'gs001.pdb')),@('GenerateMapFile','true'),
                @('MapFileName',(Join-Path $out 'gs001.map')),@('EnableCOMDATFolding','false'),
                @('OptimizeReferences','false'),@('LinkTimeCodeGeneration','Default'),
                @('AdditionalDependencies',$deps),@('AdditionalLibraryDirectories',(Join-Path $copy 'Lib\release')),
                @('AdditionalOptions','/DEBUG:FULL /INCREMENTAL:NO'))) {
                Set-NodeValue $xml $link $pair[0] $pair[1]
            }
        }
        $lib = $group.SelectSingleNode('m:Lib',$ns)
        if ($lib) { Set-NodeValue $xml $lib 'OutputFile' (Join-Path $out 'Common.lib') }
    }
    foreach ($node in $xml.SelectNodes('//m:PostBuildEvent/m:Command',$ns)) { $node.InnerText = '' }
    $xml.Save($project)
    $int = Join-Path $root "obj\$name\"
    $log = Join-Path $logs "$name-debug.log"
    $arguments = @($project,'/t:Rebuild','/m:1','/nologo','/v:minimal',
        '/p:Configuration=Debug','/p:Platform=x64','/p:PlatformToolset=v143',
        '/p:WindowsTargetPlatformVersion=10.0.19041.0',"/p:OutDir=$out\", "/p:IntDir=$int",
        '/p:BuildProjectReferences=false',"/flp:logfile=$log;verbosity=diagnostic")
    ('"'+$MsBuild+'" '+(($arguments | ForEach-Object {'"'+$_+'"'}) -join ' ')) | Add-Content -LiteralPath $commands
    & $MsBuild @arguments
    if ($LASTEXITCODE -ne 0) { throw "MSBuild $name that bai ($LASTEXITCODE). Giu checkpoint; xem $log. Khong tu chay binary." }
}
if (-not (Test-Path -LiteralPath (Join-Path $out 'gs001.pdb'))) { throw 'Khong co gs001.pdb; chua dat tieu chi symbol.' }
Get-FileHash -LiteralPath (Join-Path $out 'gs001.exe'),(Join-Path $out 'gs001.pdb') -Algorithm SHA256 | Format-List | Out-File (Join-Path $logs 'artifacts-hash.txt')
Write-Host "Da dung Common + gs001 Debug x64 /MT /Od /Zi /RTC1 va /DEBUG:FULL. Chua chay exe; log: $logs"
