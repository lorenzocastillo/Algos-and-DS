from collections import deque
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


def weave(first, second):
    """
    if there's no first or second, prepend the prefix to first and second
    else:
        remove the head of first, and make that a prefix.
        Recurse with the new prefix.
        restore the head and remove the prefix
        repeat for the second prefix 
    :param first:
    :param second:
    :return:
    """
    results = list()

    def aux(prefix):
        if not first or not second:
            results.append(prefix + first + second)
        else:
            head_first = first.popleft()
            prefix.append(head_first)
            aux(prefix)
            first.appendleft(head_first)
            prefix.pop()

            head_second = second.popleft()
            prefix.append(head_second)
            aux(prefix)
            second.appendleft(head_second)
            prefix.pop()

    aux(deque())
    return results

results = []
print(weave(deque([1,2]),deque([3,4])))
print(results)


def append_all(x, deques):
    for deque in deques:
        deque.appendleft(x)


def find_sequence(root):
    if root is None:
        return [deque()]
    else:
        all_left = find_sequence(root.left)
        all_right = find_sequence(root.right)
        results = list()
        for left in all_left:
            for right in all_right:
                results += weave(left,right)
        append_all(root, results)
        return results


one = Node(1)
two = Node(2)
three = Node(3)
two.left = one
two.right = three

print(find_sequence(two))