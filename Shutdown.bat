@echo off
chcp 65001
cls
title Exit Private Space
color 9f
echo Private Space by Drygval Artyom
echo.
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo Running as SYSTEM, no special permission required
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo.
echo Launching script...
ping localhost -n 2 > nul
echo Exiting MS-DOS mode...
echo.
echo Updating the registry...
reg add HKLM\System\Setup /v CmdLine /t REG_SZ /d "" /f
reg add HKLM\System\Setup /v SystemSetupInProgress /t REG_DWORD /d 0 /f > nul
reg add HKLM\System\Setup /v SetupType /t REG_DWORD /d 0 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableCursorSuppression /t REG_DWORD /d 1 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 0 /f > nul
echo.
echo Ready, shutting down. (3 attempts)
echo Attempt #1
shutdown -s -t 0
ping localhost -n 3 > nul
echo Failed. Attempt #2
shutdown -s -t 0
ping localhost -n 3 > nul
echo Failed. Attempt #3
shutdown -s -t 0
echo Failed. Windows may not shut down immediately; wait 5 seconds
timeout 5
:err
cls
color 4f
echo If you see this message, please shut down the computer manually!
pause
goto err
