n, m, v = map(int, input().split())

edges = dict()

for i in range(1, n+1):
    edges[i] = []

for i in range(m):
    s ,e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)


def dfs(edges, start):
    for i in range(1, n + 1):
        edges[i].sort(reverse=True)

    non_visit, visited = list(), list()
    non_visit.append(start)

    while non_visit:
        node = non_visit.pop()
        if node not in visited:
            print(node, end = ' ')
            visited.append(node)
            non_visit.extend(edges[node])

def bfs(edges, start):

    for i in range(1, n + 1):
        edges[i].sort(reverse=False)

    non_visit, visited = list(), list()
    non_visit.append(start)

    while non_visit:
        node = non_visit.pop(0)
        if node not in visited:
            print(node, end = ' ')
            visited.append(node)
            non_visit.extend(edges[node])


dfs(edges, v)
print()
bfs(edges, v)

