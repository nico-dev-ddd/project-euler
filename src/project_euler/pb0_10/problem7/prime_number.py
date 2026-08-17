"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and we can see that the 6th prime is 13
What is the 10 001st prime number ?
"""

import math

from project_euler.shared.prime_numbers import list_prime_numbers


def nth_prime_number(n: int) -> int:
    if n == 1:
        return 2
    if n == 2:
        return 3
    return list_prime_numbers(n * (math.log(n, 2) ** 2))[n - 1]


if __name__ == "__main__":
    print("10eme premier : ", nth_prime_number(10))
    print("100eme premier : ", nth_prime_number(100))
    print("1000eme premier : ", nth_prime_number(1000))
    print("10001eme premier : ", nth_prime_number(10001))
