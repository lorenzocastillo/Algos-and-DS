from TestSuite import Assert
"""
Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers
"""

def all_subarrays(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr) + 1):
            result.append((i,j))

    return result


def count_letters_numbers(arr, start, finish):
    count_letters = 0
    count_numbers = 0
    for i in range(start, finish):
        if type(arr[i]) == int:
            count_numbers += 1
        if type(arr[i]) == str:
            count_letters += 1

    return (count_letters, count_numbers)


def find_longest(arr):
    """
    Brute force solution: generate all the subarray indices (O(n^2)). Then, iterate through all the indices and remember
    the longest sequence whose count_letters == count_numbers
    :param arr:
    :return:
    """
    indices = all_subarrays(arr)

    max_length = 0
    for start, finish in sorted(indices):
        count_letters, count_numbers = count_letters_numbers(arr, start, finish)

        if count_letters == count_numbers:
            max_length = max(max_length, finish - start)
    return max_length


def find_longest_better(arr):
    count_letters, count_numbers = count_letters_numbers(arr, 0, len(arr))
    smallest_type = int if count_letters > count_numbers else str
    small_count = min(count_letters, count_numbers)
    big_count = max(count_letters, count_numbers)

    def aux(i,j,smallest, biggest):

        while True:
            if smallest == biggest:
                return i,j
            if not isinstance(arr[i],smallest_type):
                i += 1
                biggest -= 1
            elif not isinstance(arr[j],smallest_type):
                j -= 1
                biggest -= 1
            else:
                best_left = aux(i,j-1,smallest-1, biggest)
                best_right = aux(i+1,j,smallest-1, biggest)
                return max(best_left, best_right, key=lambda x: x[1] - x[0])

    return aux(0, len(arr) - 1, small_count, big_count)


def test():
    arr = ['a', 1, 'b', 2, 'c', 3]
    f = find_longest_better
    Assert((0,5), f, arr)
    arr = ['a', 'a', 1, 2, 'a']
    Assert((1,4), f, arr)
    arr = ['a', 'a', 1, 2, 'a', 'a', 'a', 'a', 'a', 'b', 'b', 3, 5]
    print(f(arr))

if __name__ == '__main__':
    test()

