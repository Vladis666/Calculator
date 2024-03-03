import pytest


def int_sub(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    return int(a - b)


def int_sum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    return int(a + b)


def int_mult(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    return int(a * b)


def int_dev(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    if b == 0:
        raise TypeError("The denominator of the expression is equal to zero --> Inf ")
    return a / b


def test_division_integers():
    assert int_dev(10, 2) == 5, "Should return the correct division result for two integers"


def test_division_floats():
    assert int_dev(9.0, 3.0) == 3.0, "Should return the correct division result for two floats"


def test_division_negative_numbers():
    assert int_dev(-10, -5) == 2, "Should handle division with negative numbers correctly"


def test_division_by_zero():
    with pytest.raises(TypeError):
        int_dev(5, 0), "Should raise an error when dividing by zero"


def test_division_with_zero_numerator():
    assert int_dev(0, 5) == 0, "Should return zero when numerator is zero"


def test_division_string_input():
    with pytest.raises(TypeError):
        int_dev('10', '2'), "Should raise a TypeError when input is not a number"


def test_multiply_integers():
    assert int_mult(3, 4) == 12, "Should return the product of two integers"


def test_multiply_floats():
    assert int_mult(2.5, 4.0) == 10, "Should return the integer product of two floats"


def test_multiply_negative_numbers():
    assert int_mult(-2, 3) == -6, "Should return the product of a negative and a positive number"


def test_multiply_by_zero():
    assert int_mult(0, 5) == 0, "Multiplying by zero should return zero"


def test_multiply_negative_floats():
    assert int_mult(-2.5, -4.0) == 10, "Should return the product of two negative floats as a positive integer"


def test_multiply_string_input():
    with pytest.raises(TypeError):
        int_mult('4', '5')


@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 25),
    (2, 8, 16),
    (3, -3, -9),
    (-4, -5, 20),
    (0, 10, 0),
])
def test_multiplication_independence_from_order_and_type(a, b, expected):
    assert int_mult(a, b) == expected, "Should correctly multiply two numbers regardless of their order and type"


def test_sub_integers():
    assert int_sub(7, 5) == 2, "Should return the difference of two integers"


def test_sub_floats():
    assert int_sub(5.5, 2.5) == 3, "Should return the integer difference of two floats"


def test_sub_negative_numbers():
    assert int_sub(-4, -6) == 2, "Should return the difference of two negative numbers"


def test_sub_string_input():
    with pytest.raises(TypeError):
        int_sub('4', '5')


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
    (20, 4, 5),
    (15, 3, 5),
    (10.0, 2.5, 4.0),
    (-8, 2, -4),
    (-9, -3, 3)
])
def test_division_parametrized(a, b, expected):
    assert int_dev(a, b) == expected, "Should return the correct division result for given inputs"


@pytest.mark.parametrize("a, b, expected", [
    (4, 5, 9),
    (5, 4, 9),
])
def test_independence_from_order(a, b, expected):
    assert int_sum(a, b) == expected, "Should be independent from the order of inputs"


@pytest.mark.parametrize("a, b, expected", [
    (1, 4, -3),
    (9, 2, 7),
])
def test_independence_from_order_sub(a, b, expected):
    assert int_sub(a, b) == expected, "Should be independent from the order of inputs"


@pytest.mark.parametrize("a, b, expected_difference", [
    (4, 5, -1),
    (5, 4, 1),
])
def test_subtraction_order(a, b, expected_difference):
    assert int_sub(a, b) == expected_difference, "Subtraction result should depend on the order of inputs"
