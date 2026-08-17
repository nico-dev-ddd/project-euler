"""
Amicable number
"""

from project_euler.shared.sum_divisors import sum_divisors


def is_amicable_numbers(m: int, n: int) -> bool:
    """
    Determine whether two numbers are amicable.
    """
    return sum_divisors(m) == n and sum_divisors(n) == m


def amicable_numbers(limit: int) -> list:
    """List all amicable pairs (m, n) with m < n < limit.

    Args:
        limit: exclusive upper bound for m.

    Returns:
        A list of (m, n) amicable pairs.
    """
    amicable_nb = list()
    for m in range(limit):
        n = sum_divisors(m)
        if m < n and is_amicable_numbers(m, n):
            amicable_nb.append((m, n))
    return amicable_nb


def sum_amicable_numbers(limit: int) -> int:
    """Sum of all numbers in amicable pairs below limit.

    Args:
        limit: exclusive upper bound for the amicable pairs.

    Returns:
        The sum of all amicable numbers under limit.
    """
    return sum([m + n for m, n in amicable_numbers(limit)])


if __name__ == "__main__":
    print(sum_amicable_numbers(10000))
