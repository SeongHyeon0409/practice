from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

ans = [0] * (n+1)
visited = [0] * (n+1)
visited[1] = 1

while q:
    p = q.popleft()
    for i in graph[p]:
        if visited[i] == 0:
            ans[i] = p
            q.append(i)
            visited[i] = 1

for i in range(2, n+1):
    print(ans[i])
