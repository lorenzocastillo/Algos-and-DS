from collections import Counter
from QuickSelectSort import select
from functools import total_ordering

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

@total_ordering
class Count:
    def __init__(self, data):
        self.data = data
        self.count = 1

    def inc(self):
        self.count += 1

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count

    def __gt__(self, other):
        return self.count > other.count

    def __le__(self, other):
        return self.count <= other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __repr__(self):
        return "Count of %s is %i" % (self.data, self.count)


def get_suggestions(user, k=5):
    suggestions = dict()
    for friend in user.friends:
        for second_degree in friend.friends:
            if second_degree != user and second_degree not in user.friends:
                if second_degree in suggestions:
                    suggestions[second_degree].inc()
                else:
                    suggestions[second_degree] = Count(second_degree)

    counts = list(suggestions.values())
    print('Counts: ', counts)
    result, top = select(counts,0, len(counts) - 1, k, True)
    print('Results: ',result,top)

a = User('a')
b = User('b')
c = User('c')
d = User('d')
e = User('e')
f = User('f')
a.add_friend(b)
a.add_friend(c)
a.add_friend(d)
b.add_friend(d)
b.add_friend(f)
b.add_friend(e)
c.add_friend(e)
d.add_friend(f)
d.add_friend(e)
f.add_friend(e)

get_suggestions(c)