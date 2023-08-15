from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
from sources.main.esd.esd import Esd
import time


class WimToEsd(Esd):
    def __init__(self):
        self.command = (
            f"dism /Export-Image /SourceImageFile:\"{self.wim_path}\"" +
            f" /SourceIndex:{self.index}" +
            f" /DestinationImageFile:\"{self.future_esd_path}\"" +
            " /Compress:recovery"
        )

    def wim_to_esd(self):
        e = ErrorWhileRunning(
            command=self.command,
            epilog="changing wim to esd",
            show_stdout_at_run=True,
        )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        return True
