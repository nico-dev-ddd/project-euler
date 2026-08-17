import pytest

from project_euler.pb0_10.problem3.largest_prime_factor import largest_prime_factor


@pytest.mark.parametrize("n, expected", [(2, 2), (3, 3), (4, 2), (5, 5), (6, 3)])
def test_largest_prime_factor(n, expected):
    assert largest_prime_factor(n) == expected
