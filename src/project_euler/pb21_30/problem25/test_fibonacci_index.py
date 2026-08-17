import pytest

from project_euler.pb21_30.problem25.fibonacci_index import (
    index_first_term_with_n_digits,
)


@pytest.mark.parametrize("n_digits, expected", [(1, 1), (2, 7), (3, 12)])
def test_index_first_term_with_n_digits(n_digits: int, expected: int) -> None:
    assert index_first_term_with_n_digits(n_digits) == expected
