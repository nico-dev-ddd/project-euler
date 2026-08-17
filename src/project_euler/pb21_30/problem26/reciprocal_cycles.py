def recurring_cycle_length(d: int) -> int:
    remainder = 1 % d
    position_by_remainder = {}
    position = 0
    while remainder != 0 and remainder not in position_by_remainder:
        position_by_remainder[remainder] = position
        remainder = (remainder * 10) % d
        position += 1
    if remainder == 0:
        return 0
    return position - position_by_remainder[remainder]


def denominator_with_longest_cycle(limit: int) -> int:
    return max(range(2, limit), key=recurring_cycle_length)


if __name__ == "__main__":
    print(denominator_with_longest_cycle(1000))
