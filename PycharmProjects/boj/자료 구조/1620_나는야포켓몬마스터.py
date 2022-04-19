# 2020.04.19
# Presented by SeongHyeon0409
# 해시

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

pocket = {}

for i in range(1, n+1):
    name = input().strip()
    pocket[i] = name
    pocket[name] = i

for i in range(m):
    ques = input().strip()
    if ord(ques[0]) >= 65:
        print(pocket[ques])
    else:
        print(pocket[int(ques)])