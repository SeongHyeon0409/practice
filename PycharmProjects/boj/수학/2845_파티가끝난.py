# 2020.04.21
# Presented by SeongHyeon0409

l, p = map(int, input().split())
n = list(map(int, input().split()))

for i in n:
    print(i - l*p, end= ' ')