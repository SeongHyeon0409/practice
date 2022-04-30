#2020.04.30
#Presented by SeongHyeon0409
#분할정복, 재귀

n = int(input())
a = [list(input()) for _ in range(n)]
ans = ''

def b(x, y, n):
    global ans
    temp = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[i][j] != temp:
                ans += '('
                b(x, y, n // 2)
                b(x, y + n//2, n // 2)
                b(x + n//2, y, n // 2)
                b(x + n//2, y + n//2, n // 2)
                ans += ')'
                return

    if temp == '0':
        ans += '0'
    else:
        ans += '1'

b(0, 0, n)
print(ans)