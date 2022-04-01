from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.a = a
        self.perimeter = a * 4
        self.area = a ** 2
