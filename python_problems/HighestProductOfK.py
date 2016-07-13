"""
Given a list_of_ints, find the highest_product you can get from k of the integers.
"""
from helpers.TestSuite import Assert
from helpers.TraceCalls import TraceCalls


def memoize(f):
    memo = dict()

    def helper(*x):
        if x not in memo:
            memo[x] = f(*x)
        return memo[x]
    return helper


def highest_prod_k(arr, k):
    @memoize
    def f(i, k):
        if i == len(arr):
            return 1, 1
        elif k == 0:
            return 1, 1
        else:
            res1, res2 = f(i + 1, k - 1)
            res3, res4 = f(i+1, k)
            return max(arr[i] * res1, arr[i]*res2, res3, res4), \
                min(arr[i] * res1, arr[i]*res2, res3, res4)
    return max(f(0, k))


def test():
    f = highest_prod_k
    arr = [2, 1, 4, 6, 5, 5, 3]
    Assert(150, f, arr, 3)
    Assert(600,f, arr, 4)
    arr = [-1,-100,3,4,2,4,5]
    Assert(500, f, arr, 3)
    Assert(2000, f, arr, 4)
    arr = [1, 2, 3, -10, 1, -10, 1, -10, 2, -10]
    Assert(30000, f, arr, 5)
    Assert(300, f, arr, 3)
    arr = [-100, -100, 4, 2, 3, 8]
    Assert(80000, f, arr, 3)

if __name__ == '__main__':
    test()

from timeit import Timer
setup = """
from __main__ import highest_prod_k
arr = [1, 2, 3, -10, 1, -10, 1, -10, 2, -10, 4, 3, 5, 1, 2, 6, 10, -2, 10, 9, -9, 1, 2, 3, 4, 5]
"""
t = Timer(setup=setup, stmt="highest_prod_k(arr, 5)").timeit(100)
print(t)