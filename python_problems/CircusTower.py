def circus_tower(arr):
    visited = set()
    cur_tower = tuple(tuple())
    print(cur_tower)
    best = list()

    def get_neighbors(elem, cur_tower):
        return [person for person in arr if elem != person and person not in cur_tower]

    def find_longest(cur, tower):
        neighbors = get_neighbors(cur, tower)
        neighbors = filter(lambda x: x not in tower, neighbors)
        for neighbor in neighbors:
            temp = tower + (neighbor,)
            if temp not in visited:
                visited.add(temp)
                prev = tower[-1]
                if neighbor[0] <= prev[0] or neighbor[1] <= prev[1]:
                    find_longest(neighbor, temp)
                    if len(temp) > len(best):
                        best.append(temp)
    for person in arr:
        temp = ((person),)
        print(temp)
        visited.add(temp)
        find_longest(person, temp)

    print(visited)
    best.sort(key=lambda x: len(x))
    print('Best: ', best[-1])

arr = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print(circus_tower(arr))