import pytest

from project_euler.pb11_20.problem12.triangular_number import first_triangular_number


@pytest.mark.parametrize(
    "nb_divisors, expected", [(1, 1), (2, 3), (3, 6), (4, 6), (5, 28)]
)
def test_first_triangular_number(nb_divisors: int, expected: int) -> None:
    assert first_triangular_number(nb_divisors) == expected
