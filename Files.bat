@echo off
chcp 65001
title Мои файлы
color 8f
cd C:\Progra~1\PrivateSpace\Files
dir "C:\Progra~1\PrivateSpace\Files" /a-d > nul 2> nul && echo Готово! || goto MainEmpty
:ShowFiles
color 9f
cls
echo.
echo %cd%
echo Содержимое папки:
echo.
dir /d /p /w /b
dir "%cd%" /a-d > nul 2> nul && goto NotEmpty || goto Empty
:NotEmpty
echo.
echo Выберите действие:
echo 1. Перейти назад
echo 2. Перейти по пути
echo 3. Открыть файл
goto Choose
:Empty
cls
echo.
echo Папка пустая!
echo Нажмите любую клавишу, для перехода назад...
echo.
pause
goto Back
:Choose
set/p "cho=>"
if %cho%==1 goto Back
if %cho%==2 goto Teleport
if %cho%==3 goto Open
echo Неверное действие
goto Choose
:Back
cd..
if NOT %cd%==C:\Progra~1\PrivateSpace\Files* goto CantBack
goto ShowFiles
:Teleport
echo Введите путь.
set/p "cho=%cd%\"
cd %cd%\%cho%
goto ShowFiles
:Open
echo Введите имя файла.
echo Обязательно добавьте расширение!
echo.
set/p "cho=%cd%\"
start %cd%\%cho% /max
goto ShowFiles
:CantBack
cls
echo.
echo Невозможно выйти за пределы папки C:\Progra~1\PrivateSpace\Files
echo Нажмите любую клавишу, для возврата...
echo.
pause
cd C:\Progra~1\PrivateSpace\Files
goto ShowFiles
:MainEmpty
cls
color 4f
echo Папка "Мои файлы" пуста!
echo Нажмите любую клавишу, для выхода.
pause
exit