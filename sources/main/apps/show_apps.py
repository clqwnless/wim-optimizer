class ShowApps:
    def __init__(self, apps, epilog=None):
        self.apps = apps
        self.epilog = epilog

    def show_apps(self):
        if not self.apps:
            print(
                f"\n[*INFO] No {self.epilog} found"
            )
            return None

        len_max = max(len(i) for i in self.apps)

        len_max += 10

        flag = False

        for count, app in enumerate(self.apps, 1):
            if len(self.apps) == count:
                if count % 2 != 0:
                    flag = True

            if count % 2 == 0:
                if count < 9:
                    print(f"[{count}]  | " + app, end="")
                    print()
                    continue

                print(f"[{count}] | " + app, end="")
                print()

                continue

            if count <= 9:
                print(f"[{count}]  | " + app.ljust(len_max), end="")
                if flag:
                    print()

                continue

            print(f"[{count}] | " + app.ljust(len_max), end="")

            if flag:
                print()
