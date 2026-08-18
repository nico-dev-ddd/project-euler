from timeit import timeit

from project_euler.shared.sum.sum_divisors import sum_divisors


def is_abundant_number(n: int) -> bool:
    """Whether n is smaller than the sum of its proper divisors.

    Args:
        n: the number to test.

    Returns:
        True if n is an abundant number.
    """
    return sum_divisors(n) > n


def numbers_not_sum_of_two_abundant_numbers() -> set:
    abundant_numbers = [n for n in range(2, 28123) if is_abundant_number(n)]
    numbers_sum_of_two_abundant_numbers = set()
    for i, m in enumerate(abundant_numbers):
        for n in abundant_numbers[i:]:
            s = m + n
            if s > 28123:
                break
            numbers_sum_of_two_abundant_numbers.add(s)
    return set(range(1, 28124)) - numbers_sum_of_two_abundant_numbers


if __name__ == "__main__":
    print(timeit(numbers_not_sum_of_two_abundant_numbers, number=10))
