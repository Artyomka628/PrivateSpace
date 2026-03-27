echo.
if exist restrictions.txt (goto yes) else (goto no)

:Yes
set text=%random%%random%
echo.
echo Отключение ограничений терминала
echo.
echo Внимание! Редактирование или открытие файлов из корневой папки Private Space, может навредить компьютёру!
echo.
echo Создатель не несёт ответственность за потерянные данные!
echo.
echo Вы действительно хотите снять ограничения?
echo Напечатайте "%text%", если хотите снять ограничения...
echo.
set/p "cho=>"
if %cho%==%text% goto Disable
echo Неверный ввод!
goto exit
:No
echo Ограничения отключены.
echo.
echo Помните! Не запускайте и не редактируйте файлы из корневой папки Private Space!
echo Вы можете навредить вашему компьютеру!
goto Exit
:Disable
echo.
del c:\progra~1\PrivateSpace\restrictions.txt
echo Ограничения сняты!
echo Требуется перезапуск терминала. Нажмите любую клавишу для выхода...
echo.
pause
exit
:Exit
echo off