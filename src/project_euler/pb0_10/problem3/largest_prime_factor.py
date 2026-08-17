from project_euler.shared.prime_numbers import list_prime_numbers


def list_prime_factors(n: int) -> list:
    l_primes = []
    for p in list_prime_numbers(n):
        if n % p == 0:
            l_primes.append(p)
    return l_primes


def largest_prime_factor(n: int) -> int:
    return max(list_prime_factors(n))


if __name__ == "__main__":
    print(list_prime_factors(2))
    # print(largest_prime_factor(600851475143))
