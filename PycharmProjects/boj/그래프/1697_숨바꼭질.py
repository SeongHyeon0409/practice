from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001
def bfs():
    global n, k
    q = deque()
    q.append((n, 0))
    while q:
        n, d= q.popleft()

        if n == k:
            return d

        if n - 1 >= 0 and visited[n - 1] == 0:
            q.append((n - 1, d + 1))
            visited[n-1] = 1
        if n + 1 < 100001 and visited[n + 1] == 0:
            q.append((n + 1, d + 1))
            visited[n+1] = 1
        if n * 2 < 100001 and visited[n * 2] == 0:
            q.append((n * 2, d + 1))
            visited[n*2] = 1

print(bfs())