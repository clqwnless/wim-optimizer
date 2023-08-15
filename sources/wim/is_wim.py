from sources.wim.wim import Wim


class IsWim(Wim):
    def is_wim(self):
        if not self.wim_path.endswith(".wim"):
            print(
                "\n[*ERROR] Wim path you entered, "
                "is not straight to wim"
            )
            return False

        return True
