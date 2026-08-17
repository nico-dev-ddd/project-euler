def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def length_seq_collatz(n: int) -> int:
    length = 0
    s = n
    while s != 1:
        s = collatz(s)
        length += 1
    return length + 1


def longest_collatz(limit: int) -> int:
    max_length = 0
    n_max = 0
    for i in range(1, limit + 1):
        length = length_seq_collatz(i)
        if length > max_length:
            max_length = length_seq_collatz(i)
            n_max = i
    print("n_max = ", n_max, " => ", "max_length =", max_length)
    return n_max


if __name__ == "__main__":
    print(longest_collatz(1_000))
    print(longest_collatz(10_000))
    print(longest_collatz(100_000))
    print(longest_collatz(1_000_000))
