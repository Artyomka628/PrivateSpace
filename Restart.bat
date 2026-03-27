@echo off
chcp 65001
cls
title Перезагрузка
color 9f
echo Private Space от Artyomka App Studio
echo.
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo  Запущено как система, не требуется разрешение
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
echo.
echo Запуск файла... 
ping localhost -n 2 > nul
echo Перезагрузка в систему Private Space...
echo.
echo Редактирование реестра...
reg add HKLM\System\Setup /v CmdLine /t REG_SZ /d "cmd.exe /k C:\dosexec.bat" /f
reg add HKLM\System\Setup /v SystemSetupInProgress /t REG_DWORD /d 1 /f > nul
reg add HKLM\System\Setup /v SetupType /t REG_DWORD /d 2 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableCursorSuppression /t REG_DWORD /d 0 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f > nul
echo.
echo Готово, перезагрузка. (3 попытки)
echo Попытка #1
shutdown -r -t 0
ping localhost -n 3 > nul
echo Ошибка. Попытка #2
shutdown -r -t 0
ping localhost -n 3 > nul
echo Ошибка. Попытка #3
shutdown -r -t 0
echo Ошибка. Обычно система не сразу перезагружает компьютер, подождите 5 секунд
timeout 5
:err
cls
color 4f
echo Если вы видите эту надпись, перезагрузитесь самостоятельно!
pause
goto err