import sys
sys.setrecursionlimit(99999)

t = int(input())
def printc(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            print(c[i][j], end= " ")
        print()

def dfs(c, y, x):
    c[y][x] = 0
    if x+1<len(c[0]):
        if c[y][x+1] == 1:
            c[y][x+1] = 0
            dfs(c, y, x+1)
    if y+1<len(c):
        if c[y+1][x] == 1:
            c[y+1][x] = 0
            dfs(c, y+1, x)
    if x>0:
        if c[y][x-1] == 1:
            c[y][x-1] = 0
            dfs(c, y, x-1)
    if y>0:
        if c[y-1][x] == 1:
            c[y-1][x] = 0
            dfs(c, y-1, x)
    return

for i in range(t):
    m, n, k = map(int, input().split())
    c = [[0] * m for _ in range(n)]
    answer = 0
    for j in range(k):
        x, y = map(int, input().split())
        c[y][x] = 1

    for j in range(n):
        for k in range(m):
            if c[j][k] == 1:
                answer += 1
                dfs(c, j, k)


    print(answer)
    #printc(c)
    #print("-------------------")