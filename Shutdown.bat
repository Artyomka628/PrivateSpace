@echo off
chcp 65001
cls
title Выход из Private Space
color 9f
echo Private Space от Artyomka App Studio
echo.
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo Запущено как система, не требуется разрешение
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo.
echo Запуск файла... 
ping localhost -n 2 > nul
echo Выход из режима MS-DOS...
echo.
echo Изменение реестра...
reg add HKLM\System\Setup /v CmdLine /t REG_SZ /d "" /f
reg add HKLM\System\Setup /v SystemSetupInProgress /t REG_DWORD /d 0 /f > nul
reg add HKLM\System\Setup /v SetupType /t REG_DWORD /d 0 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableCursorSuppression /t REG_DWORD /d 1 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 0 /f > nul
echo.
echo Готово, выключение. (3 попытки)
echo Попытка #1
shutdown -s -t 0
ping localhost -n 3 > nul
echo Ошибка. Попытка #2
shutdown -s -t 0
ping localhost -n 3 > nul
echo Ошибка. Попытка #3
shutdown -s -t 0
echo Ошибка. Обычно система не сразу выключает компьютер, подождите 5 секунд
timeout 5
:err
cls
color 4f
echo Если вы видите эту надпись, выключите компьютер самостоятельно!
pause
goto err