from math_series import __version__
from math_series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fabonacci_with_a_number_0():
    expected = 0
    index = 0
    actual = fibonacci(index)
    assert actual == expected


def test_fabonacci_with_a_number_5():
    expected = 5
    index = 5
    actual = fibonacci(index)
    assert actual == expected


def test_lucas_with_a_number_0():
    expected = 2
    index = 0
    actual = lucas(index)
    assert actual == expected


def test_lucas_with_a_number_5():
    expected = 7
    index = 5
    actual = lucas(index)
    assert actual == expected


def test_sum_series_with_just_an_index_10():
    expected = 55
    index = 10
    actual = sum_series(index)
    assert actual == expected


def test_sum_series_with_just_an_index_5_and_positional_arguments_2_1():
    expected = 7
    index = 5
    base1 = 2
    base2 = 1
    actual = sum_series(index, base1, base2)
    assert actual == expected
