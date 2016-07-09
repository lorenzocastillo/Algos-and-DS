"""
Given a list of baby names with their frequencies, and synonyms for the names, print the total number of frequencies
for that name including the synonyms

"""
from collections import defaultdict
from helpers.TestSuite import  Assert


def union(arr, a,b):
    num = arr[a]
    for i, val in enumerate(arr):
        if val == num:
            arr[i] = arr[b]


def find(arr, a,b):
    return arr[a] == arr[b]


def baby_names(names_frequencies, synonyms):
    """

    :param names_frequencies:
    :param synonyms:
    :return:
    """
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
    """
    Build a graph of synonyms. This will create connected subgraphs for all the synonyms of each game. We will then
    traverse the graph, keeping track of the frequencies of the names. Once a subgraph is traversed, we will print the
    total frequency for that subgraph.
    :param name_frequencies:
    :param synonyms:
    :return:
    """
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

    # Sorting to give consistent output in test function
    result = list()
    for name in sorted(name_frequencies.keys()):
        if name not in visited:
            visited.add(name)
            count = name_frequencies[name]
            count += dfs(name)
            result.append((name, count))
    return result

def test():
    names_freqs = {'john': 15, 'jon': 12, 'chris': 13, 'kris': 4, 'christopher': 20, 'phil': 5}
    synonyms = [('john', 'jon'), ('chris', 'kris'), ('chris', 'christopher')]
    answer = [('chris', 37), ('john', 27), ('phil', 5)]
    f = baby_names2
    Assert(answer, f, names_freqs, synonyms)

if __name__ == '__main__':
    test()
