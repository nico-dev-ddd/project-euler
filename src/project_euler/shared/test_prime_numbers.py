import pytest

from project_euler.shared.prime_numbers import list_prime_numbers


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
def test_list_prime_numbers(limit, expected):
    assert list_prime_numbers(limit) == expected
