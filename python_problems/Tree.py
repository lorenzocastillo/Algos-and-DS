from collections import defaultdict
class Node:
    def __init__(self,data):
        self.children = []
        self.data = data
        self.parent = None
    def __repr__(self):
        return self.data
    def __hash__(self):
        return hash(self.data)
    def __eq__(self, other):
        return self.data == other.data

def print_tree(root):
    levels = defaultdict(list)

    def visit(node, level):
        levels[level].append(node)
        for child in node.children:
            visit(child, level + 1)

    visit(root, 0)

    for i in range(len(levels)):
        print(levels[i])


def get_deepest_nodes(root):
    max_lst = []
    max_level = 0

    def visit(node, level):
        nonlocal max_level
        if level > max_level:
            max_level = level
            max_lst.clear()
        if level == max_level:
            max_lst.append(node)
        for child in node.children:
            visit(child, level + 1)

    visit(root, 0)
    return max_lst

def find_smallest_subtree(root):
    deepest_nodes = get_deepest_nodes(root)
    deepest_nodes_set = set(deepest_nodes)
    while len(deepest_nodes_set) != 1:
        deepest_nodes_set = {node.parent for node in deepest_nodes_set}

    for node in deepest_nodes_set:
        return node
    return None

def find_smallest_subtree_optimal(root):

    def visit(node,level):

        children_heights = list()
        max_level = 0
        for child in node.children:
            result = visit(child, level + 1)
            print(result)
            max_for_child = max(result, key=lambda x : x[0])[0]
            if max_for_child > max_level:
                children_heights = list()
                max_level = max_for_child
            if max_for_child == max_level:
                for res in result:
                    if res[0] == max_level:
                        children_heights.append(res)

        if len(children_heights) == 1:
            return children_heights
        else:
            return [(max(max_level,level),node)]

    return visit(root,0)
letters = 'abcdefghijklm'
table = {letter: Node(letter) for letter in letters}
def make_a_parent_of_b(a,b):
    table[a].children.append(table[b])
    table[b].parent = table[a]

make_a_parent_of_b('a','b')
make_a_parent_of_b('a','c')
make_a_parent_of_b('a','d')
make_a_parent_of_b('c','e')
make_a_parent_of_b('e','f')
make_a_parent_of_b('e','g')
# make_a_parent_of_b('e','h')
# make_a_parent_of_b('f','i')
# make_a_parent_of_b('h','j')
make_a_parent_of_b('d','k')
make_a_parent_of_b('k','l')


print_tree(table['a'])
print(get_deepest_nodes(table['a']))
print(find_smallest_subtree(table['a']))
print(find_smallest_subtree_optimal(table['a']))
