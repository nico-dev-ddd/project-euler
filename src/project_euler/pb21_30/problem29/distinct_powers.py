from __future__ import annotations

from project_euler.shared.primes.prime_numbers import Prime


class Valuation:
    n: int
    valuations: tuple[int, ...]

    def __init__(self, n: int, primes: list[int]) -> None:
        self.n = n
        self.valuations = self._calculate_valuations(primes)

    def _calculate_valuations(self, primes: list[int]) -> tuple[int, ...]:
        valuations = len(primes) * [0]
        for index, p in enumerate(primes):
            val = self._valuation(p)
            if val:
                valuations[index] = val
        return tuple(valuations)

    def _valuation(self, p: int) -> int:
        k = 1
        while self.n % p**k == 0:
            k = k + 1
        return k - 1

    def power(self, b: int) -> tuple[int, ...]:
        return tuple(b * v for v in self.valuations)


def count_distinct_powers(a_max: int, b_max: int) -> int:
    powers = set()
    primes = Prime.list_prime_numbers(a_max)
    for a in range(2, a_max + 1):
        valuations = Valuation(a, primes)
        for b in range(2, b_max + 1):
            powers.add(valuations.power(b))
    return len(powers)


if __name__ == "__main__":
    print(count_distinct_powers(100, 100))
