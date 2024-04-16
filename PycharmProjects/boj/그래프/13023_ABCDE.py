n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False]*(n)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 친구 depth가 4 이상이면 1
ans = 0

def dfs(s, d):
    visited[s] = True
    if d > 4:
        print(1)
        exit()

    for i in graph[s]:
        if visited[i] == False:
            dfs(i, d+1)

    visited[s] = False

for i in range(n):
    dfs(i, 1)
print(0)