from sources.wim.wim import Wim
from sources.other_sources.exceptions.error_while_running import ErrorWhileRunning
import time
import re


class WindowsApps(Wim):
    packages = list()
    human_packages = list()

    def __init__(self):
        self.command = f"dism /Image:\"{self.mount_path}\" /Get-ProvisionedAppxPackages"
        self.output = None

    def get_windows_apps(self):
        epilog = "getting windows apps"

        e = ErrorWhileRunning(
            command=self.command,
            epilog=epilog,
            return_value=True
        )

        e_ = e.error_while_running()

        if e_[0]:
            time.sleep(3)
            return False

        self.output = e_[1]

        return True

    def find_package_names(self):
        matches = re.findall(
            "PackageName : (.*)",
            self.output
        )

        self.packages.extend(matches)

    def find_human_readable_packages(self):
        matches = re.findall(
            pattern="DisplayName : (.*)",
            string=self.output
        )

        for match in matches:
            if match == "Microsoft.WindowsStore":
                self.human_packages.append("MicrosoftStore")
                continue

            match = re.sub(
                pattern=r"[mM]icrosoft\.*",
                repl="",
                string=match,
            )

            match = re.sub(
                pattern=r"[wW]indows\.*",
                repl="",
                string=match,
            )

            self.human_packages.append(match)
