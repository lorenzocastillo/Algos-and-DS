from functools import reduce


def diving_boards(k, short_length, long_length):
    def append_all(arr, board_lengths):
        result = []
        for a in arr:
            for b in board_lengths:
                c = a + [b]
                result.append(c)
        return result

    res = [[]]
    for i in range(k):
        res = append_all(res, [short_length, long_length])

    return set([reduce(lambda x, y: x + y, elem, 0) for elem in res])


def diving_boards_better(k, short_length, long_length):
    res = set()
    res.add(0)

    board_lengths = (short_length, long_length)

    def append_all(arr):
        result = set()
        for a in arr:
            for b in board_lengths:
                result.add(a + b)
        return result

    for i in range(k):
        res = append_all(res)

    return res


def all_lengths(k, shorter, longer):
    lengths = set()
    cache = set()

    def get_all_lengths(k, total):
        if k == 0:
            lengths.add(total)
            return
        else:
            if (k, total) in cache:
                return

            get_all_lengths(k - 1, total + shorter)
            get_all_lengths(k - 1, total + longer)
            cache.add((k,total))

    get_all_lengths(k, 0)
    return lengths

from timeit import Timer
setup ="""
from __main__ import diving_boards_better, all_lengths
f = diving_boards_better
g = all_lengths
"""
t = Timer(stmt='f(500,1,2)',setup=setup).timeit(number=10)
print(t)
t = Timer(stmt='g(500,1,2)',setup=setup).timeit(number=10)
print(t)