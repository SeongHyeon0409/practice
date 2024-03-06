import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
maps = []
visited = [[False]*m for _ in range(n)]
answer = 0

for i in range(n):
    temp = input()
    if 'I' in temp:
        start = (i, temp.index('I'))
    maps.append(temp)

def dfs(y, x):
    global answer

    if maps[y][x] == 'P':
        answer += 1

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(ny, nx)


dfs(start[0], start[1])
if answer == 0:
    answer = 'TT'
print(answer)

