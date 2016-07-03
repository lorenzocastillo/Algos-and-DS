"""
We have a list of integers, where:

The integers are in the range
1..n
The list has a length of
n + 1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates,
and each duplicate may appear more than twice.
"""


def count_le(arr, x):
    """
    Find the numbers in the array that are less than x
    :param arr:
    :param x:
    :return:
    """
    count_lt = 0
    count_e = 0
    for elem in arr:
        if elem < x:
            count_lt += 1
        elif elem == x:
            count_e += 1
    return count_lt, count_e


def find_repeat(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end)/2)
        count_lt, count_e = count_le(arr, mid)
        if count_e > 1:
            return mid
        elif count_lt + count_e == mid:
            start = mid + 1
        elif count_lt + count_e > mid:
            end = mid - 1
    raise RuntimeError("No duplicates")


arr = [2,1,4,5,3,2]
print(find_repeat(arr))