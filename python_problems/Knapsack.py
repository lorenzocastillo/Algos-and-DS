from TestSuite import Assert


def knapsack(c, items):
    if c < 0:
        return 0
    else:
        max_val = -10000
        for w,v in items:
            if c - w == 0:
                max_val = max(max_val, v)
            else:
                val_i = knapsack(c - w, items)
                val_i = val_i + v if val_i > 0 else 0
                max_val = max(val_i, max_val)

        return max_val


def knapsack_dynamic(capacity, items):
    cache = {}

    for w, v in items:
        if w == 0 and v != 0:
            return float('inf')

    def aux(c):
        if c < 0:
            return 0
        else:
            if c in cache:
                return cache[c]

            max_val = -10000

            for w, v in items:
                if w == 0:
                    continue

                if c - w == 0:
                    max_val = max(max_val, v)
                else:
                    val_i = aux(c - w)
                    val_i = val_i + v if val_i > 0 else 0
                    max_val = max(val_i, max_val)

            cache[c] = max_val
            return max_val

    return aux(capacity)


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

    for f in [knapsack_dynamic, knapsack_iter]:
        Assert(0, f, 0, [(1,40)])
        Assert(float('inf'), f, 100, [(0,40)])
        Assert(200, f, 3, [(1, 10), (3, 200), (0,0)])
        Assert(200, f, 3, [(1, 10), (3, 200)])
        Assert(3000, f, 3, [(1,1000),(3,200)])
        Assert(2010, f, 3, [(1, 10), (3, 200), (2, 2000)])


if __name__ == '__main__':
    test()
