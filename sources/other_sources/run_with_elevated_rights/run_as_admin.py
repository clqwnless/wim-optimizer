from elevate import elevate


class RunAsAdmin:
    @staticmethod
    def run_as_admin():
        try:
            elevate()
        except OSError:
            print(
                "\n[*ERROR] Script requires admin rigths"
            )
            return False

        return True
