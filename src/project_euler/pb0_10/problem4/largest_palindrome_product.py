def is_a_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def largest_palindrome_product(nb_digits: int) -> int:
    palindromes = []
    start = 10 ** (nb_digits - 1)
    end = 10**nb_digits
    for n in range(start, end):
        for m in range(n, end):
            if is_a_palindrome(n * m):
                palindromes.append(n * m)
    return max(palindromes)


if __name__ == "__main__":
    print(largest_palindrome_product(1))
    print(largest_palindrome_product(2))
    print(largest_palindrome_product(3))
