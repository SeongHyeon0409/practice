#분할정복, 재귀

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def b(x, y, n):
    global white, blue
    temp = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[i][j] != temp:
                b(x, y, n // 2)
                b(x + n//2, y, n // 2)
                b(x + n//2, y + n//2, n // 2)
                b(x, y + n//2, n // 2)
                return

    if temp == 0:
        white += 1
    else:
        blue += 1

b(0, 0, n)
print(white, blue, sep='\n')