from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1, -1, 1, -1, 1]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]


while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().strip().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    maps[y][x] = 0
                    for d in range(8):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] == 1:
                            q.append((ny, nx))
                            maps[ny][nx] = 0
                ans += 1

    print(ans)




