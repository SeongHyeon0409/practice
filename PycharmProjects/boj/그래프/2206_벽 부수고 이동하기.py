from collections import deque

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())
maps = [list(map(int, list(input()))) for _ in range(n)]

# 벽 부쉇을때 안부섰을때 visited를 따로?
visited = [[[0] * m for _ in range(n)] for i in range(2)]
visited[0][0][0] = 1

q = deque()
q.append((0, 0, 0))

while q:
    y, x, w = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if w == 0:
                if maps[ny][nx] == 0 and visited[0][ny][nx] == 0:
                    q.append((ny, nx, 0))
                    visited[0][ny][nx] += visited[0][y][x] + 1
                if maps[ny][nx] == 1 and visited[1][ny][nx] == 0:
                    q.appendleft((ny, nx, 1))
                    visited[1][ny][nx] += visited[0][y][x] + 1

            if w == 1:
                if maps[ny][nx] == 0 and visited[1][ny][nx] == 0:
                    q.append((ny, nx, 1))
                    visited[1][ny][nx] += visited[1][y][x] + 1

ans1 = visited[0][n-1][m-1]
ans2 = visited[1][n-1][m-1]
if ans1 == ans2 == 0 :
    print(-1)
elif ans1 != 0 and ans2 != 0 :
    print(min(ans1, ans2))
elif ans1 == 0:
    print(ans2)
elif ans2 == 0:
    print(ans1)
