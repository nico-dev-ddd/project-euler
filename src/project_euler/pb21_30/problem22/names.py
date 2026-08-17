import string
from urllib.request import urlopen
import csv


def score(name: str) -> int:
    alphabet = dict((val, i + 1) for i, val in enumerate(list(string.ascii_uppercase)))
    return sum(alphabet[letter] for letter in name)


def load_names() -> list:
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    with urlopen(url) as response:
        content = response.read().decode("utf-8")
    return list(csv.reader([content]))[0]


def total_score() -> int:
    names = load_names()
    names.sort()
    return sum((i + 1) * score(name) for i, name in enumerate(names))


if __name__ == "__main__":
    print(total_score())
