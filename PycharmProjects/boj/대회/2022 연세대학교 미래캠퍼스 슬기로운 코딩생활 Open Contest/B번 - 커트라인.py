# 2020.06.25
# Written by SeongHyeon0409

n, k = map(int, input().split())

s = sorted(list(map(int, input().split())), reverse=True)

print(s[k-1])

