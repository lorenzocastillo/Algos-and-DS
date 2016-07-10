"""
Given an array, rotate the array k times:
ex:
[1, 2, 3, 4], k = 1 => [4, 1, 2, 3]
[1, 2, 3, 4], k = -1 => [2, 3, 4, 1]
[1, 2, 3, 4], k = 2 => [3, 4, 1, 2]
"""
from helpers.TestSuite import Assert


def rotate_in_place(arr, k=1):
    """
    First, reverse the entire array. Then, reverse the array from [0, k) and again from [k, n)
    :param arr: array to be rotated
    :param k: number of times for array to be rotated
    :return:
    """
    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    n = len(arr)
    # converts negative to positive and if k > n.
    k = (k + n) % n
    arr = arr.copy()
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return arr


def test():
    arr = [1, 2, 3, 4, 5, 6, 7]
    f = rotate_in_place
    Assert([3, 4, 5, 6, 7, 1, 2], f, arr, -2)
    Assert([1, 2, 3, 4, 5, 6, 7], f, arr, 0)
    Assert([6, 7, 1, 2, 3, 4, 5], f, arr, 2)
    Assert([6, 7, 1, 2, 3, 4, 5], f, arr, 9)

if __name__ == '__main__':
    test()
