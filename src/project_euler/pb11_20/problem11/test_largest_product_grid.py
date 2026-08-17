import pytest

from project_euler.pb11_20.problem11.largest_product_grid import Grid


@pytest.mark.parametrize(
    "cells, nb_adjacent, expected",
    [
        ("1", 1, 1),
        ("2", 1, 2),
        ("1 3\n2 1", 1, 3),
        ("1 3\n2 1", 2, 3),
        ("1 3 4\n2 1 5\n7 5 8", 2, 40),
    ],
)
def test_max_product_line(cells, nb_adjacent, expected):
    # GIVEN
    grid = Grid.build_grid(cells, nb_adjacent)
    # WHEN
    max_product = grid.max_product_line()
    # THEN
    assert max_product == expected


@pytest.mark.parametrize(
    "cells, nb_adjacent, expected",
    [
        ("1", 1, 1),
        ("2", 1, 2),
        (
            """
          1 3
          2 1
          """,
            1,
            3,
        ),
        (
            """
        2 3
        2 1
        """,
            2,
            4,
        ),
        (
            """
        1 3 4
        2 1 8
        7 5 5
        """,
            2,
            40,
        ),
    ],
)
def test_max_product_column(cells, nb_adjacent, expected):
    # GIVEN
    grid = Grid.build_grid(cells, nb_adjacent)
    # WHEN
    max_product = grid.max_product_column()
    # THEN
    assert max_product == expected

    # def test_max_product_diagonal(self):
    #    assert self.grid.max_product_diagonal() == 4 * 5


@pytest.mark.parametrize(
    "cells, nb_adjacent, expected",
    [
        ("1", 1, 1),
        ("2", 1, 2),
        (
            """
          1 3
          2 1
          """,
            1,
            3,
        ),
        (
            """
        2 3
        2 3
        """,
            2,
            6,
        ),
        (
            """
        1 3 4
        2 1 8
        7 5 5
        """,
            2,
            24,
        ),
        (
            """
        1 3 4 5
        2 8 8 5
        7 5 5 2
        9 7 4 9
         """,
            3,
            8 * 5 * 9,
        ),
    ],
)
def test_max_product_diagonal(cells, nb_adjacent, expected):
    # GIVEN
    grid = Grid.build_grid(cells, nb_adjacent)
    # WHEN
    max_product = grid.max_product_diagonal()
    # THEN
    assert max_product == expected


@pytest.mark.parametrize(
    "cells, nb_adjacent, expected",
    [
        ("1", 1, 1),
        ("2", 1, 2),
        (
            """
          1 3
          2 1
          """,
            1,
            3,
        ),
        (
            """
        2 3
        4 3
        """,
            2,
            12,
        ),
        (
            """
        1 3 4
        2 1 8
        7 5 5
        """,
            2,
            40,
        ),
        (
            """
        1 3 4 5
        2 8 8 5
        7 5 5 2
        1 7 4 9
         """,
            3,
            7 * 8 * 4,
        ),
    ],
)
def test_max_product_anti_diagonal(cells, nb_adjacent, expected):
    # GIVEN
    grid = Grid.build_grid(cells, nb_adjacent)
    # WHEN
    max_product = grid.max_product_anti_diagonal()
    # THEN
    assert max_product == expected
