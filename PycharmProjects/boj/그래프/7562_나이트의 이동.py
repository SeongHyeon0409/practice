from collections import deque
import sys
input = sys.stdin.readline

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]
t = int(input())


for _ in range(t):
    n = int(input())

    sy, sx = map(int, input().split())
    fy, fx = map(int, input().split())

    maps = [[0] * n for i in range(n)]

    q = deque()
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        if x == fx and y == fy:
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 0:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))


    print(maps[fy][fx])