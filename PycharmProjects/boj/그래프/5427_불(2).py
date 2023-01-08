# 2023. 01. 08
# Written by SeongHyeon0409

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def printmap(m):
    for i in m:
        print(*i)

def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != '#' and maps[nx][ny] != '*':
                    maps[nx][ny] = '*'
                    fire.append((nx, ny))

def move():
    end = False
    for _ in range(len(start)):
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] != '#' and maps[nx][ny] != '*':
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
                    end = True
            else:
                return visited[x][y]
    if end == False:
        return('IMPOSSIBLE')

t = int(input())

for _ in range(t):
    m, n = map(int, input().strip().split())
    answer = 0
    maps = [list(input().strip()) for _ in range(n)]
    # if 상근이가 w, h보다 커지면 break
    # 불의 범위가 1칸씩 먼저 넓어짐
    # 상근이 이동 불가 break

    fire = deque()
    start = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '*':
                fire.append((i, j))
            if maps[i][j] == '@':
                start.append((i, j))
    visited = [[0] * m for _ in range(n)]
    visited[start[0][0]][start[0][1]] = 1

    while True:
        burn()
        answer = move()
        if answer:
            break

    print(answer)





