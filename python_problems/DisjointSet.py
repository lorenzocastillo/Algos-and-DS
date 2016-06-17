class DisjointSet:
    def __init__(self, elements):
        self.arr = []
        self.size = [1]*elements
        self.count = elements
        for i in range(elements):
            self.append(i)

    def find(self,a,b):
        return self.root(a) == self.root(b)

    def union(self,a,b):
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b:
            return
        if self.size[root_a] < self.size[root_b]:
            self.arr[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.arr[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        self.count -= 1

    def root(self, a):
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
        return self.arr.__repr__()


ds = DisjointSet(10)
ds.union(0,1)
