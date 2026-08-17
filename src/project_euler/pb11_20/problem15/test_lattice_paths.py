import pytest

from project_euler.pb11_20.problem15.lattice_paths import LatticePaths


@pytest.mark.parametrize(
    "n, m, expected", [(1, 1, 2), (1, 2, 3), (2, 1, 3), (2, 2, 6), (2, 3, 10)]
)
def test_nb_paths(n, m, expected):
    # GIVEN
    lattice_paths = LatticePaths()
    # WHEN + THEN
    assert lattice_paths.nb_paths(n, m) == expected
