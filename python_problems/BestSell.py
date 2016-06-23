from TestSuite import Assert
"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of the stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1
purchase and 1 sale of 1 stock yesterday.

"""


def best_sell(prices):
    """
    Given the prices, we remember the minimum price we have seen so far and the best sell. We iterate through the prices.
    If price >= prev, then we are better off selling now, so we update the best price.
    Else If the price < prev, then we might as well have not bought anything before, and set this as the minimum price
    :param prices:
    :return:
    """
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


def test():
    prices = [4, 2, 7, 1, 3, 2, 1, 6, 5, 8, 0, 2]
    Assert(7, best_sell, prices)
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Assert(8, best_sell, prices)
    prices = [10, 5, 2, 1]
    Assert(-100000, best_sell, prices)

if __name__ == '__main__':
    test()

