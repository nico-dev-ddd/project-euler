import pytest

from project_euler.pb61_70.problem67.maximum_path_sum_ii import max_path_sum


@pytest.mark.parametrize(
    "pyramid, expected",
    [
        ([(1,)], 1),
        ([(2,)], 2),
        ([[2], [5, 3]], 7),
        (
            [
                [
                    2,
                ],
                [5, 3],
                [1, 2, 8],
            ],
            13,
        ),
        (
            [
                [
                    3,
                ],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3],
            ],
            23,
        ),
    ],
)
def test_maximum_path_sum(pyramid, expected):
    assert max_path_sum(pyramid) == expected
