class IsNotStraightPath:
    def __init__(self, path, end, epilog):
        self.path = path
        self.end = end
        self.epilog = epilog

    def is_not_straight_path(self):
        if not self.path.endswith(self.end):
            print(
                "\n[*ERROR] Path you entered "
                f"is not straight to: {self.epilog}"
            )
            return True

        return False
