"""
Given two iterables, do they contain duplicates?
"""


def solution_brute_force(iter1, iter2):
    """
    Given two iterables compare all possible pairs
    Complexity: Running time O(N^2). Space O(1)
    :param iter1:
    :param iter2:
    :return:
    """
    for i, a in enumerate(iter1):
        for j, b in enumerate(iter2):
            if a == b:
                return True
    return False


def solution_by_set(iter1, iter2):
    """
    Given two iterables, make one a set, and check all other elems in iter2 and see if they are in iter1
    Complexity: Running time O(N). Space O(N)
    :param iter1:
    :param iter2:
    :return:
    """
    if len(iter1) == 0 or len(iter2) == 0:
        return False # No duplicates if either are empty

    elems_in_a = set(iter1)
    for elem in iter2:
        if elem in elems_in_a:
            return True
    return False


def solution_by_sorting(iter1, iter2):
    return solution_if_sorted(sorted(iter1),sorted(iter2))


def solution_if_sorted(iter1, iter2):
    """
    Given two sorted iterables, loop through all of the elements of iter1 (e1),
    and compare the next element of iter2 (e2). If equal, we are done. If e1 > e2,
    we need to look for the next element in iter2. Else, we need to look for the
    next element in iter1
    Complexity: O(N) Running time. Space O(1)
    :param iter1:
    :param iter2:
    :return:
    """

    j = 0
    for e1 in iter1:
        while j < len(iter2):
            e2 = iter2[j]
            if e1 > e2:
                j += 1
            elif e1 == e2:
                return True
            else:
                break

    return False

def test():

    inputs_a = [(1,2,3,4),[3,6,1,4,7,9],[],[1,1,1,1,1],[],[1],[1],"dawg",set([1,2,3])]
    inputs_b = [(5,6,7,8),[0,7,2,5,12,8],[0,0,0,0],[],[],[2],[1],"abc", set([5,2])]
    functions = [solution_by_set, solution_by_sorting, solution_brute_force]

    for x in zip(inputs_a,inputs_b):
        a, b = x
        result = [f(a,b) for f in functions]
        assert result[0] == result[1] == result[2], (a,b, result)

if __name__ == "__main__":
    test()
