from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning


class ExecuteCommand:
    def __init__(self, command):
        self.command = command

    def execute_command(self):
        epilog = f"running {self.command} command"

        e = ErrorWhileRunning(
            command=self.command,
            epilog=epilog,
            show_stdout_at_run=True
        )

        e_ = e.error_while_running()

        if e_:
            return False

        return True
