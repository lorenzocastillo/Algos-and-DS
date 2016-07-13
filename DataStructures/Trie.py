"""
An implementation of a Trie
"""
from collections import defaultdict
from TestSuite import Assert

class TrieNode:
    def __init__(self):
        self.data = None
        self.children = defaultdict(TrieNode)

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.children)

    def __getitem__(self, item):
        if item in self.children:
            return self.children[item]
        else:
            return None


def print_trie(trie, depth=0):
    if len(trie) == 0:
        print("--" * (depth) + '*')
    else:
        for key, value in trie.children.items():
            print("--" * depth + str(key))
            print_trie(value, depth + 1)


def build_trie(arr):
    cur = root = TrieNode()
    for string in arr:
        cur = root
        for i,letter in enumerate(string):
            cur.children[letter].data = letter
            cur = cur.children[letter]

    return root


def find_prefix(string, trie):
    cur = trie
    prefix = string[0]
    cur_prefix = ''
    for i, c in enumerate(string):
        cur = cur[c]
        if len(cur) == 0:
            break
        elif len(cur) > 1:
            prefix += cur_prefix + string[i + 1]
            cur_prefix = ''
        else:
            cur_prefix += string[i + 1]

    return prefix


def solution(arr):
    trie = build_trie(arr)
    print_trie(trie)
    return [find_prefix(string,trie) for string in arr]


def test():
    arr = ['aabc', 'aad', 'aabd']
    f = solution
    Assert(['aabc','aad','aabd'], solution, arr)
    arr = ['aaaabc','aaaabd']
    Assert(['aaaabc','aaaabd'],solution, arr)
    arr = ['aad','aabc']
    Assert(['aad','aab'], solution, arr)
    arr = ['aabc','bca','cda']
    Assert(['a','b','c'], solution, arr)

if __name__ == '__main__':
    test()



