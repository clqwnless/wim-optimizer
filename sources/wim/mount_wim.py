from sources.wim.wim import Wim
from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import time


class MountWim(Wim):
    def __init__(self):
        self.command = (
            f"dism /Mount-WIM /WimFile:\"{self.wim_path}\" " +
            f"/Index:{self.index} /MountDir:\"{self.mount_path}\""
        )

    def mount_wim(self):
        e = ErrorWhileRunning(
            command=self.command,
            epilog="mounting wim",
            show_stdout_at_run=True,
            end=False
        )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        return True
