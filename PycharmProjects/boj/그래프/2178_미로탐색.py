# 2020.05.02
# Presented by SeongHyeon0409

from collections import deque

n, m = map(int, input().split())
map = [ list(map(int, input())) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
que = deque()
que.append([0, 0])

while que:
    x, y = que[0][0], que[0][1]
    que.popleft()

    for i in range(4):
        nx ,ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and map[ny][nx] == 1:
            map[ny][nx] = map[y][x] + 1
            que.append([nx, ny])

print(map[n-1][m-1])


