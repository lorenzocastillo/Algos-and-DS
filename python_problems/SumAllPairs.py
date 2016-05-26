"""
Given a list of integers and some number k,
find if there is one pair of integers that sum to k
"""
from BinarySearch import binary_search


def solution_by_set(arr, k):
    """
    walk through the array.
    For each element e in arr,
        check if the e is in the set.
            If it is, we are done.
            Else, store the complement in a set.
    Complexity: Running time O(N), Space O(N)
    :param arr:
    :param k:
    :return:
    """
    complements = set()
    for a in arr:
        complement = k - a
        if a in complements:
            return True
        complements.add(complement)
    return False


def solution_by_binsearch(arr, k):
    """
    sort the array
    for each element, e, in the array
        check if the complement is in the array, given that it's not the current element
        if so, done
    Complexity: Running time O(N lg N) Space: O(1)
    :param arr:
    :param k:
    :return:
    """
    arr = sorted(arr)
    for i, a in enumerate(arr):
        complement = k - a
        res = binary_search(arr, complement)
        if res != -1 and res != i:
            return True
    return False


def solution_by_sort_efficient(arr, k ):
    """
    sort the array
    start two pointers, i,j at the start and end of array, respectively
    loop until i >= j
        sum_ = arr[i] + arr[j]
        if sum_ == k, we are done
        else if sum_ < k we need to grab a bigger number, so we increment i
        else if sum_ > k we need to grab a smaller number, so we decrement j
        return False if the pair hasn't been found
    :param arr:
    :param k:
    :return:
    """
    arr = sorted(arr)
    i = 0
    j = len(arr) - 1
    while i < j :
        sum_ = arr[i] + arr[j]
        if sum_ == k:
            return True
        elif sum_ < k:
            i += 1
        else:
            j -= 1
    return False


def test():
    input_arrs = [[1,2,3,4,5],[],[5],[1,2,3,4,5],[2,1,9,4], [-5,1,2,5]]
    ks = [3, 5, 6, 10, 5, -3]
    answers = [True, False, False, False, True, True]
    for i, input_ in enumerate(zip(input_arrs, ks)):
        arr, k = input_
        assert answers[i] == solution_by_set(arr, k) == solution_by_binsearch(arr, k) == solution_by_sort_efficient(arr, k)

if __name__ == '__main__':
    test()