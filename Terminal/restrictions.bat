echo.
if exist restrictions.txt (goto yes) else (goto no)

:Yes
set text=%random%%random%
echo.
echo Disabling terminal restrictions
echo.
echo Warning! Editing or opening files from the Private Space root folder can damage your computer!
echo.
echo The creator is not responsible for lost data!
echo.
echo Do you really want to lift the restrictions?
echo Type "%text%" to confirm...
echo.
set/p "cho=>"
if %cho%==%text% goto Disable
echo Invalid input!
goto exit
:No
echo Restrictions are already disabled.
echo.
echo Remember: do not run or edit files in the Private Space root folder!
echo You might damage your computer!
goto Exit
:Disable
echo.
del c:\progra~1\PrivateSpace\restrictions.txt
echo Restrictions removed!
echo The terminal needs to restart. Press any key to exit...
echo.
pause
exit
:Exit
echo off
