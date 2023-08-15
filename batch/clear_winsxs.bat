@echo off

setlocal

set possible=defender onedrive quickassist smartscreen mixedreality adobeflash skype-ortc xbox cortana edge maps mapcontrol internetexplorer people

set choice="%1"

set path="%2"

if %choice% equ "" (
    echo choice cannot be empty
    exit /b 1
)

if %path% equ "" (
    echo path cannot be empty
    exit /b 1
)

set flag=False

for %%i in (%possible%) do (
    if %choice% equ "%%i" (
        set flag=True
    )
)

if %flag% neq True (
    echo invalid choice: %choice%
    echo possible choices: %possible%
    exit /b 1
)

if %choice% equ "adobeflash" (
    set choice="flash"
)

for /d %%i in ("%path%\Windows\WinSxS\*%choice%*") do (
    rmdir /s /q %%i
)

if %choice% equ "defender" (
    for /d %%i in ("%path%\Windows\WinSxS\*sechealthui*") do (
        rmdir /s /q %%i
    )
)

if %choice% equ "people" (
        for /d %%i in ("%path%\Windows\WinSxS\*-p..riencehost*") do (
        rmdir /s /q %%i
    )
)

endlocal
