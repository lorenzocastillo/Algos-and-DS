"""
Given a string, find a permutation with no duplicates a distance, d, of each other
"""
from collections import Counter
from helpers.TestSuite import Assert
from python_problems.Permutations import permutations_nodups


def permutation_dist(string, d=1):
    def get_next():
        """
        Determine which item to use
        :return:
        """
        for item, value in counts.most_common():
            if item not in last or last[item] <= len(result) - d:
                return item
        return None

    counts = Counter(string)
    last = dict()
    result = list()
    while len(result) != len(string):
        c = get_next()
        if c is None:
            return None
        last[c] = len(result)
        counts[c] -= 1
        if counts[c] <= 0:
            del counts[c]
        result.append(c)
    return "".join(result)


def test():
    def dups_within_d(string, d):
        """
        Given a distance d and a string, determine whether any two duplicates within the string are d unit apart.
        Used to filter all possible results for test cases.
        :param string:
        :param d:
        :return:
        """
        last = dict()
        for i, c in enumerate(string):
            if c in last and i - last[c] >= d:
                return True
            last[c] = i
        return False

    def generate_case_for(string, distance):
        result = list(filter(lambda x: dups_within_d(x, distance), permutations_nodups(string)))
        #  For the case in which you can't form a permutation, since we are returning None instead of the empty list.
        if result == list():
            return None
        else:
            return result

    strings = ['aabc', 'aabc','abcdabe', 'aa']
    distances = [2, 3, 3, 3]
    f = permutation_dist
    for string, dist in zip(strings, distances):
        value = generate_case_for(string, dist)
        Assert(value, f, string, dist, multiple_expected=True)


if __name__ == '__main__':
    test()