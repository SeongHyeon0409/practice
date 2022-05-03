# 2020.05.03
# Presented by SeongHyeon0409

from collections import deque

n = int(input())

edges = dict()
for i in range(n):
    edges[i] = []

for i in range(n):
    edge = list(map(int, input().split()))
    for j in range(n):
        if edge[j] == 1:
            edges[i].append(j)

ans = [[0] * n for _ in range(n)]

for i in range(n):
    que = deque()
    que += edges[i]
    while que:
        np = que.pop()
        if ans[i][np] == 1:
            continue
        else:
            ans[i][np] = 1
            que += edges[np]

for i in ans:
    print(*i)

