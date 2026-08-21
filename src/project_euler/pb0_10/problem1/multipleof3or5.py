def sum_multiples(limit: int) -> int:
    sum_mult = 0
    for current_number in range(1, limit):
        if current_number % 3 == 0 or current_number % 5 == 0:
            sum_mult = sum_mult + current_number
    return sum_mult


if __name__ == "__main__":
    print(sum_multiples(1000))
