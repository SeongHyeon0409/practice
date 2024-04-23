from collections import deque
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
m, n = map(int, input().split())

maps = [list(map(int, input())) for i in range(n)]
visited = [[0] * m for i in range(n)]
visited[0][0] = 1
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    if x == m-1 and y == n-1:
        print(maps[n-1][m-1])
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
            if maps[ny][nx] == 0:
                q.appendleft((nx, ny))
                maps[ny][nx] = maps[y][x]
                visited[ny][nx] = 1
            else:
                q.append((nx, ny))
                maps[ny][nx] = maps[y][x] + 1
                visited[ny][nx] = 1



