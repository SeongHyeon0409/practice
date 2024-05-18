from collections import deque

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(y, x):

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if maps[ny][nx] + visited[y][x] < visited[ny][nx]:
                visited[ny][nx] = maps[ny][nx] + visited[y][x]
                dfs(ny ,nx)

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if maps[ny][nx] + visited[y][x] < visited[ny][nx]:
                    visited[ny][nx] = maps[ny][nx] + visited[y][x]
                    q.append((ny, nx))

t = int(input())
for tc in range(t):
    n = int(input())
    maps = [list(map(int, list(input()))) for i in range(n)]
    visited = [[float('inf')] * n for i in range(n)]
    visited[0][0] = 0
    bfs(0, 0)
    print(f'#{tc+1} {visited[n-1][n-1]}')

    # 더 낮으면 갱신

