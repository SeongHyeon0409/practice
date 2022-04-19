# 2020.04.19
# Presented by SeongHyeon0409
# 분할정복, 재귀

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m1 = 0
ze = 0
p1 = 0

def b(x, y, n):
    global m1, ze, p1
    temp = a[x][y]
    xm = [0, n // 3, n // 3 * 2]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[i][j] != temp:
                for k in range(3):
                    for l in range(3):
                        b(x + xm[l], y + xm[k], n//3)
                return

    if temp == -1:
        m1 += 1
    elif temp == 0:
        ze += 1
    else:
        p1 += 1

b(0, 0, n)
print(m1, ze, p1, sep='\n')