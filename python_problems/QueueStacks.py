class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop(len(self.stack) - 1)

    def is_empty(self):
        return self.stack == []


class Queue2Stacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.move_data(self.stack2, self.stack1)
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.is_empty():
            self.move_data(self.stack1,self.stack2)
        if self.stack2.is_empty():
            raise Exception("Empty. Cannot Dequeue")
        return self.stack2.pop()

    def move_data(self, s1, s2):
        while not s1.is_empty():
            val = s1.pop()
            s2.push(val)

