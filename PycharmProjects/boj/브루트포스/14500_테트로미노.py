# 2020.05.07
# Presented by SeongHyeon0409

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

ans = 0

dx = [0, 1, 2, 0, 1, 2, -1, 3]
dy = [-1, -1, -1, 1, 1, 1, 0, 0]

for i in range(n):
    for j in range(m-2):
        temp = map[i][j] + map[i][j+1] + map[i][j+2]
        for k in range(8):
            nx, ny = j + dx[k], i + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                ans = max(ans, temp + map[ny][nx])

for i in range(m):
    for j in range(n-2):
        temp = map[j][i] + map[j+1][i] + map[j+2][i]
        for k in range(8):
            nx, ny = i + dy[k], j + dx[k]
            if 0 <= nx < m and 0 <= ny < n:
                ans = max(ans, temp + map[ny][nx])

for i in range(n):
    for j in range(m-1):
        temp = map[i][j] + map[i][j+1]
        if j > 0 and i < n-1:
            ans = max(ans, temp + map[i+1][j] + map[i+1][j-1])
        if j > 0 and i > 0:
            ans = max(ans, temp + map[i-1][j] + map[i-1][j-1])
        if i < n-1:
            ans = max(ans, temp + map[i+1][j] + map[i+1][j+1])

for i in range(m):
    for j in range(n-1):
        temp = map[j][i] + map[j+1][i]
        if j > 0 and i < m-1:
            ans = max(ans, temp + map[j][i+1] + map[j-1][i+1])
        if j > 0 and i > 0:
            ans = max(ans, temp + map[j][i-1] + map[j-1][i-1])

print(ans)
