import heapq
from collections import defaultdict


def dijkstra(start):
    visited = set()
    q = list()
    heapq.heappush(q, (0, start))

    while q:
        cur = heapq.heappop(q)
        cur_dist, cur = cur
        visited.add(cur)
        for adj in edges[cur]:
            if adj not in visited:
                if cur_dist + distances[(cur, adj)] < distances[(start,adj)]:
                    distances[(start, adj)] = cur_dist + distances[(cur, adj)]
                heapq.heappush(q, (distances[(start,adj)], adj))

    for w in vertices:
        print(start, w, distances[(start, w)])


def add_edge(v, w, d):
    edges[v].append(w)
    distances[(v,w)] = d


def fill():
    for i, v in enumerate(vertices):
        for j in range(len(vertices)):
            w = vertices[j]
            if i == j:
                distances[(v, w)] = 0
                distances[(w, v)] = 0
            else:
                if w not in edges[v]:
                    distances[(v, w)] = 100000
distances = dict()
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

print(distances)
print(edges)

for vertex in vertices:
    dijkstra(vertex)
    print('-'*10)

