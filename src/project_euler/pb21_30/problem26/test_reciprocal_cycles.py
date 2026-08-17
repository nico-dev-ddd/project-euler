import pytest

from project_euler.pb21_30.problem26.reciprocal_cycles import (
    denominator_with_longest_cycle,
)


@pytest.mark.parametrize("limit, expected", [(3, 2), (4, 3)])
def test_denominator_with_longest_cycle(limit: int, expected: int) -> None:
    assert denominator_with_longest_cycle(limit) == expected
