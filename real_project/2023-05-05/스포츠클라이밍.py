from collections import deque
import sys

input = sys.stdin.readline

def printm(m):
    for i in m:
        print(*i)

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n = int(input())
    maps = [list(input().split()) for _ in range(n)]
    distance = [[0] * n for _ in range(n)
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 'H':
                distance[i][j] = float('inf')

    distance[n-1][0] = 1

    q = deque()

    start = (n-1, 0)
    q.append(start)

    while q:
        coor = q.popleft()
        y, x = coor[0], coor[1]
        count = distance[y][x]
        #print(coor, count)
        #1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if -1 < ny < n and -1 < nx < n:
                if maps[ny][nx] == 'H':
                    if count + 1 < distance[ny][nx]:
                        distance[ny][nx] = count + 1
                        q.append((ny, nx))
        #2
        dx2 = [-2, 2, -3, 3]
        if y > 0:
            flag = 0
            if -1 < x-2 < n and maps[y][x-2] == 'H':
                if maps[y][x-1] == '.':
                    flag = 2
                    for i in range(-2, 1):
                        if maps[y-1][x+i] != '.':
                            flag = 1
                            break
            if flag == 2 and -1 < x - 2 < n:
                if count + 1 < distance[y][x-2]:
                    distance[y][x-2] = count + 1
                    q.append((y, x-2))

            flag = 0
            if -1 < x-3 < n and maps[y][x-3] == 'H':
                if maps[y][x-1] == '.' and maps[y][x-2] == '.':
                    flag = 2
                    for i in range(-3, 1):
                        if maps[y - 1][x + i] != '.':
                            flag = 1
                            break
                if flag == 2 and -1 < x - 3 < n:
                    if count + 1 < distance[y][x - 3]:
                        distance[y][x - 3] = count + 1
                        q.append((y, x - 3))
            flag = 0
            if -1 < x + 2 < n and maps[y][x + 2] == 'H':
                if maps[y][x + 1] == '.':
                    flag = 2
                    for i in range(0, 3):
                        if maps[y - 1][x + i] != '.':
                            flag = 1
                            break
                if flag == 2 and -1 < x + 2 < n:
                    if count + 1 < distance[y][x + 2]:
                        distance[y][x + 2] = count + 1

                        q.append((y, x + 2))

            flag = 0
            if -1 < x + 3  < n and maps[y][x + 3] == 'H':
                if maps[y][x + 1] == '.' and maps[y][x + 2] == '.':
                    flag = 2
                    for i in range(0, 4):
                        if maps[y - 1][x + i] != '.':
                            flag = 1
                            break

                if flag == 2 and -1 < x + 3 < n:
                    if count + 1 < distance[y][x + 3]:
                        distance[y][x + 3] = count + 1
                        q.append((y, x + 3))

            #3
            if y - 2 > -1 and maps[y-1][x] == '.' and maps[y-2][x] == 'H':
                if count + 1 < distance[y - 2][x]:
                    distance[y - 2][x] = count + 1
                    q.append((y - 2, x))

            #4
            if x > 0 and y > 0:
                if maps[y][x-1] == '.' and maps[y-1][x] == '.' and maps[y-1][x-1] == 'H':
                    if count + 1 < distance[y - 1][x - 1]:
                        distance[y - 1][x - 1] = count + 1
                        q.append((y - 1, x - 1))

            if x < n-1 and y > 0:
                if maps[y][x + 1] == '.' and maps[y - 1][x] == '.' and maps[y - 1][x + 1] == 'H':
                    if count + 1 < distance[y - 1][x + 1]:
                        distance[y - 1][x + 1] = count + 1
                        q.append((y - 1, x + 1))


    for i in range(n):
        for j in range(n):

            if distance[i][j] == float('inf'):
                distance[i][j] = -1
    printm(distance)