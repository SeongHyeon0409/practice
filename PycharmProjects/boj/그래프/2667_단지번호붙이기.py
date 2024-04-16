# 2020.04.11
# Presented by SeongHyeon0409

n = int(input())

map = [ list(map(int, input())) for _ in range(n)]

def dsf(i, j, label):
    global count
    if map[i][j] == 1:
        map[i][j] = label
        count += 1
        if j < n-1:
            dsf(i, j+1, label)
        if i > 0:
            dsf(i-1, j, label)
        if j > 0:
            dsf(i, j-1, label)
        if i < n-1:
            dsf(i+1, j, label)
    return count

label = 2
ans = []

for i in range(n):
    for j in range(n):
        count = 0
        if map[i][j] == 1:
            dsf(i, j, label)
            ans.append(count)
            label += 1

print(label-2)
print(*sorted(ans), sep='\n')

#------------

n = int(input())
maps = [input() for i in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(y, x):
    global tmp
    visited[y][x] = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if maps[ny][nx] == '1' and visited[ny][nx] == 0:
                tmp += 1
                dfs(ny, nx)

ans = []
tmp = 1
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1' and visited[i][j] == 0:
            dfs(i, j)
            ans.append(tmp)
            tmp = 1

ans.sort()
print(len(ans))
for an in ans:
    print(an)



