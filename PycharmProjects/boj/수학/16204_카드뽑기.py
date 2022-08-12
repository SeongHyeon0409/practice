# 2020.07.05
# Written by SeongHyeon0409

n, m, k = map(int, input().split())

print(min((n-(n-m)), (n-(n-k))) + min((n-m), (n-k)))