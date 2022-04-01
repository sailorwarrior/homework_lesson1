from src.Figure import Figure
from src.Rectangle import Rectangle


def check_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = a + b + c
        half_perimeter = self.perimeter / 2
        self.area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5


triangle = Triangle(13, 14, 15)
rectangle = Rectangle(2, 3)
print(triangle.add_area(rectangle))
