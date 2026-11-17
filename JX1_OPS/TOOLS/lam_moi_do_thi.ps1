# Làm mới đồ thị Graphify (AST, không LLM, không gửi mã ra ngoài) cho client bản A và server src18, rồi ghi STATE/DO-THI.md.
# Chạy: powershell -NoProfile -File TOOLS\lam_moi_do_thi.ps1   (khoảng 2-3 phút; nên chạy sau mỗi lần gộp mã / trước khi build APK)
$g = 'D:\JX-tools\graphify-venv\Scripts\graphify.exe'
$roots = @(@{n='client bản A'; p='D:\JX-build\qh9A\Classes'}, @{n='server src18'; p='D:\JX-build\src18'})
$out = @("# TRẠNG THÁI ĐỒ THỊ GRAPHIFY", "", "Ghi tự động bởi TOOLS/lam_moi_do_thi.ps1 lúc $(Get-Date -Format 'yyyy-MM-dd HH:mm'). Đồ thị cũ hơn mã thì chạy lại script trước khi tra.", "", "| Gốc | Đường dẫn | Đồ thị lúc | Mã mới nhất lúc | Trạng thái |", "|---|---|---|---|---|")
foreach ($r in $roots) {
  Push-Location $r.p
  & $g update . *> $null
  Pop-Location
  $gj = Get-Item (Join-Path $r.p 'graphify-out\graph.json')
  $newest = Get-ChildItem $r.p -Recurse -Include *.cpp,*.h,*.c,*.lua -File -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
  $st = if ($newest.LastWriteTime -gt $gj.LastWriteTime) { 'CŨ hơn mã' } else { 'mới' }
  $out += "| $($r.n) | $($r.p) | $($gj.LastWriteTime.ToString('MM-dd HH:mm')) | $($newest.LastWriteTime.ToString('MM-dd HH:mm')) ($($newest.Name)) | $st |"
}
$out | Set-Content -Encoding UTF8 (Join-Path $PSScriptRoot '..\STATE\DO-THI.md')
