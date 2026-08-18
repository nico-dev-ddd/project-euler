from project_euler.shared.primes.prime_numbers import Prime


def sum_primes(limit):
    return sum(Prime.list_prime_numbers(limit))


if __name__ == "__main__":
    print("10 => ", sum_primes(10))
    print("1_000 => ", sum_primes(1_000))
    print("10_000 => ", sum_primes(10_000))
    print("100_000 => ", sum_primes(100_000))
    print("1_000_000 => ", sum_primes(1_000_000))
    print("2_000_000 => ", sum_primes(2_000_000))
