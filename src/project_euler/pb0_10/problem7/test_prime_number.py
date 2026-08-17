import pytest

from project_euler.pb0_10.problem7.prime_number import nth_prime_number


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
        (6, 13),
    ],
)
def test_nth_prime_numbers(n: int, expected: int) -> None:
    assert nth_prime_number(n) == expected
