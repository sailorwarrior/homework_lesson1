from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.a = a

    @property
    def perimeter(self):
        return self.a * 4

    @property
    def area(self):
        return self.a ** 2
