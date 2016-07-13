"""
A double-ended LinkedList class supporting iteration, reversal, partitioning and insertion at the end and back of the
list.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data

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
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __add__(self,b):
        """
        Joins two list, creating a new list
        :param b: a linkedlist object
        :return: new merged list
        """
        c = LinkedList()
        for elem in self:
            c.append(elem.data)
        for elem in b:
            c.append(elem.data)
        return c

    def append(self, num):
        node = Node(num)
        if not self.__head:
            self.__head = node
            self.__tail = node
        else:
            if self.__head is self.__tail:
                self.__head.next = node
                self.__tail = node
            else:
                self.__tail.next = node
                self.__tail = node
        self.__size += 1

    def __reversed__(self):
        if not self.__head:
            return None
        else:
            self.__reverse(self.__head)
            return self

    def __reverse(self, node):
        if not node.next:
            self.__head = node
            return node
        else:
            next_ = node.next
            node.next = None
            next_rev = self.__reverse(next_)
            next_rev.next = node
            return node

    def remove_first(self):
        if len(self) == 0:
            raise RuntimeError("The list is empty")
        elif len(self) == 1:
            node = self.__head
            self.__tail = None
            self.__head = None
            node.next = None
            return node.data
        else:
            node = self.__head
            self.__head = self.__head.next
            node.next = None
            return node.data

    def partition(self, x, stable = True):
        if stable:
            greater_than_x = LinkedList()
            less_than_x = LinkedList()
            for elem in self:
                if elem.data < x:
                    less_than_x.append(elem.data)
                else:
                    greater_than_x.append(elem.data)
            return less_than_x + greater_than_x
        else:
            new_list = LinkedList()
            for elem in self:
                if elem.data < x:
                    new_list.prepend(elem.data)
                else:
                    new_list.append(elem.data)
            return new_list

    def prepend(self, data):
        node = Node(data)
        if len(self) == 0:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head = node

    def get_first(self):
        return self.__head

    def get_last(self):
        return self.__tail

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.__size

    def __iter__(self):
        return LinkedListIter(self.__head)

    def __repr__(self):
        sb = [str(i) for i in self]
        return '->'.join(sb)

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        cur_a = self.get_first()
        cur_o = other.get_first()

        while cur_a and cur_o:
            if cur_a != cur_o:
                return False
            else:
                cur_a = cur_a.next
                cur_o = cur_o.next
        return True


def test():
    numbers = [6,6,0,4,8,7,6,4,7,5]
    a = LinkedList()
    for num in numbers:
        a.append(num)
    print(a)
    x = a.partition(5)
    print('x: ', x)
    y = a.partition(5, False)
    print('y: ', y)


if __name__ == "__main__":
    test()

