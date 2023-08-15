from sources.other_sources.other_sources import InitValue
from sources.other_sources.other_sources import InitMode
from exceptions.value_is_not_in_list import ValueIsNotInList
from sources.wim.wim import Wim
from sources.other_sources.other_sources import ConfigInit
from sources.other_sources.exceptions.path_does_not_exist import PathDoesNotExist
from sources.other_sources.other_sources import DefaultPathExists
from sources.other_sources.other_sources import CreateDefaultPath
from sources.wim.is_wim import IsWim
from sources.wim.mount_wim import MountWim
from sources.other_sources.exceptions.is_not_int import IsNotInt
from sources.main.interface.show_banners import ShowBanners
from sources.main.choice.choice import Choice
from sources.main.choice.parse_choice import ParseChoice
from sources.main.interface.show_default_menu import ShowDefaultMenu
import sys
import subprocess


class OnResume:
    __links_one = [
        InitValue,
        InitMode,
        ConfigInit
    ]

    __links_two = [
        ValueIsNotInList
    ]

    __links_three = [
        PathDoesNotExist,
        DefaultPathExists,
        CreateDefaultPath
    ]

    __links_four = [
        IsWim,
        MountWim
    ]

    __links_five = [
        ShowBanners
    ]

    def on_resume(self):
        epilog = "\n[*INFO] Answer in user_input(ui) or config.json(cj)"
        init_mode = self.__links_one[0](
            cls=InitMode,
            name="mode",
            epilog=epilog
        )

        self.__links_five[0]().show_init_banner()

        print(
            "\n[*INFO] Which method of initialization" +
            " do you want to use?:", end=""
        )

        if not init_mode.init_value():
            sys.exit(3)

        epilog = (
            f"\n[*ERROR] You answered: {self.__links_one[1].mode} " +
            "instead of \"user_input(ui)\" or \"config.json(cj)\""
        )

        matches = [
            "user_input",
            "user input",
            "user",
            "ui",
            "config.json",
            "config",
            "cj"
        ]

        correct_mode = self.__links_two[0](
            value=self.__links_one[1].mode,
            epilog=epilog,
            matches=matches
        )

        if not correct_mode.value_is_not_in_list():
            sys.exit(4)

        user_input_matches = matches[:4]

        if correct_mode.found[0] in user_input_matches:
            wim_path_init = self.__links_one[0](
                cls=Wim,
                name="wim_path",
                epilog="\n[*] Wim path:"
            )

            mount_path_init = self.__links_one[0](
                cls=Wim,
                name="mount_path",
                epilog="\n[*] Mount path:"
            )

            index_init = self.__links_one[0](
                cls=Wim,
                name="index",
                epilog="\n[*] Index:"
            )

            init = [
                wim_path_init,
                mount_path_init,
                index_init
            ]

            for i in init:
                if not i.init_value():
                    sys.exit(5)
        else:
            if not self.__links_one[2].config_init():
                sys.exit(6)

        epilog = "\n[*ERROR] Index should be integer"
        epilog += f"\n[*INFO] Not: {Wim.index}"

        index_is_not_int = IsNotInt(
            value=Wim.index,
            epilog=epilog
        )

        if index_is_not_int.is_not_int():
            print(
                "\n[*INFO] Script will use default index (1)"
            )
            setattr(Wim, "index", 1)

        wim_path_exists = self.__links_three[0](
            path=Wim.wim_path,
            epilog="Wim"
        )

        if wim_path_exists.path_does_not_exist():
            sys.exit(7)

        if not self.__links_four[0]().is_wim():
            sys.exit(8)

        mount_path_exists = self.__links_three[0](
            path=Wim.mount_path,
            epilog="Mount"
        )

        epilog = "[*INFO] However found default mount path"
        epilog += f"\n[*INFO] Straight path to it: {Wim.default_mount_path}"
        epilog += "\n[*INFO] Script will use it"

        if mount_path_exists.path_does_not_exist():
            default_mount_path_exists = self.__links_three[1](
                path=Wim.default_mount_path,
                epilog=epilog
            )

            if default_mount_path_exists.default_path_exists():
                setattr(Wim, "mount_path", Wim.default_mount_path)
            else:
                print(
                    "\n[*INFO] Script will create default mount path",
                    f"\n[*INFO] Path to it: {Wim.default_mount_path}"
                )

                create_default_path = self.__links_three[2](
                    path=Wim.default_mount_path,
                    epilog="mount"
                )

                create_default_path.create_default_path()
                setattr(Wim, "mount_path", Wim.default_mount_path)

        if not self.__links_four[1]().mount_wim():
            sys.exit(9)

        while True:
            subprocess.run("cls", shell=True)
            ShowBanners.show_default_banner()

            print("\n[*INFO] Made by github.com/clqwnless\n")

            ShowDefaultMenu.show_default_menu()
            c = Choice()

            choice = c.select_choice()

            if not choice:
                continue

            p = ParseChoice(
                choice=choice[1]
            )

            if p.parse_choice() in ["do not wait", True]:
                continue

            continue
