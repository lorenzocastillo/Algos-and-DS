"""
Generate all the subsets of a set
"""
from helpers.TestSuite import Assert


def distribute(value, values):
    return [[value] + subset for subset in values]
    # return list(map(lambda subset: [value] + subset, values)) list comprehensions is ~ 25-50% faster


def powersets(set_,i=0):
    if i >= len(set_):
        return [[]]
    ps = powersets(set_, i + 1)
    return distribute(set_[i], ps) + ps


def gen_binaries(up_to, n):
    bins = list()
    for i in range(0, up_to):
        binary_i = bin(i)[2:]
        binary_i = '0' * (n - len(binary_i)) + binary_i
        bins.append(binary_i)
    return bins


def powersets_alt(set_):
    n = len(set_)
    total_sets = 2 ** n
    binaries = gen_binaries(total_sets,n)
    result = list()
    for binary in binaries:
        res = [set_[i] for i,digit in enumerate(binary) if digit == '1']
        result.append(res)
    return result


def test():
    arr = []
    f = powersets
    Assert([[]], f, arr)
    arr = [1, 2, 3, 4]
    solution = [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4],
                [2], [3, 4], [3], [4], []]
    Assert(solution, f, arr)


if __name__ == '__main__':
    test()