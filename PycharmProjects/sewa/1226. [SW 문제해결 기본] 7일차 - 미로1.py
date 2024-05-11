dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(y, x):
    global tc, ans
    if maps[y][x] == 3:
        ans = 1
        return

    for i in range(4):
        nx, ny = x + dx[i], y +dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[ny][nx] == 0 and maps[ny][nx] != 1:
                visited[ny][nx] = 1
                dfs(ny, nx)


for tc in range(1, 11):
    t = input()
    n = 100
    maps = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                dfs(i, j)
                break

    print(f'#{tc} {ans}')