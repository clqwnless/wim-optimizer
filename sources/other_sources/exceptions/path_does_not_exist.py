import os


class PathDoesNotExist:
    def __init__(self, path, epilog):
        self.path = path
        self.epilog = epilog

    def path_does_not_exist(self):
        if not os.path.exists(self.path):
            print(
                f"\n[*ERROR] {self.epilog} path does not exist"
            )
            return True

        return False
