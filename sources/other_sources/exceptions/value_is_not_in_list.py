class ValueIsNotInList:
    def __init__(self, value, epilog=None, matches=None, lower=True, strip=True):
        self.value = value
        self.epilog = epilog
        self.matches = matches
        self.lower = lower
        self.strip = strip
        self.found = list()

    def value_is_not_in_list(self):
        for value in self.matches:
            if isinstance(value, str) or isinstance(value, bytes) and self.lower:
                value = value.lower()

            if isinstance(value, str) or isinstance(value, bytes) and self.strip:
                value = value.strip()

            if value == self.value:
                self.found.append(value)

        if not len(self.found) >= 1:
            if self.epilog is not None:
                print(f"\n{self.epilog}", end="")
                return False

            return False

        return True
