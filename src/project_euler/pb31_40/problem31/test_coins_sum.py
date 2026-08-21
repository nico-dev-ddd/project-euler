import pytest

from project_euler.pb31_40.problem31.coins_sum import (
    count_different_ways_to_make_change,
)


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (1, [1], 1),
        (2, [1, 2], 2),
        (3, [1, 2], 2),
        (5, [1, 2, 5], 4),
        (10, [1, 2, 5, 10], 11),
    ],
)
def test_count_different_ways_to_make_change(
    amount: int, coins: list[int], expected: int
) -> None:
    assert count_different_ways_to_make_change(amount, coins) == expected
