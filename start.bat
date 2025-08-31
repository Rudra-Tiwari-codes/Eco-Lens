@echo off
echo ========================================
echo Starting EcoLens - AI Sustainability Tracker
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Starting EcoLens server...
python run.py

echo.
echo ========================================
echo EcoLens is now running!
echo ========================================
echo Web interface: http://127.0.0.1:8000
echo.
echo Press any key to close this window...
pause > nul
