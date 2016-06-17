

def change(amount, denominations):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif len(denominations) == 0:
        return 0
    else:
        current_coin, denominations_left = denominations[0], denominations[1:]
        ways = 0
        while amount >= 0:
            ways += change(amount, denominations_left)
            amount -= current_coin
        return ways


def change_2(amount, denominations):
    ways_of_making_n_cents = [0]* (amount+1)
    ways_of_making_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_making_n_cents[higher_amount] += ways_of_making_n_cents[higher_amount_remainder]

    return ways_of_making_n_cents[amount]



denominations = [1,2,3]
print(change(9, denominations))
print(change_2(9, denominations))