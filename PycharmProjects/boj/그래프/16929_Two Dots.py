import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [input() for _ in range(n)]
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

visited = [[0] * m for _ in range(n)]

def dfs(w, y, x, d):
    global start
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if maps[ny][nx] != w:
            continue

        if ny == start[0] and nx == start[1] and d+1 > 3:
            print("Yes")
            sys.exit()

        if visited[ny][nx] != 0:
            continue

        visited[ny][nx] = 1
        dfs(w, ny, nx, d+1)
        visited[ny][nx] = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            start = (i, j)
            visited[i][j] = 1
            dfs(maps[i][j], i, j, 0)

print("No")