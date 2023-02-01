# 2023.02.01
# Written by SeongHyeon0409
from collections import deque

n, m = map(int, input().split())
distance = [[0]*(n+1) for _ in range(n+1)]
edges = dict()

for i in range(1, n+1):
    edges[i] = []

for i in range(n-1):
    s ,e, d= map(int, input().split())
    distance[s][e] = d
    distance[e][s] = d
    edges[s].append(e)
    edges[e].append(s)

for i in range(m):
    s, e = map(int, input().split())
    dis = float('INF')
    visited = list()
    q = deque()
    q.append((s, 0))
    while q:
        s, d = q.popleft()
        if s == e:
            dis = min(dis, d)
            break
        for i in edges[s]:
            if i not in visited and distance[s][i]:
                q.append((i, d + distance[s][i]))
                visited.append(i)


    print(dis)



