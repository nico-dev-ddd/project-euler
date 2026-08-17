"""
Permutation
"""


def permutations(prefix: str, elements: set[str]):
    if len(elements) == 1:
        yield prefix + next(iter(elements))
        return
    for element in sorted(elements):
        yield from permutations(prefix + element, elements - {element})


def ith_permutation(elements: list, i: int) -> int:
    """_summary_

    Args:
        elements (set): _description_
        i (int): _description_

    Returns:
        int: _description_
    """

    for k, p in enumerate(permutations("", {str(e) for e in elements}), start=1):
        if k == i:
            return p


if __name__ == "__main__":
    print(ith_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1_000_000))
