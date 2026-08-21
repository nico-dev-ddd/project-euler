def prepare_values(file_name: str) -> list[list[int]]:
    with open(file_name) as file:
        values_string = file.readlines()
    return [list(int(val) for val in line.strip().split()) for line in values_string]


def max_path_sum(pyramid: list[list[int]]) -> int:
    max_sum = pyramid
    for stage in range(len(pyramid) - 1, 0, -1):
        for i in range(len(pyramid[stage - 1])):
            max_sum[stage - 1][i] = pyramid[stage - 1][i] + max(
                max_sum[stage][i], max_sum[stage][i + 1]
            )
    return max_sum[0][0]


if __name__ == "__main__":
    values = prepare_values("triangle.txt")
    print(max_path_sum(values))
