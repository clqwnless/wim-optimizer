param (
    [string]$python_path,
    [string]$on_resume_path
)

if ($python_path -eq "") {
    Write-Error "python path argument cannot not empty"
    Start-Sleep -Seconds 3
    exit 1
}

if ($on_resume_path -eq "") {
    Write-Error "on resume path argument cannot not empty"
    Start-Sleep -Seconds 3
    exit 1
}

$command = "cmd.exe /k cd batch && on_resume.bat ""$python_path"" ""$on_resume_path"""

Start-Service -Name TrustedInstaller
$parent = Get-NtProcess -ServiceName TrustedInstaller
New-Win32Process $command -CreationFlags NewConsole -ParentProcess $parent
