from sources.main.interface.menus import components_menu
from sources.main.interface.menus import other_etc_menu
from sources.main.interface.menus import save_exit_menu
import colorama


class ShowDefaultMenu:
    @staticmethod
    def show_default_menu():
        colorama.init()

        max_len = max(len(i) for i in other_etc_menu)

        other_etc_iter = iter(other_etc_menu)

        save_exit_menu_iter = iter(save_exit_menu)

        for option in components_menu:
            print(
                colorama.Fore.RED + option.ljust(max_len), end=""
            )
            try:
                print(
                    colorama.Fore.GREEN + next(other_etc_iter).ljust(max_len + 10), end=""
                )
                print(
                    colorama.Fore.CYAN + next(save_exit_menu_iter), end=""
                )
            except StopIteration:
                ...
            print()
