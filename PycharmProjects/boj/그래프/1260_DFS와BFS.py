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
            visited.append(node)
            non_visit.extend(edges[node])

    return visited

#재귀함수
def dfs_re(edges, start):

    for i in range(1, n + 1):
        edges[i].sort()

    visited = [start]
    dfs_rec(edges, start, visited)
    return visited

def dfs_rec(edges, start, visited):
    for i in edges[start]:
        if i not in visited:
            visited.append(i)
            dfs_rec(edges, i, visited)

def bfs(edges, start):
    for i in range(1, n + 1):
        edges[i].sort(reverse=False)

    non_visit, visited = list(), list()
    non_visit.append(start)

    while non_visit:
        node = non_visit.pop(0)
        if node not in visited:
            visited.append(node)
            non_visit.extend(edges[node])

    return visited

print(*dfs_re(edges, v))
print(*bfs(edges, v))
