@echo off
cd /d "%~dp0"
.venv\Scripts\python.exe -m workflow.graph %*
exit /b %errorlevel%
