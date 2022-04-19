# 2020.04.19
# Presented by SeongHyeon0409

import sys

input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    cloth = dict()
    for j in range(n):
        cl, name = input().strip().split()
        if name not in cloth:
            cloth[name] = 1
        else:
            cloth[name] += 1

    ans = 1

    for j in cloth.values():
        ans *= j + 1

    print(ans-1)

