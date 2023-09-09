from sources.main.delete_component import DeleteComponent
from sources.main.interface.show_default_menu import ShowDefaultMenu
from sources.main.apps.windows_apps.windows_apps import WindowsApps
from sources.main.apps.show_apps import ShowApps
from sources.main.interface.show_banners import ShowBanners
from sources.other_sources.other_sources import InitValue
from sources.other_sources.exceptions.is_not_int import IsNotInt
from sources.main.apps.windows_apps.delete_windows_app import DeleteWindowsApp
from sources.main.apps.system_apps.system_apps import SystemApps
from sources.main.apps.system_apps.delete_system_app import DeleteSystemApp
from sources.main.execute_command import ExecuteCommand
from sources.main.winsxs.delete_winsxs_backup import DeleteWinSxSBackup
from sources.main.esd.esd import Esd
from sources.other_sources.exceptions.path_does_not_exist import PathDoesNotExist
from sources.other_sources.other_sources import DefaultPathExists
from sources.other_sources.other_sources import CreateDefaultPath
from sources.main.esd.wim_to_esd import WimToEsd
from sources.main.winsxs.clear_winsxs import ClearWinSxS
from sources.wim.unmount_wim import UnmountWim
import subprocess
import sys
import time
import os


class ParseChoice(ShowDefaultMenu):
    __links_one = [
        ShowApps,
        InitValue,
    ]

    __links_two = [
        WindowsApps,
        DeleteWindowsApp
    ]

    __links_three = [
        SystemApps,
        DeleteSystemApp
    ]

    __links_four = [
        DefaultPathExists,
        CreateDefaultPath
    ]

    def __init__(self, choice):
        self.choice = choice

    def parse_choice(self):
        if self.choice is None:
            return "do not wait"

        if self.choice in range(0, 10):
            d = DeleteComponent(
                choice=self.choice - 1
            )
            d.delete_component()

        match self.choice:
            case 10:
                windows_apps = self.__links_two[0]()
                while True:
                    subprocess.run("cls", shell=True)

                    if not windows_apps.human_packages:
                        if not windows_apps.get_windows_apps():
                            return False

                        windows_apps.find_package_names()

                        windows_apps.find_human_readable_packages()

                    show_apps = self.__links_one[0](
                        apps=WindowsApps.human_packages,
                        epilog="windows apps"
                    )

                    ShowBanners.show_default_banner()

                    print("\n\n[*INFO] Type \"back\" to back\n\n")

                    show_apps.show_apps()

                    init_app = self.__links_one[1](
                        cls=None,
                        name=None,
                        epilog=None,
                        return_value=True,
                        show_epilog=False
                    )

                    init_value = init_app.init_value()

                    if init_value[1].lower() == "back":
                        break

                    if not init_value[0]:
                        continue

                    app = init_value[1]

                    is_not_int = IsNotInt(
                        value=app,
                        epilog=None,
                        show_epilog=False
                    )

                    if is_not_int.is_not_int():
                        continue

                    if int(app) not in range(len(windows_apps.human_packages) + 1):
                        continue

                    app_ = int(app)

                    app_ -= 1

                    app = windows_apps.packages[app_]

                    app_human = windows_apps.human_packages[app_]

                    delete_windows_app = self.__links_two[1](
                        windows_app=app,
                        windows_app_human=app_human
                    )

                    if not delete_windows_app.delete_windows_app():
                        continue

                return True
            case 11:
                system_apps = self.__links_three[0]()
                while True:
                    if not system_apps.system_apps_human:
                        if not system_apps.get_system_apps():
                            return False

                        system_apps.get_system_apps()

                        system_apps.get_human_system_apps()

                    show_apps = self.__links_one[0](
                        apps=system_apps.system_apps_human,
                        epilog="system apps"
                    )

                    subprocess.run(
                        "cls",
                        shell=True
                    )

                    ShowBanners.show_default_banner()

                    print("\n\n[*INFO] Type \"back\" to back\n\n")

                    show_apps.show_apps()

                    init_app = self.__links_one[1](
                        cls=None,
                        name=None,
                        epilog=None,
                        return_value=True,
                        show_epilog=False
                    )

                    init_value = init_app.init_value()

                    if init_value[1].lower() == "back":
                        break

                    if not init_value[0]:
                        continue

                    app = init_value[1]

                    is_not_int = IsNotInt(
                        value=app,
                        epilog=None,
                        show_epilog=False
                    )

                    if is_not_int.is_not_int():
                        continue

                    app_ = int(app)

                    if app_ not in range(len(system_apps.system_apps_human) + 1):
                        continue

                    app_ -= 1

                    app = system_apps.system_apps[app_]

                    human_app = system_apps.system_apps_human[app_]

                    delete_system_app = self.__links_three[1](
                        system_app=app,
                        system_app_human=human_app
                    )

                    if not delete_system_app.delete_system_app():
                        continue

                return True
            case 12:
                subprocess.run("cls", shell=True)

                ShowBanners.show_default_banner()

                print("\n\n[*INFO] Type \"back\" to back\n")
                while True:
                    command_init = self.__links_one[1](
                        cls=None,
                        name=None,
                        epilog=None,
                        return_value=True,
                        show_epilog=False
                    )

                    init_value = command_init.init_value()

                    if not init_value[0]:
                        return False

                    command = init_value[1]

                    if command.lower() == "back":
                        break

                    execute_command = ExecuteCommand(
                        command=command,
                    )

                    execute_command.execute_command()

                return True
            case 13:
                delete_winsxs_backup = DeleteWinSxSBackup()
                delete_winsxs_backup.delete_winsxs_backup()
                return True
            case 14:
                print("\n\n[*INFO] Type \"back\" to back\n\n")

                subprocess.run("cls", shell=True)

                ShowBanners.show_default_banner()

                wim_path_init = self.__links_one[1](
                    cls=Esd,
                    name="wim_path",
                    epilog="[*] Wim path:",
                )

                wim_path = wim_path_init.init_value()

                if not wim_path:
                    return False

                if not Esd.wim_path:
                    return False

                if Esd.wim_path.lower() == "back":
                    return True

                future_esd_path_init = self.__links_one[1](
                    cls=Esd,
                    name="future_esd_path",
                    epilog="[*] Future esd path:",
                )

                future_esd_path = future_esd_path_init.init_value()

                if not future_esd_path:
                    return False

                if not Esd.future_esd_path:
                    return False

                if Esd.future_esd_path.lower() == "back":
                    return True

                index_init = self.__links_one[1](
                    cls=Esd,
                    name="index",
                    epilog="[*] Index:"
                )

                index = index_init.init_value()

                if not index:
                    return False

                if not Esd.index:
                    return False

                if Esd.index.lower() == "back":
                    return True

                wim_path_exists = PathDoesNotExist(
                    path=Esd.wim_path,
                    epilog="Wim path"
                )

                if wim_path_exists.path_does_not_exist():
                    time.sleep(3)
                    return False

                epilog = "\n[*ERROR] Index should be integer"
                epilog += f"\n[*INFO] Not: {Esd.index}"

                is_not_int = IsNotInt(
                    value=Esd.index,
                    epilog=epilog
                )

                if is_not_int.is_not_int():
                    print(
                        "\n[*INFO] Script will use default index (1)"
                    )
                    setattr(Esd, "index", 1)

                future_path_exists = PathDoesNotExist(
                    path=Esd.future_esd_path,
                    epilog="Esd future path"
                )

                epilog = "\n[*INFO] However found default future esd path"
                epilog += f"\n[*INFO] Straight path to it: {Esd.default_future_esd_path}"
                epilog += f"\n[*INFO] Script will use it"

                if future_path_exists.path_does_not_exist():
                    default_path_exists = DefaultPathExists(
                        path=Esd.default_future_esd_path,
                        epilog=epilog
                    )

                    if default_path_exists.default_path_exists():
                        setattr(
                            Esd,
                            "future_esd_path",
                            Esd.default_straight_future_esd_path
                        )
                    else:
                        epilog = "\n[*INFO] Script will create default future esd path"
                        epilog += f"\n[*INFO] Straight path to it: {Esd.default_future_esd_path}"

                        print(
                            "\n[*INFO] Script will create default future esd path",
                            f"\n[*INFO] Straight path to it: {Esd.default_future_esd_path}"
                        )

                        create_default_path = CreateDefaultPath(
                            path=Esd.default_future_esd_path,
                            epilog="future esd"
                        )

                        create_default_path.create_default_path()
                        setattr(
                            Esd,
                            "future_esd_path",
                            Esd.default_straight_future_esd_path
                        )

                if not Esd.future_esd_path.endswith(".esd"):
                    print(
                        "\n[*ERROR] You did not entered straight esd path, "
                        "so the script will add \"install.esd\" to path"
                    )
                    setattr(
                        Esd,
                        "future_esd_path",
                        os.path.join(
                            Esd.future_esd_path,
                            "install.esd"
                        )
                    )

                wim_to_esd = WimToEsd()

                if not wim_to_esd.wim_to_esd():
                    return False

                return True
            case 15:
                while True:
                    subprocess.run("cls", shell=True)

                    ShowBanners.show_default_banner()

                    print("\n\n[*INFO] Type \"back\" to back\n\n")

                    for count, possible in enumerate(ClearWinSxS.possible_clean, 1):
                        if count <= 9:
                            print(f"[{count}]  | {possible}")
                            continue

                        print(f"[{count}] | {possible}")

                    init_clean_win_sxs_value = self.__links_one[1](
                        cls=None,
                        name=None,
                        epilog=None,
                        return_value=True,
                        show_epilog=False
                    )

                    init_value = init_clean_win_sxs_value.init_value()

                    if init_value[1].lower() == "back":
                        break

                    if not init_value[0]:
                        continue

                    clean_choice = init_value[1]

                    is_not_int = IsNotInt(
                        value=clean_choice,
                        epilog=None,
                        show_epilog=False
                    )

                    if is_not_int.is_not_int():
                        continue

                    clean_choice = int(clean_choice)

                    clean_choice -= 1

                    if clean_choice not in range(15):
                        continue

                    clear_winsxs = ClearWinSxS(
                        choice=clean_choice
                    )

                    clear_winsxs.clear_winsxs()
                return True
            case 16:
                unmount_wim = UnmountWim()
                if not unmount_wim.unmount_wim():
                    sys.exit(1)

                sys.exit(0)
            case 17:
                unmount_wim = UnmountWim(
                    mode="discard"
                )
                if not unmount_wim.unmount_wim():
                    sys.exit(1)

                sys.exit(0)
            case 18:
                sys.exit(0)
