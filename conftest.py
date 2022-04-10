import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def create_triangle():
    return Triangle.create_valid_triangle(13, 14, 15)


@pytest.fixture()
def create_invalid_triangle():
    return Triangle.create_valid_triangle(1, 2, 15)


@pytest.fixture()
def create_rectangle():
    return Rectangle(2, 3)


@pytest.fixture()
def create_square():
    return Square(5)


@pytest.fixture()
def create_circle():
    return Circle(6)
