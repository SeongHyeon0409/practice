from collections import deque
import copy

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * m for i in range(n)]
ans = 0
cnt = 0

def bfs(map):
    q = deque()

    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 0:
                    map[ny][nx] = 2
                    q.append((ny, nx))



def dfs(wall):
    global ans

    if wall == 3:
        cnt = 0
        nmap = copy.deepcopy(maps)
        bfs(nmap)
        for i in range(n):
            for j in range(m):
                if nmap[i][j] == 0:
                    cnt += 1

        ans = max(cnt, ans)
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                dfs(wall + 1)
                maps[i][j] = 0


dfs(0)
print(ans)

