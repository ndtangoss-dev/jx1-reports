# CHUA CHAY. Tao CODEX_HOME rieng cho Gemini; KHONG dung vao C:\Users\PC\.codex (xingchi).
$h = 'D:\JX-keys\codex-home-gemini'
New-Item -ItemType Directory -Force $h | Out-Null
@'
model_provider = "gemini_local"
model = "gemini-flash"
[model_providers.gemini_local]
name = "gemini qua LiteLLM cuc bo"
base_url = "http://127.0.0.1:4000/v1"
wire_api = "responses"
env_key = "LITELLM_LOCAL_KEY"
'@ | Set-Content -Encoding UTF8 (Join-Path $h 'config.toml')
Write-Host "Da tao $h (khoa LiteLLM cuc bo la chuoi bat ky, dat bang bien moi truong khi chay)."
