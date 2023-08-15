class Choice:
    __choices = [
        str(i) for i in range(1, 19)
    ]

    def select_choice(self):
        try:
            choice = input(
                "\n>>> "
            )
        except KeyboardInterrupt:
            return False, None

        if choice not in self.__choices:
            return False, None

        return True, int(choice)
