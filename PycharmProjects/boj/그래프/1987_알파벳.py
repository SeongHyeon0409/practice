dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
r, c = map(int, input().split())
maps = [input() for i in range(r)]
visited = [0] * 26
visited[ord(maps[0][0])-65] = 1
ans = 0

def dfs(y, x, d):
    global ans
    ans = max(ans, d)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if maps[ny][nx] and visited[ord(maps[ny][nx])-65] == 0:
                visited[ord(maps[ny][nx])-65] = 1
                dfs(ny, nx, d+1)
                visited[ord(maps[ny][nx])-65] = 0


dfs(0, 0, 1)
print(ans)