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
    def __init__(self, root):
        self.node = root
        self.stack = []
        print("binary iter")

    def __iter__(self):
        return self

    def in_order(self, x):
        print('in_order ', x)
        if x == None:
            return
        else:
            print('hre' , x)
            yield (x)
            self.in_order(x.left)
            self.in_order(x.right)

    def __next__(self):

        cur = self.node
        if cur == None:
            raise StopIteration
        else:
            print('next___')
            self.stack.append(cur)
            if self.stack:
                cur = self.stack.pop()
                yield cur
                if cur.right:
                    self.stack.append(cur.right)
                if cur.left:
                    self.stack.append(cur.left)
        print('stop')
        raise StopIteration


class BinaryTree:

    def __init__(self):
        self.root = None

    def search(self,root,key):
        if root == None:
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
        if node == None:
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

    def size(self, root = None):
        return 0 if root == None else root.count

    def rank(self, key, node = None):
        if node == None:
            return 0
        if node.key > key:
            return self.rank(key, node.left)
        elif node.key < key:
            return 1 + self.size(node.left) + self.rank(key, node.right)
        else:
            return self.size(node.left)

    def delete(self, key):
        pass

    def preorder(self):
        stack = []
        cur = self.root
        stack.append(cur)
        while stack:
            cur = stack.pop()
            print(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def __iter__(self):
        return BinaryTreeIter(self.root)



