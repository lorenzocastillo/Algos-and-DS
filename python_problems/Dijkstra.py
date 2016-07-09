import heapq
from collections import defaultdict
INF = 100000


def dijkstra(start):
    visited = set()
    q = list()
    heapq.heappush(q, (0, start))

    while q:
        dist_s_v, v = heapq.heappop(q)
        visited.add(v)
        for w in edges[v]:
            if w not in visited:
                distance[(start, w)] = min(distance[(start, w)], dist_s_v + distance[(v, w)])
                heapq.heappush(q, (distance[(start, w)], w))

    for w in vertices:
        print(start, w, distance[(start, w)])


def add_edge(v, w, d):
    edges[v].append(w)
    distance[(v, w)] = d


def fill():
    """
    for all the distances not set, it will set the distance to and from the same vertex to 0, and distances between
    non connected vertices to INF
    :return:
    """
    for i, v in enumerate(vertices):
        for j, w in enumerate(vertices):
            if i == j:
                distance[(v, w)] = distance[(w, v)] = 0
            else:
                if w not in edges[v]:
                    distance[(v, w)] = INF
distance = dict()
edges = defaultdict(list)

vertices = ['a', 'b', 'c', 'd', 'e']
add_edge('a', 'b', 50)
add_edge('a', 'd', 80)
add_edge('b', 'd', 90)
add_edge('b', 'c', 60)
add_edge('c', 'e', 40)
add_edge('d', 'c', 20)
add_edge('d', 'e', 70)
add_edge('e', 'b', 50)
fill()

print(distance)
print(edges)

for vertex in vertices:
    dijkstra(vertex)
    print('-'*10)

