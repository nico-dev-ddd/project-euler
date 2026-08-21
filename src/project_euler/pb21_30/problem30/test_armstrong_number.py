import pytest

from project_euler.pb21_30.problem30.armstrong_number import (
    numbers_sum_of_power_of_digits,
)


@pytest.mark.parametrize(
    "power, expected",
    [
        (2, set()),
        (3, {153, 370, 371, 407}),
        (4, {1634, 8208, 9474}),
        (5, {4150, 4151, 54748, 92727, 93084, 194979}),
    ],
)
def test_numbers_sum_of_power_of_digits(power: int, expected: set[int]) -> None:
    assert numbers_sum_of_power_of_digits(power) == expected
