import pytest

from project_euler.pb21_30.problem23.abundant_number import is_abundant_number


@pytest.mark.parametrize("n, expected", [(1, False), (12, True), (10, False)])
def test_is_abundant_number(n: int, expected: bool) -> None:
    assert is_abundant_number(n) == expected
