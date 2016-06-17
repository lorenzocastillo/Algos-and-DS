class LRUCache:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    def insert(self, key, value):
        node = self.__create_node(key, value)
        if self.max_capacity <= len(self.cache.keys()):
            removed_node = self.__remove_lru()
            self.cache.pop(removed_node.key)

        self.cache[key] = node
        self.__insert_front(node)

    def get(self, key):
        item = self.cache.get(key)
        if item is None:
            return None
        else:
            self.__remove_node(item)
            self.__insert_front(item)
        return item

    def __remove_node(self, node):
        if node is None:
            return

        if node.key == self.head.key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        if node.key == self.tail.key:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = node.next = None
        return node

    def __insert_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def __remove_lru(self):
        return self.__remove_node(self.tail)

    def __create_node(self, key, value):
        class LinkedListNode:
            def __init__(self, key, value):
                self.prev = None
                self.next = None
                self.key = key
                self.value = value

        return LinkedListNode(key, value)

    def __repr__(self):
        cur = self.head
        result = []
        while cur:
            result.append(str((cur.key, cur.value)))
            cur = cur.next

        cur = self.tail
        result2 = []
        while cur:
            result2.insert(0,str((cur.key,cur.value)))
            cur = cur.prev

        return '->'.join(result) + "\n" + '<-'.join(result2)

    def test_list(self):
        self.__insert_front(self.__create_node(1,'one'))
        node = self.__create_node(2, 'dos')
        self.__insert_front(node)
        node3 = self.__create_node(3, 'tres')
        self.__insert_front(node3)
        self.__insert_front(self.__create_node(4, 'cuatro'))
        self.__remove_node(self.head)
        self.__remove_node(node)
        self.__remove_node(node3)


c = LRUCache(3)
#c.test_list()
c.insert(1, 'one')
c.insert(2, 'two')
c.insert(3, 'three')
c.insert(4, 'cuatro')
c.get(2)
c.get(2)
c.get(4)
c.insert(5, 'cinco')
c.get(3)
c.get(2)

print(c)
