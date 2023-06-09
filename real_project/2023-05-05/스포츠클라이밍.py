from collections import deque

def printm(m):
    for i in m:
        print(*i)

t = int(input())
dx = [1, -1, 0, 0, -1, 1]
dy = [0, 0, -1, 1, -1, -1]

for _ in range(t):
    n = int(input())
    maps = [list(input().split()) for _ in range(n)]
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 'H':
                d[i][j] = float('inf')

    d[n-1][0] = 1
    q = deque()

    start = (n-1, 0)
    q.append(start)

    while q:
        pos = q.popleft()
        y, x = pos[0], pos[1]
        count = d[y][x]

        #1, 4, 5
        for i in range(6):
            ny, nx = y + dy[i], x + dx[i]
            if -1 < ny < n and -1 < nx < n:
                if i > 3:
                    if maps[ny][nx] == 'H' and maps[ny][x] == '.' and maps[y][nx] == '.':
                        if count + 1 < d[ny][nx]:
                            d[ny][nx] = count + 1
                            q.append((ny,nx))
                elif maps[ny][nx] == 'H':
                    if count + 1 < d[ny][nx]:
                        d[ny][nx] = count + 1
                        q.append((ny, nx))
        #2

        if y > 0:
            dx2 = [-3, -2, 2, 3]
            for i in range(4):
                flag = 0
                nx = x + dx2[i]
                if -1 < nx < n and maps[y][nx] == 'H':
                    a = min(x, nx) # 1,
                    b = max(x, nx)
                    for j in range(a, b+1):
                        if maps[y-1][j] != '.':
                            flag = 1
                            break
                    for j in range(a+1, b):
                        if maps[y][j] != '.':
                            flag = 1
                            break
                else:
                    continue
                if flag == 0:
                    if count + 1 < d[y][nx]:
                        d[y][nx] = count + 1
                        q.append((y, nx))

            #3
            if y - 2 > -1 and maps[y-1][x] == '.' and maps[y-2][x] == 'H':
                if count + 1 < d[y - 2][x]:
                    d[y - 2][x] = count + 1
                    q.append((y - 2, x))

    for i in range(n):
        for j in range(n):
            if d[i][j] == float('inf'):
                d[i][j] = -1
    printm(d)