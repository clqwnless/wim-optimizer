from sources.wim.wim import Wim
import os
import re


class SystemApps(Wim):
    system_apps = list()
    system_apps_human = list()

    def __init__(self):
        self.system_apps_path = os.path.join(
            self.mount_path,
            "Windows",
            "SystemApps"
        )

    def get_system_apps(self):
        try:
            for app in os.listdir(self.system_apps_path):
                self.system_apps.append(app)
        except FileNotFoundError:
            return False

        return True

    def get_human_system_apps(self):
        for app in os.listdir(self.system_apps_path):
            app = re.sub(
                pattern=r"[mM]icrosoft\.*",
                repl="",
                string=app
            )

            app = re.sub(
                pattern=r"[wW]indows\.*",
                repl="",
                string=app
            )

            app = re.sub(
                pattern="_.*",
                repl="",
                string=app
            )

            self.system_apps_human.append(app)
