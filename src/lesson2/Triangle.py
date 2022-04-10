from src.Figure import Figure


def check_triangle(a, b, c):
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        return True
    else:
        return False


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return (half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (
                half_perimeter - self.c)) ** 0.5

    @staticmethod
    def create_valid_triangle(a, b, c):
        if check_triangle(a, b, c):
            return Triangle(a, b, c)
        else:
            return None
