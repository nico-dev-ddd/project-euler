import pytest

from project_euler.pb11_20.problem16.power_digit_sum import power_digit_sum


@pytest.mark.parametrize(
    "n, m, expected", [(1, 1, 1), (2, 3, 8), (2, 4, 7), (2, 15, 26)]
)
def test_power_digit_sum(n, m, expected):
    assert power_digit_sum(n, m) == expected
