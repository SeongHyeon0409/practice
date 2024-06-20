def pl(maps):
    for i in maps:
        print(*i)

r, c = map(int, input().split())
maps = [['.'] * (c+2)]
for i in range(r):
    temp = ['.']
    temp.extend(list(input()))
    temp.extend(['.'])
    maps.append(temp)

maps.append(['.'] * (c+2))

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
cmap = [[0] * (c+2) for i in range(r+2)]

for i in range(1, r+1):
    for j in range(1, c+1):
        if maps[i][j] == 'X':
            for k in range(4):
                y, x = i + dy[k], j + dx[k]
                if maps[y][x] == '.':
                    cmap[i][j] += 1

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if cmap[i][j] >= 3:
            maps[i][j] = '.'

maxx, maxy, minx, miny = 0, 0, c, r

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if maps[i][j] == 'X':
            maxx = max(maxx, j)
            minx = min(minx, j)
            maxy = max(maxy, i)
            miny = min(miny, i)


for i in range(miny, maxy + 1):
    for j in range(minx, maxx + 1):
        print(maps[i][j], end='')
    print()

