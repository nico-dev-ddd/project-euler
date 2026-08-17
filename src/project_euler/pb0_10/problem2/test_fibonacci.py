import pytest

from project_euler.pb0_10.problem2.fibonacci import sum_fibonacci


@pytest.mark.parametrize(
    "limit, expected",
    [
        (1, 0),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 10),
        (9, 10),
    ],
)
def test_sum_fibonacci(limit: int, expected: int) -> None:
    assert sum_fibonacci(limit) == expected
