import pytest

from project_euler.pb0_10.problem4.largest_palindrome_product import (
    largest_palindrome_product,
    is_a_palindrome,
)


@pytest.mark.parametrize("n, expected", [(9, True), (12, False), (11, True)])
def test_is_a_palindrome(n: int, expected: bool) -> None:
    assert is_a_palindrome(n) == expected


def test_largest_palindrome_product():
    assert largest_palindrome_product(1) == 9
    assert largest_palindrome_product(2) == 9009
