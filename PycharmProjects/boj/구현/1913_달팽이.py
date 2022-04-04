def lprint(l):
    for i in l:
        print(*i)

n = int(input())
m = int(input())
l = [[0]*n for _ in range(n)]

x = n//2
y = n//2
l[y][x] = 1
a = 1
b = 1
ansx, ansy = n//2, n//2

while a < (n**2)+1:
    if a > ((n**2) - n):
        for i in range(b-1):
            y -= 1
            a += 1
            l[y][x] = a

            if a == m:
                ansx, ansy = x, y

        break
    else:
        for i in range(b):
            y -= 1
            a += 1
            l[y][x] = a

            if a == m:
                ansx, ansy = x, y
    for i in range(b):
        x += 1
        a += 1
        l[y][x] = a

        if a == m:
            ansx, ansy = x, y
    b += 1
    for i in range(b):
        y += 1
        a += 1
        l[y][x] = a

        if a == m:
            ansx, ansy = x, y
    for i in range(b):
        x -= 1
        a += 1
        l[y][x] = a

        if a == m:
            ansx, ansy = x, y
    b += 1

lprint(l)
print(ansy+1, ansx+1)


