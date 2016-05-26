def powersets(set_):
    if not set_:
        return [[]]
    ps = powersets(set_[1:])
    ps = list(map(lambda x: x + [set_[0]],ps)) + ps
    return ps

print(powersets([]))
print(powersets([1]))
print(powersets([2,3]))
print(powersets([1,2,3]))