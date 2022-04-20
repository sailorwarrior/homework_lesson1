import pytest

from src.lesson2.Circle import Circle
from src.lesson2.Rectangle import Rectangle
from src.lesson2.Square import Square
from src.lesson2.Triangle import Triangle


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action='store', default='type1', help="my option: type1 or type2")
    parser.addoption("--url", default='https://ya.ru', help='Base url')
    parser.addoption("--status_code", default='200', help='Status codes')


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


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("---cmdopt")


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def status_code(request):
    return request.config.getoption('--status_code')
