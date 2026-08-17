import pytest

from project_euler.pb21_30.problem22.names import score


@pytest.mark.parametrize(
    "name, expected",
    [("A", 1), ("B", 2), ("OH", 23), ("COLIN", 53)],
)
def test_name_score(name, expected):
    assert score(name) == expected
