import sys
sys.setrecursionlimit(999999)

# 좌우 우선순위
dy, dx = [0, 0, -1], [-1, 1, 0]

def dfs(y, x):
    global visited, ans
    if y == 0:
        ans[x] = visited[y][x]
        return

    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 100 and 0 <= nx < 100:
            if visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                dfs(ny, nx)
                break



for tc in range(1, 11):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]
    ans = [float('inf')] * 100
    for i in range(100):
        visited = [[0] * 100 for _ in range(100)]
        if maps[99][i] == 1:
            sy, sx = 99, i
            dfs(sy, sx)

    minv = float('inf')
    ansidx = 0
    for i in range(100):
        if ans[i] <= minv:
            ansidx = i
            minv = ans[i]

    print(f'#{tc} {ansidx}')