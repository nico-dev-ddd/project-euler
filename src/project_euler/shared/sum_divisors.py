"""
Somme des diviseurs
"""

import math


def sum_divisors(n: int) -> list:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        list: _description_
    """
    limit = math.floor(math.sqrt(n)) + 1
    return (
        sum(
            d + (int(n / d) if d < n / d else 0)
            for d in range(2, limit)
            if n % d == 0 and d < limit
        )
        + 1
    )
