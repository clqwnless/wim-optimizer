class ValueDoesNotMatch:
    def __init__(self, value, match_value, epilog, lower=True, strip=True):
        self.value = value
        self.match_value = match_value
        self.epilog = epilog
        self.lower = lower
        self.strip = strip

    def value_does_not_match(self):
        if isinstance(self.value, str) or isinstance(self.value, bytes):
            if self.lower:
                self.value = self.value.lower()

            if self.strip:
                self.value = self.value.strip()

            if not self.value == self.match_value:
                print(
                    f"\n[*ERROR] {self.epilog}: {self.value}"
                )
                return True
        else:
            if not self.value == self.match_value:
                print(
                    f"\n[*ERROR] {self.epilog}: {self.value}"
                )

        return False
