from src.Figure import Figure


class Square(Figure):
    PI = 3.14

    def __init__(self, r):
        self.r = r
        self.perimeter = 2 * r * self.PI
        self.area = r ** 2 * self.PI
