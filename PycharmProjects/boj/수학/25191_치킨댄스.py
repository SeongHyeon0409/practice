# 2020.07.16
# Written by SeongHyeon0409

n = int(input())
a, b = map(int, input().split())

a = a//2

ans = n - a - b

if ans < 0:
    ans = n
else:
    ans = n - ans

print(ans)