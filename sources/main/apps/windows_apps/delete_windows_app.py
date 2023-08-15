from sources.main.apps.windows_apps.windows_apps import WindowsApps
from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import time


class DeleteWindowsApp(WindowsApps):
    def __init__(self, windows_app, windows_app_human):
        super().__init__()
        self.windows_app = windows_app
        self.windows_app_human = windows_app_human
        self.command = (
            f"dism /Image:\"{self.mount_path}\" /Remove-ProvisionedAppxPackage" +
            f" /PackageName:{self.windows_app}"
        )

    def delete_windows_app(self):
        e = ErrorWhileRunning(
            command=self.command,
            epilog="deleting windows app",
        )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        self.packages.remove(
            self.windows_app
        )

        self.human_packages.remove(
            self.windows_app_human
        )

        return True
