import sys
from collections import deque
#sys.stdin = open("../input.txt", "r")

input = sys.stdin.readline
n, m = map(int, input().split())
maps = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
visited = [[False] * m for _ in range(n)]
maps = []
distance = [[-1] * m for _ in range(n)]

for i in range(n):
    p = list(map(int, input().split()))
    maps.append(p)
    for j in range(m):
        if p[j] == 2:
            start = (i, j)
            queue.append(start)
            visited[i][j] = True
            distance[i][j] = 0
        if maps[i][j] == 0:
           distance[i][j] = 0

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 1:
            distance[ny][nx] = distance[y][x] + 1
            queue.append((ny, nx))
            visited[ny][nx] = True

for i in range(n):
    print(*distance[i])




