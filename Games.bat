@echo off
chcp 65001
title Games
color 8f
cd C:\Progra~1\PrivateSpace\Games
dir "C:\Progra~1\PrivateSpace\Games" /a-d > nul 2> nul && echo Ready! || goto MainEmpty
:ShowFiles
color 9f
cls
echo.
echo %cd%
echo Folder contents:
echo.
dir /d /p /w /b
dir "%cd%" /a-d > nul 2> nul && goto NotEmpty || goto Empty
:NotEmpty
echo.
echo Choose an action:
echo 1. Go back
echo 2. Enter a path
echo 3. Open a file
goto Choose
:Empty
cls
echo.
echo The folder is empty!
echo Press any key to go back...
echo.
pause
goto Back
:Choose
set/p "cho=>"
if %cho%==1 goto Back
if %cho%==2 goto Teleport
if %cho%==3 goto Open
echo Invalid action
goto Choose
:Back
cd..
if NOT %cd%==C:\Progra~1\PrivateSpace\Games* goto CantBack
goto ShowFiles
:Teleport
echo Enter a path.
set/p "cho=%cd%\"
cd %cd%\%cho%
goto ShowFiles
:Open
echo Enter a file name.
echo Make sure to include the extension!
echo.
set/p "cho=%cd%\"
start %cd%\%cho% /max
goto ShowFiles
:CantBack
cls
echo.
echo You cannot move outside C:\Progra~1\PrivateSpace\Games
echo Press any key to return...
echo.
pause
cd C:\Progra~1\PrivateSpace\Games
goto ShowFiles
:MainEmpty
cls
color 4f
echo The "Games" folder is empty!
echo Press any key to exit.
pause
exit
