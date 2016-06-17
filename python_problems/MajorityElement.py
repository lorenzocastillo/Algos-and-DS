def validate_majority(arr, possible_majority):
    count = 0
    for elem in arr:
        if elem == possible_majority:
            count += 1

    return possible_majority if count > int(len(arr)/2) else -1


def majority_element(arr):
    def m_e(left, right):
        if left > right:
            return -1
        elif right == left:
            return arr[left]
        else:
            mid = int((left + right)/2)
            majority_left = m_e(left, mid)
            majority_right = m_e(mid + 1, right)
            if majority_left == majority_right or (min(majority_left,majority_right) == -1 and max(majority_left, majority_right) != -1):
                return max(majority_left, majority_right)
            else:
                return -1
    possible_majority = m_e(0, len(arr)-1)
    if possible_majority == -1:
        return -1
    return validate_majority(arr, possible_majority)


def majority_element_better(arr):
    count = 0
    possible_majority = 0
    for elem in arr:
        if count == 0:
            possible_majority = elem
        if elem == possible_majority:
            count += 1
        else:
            count -= 1

    return validate_majority(arr, possible_majority)
