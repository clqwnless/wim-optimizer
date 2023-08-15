class ValueIsNone:
    def __init__(self, value, epilog):
        self.value = value
        self.epilog = epilog

    def value_is_none(self):
        if self.value is None:
            print(
                f"\n[*ERROR] {self.epilog} value cannot be None"
            )
            return True

        return False
