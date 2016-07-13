"""
Given a list of integers, return three numbers at distinct integers that sum to target
"""
from helpers.TestSuite import Assert


def solution(arr, target):
    arr = sorted(arr)
    prev = set()

    for i in range(len(arr)):
        s1 = target - arr[i]
        for j in range(i):
            s2 = s1 - arr[j]
            if s2 in prev and i != j:
                return tuple(sorted([arr[i], arr[j], s2]))
        prev.add(arr[i])

    return None


def optional(arr, target):
    """
    Sort the list.
    :param arr:
    :param target:
    :return:
    """
    arr = sorted(arr)

    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1

        while j < k:
            val = arr[i] + arr[j] + arr[k]
            if val < target:
                j += 1
            elif val > target:
                k -= 1
            else:
                return tuple([arr[i], arr[j], arr[k]])
    return None


def test():
    arr = [2, 1, 7, 9, 0, 6, 3, -2]
    f = optional
    Assert((-2, 1, 9), f, arr, 8)
    Assert((1, 6, 7), f, arr, 14)

if __name__ == '__main__':
    test()