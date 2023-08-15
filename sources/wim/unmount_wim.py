from sources.wim.wim import Wim
from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import time


class UnmountWim(Wim):
    def __init__(self, mode="save"):
        self.mode = mode
        self.save_command = (
            f"dism /Unmount-WIM /MountDir:\"{self.mount_path}\" /Commit"
        )
        self.discard_command = (
            f"dism /Unmount-WIM /MountDir:\"{self.mount_path}\" /Discard"
        )

    def unmount_wim(self):
        if self.mode == "save":
            e = ErrorWhileRunning(
                command=self.save_command,
                epilog="saving wim",
                show_stdout_at_run=True,
            )
        else:
            e = ErrorWhileRunning(
                command=self.discard_command,
                epilog="discarding wim changes",
                show_stdout_at_run=True
            )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        return True
