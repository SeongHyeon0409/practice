h, m = map(int, input().split())
a = int(input())

if m + a < 60:
    m += a
else:
    m += a
    while m >= 60:
        h += 1
        if h > 23:
            h = 0
        m -= 60


print(h, m)