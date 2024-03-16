import pytest


# release v1.0 your surname

def power(base, exp):
    if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
        raise TypeError("Both base and exponent must be integers or floats")
    if base == 0 and exp == 0:
        raise TypeError("ArithmeticException")
    return base ** exp


def test_zero_in_power_0():
    with pytest.raises(TypeError):
        power(0, 0), "Should raise an error when zero is in power zero"


def gcd(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats")
    while b:
        a, b = b, a % b
    return abs(a)


def int_dev(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be integers or floats")
    if b == 0:
        raise TypeError("ArithmeticException")
    return a / b


def test_division_by_zero():
    with pytest.raises(TypeError):
        int_dev(5, 0), "Should raise an error when dividing by zero"


def lcm(a, b):
    # Ensure both inputs are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats")

    # Ensure neither input is zero to avoid division by zero in LCM calculation
    if a == 0 or b == 0:
        raise ValueError("Neither input can be zero")

    return abs(a * b) // gcd(a, b)


def test_lcm_positive_numbers():
    assert lcm(6, 8) == 24, "Should return the least common multiple of two positive numbers"


def test_lcm_negative_numbers():
    # LCM should always be positive, even if inputs are negative
    assert lcm(-6, 8) == 24, "Should return the least common multiple of a negative and a positive number"
    assert lcm(-6, -8) == 24, "Should return the least common multiple of two negative numbers"


def test_lcm_with_zero_raises_error():
    # Testing that providing zero as input correctly raises a ValueError
    with pytest.raises(ValueError):
        lcm(0, 8)
    with pytest.raises(ValueError):
        lcm(6, 0)
    with pytest.raises(ValueError):
        lcm(0, 0)


def test_lcm_same_number():
    # LCM of a number with itself should be itself
    assert lcm(7, 7) == 7, "LCM of a number with itself should be the number"


def test_lcm_one_is_factor_of_other():
    # If one number is a factor of the other, LCM should be the larger number
    assert lcm(5, 20) == 20, "LCM should be the larger number if one number is a factor of the other"
    assert lcm(20, 5) == 20, "LCM should be the larger number if one number is a factor of the other"


@pytest.mark.parametrize("a, b, expected", [
    (12, 18, 36),
    (18, 12, 36),
    (21, 6, 42),
    (8, 9, 72),
])
def test_lcm_various(a, b, expected):
    assert lcm(a, b) == expected, f"LCM of {a} and {b} should be {expected}"


def test_gcd_multiple():
    assert gcd(8, 4) == 4, "Should return 4 as GCD of 8 and 4"


def test_gcd_coprime():
    assert gcd(9, 28) == 1, "9 and 28 are coprime, so GCD should be 1"


def test_gcd_one_zero():
    assert gcd(0, 5) == 5, "GCD of 0 and any number should be the number itself"


def test_gcd_same_numbers():
    assert gcd(10, 10) == 10, "GCD of the same numbers should be the number itself"


def test_gcd_negative_numbers():
    assert gcd(-12, -18) == 6, "GCD should be positive even if the numbers are negative"


def test_gcd_invalid_input():
    with pytest.raises(TypeError):
        gcd('12', 18)


def test_power_positive_integers():
    assert power(2, 3) == 8, "Should calculate the power of positive integers correctly"


def test_power_negative_base():
    assert power(-2, 3) == -8, "Should handle negative base correctly"


def test_power_zero_base():
    assert power(0, 3) == 0, "Zero raised to any power should be zero"


def test_power_zero_exponent():
    assert power(2, 0) == 1, "Any number raised to the power of zero should be one"


def test_power_floats():
    assert power(2.0, 3.5) == 2.0 ** 3.5, "Should handle floats correctly"


def test_power_negative_exponent():
    assert power(2, -3) == 0.125, "Should calculate the power with negative exponent correctly"


def test_power_invalid_base():
    with pytest.raises(TypeError):
        power('2', 3)


def test_power_invalid_exponent():
    with pytest.raises(TypeError):
        power(2, '3')
