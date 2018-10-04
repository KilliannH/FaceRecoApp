class Treshold:

    tricks = []             # mistaken use of a class variable

    def __init__(self, max_width, min_width, height):
        self.max_width = max_width
        self.min_width = min_width
        self.height = height

    def add_trick(self, trick):
        self.tricks.append(trick)
