from collections import defaultdict


def union(arr, a,b):
    num = arr[a]
    for i, val in enumerate(arr):
        if val == num:
            arr[i] = arr[b]


def find(arr, a,b):
    return arr[a] == arr[b]


def baby_names(names_frequencies, synonyms):
    arr = list()
    name_to_group = dict()
    group_to_name = dict()
    name_to_freq = names_frequencies
    for i,name_frequency in enumerate(names_frequencies):
        arr.append(i)
        name, freq = name_frequency
        name_to_group[name] = i
        group_to_name[i] = name

    for a,b in synonyms:
        union(arr, name_to_group[a], name_to_group[b])

    group_to_names = defaultdict(list)
    for i, elem in enumerate(arr):
        group_to_names[elem].append(group_to_name[i])

    print(name_to_freq)
    for group in group_to_names.values():
        count = 0
        for name in group:
            count += name_to_freq[name]
        print(group[0],count)


def baby_names2(name_frequencies, synonyms):
    edges = defaultdict(list)
    for name1, name2 in synonyms:
        edges[name1].append(name2)
        edges[name2].append(name1)

    visited = set()

    def dfs(start):
        count = 0
        for synonym in  edges[start]:
            if synonym not in visited:
                visited.add(synonym)
                count += dfs(synonym) + name_frequencies[synonym]
        return count

    for name in name_frequencies.keys():
        if name not in visited:
            visited.add(name)
            count = name_frequencies[name]
            count += dfs(name)
            print(name, count)


names_freqs = {'john':15,'jon':12,'chris':13,'kris':4,'christopher':20,'phil':5}
synonyms = [('john','jon'),('chris','kris'),('chris','christopher')]
baby_names2(names_freqs, synonyms)