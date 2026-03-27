@echo off
chcp 65001
color f
cd C:\Progra~1\PrivateSpace

for /f "delims=" %%a in (theme.txt) do set "theme=%%a"

rem Apply the theme directly
if /i "%theme%"=="theme.h1" color a
if /i "%theme%"=="theme.h2" color f2
if /i "%theme%"=="theme.d" color f
if /i "%theme%"=="theme.g" color 6f
if /i "%theme%"=="theme.b" color 9f
if /i "%theme%"=="theme.r" color cf

cls
echo.
echo        Terminal
echo Drygval Artyom, 2026.
echo.
echo This terminal comes with extra commands.
echo For help, type "help+"
goto Console

:Console
set /p "cho=%cd%> "

:Run
if "%cho%"=="" goto Console

if /i "%cho%"=="disablerestrictions" call C:\Progra~1\PrivateSpace\Terminal\restrictions.bat & echo. & goto Console
if /i "%cho%"=="ver" call C:\Progra~1\PrivateSpace\Terminal\ver.bat & echo. & goto Console
if /i "%cho%"=="help+" call C:\Progra~1\PrivateSpace\Terminal\help.bat & echo. & goto Console
if /i "%cho%"=="theme" call C:\Progra~1\PrivateSpace\Terminal\theme.bat & echo. & goto Console
if /i "%cho%"=="theme.h1" (
    color a
    echo theme.h1>theme.txt
    goto Console
)
if /i "%cho%"=="theme.h2" (
    color f2
    echo theme.h2>theme.txt
    goto Console
)
if /i "%cho%"=="theme.d" (
    color f
    echo theme.d>theme.txt
    goto Console
)
if /i "%cho%"=="theme.g" (
    color 6f
    echo theme.g>theme.txt
    goto Console
)
if /i "%cho%"=="theme.b" (
    color 9f
    echo theme.b>theme.txt
    goto Console
)
if /i "%cho%"=="theme.r" (
    color cf
    echo theme.r>theme.txt
    goto Console
)
if /i "%cho%"=="parrot" color f & curl parrot.live & goto Console
if /i "%cho%"=="rickroll" color f & curl ascii.live/rick & goto Console

cmd /c %cho%
if errorlevel 1 (
    goto Console
)
goto Console
