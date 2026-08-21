def sum_odd_squares(limit: int) -> int:
    sum_squares = 0
    for n in range(1, limit + 1):
        if n % 2 == 1:
            sum_squares += n * n
    return sum_squares


if __name__ == "__main__":
    print(sum_odd_squares(835000))
