from collections import deque
dy = [0, 0, -1, -1, -1, 1, 1, 1, 0]
dx = [-1, 1, -1, 0, 1, -1, 0, 1, 0]
maps = deque(list(input()) for i in range(8))
visited = [[0] * 8 for i in range(8)]

q = deque()
q.append((7, 0))
visited[7][0] = 0

while q:
    lq = len(q)
    t = 0
    for _ in range(lq):
        y, x = q.popleft()
        if y == 0 and x == 7:
            print(1)
            exit()

        if maps[y][x] == '#':
            continue

        for i in range(9):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
                continue

            if maps[ny][nx] == '.' :
                q.append((ny, nx))
                visited[ny][nx] = 1

    maps.pop()
    maps.appendleft(list('........'))

    t += 1

    if t > 8:
        print(1)
        exit()



print(0)