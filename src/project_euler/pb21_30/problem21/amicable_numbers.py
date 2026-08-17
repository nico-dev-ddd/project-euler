"""
Amicable number
"""

import math

from project_euler.shared.sum_divisors import sum_divisors

# def sum_divisors(n: int) -> list:
#     """_summary_

#     Args:
#         n (int): _description_

#     Returns:
#         list: _description_
#     """
#     limit = math.floor(math.sqrt(n)) + 1
#     return sum(d + int(n / d) for d in range(2, limit) if n % d == 0 and d < limit) + 1


def is_amicable_numbers(m: int, n: int) -> bool:
    """
    Determine si deux nombres sont amicaux
    """
    return sum_divisors(m) == n and sum_divisors(n) == m


def amicable_numbers(limit: int) -> list:
    """_summary_

    Args:
        limit (int): _description_

    Returns:
        list: _description_
    """
    amicable_nb = list()
    for m in range(limit):
        n = sum_divisors(m)
        if m < n and is_amicable_numbers(m, n):
            amicable_nb.append((m, n))
    return amicable_nb


def sum_amicable_numbers(limit: int) -> int:
    """_summary_

    Args:
        limit (int): _description_

    Returns:
        int: _description_
    """
    return sum([m + n for m, n in amicable_numbers(limit)])


if __name__ == "__main__":
    print(sum_amicable_numbers(10000))
