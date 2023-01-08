# 2023. 01. 08
# Written by SeongHyeon0409

from collections import deque
import copy

def printmap(m):
    for i in m:
        print(*i)

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    answer = 0
    m = [list(input()) for _ in range(h)]
    # if 상근이가 w, h보다 커지면 break
    # 불의 범위가 1칸씩 먼저 넓어짐
    # 상근이 이동 불가 break
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    flag = 0
    answy, answx = -1, -1
    while flag == 0:
        answer += 1
        mcopy = copy.deepcopy(m)
        flag = 1
        for y in range(h):
            for x in range(w):
                if m[y][x] == '.':
                    for i in range(4):
                        ny, nx = dy[i] + y, dx[i] + x
                        if 0 <= nx < w and 0 <= ny < h:
                            if m[ny][nx] == '*':
                                mcopy[y][x] = '*'
                            elif m[ny][nx] == '@' and mcopy[y][x] == '.':
                                mcopy[y][x] = '@'
                                answy, answx = y, x
                                flag = 0
        m =copy.deepcopy(mcopy)

    if answy + 1 == h or answy == 0 or answx + 1== w or answx == 0:
        print(answer)
    else:
        print('IMPOSSTIBLE')




