import sys
sys.setrecursionlimit(999999)

sdk = [list(map(int, input().split())) for i in range(9)]

def row(y, x, n):
    for i in range(9):
        if sdk[y][i] == n:
            return False
    return True

def colom(y, x, n):
    for i in range(9):
        if sdk[i][x] == n:
            return False

    return True

def thr(y, x, n):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(y, y+3):
        for j in range(x, x+3):
            if sdk[i][j] == n:
                return False

    return True

def dfs(c):
    if c == len(cnt):
        for i in sdk:
            print(*i)
        exit()


    for i in range(1, 10):
        y = cnt[c][0]
        x = cnt[c][1]
        if row(y, x, i) and colom(y, x, i) and thr(y, x, i):
            sdk[y][x] = i
            dfs(c+1)
            sdk[y][x] = 0



cnt = []
# 0의 개수
# 0의 개수를 모두 사용할때 까지 반복
for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            cnt.append([i, j])

dfs(0)