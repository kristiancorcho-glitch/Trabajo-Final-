@echo off
setlocal
cd /d "%~dp0"

python -m src.main
if errorlevel 1 (
    echo.
    echo No se pudo iniciar PatiTrack. Verifique que Python este instalado
    echo y disponible en el PATH del sistema.
)

echo.
pause
