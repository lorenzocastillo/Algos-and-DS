def best_sell(prices):
    best = -100000
    min_ = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        prev = prices[i-1]
        if price >= prev:
            best = max(best, price - min_)
        else:
            min_ = min(price, min_)

    return best


prices = [4, 2, 7, 1, 3, 2, 1, 6, 5, 8, 0, 2]
print(best_sell(prices))
prices = [1, 2, 3, 4, 5, 6, 7, 8]
print(best_sell(prices))
prices = [10, 5, 2, 1]
print(best_sell(prices))
