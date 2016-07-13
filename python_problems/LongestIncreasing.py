"""
Given a list of numbers, find the longest "increasing by one" subarray. What if you're allowed 1 mistake?
"""
from collections import namedtuple
from helpers.TestSuite import Assert


def range_size(x):
    """
    determines the size of a range x
    :param x: a range tuple (start, end)
    :return: the size of the range
    """
    return x[1] - x[0]


def longest_increasing(arr):
    start = 0
    longest = (start,0)
    for i in range(1, len(arr)):
        if arr[i - 1] + 1 != arr[i]:
            start = i + 1
        longest = max(longest, (start, i), key=range_size)
    return longest


def longest_increasing_mistake(arr):
    """
    Iterate through the array, if a mistake is found, keep track of the last occurrence of a mistake so that if
    we make another mistake, we can restart our range from that spot.
    :param arr:
    :return:
    """
    m = 1
    Range = namedtuple('Range', 'start end last_valid')
    longest = Range(0, 0, 0)
    cur = 1
    prev = Range(0, 0, arr[0])
    mistakes = 0
    last_mistake = 1
    while cur < len(arr):
        if prev.last_valid + 1 != arr[cur]:
            mistakes += 1
            if mistakes > m:
                mistakes = 1
                prev = Range(last_mistake + 1, cur, arr[cur - 1])
            last_mistake = cur
            prev = Range(prev.start, cur, prev.last_valid)
        else:
            prev = Range(prev.start, cur, arr[cur])
        longest = max(prev, longest, key=range_size)
        cur += 1
    return longest[:2]


def test():
    arr = [2, 3, 4, -9, 5, 6, -2, 7, 8, 9, 10, 11]
    f = longest_increasing_mistake
    Assert((4, 11), f, arr)
    arr = [1, 2, 3, 4, 5, 6, 7]
    Assert((0, 6), f, arr)
    arr = [6, 5, 4, 3, 2]
    Assert((0, 1), f, arr)

if __name__ == '__main__':
    test()

