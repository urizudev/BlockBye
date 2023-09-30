@echo off
title -[BLOCKBYE]-

:menu
cls
echo ==============================
echo BlockBye Menu
echo ==============================
echo 1. Run BlockBye
echo 2. Install Requirements
echo 3. Exit
echo ==============================
set /p choice=Enter your choice (1/2/3): 

if "%choice%"=="" goto menu
if "%choice%"=="1" goto run_script
if "%choice%"=="2" goto install_requirements
if "%choice%"=="3" exit

:run_script
cls
echo Running Python Script...
python main.py
pause
goto menu

:install_requirements
cls
echo Installing Python Requirements...
pip install -r requirements.txt
pause
goto menu
