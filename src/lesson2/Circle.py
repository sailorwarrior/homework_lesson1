from src.lesson2.Figure import Figure


class Circle(Figure):
    PI = 3.14

    def __init__(self, r):
        self.r = r

    @property
    def perimeter(self):
        return 2 * self.r * self.PI

    @property
    def area(self):
        return self.r ** 2 * self.PI
