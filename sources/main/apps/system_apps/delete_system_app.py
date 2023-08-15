from sources.main.apps.system_apps.system_apps import SystemApps
from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import os
import time


class DeleteSystemApp(SystemApps):
    def __init__(self, system_app, system_app_human):
        super().__init__()
        self.system_app = system_app
        self.system_app_human = system_app_human
        self.system_app_path = os.path.join(
            self.system_apps_path,
            self.system_app
        )

    def delete_system_app(self):
        e = ErrorWhileRunning(
            command=f"rmdir /s /q {self.system_app_path}",
            epilog="deleting system app",
        )

        e_ = e.error_while_running()

        if e_:
            time.sleep(3)
            return False

        self.system_apps.remove(
            self.system_app
        )
        self.system_apps_human.remove(
            self.system_app_human
        )
        return True
