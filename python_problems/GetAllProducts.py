"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
"""
from helpers import RandomGenerators


def get_all_products_except_i(arr):
    product = 1
    product_arr = [1]
    for i in range(len(arr) - 1):
        product *= arr[i]
        product_arr.append(product)

    product = 1
    for i in range(len(arr) - 1, 0, -1):
        product *= arr[i]
        product_arr[i-1] *= product

    print(product_arr)

arr = RandomGenerators.get_iterable(size=5,min_num=1,max_num=5)
get_all_products_except_i([0,0,0,0])
