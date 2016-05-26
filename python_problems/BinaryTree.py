class Node:
    def __init__(self,key,value):
        self.right = None
        self.left = None
        self.value = value
        self.key = key
        self.count = 0

    def __repr__(self):
        return str(self.key) + ": " + str(self.value)


class BinaryTreeIter:
    def __init__(self, tree):
        self.tree = tree
        self.i = 0
        self.res = self.in_order(self.tree.root)
        print("binary iter")

    def __iter__(self):
        print('BinTreeIter::__iter__')
        return self

    def in_order(self, root):
        if not root:
            return
        if root.left:
            for x in self.in_order(root.left):
                yield x
        yield (root)
        if root.right:
            for x in self.in_order(root.right):
                yield x

    def __next__(self):
        if self.res is None:
            self.res = self.in_order(self.tree.root)
        for node in self.res:
            return node
        raise StopIteration


class BinaryTree:

    def __init__(self):
        self.root = None

    def search(self,root,key):
        if root is None :
            return root
        if root.key == key:
            return root
        elif root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)
        
    def put(self, key, value):
        self.root = self.put_aux(self.root, key, value)
        
    def put_aux(self, root, key, value):
        if root == None:
            return Node(key,value)
        if root.key > key:
            root.left = self.put_aux(root.left, key, value)
        elif root.key < key:
            root.right = self.put_aux(root.right, key, value)
        else:
            root.value = value
        root.count = 1 + self.size(root.left) + self.size(root.right)
        return root

    def get(self, key):
        return self.search(self.root, key)

    def minimum(self):
        if self.root == None:
            raise ValueError('arg is an empty sequence')
        cur = self.root
        while cur.left:
            cur = cur = cur.left
        return cur

    def floor(self, key):
        node = self.floor_aux(self.root, key)
        if not node:
            return None
        else:
            return node.key
        
        def floor_aux(self, node, key):
            if node == None:
                return None
            if node.key == key:
                return node
            elif node.key > key:
                return self.floor_aux(node.left, key)

            t = self.floor_aux(node.right, key)
            if t:
                return t
            else:
                return node

    def size(self, root=None):
        return 0 if not root else root.count

    def rank(self, key, node=None):
        if not node:
            return 0
        if node.key > key:
            return self.rank(key, node.left)
        elif node.key < key:
            return 1 + self.size(node.left) + self.rank(key, node.right)
        else:
            return self.size(node.left)

    def delete(self, key):
        pass

    def is_balanced(self):
        def aux(root):
            if root is None:
                return True
            h_left = root.left.count if root.left else 0
            h_right = root.right.count if root.right else 0
            diff = abs(h_left - h_right)
            if diff > 2:
                return False
            else:
                return aux(root.left) and aux(root.right)
        return aux(self.root)

    def __iter__(self):
        print('BinaryTree::__iter__')
        return BinaryTreeIter(self)


def build_tree(numbers):
    tree = BinaryTree()
    for num in numbers:
        tree.put(num, num)
    return tree


def test():
    tree = build_tree([10,5,15,1,8,12,20])

    tree2 = build_tree([1,2,3])

    print(tree.is_balanced())
    print(tree2.is_balanced())

if __name__ == '__main__':
    test()

