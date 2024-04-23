from collections import deque

s = int(input())

visited = [[-1] * (s+1) for _ in range(s+1)]
visited[1][0] = 0

def bfs():
    q = deque()
    q.append([1, 0])
    while q:
        n, clip = q.popleft()
        if visited[n][n] == -1:
            visited[n][n] = visited[n][clip] + 1
            q.append([n, n])
        if n + clip <= s and visited[n + clip][clip] == -1:
            visited[n + clip][clip] = visited[n][clip] + 1
            q.append([n+clip, clip])
        if n - 1 >= 0 and visited[n - 1][clip] == -1:
            visited[n - 1][clip] = visited[n][clip] + 1
            q.append([n - 1, clip])

#복사해놓고 나중에 붙여넣기?

bfs()
ans = float('inf')

for i in visited[s]:
    if i != -1 and ans > i:
        ans = i
print(ans)
