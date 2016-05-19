from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)
    def __str__(self):
        return str(self.data)
    def __hash__(self):
        return self.data.__hash__()


class LinkedListIter:
    def __init__(self,node):
        self.node = node
    def __iter__(self):
        return self
    def __next__(self):
        if self.node:
            cur = self.node
            self.node = self.node.next
            return cur
        else:
            raise StopIteration()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __add__(self,b):
        if self.head and b.head:
            c.append(self.head.data)
            self.tail.next = b.head
            self.tail = b.tail
            return self
        elif b.head:
             self.head = b.head
             self.tail = b.tail
             return self
        elif self.head:
        
             return self
        else:
            raise RuntimeError('Empty lists')
    def append(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            if self.head == self.tail:
                self.head.next = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
    
    def __iter__(self):
        return LinkedListIter(self.head)
    def __repr__(self):
        sb = [str(i) for i in self]
        return '->'.join(sb)

def test():    
    a = LinkedList()
    print(a)
    b = LinkedList()
    b.append(6)
    b.append(5)
    print(b)
    c = a + b
    print(c)

if __name__ == "__main__":
    test()

