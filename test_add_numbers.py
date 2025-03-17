import pytest

def add_numbers(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [(3, 5, 8), (-2, -3, -5), (5, -3, 2), (0, 7, 7), (10, 0, 10)])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected