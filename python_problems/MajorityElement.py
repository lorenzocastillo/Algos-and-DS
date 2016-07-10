"""
Given a list of items, determine if there's a majority element. A majority element is one in which its count is greater
than floor(len(lst)/2).
"""
from helpers.TestSuite import Assert


def validate_majority(arr, possible_majority):
    count = 0
    for elem in arr:
        if elem == possible_majority:
            count += 1

    return possible_majority if count > len(arr)//2 else None


def majority_element(arr):
    """
    Walk through the array, keeping track of the potential majority element. Increment the count if you encounter that
    element again, or decrement the count if you encounter another element. If the count reaches 0, reset the majority
    element with the next element you see. Lastly, verify that the element is the majority element
    :param arr:
    :return:
    """
    count = 0
    possible_majority = arr[0]
    for elem in arr:
        if count == 0:
            possible_majority = elem
        if elem == possible_majority:
            count += 1
        else:
            count -= 1

    return validate_majority(arr, possible_majority)


def test():
    arr = [1, 2, 3, 4, 5]
    f = majority_element
    Assert(None, f, arr)
    arr = [1, 1, 1, 2, 4]
    Assert(1, f, arr)
    arr = [1, 1, 2, 4, 4]
    Assert(None, f, arr)

if __name__ == '__main__':
    test()