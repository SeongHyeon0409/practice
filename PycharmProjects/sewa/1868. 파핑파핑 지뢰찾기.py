from collections import deque

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def dfs(y, x):
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            trap = check8(ny, nx)
            if visited[ny][nx] == -1 and maps[ny][nx] == '.':
                visited[ny][nx] = trap
                if trap == 0:
                    dfs(ny, nx)
def check8(y, x):
    tmp = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[ny][nx] == '*':
                tmp += 1
    return tmp

t = int(input())
for _ in range(1, t+1):
    n = int(input())
    maps = [list(input()) for i in range(n)]
    visited = [[-1] * n for i in range(n)]

    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.':
                if check8(i, j) == 0:
                    q.appendleft((i, j))

    ans = 0

    while q:
        y, x = q.popleft()
        if visited[y][x] == -1:
            ans += 1
            visited[y][x] = 0
            dfs(y, x)

    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.' and visited[i][j] == -1:
                ans += 1

    print(f'#{_} {ans}')

