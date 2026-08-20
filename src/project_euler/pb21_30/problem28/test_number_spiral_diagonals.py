import pytest

from project_euler.pb21_30.problem28.number_spiral_diagonals import (
    sum_of_numbers_on_the_diagonals,
)


@pytest.mark.parametrize(
    "size, expected",
    [(1, 1), (3, 25), (5, 101), (7, 261), (9, 537), (11, 961)],
)
def test_sum_of_numbers_on_the_diagonals(size: int, expected: int) -> None:
    assert sum_of_numbers_on_the_diagonals(size) == expected
