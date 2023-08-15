from sources.other_sources.exceptions.value_is_none import ValueIsNone
from sources.wim.wim import Wim
import os
import json
import re


class InitMode:
    mode = None


class InitValue:
    def __init__(self, cls, name, epilog, return_value=False, show_epilog=True):
        self.cls = cls
        self.name = name
        self.epilog = epilog
        self.return_value = return_value
        self.show_epilog = show_epilog

    def init_value(self):
        try:
            if not self.show_epilog:
                value = input("\n>>> ").strip()
            else:
                print(f"\n{self.epilog}", end="")
                value = input("\n>>> ").strip()
        except KeyboardInterrupt:
            return False

        if self.return_value:
            return True, value

        setattr(self.cls, self.name, value)

        return True


class ConfigInit:
    @staticmethod
    def config_init():
        os.chdir("config")

        with open("config.json", mode="r") as f:
            data = json.load(f)

        for key, value in data.items():
            if ValueIsNone(value, f"{key}").value_is_none():
                return False

        updated = dict()

        for count, value in enumerate(data.values(), 1):
            updated.update({count: value})

        updated_second = dict()

        for key, value in updated.items():
            match key:
                case 1:
                    key = "wim_path"
                case 2:
                    key = "mount_path"
                case 3:
                    key = "index"

            updated_second.update({key: value})

        data = updated_second

        setattr(Wim, "wim_path", data["wim_path"])
        setattr(Wim, "mount_path", data["mount_path"])
        setattr(Wim, "index", data["index"])

        os.chdir("..")
        return True


class DefaultPathExists:
    def __init__(self, path, epilog):
        self.path = path
        self.epilog = epilog

    def default_path_exists(self):
        if os.path.exists(self.path):
            print(f"\n{self.epilog}")
            return True

        return False


class CreateDefaultPath:
    def __init__(self, path, epilog, endswith_file=False):
        self.path = path
        self.epilog = epilog
        self.endswith_file = endswith_file

    def create_default_path(self):
        os.makedirs(self.path)
        print(
            "\n[*INFO] Successfully created default "
            f"{self.epilog} path"
        )
