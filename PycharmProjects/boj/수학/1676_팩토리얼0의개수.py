# 2020.04.19
# Presented by SeongHyeon0409

import math

n = int(input())
facto = math.factorial(n)
ans = 0

while facto % 10 == 0:
    facto //= 10
    ans += 1

print(ans)