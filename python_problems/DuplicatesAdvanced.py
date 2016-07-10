"""
Given an array of integers, determine if there are any fuzzy duplicates a distance of k from each other.
A fuzzy duplicate is a value that differs by d
Ex: fuzzy_dup(4, d= 2) -> 2, 3, 4, 5, 6
"""
from helpers.TestSuite import Assert


def dups(arr, k=10000, d=0):
    """

    :param arr:
    :param k: distance between duplicates allowed in array
    :param d: distance value allowed to be considered fuzzy
    :return:
    """
    bins = dict()
    d += 1  # To prevent division by zero
    for i, a in enumerate(arr):
        b = a // d
        for delta in (-1, 0, 1):
            if b+delta in bins and abs(bins[b+delta] - a) < d:
                print("%i is a duplicate " % a)
                return True
        bins[b] = a
        old = i - k
        if old >= 0:
            del bins[arr[old]//d ]
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
