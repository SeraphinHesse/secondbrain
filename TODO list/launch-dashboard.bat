@echo off
:: Check if server is already running
curl -s http://localhost:8765/api/tasks >nul 2>&1
if %errorlevel% neq 0 (
    start /min "" node "%~dp0todo-server.js"
    timeout /t 2 /nobreak >nul
)
start "" "http://localhost:8765"
