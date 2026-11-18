@echo off
rem Xuong JX1: chi nghe 127.0.0.1. Ma truy cap: D:\JX-xuong\ma.txt
cd /d "%~dp0"
start "" http://127.0.0.1:8770/
python -I -X utf8 app.py
pause
