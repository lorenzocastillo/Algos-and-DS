"""
Given some amount and coin denominations, find the number of ways to make change for that amount.
"""
from helpers.TestSuite import Assert


def change(amount, denominations):
    """
    The number of ways to make a change of for an amount is the sum of the ways to either use the current coin, or not.
    Improvements can be made by caching the results. However, an iterative approach will be even faster.
    :param amount:
    :param denominations:
    :return:
    """
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif len(denominations) == 0:
        return 0
    else:
        return change(amount - denominations[0], denominations) + change(amount, denominations[1:])


def change_iter(amount, denominations):
    ways_of_making_n_cents = [0]* (amount+1)
    ways_of_making_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_making_n_cents[higher_amount] += ways_of_making_n_cents[higher_amount_remainder]

    return ways_of_making_n_cents[amount]


def test():
    denominations = [1, 2, 3]
    f = change_iter
    Assert(4, f, 4, denominations)
    denominations = [2, 5, 3, 6]
    Assert(5, f, 10, denominations)
    denominations = [16, 30, 9, 17, 40, 13, 42, 5, 25, 49, 7, 23, 1, 44, 4, 11, 33, 12, 27, 2, 38, 24, 28, 32, 14, 50]
    Assert(64027917156, f, 245, denominations)
    denominations = [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26]
    Assert(168312708, f, 219, denominations)

if __name__ == '__main__':
    test()

