import pytest

from project_euler.pb21_30.problem24.permutation import ith_permutation


@pytest.mark.parametrize(
    "elements, i, expected",
    [
        ({0, 1}, 1, "01"),
        ({0, 1}, 2, "10"),
        ({0, 1, 2}, 2, "021"),
        # ({0, 1, 2}, 4, "120"),
    ],
)
def test_ith_permutation(elements: list, i: int, expected: str) -> None:
    assert ith_permutation(elements, i) == expected
