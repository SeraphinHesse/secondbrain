@echo off
:: Adds the todo server to Windows startup (no admin required)
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set TARGET=%~dp0todo-server.js

echo @echo off > "%STARTUP%\secondbrain-server.bat"
echo start /min "" node "%TARGET%" >> "%STARTUP%\secondbrain-server.bat"

echo.
echo Done. The server will now start automatically when you log into Windows.
echo To remove it, delete: %STARTUP%\secondbrain-server.bat
echo.
pause
