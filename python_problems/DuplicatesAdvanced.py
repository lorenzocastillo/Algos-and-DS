from helpers.RandomGenerators import get_iterable
from python_problems.TestSuite import Assert


def dups(arr, k=10000, d=0):
    """

    :param arr:
    :param k: distance between duplicates allowed in array
    :param d: distance value allowed to be considered fuzzy
    :return:
    """
    bins = dict()
    for i, a in enumerate(arr):
        b = a // (d+1)
        for delta in (-1, 0, 1):
            if b+delta in bins and abs(bins[b+delta] - a) <= d:
                print("%i is a duplicate " % a)
                return True
        bins[b] = a
        old = i - k
        if old >= 0:
            del bins[arr[old]//(d+1)]

    return False


def test():
    arr = [8, 1, 15, 11, 1, 9, 19, 5, 2, 3, 8, 7, 4, 10]
    f = dups
    Assert(True, f, arr)
    Assert(False, f, arr, 2)
    Assert(True, f, arr, 3)
    Assert(True, f, arr, 2, 1)


if __name__ == '__main__':
    test()