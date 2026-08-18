import pytest

from project_euler.pb11_20.problem17.number_letter_counts import (
    count_letters,
    count_total_letters,
    write_number,
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
        (6, "six"),
        (7, "seven"),
        (8, "eight"),
        (9, "nine"),
        (14, "fourteen"),
        (21, "twenty-one"),
        (92, "ninety-two"),
        (100, "one hundred"),
        (123, "one hundred and twenty-three"),
        (201, "two hundred and one"),
        (211, "two hundred and eleven"),
        (300, "three hundred"),
        (342, "three hundred and forty-two"),
        (115, "one hundred and fifteen"),
        (1000, "one thousand"),
    ],
)
def test_write_number(n, expected):
    assert write_number(n) == expected


@pytest.mark.parametrize(
    "limit, expected",
    [(5, 19), (6, 22), (7, 27), (8, 32)],
)
def test_count_total_letters(limit, expected):
    assert count_total_letters(limit) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(1, 3), (342, 23), (115, 20)],
)
def test_count_letters(n, expected):
    assert count_letters(n) == expected
