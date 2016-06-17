from functools import reduce
from TestSuite import Assert

"""
Given a list_of_ints, find the highest_product you can get from k of the integers.
"""
def highest_product_of_3(arr, k=3):
    if len(arr) < k:
        return -1
    if k == 1:
        return max(arr)
    elif k == 2:
        sorted_arr = sorted(arr)
        return max(sorted_arr[0]*sorted_arr[1], sorted_arr[-1]*sorted_arr[-2])


    lowest_k_minus_2 = sorted(arr[:k-1])[:k-2]
    highest_k_minus_2 = sorted(arr[:k-1], reverse=True)[:k-2]
    lowest_prod_of_k_minus_one = 1
    highest_prod_of_k_minus_one = 1

    for cur in arr[:k-1]:
        highest_prod_of_k_minus_one *= cur
        lowest_prod_of_k_minus_one *= cur

    highest_prod_of_k = highest_prod_of_k_minus_one * arr[k-1]

    arr = sorted(arr)

    for i in range(0, len(arr)):
        cur = arr[i]

        highest_prod_of_k = max(highest_prod_of_k, lowest_prod_of_k_minus_one * cur, highest_prod_of_k_minus_one * cur)

        potential_lowest = reduce(lambda x, y: x * y, lowest_k_minus_2, cur)
        potential_highest = reduce(lambda x,y: x * y, highest_k_minus_2, cur)

        lowest_prod_of_k_minus_one = min(lowest_prod_of_k_minus_one, potential_highest, potential_lowest)
        highest_prod_of_k_minus_one = max(highest_prod_of_k_minus_one, potential_highest, potential_lowest)

        lowest_k_minus_2 = sorted(lowest_k_minus_2 + [cur])[:k - 2]
        highest_k_minus_2 = sorted(highest_k_minus_2 + [cur], reverse=True)[:k - 2]

    return highest_prod_of_k


def test():
    f = highest_product_of_3
    arr = [2,1,4,6,5,5,3]

    Assert(150, f, arr, 3)
    Assert(600,f, arr, 4)
    arr = [-1,-100,3,4,2,4,5]
    Assert(500, f, arr, 3)
    Assert(2000, f, arr, 4)
    arr = [1, 2, 3, -10, 1, -10, 1, -10, 2, -10]
    Assert(30000, f, arr, 5)
    Assert(300, f, arr, 3)

if __name__ == '__main__':
    test()