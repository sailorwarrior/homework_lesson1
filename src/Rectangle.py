from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter = a * 2 + b * 2
        self.area = a * b

rectangle = Rectangle(2, 3)
ra = rectangle.area
