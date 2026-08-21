numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1_000: "thousand",
}


def write_number(n: int) -> str:
    if n == 100:
        return "one hundred"
    if n == 1000:
        return "one thousand"
    if n in numbers:
        return numbers[n]
    hundreds = n // 100
    return (
        write_hundreds(hundreds)
        + (" and " if hundreds > 0 and n % 100 != 0 else "")
        + write_under_hundred(n % 100)
    )


def write_under_hundred(n: int) -> str:
    if n == 0:
        return ""
    if n in numbers:
        return numbers[n]
    dozen = n // 10
    return numbers[dozen * 10] + "-" + numbers[n % 10]


def write_hundreds(hundreds: int) -> str:
    return numbers[hundreds] + " " + numbers[100] if hundreds > 0 else ""


def clean_number(param: str) -> str:
    return param.replace("-", "").replace(" ", "")


def count_letters(n: int) -> int:
    return len(clean_number(write_number(n)))


def count_total_letters(limit: int) -> int:
    return sum([count_letters(n) for n in range(1, limit + 1)])


if __name__ == "__main__":
    print(count_total_letters(1_000))
