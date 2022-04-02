def test_check_invalid_triangle_creation(create_invalid_triangle):
    assert create_invalid_triangle is None


def test_check_triangle_perimeter(create_triangle):
    assert create_triangle.perimeter == 42


def test_check_triangle_area(create_triangle):
    assert create_triangle.area == 84
