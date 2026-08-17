import math


def list_prime_numbers(limit: float) -> list:
    """
    :param limit: bounded limit of prime numbers
    :return: list of prime numbers
    """
    limit = math.floor(limit)
    if limit == 1:
        return []
    if limit == 2:
        return [2]
    sqrt = math.sqrt(limit)
    l_primes = list(range(2, limit + 1))
    k = 2
    rk = 0
    while k <= sqrt:
        l_primes = [p for p in l_primes if p == k or p % k != 0]
        rk += 1
        k = l_primes[rk]
    return l_primes


if __name__ == "__main__":
    print(list_prime_numbers(2))
