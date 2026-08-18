import pytest

from project_euler.shared.primes.prime_numbers import Prime


@pytest.mark.parametrize(
    "limit, expected",
    [
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (4, [2, 3]),
        (5, [2, 3, 5]),
        (6, [2, 3, 5]),
        (7, [2, 3, 5, 7]),
        (8, [2, 3, 5, 7]),
        (9, [2, 3, 5, 7]),
        (10, [2, 3, 5, 7]),
        (11, [2, 3, 5, 7, 11]),
        (12, [2, 3, 5, 7, 11]),
    ],
)
def test_list_prime_numbers(limit:int, expected:list) -> None:
    assert Prime.list_prime_numbers(limit) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, False), (2,True),(3,True)
    ],
)
def test_is_prime(n:int, expected:bool) -> None:
    assert Prime.is_prime(n) == expected
