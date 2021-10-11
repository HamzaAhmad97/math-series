from math_series import __version__
from math_series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fabonacci_with_a_number_0():
    expected = 0
    index = 0
    actual = fibonacci(index)
    assert actual == expected
