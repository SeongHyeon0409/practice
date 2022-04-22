# 2020.04.22
# Presented by SeongHyeon0409
# 그래프
import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
edges = dict()
visited = [False] * (n + 1)
count = 0

for i in range(1, n+1):
    edges[i] = []

for i in range(m):
    s ,e = map(int, input().strip().split())
    edges[s].append(e)
    edges[e].append(s)

for i in range(1, n + 1):
    edges[i].sort()

def dfs(edges, start, visited):
    visited[start] = True
    for i in edges[start]:
        if not visited[i]:
            dfs(edges, i, visited)

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(edges, i, visited)

print(count)
