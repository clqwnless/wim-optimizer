import subprocess


class ErrorWhileRunning:
    def __init__(self, command, epilog, show_stdout_at_run=False, end=True, return_value=False):
        self.command = command
        self.epilog = epilog
        self.show_stdout_at_run = show_stdout_at_run
        self.end = end
        self.return_value = return_value
        self.ran = None

    def _run_command(self):
        try:
            if self.show_stdout_at_run:
                self.ran = subprocess.run(
                    self.command,
                    shell=True,
                    text=True,
                    stderr=subprocess.PIPE
                )
            else:
                self.ran = subprocess.run(
                    self.command,
                    shell=True,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
        except Exception as e:
            print(
                f"\n[*ERROR] An error occurred while "
                f"{self.epilog}: {e}"
            )
            return False

        return True

    def error_while_running(self):
        if not self._run_command() and self.return_value:
            return True, self.ran.stdout

        if self.show_stdout_at_run and self.ran.returncode != 0:
            if self.ran.stderr and not self.ran.stdout:
                print(
                    "\n[*ERROR] An error occurred while "
                    f"{self.epilog}: \n{self.ran.stderr}"
                )

            return True

        if self.ran.returncode != 0 and not self.ran.stderr:
            print(
                "\n[*ERROR] An error occurred while "
                f"{self.epilog}: \n{self.ran.stdout}"
            )
            if self.return_value:
                return True, self.ran.stdout

            return True

        if self.ran.returncode != 0:
            print(
                "\n[*ERROR] An error occurred while "
                f"{self.epilog}: \n{self.ran.stderr}"
            )
            if self.return_value:
                return True, self.ran.stdout

            return True

        if self.return_value:
            return False, self.ran.stdout

        return False
