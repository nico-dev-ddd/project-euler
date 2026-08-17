def power_digit_sum(n, m):
    return sum(int(digit) for digit in str(n**m))


if __name__ == "__main__":
    print(power_digit_sum(2, 50))
    print(power_digit_sum(2, 100))
    print(power_digit_sum(2, 500))
    print(power_digit_sum(2, 1_000))
