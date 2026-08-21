def numbers_sum_of_power_of_digits(power: int) -> set[int]:
    return set(
        n
        for n in range(10, 10 ** (power + 1))
        if n == sum(int(digit) ** power for digit in str(n))
    )


if __name__ == "__main__":
    power = 5
    armstrong_numbers = numbers_sum_of_power_of_digits(power)
    print(f"Sum of Armstrong numbers for power {power}: {sum(armstrong_numbers)}")
