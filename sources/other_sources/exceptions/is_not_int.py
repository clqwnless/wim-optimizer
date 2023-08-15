class IsNotInt:
    def __init__(self, value, epilog, show_epilog=True):
        self.value = value
        self.epilog = epilog
        self.show_epilog = show_epilog

    def is_not_int(self):
        try:
            self.value = int(self.value)
        except ValueError:
            if not self.show_epilog:
                return True

            print(f"\n{self.epilog}")
            return True

        return False
