def test_check_rectangle_perimeter(create_rectangle):
    assert create_rectangle.perimeter == 10


def test_check_rectangle_area(create_rectangle):
    assert create_rectangle.area == 6
