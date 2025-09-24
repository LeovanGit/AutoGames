@echo off

:: return back to working dir:
echo %~dp0
cd /d %~dp0

python input_app.py
pause

@echo on