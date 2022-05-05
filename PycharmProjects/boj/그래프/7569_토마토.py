# 2020.05.01
# Presented by SeongHyeon0409
from collections import deque


def printm(map):
    for i in map:
        print(*i)


m, n, h = map(int, input().split())
map = [[list(map(int, input().split())) for _ in range(n)] for k in range(h)]


que = deque()
temp = []
ans = -1

for k in range(h):
    for i in range(n):
        for j in range(m):
            if map[k][i][j] == 1:
                temp.append([k, i, j])

que.append(temp)

dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], \
             [0, 0, 0, 0, -1, 1]

while que:
    ans += 1
    xy = que.popleft()
    temp = deque()
    for k in xy:
        l, i, j = k[0], k[1], k[2]
        for o in range(6):
            nh, ny, nx = dh[o] + l, dy[o] + i, dx[o] + j
            if 0 <= nh < h and 0 <= ny < n and 0 <= nx < m and map[nh][ny][nx] == 0:
                map[nh][ny][nx] = 1
                temp.append([nh, ny, nx])

    # 이게 속도 더 잘 나옴
    # for k in xy:
    #     l, i, j = k[0], k[1], k[2]
    #     if j > 0 and map[l][i][j - 1] == 0:
    #         map[l][i][j - 1] = 1
    #         temp.append([l, i, j - 1])
    #     if j < m - 1 and map[l][i][j + 1] == 0:
    #         map[l][i][j + 1] = 1
    #         temp.append([l, i, j + 1])
    #     if i > 0 and map[l][i - 1][j] == 0:
    #         map[l][i - 1][j] = 1
    #         temp.append([l, i - 1, j])
    #     if i < n - 1 and map[l][i + 1][j] == 0:
    #         map[l][i + 1][j] = 1
    #         temp.append([l, i + 1, j])
    #     if l > 0 and map[l - 1][i][j] == 0:
    #         map[l - 1][i][j] = 1
    #         temp.append([l - 1, i, j])
    #     if l < h - 1 and map[l + 1][i][j] == 0:
    #         map[l + 1][i][j] = 1
    #         temp.append([l + 1, i, j])

    if temp:
        que.append(temp)

for k in range(h):
    for i in range(n):
        for j in range(m):
            if map[k][i][j] == 0:
                ans = -1
                break

print(ans)

