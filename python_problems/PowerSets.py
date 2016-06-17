def distribute(value, values):
    return list(map(lambda subset: [value] + subset, values))


def powersets(set_,i=0):
    if i >= len(set_):
        return [[]]
    ps = powersets(set_, i + 1)
    return distribute(set_[i], ps) + ps


def gen_binaries(up_to, n):
    bins = []
    for i in range(0, up_to):
        binary_i = bin(i)[2:]
        binary_i = '0' * (n - len(binary_i)) + binary_i
        bins.append(binary_i)
    return bins

def powersets_alt(set_):
    n = len(set_)
    total_sets = 2 ** n
    binaries = gen_binaries(total_sets,n)
    result = []
    for binary in binaries:
        res = [set_[i] for i,digit in enumerate(binary) if digit == '1']
        for i,digit in enumerate(binary):
            if digit == '1':
                res.append(set_[i])
        result.append(res)
    return result

print(powersets([]))
print(powersets([1]))
print(powersets([2,3]))
print(powersets([1,2,3]))


print(powersets_alt([1, 2, 3]))