from sources.main.interface.banners import init_banner
from sources.main.interface.banners import default_banner
import colorama


class ShowBanners:

    @staticmethod
    def show_init_banner():
        colorama.init()
        print(colorama.Fore.RED + init_banner)

    @staticmethod
    def show_default_banner():
        colorama.init()
        print(colorama.Fore.MAGENTA + default_banner)
