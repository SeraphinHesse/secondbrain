@echo off
echo ========================================
echo  GDD XP Card Parser - EXE Builder
echo ========================================
echo.

REM Install dependencies
echo Installing dependencies...
pip install pymupdf pyinstaller pyyaml
echo.

REM Build single-file EXE
echo Building EXE...
pyinstaller --onefile --noconsole --name "GDD_XP_Card_Parser" --icon NONE gui.py

echo.
echo ========================================
if exist dist\GDD_XP_Card_Parser.exe (
    echo  SUCCESS! EXE is at: dist\GDD_XP_Card_Parser.exe
    echo.
    echo  You can move GDD_XP_Card_Parser.exe anywhere.
    echo  Optional: put config.yaml next to the EXE to customise section mapping.
) else (
    echo  BUILD FAILED - check output above for errors
)
echo ========================================
pause
