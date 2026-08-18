import math

from project_euler.shared.primes.prime_numbers import Prime


def smallest_multiple(n: int) -> int:
    list_factors = []
    for prime in Prime.list_prime_numbers(n):
        puissance = math.floor(math.log(n, prime))
        list_factors.append(prime**puissance)
    return math.prod(list_factors)


if __name__ == "__main__":
    print(smallest_multiple(20))
