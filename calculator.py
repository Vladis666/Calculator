import pytest


def int_sum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    return int(a + b)


def test_integers():
    assert int_sum(5, 7) == 12, "Should return the sum of two integers"


def test_floats():
    assert int_sum(3.5, 2.5) == 6, "Should return the integer sum of two floats"


def test_negative_numbers():
    assert int_sum(-4, -6) == -10, "Should return the sum of two negative numbers"


def test_string_input():
    with pytest.raises(TypeError):
        int_sum('4', '5')


@pytest.mark.parametrize("a, b, expected", [
    (4, 5, 9),
    (5, 4, 9),
])
def test_independence_from_order(a, b, expected):
    assert int_sum(a, b) == expected, "Should be independent from the order of inputs"
