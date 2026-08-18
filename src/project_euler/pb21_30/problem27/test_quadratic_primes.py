import pytest

from project_euler.pb21_30.problem27.quadratic_primes import (
    product_the_coefficients_with_maximum_number_of_primes,
)


@pytest.mark.parametrize("a_max,b_max, expected", [(0,1, 0), (3,1,-3)])
def test_tdd_quadratic_primes(a_max:int, b_max: int, expected: int) -> None:
    assert (
        product_the_coefficients_with_maximum_number_of_primes(a_max,b_max) == expected
    )
