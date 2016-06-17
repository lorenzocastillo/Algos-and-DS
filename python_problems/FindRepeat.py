def count_le(arr, x):
    count_lt = 0
    count_e = 0
    for elem in arr:
        if elem < x:
            count_lt += 1
        elif elem == x:
            count_e += 1
    return count_lt, count_e


def find_repeat(arr, start, end):

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


arr = [1,4,5,3,2]
print(find_repeat(arr,0, len(arr) - 1))