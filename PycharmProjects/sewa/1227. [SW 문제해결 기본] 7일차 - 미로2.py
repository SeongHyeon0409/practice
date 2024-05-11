from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(y, x):
    global ans
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        if maps[y][x] == 3:
            ans = 1
            return

        for i in range(4):
            nx, ny = x + dx[i], y +dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == 0 and maps[ny][nx] != 1:
                    visited[ny][nx] = 1
                    q.append((ny, nx))


for tc in range(1, 11):
    t = input()
    n = 100
    maps = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                bfs(i, j)
                break

    print(f'#{tc} {ans}')