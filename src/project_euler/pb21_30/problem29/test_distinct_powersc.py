import pytest

from project_euler.pb21_30.problem29.distinct_powers import count_distinct_powers


@pytest.mark.parametrize(
    "a_max, b_max, expected",
    [(2, 2, 1), (3, 2, 2), (3, 3, 4), (4, 4, 8)],
)
def test_count_distinct_powers(a_max: int, b_max: int, expected: int) -> None:
    assert count_distinct_powers(a_max, b_max) == expected
