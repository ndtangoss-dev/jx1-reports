@echo off
chcp 65001 >nul
rem Luu khoa vao D:\JX-keys\gemini.txt (NGOAI kho). Khong in lai khoa. Chi chu may chay.
title Nhap khoa Gemini
echo.
echo  Dan khoa Gemini (AI Studio) roi bam Enter. Khoa se KHONG hien tren man hinh.
echo.
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
 "$d='D:\JX-keys'; New-Item -ItemType Directory -Force $d | Out-Null; $s=Read-Host 'Khoa' -AsSecureString; $b=[Runtime.InteropServices.Marshal]::SecureStringToBSTR($s); $k=[Runtime.InteropServices.Marshal]::PtrToStringBSTR($b); [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($b); if($k.Trim().Length -lt 20){Write-Host 'Khoa qua ngan, chua luu.'; exit 1}; $f=Join-Path $d 'gemini.txt'; [IO.File]::WriteAllText($f,$k.Trim()); icacls $d /inheritance:r /grant:r \"$env:USERNAME`:(OI)(CI)F\" | Out-Null; Write-Host ('Da luu, do dai ' + $k.Trim().Length + ' ky tu. Khong hien lai khoa.')"
echo.
pause
