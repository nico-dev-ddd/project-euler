def list_fibonacci(limit: int) -> list:
    if limit == 0:
        return []
    if limit == 1:
        return [1]
    if limit == 2:
        return [1, 2]
    n = 1
    l_fibonacci = [1, 2]
    while True:
        n += 1
        current_term = l_fibonacci[n - 1] + l_fibonacci[n - 2]
        if current_term > limit:
            break
        l_fibonacci.append(current_term)

    return l_fibonacci


def sum_fibonacci(limit: int) -> int:
    return sum([f for f in list_fibonacci(limit) if f % 2 == 0])


if __name__ == "__main__":
    print(sum_fibonacci(4000000))
