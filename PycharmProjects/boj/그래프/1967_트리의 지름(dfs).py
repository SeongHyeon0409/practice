import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for i in range(n+1)]
visited = [-1] * (n+1)
visited[1] = 0

for i in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dfs(start, weight):
    for next, nw in graph[start]:
        if visited[next] == -1:
            visited[next] = weight + nw
            dfs(next, weight + nw)

dfs(1, 0)

ln = visited.index(max(visited))
visited = [-1] * (n+1)
visited[ln] = 0
dfs(ln, 0)
print(max(visited))