def le(x, y):
    return x <= y


def ge(x, y):
    return x >= y


def partition(arr, left=0, right=None, pivot_value=None, cmp=le):

    if right is None:
        right = len(arr) - 1
    if pivot_value is None:
        pivot_value = arr[right]
    left_ptr = left

    for i in range(left, right):
        if cmp(arr[i],pivot_value):
            arr[left_ptr], arr[i] = arr[i], arr[left_ptr]
            left_ptr += 1
    arr[right], arr[left_ptr] = arr[left_ptr], arr[right]  # Move pivot to its final place
    return left_ptr


def select(arr, start=None, end=None, k=None, reverse=False):
    if arr is None:
        return None
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    if k is None or k >= len(arr):
        return arr, len(arr)

    cmp = le
    if reverse:
        cmp = ge

    while True:
        pivot = arr[end]
        new_pivot_index = partition(arr, start, end, pivot,cmp)
        pivot_dist = new_pivot_index - start
        if pivot_dist == k:
            return arr, new_pivot_index
        elif pivot_dist > k:
            end = new_pivot_index - 1
        else:
            k -= pivot_dist + 1
            start = new_pivot_index + 1


def sort(arr, start, end):
    if start <= end:
        pivot = arr[end]
        new_pivot_index = partition(arr, start, end, pivot)
        sort(arr, start, new_pivot_index - 1)
        sort(arr, new_pivot_index + 1, end)
    return arr


def test():
    import random
    random.seed(9)
    arr = [random.randrange(0, 100) for i in range(100)]
    sorted_arr = sorted(arr, reverse=True)
    for k in range(1, 100):
        result, _ = select(list(arr), 0, len(arr) - 1, k, True)
        assert sorted(result[:k], reverse=True) == sorted_arr[:k]


def test_sort():
    import random
    arr = [random.randrange(0, 10) for i in range(10)]
    print(arr)
    print(partition(arr))
    print(partition(arr))
    sorted_arr = sorted(arr)
    assert sort(arr, 0, len(arr) -1) == sorted_arr

if __name__ == '__main__':
    test()
    test_sort()


def is_number(val):
    return isinstance(val, int)

def q_sort(arr, start, end):
    if start <= end:
        while end >= 0 and is_number(arr[end]):
            end -= 1
        while start < len(arr) and is_number(arr[start]):
            start += 1
        if start >= len(arr) or end < 0:
            return
        pivot_value = arr[end]
        pivot_index = modified_partition(arr, start, end, pivot_value)
        q_sort(arr, start, pivot_index - 1)
        q_sort(arr, pivot_index + 1, end)

def modified_partition(arr, start=0, end=None, pivot_value=None, cmp=le):
    if end is None:
        end = len(arr) - 1
    if pivot_value is None:
        pivot_value = arr[end]

    left_ptr = start
    for i in range(start, end):
        if left_ptr >= end:
            break
        if is_number(arr[i]):
            continue
        else:
            if cmp(arr[i], pivot_value):
                arr[i], arr[left_ptr] = arr[left_ptr], arr[i]
                left_ptr += 1
                while left_ptr < end and is_number(arr[left_ptr]):
                    left_ptr += 1
    arr[end], arr[left_ptr] = arr[left_ptr], arr[end]
    return left_ptr

arr = [5,2,3,1,4]
q_sort(arr, 0 , 4)
print(arr)
arr = ['d','b','a','c','b']
#modified_partition(arr, 0, len(arr)-1, 'b')
q_sort(arr,0, 4)
print(arr)

