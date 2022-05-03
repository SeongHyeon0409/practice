# 2020.05.03
# Presented by SeongHyeon0409
import sys, copy
sys.setrecursionlimit(99999)

n = int(input())

map = [list(input()) for _ in range(n)]
rgmap = copy.deepcopy(map)

def printm(map):
    for i in range(len(map)):
        print(map[i])

R, G, B, RG = 0, 0, 0, 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j, c, f):
    global R, G, B
    for k in range(4):
        nx, ny = j + dx[k], i + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if f == 1:
                if rgmap[ny][nx] == 'R' or rgmap[ny][nx] == 'G':
                    rgmap[ny][nx] = 'O'
                    bfs(ny, nx, c, 1)
            else:
                if map[ny][nx] == c:
                    map[ny][nx] = 'O'
                    bfs(ny, nx, c, f)

for i in range(n):
    for j in range(n):
        if map[i][j] == 'R':
            R += 1
            if rgmap[i][j] != 'O':
                RG += 1
            bfs(i, j, 'R', 0)
            bfs(i, j, 'R', 1)
        elif map[i][j] == 'G':
            G += 1
            if rgmap[i][j] != 'O':
                RG += 1
            bfs(i, j, 'G', 0)
            bfs(i, j, 'G', 1)
        elif map[i][j] == 'B':
            B += 1
            bfs(i, j, 'B', 0)

print(R + G + B, RG + B)