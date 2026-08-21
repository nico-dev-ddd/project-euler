import math


class Triplet:
    a: int
    b: int
    c: int

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_pythagorean(self) -> bool:
        return self.a**2 + self.b**2 == self.c**2

    def product(self) -> int:
        return self.a * self.b * self.c

    def __str__(self) -> str:
        return f"Triplet({str(self.a)}, {str(self.b)}, {str(self.c)})"


def find_pythagorian_triplets(sum_triplets: int) -> Triplet | None:
    for a in range(1, math.floor(sum_triplets / 3)):
        for b in range(a + 1, math.floor((sum_triplets - a) / 2)):
            triplet = Triplet(a, b, sum_triplets - a - b)
            if triplet.is_pythagorean():
                return triplet
    return None


if __name__ == "__main__":
    p = find_pythagorian_triplets(sum_triplets=1000)
    print(p)
    print(p.product())
