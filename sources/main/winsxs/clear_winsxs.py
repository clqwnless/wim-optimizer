from sources.wim.wim import Wim
import os
import subprocess


class ClearWinSxS(Wim):
    possible_clean = [
        "defender",
        "onedrive",
        "quickassist",
        "smartscreen",
        "mixedreality",
        "adobeflash",
        "xbox",
        "cortana",
        "edge",
        "skype-ortc",
        "maps",
        "mapcontrol",
        "internetexplorer",
        "people"
    ]

    def __init__(self, choice):
        self.choice = self.possible_clean[choice]
        self.command = f"clear_winsxs.bat {self.choice} {self.mount_path}"

    def clear_winsxs(self):
        os.chdir("batch")

        subprocess.run(self.command, shell=True)

        os.chdir("..")
