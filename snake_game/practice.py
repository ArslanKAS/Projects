class Animal:
    def __init__(self):
        self.legs = 4
        self.tail = 1


class Wolf(Animal):
    def __init__(self):
        super().__init__()
        print(self.legs)


new_wolf = Wolf()
