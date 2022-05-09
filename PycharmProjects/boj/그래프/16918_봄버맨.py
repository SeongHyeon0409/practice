# 2020.04.26
# Presented by SeongHyeon0409
import sys
sys.setrecursionlimit(99999)

r, c, n = map(int, input().split())

map = [list(input()) for i in range(r)]

for i in range(r):
    for j in range(c):
        if map[i][j] == 'O':
            map[i][j] = 1

# 폭탄 3초가 지난 후 폭발 > 인접한 네칸 파괴(폭탄이 있던 칸도 파괴)
# 1초 후 아무것도 x
# 1초 후 폭탄 이 설치되어 있지 않은 칸에 폭탄 설치
# 3, 4 반복

def printm(map):
    for i in map:
        print("".join(i))

def boom(j, k):
    map[j][k] = '.'
    if j > 0:
        if map[j-1][k] == 2:
            boom(j-1, k)
        map[j - 1][k] = '.'
    if j < r-1:
        if map[j+1][k] == 2:
            boom(j+1, k)
        map[j + 1][k] = '.'
    if k > 0:
        if map[j][k-1] == 2:
            boom(j, k-1)
        map[j][k - 1] = '.'
    if k < c-1:
        if map[j][k+1] == 2:
            boom(j, k+1)
        map[j][k + 1] = '.'

for i in range(1, n):
    for j in range(r):
        for k in range(c):
            if map[j][k] != '.':
                map[j][k] += 1

            if map[j][k] == 3:
                boom(j, k)

            if i % 2 == 1:
                if map[j][k] == '.':
                    map[j][k] = 0

for i in range(r):
    for j in range(c):
        if map[i][j] != '.':
            map[i][j] = 'O'

printm(map)