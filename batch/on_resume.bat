@echo off

cd ..

setlocal

set python_path=%1

set on_resume_path=%2

if %python_path% equ "" (
    echo python path cannot be empty
    exit /b 1
)

if %on_resume_path% equ "" (
    echo on_resume path cannot be empty
    exit /b 1
)

%python_path% %on_resume_path%

endlocal
