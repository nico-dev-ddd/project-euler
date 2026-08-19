import math


class Prime:
    @staticmethod
    def list_prime_numbers(limit: float) -> list:
        """
        :param limit: bounded limit of prime numbers
        :return: list of prime numbers
        """
        limite = math.floor(limit)
        if limite < 2:
            return []
        est_premier = bytearray([1]) * (limite + 1)
        est_premier[0:2] = b"\x00\x00"
        for candidat in range(2, math.isqrt(limite) + 1):
            if est_premier[candidat]:
                nb_multiples = (limite - candidat * candidat) // candidat + 1
                est_premier[candidat * candidat :: candidat] = bytearray(nb_multiples)
        return [n for n in range(limite + 1) if est_premier[n]]

    @staticmethod
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        return all(n % p != 0 for p in Prime.list_prime_numbers(math.sqrt(n)))


if __name__ == "__main__":
    print(Prime.list_prime_numbers(10000))
