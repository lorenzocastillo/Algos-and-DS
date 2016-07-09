"""
Given some amount and coin denominations, find the number of ways to make change for that amount.
"""


def change(amount, denominations):
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


denominations = [1,2]
print(change(4, denominations))
print(change_iter(4, denominations))