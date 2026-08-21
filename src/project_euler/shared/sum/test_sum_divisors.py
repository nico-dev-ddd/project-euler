import pytest

from project_euler.shared.sum.sum_divisors import sum_divisors


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 1),
        (4, 3),
        (12, 16),
        (28, 28),
    ],
)
def test_sum_divisors(n: int, expected: int) -> None:
    assert sum_divisors(n) == expected
