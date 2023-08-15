from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import os
import sys
import time


class RunAsTrustedInstaller:
    def __init__(self):
        self.python_path = sys.executable
        self.on_resume_path = os.path.join(
            os.getcwd(), r"sources\other_sources\on_run_resume.py"
        )
        self.script_path = os.path.join(
            os.getcwd(), "powershell", "run_as_trustedinstaller.ps1 "
        )

        self.command = (
            f"powershell.exe -executionpolicy bypass " +
            "-File {self.script_path} " +
            f"\"{self.python_path}\" \"{self.on_resume_path}\""
        )

    def run_as_trustedinstaller(self):
        epilog = "error while running as TrustedInstaller"
        e = ErrorWhileRunning(
            command=self.command,
            epilog=epilog
        )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        return True
