"""
A disjoint-set data structure with weighting and path compression.
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class DisjointSet:
    def __init__(self, n):
        self.arr = list()
        self.size = [1] * n
        self.count = n

        for i in range(n):
            self.arr.append(i)

    def find(self, a, b):
        """
        if a and b have the same root, then they're in the same connected component
        :param a:
        :param b:
        :return:
        """
        return self.root(a) == self.root(b)

    def union(self, a, b):
        """
        Get the root of a and b, and attach the smaller tree to the bigger tree
        :param a:
        :param b:
        :return:
        """
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b:
            return

        root_a, root_b = (root_a, root_b) if self.size[root_a] < self.size[root_b] else (root_b, root_a)

        self.arr[root_a] = root_b
        self.size[root_b] += self.size[root_a]
        self.count -= 1

    def root(self, a):
        """
        Finds the root of a. Then proceeds to make all nodes in that path to have the same root as a for path compression
        :param a:
        :return:
        """
        cur = self.arr[a]
        while cur != self.arr[cur]:
            cur = self.arr[cur]
        root_a = cur
        cur = a
        while cur != root_a:
            parent = self.arr[cur]
            self.arr[cur] = root_a
            cur = parent
        return root_a

    def __repr__(self):
        return repr(self.arr)