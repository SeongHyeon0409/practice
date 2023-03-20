# 2023.03.20
# Written by SeongHyeon0409

import copy
def printm(m):
    for i in m:
        print(*i)

r, c = map(int, input().split())

maps = []
ans = 0

dx = [1, 1, 1]
dy = [-1, 0, 1]

for i in range(r):
    maps.append(list(input().strip()))

for i in range(r):
    cy, cx = i, 0
    flag = True
    mapl = []

    while cx != c-1:
        flag1 = False
        for j in range(3):
            ny, nx = cy + dy[j], cx + dx[j]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == '.':
                mapl.append([ny, nx])
                cy, cx = ny, nx
                flag1 = True
                break

        if flag1:
            continue

        flag = False
        break

    if flag:
        for _ in mapl:
            maps[_[0]][_[1]] = 'x'
        ans += 1

print(ans)