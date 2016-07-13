"""
Given some capacity and unlimited items with weights and values, determine which items to take that will maximize the
value in the knapsack.
"""

from helpers.TestSuite import Assert


def knapsack(capacity, items):
    cache = dict()

    for w, v in items:
        if w == 0 and v != 0:
            return float('inf')

    def value_for_cap(c):
        if c in cache:
            return cache[c]
        elif c < 0:
            return 0
        else:
            max_val = -10000

            for w, v in items:
                val_i = 0
                if w == 0:
                    continue
                elif c - w == 0:
                    val_i = v
                elif c - w > 0:
                    val_i = value_for_cap(c - w) + v

                max_val = max(max_val, val_i)

            cache[c] = max_val
            return max_val

    return value_for_cap(capacity)


def knapsack_iter(capacity, items):
    table = [0] * (capacity + 1)

    for w, v in items:
        if w == 0 and v != 0:
            return float('inf')

    for cur_capacity in range(capacity + 1):
        for w, v in items:
            remaining = cur_capacity - w
            if remaining >= 0:
                table[cur_capacity] = max(table[cur_capacity], table[remaining] + v)

    return table[capacity]


def test():

    for f in [knapsack, knapsack_iter]:
        Assert(0, f, 0, [(1,40)])
        Assert(float('inf'), f, 100, [(0,40)])
        Assert(200, f, 3, [(1, 10), (3, 200), (0,0)])
        Assert(200, f, 3, [(1, 10), (3, 200)])
        Assert(3000, f, 3, [(1,1000),(3,200)])
        Assert(2010, f, 3, [(1, 10), (3, 200), (2, 2000)])
        Assert(555, f, 20, [(7, 160), (3, 90), (2, 15)])


if __name__ == '__main__':
    test()
