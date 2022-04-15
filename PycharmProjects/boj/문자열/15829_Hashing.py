# 2020.04.14
# Presented by SeongHyeon0409

n = int(input())
h = input()
r = 31
mod = 1234567891

ans = 0
a = 0

for i in h:
    ans += (ord(i)-96) * (r ** a)
    ans %= mod
    a += 1

print(ans)
