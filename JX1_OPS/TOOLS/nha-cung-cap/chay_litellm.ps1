# CHUA CHAY (#172: chi chuan bi). Chay lop chuyen o 127.0.0.1:4000, khoa doc tu D:\JX-keys\gemini.txt.
# Cai (mot lan, trong venv rieng, khong dung python he thong):  python -m venv D:\JX-keys\venv ; D:\JX-keys\venv\Scripts\pip install "litellm[proxy]"
$ErrorActionPreference = 'Stop'
$kf = 'D:\JX-keys\gemini.txt'
if (-not (Test-Path $kf)) { throw 'Chua co khoa: chu chay nhap_khoa.bat truoc.' }
$env:GEMINI_API_KEY = (Get-Content -Raw $kf).Trim()
& 'D:\JX-keys\venv\Scripts\litellm.exe' --config "$PSScriptRoot\litellm_gemini.yaml" --host 127.0.0.1 --port 4000
