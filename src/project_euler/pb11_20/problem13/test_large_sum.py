import pytest

from project_euler.pb11_20.problem13.large_sum import ten_first_digit_of_large_sum


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([37107287533902102798797998220837590246510135740250], 3710728753),
        ([1234567890123456789, 1234567890123456789], 1234567890 * 2),
    ],
)
def test_sum_large_number(numbers, expected):
    assert ten_first_digit_of_large_sum(numbers) == expected
