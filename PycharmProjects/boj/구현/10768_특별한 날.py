# 2020.06.21
# Written by SeongHyeon0409

m = int(input())
d = int(input())

ans = ''

if m < 2:
    ans = 'Before'
elif m == 2:
    if d < 18:
        ans = 'Before'
    elif d == 18:
        ans = 'Special'
    elif d > 18:
        ans = 'After'
else:
    ans = 'After'

print(ans)