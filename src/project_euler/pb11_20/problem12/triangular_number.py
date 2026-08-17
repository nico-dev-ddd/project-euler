import math


def triangular_number(n: int) -> int:
    return n * (n + 1) // 2


def nb_divisors_opt(n: int) -> int:
    if n == 1:
        return 1
    nb_div = 2
    for d in range(2, math.floor(math.sqrt(n)) + 1):
        if n % d == 0:
            nb_div += 1
            if n != d**2:
                nb_div += 1

    print(n, "a", nb_div, "diviseurs")
    return nb_div


def first_triangular_number(nb_max_divisors: int) -> int:
    n = 1
    while nb_divisors_opt(triangular_number(n)) < nb_max_divisors:
        n = n + 1
        print("-----", n)
    return triangular_number(n)


if __name__ == "__main__":
    print(first_triangular_number(500))
