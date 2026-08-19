"""
Sum of divisors
"""

import math


def sum_divisors(n: int) -> int:
    """Sum of the proper divisors of n (divisors of n excluding n itself).

    Args:
        n: the number to sum divisors of.

    Returns:
        The sum of the proper divisors of n.
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
