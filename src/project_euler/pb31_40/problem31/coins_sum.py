def count_different_ways_to_make_change(amount: int, coins: list[int]) -> int:
    """
    Count the number of different ways to make change for a given
    amount using the provided coin denominations.

    :param amount: The total amount for which we want to make change.
    :param coins: A list of coin denominations available for making change.
    :return: The number of different ways to make change for the given amount.
    """
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        if coin <= amount:
            for sub_amount in range(coin, amount + 1):
                ways[sub_amount] += ways[sub_amount - coin]
    return ways[amount]


if __name__ == "__main__":
    print(count_different_ways_to_make_change(200, [1, 2, 5, 10, 20, 50, 100, 200]))
