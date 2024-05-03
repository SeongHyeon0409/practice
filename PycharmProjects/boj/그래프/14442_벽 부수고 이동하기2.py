from collections import deque
import sys

input = sys.stdin.readline

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m, k = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1

q = deque()
q.append((0, 0, k))

while q:
    y, x, w = q.popleft()
    if y == n-1 and x == m-1:
        print(visited[y][x][w])
        exit()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if maps[ny][nx] == 0 and visited[ny][nx][w] == 0:
            q.append((ny, nx, w))
            visited[ny][nx][w] = visited[y][x][w] + 1
        elif w > 0 and maps[ny][nx] == 1 and visited[ny][nx][w - 1] == 0:
            q.append((ny, nx, w-1))
            visited[ny][nx][w-1] = visited[y][x][w] + 1

print(-1)