@echo off
:: Kill any existing server on port 8765, start fresh, open browser

for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8765 " ^| findstr "LISTENING"') do (
    taskkill /PID %%p /F >nul 2>&1
)

timeout /t 1 /nobreak >nul

start /min "" cmd /c "cd /d "%~dp0" && node todo-server.js"
timeout /t 2 /nobreak >nul

start "" "http://localhost:8765"
