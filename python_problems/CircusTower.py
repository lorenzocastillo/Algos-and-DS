def circus_tower(arr):

    best = list((arr[0],))

    def get_neighbors(elem, cur_tower):
        return [person for person in arr if elem != person and person not in cur_tower]

    def find_longest(cur, tower):
        if len(tower) > len(best[-1]):
            best.append(tower)
        for neighbor in get_neighbors(cur, tower):
            if neighbor <= tower[-1]:
                find_longest(neighbor, tower + (neighbor,))

    for person in arr:
        temp = ((person),)
        find_longest(person, temp)

    best.sort(key=len)

    #print('Best: ', best[-1])
    return best


def circus_tower2(arr):

    def get_neighbors(elem):
        return [person for person in arr if elem != person and person not in visited]

    cache = dict()
    visited = set()

    def find_longest(cur, tower):
        if cur in cache:
            return cache[cur]
        neighbors = get_neighbors(cur)
        if not neighbors:
            return [cur]
        else:
            best = list()
            for neighbor in neighbors:
                if neighbor <= tower[-1]:
                    visited.add(neighbor)
                    best = max(find_longest(neighbor, tower + (neighbor,)), best, key=len)
                    visited.remove(neighbor)
            cache[cur] = [cur] + best
            return cache[cur]

    best = list()
    for person in arr:
        temp = ((person),)
        visited.add(person)
        best = max(find_longest(person, temp), best, key=len)
        visited.remove(person)

    return best

arr = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
#print(circus_tower2(arr))

from timeit import Timer
setup = """
from __main__ import circus_tower2, circus_tower
arr = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110),(66,105),(62,98),(73,188),(74,189)]
"""
t = Timer(stmt='circus_tower(arr)', setup=setup).timeit(number=100)
print(t)
t = Timer(stmt='circus_tower2(arr)', setup=setup).timeit(number=100)
print(t)