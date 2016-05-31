from TestSuite import Test, Assert


def binary_search(arr, x, lo = 0, hi = None):
    if not hi:
        hi = len(arr) - 1

    while lo < hi:
        mid = int((lo + hi)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def find_first_last(arr, x):
    """
    Given  a sorted array with duplicates, find where x first occurs and where it last occurs
    :param arr: a sorted array
    :param x: the value that you are looking for
    :return: a tuple of x's first and last occurrence, or a tuple of -1, -1 if x is not in the array
    """
    def modified_bin_search(find_first=True):
        start = 0
        end = len(arr) - 1
        result = -1
        while start <= end:
            mid = int((start + end)/2)
            if arr[mid] == x:
                result = mid
                if find_first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif arr[mid] < x:
                start = mid + 1

            else:
                end = mid - 1

        return result
    return modified_bin_search(True), modified_bin_search(False)


def count_occurrences(arr, x):
    """
    Count the number of occurrences of x in a sorted array
    :param arr: a sorted array
    :param x: the number you are looking for
    :return: the number of occurrences of x in the array
    """
    first, last = find_first_last(arr, x)
    if first == -1:
        return 0
    else:
        return last - first + 1


def find_rotation(arr):
    """
    Given a sorted array with no duplicates, find how many times it has been
    rotated. Ex:
        [1,2,3,4,5] => [3,4,5,1,2] has been rotated twice
    :param arr: a sorted array with no duplicates
    :return: the number of times a rotation has occurred
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end /2))
        prev = (mid + len(arr) - 1) % len(arr)
        next_ = (mid + 1) % len(arr)
        if arr[start] < arr[end]:
            return start
        elif arr[prev] >= arr[mid] and arr[next_] <= arr[mid]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[end] >= arr[mid]:
            end = mid - 1
    return -1


def sparse_search(arr, x):
    """
    Given a sorted array of strings, interspersed with '',
    find x
    :param arr: a sorted array of strings with '' interspersed
    :param x: the string you are looking for
    :return: the index of x or -1 if no such string is found
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end/2))
        if arr[mid] == x:
            return mid
        elif arr[mid] == '':
            if arr[start] == '':
                start += 1
            if arr[end] == '':
                end -=1
        elif arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1

    return -1


@Test
def test_find_rotation():
    pass


@Test
def test_find_first_last():
    f = find_first_last
    arr_even = [1, 2, 2, 2, 2, 4, 5, 7, 8, 10, 10, 12, 20, 20, 21, 34]
    arr_odd = [1, 2, 2, 2, 2, 4, 5, 7, 8, 10, 10, 12, 20, 20, 21]
    Assert((1,4), f, arr_odd, 2)
    Assert((0,0), f, arr_odd, 1)
    Assert((14, 14), f, arr_odd, 21)
    Assert((14, 14), f, arr_even, 21)
    Assert((15, 15), f, arr_even, 34)
    Assert((-1, -1), f, [], 0)
    Assert((0,0), f, [55], 55)


@Test
def test_count_occurrences():
    arr = [1, 2, 2, 2, 2, 4, 5, 7, 8, 10, 10, 12, 20, 20, 21, 34]
    f = count_occurrences
    Assert(0, f, arr, 0)
    Assert(1, f, arr, 1)
    Assert(4, f, arr, 2)


@Test
def test_sparse_search():
    pass


def test():
    test_find_first_last()
    test_count_occurrences()
    test_find_rotation()
    test_sparse_search()

if __name__ == '__main__':
    #test()
    pass

# def best_sell_(arr):
#     best = 1
#     best_sell = 0
#
#     for i in range(len(arr) -2, -1, -1):
#         cur = arr[i]
#         if cur > best:
#             best = cur
#         else:
#             result = best - cur
#             if result > best_sell:
#                 best_sell = result
#     return best_sell
#
# print(best_sell_([20, 8, 7, 11, 5, 3, 1]))
#

def fib(N):
    if N == 0:
        return [0]
    result = [0,1]
    for i in range(2,N):
        result.append(result[i-2] + result[i-1])
    return result

N = int(1)
print(list(map(lambda x : x**3, fib(N))))