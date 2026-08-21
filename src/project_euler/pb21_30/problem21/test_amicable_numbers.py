import pytest

from project_euler.pb21_30.problem21.amicable_numbers import is_amicable_numbers


@pytest.mark.parametrize(
    "m, n",
    [
        (220, 284),
        (1184, 1210),
        (63020, 76084),
    ],
)
def test_is_amicable_number(m: int, n: int) -> None:
    assert is_amicable_numbers(m, n)
