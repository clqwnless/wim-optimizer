@echo off

setlocal

set path="%1"

if %path% equ "" (
    echo path argument is required to delete winsxs backup folder
    exit /b 1
)

rmdir /s /q "%path%\Windows\WinSxS\Backup"

endlocal
