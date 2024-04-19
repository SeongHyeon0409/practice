from collections import deque
#거리가 1인경우 제외
#bfs
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]


ans = float('inf')
color = 2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = color
            q = deque()
            q.append((i,j))
            while q:
                y, x = q.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < n and 0 <= nx < n:
                        if maps[ny][nx] == 1:
                            maps[ny][nx] = color
                            q.append((ny, nx))
            color += 1

# 만나기만 하면 종료시키면됨.

def bfs():
    global ans
    q = deque()
    color = maps[i][j]
    q.append([i, j, 0])
    while q:
        y, x, c = q.popleft()
        if maps[y][x] != color and maps[y][x] != 0:
            ans = min(ans, c)
            return
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] != color and visited[ny][nx] == 0:
                q.append([ny, nx, c + 1])
                visited[ny][nx] = 1


for i in range(n):
    for j in range(n):
        visited = [[0] * n for _ in range(n)]
        if maps[i][j] != 0:
            bfs()

print(ans-1)