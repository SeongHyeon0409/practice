# 2020.05.01
# Presented by SeongHyeon0409
from collections import deque

def printm(map):
    for i in map:
        print(*i)

m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

que = deque()
temp = []
ans = -1

for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            temp.append([i, j])

que.append(temp)

while que:
    ans += 1
    xy = que.popleft()
    temp = []
    for k in xy:
        i, j = k[0], k[1]
        if j > 0 and map[i][j-1] == 0:
            map[i][j-1] = 1
            temp.append([i, j-1])
        if j < m-1 and map[i][j+1] == 0:
            map[i][j+1] = 1
            temp.append([i, j+1])
        if i > 0 and map[i-1][j] == 0:
            map[i-1][j] = 1
            temp.append([i-1, j])
        if i < n-1 and map[i+1][j] == 0:
            map[i+1][j] = 1
            temp.append([i+1, j])
    if temp:
        que.append(temp)

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            ans = -1
            break

print(ans)

