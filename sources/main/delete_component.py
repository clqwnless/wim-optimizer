from sources.wim.wim import Wim
import os
import json
import subprocess


class DeleteComponent(Wim):
    __available_components = [
        "defender",
        "onedrive",
        "quickassist",
        "smartscreen",
        "mixedreality",
        "adobeflash",
        "skypeortc",
        "xbox",
        "internetexplorer"
    ]

    extensions = [
        ".exe",
        ".dll",
        ".lnk",
        ".ico",
        ".cpl"
    ]

    def __init__(self, choice=None):
        super().__init__()
        self.choice = choice
        self.json_path = self.__available_components[self.choice] + ".json"

    def delete_component(self):
        os.chdir("config")
        with open(self.json_path, mode="r") as f:
            data = json.load(f)

        first_key = list(data.keys())[0]

        paths = data[first_key]

        for path in paths:
            path = os.path.join(
                Wim.mount_path,
                path
            )
            if path[-4:].lower() in self.extensions:
                subprocess.run(
                    f"del /s /q \"{path}\"",
                    shell=True,
                )
                continue

            subprocess.run(
                f"rmdir /s /q \"{path}\"",
                shell=True,
            )

        os.chdir("..")
