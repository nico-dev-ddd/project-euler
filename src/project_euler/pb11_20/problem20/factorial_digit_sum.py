import math


def sum_digits_factorial(n: int) -> int:
    return sum(int(d) for d in str(math.factorial(n)))


if __name__ == "__main__":
    print(sum_digits_factorial(10))
    print(sum_digits_factorial(100))
