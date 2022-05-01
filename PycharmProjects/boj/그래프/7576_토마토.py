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

    # dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # for i in range(4):
    #     nx, ny = dx[i] + x, dy[i] + y
    #     # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
    #     if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
    #         # 익히고 1을 더해주면서 횟수를 세어주기
    #         # 여기서 나온 제일 큰 값이 정답이 될 것임
    #         matrix[nx][ny] = matrix[x][y] + 1

    if temp:
        que.append(temp)

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            ans = -1
            break

print(ans)

