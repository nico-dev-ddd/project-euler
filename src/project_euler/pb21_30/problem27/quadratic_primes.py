from project_euler.shared.primes.prime_numbers import Prime


def quadratic_function(a, b):
    return lambda n: n * n + a * n + b


def product_the_coefficients_with_maximum_number_of_primes(
    a_max: int, b_max: int
) -> int:
    max = 0
    a_optimal = 0
    b_optimal = 0
    primes = Prime.list_prime_numbers(b_max)
    for b in primes:
        borne = min(a_max, b)
        for a in range(-borne, borne + 1):
            longueur_max = 0
            for n in range(0, b_max + 1):
                val = quadratic_function(a, b)(n)
                if val < 1 or not Prime.is_prime(val):
                    longueur_max = n
                    break
            if longueur_max > max:
                max = longueur_max
                a_optimal = a
                b_optimal = b
    print(
        f"longueur maximale de {max} obtenue avec ",
        f"a_optimal = {a_optimal}, b_optimal = {b_optimal}",
    )
    return a_optimal * b_optimal


if __name__ == "__main__":
    print(product_the_coefficients_with_maximum_number_of_primes(999, 1000))
