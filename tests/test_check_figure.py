from itertools import product


def test_check_figure_adding(create_triangle, create_rectangle, create_circle, create_square):
    expected_adding_result = [168.0, 90.0, 197.04000000000002, 109.0, 90.0, 12, 119.04, 31, 197.04000000000002, 119.04,
                              226.08, 138.04000000000002, 109.0, 31, 138.04000000000002, 50]

    first_figures_list = [create_triangle, create_rectangle, create_circle, create_square]
    second_figures_list = first_figures_list.copy()
    actual_adding_result = []
    for pair in list(product(first_figures_list, second_figures_list)):
        actual_adding_result.append(pair[0].add_area(pair[1]))
    assert actual_adding_result == expected_adding_result


def test_check_not_figure_adding(create_triangle, create_rectangle, create_circle, create_square):
    figures_list = [create_triangle, create_rectangle, create_circle, create_square]
    for figure in figures_list:
        is_valid = True
        try:
            figure.add_area('create_triangle')
        except ValueError:
            is_valid = not is_valid
        assert is_valid is False
