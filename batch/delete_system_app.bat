@echo off

setlocal

set --path="%1"

set --app="%2"

if %--path% equ "" (
    echo --path argument is required to delete system_app
    exit /b 1
)

if %--app% equ "" (
    echo --app argument is requires to delete system_app
    exit /b 1
)

for /d %%i in ("%--path%\Windows\SystemApps\*%--app%*") do (
    rmdir /s /q %%i
)

endlocal
