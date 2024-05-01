from collections import deque
import sys

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dy, dx = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
visited = [[0] * n for i in range(n)]

q = deque()
q.append((r1, c1))

while q:
    y, x = q.popleft()
    if y == r2 and x == c2:
        print(visited[r2][c2])
        exit()

    for i in range(6):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx <n:
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] +1
                q.append((ny, nx))


print(-1)